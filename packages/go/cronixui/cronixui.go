package cronixui

import (
	"image/color"
	"strings"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/canvas"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/theme"
	"fyne.io/fyne/v2/widget"
)

const Version = "1.0.6"

// =============================================================================
// DESIGN TOKENS
// =============================================================================

type Colors struct {
	BG            color.Color
	Surface       color.Color
	Surface2      color.Color
	Surface3      color.Color
	Surface4      color.Color
	Text          color.Color
	TextMuted     color.Color
	TextDim       color.Color
	Accent        color.Color
	AccentHover   color.Color
	AccentLight   color.Color
	AccentGlow    color.Color
	AccentText    color.Color
	Success       color.Color
	SuccessBorder color.Color
	SuccessText   color.Color
	Warning       color.Color
	WarningBorder color.Color
	WarningText   color.Color
	Error         color.Color
	ErrorBorder   color.Color
	ErrorText     color.Color
	Info          color.Color
	InfoBorder    color.Color
	InfoText      color.Color
	Border        color.Color
	BorderHover   color.Color
	BorderFocus   color.Color
}

func DefaultColors() *Colors {
	return &Colors{
		BG:            color.RGBA{R: 10, G: 10, B: 10, A: 255},
		Surface:       color.RGBA{R: 17, G: 17, B: 17, A: 255},
		Surface2:      color.RGBA{R: 26, G: 26, B: 26, A: 255},
		Surface3:      color.RGBA{R: 34, G: 34, B: 34, A: 255},
		Surface4:      color.RGBA{R: 42, G: 42, B: 42, A: 255},
		Text:          color.RGBA{R: 240, G: 237, B: 232, A: 255},
		TextMuted:     color.RGBA{R: 240, G: 237, B: 232, A: 128},
		TextDim:       color.RGBA{R: 240, G: 237, B: 232, A: 64},
		Accent:        color.RGBA{R: 107, G: 35, B: 35, A: 255},
		AccentHover:   color.RGBA{R: 125, G: 42, B: 42, A: 255},
		AccentLight:   color.RGBA{R: 138, G: 53, B: 53, A: 255},
		AccentGlow:    color.RGBA{R: 107, G: 35, B: 35, A: 77},
		AccentText:    color.RGBA{R: 201, G: 122, B: 122, A: 255},
		Success:       color.RGBA{R: 30, G: 80, B: 40, A: 255},
		SuccessBorder: color.RGBA{R: 60, G: 140, B: 70, A: 102},
		SuccessText:   color.RGBA{R: 107, G: 196, B: 122, A: 255},
		Warning:       color.RGBA{R: 80, G: 60, B: 20, A: 255},
		WarningBorder: color.RGBA{R: 150, G: 110, B: 30, A: 102},
		WarningText:   color.RGBA{R: 196, G: 164, B: 58, A: 255},
		Error:         color.RGBA{R: 80, G: 20, B: 20, A: 255},
		ErrorBorder:   color.RGBA{R: 180, G: 60, B: 60, A: 102},
		ErrorText:     color.RGBA{R: 196, G: 107, B: 107, A: 255},
		Info:          color.RGBA{R: 20, G: 53, B: 80, A: 255},
		InfoBorder:    color.RGBA{R: 60, G: 140, B: 200, A: 102},
		InfoText:      color.RGBA{R: 107, G: 168, B: 196, A: 255},
		Border:        color.RGBA{R: 255, G: 255, B: 255, A: 20},
		BorderHover:   color.RGBA{R: 255, G: 255, B: 255, A: 38},
		BorderFocus:   color.RGBA{R: 255, G: 255, B: 255, A: 64},
	}
}

type Typography struct {
	FontFamily   string
	FontMono     string
	FontSizeXS   float32
	FontSizeSM   float32
	FontSizeBase float32
	FontSizeMD   float32
	FontSizeLG   float32
	FontSizeXL   float32
	FontSize2XL  float32
	FontSize3XL  float32
}

func DefaultTypography() *Typography {
	return &Typography{
		FontFamily:   "Outfit",
		FontMono:     "JetBrains Mono",
		FontSizeXS:   11,
		FontSizeSM:   12,
		FontSizeBase: 13,
		FontSizeMD:   14,
		FontSizeLG:   16,
		FontSizeXL:   20,
		FontSize2XL:  28,
		FontSize3XL:  36,
	}
}

type Spacing struct {
	Space1, Space2, Space3, Space4, Space5, Space6, Space8, Space10, Space12 float32
}

