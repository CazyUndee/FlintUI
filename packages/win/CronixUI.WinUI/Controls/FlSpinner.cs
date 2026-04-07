using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;

namespace CronixUI.Controls;

public sealed class FlSpinner : ProgressRing
{
    public FlSpinner()
    {
        DefaultStyleKey = typeof(FlSpinner);
    }

    public static readonly DependencyProperty SizeProperty =
        DependencyProperty.Register(nameof(Size), typeof(string), typeof(FlSpinner), new PropertyMetadata("md"));

    public string Size
    {
        get => (string)GetValue(SizeProperty);
        set => SetValue(SizeProperty, value);
    }
}
