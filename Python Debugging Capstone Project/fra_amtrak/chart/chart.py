import fra_amtrak.chart.chart_types as typ
import fra_amtrak.chart.protocols.schema as pschm
import pandas as pd

from dataclasses import dataclass
from typing import Any


COLORS = {
    "amtk_blue": "#00537e",
    "amtk_deep_blue": "#003a7b",
    "amtk_heritage_blue": "#0078b9",
    "amtk_red": "#ef3824",
    "anth_gray": "#495153",
    "blue": "#00b1eb",
    "green": "#62a744",
    "lt_blue": "#7bc2d0",
    "orange": "#f9a13f",
}
ARRIVAL_COLORS = {
    "On Time": COLORS["amtk_blue"],
    "Late": COLORS["amtk_red"],
}
SERVICE_COLORS = {
    "Northeast Corridor": COLORS["amtk_blue"],
    "State Supported": COLORS["amtk_red"],
    "Long Distance": COLORS["anth_gray"],
}


@dataclass(kw_only=True)
class Axis:
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
        values (typ.AltAxisValues | None): values for constant lines
    """

    grid: bool | None = False
    label_angle: float | None = 0.0
    label_font_weight: typ.AltFontWeight | None = 400  # 400=normal
    label_padding: float | None = 5.0
    tick_count: typ.AltTickCount | None = None
    title: str | None = None
    title_font_size: float | None = 10.0
    title_font_weight: typ.AltFontWeight | None = 700  # 700=bold
    values: typ.AltAxisValues | None = None  # used for constant lines


@dataclass(kw_only=True)
class BinParams:
    """Select Altair alt.BinParams schema attributes.

    Fields:
        max_bins (int): maximum number of bins
        step (int): bin width
    """

    max_bins: float | None = 20.0
    step: float | None = 5.0  # bin_width


@dataclass(kw_only=True)
class ChartProperties:
    """Select Altair top-level chart properties.

    Fields:
        height (float): chart height
        width (float): chart width
        padding (int): chart padding
        title (str): chart title
    """

    height: float | None = 300.0
    width: float | None = 600.0
    padding: int | None = 15
    title: str | None = None


@dataclass(kw_only=True)
class ChartViewConfig:
    """Select Altair view configuration attributes that control the visual feautures
    associated with a chart.

    Fields:
        stroke (str): stroke color
        stroke_dash (str): stroke dash pattern
        stroke_opacity (float): stroke opacity
        stroke_width (float): stroke width
    """

    stroke: str | None = "#000000"
    stroke_dash: str | None = "solid"
    stroke_opacity: float | None = 1.0
    stroke_width: float | None = 0.0


@dataclass(kw_only=True)
class Color:
    """Select Altair alt.Color schema attributes.

    Fields:
        shorthand (str): color shorthand
        legend (str | None): legend shorthand
        scale (pschm.Scale): scale attributes
        title (str | None): color title
        disable_legend (bool): whether to disable the legend
    """

    shorthand: str
    legend: str | None = None
    scale: pschm.Scale | None = None
    title: str | None = None
    disable_legend: bool = False


@dataclass(kw_only=True)
class Order:
    """Select Order attributes.

    Fields:
        shorthand (str): order shorthand for field, aggregate, and type
    """

    shorthand: str


@dataclass(kw_only=True)
class Scale:
    """Select Altair alt.Scale schema attributes.

    Fields:
        domain (list[float] | list[str] | None): domain values
        range_ (list[str] | None): list of color range values
        zero (bool | None): whether to start the scale at zero
    """

    domain: list[float] | list[str] | None = None
    range_: list[str] | None = None
    zero: bool | None = None


@dataclass(kw_only=True)
class Tooltip:
    """Select Altair alt.Tooltip schema attributes. Default values for < format_type > include
    "number" and "time" respectively which can both be overridden.

    Fields:
        shorthand (str): tooltip shorthand
        title (str | None): tooltip title
        format (str | None): tooltip format
    """

    shorthand: str | None = None
    title: str | None = None
    format: str | None = None
    format_type: str | None = None


@dataclass(kw_only=True)
class PrimaryChannel:
    """Select Altair X or Y axis schema attributes.

    Fields:
        shorthand (str): shorthand for the x-axis
        axis (pschm.Axis): axis attributes
        bin (pschm.BinParams | str | None): bin parameters
        scale (pschm.Scale | None): scale attributes
        sort (list[str] | None): sort order
        stack (bool | None): whether to stack the x-axis
        title (str | None): x-axis title
    """

    shorthand: str
    axis: pschm.Axis | None = None
    bin: pschm.BinParams | str | None = None
    scale: pschm.Scale | None = None
    sort: list[str] | None = None
    stack: bool | None = False
    title: str | None = None


@dataclass(kw_only=True)
class PrimaryChannelOffset:
    """Select Altair X or Y axis offset schema attributes.

    Fields:
        shorthand (str): shorthand for the x-offset
        sort (str): sort order
        title (str): title for the x-offset
    """

    shorthand: str
    sort: list[str] | None = None
    title: str | None = None


@dataclass(kw_only=True)
class SecondaryChannel:
    """Select Altair secondary X2 or Y2 schema attributes.

    Fields:
        shorthand (str): shorthand for the x-axis
    """

    shorthand: str


def format_title(
    frame: pd.DataFrame,
    title_text: str,
    multiline: bool = True,
    anchor: str = "middle",
    font_size: int = 14,
    subtitle_font_size: int = 12,
) -> dict[str, Any]:
    """Returns a formatted title for the chart.

    Returns:
        frame (pd.DataFrame): summary statistics DataFrame
        title_text (str): title of the chart
        multiline (bool): whether the title should be split into multiple lines
        anchor (str): anchor position
        font_size (int): font size
        subtitle_font_size (int): subtitle font size
    """

    detrain_total = int(frame["Total Detraining Customers sum"].sum())
    detrain_late = int(frame["Late Detraining Customers sum"].sum())
    detrain_late_pct = round(detrain_late / detrain_total * 100, 2)
    detrain_on_time = int(detrain_total - detrain_late)
    detrain_on_time_pct = round(detrain_on_time / detrain_total * 100, 2)
    mean_mins_late = frame["Late Detraining Customers Avg Min Late mean"].mean()

    return {
        "text": title_text.split("\n") if multiline else title_text,
        "subtitle": (
            f"total: {detrain_total:,}; "
            f"on time: {detrain_on_time:,} ({detrain_on_time_pct}%); "
            f"late: {detrain_late:,} ({detrain_late_pct}%) | "
            f"mean mins late: {mean_mins_late:.2f}"
        ),
        "anchor": anchor,
        "fontSize": font_size,
        "subtitleFontSize": subtitle_font_size,
    }
