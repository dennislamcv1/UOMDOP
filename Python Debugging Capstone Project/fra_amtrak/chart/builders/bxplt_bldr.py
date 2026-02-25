import altair as alt
import fra_amtrak.chart.chart_types as typ
import fra_amtrak.chart.builders.bldr_helpers as bhlp
import fra_amtrak.chart.protocols.chart as pchrt
import fra_amtrak.chart.protocols.mark as pmrk
import fra_amtrak.chart.protocols.schema as pschm

from altair.utils.schemapi import Undefined
from typing import cast, Sequence


class BoxPlotBuilder:
    """Builder for creating an Altair boxplot chart.

    Attributes:
        _obj (Boxplot): Boxplot object containing chart attributes.

    Methods:
        x(...): Set x-axis attributes.
        y(...): Set y-axis attributes.
        color(...): Set color attributes.
        tooltip(...): Set tooltip for the chart.
        bxplt_mark_props(...): Set boxplot mark properties.
        chart_config_view(...): Set chart view configuration.
        chart_properties(...): Set chart properties.
        build() -> alt.Chart: Build and return the Altair chart.
    """

    def __init__(self, boxplot: pchrt.BoxplotChart) -> None:
        """Initialize the < BoxPlotBuilder > with a < Boxplot > object.

        Parameters:
            boxplot (pchrt.Boxplot): The boxplot object containing chart attributes.

        Returns:
            None
        """

        self._obj = boxplot

    def x(
        self,
        shorthand: str | None = None,
        axis_grid: bool | None = None,
        axis_title: str | None = None,
        scale_zero: bool | None = False,
    ) -> "BoxPlotBuilder":
        """Set x-axis attributes.

        Parameters:
            shorthand (str | None): The shorthand for the x-axis encoding.
            axis_grid (bool | None): Whether to display grid lines on the x-axis.
            axis_title (str | None): The title for the x-axis.
            scale_zero (bool | None): Whether to set the x-axis scale to zero.

        Returns:
            BoxPlotBuilder: The current builder instance.
        """

        x = self._obj.encode.x
        if shorthand is not None:
            x.shorthand = shorthand

        if any([axis_grid is not None, axis_title is not None]):
            if x.axis is None:
                raise ValueError("To assign < x.axis > attributes, the object must not be None.")
            if axis_grid is not None:
                x.axis.grid = axis_grid
            if axis_title is not None:
                x.axis.title = axis_title

        if x.scale is None:
            raise ValueError("To assign < x.scale > attributes, the object must not be None.")
        if x.scale.zero is not None:
            x.scale.zero = scale_zero

        return self

    def y(
        self,
        shorthand: str | None = None,
        axis_grid: bool | None = None,
        axis_title: str | None = None,
        sort: list[str] | None = None,
    ) -> "BoxPlotBuilder":
        """Set y-axis attributes.

        Parameters:
            shorthand (str | None): The shorthand for the y-axis encoding.
            axis_grid (bool | None): Whether to display grid lines on the y-axis.
            axis_title (str | None): The title for the y-axis.
            sort (list[str] | None): The sorting order for the y-axis values.

        Returns:
            BoxPlotBuilder: The current builder instance.
        """

        y = self._obj.encode.y
        if shorthand is not None:
            y.shorthand = shorthand

        if any([axis_grid is not None, axis_title is not None]):
            if y.axis is None:
                raise ValueError("To assign < y.axis > attributes, the object must not be None.")
            if axis_grid is not None:
                y.axis.grid = axis_grid
            if axis_title is not None:
                y.axis.title = axis_title

        if sort is not None:
            y.sort = sort

        return self

    def color(
        self,
        shorthand: str | None = None,
        scale_domain: list[float] | list[str] | None = None,
        scale_range: list[str] | None = None,
        title: str | None = None,
        disable_legend: bool = False,
    ) -> "BoxPlotBuilder":
        """Set color attributes.

        Parameters:
            shorthand (str): The shorthand for the color encoding.
            scale_domain (list[str] | None): The domain for the color scale.
            scale_range (list[str] | None): The range for the color scale.
            title (str | None): The title for the color encoding.
            disable_legend (bool): Whether to disable the legend for the color encoding.

        Returns:
            BoxPlotBuilder: The current builder instance.
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

    def tooltips(self, tooltips: Sequence[pschm.Tooltip]) -> "BoxPlotBuilder":
        """Set tooltips for the boxplot chart.

        Parameters:
            tooltips (Sequence[pschm.Tooltip]): A list of tooltip objects to be applied to the chart.

        Returns:
            BoxPlotBuilder: The current builder instance.
        """

        if self._obj.encode.tooltip is None:
            raise ValueError("To assign < tooltip > attributes, the object must not be None.")
        self._obj.encode.tooltip = tooltips

        return self

    def boxplot_mark_properties(
        self,
        extent: str | None = None,
        orient: typ.AltMarkOrient | None = None,
        size: int | None = None,
    ) -> "BoxPlotBuilder":
        """Set boxplot mark properties.

        Parameters:
            extent (str | None): The extent of the boxplot (e.g., "min-max").
            orient (typ.AltMarkOrient | None): The orientation of the boxplot (e.g., "vertical").
            size (int | None): The size of the boxplot.

        Returns:
            BoxPlotBuilder: The current builder instance.
        """

        mrk = self._obj.mark
        if mrk is None:
            raise ValueError("To assign < mark > attributes, the object must not be None.")
        if extent is not None:
            mrk.extent = extent
        if orient is not None:
            mrk.orient = orient
        if size is not None:
            mrk.size = size

        return self

    def chart_config_view(
        self,
        stroke: str | None = None,
        stroke_dash: str | None = None,
        stroke_opacity: float | None = None,
        stroke_width: float | None = None,
    ) -> "BoxPlotBuilder":
        """Set chart view configuration.

        Parameters:
            stroke (str | None): The stroke color for the chart view.
            stroke_dash (str | None): The stroke dash pattern for the chart view.
            stroke_opacity (float | None): The opacity of the stroke.
            stroke_width (float | None): The width of the stroke.

        Returns:
            BoxPlotBuilder: The current builder instance.
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
    ) -> "BoxPlotBuilder":
        """Set chart properties.
        Parameters:
            height (float | None): The height of the chart.
            width (float | None): The width of the chart.
            padding (int | None): The padding around the chart.
            title (str | None): The title of the chart.

        Returns:
            BoxPlotBuilder: The current builder instance.
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
        """Build and return the Altair boxplot chart. Note that the tooltips are applied to
        outlier marks only. Altair provides its own tooltips for each boxplot.

        Parameters:
            None

        Returns:
            alt.Chart: The constructed Altair chart object.
        """

        # Chart attributes
        enc: pchrt.ChartEncodings = self._obj.encode
        mrk: pmrk.BoxplotMarkProperties = self._obj.mark
        cvw: pchrt.ChartViewConfig = self._obj.config_view
        prp: pchrt.ChartProperties = self._obj.properties

        encodings = {
            "x": alt.X(
                shorthand=enc.x.shorthand,
                axis=alt.Axis(),
                scale=bhlp.build_scale(enc.x.scale),
            ),
            "y": alt.Y(
                shorthand=enc.y.shorthand,
                axis=bhlp.build_axis(enc.y.axis),
                sort=enc.y.sort,
            ),
            "color": bhlp.build_color(enc.color),
            "tooltip": bhlp.create_tooltips(enc.tooltip),
        }

        chart: alt.Chart = (
            alt.Chart(self._obj.frame)
            .mark_boxplot(size=cast(typ.AltMarkSize, mrk.size if mrk.size is not None else Undefined))
            .encode(**encodings)
            .configure_view(stroke=cvw.stroke, strokeWidth=cvw.stroke_width)
            .properties(height=prp.height, width=prp.width, padding=prp.padding, title=prp.title)
        )

        return chart
