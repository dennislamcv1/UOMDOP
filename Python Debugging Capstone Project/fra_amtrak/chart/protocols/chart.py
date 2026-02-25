import fra_amtrak.chart.protocols.mark as pmrk
import fra_amtrak.chart.protocols.schema as pschm
import pandas as pd

from typing import Protocol, Sequence


class ChartEncodings(Protocol):
    """Select Altair boxplot chart encodings.

    Fields:
        x (pschm.PrimaryChannel): x-axis attributes
        y (pschm.PrimaryChannel): y-axis attributes
        color (pschm.Color): color attributes
        tooltip (Sequence[pschm.Tooltip]): tooltip attributes
    """

    x: pschm.PrimaryChannel
    y: pschm.PrimaryChannel
    color: pschm.Color
    tooltip: Sequence[pschm.Tooltip]


class ChartProperties(Protocol):
    """Select Altair top-level chart properties.

    Fields:
        height (float | None): chart height
        width (float | None): chart width
        padding (int | None): chart padding
        title (str | None): chart title
    """

    height: float | None
    width: float | None
    padding: int | None
    title: str | None


class ChartViewConfig(Protocol):
    """Select Altair view configuration attributes that control the visual feautures
    associated with a chart.

    Fields:
        stroke (str | None): stroke color
        stroke_dash (str | None): stroke dash pattern
        stroke_opacity (float | None): stroke opacity
        stroke_width (float | None): stroke width
    """

    stroke: str | None
    stroke_dash: str | None
    stroke_opacity: float | None
    stroke_width: float | None


class BoxplotChart(Protocol):
    """Select Altair boxplot chart attributes.

    Fields:
        frame (pd.DataFrame): DataFrame
        title (str): chart title
        mark (pmrk.BoxplotMarkProperties): boxplot mark properties
        encode (ChartEncodings): chart encodings
        config_view (ChartViewConfig): chart view configuration
        properties (ChartProperties): chart properties
    """

    frame: pd.DataFrame
    title: str
    mark: pmrk.BoxplotMarkProperties
    encode: ChartEncodings
    config_view: ChartViewConfig
    properties: ChartProperties


class BoxplotPreAggChart(Protocol):
    """Select Altair boxplot chart attributes (data preaggregated).

    Fields:
        frame (pd.DataFrame): DataFrame
        title (str): chart title
        mark (pmrk.BoxplotMarkProperties): boxplot mark properties
        encode (ChartEncodings): chart encodings
        median (pmrk.TickMarkProperties): median attributes
        outlier (pschm.PrimaryChannel): outlier attributes
    """

    frame: pd.DataFrame
    title: str
    mark: pmrk.BoxplotMarkProperties
    encode: ChartEncodings
    median: pmrk.TickMarkProperties
    outlier: pschm.PrimaryChannel
    properties: ChartProperties


class GrpBarChartEncodings(Protocol):
    """Select Altair grouped bar chart encodings.

    Fields:
        x (pschm.PrimaryChannel): x-axis attributes
        xoffset (pschm.PrimaryChannelOffset): x-offset attributes
        y (pschm.PrimaryChannel): y-axis attributes
        color (pschm.Color): color attributes
        tooltip (Sequence[pschm.Tooltip]): tooltip attributes
    """

    x: pschm.PrimaryChannel
    xoffset: pschm.PrimaryChannelOffset
    y: pschm.PrimaryChannel
    color: pschm.Color
    tooltip: Sequence[pschm.Tooltip]


class GrpBarChart(Protocol):
    """Select Altair grouped bar chart attributes.

    Fields:
        frame (pd.DataFrame): DataFrame
        title (str): chart title
        mark (pmrk.BarMarkProperties): bar mark properties
        encode (GrpBarChartEncodings): chart encodings
        config_view (ChartViewConfig): chart view configuration
        properties (ChartProperties): chart properties
    """

    frame: pd.DataFrame
    title: str
    mark: pmrk.BarMarkProperties
    encode: GrpBarChartEncodings
    config_view: ChartViewConfig
    properties: ChartProperties


class HistogramChartEncodings(Protocol):
    """Select Altair histogram chart encodings.

    Fields:
        x (pschm.PrimaryChannel): x-axis attributes
        y (pschm.PrimaryChannel): y-axis attributes
        color (str): color attributes
        tooltip (Sequence[pschm.Tooltip]): tooltip attributes
    """

    x: pschm.PrimaryChannel
    y: pschm.PrimaryChannel
    color: str  # -> alt.value()
    tooltip: Sequence[pschm.Tooltip]


class HistogramChart(Protocol):
    """Select Altair histogram chart attributes.

    Fields:
        frame (pd.DataFrame): DataFrame
        title (str): chart title
        mark (pmrk.BarMarkProperties): bar mark properties
        encode (HistogramChartEncodings): chart encodings
        mu_rule (pmrk.RuleMarkMu): mu rule attributes
        sigma_rule (pmrk.MRuleMarkSigma): sigma rule attributes
        properties (ChartProperties): chart properties
    """

    frame: pd.DataFrame
    title: str
    mark: pmrk.BarMarkProperties
    encode: HistogramChartEncodings
    mu_rule: pmrk.RuleMarkMu
    sigma_rules: pmrk.RuleMarkSigma
    properties: ChartProperties


class LayeredHistogramChartEncodings(Protocol):
    """Select Altair layered histogram chart encodings.

    Fields:
        x (pschm.PrimaryChannel): x-axis attributes
        x2 (pschm.SecondaryChannel): secondary x-axis attributes
        y (pschm.PrimaryChannel): y-axis attributes
        color (str): color attributes
        order (pschm.Order): order attributes
        tooltip (Sequence[pschm.Tooltip]): tooltip attributes
    """

    x: pschm.PrimaryChannel
    x2: pschm.SecondaryChannel
    y: pschm.PrimaryChannel
    color: pschm.Color
    order: pschm.Order
    tooltip: Sequence[pschm.Tooltip]


class LayeredHistogramChart(Protocol):
    """Select Altair layered histogram chart attributes.

    Fields:
        frame (pd.DataFrame): DataFrame
        title (str): chart title
        mark (pmrk.BarMarkProperties): bar mark properties
        encode (LayeredHistogramChartEncodings): chart encodings
        mu_rule (pmrk.RuleMarkMu): mu rule attributes
        sigma_rule (pmrk.MRuleMarkSigma): sigma rule attributes
        properties (ChartProperties): chart properties
    """

    frame: pd.DataFrame
    title: str
    mark: pmrk.BarMarkProperties
    encode: LayeredHistogramChartEncodings
    mu_rule: pmrk.RuleMarkMu
    sigma_rules: pmrk.RuleMarkSigma
    properties: ChartProperties


class LineChart(Protocol):
    """Select Altair line chart attributes. The < properties > attribute is
    initialized by the < __post_init__ > method.

    Fields:
        frame (pd.DataFrame): data frame for the chart
        title (str): title of the chart
        mark (pmrk.LineMarkProperties): line mark properties
        encode (ChartEncodings): chart encodings
        properties (ChartProperties): chart properties
    """

    frame: pd.DataFrame
    title: str
    mark: pmrk.LineMarkProperties
    encode: ChartEncodings
    properties: ChartProperties