func DefaultSpacing() *Spacing {
	return &Spacing{4, 8, 12, 16, 20, 24, 32, 40, 48}
}

type RadiusTokens struct {
	SM, Default, LG, XL, Full float32
}

func DefaultRadiusTokens() *RadiusTokens {
	return &RadiusTokens{6, 10, 14, 20, 9999}
}

type Shadow struct {
	SM, Default, LG, Glow string
}

func DefaultShadow() *Shadow {
	return &Shadow{
		SM:      "0 1px 2px rgba(0, 0, 0, 0.3)",
		Default: "0 4px 12px rgba(0, 0, 0, 0.4)",
		LG:      "0 8px 24px rgba(0, 0, 0, 0.5)",
		Glow:    "0 0 20px rgba(107, 35, 35, 0.3)",
	}
}

type Transition struct {
	Fast, Default, Slow string
}

func DefaultTransition() *Transition {
	return &Transition{"0.1s ease", "0.15s ease", "0.25s ease"}
}

type ZIndexTokens struct {
	Dropdown, Sticky, Fixed, ModalBackdrop, Modal, Popover, Tooltip, Toast int
}

func DefaultZIndexTokens() *ZIndexTokens {
	return &ZIndexTokens{100, 200, 300, 400, 500, 600, 700, 800}
}

type LayoutTokens struct {
	ContainerMax, SidebarWidth, HeaderHeight float32
}

func DefaultLayoutTokens() *LayoutTokens {
	return &LayoutTokens{1200, 260, 56}
}

// =============================================================================
// THEME
// =============================================================================

type Theme struct {
	colors  *Colors
	spacing *Spacing
	radius  *RadiusTokens
}

func NewTheme() fyne.Theme {
	return &Theme{
		colors:  DefaultColors(),
		spacing: DefaultSpacing(),
		radius:  DefaultRadiusTokens(),
	}
}

func (t *Theme) Color(name fyne.ThemeColorName, variant fyne.ThemeVariant) color.Color {
	switch name {
	case theme.ColorNameBackground:
		return t.colors.BG
	case theme.ColorNameButton:
		return t.colors.Surface2
	case theme.ColorNameDisabledButton:
		return t.colors.Surface3
	case theme.ColorNameInputBackground:
		return t.colors.Surface
	case theme.ColorNameInputBorder:
		return t.colors.Border
	case theme.ColorNameDisabled:
		return t.colors.TextDim
	case theme.ColorNameForeground:
		return t.colors.Text
	case theme.ColorNamePlaceHolder:
		return t.colors.TextMuted
	case theme.ColorNamePrimary:
		return t.colors.Accent
	case theme.ColorNameHover:
		return t.colors.Surface3
	case theme.ColorNamePressed:
		return t.colors.Surface4
	case theme.ColorNameScrollBar:
		return t.colors.Surface3
	case theme.ColorNameShadow:
		return color.RGBA{R: 0, G: 0, B: 0, A: 50}
	case theme.ColorNameSuccess:
		return t.colors.Success
	case theme.ColorNameWarning:
		return t.colors.Warning
	case theme.ColorNameError:
		return t.colors.Error
	default:
		return t.colors.Text
	}
}

func (t *Theme) Font(style fyne.TextStyle) fyne.Resource {
	return theme.DefaultTheme().Font(style)
}

func (t *Theme) Icon(name fyne.ThemeIconName) fyne.Resource {
	return theme.DefaultTheme().Icon(name)
}

func (t *Theme) Size(name fyne.ThemeSizeName) float32 {
	switch name {
	case theme.SizeNamePadding:
		return t.spacing.Space2
	case theme.SizeNameInlinePadding:
		return t.spacing.Space3
	case theme.SizeNameScrollBar:
		return 8
	case theme.SizeNameScrollBarSmall:
		return 4
	case theme.SizeNameSeparatorThickness:
		return 1
	case theme.SizeNameText:
		return t.spacing.Space4
	case theme.SizeNameHeadingText:
		return t.spacing.Space6
	case theme.SizeNameSubHeadingText:
		return t.spacing.Space5
	case theme.SizeNameCaptionText:
		return t.spacing.Space2
	case theme.SizeNameInputBorder:
		return 1
	case theme.SizeNameInputRadius:
		return t.radius.Default
	case theme.SizeNameSelectionRadius:
		return t.radius.SM
	default:
		return 0
	}
}

