using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;

namespace CronixUI.Controls;

public sealed class FlProgressBar : ProgressBar
{
    public FlProgressBar()
    {
        DefaultStyleKey = typeof(FlProgressBar);
    }

    public static readonly DependencyProperty VariantProperty =
        DependencyProperty.Register(nameof(Variant), typeof(string), typeof(FlProgressBar), new PropertyMetadata("default"));

    public string Variant
    {
        get => (string)GetValue(VariantProperty);
        set => SetValue(VariantProperty, value);
    }
}
