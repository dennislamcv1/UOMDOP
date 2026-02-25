import fra_amtrak.chart.chart as chrt
import fra_amtrak.chart.protocols.chart as pchrt
import fra_amtrak.chart.protocols.mark as pmrk
import fra_amtrak.chart.protocols.schema as pschm
import pandas as pd

from dataclasses import dataclass, field
from enum import Enum
from typing import Sequence


@dataclass(frozen=True)
class EncodingDescriptor:
    """Descriptor for chart encoding.

    ields:
        shorthand (str): Altair shorthand notation for the field (e.g., 'field_name:Q')
        title (str | None): Human-readable title for axis or legend
    """

    shorthand: str
    title: str | None = None


class ChannelDescriptor(Enum):
    """Enum for chart channel descriptors.

    Members:
        X (EncodingDescriptor): x-axis descriptor
        Y (EncodingDescriptor): y-axis descriptor
        COLOR (EncodingDescriptor): color encoding descriptor
    """

    X = EncodingDescriptor("Fiscal Period:N", "Fiscal Period")
    XOFFSET = EncodingDescriptor("Arrival Status:N", "Arrival Status")
    Y = EncodingDescriptor("Passengers:Q", "Passengers")
    COLOR = EncodingDescriptor("Arrival Status:N", "Arrival Status")


@dataclass(kw_only=True)
class GrpBarChartEncodings:
    """Select Altair chart encodings.

    Fields:
        x (pschm.X): x-axis attributes
        y (pschm.Y): y-axis attributes
        xoffset (pschm.XOffset): x-offset attributes
        color (pschm.Color): color attributes
        tooltip (Sequence[pschm.Tooltip]): tooltip attributes
    """

    x: pschm.PrimaryChannel = field(
        default_factory=lambda: chrt.PrimaryChannel(
            shorthand=ChannelDescriptor.X.value.shorthand,
            axis=chrt.Axis(grid=False, title=ChannelDescriptor.X.value.title),
        )
    )
    y: pschm.PrimaryChannel = field(
        default_factory=lambda: chrt.PrimaryChannel(
            shorthand=ChannelDescriptor.Y.value.shorthand,
            axis=chrt.Axis(grid=True, title=ChannelDescriptor.Y.value.title),
        )
    )
    xoffset: pschm.PrimaryChannelOffset = field(
        default_factory=lambda: chrt.PrimaryChannelOffset(
            shorthand=ChannelDescriptor.XOFFSET.value.shorthand,
            sort=["On Time", "Late"],
            title=ChannelDescriptor.XOFFSET.value.title,
        )
    )
    color: pschm.Color = field(
        default_factory=lambda: chrt.Color(
            shorthand=ChannelDescriptor.COLOR.value.shorthand,
            scale=chrt.Scale(
                domain=list(chrt.ARRIVAL_COLORS.keys()), range_=list(chrt.ARRIVAL_COLORS.values())
            ),
            title=ChannelDescriptor.COLOR.value.title,
        )
    )
    tooltip: Sequence[pschm.Tooltip] = field(
        default_factory=lambda: [
            chrt.Tooltip(
                shorthand=ChannelDescriptor.X.value.shorthand, title=ChannelDescriptor.X.value.title
            ),
            chrt.Tooltip(
                shorthand=ChannelDescriptor.Y.value.shorthand, title=ChannelDescriptor.Y.value.title
            ),
        ]
    )


@dataclass(kw_only=True)
class BarMarkProperties:
    """Select Altair bar mark attributes.

    Fields:
        bin_spacing (float | None): bin spacing
        opacity (float | None): bar opacity
    """

    bin_spacing: float | None = None
    opacity: float | None = None


@dataclass(kw_only=True)
class GrpBarChart:
    """Select Altair grouped bar chart attributes. The < properties > attribute is
    initialized by the < __post_init__ > method.

    Fields:
        frame (pd.DataFrame): data frame for the chart
        title (str): title of the chart
        mark (pmrk.BarMarkProperties): bar mark properties
        encode (pchrt.GrpBarChartEncodings): chart encodings
        config_view (pchrt.ChartViewConfig): chart view configuration
        properties (pchrt.ChartProperties): chart properties
    """

    frame: pd.DataFrame
    title: str
    mark: pmrk.BarMarkProperties = field(default_factory=BarMarkProperties)
    encode: pchrt.GrpBarChartEncodings = field(default_factory=GrpBarChartEncodings)
    config_view: pchrt.ChartViewConfig = field(default_factory=chrt.ChartViewConfig)
    properties: pchrt.ChartProperties = field(init=False)

    def __post_init__(self) -> None:
        self.properties = chrt.ChartProperties(height=300, width=580, padding=15, title=self.title)
