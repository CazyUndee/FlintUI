using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;

namespace CronixUI.Controls;

public sealed class FlTextBox : TextBox
{
    public FlTextBox()
    {
        DefaultStyleKey = typeof(FlTextBox);
    }

    public static readonly DependencyProperty ErrorProperty =
        DependencyProperty.Register(nameof(Error), typeof(bool), typeof(FlTextBox), new PropertyMetadata(false));

    public bool Error
    {
        get => (bool)GetValue(ErrorProperty);
        set => SetValue(ErrorProperty, value);
    }
}
