"""CronixUI Form Components.

Generates HTML for form inputs, textareas, checkboxes, radios, selects, sliders,
file inputs, and form field wrappers.
No browser DOM APIs are used - all output is HTML strings or data structures.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class FormElement:
    """Represents a rendered form element."""

    tag: str = "div"
    classes: list[str] = field(default_factory=list)
    attributes: dict[str, str] = field(default_factory=dict)
    inner_html: str = ""

    def render_html(self) -> str:
        """Render as HTML string.

        Returns:
            Complete HTML for the form element
        """
        class_str = " ".join(self.classes)
        class_attr = f' class="{class_str}"' if class_str else ""
        attrs_str = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        return f"<{self.tag}{class_attr}{attrs_str}>{self.inner_html}</{self.tag}>"

    def render(self) -> FormElement:
        """Return self for API compatibility."""
        return self


class Input:
    """Input component for text and other input types.

    Args:
        placeholder: Placeholder text
        size: Input size - sm, md, lg (default: md)
        error: Whether input has an error state (default: False)
        disabled: Whether input is disabled (default: False)
        icon: Optional SVG icon markup
        name: Optional input name attribute
        value: Optional initial value
        input_type: HTML input type (text, email, password, etc.) (default: text)

    Example:
        >>> inp = Input(placeholder="Enter your name", size="lg")
        >>> print(inp.render_html())
        <input class="cn-input cn-input-lg" placeholder="Enter your name" />

        >>> with_icon = Input(placeholder="Search...", icon="<svg>...</svg>")
        >>> print(with_icon.render_html())
        <div class="cn-input-icon-wrapper">
            <span class="cn-input-icon">...</span>
            <input class="cn-input" placeholder="Search..." />
        </div>
    """

    SIZES = ("sm", "md", "lg")

    def __init__(
        self,
        placeholder: str = "",
        size: str = "md",
        error: bool = False,
        disabled: bool = False,
        icon: str | None = None,
        name: str | None = None,
        value: str | None = None,
        input_type: str = "text",
    ):
        if size not in self.SIZES:
            raise ValueError(f"Invalid size '{size}'. Must be one of {self.SIZES}")

        self.placeholder = placeholder
        self.size = size
        self.error = error
        self.disabled = disabled
        self.icon = icon
        self.name = name
        self.value = value
        self.input_type = input_type

    def render(self) -> FormElement:
        """Render the input as a FormElement.

        Returns:
            FormElement representing the input
        """
        classes = ["cn-input"]
        if self.size != "md":
            classes.append(f"cn-input-{self.size}")
        if self.error:
            classes.append("cn-input-error")

        attrs: dict[str, str] = {
            "type": self.input_type,
            "placeholder": self.placeholder,
        }
        if self.name is not None:
            attrs["name"] = self.name
        if self.value is not None:
            attrs["value"] = self.value
        if self.disabled:
            attrs["disabled"] = ""

        attrs_str = "".join(f' {k}="{v}"' for k, v in attrs.items())
        inner = f"<input{attrs_str} />"

        if self.icon:
            wrapper_classes = "cn-input-icon-wrapper"
            icon_html = f'<span class="cn-input-icon">{self.icon}</span>'
            inner = f'<div class="{wrapper_classes}">{icon_html}{inner}</div>'

        return FormElement(inner_html=inner)

    def render_html(self) -> str:
        """Render the input as an HTML string.

        Returns:
            HTML string representation of the input
        """
        return self.render().render_html()


class Textarea:
    """Textarea component for multi-line text input.

    Args:
        placeholder: Placeholder text
        rows: Number of visible rows (default: 4)
        name: Optional name attribute
        disabled: Whether textarea is disabled (default: False)

    Example:
        >>> ta = Textarea(placeholder="Write your message...", rows=6)
        >>> print(ta.render_html())
        <textarea class="cn-input cn-textarea" placeholder="Write your message..." rows="6">
        </textarea>
    """

    def __init__(
        self,
        placeholder: str = "",
        rows: int = 4,
        name: str | None = None,
        disabled: bool = False,
    ):
        if rows < 1:
            raise ValueError("rows must be at least 1")

        self.placeholder = placeholder
        self.rows = rows
        self.name = name
        self.disabled = disabled

    def render(self) -> FormElement:
        """Render the textarea as a FormElement.

        Returns:
            FormElement representing the textarea
        """
        attrs: dict[str, str] = {
            "placeholder": self.placeholder,
            "rows": str(self.rows),
        }
        if self.name is not None:
            attrs["name"] = self.name
        if self.disabled:
            attrs["disabled"] = ""

        attrs_str = "".join(f' {k}="{v}"' for k, v in attrs.items())
        inner = f'<textarea class="cn-input cn-textarea"{attrs_str}></textarea>'

        return FormElement(inner_html=inner)

    def render_html(self) -> str:
        """Render the textarea as an HTML string.

        Returns:
            HTML string representation of the textarea
        """
        return self.render().render_html()


class FormField:
    """Form field wrapper with label, error message, and help text.

    Args:
        label: Field label text
        input_component: An Input, Textarea, or any component with render_html()
        error: Optional error message text
        help_text: Optional help/description text
        required: Whether to mark the field as required (default: False)

    Example:
        >>> field = FormField(
        ...     label="Email",
        ...     input_component=Input(placeholder="you@example.com"),
        ...     help_text="We'll never share your email.",
        ... )
        >>> print(field.render_html())
        <div class="cn-form-group">
            <label class="cn-form-label">Email</label>
            <input class="cn-input" placeholder="you@example.com" />
            <span class="cn-form-help">We'll never share your email.</span>
        </div>
    """

    def __init__(
        self,
        label: str,
        input_component: Input | Textarea | Checkbox | Radio | Select | Slider | HasRenderHtml,
        error: str | None = None,
        help_text: str | None = None,
        required: bool = False,
    ):
        if not label:
            raise ValueError("label cannot be empty")

        self.label = label
        self.input = input_component
        self.error = error
        self.help_text = help_text
        self.required = required

    def render(self) -> FormElement:
        """Render the form field as a FormElement.

        Returns:
            FormElement wrapping the label, input, and optional messages
        """
        required_mark = ' <span class="cn-form-required">*</span>' if self.required else ""
        label_text = f'{self._esc(self.label)}{required_mark}'

        if hasattr(self.input, "render_html"):
            input_html = self.input.render_html()
        else:
            input_html = str(self.input)

        parts = [
            f'<label class="cn-form-label">{label_text}</label>',
            input_html,
        ]

        if self.error:
            parts.append(f'<span class="cn-form-error">{self._esc(self.error)}</span>')

        if self.help_text:
            parts.append(f'<span class="cn-form-help">{self._esc(self.help_text)}</span>')

        return FormElement(
            classes=["cn-form-group"],
            inner_html="".join(parts),
        )

    def render_html(self) -> str:
        """Render the form field as an HTML string.

        Returns:
            HTML string representation of the form field
        """
        return self.render().render_html()

    @staticmethod
    def _esc(text: str) -> str:
        """Escape HTML special characters."""
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;")
        )


class Checkbox:
    """Checkbox component with label.

    Args:
        label: Checkbox label text
        checked: Whether checkbox is initially checked (default: False)
        disabled: Whether checkbox is disabled (default: False)
        name: Optional name attribute

    Example:
        >>> cb = Checkbox("Accept terms", checked=True)
        >>> print(cb.render_html())
        <label class="cn-checkbox">
            <input type="checkbox" checked="" />
            <span class="cn-checkbox-box"></span>
            <span class="cn-checkbox-label">Accept terms</span>
        </label>
    """

    def __init__(
        self,
        label: str,
        checked: bool = False,
        disabled: bool = False,
        name: str | None = None,
    ):
        if not label:
            raise ValueError("label cannot be empty")

        self.label = label
        self.checked = checked
        self.disabled = disabled
        self.name = name

    def render(self) -> FormElement:
        """Render the checkbox as a FormElement.

        Returns:
            FormElement representing the checkbox
        """
        attrs: dict[str, str] = {"type": "checkbox"}
        if self.name is not None:
            attrs["name"] = self.name
        if self.checked:
            attrs["checked"] = ""
        if self.disabled:
            attrs["disabled"] = ""

        attrs_str = "".join(f' {k}="{v}"' for k, v in attrs.items())

        label_classes = "cn-checkbox"
        if self.disabled:
            label_classes += " disabled"

        inner = (
            f'<label class="{label_classes}">'
            f'<input{attrs_str} />'
            f'<span class="cn-checkbox-box"></span>'
            f'<span class="cn-checkbox-label">{self._esc(self.label)}</span>'
            f"</label>"
        )

        return FormElement(inner_html=inner)

    def render_html(self) -> str:
        """Render the checkbox as an HTML string.

        Returns:
            HTML string representation of the checkbox
        """
        return self.render().render_html()

    @staticmethod
    def _esc(text: str) -> str:
        """Escape HTML special characters."""
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;")
        )


class Radio:
    """Radio button group component.

    Args:
        name: Radio group name (shared name attribute)
        options: List of (value, label) tuples or plain strings
        selected: Currently selected value
        disabled: Whether entire group is disabled (default: False)

    Example:
        >>> radio = Radio("color", [("red", "Red"), ("blue", "Blue")], selected="red")
        >>> print(radio.render_html())
    """

    def __init__(
        self,
        name: str,
        options: list[tuple[str, str] | str],
        selected: str | None = None,
        disabled: bool = False,
    ):
        if not name:
            raise ValueError("name cannot be empty")
        if not options:
            raise ValueError("options cannot be empty")

        self.name = name
        self.options = options
        self.selected = selected
        self.disabled = disabled

    def render(self) -> FormElement:
        """Render the radio group as a FormElement.

        Returns:
            FormElement containing all radio options
        """
        parts = []
        for option in self.options:
            if isinstance(option, tuple):
                value, label = option
            else:
                value = label = option

            input_attrs: dict[str, str] = {
                "type": "radio",
                "name": self.name,
                "value": value,
            }
            if value == self.selected:
                input_attrs["checked"] = ""
            if self.disabled:
                input_attrs["disabled"] = ""

            attrs_str = "".join(f' {k}="{v}"' for k, v in input_attrs.items())

            parts.append(
                f'<label class="cn-radio">'
                f'<input{attrs_str} />'
                f'<span class="cn-radio-box"></span>'
                f'<span class="cn-radio-label">{self._esc(label)}</span>'
                f"</label>"
            )

        return FormElement(inner_html="".join(parts))

    def render_html(self) -> str:
        """Render the radio group as an HTML string.

        Returns:
            HTML string representation of the radio group
        """
        return self.render().render_html()

    @staticmethod
    def _esc(text: str) -> str:
        """Escape HTML special characters."""
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;")
        )


class Select:
    """Select dropdown component.

    Args:
        options: List of (value, label) tuples or plain strings
        placeholder: Optional placeholder/disabled first option
        name: Optional name attribute
        disabled: Whether select is disabled (default: False)

    Example:
        >>> sel = Select(
        ...     options=[("1", "One"), ("2", "Two")],
        ...     placeholder="Choose...",
        ... )
        >>> print(sel.render_html())
    """

    def __init__(
        self,
        options: list[tuple[str, str] | str],
        placeholder: str = "",
        name: str | None = None,
        disabled: bool = False,
    ):
        if not options:
            raise ValueError("options cannot be empty")

        self.options = options
        self.placeholder = placeholder
        self.name = name
        self.disabled = disabled

    def render(self) -> FormElement:
        """Render the select as a FormElement.

        Returns:
            FormElement representing the select dropdown
        """
        parts = []

        select_attrs: dict[str, str] = {}
        if self.name is not None:
            select_attrs["name"] = self.name
        if self.disabled:
            select_attrs["disabled"] = ""

        attrs_str = "".join(f' {k}="{v}"' for k, v in select_attrs.items())
        attrs_str = f' class="cn-select"{attrs_str}' if attrs_str else ' class="cn-select"'

        if self.placeholder:
            parts.append(
                f'<option value="" disabled selected>{self._esc(self.placeholder)}</option>'
            )

        for option in self.options:
            if isinstance(option, tuple):
                value, label = option
            else:
                value = label = option

            parts.append(f'<option value="{self._esc(value)}">{self._esc(label)}</option>')

        inner = f"<select{attrs_str}>{''.join(parts)}</select>"

        return FormElement(
            classes=["cn-select-wrapper"],
            inner_html=inner,
        )

    def render_html(self) -> str:
        """Render the select as an HTML string.

        Returns:
            HTML string representation of the select dropdown
        """
        return self.render().render_html()

    @staticmethod
    def _esc(text: str) -> str:
        """Escape HTML special characters."""
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;")
        )


class Slider:
    """Slider (range input) component.

    Args:
        min: Minimum value (default: 0)
        max: Maximum value (default: 100)
        value: Initial value (default: 50)
        name: Optional name attribute
        step: Optional step value

    Example:
        >>> slider = Slider(min=0, max=100, value=50)
        >>> print(slider.render_html())
        <input class="cn-slider" type="range" min="0" max="100" value="50" />
    """

    def __init__(
        self,
        min: float = 0,
        max: float = 100,
        value: float = 50,
        name: str | None = None,
        step: float | None = None,
    ):
        if min >= max:
            raise ValueError("min must be less than max")
        if value < min or value > max:
            raise ValueError("value must be between min and max")

        self.min = min
        self.max = max
        self.value = value
        self.name = name
        self.step = step

    def render(self) -> FormElement:
        """Render the slider as a FormElement.

        Returns:
            FormElement representing the range input
        """
        attrs: dict[str, str] = {
            "type": "range",
            "min": str(self.min),
            "max": str(self.max),
            "value": str(self.value),
        }
        if self.name is not None:
            attrs["name"] = self.name
        if self.step is not None:
            attrs["step"] = str(self.step)

        attrs_str = "".join(f' {k}="{v}"' for k, v in attrs.items())
        inner = f'<input class="cn-slider"{attrs_str} />'

        return FormElement(inner_html=inner)

    def render_html(self) -> str:
        """Render the slider as an HTML string.

        Returns:
            HTML string representation of the slider
        """
        return self.render().render_html()


class FileInput:
    """File input component with drag-and-drop styling.

    Args:
        accept: Accepted file types (e.g. ".png,.jpg")
        multiple: Whether multiple files can be selected (default: False)
        name: Optional name attribute

    Example:
        >>> file = FileInput(accept=".png,.jpg", multiple=True)
        >>> print(file.render_html())
    """

    _UPLOAD_ICON = (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor">'
        '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>'
        '<polyline points="17 8 12 3 7 8"/>'
        '<line x1="12" y1="3" x2="12" y2="15"/>'
        '</svg>'
    )

    def __init__(
        self,
        accept: str = "",
        multiple: bool = False,
        name: str | None = None,
    ):
        self.accept = accept
        self.multiple = multiple
        self.name = name

    def render(self) -> FormElement:
        """Render the file input as a FormElement.

        Returns:
            FormElement representing the file input with label
        """
        input_attrs: dict[str, str] = {"type": "file"}
        if self.name is not None:
            input_attrs["name"] = self.name
        if self.accept:
            input_attrs["accept"] = self.accept
        if self.multiple:
            input_attrs["multiple"] = ""

        input_attrs_str = "".join(f' {k}="{v}"' for k, v in input_attrs.items())

        inner = (
            f'<div class="cn-file-input">'
            f'<input{input_attrs_str} />'
            f'<div class="cn-file-input-label">'
            f'<div class="cn-file-input-icon">{self._UPLOAD_ICON}</div>'
            f'<div class="cn-file-input-text">Drag and drop or <span>browse</span></div>'
            f"</div>"
            f"</div>"
        )

        return FormElement(inner_html=inner)

    def render_html(self) -> str:
        """Render the file input as an HTML string.

        Returns:
            HTML string representation of the file input
        """
        return self.render().render_html()


class HasRenderHtml:
    """Protocol-like base for type hints: any object with render_html()."""

    def render_html(self) -> str:
        ...
