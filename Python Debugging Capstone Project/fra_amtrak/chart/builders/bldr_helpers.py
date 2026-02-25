import altair as alt
import fra_amtrak.chart.chart as chrt
import fra_amtrak.chart.chart_types as typ
import fra_amtrak.chart.protocols.chart as pchrt
import fra_amtrak.chart.protocols.schema as pschm
import pandas as pd

from altair.utils.schemapi import Undefined, UndefinedType
from typing import Any, Sequence, cast


def build_axis(axis: pschm.Axis | None) -> alt.Axis | UndefinedType:
    """Build Altair axis from the provided axis configuration.

    Parameters:
        axis (pschm.Axis | None): Axis configuration to build.

    Returns:
        alt.Axis | None: Altair axis or None if no axis is provided.
    """

    if axis is None:
        return Undefined

    return alt.Axis(
        labelAngle=axis.label_angle if axis.label_angle is not None else Undefined,
        labelFontWeight=cast(
            typ.AltFontWeight,
            axis.label_font_weight if axis.label_font_weight is not None else Undefined,
        ),
        labelPadding=axis.label_padding if axis.label_padding is not None else Undefined,
        tickCount=cast(
            typ.AltTickCount, axis.tick_count if axis.tick_count not in (None, 0) else Undefined
        ),
        title=axis.title if axis.title is not None else Undefined,
        titleFontSize=axis.title_font_size if axis.title_font_size is not None else Undefined,
        titleFontWeight=cast(
            typ.AltFontWeight,
            axis.title_font_weight if axis.title_font_weight is not None else Undefined,
        ),
        grid=axis.grid if axis.grid is not None else Undefined,
        values=axis.values if axis.values is not None else Undefined,
    )


def build_bxplt_preagg_tooltips(
    orient: typ.AltMarkOrient,
    encode: pchrt.ChartEncodings,
) -> Sequence[pschm.Tooltip]:
    """Generate default orientation-aware tooltips."""

    return [
        chrt.Tooltip(
            shorthand=encode.y.shorthand,
            title=encode.y.axis.title if encode.y.axis is not None else None,
        )
        if orient == "horizontal"
        else chrt.Tooltip(
            shorthand=encode.x.shorthand,
            title=encode.x.axis.title if encode.x.axis is not None else None,
        ),
        chrt.Tooltip(shorthand="lower", title="Lower Whisker"),
        chrt.Tooltip(shorthand="25%", title="25% Quartile"),
        chrt.Tooltip(shorthand="50%", title="Median"),
        chrt.Tooltip(shorthand="75%", title="75% Quartile"),
        chrt.Tooltip(shorthand="upper", title="Upper Whisker"),
    ]


def build_scale(scale: pschm.Scale | None) -> alt.Scale | UndefinedType:
    """Build Altair scale from the provided scale configuration.

    Parameters:
        scale (pschm.Scale | None): Scale configuration to build.

    Returns:
        alt.Scale | None: Altair scale or None if no scale is provided.
    """

    if scale is None:
        return Undefined
    # Use cast to ensure type compatibility with alt.Scale
    return alt.Scale(
        domain=cast(list[str], scale.domain if scale.domain is not None else Undefined),
        range=cast(list[str], scale.range_ if scale.range_ is not None else Undefined),
        zero=cast(bool, scale.zero if scale.zero is not None else Undefined),
    )


def build_color(color: pschm.Color | str) -> alt.Color | Any:
    """Build Altair color encoding from provided configuration. If < color > is a string, the
    function will return an < alt.value > encoding with the specified color value (typed as Any
    because Altair's internal Channel system doesn't have a fully typed constructor in the stubs).
    Otherwise, the function will return an < alt.Color > encoding constructed from the provided
    < color > configuration values.

    INFO: Suppress mypy error for no-untyped-call since alt.Color is dynamically constructed via
    Altair's internal Channel system and doesn't have a fully typed constructor in the stubs.

    WARN: Note that both `legend` and `scale` can be None, which will hide the legend and
    disable the scale respectively. If `title` is None, it will default to Undefined.

    Parameters:
        shorthand (str): Field shorthand for the color channel.
        legend (str | None): Legend shorthand for the color channel.
        scale (pschm.Scale | None): Optional scale configuration.
        title (str | None): Title for the color legend.

    Returns:
        alt.Color: Altair color encoding.
    """

    if isinstance(color, str):
        return alt.value(color)
    return alt.Color(  # type: ignore[no-untyped-call]
        shorthand=color.shorthand,
        legend=None
        if color.disable_legend
        else (color.legend if color.legend is not None else Undefined),
        scale=None if color.scale is None else build_scale(color.scale),
        title=color.title if color.title is not None else Undefined,
    )


