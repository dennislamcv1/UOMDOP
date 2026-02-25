import fra_amtrak.chart.chart_types as typ
import fra_amtrak.chart.protocols.schema as pschm

from typing import Protocol


class BarMarkProperties(Protocol):
    """Select Altair bar mark attributes.

    Fields:
        bin_spacing (float | None): bin spacing
        opacity (float | None): bar opacity
    """

    bin_spacing: float | None
    opacity: float | None


class BoxplotMarkProperties(Protocol):
    """Select Altair boxplot mark attributes.

    Fields:
        extent (str | None): extent of the boxplot
        orient (typ.AltMarkOrient | None): orientation of the boxplot
        size (float | None): size of the boxplot
    """

    extent: str | None
    orient: typ.AltMarkOrient | None
    size: float | None

class LineMarkProperties(Protocol):
    """Select Altair line mark attributes.

    Fields:
        point (bool | None): whether to display points on the line chart
        stroke_dash (list[int] | None): stroke dash pattern for the line
    """

    point: bool | None
    stroke_dash: list[int] | None


class RuleMarkEncodings(Protocol):
    """Select Altair rule mark encodings.

    Fields:
        x (RuleMarkMuX): x-axis
        color (str): rule color
    """

    x: pschm.PrimaryChannel
    color: str


class RuleMarkMu(Protocol):
    """Select Altair "mu" (mean) rule mark attributes.

    Fields:
        encodings (RuleMarkMuEncodings): rule mark encodings
        mu (float): mu value
    """

    encode: RuleMarkEncodings
    mu: float


class RuleMarkSigma(Protocol):
    """Select Altair "sigma" (standard deviation) rule mark attributes. The field
    < n > represents the number of desired standard deviation rule marks
    to include in the chart.

    Fields:
        encodings (RuleMarkSigmaEncodings): rule mark encodings
        sigma (float): sigma value
        n (int): number of standard deviations
    """

    encode: RuleMarkEncodings
    sigma: float
    n: int


class TickMarkProperties(Protocol):
    """Select Altair tick mark attributes.

    Fields:
        color (str | None): tick color
        size (float | None): tick size
    """

    color: str | None
    size: float | None