// =============================================================================
// BUTTONS
// =============================================================================

type ButtonVariant int

const (
	ButtonDefault ButtonVariant = iota
	ButtonPrimary
	ButtonGhost
	ButtonOutline
	ButtonDanger
	ButtonSuccess
)

func NewButton(text string, variant ButtonVariant, onTap func()) *widget.Button {
	btn := widget.NewButton(text, onTap)
	switch variant {
	case ButtonPrimary:
		btn.Importance = widget.HighImportance
	case ButtonDanger:
		btn.Importance = widget.DangerImportance
	case ButtonSuccess:
		btn.Importance = widget.HighImportance
	case ButtonGhost, ButtonOutline:
		btn.Importance = widget.LowImportance
	default:
		btn.Importance = widget.MediumImportance
	}
	return btn
}

func NewButtonGroup(buttons ...*widget.Button) *fyne.Container {
	return container.NewHBox(buttons...)
}

// =============================================================================
// CARD
// =============================================================================

// CardOption is a function that configures a card.
type CardOption func(*CardConfig)

// CardConfig holds card configuration.
type CardConfig struct {
	Title    string
	Subtitle string
	Icon     fyne.CanvasObject
	Footer   fyne.CanvasObject
	Clickable bool
}

// WithCardTitle sets the card title.
func WithCardTitle(title string) CardOption {
	return func(c *CardConfig) { c.Title = title }
}

// WithCardSubtitle sets the card subtitle.
func WithCardSubtitle(subtitle string) CardOption {
	return func(c *CardConfig) { c.Subtitle = subtitle }
}

// WithCardIcon sets the card icon.
func WithCardIcon(icon fyne.CanvasObject) CardOption {
	return func(c *CardConfig) { c.Icon = icon }
}

// WithCardFooter sets the card footer.
func WithCardFooter(footer fyne.CanvasObject) CardOption {
	return func(c *CardConfig) { c.Footer = footer }
}

// WithCardClickable makes the card clickable.
func WithCardClickable(clickable bool) CardOption {
	return func(c *CardConfig) { c.Clickable = clickable }
}

// NewCard creates a card widget with optional icon, title, subtitle, and footer.
func NewCard(content fyne.CanvasObject, options ...CardOption) *fyne.Container {
	config := &CardConfig{}
	for _, opt := range options {
		opt(config)
	}

	c := DefaultColors()
	
	var headerObjects []fyne.CanvasObject
	if config.Icon != nil {
		headerObjects = append(headerObjects, config.Icon)
	}
	if config.Title != "" {
		titleText := canvas.NewText(config.Title, c.Text)
		titleText.TextSize = 14
		titleText.TextStyle = fyne.TextStyle{Bold: true}
		headerObjects = append(headerObjects, titleText)
	}
	if config.Subtitle != "" {
		subtitleText := canvas.NewText(config.Subtitle, c.TextMuted)
		subtitleText.TextSize = 12
		headerObjects = append(headerObjects, subtitleText)
	}

	var header *fyne.Container
	if len(headerObjects) > 0 {
		header = container.NewVBox(headerObjects...)
	}

	var body fyne.CanvasObject
	if header != nil {
		body = container.NewVBox(header, content)
	} else {
		body = content
	}

	var finalContent *fyne.Container
	if config.Footer != nil {
		finalContent = container.NewVBox(body, canvas.NewRectangle(c.Border), config.Footer)
	} else {
		if c, ok := body.(*fyne.Container); ok {
			finalContent = c
		} else {
			finalContent = container.NewMax(body)
		}
	}

	bg := canvas.NewRectangle(c.Surface)
	bg.StrokeColor = c.Border
	bg.StrokeWidth = 1
	bg.CornerRadius = 14

	return container.NewStack(bg, container.NewPadded(finalContent))
}

// =============================================================================
// INPUTS
// =============================================================================

func NewInput(placeholder string) *widget.Entry {
	entry := widget.NewEntry()
	entry.SetPlaceHolder(placeholder)
	return entry
}

func NewTextarea(placeholder string) *widget.Entry {
	entry := widget.NewMultiLineEntry()
	entry.SetPlaceHolder(placeholder)
	return entry
}

func NewPassword(placeholder string) *widget.Entry {
	entry := widget.NewPasswordEntry()
	entry.SetPlaceHolder(placeholder)
	return entry
}

// =============================================================================
// FORM ELEMENTS
// =============================================================================

