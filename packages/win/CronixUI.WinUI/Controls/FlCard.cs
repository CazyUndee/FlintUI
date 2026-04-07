using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;

namespace CronixUI.Controls;

public sealed class FlCard : ContentControl
{
    public FlCard()
    {
        DefaultStyleKey = typeof(FlCard);
    }

    public static readonly DependencyProperty HoverableProperty =
        DependencyProperty.Register(nameof(Hoverable), typeof(bool), typeof(FlCard), new PropertyMetadata(false));

    public bool Hoverable
    {
        get => (bool)GetValue(HoverableProperty);
        set => SetValue(HoverableProperty, value);
    }
}
