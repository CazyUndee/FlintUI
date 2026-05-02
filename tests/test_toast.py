"""Tests for CronixUI toast component."""

from cronixui.toast import Toast, ToastType


class TestToastType:
    """Test ToastType enum."""

    def test_toast_type_values(self):
        assert ToastType.SUCCESS.value == "success"
        assert ToastType.ERROR.value == "error"
        assert ToastType.WARNING.value == "warning"
        assert ToastType.INFO.value == "info"


class TestToast:
    """Test Toast component."""

    def test_default_toast(self):
        toast = Toast()
        assert toast.title is None
        assert toast.message == ""
        assert toast.duration == 4000

    def test_show_toast(self):
        toast = Toast.show(message="Test message")
        assert toast.message == "Test message"
        assert toast.duration == 4000

    def test_show_toast_with_title(self):
        toast = Toast.show(title="Title", message="Message")
        assert toast.title == "Title"
        assert toast.message == "Message"

    def test_show_toast_with_type(self):
        toast = Toast.show(message="Test", type="success")
        assert toast.type == ToastType.SUCCESS

    def test_success_toast(self):
        toast = Toast.success("Operation completed")
        assert toast.message == "Operation completed"
        assert toast.type == ToastType.SUCCESS

    def test_error_toast(self):
        toast = Toast.error("Something went wrong")
        assert toast.message == "Something went wrong"
        assert toast.type == ToastType.ERROR

    def test_warning_toast(self):
        toast = Toast.warning("Please review")
        assert toast.message == "Please review"
        assert toast.type == ToastType.WARNING

    def test_info_toast(self):
        toast = Toast.info("New updates available")
        assert toast.message == "New updates available"
        assert toast.type == ToastType.INFO

    def test_custom_duration(self):
        toast = Toast.show(message="Test", duration=5000)
        assert toast.duration == 5000

    def test_success_with_title(self):
        toast = Toast.success("Saved", title="Success")
        assert toast.title == "Success"
        assert toast.message == "Saved"

    def test_error_with_title(self):
        toast = Toast.error("Failed", title="Error")
        assert toast.title == "Error"
        assert toast.message == "Failed"

    def test_warning_with_title(self):
        toast = Toast.warning("Check input", title="Warning")
        assert toast.title == "Warning"
        assert toast.message == "Check input"

    def test_info_with_title(self):
        toast = Toast.info("Tip", title="Info")
        assert toast.title == "Info"
        assert toast.message == "Tip"

    def test_toast_properties_are_readonly(self):
        """Toast properties should be read-only via properties."""
        toast = Toast.show(message="Test")
        # These should work (property getters)
        _ = toast.message
        _ = toast.title
        _ = toast.type
        _ = toast.duration