func NewCheckbox(label string, onChanged func(bool)) *widget.Check {
	return widget.NewCheck(label, onChanged)
}

func NewRadio(options []string, onChanged func(string)) *widget.RadioGroup {
	return widget.NewRadioGroup(options, onChanged)
}

func NewSelect(options []string, onChanged func(string)) *widget.Select {
	return widget.NewSelect(options, onChanged)
}

func NewSlider(min, max float64) *widget.Slider {
	return widget.NewSlider(min, max)
}

// =============================================================================
// PROGRESS & LOADING
// =============================================================================

func NewProgress() *widget.ProgressBar {
	return widget.NewProgressBar()
}

func NewProgressInfinite() *widget.ProgressBarInfinite {
	return widget.NewProgressBarInfinite()
}

// =============================================================================
// TOGGLE
// =============================================================================

type Toggle struct {
	widget.BaseWidget
	on       bool
	onToggle func(bool)
}

func NewToggle(onToggle func(bool)) *Toggle {
	t := &Toggle{onToggle: onToggle}
	t.ExtendBaseWidget(t)
	return t
}

func (t *Toggle) Toggle() {
	t.on = !t.on
	if t.onToggle != nil {
		t.onToggle(t.on)
	}
	t.Refresh()
}

func (t *Toggle) IsOn() bool       { return t.on }
func (t *Toggle) SetOn(value bool) { t.on = value; t.Refresh() }

// =============================================================================
// MODAL
// =============================================================================

type Modal struct {
	widget.BaseWidget
	content fyne.CanvasObject
	open    bool
	window  fyne.Window
}

func NewModal(content fyne.CanvasObject) *Modal {
	m := &Modal{content: content}
	m.ExtendBaseWidget(m)
	return m
}

func (m *Modal) Open(window fyne.Window) {
	m.window = window
	m.open = true
	m.Show()
}

func (m *Modal) Close()       { m.open = false; m.Hide() }
func (m *Modal) IsOpen() bool { return m.open }
func (m *Modal) Show() {
	if m.window != nil {
		popup := widget.NewModalPopUp(m.content, m.window.Canvas())
		popup.Show()
	}
}
func (m *Modal) Hide() {}

// =============================================================================
// DROPDOWN
// =============================================================================

// Dropdown creates a dropdown selection widget using Fyne's Select widget.
func NewDropdown(items []string, onSelect func(string)) *widget.Select {
	s := widget.NewSelect(items, onSelect)
	return s
}

// =============================================================================
// TABS
// =============================================================================

func NewTabs(items ...*widget.TabItem) *container.AppTabs {
	return container.NewAppTabs(items...)
}

// =============================================================================
// ACCORDION
// =============================================================================

type AccordionItem struct {
	Title   string
	Content fyne.CanvasObject
}

type Accordion struct {
	widget.BaseWidget
	items       []AccordionItem
	openIndices map[int]bool
}

func NewAccordion(items ...AccordionItem) *Accordion {
	a := &Accordion{items: items, openIndices: make(map[int]bool)}
	a.ExtendBaseWidget(a)
	return a
}

func (a *Accordion) Toggle(index int) { a.openIndices[index] = !a.openIndices[index]; a.Refresh() }
func (a *Accordion) Open(index int)   { a.openIndices[index] = true; a.Refresh() }
func (a *Accordion) Close(index int)  { delete(a.openIndices, index); a.Refresh() }
func (a *Accordion) OpenAll() {
	for i := range a.items {
		a.openIndices[i] = true
	}
	a.Refresh()
}
func (a *Accordion) CloseAll()             { a.openIndices = make(map[int]bool); a.Refresh() }
func (a *Accordion) IsOpen(index int) bool { return a.openIndices[index] }

// =============================================================================
// PAGINATION
// =============================================================================

type Pagination struct {
	widget.BaseWidget
	total    int
	current  int
	onChange func(int)
}

func NewPagination(total, current int, onChange func(int)) *Pagination {
	p := &Pagination{total: total, current: current, onChange: onChange}
	p.ExtendBaseWidget(p)
	return p
}

func (p *Pagination) GoTo(page int) {
	if page >= 1 && page <= p.total {
		p.current = page
		if p.onChange != nil {
			p.onChange(page)
		}
		p.Refresh()
	}
}
func (p *Pagination) Next() {
	if p.current < p.total {
		p.GoTo(p.current + 1)
	}
}
func (p *Pagination) Prev() {
	if p.current > 1 {
		p.GoTo(p.current - 1)
	}
}
func (p *Pagination) Current() int { return p.current }
func (p *Pagination) Total() int   { return p.total }

