using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;

namespace CronixUI.Controls;

public sealed class FlTooltip : ContentControl
{
    public FlTooltip()
    {
        DefaultStyleKey = typeof(FlTooltip);
    }

    public static readonly DependencyProperty TooltipContentProperty =
        DependencyProperty.Register(nameof(TooltipContent), typeof(object), typeof(FlTooltip), new PropertyMetadata(null));

    public object TooltipContent
    {
        get => GetValue(TooltipContentProperty);
        set => SetValue(TooltipContentProperty, value);
    }
}
