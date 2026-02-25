import altair as alt
import fra_amtrak.chart.chart_types as typ
import fra_amtrak.chart.builders.bldr_helpers as bhlp
import fra_amtrak.chart.protocols.chart as pchrt
import fra_amtrak.chart.protocols.schema as pschm

from typing import Sequence


class GrpBarBuilder:
    """Builder for creating an Altair grouped bar chart.

    Attributes:
        _obj (GrpBarChart): GrpBarChart object containing chart attributes.

    Methods:
        x(...): Set x-axis attributes.
        y(...): Set y-axis attributes.
        color(...): Set color attributes.
        tooltip(...): Set tooltip for the chart.
        grp_bar plot mark properties.
        chart_config_view(...): Set chart view configuration.
        chart_properties(...): Set chart properties.
        build() -> alt.Chart: Build and return the Altair chart.
    """

    def __init__(self, grp_bar: pchrt.GrpBarChart) -> None:
        """Initialize the < GrpBarBuilder > with a < GrpBarChart > object.

        Parameters:
            grp_bar (pchrt.GrpBarChart): The grouped bar chart object containing chart attributes

        Returns:
            None
        """

        self._obj = grp_bar

    def x(
        self,
        shorthand: str | None = None,
        axis_grid: bool | None = None,
        axis_label_angle: float | None = None,
        axis_label_font_weight: typ.AltFontWeight | None = None,
        axis_label_padding: float | None = None,
        axis_title: str | None = None,
        axis_title_font_size: float | None = None,
        axis_title_font_weight: typ.AltFontWeight | None = None,
    ) -> "GrpBarBuilder":
        """Set x-axis attributes.

        Parameters:
            shorthand (str | None): The shorthand for the x-axis encoding.
            axis_grid (bool | None): Whether to show grid lines for the x-axis.
            axis_label_angle (float | None): The angle of the x-axis labels.
            axis_label_font_weight (int | None): The font weight of the x-axis labels.
            axis_label_padding (float | None): The padding for the x-axis labels.
            axis_title (str | None): The title for the x-axis.
            axis_title_font_size (float | None): The font size of the x-axis title.
            axis_title_font_weight (int | None): The font weight of the x-axis title.

        Returns:
            GrpBarBuilder: The current builder instance.
        """

        x = self._obj.encode.x
        if shorthand is not None:
            x.shorthand = shorthand

        if any([
            axis_grid is not None,
            axis_label_angle is not None,
            axis_label_font_weight is not None,
            axis_label_padding is not None,
            axis_title is not None,
            axis_title_font_size is not None,
            axis_title_font_weight is not None,
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
            if axis_title is not None:
                x.axis.title = axis_title
            if axis_title_font_size is not None:
                x.axis.title_font_size = axis_title_font_size
            if axis_title_font_weight is not None:
                x.axis.title_font_weight = axis_title_font_weight

        return self

    def xoffset(
        self,
        shorthand: str | None = None,
        sort: list[str] | None = None,
        title: str | None = None,
    ) -> "GrpBarBuilder":
        """Set x-offset attributes.

        Parameters:
            shorthand (str | None): The shorthand for the x-offset encoding.
            sort (list[str] | None): The sorting order for the x-offset values.
            title (str | None): The title for the x-offset.

        Returns:
            GrpBarBuilder: The current builder instance.
        """

        xoffset = self._obj.encode.xoffset
        if xoffset is None:
            raise ValueError("To assign < xoffset > attributes, the object must not be None.")
        if shorthand is not None:
            xoffset.shorthand = shorthand
        if sort is not None:
            xoffset.sort = sort
        if title is not None:
            xoffset.title = title

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
    ) -> "GrpBarBuilder":
        """Set y-axis attributes.

        Parameters:
            shorthand (str | None): The shorthand for the y-axis encoding.
            axis_grid (bool | None): Whether to show grid lines for the y-axis.
            axis_label_angle (float | None): The angle of the y-axis labels.
            axis_label_font_weight (int | None): The font weight of the y-axis labels.
            axis_label_padding (float | None): The padding for the y-axis labels.
            axis_title (str | None): The title for the y-axis.
            axis_title_font_size (float | None): The font size of the y-axis title.
            axis_title_font_weight (int | None): The font weight of the y-axis title.

        Returns:
            GrpBarBuilder: The current builder instance.
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

        return self

    def color(
        self,
        shorthand: str | None = None,
        scale_domain: list[float] | list[str] | None = None,
        scale_range: list[str] | None = None,
        title: str | None = None,
        disable_legend: bool = False,
    ) -> "GrpBarBuilder":
        """Set color attributes.

        Parameters:
            shorthand (str): The shorthand for the color encoding.
            scale_domain (list[str] | None): The domain for the color scale.
            scale_range (list[str] | None): The range for the color scale.
            title (str | None): The title for the color encoding.
            disable_legend (bool): Whether to disable the legend for the color encoding.

        Returns:
            GrpBarBuilder: The current builder instance.
        """

        color = self._obj.encode.color
        if color is None:
            raise ValueError("To assign < color > attributes, the object must not be None.")
        if shorthand is not None:
            color.shorthand = shorthand

        if any([scale_domain is not None, scale_range is not None]):
            if color.scale is None:
                raise ValueError(
                    "To assign < color.scale > attributes, the object must not be None."
                )
            if scale_domain is not None:
                color.scale.domain = scale_domain
            if scale_range is not None:
                color.scale.range_ = scale_range

        if title is not None:
            color.title = title
        color.disable_legend = disable_legend

        return self

    def tooltips(self, tooltips: Sequence[pschm.Tooltip]) -> "GrpBarBuilder":
        """Set tooltip for the chart.

        Parameters:
            tooltips (Sequence[pschm.Tooltip]): A list of Tooltip objects containing tooltip
                attributes such as shorthand, title, format, and format_type.

        Returns:
            GrpBarBuilder: The current builder instance.
        """

        if self._obj.encode.tooltip is None:
            raise ValueError("To assign < tooltip > attributes, the object must not be None.")
        self._obj.encode.tooltip = tooltips

        return self

    def chart_config_view(
        self,
        stroke: str | None = None,
        stroke_dash: str | None = None,
        stroke_opacity: float | None = None,
        stroke_width: float | None = None,
    ) -> "GrpBarBuilder":
        """Set chart view configuration.

        Parameters:
            stroke (str | None): The stroke color for the chart view.
            stroke_dash (str | None): The stroke dash pattern for the chart view.
            stroke_opacity (float | None): The opacity of the stroke for the chart view.
            stroke_width (float | None): The width of the stroke for the chart view.

        Returns:
            GrpBarBuilder: The current builder instance.
        """

        cvw = self._obj.config_view
        if cvw is None:
            raise ValueError("To assign < config_view > attributes, the object must not be None.")
        if stroke is not None:
            cvw.stroke = stroke
        if stroke_dash is not None:
            cvw.stroke_dash = stroke_dash
        if stroke_opacity is not None:
            cvw.stroke_opacity = stroke_opacity
        if stroke_width is not None:
            cvw.stroke_width = stroke_width

        return self

    def chart_properties(
        self,
        height: float | None = None,
        width: float | None = None,
        padding: int | None = None,
        title: str | None = None,
    ) -> "GrpBarBuilder":
        """Set top-level properties for the chart.

        Parameters:
            height (float | None): The height of the chart.
            width (float | None): The width of the chart.
            padding (int | None): The padding around the chart.
            title (str | None): The title of the chart.

        Returns:
            GrpBarBuilder: The current builder instance.
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

    def build(self) -> alt.Chart:
        """Build and return the Altair grouped bar chart.

        Parameters:
            None

        Returns:
            alt.Chart: The constructed Altair chart object.
        """

        # Chart attributes
        enc: pchrt.GrpBarChartEncodings = self._obj.encode
        cvw: pchrt.ChartViewConfig = self._obj.config_view
        prp: pchrt.ChartProperties = self._obj.properties

        encodings = {
            "x": alt.X(shorthand=enc.x.shorthand, axis=bhlp.build_axis(enc.x.axis)),
            "y": alt.Y(shorthand=enc.y.shorthand, axis=bhlp.build_axis(enc.y.axis)),
            "xOffset": alt.XOffset(
                shorthand=enc.xoffset.shorthand,
                sort=enc.xoffset.sort,
                title=enc.xoffset.title,
            ),
            "color": bhlp.build_color(enc.color),
            "tooltip": bhlp.create_tooltips(enc.tooltip),
        }

        chart: alt.Chart = (
            alt.Chart(self._obj.frame)
            .mark_bar()
            .encode(**encodings)
            .configure_view(stroke=cvw.stroke, strokeWidth=cvw.stroke_width)
            .properties(height=prp.height, width=prp.width, padding=prp.padding, title=prp.title)
        )

        return chart
