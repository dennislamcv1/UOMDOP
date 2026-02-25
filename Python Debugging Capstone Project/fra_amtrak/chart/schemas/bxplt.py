import fra_amtrak.chart.chart as chrt
import fra_amtrak.chart.chart_types as typ
import fra_amtrak.chart.protocols.chart as pchrt
import fra_amtrak.chart.protocols.mark as pmrk
import fra_amtrak.chart.protocols.schema as pschm
import pandas as pd

from dataclasses import dataclass, field
from enum import Enum
from typing import Sequence

Y_SORT = ["Northeast Corridor", "State Supported", "Long Distance"]


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

    X = EncodingDescriptor("Late Detraining Customers Avg Min Late:Q", "Average Minutes Late")
    Y = EncodingDescriptor("Service Line:N", "Service Line")
    COLOR = EncodingDescriptor("Service Line:N", "Service Line")


@dataclass(kw_only=True)
class ChartEncodings:
    """Select Altair chart encodings. Note that the tooltips are applied to outlier marks only.

    Fields:
        x (X): x-axis attributes
        y (Y): y-axis attributes
        color (Color): color attributes
        tooltip (list[chrt.Tooltip]): tooltip attributes
    """

    x: pschm.PrimaryChannel = field(
        default_factory=lambda: chrt.PrimaryChannel(
            shorthand=ChannelDescriptor.X.value.shorthand,
            axis=chrt.Axis(grid=True, title=ChannelDescriptor.X.value.title),
            scale=chrt.Scale(zero=False),
            title=ChannelDescriptor.X.value.title,
        )
    )
    y: pschm.PrimaryChannel = field(
        default_factory=lambda: chrt.PrimaryChannel(
            shorthand=ChannelDescriptor.Y.value.shorthand,
            axis=chrt.Axis(grid=False, title=ChannelDescriptor.Y.value.title),
            sort=Y_SORT,
        )
    )
    color: pschm.Color = field(
        default_factory=lambda: chrt.Color(
            shorthand=ChannelDescriptor.COLOR.value.shorthand,
            legend=None,  # Hide legend
            scale=chrt.Scale(
                domain=list(chrt.SERVICE_COLORS.keys()), range_=list(chrt.SERVICE_COLORS.values())
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
class BoxplotMarkProperties:
    """Select Altair boxplot mark attributes.

    Fields:
        extent (str | None): extent of the boxplot
        orient (typ.AltMarkOrient | None): orientation of the boxplot
        size (float | None): size of the boxplot
    """

    extent: str | None = "min-max"
    orient: typ.AltMarkOrient | None = "vertical"
    size: float | None = 20.0


@dataclass(kw_only=True)
class BoxplotChart:
    """Select Altair boxplot chart attributes. The < properties > attribute is
    initialized by the < __post_init__ > method.

    Fields:
        frame (pd.DataFrame): data frame for the chart
        title (str): title of the chart
        mark (pmrk.BoxplotMarkProperties): boxplot mark properties
        encode (pchrt.ChartEncodings): chart encodings
        config_view (pchrt.ChartViewConfig): chart view configuration
        properties (pchrt.ChartProperties): chart properties
    """

    frame: pd.DataFrame
    title: str
    mark: pmrk.BoxplotMarkProperties = field(default_factory=BoxplotMarkProperties)
    encode: pchrt.ChartEncodings = field(default_factory=ChartEncodings)
    config_view: pchrt.ChartViewConfig = field(default_factory=chrt.ChartViewConfig)
    properties: pchrt.ChartProperties = field(init=False)

    def __post_init__(self) -> None:
        self.properties = chrt.ChartProperties(height=200, width=650, padding=15, title=self.title)
