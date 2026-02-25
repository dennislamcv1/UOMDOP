import fra_amtrak.chart.chart_types as typ

from typing import Protocol


class Axis(Protocol):
    """Select Altair alt.Axis schema attributes.

    Fields:
        grid (bool | None): display grid lines
        label_angle (float | None): angle of the axis labels
        label_font_weight (typ.AltFontWeight | None): font weight of the axis labels
        label_padding (float | None): padding between the axis labels and the axis line
        tick_count (typ.AltTickCount | None): number of ticks on the axis
        title (str | None): title of the axis
        title_font_size (float | None): font size of the axis title
        title_font_weight (typ.AltFontWeight | None): font weight of the axis title
        values (typ.AltAxisValues | None): specific values to display on the axis
    """

    grid: bool | None
    label_angle: float | None
    label_font_weight: typ.AltFontWeight | None
    label_padding: float | None
    tick_count: typ.AltTickCount | None
    title: str | None
    title_font_size: float | None
    title_font_weight: typ.AltFontWeight | None
    values: typ.AltAxisValues | None


class BinParams(Protocol):
    """Select Altair alt.BinParams schema attributes.

    Fields:
        max_bins (int | None): maximum number of bins
        step (int | None): bin width
    """

    max_bins: float | None
    step: float | None


class Scale(Protocol):
    """Select Altair alt.Scale schema attributes.

    Fields:
        domain (list[float] | list[str] | None): domain values
        range_ (list[str] | None): range values
        zero (bool | None): whether to start the scale at zero
    """

    domain: list[float] | list[str] | None
    range_: list[str] | None
    zero: bool | None


class Color(Protocol):
    """Select Altair alt.Color schema attributes.

    Fields:
        shorthand (str): color shorthand
        legend (str | None): legend shorthand
        scale (chrt.Scale | None): scale attributes
        title (str | None): color title
        disable_legend (bool): whether to disable the legend
    """

    shorthand: str
    legend: str | None
    scale: Scale | None
    title: str | None
    disable_legend: bool = False


class Order(Protocol):
    """Select Order attributes.

    Fields:
        shorthand (str): order shorthand for field, aggregate, and type
    """

    shorthand: str


class PrimaryChannel(Protocol):
    """Select Altair X or Y schema attributes.

    Fields:
        shorthand (str): shorthand for the axis
        axis (Axis | None): axis format attributes
        bin (BinParams | str | None): bin parameters
        scale (Scale | None): scale attributes
        sort (list[str] | None): sort order for the axis
        stack (bool | None): whether to stack the axis
        title (str | None): axis title
    """

    shorthand: str
    axis: Axis | None
    bin: BinParams | str | None
    scale: Scale | None
    sort: list[str] | None
    stack: bool | None
    title: str | None


class PrimaryChannelOffset(Protocol):
    """Select Altair XOffset or YOffset schema attributes.

    Fields:
        shorthand (str): shorthand for the x-offset
        sort (list[str] | None): sort order
        title (str | None): title for the x-offset
    """

    shorthand: str
    sort: list[str] | None
    title: str | None


class SecondaryChannel(Protocol):
    """Select Altair secondary X2 or Y2 schema attributes.

    Fields:
        shorthand (str): shorthand for the axis
    """

    shorthand: str


class Tooltip(Protocol):
    """Select Altair alt.Tooltip schema attributes. Default values for < format_type > include
    "number" and "time" respectively.

    Fields:
        shorthand (str | None): tooltip shorthand
        title (str | None): tooltip title
        format (str | None): tooltip format
        format_type (str | None): tooltip format type
    """

    shorthand: str | None
    title: str | None
    format: str | None
    format_type: str | None
