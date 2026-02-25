import altair as alt
import fra_amtrak.chart.chart_types as typ
import fra_amtrak.chart.builders.bldr_helpers as bhlp
import fra_amtrak.chart.protocols.chart as pchrt
import fra_amtrak.chart.protocols.mark as pmrk
import fra_amtrak.chart.protocols.schema as pschm

from typing import Sequence


class LineChartBuilder:
    """Builder for creating an Altair line chart.

    Attributes:
        _obj (Line): line object containing chart attributes.
        _interpolate (bool): whether to interpolate the line chart.


    Methods:
        x(...): Set x-axis attributes.
        y(...): Set y-axis attributes.
        color(...): Set color attributes.
        tooltip(...): Set tooltip for the chart.
        line_mark_props(...): Set line mark properties.
        chart_properties(...): Set chart properties.
        build() -> alt.Chart: Build and return the Altair chart.
    """

    def __init__(self, line: pchrt.LineChart, interpolate: bool = False) -> None:
        """Initialize the < LineChartBuilder > with a < LineChart > object.

        Parameters:
            line (pchrt.LineChart): The line chart object containing chart attributes.
            interpolate (bool): Whether to interpolate the line chart. Defaults to False.

        Returns:
            None
        """

        self._obj = line
        self._interpolate = interpolate

    def x(
        self,
        shorthand: str | None = None,
        axix_grid: bool | None = None,
        axis_label_angle: float | None = None,
        axis_title: str | None = None,
        sort: list[str] | None = None,
    ) -> "LineChartBuilder":
        """Set x-axis attributes.

        Parameters:
            shorthand (str): The shorthand for the x-axis encoding.
            axix_grid (bool | None): Whether to show grid lines on the x-axis.
            axis_title (str | None): The title for the x-axis.
            sort (list[str] | None): The sorting order for the x-axis values.

        Returns:
            LineChartBuilder: The current builder instance.
        """

        x = self._obj.encode.x
        if shorthand is not None:
            x.shorthand = shorthand

        if any([
            axix_grid is not None,
            axis_label_angle is not None,
            axis_title is not None
        ]):
            if x.axis is None:
                raise ValueError("To assign < x.axis > attributes, the object must not be None.")
            if axix_grid is not None:
                x.axis.grid = axix_grid
            if axis_label_angle is not None:
                x.axis.label_angle = axis_label_angle
            if axis_title is not None:
                x.axis.title = axis_title

        if x.sort is not None:
            x.sort = sort

        return self

    def y(
        self,
        shorthand: str | None = None,
        axis_grid: bool | None = None,
        axis_tick_count_max: int | None = None,
        axis_title: str | None = None,
        axis_values: typ.AltAxisValues | None = None,
    ) -> "LineChartBuilder":
        """Set y-axis attributes.

        Parameters:
            shorthand (str): The shorthand for the y-axis encoding.
            axis_grid (bool | None): Whether to show grid lines on the y-axis.
            axis_tick_count_max (int | None): Maximum number of ticks on the y-axis.
            axis_title (str | None): The title for the y-axis.
            axis_values (typ.AltAxisValues | None): Specific values to display on the y-axis.

        Returns:
            LineChartBuilder: The current builder instance.
        """

        y = self._obj.encode.y
        if shorthand is not None:
            y.shorthand = shorthand

        if any([
            axis_grid is not None,
            axis_tick_count_max is not None,
            axis_title is not None,
            axis_values is not None,
        ]):
            if y.axis is None:
                raise ValueError("To assign < y.axis > attributes, the object must not be None.")
            if axis_grid is not None:
                y.axis.grid = axis_grid
            if axis_tick_count_max is not None:
                y.axis.tick_count = axis_tick_count_max
            if axis_title is not None:
                y.axis.title = axis_title
            if axis_values is not None:
                y.axis.values = axis_values

        return self

    def color(
        self,
        shorthand: str | None = None,
        scale_domain: list[float] | list[str] | None = None,
        scale_range: list[str] | None = None,
        title: str | None = None,
        disable_legend: bool = False,
    ) -> "LineChartBuilder":
        """Set color attributes.

        Parameters:
            shorthand (str): The shorthand for the color encoding.
            scale_domain (list[str] | None): The domain for the color scale.
            scale_range (list[str] | None): The range for the color scale.
            title (str | None): The title for the color encoding.
            disable_legend (bool): Whether to disable the legend for the color encoding.

        Returns:
            LineChartBuilder: The current builder instance.
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

    def tooltips(
        self,
        tooltips: Sequence[pschm.Tooltip],
    ) -> "LineChartBuilder":
        """Set tooltips.

        Parameters:
            tooltips (Sequence[pschm.Tooltip]): A list of Tooltip objects containing tooltip
                     attributes such as shorthand, title, format, and format_type.

        Returns:
            LineChartBuilder: The current builder instance.
        """

        if self._obj.encode.tooltip is None:
            raise ValueError("To assign < tooltip > attributes, the object must not be None.")
        self._obj.encode.tooltip = tooltips

        return self

    def line_mark_properties(
        self,
        point: bool = True,
        stroke_dash: list[int] | None = None,
    ) -> "LineChartBuilder":
        """Set line mark properties.

        Parameters:
            point (bool): Whether to show points on the line chart.
            stroke_dash (list[int] | None): The stroke dash pattern for the line.

        Returns:
            LineChartBuilder: The current builder instance.
        """

        mrk = self._obj.mark
        if mrk is None:
            raise ValueError("To assign < mark > attributes, the object must not be None.")
        mrk.point = point
        if stroke_dash is not None:
            mrk.stroke_dash = stroke_dash

        return self

    def chart_properties(
        self,
        height: float | None = None,
        width: float | None = None,
        padding: int | None = None,
        title: str | None = None,
    ) -> "LineChartBuilder":
        """Set top-level properties.

        Parameters:
            height (float | None): The height of the chart.
            width (float | None): The width of the chart.
            padding (int | None): The padding around the chart.
            title (str | None): The title of the chart.

        Returns:
            LineChartBuilder: The current builder instance.
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
        """Build and return the Altair line chart.

        Parameters:
            None

        Returns:
            alt.Chart: The constructed Altair chart object.
        """

        # Chart attributes
        enc: pchrt.ChartEncodings = self._obj.encode
        mrk: pmrk.LineMarkProperties = self._obj.mark
        prp: pchrt.ChartProperties = self._obj.properties

        encodings = {
            "x": alt.X(
                shorthand=enc.x.shorthand,
                axis=bhlp.build_axis(enc.x.axis),
                sort=enc.x.sort,
            ),
            "y": alt.Y(
                shorthand=enc.y.shorthand,
                axis=bhlp.build_axis(enc.y.axis),
                scale=bhlp.build_scale(enc.y.scale),
            ),
            "color": bhlp.build_color(enc.color),
            "tooltip": bhlp.create_tooltips(enc.tooltip),
        }

        line_chrt = alt.Chart(self._obj.frame).mark_line(point=mrk.point).encode(**encodings)

        # Hack: copy DataFrame; estimate missing values using linear interpolation
        if self._interpolate:
            line_interp = self._obj.frame.copy()
            line_interp["Late Detraining Customers Avg Min Late mean"] = (
                self._obj.frame.groupby("Train Number")[
                    "Late Detraining Customers Avg Min Late mean"
                ]
                .apply(lambda group: group.interpolate())
                .reset_index(drop=True)
            )

            line_interp_chrt = (
                alt.Chart(line_interp)
                .mark_line(point=False, strokeDash=mrk.stroke_dash)
                .encode(**encodings)
            )

            return alt.layer(line_chrt, line_interp_chrt).properties(
                height=prp.height, width=prp.width, padding=prp.padding, title=prp.title
            )

        layer_chrt = alt.layer(line_chrt).properties(
            height=prp.height, width=prp.width, padding=prp.padding, title=prp.title
        )

        return layer_chrt
