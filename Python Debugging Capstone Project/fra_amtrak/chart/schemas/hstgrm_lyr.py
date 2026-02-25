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

    X = EncodingDescriptor("bin_center:Q", "Average Minutes Late")
    X2 = EncodingDescriptor("bin_end:Q")
    Y = EncodingDescriptor("count:Q", "Late Arrivals Count")
    COLOR = EncodingDescriptor("Sub Service:N", "Sub Service")
    ORDER = EncodingDescriptor("order:O")
    BIN_RANGE = EncodingDescriptor("bin_range:N", "Average Minutes Late (range)")
    MEAN_LATE = EncodingDescriptor("mean_late:Q", "Average Minutes Late (mean)")
    MU = EncodingDescriptor("mu_x:Q")
    SIGMA = EncodingDescriptor("sigma_x:Q")


@dataclass(kw_only=True)
class LayeredHistogramChartEncodings:
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
            axis=chrt.Axis(
                grid=False,
                title=ChannelDescriptor.X.value.title,
                values=np.arange(0.0, 620.0, 5).tolist(),
            ),
            bin=chrt.BinParams(max_bins=20, step=5),
            scale=chrt.Scale(domain=[0.0, 620.0]),
        )
    )
    x2: pschm.SecondaryChannel = field(
        default_factory=lambda: chrt.SecondaryChannel(
            shorthand=ChannelDescriptor.X2.value.shorthand
        )
    )
    y: pschm.PrimaryChannel = field(
        default_factory=lambda: chrt.PrimaryChannel(
            shorthand=ChannelDescriptor.Y.value.shorthand,
            axis=chrt.Axis(grid=True, title=ChannelDescriptor.Y.value.title),
        )
    )
    color: pschm.Color = field(
        default_factory=lambda: chrt.Color(
            shorthand=ChannelDescriptor.COLOR.value.shorthand,
            scale=chrt.Scale(
                domain=list(chrt.SERVICE_COLORS.keys()),
                range_=list(chrt.SERVICE_COLORS.values()),
            ),
            title=ChannelDescriptor.COLOR.value.title,
        )
    )
    order: pschm.Order = field(
        default_factory=lambda: chrt.Order(shorthand=ChannelDescriptor.ORDER.value.shorthand)
    )
    tooltip: Sequence[pschm.Tooltip] = field(
        default_factory=lambda: [
            chrt.Tooltip(
                shorthand=ChannelDescriptor.COLOR.value.shorthand,
                title=ChannelDescriptor.COLOR.value.title,
            ),
            chrt.Tooltip(
                shorthand=ChannelDescriptor.BIN_RANGE.value.shorthand,
                title=ChannelDescriptor.BIN_RANGE.value.title,
            ),
            chrt.Tooltip(
                shorthand=ChannelDescriptor.MEAN_LATE.value.shorthand,
                title=ChannelDescriptor.MEAN_LATE.value.title,
                format=".3f",
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

    bin_spacing: float | None = 0.0
    opacity: float | None = 1.0


@dataclass(kw_only=True)
class RuleMarkEncodings:
    """Select Altair rule mark encodings.

    Fields:
        x (pschm.PrimaryChannel): x-axis attributes
        color (str): rule color
    """

    x: pschm.PrimaryChannel
    color: str


@dataclass(kw_only=True)
class RuleMarkMu:
    """Select Altair "mu" (mean) rule mark attributes.

    Fields:
        encodings (pmrk.RuleMarkEncodings): rule mark encodings
        mu (float): mu value
    """

    encode: pmrk.RuleMarkEncodings = field(
        default_factory=lambda: RuleMarkEncodings(
            x=chrt.PrimaryChannel(shorthand=ChannelDescriptor.MU.value.shorthand),
            color=chrt.COLORS["amtk_red"],
        )
    )
    mu: float = 0.0


@dataclass(kw_only=True)
class RuleMarkSigma:
    """Select Altair "sigma" (standard deviation) rule mark attributes. The field
    < n > represents the number of desired standard deviation rule marks
    to include in the chart.

    Fields:
        encodings (pmrk.RuleMarkSigmaEncodings): rule mark encodings
        sigma (float): sigma value
        n (int): number of standard deviations
    """

    encode: pmrk.RuleMarkEncodings = field(
        default_factory=lambda: RuleMarkEncodings(
            x=chrt.PrimaryChannel(shorthand=ChannelDescriptor.SIGMA.value.shorthand),
            color=chrt.COLORS["anth_gray"],
        )
    )
    sigma: float = 1.0
    n: int = 1


@dataclass(kw_only=True)
class LayeredHistogramChart:
    """Select Altair histogram chart attributes. The < properties > attribute is
    initialized by the < __post_init__ > method.

    Fields:
        frame (pd.DataFrame): DataFrame
        title (str): chart title
        mark (pmrk.BarMarkProperties): bar mark properties
        encode (pchrt.LayeredHistogramChartEncodings): chart encodings
        mu_rule (pmrk.RuleMarkMu): mu rule attributes
        sigma_rule (pmrk.RuleMarkSigma): sigma rule attributes
        properties (pchrt.ChartProperties): chart properties
    """

    frame: pd.DataFrame
    title: str
    mark: pmrk.BarMarkProperties = field(default_factory=BarMarkProperties)
    encode: pchrt.LayeredHistogramChartEncodings = field(
        default_factory=LayeredHistogramChartEncodings
    )
    mu_rule: pmrk.RuleMarkMu = field(default_factory=RuleMarkMu)
    sigma_rules: pmrk.RuleMarkSigma = field(default_factory=RuleMarkSigma)
    properties: pchrt.ChartProperties = field(init=False)

    def __post_init__(self) -> None:
        self.properties = chrt.ChartProperties(height=300, width=600, padding=15, title=self.title)