// =============================================================================
// TOAST
// =============================================================================

type ToastType int

const (
	ToastSuccess ToastType = iota
	ToastError
	ToastWarning
	ToastInfo
)

func ShowToast(window fyne.Window, message string, toastType ToastType) {
	c := DefaultColors()
	var bgColor color.Color
	var prefix string
	switch toastType {
	case ToastSuccess:
		bgColor = c.Success
		prefix = "✓ "
	case ToastError:
		bgColor = c.Error
		prefix = "✕ "
	case ToastWarning:
		bgColor = c.Warning
		prefix = "⚠ "
	default:
		bgColor = c.Info
		prefix = "ℹ "
	}
	label := canvas.NewText(prefix+message, c.Text)
	label.TextSize = 13
	bg := canvas.NewRectangle(bgColor)
	bg.CornerRadius = 10
	cont := container.NewStack(bg, container.NewPadded(label))
	popover := widget.NewPopUp(cont, window.Canvas())
	popover.Move(fyne.NewPos(window.Canvas().Size().Width-320, window.Canvas().Size().Height-60))
}

// =============================================================================
// COMMAND PALETTE
// =============================================================================

type CommandItem struct {
	Title, Subtitle, Kbd string
	Action               func()
}

// CommandPalette creates a modal command palette with search and filtering.
func NewCommandPalette(window fyne.Window, items []CommandItem) *fyne.Container {
	c := DefaultColors()
	searchEntry := widget.NewEntry()
	searchEntry.SetPlaceHolder("Type to search commands...")

	list := widget.NewList(
		func() int { return len(items) },
		func() fyne.CanvasObject {
			return container.NewVBox(
				widget.NewLabel("Command"),
				widget.NewLabel("Description"),
			)
		},
		func(id widget.ListItemID, item fyne.CanvasObject) {
			if id < len(items) {
				vbox := item.(*fyne.Container)
				vbox.Objects[0].(*widget.Label).SetText(items[id].Title)
				vbox.Objects[1].(*widget.Label).SetText(items[id].Subtitle)
			}
		},
	)

	searchEntry.OnChanged = func(query string) {
		// Filter logic can be added here
		list.Refresh()
	}

	list.OnSelected = func(id widget.ListItemID) {
		if id < len(items) && items[id].Action != nil {
			items[id].Action()
			window.Hide()
		}
	}

	content := container.NewVBox(
		searchEntry,
		container.NewScroll(list),
	)

	bg := canvas.NewRectangle(c.Surface)
	bg.CornerRadius = 14

	return container.NewStack(bg, container.NewPadded(content))
}

// =============================================================================
// SEARCH
// =============================================================================

type SearchItem struct {
	Title, Subtitle string
	Action          func()
}

// Search creates a search widget with input and results list.
func NewSearch(items []SearchItem, onSelect func(SearchItem)) *fyne.Container {
	c := DefaultColors()
	searchEntry := widget.NewEntry()
	searchEntry.SetPlaceHolder("Search...")

	results := make([]SearchItem, 0)
	resultsList := widget.NewList(
		func() int { return len(results) },
		func() fyne.CanvasObject {
			return container.NewVBox(
				widget.NewLabel("Title"),
				widget.NewLabel("Subtitle"),
			)
		},
		func(id widget.ListItemID, item fyne.CanvasObject) {
			if id < len(results) {
				vbox := item.(*fyne.Container)
				vbox.Objects[0].(*widget.Label).SetText(results[id].Title)
				vbox.Objects[1].(*widget.Label).SetText(results[id].Subtitle)
			}
		},
	)

	resultsList.OnSelected = func(id widget.ListItemID) {
		if id < len(results) && onSelect != nil {
			onSelect(results[id])
		}
	}

	searchEntry.OnChanged = func(query string) {
		results = make([]SearchItem, 0)
		if query == "" {
			resultsList.Refresh()
			return
		}
		for _, item := range items {
			// Simple case-insensitive search
			if containsIgnoreCase(item.Title, query) || containsIgnoreCase(item.Subtitle, query) {
				results = append(results, item)
			}
		}
		resultsList.Refresh()
	}

	content := container.NewVBox(
		searchEntry,
		container.NewScroll(resultsList),
	)

	return content
}