def build_outlier_encodings(
    orient: typ.AltMarkOrient,
    shorthand: str,
    color: pschm.Color,
    tooltips: Sequence[pschm.Tooltip] | None = None,
) -> dict[str, alt.VegaLiteSchema]:
    """Build Altair outlier encodings based on the orientation and color.
    Parameters:
        orient (typ.AltMarkOrient): Orientation of the outliers, either "horizontal" or "vertical".
        shorthand (str): Shorthand for the outlier encoding.
        color (pschm.Color): Color configuration for the outliers.
        tooltips (Sequence[pschm.Tooltip] | None): List of tooltip configurations for the outliers.

    Returns:
        dict[str, alt.VegaLiteSchema]: Dictionary of Altair encodings for the outliers.
    """

    shorthand = shorthand or "outliers:Q"
    key = "x" if orient == "horizontal" else "y"
    channel = alt.X if orient == "horizontal" else alt.Y

    return {
        key: channel(shorthand=shorthand),
        "color": build_color(
            chrt.Color(shorthand=color.shorthand, legend=color.legend, scale=color.scale)
        ),
        "tooltip": cast(alt.VegaLiteSchema, create_tooltips(tooltips) if tooltips else Undefined),
    }


def create_sigma_rules(
    frame: pd.DataFrame,
    mu_rule_mu: float,
    sigma_rule_sigma: float,
    sigma_rule_n: int,
    sigma_rule_color: str,
) -> list[alt.LayerChart]:
    """Create sigma rules for the chart.

    Parameters:
        frame (pd.DataFrame): DataFrame to use for the chart.
        mu_rule_mu (float): Mean value for the sigma rule.
        sigma_rule_sigma (float): Standard deviation for the sigma rule.
        sigma_rule_n (int): Number of sigma rules to create.
        sigma_rule_color (str): Color for the sigma rules.

    Returns:
        list[alt.LayerChart]: List of sigma rules.
    """

    rules = []
    for i in range(1, sigma_rule_n + 1):
        for sign in [+1, -1]:
            sigma_val = mu_rule_mu + sign * i * sigma_rule_sigma
            if sigma_val < 0:
                continue  # skip invalid negatives

            chart = alt.Chart(frame.head(1)).transform_calculate(**{
                f"sigma_{i}_{sign}": str(sigma_val)
            })

            mark = chart.mark_rule() if i == 1 else chart.mark_rule(strokeDash=[4, 4])

            rules.append(
                mark.encode(x=alt.X(f"sigma_{i}_{sign}:Q"), color=alt.value(sigma_rule_color))
            )

    return rules


def create_tooltips(tooltips: Sequence[pschm.Tooltip]) -> alt.VegaLiteSchema:
    """Create tooltips for the chart. Exclude < format > and < format_type > if values are not
    provided. Utilizes the unpacking operator to include only key-value pairs with provided
    values.

    Parameters:
        tooltips (Sequence[pschm.Tooltip]): List of tooltip configuration objects.

    Returns:
        alt.VegaLiteSchema: List of Altair Tooltip objects.
    """

    return cast(
        alt.VegaLiteSchema,
        [
            alt.Tooltip(
                shorthand=tooltip.shorthand,
                title=tooltip.title,
                format=tooltip.format if tooltip.format is not None else Undefined,
                formatType=tooltip.format_type if tooltip.format_type is not None else Undefined,
            )
            for tooltip in tooltips
        ],
        # Alternative: dict unpacking triggers mypy errors (bummer)
        # [
        #     alt.Tooltip(**{
        #         "shorthand": tooltip.shorthand,
        #         "title": tooltip.title,
        #         **({"format": tooltip.format} if tooltip.format is not None else {}),
        #         **({"formatType": tooltip.format_type} if tooltip.format_type is not None else {}),
        #     })
        #     for tooltip in tooltips
        # ],
    )


def format_shorthand(shorthand: str) -> str:
    """Drop the type specifier from the < shorthand > string.

    Parameters:
        shorthand (str): The shorthand string to format.

    Returns:
        str: The formatted shorthand string without the type specifier.
    """

    return shorthand.split(":")[0] if shorthand.find(":") >= 0 else shorthand


def remove_shorthand_type(shorthand: str) -> str:
    """Remove the type specifier from the shorthand string.

    Parameters:
        shorthand (str): The shorthand string to format.

    Returns:
        str: The formatted shorthand string without the type specifier.
    """

    return shorthand[:-2] if shorthand[-2] == ":" else shorthand
