import fra_amtrak.chart.chart as chrt
import fra_amtrak.chart.protocols.chart as pchrt
import fra_amtrak.chart.protocols.mark as pmrk
import fra_amtrak.chart.protocols.schema as pschm
import pandas as pd
import numpy as np

from dataclasses import dataclass, field
from enum import Enum
from typing import Sequence


@dataclass(frozen=True)
class EncodingDescriptor:
    """Descriptor for chart encoding.

    Fields:
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

    X = EncodingDescriptor("Arrival Station:N", "Arrival Station")
    Y = EncodingDescriptor("Late Detraining Customers Avg Min Late mean:Q", "Average Minutes Late")
    COLOR = EncodingDescriptor("Train Number:N", "Train Number")


@dataclass(kw_only=True)
class ChartEncodings:
    """Select Altair chart encodings.

    Fields:
        x (pschm.X): x-axis attributes
        y (pschm.Y): y-axis attributes
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
            axis=chrt.Axis(
                grid=True,
                title=ChannelDescriptor.Y.value.title,
                values=np.arange(0.0, 100.0, 5).tolist(),
            ),
        ),
    )
    color: pschm.Color = field(
        default_factory=lambda: chrt.Color(
            shorthand=ChannelDescriptor.COLOR.value.shorthand,
            scale=chrt.Scale(domain=list(chrt.COLORS.keys()), range_=list(chrt.COLORS.values())),
            title=ChannelDescriptor.COLOR.value.title,
        )
    )
    tooltip: Sequence[pschm.Tooltip] = field(
        default_factory=lambda: [
            chrt.Tooltip(
                shorthand=ChannelDescriptor.COLOR.value.shorthand,
                title=ChannelDescriptor.COLOR.value.title,
            ),
            chrt.Tooltip(
                shorthand=ChannelDescriptor.X.value.shorthand, title=ChannelDescriptor.X.value.title
            ),
            chrt.Tooltip(
                shorthand=ChannelDescriptor.Y.value.shorthand,
                title=ChannelDescriptor.Y.value.title,
            ),
        ]
    )


@dataclass(kw_only=True)
class LineMarkProperties:
    """Select Altair line mark attributes.

    Fields:
        point (bool | None): whether to display points on the line chart
        stroke_dash (list[int] | None): stroke dash pattern for the line
    """

    point: bool | None = True
    stroke_dash: list[int] | None = None


@dataclass(kw_only=True)
class LineChart:
    """Select Altair line chart attributes. The < properties > attribute is
    initialized by the < __post_init__ > method.

    Fields:
        frame (pd.DataFrame): data frame for the chart
        title (str | None): title of the chart
        mark (pmrk.LineMarkProperties): line mark properties
        encode (pschm.ChartEncodings): chart encodings
        properties (pschm.ChartProperties): chart properties
    """

    frame: pd.DataFrame
    title: str
    mark: pmrk.LineMarkProperties = field(default_factory=LineMarkProperties)
    encode: pchrt.ChartEncodings = field(default_factory=ChartEncodings)
    properties: pchrt.ChartProperties = field(init=False)

    def __post_init__(self) -> None:
        self.properties = chrt.ChartProperties(height=300, width=700, padding=15, title=self.title)