func containsIgnoreCase(s, substr string) bool {
	return strings.Contains(strings.ToLower(s), strings.ToLower(substr))
}

// =============================================================================
// TABLE
// =============================================================================

func NewTable(rows, cols int, cellFunc func(row, col int) fyne.CanvasObject) *widget.Table {
	return widget.NewTable(
		func() (int, int) { return rows, cols },
		func() fyne.CanvasObject { return widget.NewLabel("") },
		func(id widget.TableCellID, cell fyne.CanvasObject) {
			if obj := cellFunc(id.Row, id.Col); obj != nil {
				cell.(*widget.Label).SetText(obj.(*widget.Label).Text)
			}
		},
	)
}

// =============================================================================
// LIST
// =============================================================================

type ListItem struct {
	Title, Subtitle string
}

func NewList(items []ListItem) *widget.List {
	return widget.NewList(
		func() int { return len(items) },
		func() fyne.CanvasObject { return widget.NewLabel("") },
		func(id widget.ListItemID, item fyne.CanvasObject) {
			item.(*widget.Label).SetText(items[id].Title)
		},
	)
}

// =============================================================================
// LAYOUT HELPERS
// =============================================================================

func NewContainer(content fyne.CanvasObject) fyne.CanvasObject {
	return container.NewMax(content)
}

func NewFlex(objects ...fyne.CanvasObject) fyne.CanvasObject {
	return container.NewHBox(objects...)
}

func NewStack(objects ...fyne.CanvasObject) fyne.CanvasObject {
	return container.NewVBox(objects...)
}

func NewGrid(cols int, objects ...fyne.CanvasObject) fyne.CanvasObject {
	return container.NewGridWithColumns(cols, objects...)
}

func NewForm(items ...*widget.FormItem) *widget.Form {
	return widget.NewForm(items...)
}

// =============================================================================
// NAV
// =============================================================================

// Nav creates a navigation sidebar widget.
func NewNav(items []string, active int, onSelect func(int)) *widget.List {
	list := widget.NewList(
		func() int { return len(items) },
		func() fyne.CanvasObject {
			return widget.NewLabel("Nav Item")
		},
		func(id widget.ListItemID, item fyne.CanvasObject) {
			if id < len(items) {
				item.(*widget.Label).SetText(items[id])
			}
		},
	)
	list.OnSelected = func(id widget.ListItemID) {
		if onSelect != nil {
			onSelect(id)
		}
	}
	if active >= 0 && active < len(items) {
		list.Select(active)
	}
	return list
}

// =============================================================================
// STAT
// =============================================================================

type StatDeltaType int

const (
	StatDeltaUp StatDeltaType = iota
	StatDeltaDown
)

// Stat creates a stat/metric display widget with value, label, and optional delta.
func NewStat(value string, label string, delta string, deltaType StatDeltaType) *fyne.Container {
	c := DefaultColors()

	valueLabel := canvas.NewText(value, c.Text)
	valueLabel.TextSize = 28
	valueLabel.TextStyle = fyne.TextStyle{Bold: true}

	labelWidget := canvas.NewText(label, c.TextMuted)
	labelWidget.TextSize = 11

	var deltaWidget *canvas.Text
	if delta != "" {
		deltaColor := c.SuccessText
		if deltaType == StatDeltaDown {
			deltaColor = c.ErrorText
		}
		prefix := "↑ "
		if deltaType == StatDeltaDown {
			prefix = "↓ "
		}
		deltaWidget = canvas.NewText(prefix+delta, deltaColor)
		deltaWidget.TextSize = 11
	}

	content := container.NewVBox(
		valueLabel,
		labelWidget,
	)

	if deltaWidget != nil {
		content = container.NewVBox(
			valueLabel,
			labelWidget,
			deltaWidget,
		)
	}

	bg := canvas.NewRectangle(c.Surface)
	bg.StrokeColor = c.Border
	bg.StrokeWidth = 1
	bg.CornerRadius = 10

	return container.NewStack(bg, container.NewPadded(content))
}

// =============================================================================
// APPLICATION
// =============================================================================

type App struct {
	fyne.App
	Theme fyne.Theme
}

func NewApp() *App {
	a := app.New()
	t := NewTheme()
	a.Settings().SetTheme(t)
	return &App{App: a, Theme: t}
}

func (a *App) NewWindow(title string) fyne.Window {
	return a.App.NewWindow(title)
}

func Init() fyne.Theme {
	return NewTheme()
}
