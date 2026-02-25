import altair as alt
import fra_amtrak.chart.chart_types as typ
import fra_amtrak.chart.builders.bldr_helpers as bhlp
import fra_amtrak.chart.protocols.chart as pchrt
import fra_amtrak.chart.protocols.mark as pmrk
import fra_amtrak.chart.protocols.schema as pschm

from altair.utils.schemapi import Undefined
from typing import cast, Sequence


class HistogramBuilder:
    """Builder class for creating a histogram chart using Altair.

    Attributes:
        _obj (pchrt.Histogram): Histogram object containing chart attributes.

    Methods:
        x(...): Set x-axis attributes.
        y(...): Set y-axis attributes.
        tooltips(...): Set tooltip attributes.
        bar_mark_properties(...): Set bar mark properties.
        mu_rule(...): Set mu rule attributes.
        sigma_rules(...): Set sigma rule attributes.
        chart_properties(...): Set chart properties.
        build(): Compile and return the configured Vega-Altair histogram chart.
    """

    def __init__(self, histogram: pchrt.HistogramChart) -> None:
        """Initialize the < HistogramBuilder > with a < Histogram > object.

        Parameters:
            histogram (pchrt.HistogramChart): Histogram object containing chart attributes.

        Returns:
            None
        """

        self._obj = histogram

    def x(
        self,
        shorthand: str | None = None,
        axis_grid: bool | None = None,
        axis_label_angle: float | None = None,
        axis_label_font_weight: typ.AltFontWeight | None = None,
        axis_label_padding: float | None = None,
        axis_tick_count: typ.AltTickCount | None = None,
        axis_title: str | None = None,
        axis_title_font_size: float | None = None,
        axis_title_font_weight: typ.AltFontWeight | None = None,
        axis_values: typ.AltAxisValues | None = None,
        bin_max_bins: float | None = None,
        bin_step: float | None = None,
        scale_domain: list[float] | list[str] | None = None,
    ) -> "HistogramBuilder":
        """Set x-axis attributes.

        Parameters:
            shorthand (str | None): The shorthand for the x-axis encoding.
            axis_grid (bool | None): Whether to show grid lines on the x-axis.
            axis_label_angle (float | None): Angle of the x-axis labels.
            axis_label_font_weight (typ.AltFontWeight | None): Font weight of the x-axis labels.
            axis_label_padding (float | None): Padding for the x-axis labels.
            axis_tick_count (typ.AltTickCount | None): Number of ticks on the x-axis.
            axis_title (str | None): Title for the x-axis.
            axis_title_font_size (float | None): Font size of the x-axis title.
            axis_title_font_weight (typ.AltFontWeight | None): Font weight of the x-axis title.
            axis_values (typ.AltAxisValues | None): Specific values to display on the x-axis.
            bin_max_bins (float | None): Maximum number of bins for the x-axis.
            bin_step (float | None): Step size for the x-axis bins.
            scale_domain (list[float] | None): Domain for the x-axis scale.

        Returns:
            HistogramBuilder: The current builder instance.
        """

        x = self._obj.encode.x
        if shorthand is not None:
            x.shorthand = shorthand

        if any([
            axis_grid is not None,
            axis_label_angle is not None,
            axis_label_font_weight is not None,
            axis_label_padding is not None,
            axis_tick_count is not None,
            axis_title is not None,
            axis_title_font_size is not None,
            axis_title_font_weight is not None,
            axis_values is not None,
        ]):
            if x.axis is None:
                raise ValueError("To assign < x.axis > attributes, the object must not be None.")
            if axis_grid is not None:
                x.axis.grid = axis_grid
            if axis_label_angle is not None:
                x.axis.label_angle = axis_label_angle
            if axis_label_font_weight is not None:
                x.axis.label_font_weight = axis_label_font_weight
            if axis_label_padding is not None:
                x.axis.label_padding = axis_label_padding
            if axis_tick_count is not None:
                x.axis.tick_count = axis_tick_count
            if axis_title is not None:
                x.axis.title = axis_title
            if axis_title_font_size is not None:
                x.axis.title_font_size = axis_title_font_size
            if axis_title_font_weight is not None:
                x.axis.title_font_weight = axis_title_font_weight
            if axis_values is not None:
                x.axis.values = axis_values

        bin_params = cast(pschm.BinParams, x.bin)  # mypy friendly cast
        if bin_params is None:
            raise ValueError("To assign < x.bin > attributes, the object must not be None.")
        if bin_max_bins is not None:
            bin_params.max_bins = bin_max_bins
        if bin_step is not None:
            bin_params.step = bin_step

        if x.scale is None:
            raise ValueError("To assign < x.scale > attributes, the object must not be None.")
        if scale_domain is not None:
            x.scale.domain = scale_domain

        return self

    def y(
        self,
        shorthand: str | None = None,
        axis_grid: bool | None = None,
        axis_label_angle: float | None = None,
        axis_label_font_weight: typ.AltFontWeight | None = None,
        axis_label_padding: float | None = None,
        axis_title: str | None = None,
        axis_title_font_size: float | None = None,
        axis_title_font_weight: typ.AltFontWeight | None = None,
        stack: bool = False,
    ) -> "HistogramBuilder":
        """Set y-axis attributes.

        Parameters:
            shorthand (str | None): The shorthand for the y-axis encoding.
            axis_grid (bool | None): Whether to show grid lines on the y-axis.
            axis_label_angle (float | None): Angle of the y-axis labels.
            axis_label_font_weight (int | None): Font weight of the y-axis labels.
            axis_label_padding (float | None): Padding for the y-axis labels.
            axis_title (str | None): Title for the y-axis.
            axis_title_font_size (float | None): Font size of the y-axis title.
            axis_title_font_weight (int | None): Font weight of the y-axis title.
            stack (bool): Whether to stack the y-axis values.

        Returns:
            HistogramBuilder: The current builder instance.
        """

        y = self._obj.encode.y
        if shorthand is not None:
            y.shorthand = shorthand

        if any([
            axis_grid is not None,
            axis_label_angle is not None,
            axis_label_font_weight is not None,
            axis_label_padding is not None,
            axis_title is not None,
            axis_title_font_size is not None,
            axis_title_font_weight is not None,
        ]):
            if y.axis is None:
                raise ValueError("To assign < y.axis > attributes, the object must not be None.")
            if axis_grid is not None:
                y.axis.grid = axis_grid
            if axis_label_angle is not None:
                y.axis.label_angle = axis_label_angle
            if axis_label_font_weight is not None:
                y.axis.label_font_weight = axis_label_font_weight
            if axis_label_padding is not None:
                y.axis.label_padding = axis_label_padding
            if axis_title is not None:
                y.axis.title = axis_title
            if axis_title_font_size is not None:
                y.axis.title_font_size = axis_title_font_size
            if axis_title_font_weight is not None:
                y.axis.title_font_weight = axis_title_font_weight
        y.stack = stack
        return self

    def color(self, value: str) -> "HistogramBuilder":
        """Set color attribute for histogram bars.

        Parameters:
            value (str): The color value for the histogram bars.

        Returns:
            HistogramBuilder: The current builder instance.
        """

        if self._obj.encode.color is None:
            raise ValueError("To assign < color > attribute, the object must not be None.")
        self._obj.encode.color = value

        return self

    def tooltips(self, tooltips: Sequence[pschm.Tooltip]) -> "HistogramBuilder":
        """Set tooltip attributes.

        Parameters:
            tooltips (Sequence[pschm.Tooltip]): List of tooltip attributes.

        Returns:
            HistogramBuilder: The current builder instance.
        """

        if self._obj.encode.tooltip is None:
            raise ValueError("To assign < tooltip > attributes, the object must not be None.")
        self._obj.encode.tooltip = tooltips

        return self

    def bar_mark_properties(
        self,
        bin_spacing: float | None = None,
        opacity: float | None = None,
    ) -> "HistogramBuilder":
        """Set bar mark properties.

        Parameters:
            bin_spacing (float | None): Spacing between histogram bins.
            opacity (float | None): Opacity of the histogram bars.

        Returns:
            HistogramBuilder: The current builder instance.
        """

        mrk = self._obj.mark
        if mrk is None:
            raise ValueError("To assign < mark > attributes, the object must not be None.")
        if bin_spacing is not None:
            mrk.bin_spacing = bin_spacing
        if opacity is not None:
            mrk.opacity = opacity

        return self

    def mu_rule(
        self,
        shorthand: str | None = None,
        color: str | None = None,
        mu: float | None = None,
    ) -> "HistogramBuilder":
        """Set mu rule attributes.

        Parameters:
            shorthand (str | None): The shorthand for the mu rule encoding.
            color (str | None): Color of the mu rule line.
            mu (float | None): The mu value for the rule line.

        Returns:
            HistogramBuilder: The current builder instance.
        """

        mu_rule = self._obj.mu_rule
        if mu_rule is None:
            raise ValueError("To assign < mu_rule > attributes, the object must not be None.")
        if shorthand is not None:
            mu_rule.encode.x.shorthand = shorthand
        if color is not None:
            mu_rule.encode.color = color
        if mu is not None:
            mu_rule.mu = mu

        return self

    def sigma_rules(
        self,
        shorthand: str | None = None,
        color: str | None = None,
        sigma: float = 1.0,
        n: int = 1,
    ) -> "HistogramBuilder":
        """Set sigma rule attributes for the histogram. Auto extends scale domain if required.

        Parameters:
            shorthand (str | None): The shorthand for the sigma rule encoding.
            color (str | None): Color of the sigma rule lines.
            sigma (float | None): The sigma value for the sigma rules.
            n (int): The number of standard deviations to include in the sigma rules.

        Returns:
            HistogramBuilder: The current builder instance.
        """

        sigma_rules = self._obj.sigma_rules
        if sigma_rules is None:
            raise ValueError("To assign < sigma_rules > attributes, the object must not be None.")
        if shorthand is not None:
            sigma_rules.encode.x.shorthand = shorthand
        if color is not None:
            sigma_rules.encode.color = color
        sigma_rules.sigma = sigma
        sigma_rules.n = n

        mu_rule = self._obj.mu_rule
        if mu_rule is None:
            raise ValueError("To assign < mu_rule > attributes, the object must not be None.")
        sigma_pos = mu_rule.mu + n * sigma
        sigma_neg = mu_rule.mu - n * sigma

        # Auto extend
        scale = self._obj.encode.x.scale
        if scale is None:
            raise ValueError("To assign < x.scale > attributes, the object must not be None.")
        if scale.domain is None:
            raise ValueError(
                "To assign < x.scale.domain > attributes, the object must not be None."
            )
        domain_min, domain_max = scale.domain
        if isinstance(domain_min, float) and isinstance(domain_max, float):
            if sigma_neg < domain_min or sigma_pos > domain_max:
                scale.domain = [min(sigma_neg, domain_min), max(sigma_pos, domain_max)]
        else:
            raise ValueError("The < x.scale.domain > must be a list of two float values.")

        return self

    def chart_properties(
        self,
        height: float | None = None,
        width: float | None = None,
        padding: int | None = None,
        title: str | None = None,
    ) -> "HistogramBuilder":
        """Set chart properties.

        Parameters:
            height (float | None): Height of the chart.
            width (float | None): Width of the chart.
            padding (int | None): Padding around the chart.
            title (str | None): Title of the chart.

        Returns:
            HistogramBuilder: The current builder instance.
        """

        prp = self._obj.properties
        if prp is None:
            raise ValueError(
                "To assign chart < properties > attributes, the object must not be None."
            )
        if height is not None:
            prp.height = height
        if width is not None:
            prp.width = width
        if padding is not None:
            prp.padding = padding
        if title:
            prp.title = title

        return self

    def build(self) -> alt.LayerChart:
        """Compile and return the configured Vega-Altair histogram chart.

        Parameters:
            None

        Returns:
            alt.LayerChart: The constructed Altair chart object.
        """

        # Chart attributes
        enc: pchrt.HistogramChartEncodings = self._obj.encode
        if enc.x.bin is None:
            raise ValueError("To assign < x.bin > attributes, the object must not be None.")
        x_bin = cast(pschm.BinParams, enc.x.bin)
        if enc.x.scale is None:
            raise ValueError("To assign < x.scale > attributes, the object must not be None.")
        x_scale: pschm.Scale = enc.x.scale
        mrk: pmrk.BarMarkProperties = self._obj.mark
        mu_rule: pmrk.RuleMarkMu = self._obj.mu_rule
        sigma_rules: pmrk.RuleMarkSigma = self._obj.sigma_rules
        prp: pchrt.ChartProperties = self._obj.properties

        # Extend domain to include sigma lines; ensure it is at least as wide as the original domain
        # Calculate extended domain to include sigma lines if necessary.
        max_sigma = sigma_rules.n * sigma_rules.sigma
        sigma_min = mu_rule.mu - max_sigma
        sigma_max = mu_rule.mu + max_sigma

        # Clamp left edge at 0 to preserve left alignment (origin at 0)
        if x_scale.domain is None:
            raise ValueError(
                "To assign < x.scale.domain > attributes, the object must not be None."
            )
        domain_min = float(0.0 if sigma_min < 0.0 else sigma_min)
        domain_max = float(max(sigma_max, x_scale.domain[1]))
        enc.x.scale.domain = [domain_min, domain_max]  # Adjust x-axis scale domain

        # Encodings
        encodings = {
            "x": alt.X(
                shorthand=enc.x.shorthand,
                axis=bhlp.build_axis(enc.x.axis),
                bin=alt.Bin(
                    maxbins=x_bin.max_bins if x_bin.max_bins is not None else Undefined,
                    step=x_bin.step if x_bin.step is not None else Undefined,
                ),
                scale=bhlp.build_scale(enc.x.scale),
            ),
            "y": alt.Y(
                shorthand=enc.y.shorthand,
                axis=bhlp.build_axis(enc.y.axis),
                stack=enc.y.stack,
            ),
            "color": bhlp.build_color(enc.color),
            "tooltip": bhlp.create_tooltips(enc.tooltip),
        }

        # Bar chart
        bar_layer = (
            alt.Chart(self._obj.frame)
            .mark_bar(
                binSpacing=mrk.bin_spacing if mrk.bin_spacing is not None else Undefined,
                opacity=mrk.opacity if mrk.opacity is not None else Undefined,
            )
            .encode(**encodings)
        )

        # mu rule
        mu_rule_layer = (
            alt.Chart(self._obj.frame.head(1))
            .transform_calculate(mu_x=str(mu_rule.mu))
            .mark_rule()
            .encode(
                x=alt.X(shorthand=mu_rule.encode.x.shorthand), color=alt.value(mu_rule.encode.color)
            )
        )

        # sigma rules
        sigma_rule_layers = bhlp.create_sigma_rules(
            frame=self._obj.frame,
            mu_rule_mu=mu_rule.mu,
            sigma_rule_sigma=sigma_rules.sigma,
            sigma_rule_n=sigma_rules.n,
            sigma_rule_color=sigma_rules.encode.color,
        )

        layer_chart = alt.layer(bar_layer, mu_rule_layer, *sigma_rule_layers).properties(
            height=prp.height, width=prp.width, padding=prp.padding, title=prp.title
        )

        return layer_chart
