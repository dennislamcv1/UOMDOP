import altair as alt


def configure_bar_text(data, x_shorthand, y_shorthand, color):
    """Returns a text configuration object for a bar chart.

    Parameters:
        data (list): list of dictionaries
        x_shorthand (str): shorthand value for the x-axis
        y_shorthand (str): shorthand value for the y-axis
        color (str): text color

    Returns:
        alt.Chart: text configuration object
    """

    return (
        alt.Chart(alt.Data(values=data))
        .mark_text(align="center", baseline="bottom", fontSize=8, dy=-2)
        .encode(
            x=alt.X(shorthand=x_shorthand),
            y=alt.Y(shorthand=y_shorthand),
            text=alt.Text(shorthand=y_shorthand, format=".0f"),
            color=alt.value(color),
        )
    )


def configure_colors(shorthand, custom_labels, custom_colors):
    """Returns a color configuration object for a chart. The legend labels are

    Parameters:
        shorthand (str): shorthand value for the color

    Returns:
        alt.Color: color configuration object
    """

    keys = list(custom_labels.keys())

    # Interpreted as a JavaScript expression (inject string)
    label_expr = (
        f'datum.value == "{keys[0]}" ? "{custom_labels[keys[0]]}" : "{custom_labels[keys[1]]}"'
    )

    return alt.Color(
        shorthand=shorthand,
        scale=alt.Scale(domain=list(custom_labels.keys()), range=custom_colors),
        legend=alt.Legend(title="Publications", orient="top-left", labelExpr=label_expr),
    )


def configure_rolling_mean(data, x_shorthand, y_shorthand, color):
    """Returns a line chart object with a rolling mean transformation applied.

    Parameters:
        data (list): list of dictionaries
        x_shorthand (str): shorthand value for the x-axis
        y_shorthand (str): shorthand value for the y-axis
        color (str): line color

    Returns:
        alt.Chart: line chart object with rolling mean transformation applied
    """

    return (
        alt.Chart(alt.Data(values=data))
        .mark_line(color=color)
        .encode(x=alt.X(shorthand=x_shorthand), y=alt.Y(shorthand=y_shorthand))
        .transform_window(rolling_mean="mean(citations)", frame=[-2, 0])
    )


def configure_title(title, subtitle=""):
    """Returns a dictionary comprising a title and, if provided, a subtitle.

    Parameters:
        title (str): chart title
        subtitle (str): chart subtitle

    Returns:
        dict: title configuration object
    """

    return {"text": title, "subtitle": subtitle} if subtitle else {"text": title}


def configure_x_axis(x_shorthand):
    """Returns an axis object configured with the provided shorthand value.

    Parameters:
        x_shorthand (str): shorthand value for the x-axis

    Returns:
        alt.X: axis object
    """

    return alt.X(
        shorthand=x_shorthand,
        axis=alt.Axis(
            labelAngle=-60,
            labelFontWeight="normal",
            title=x_shorthand[:-2].capitalize(),
            titleFontSize=10,
            titleFontWeight="bold",
        ),
    )


def configure_y_axis(y_shorthand):
    """Returns an axis object configured with the provided shorthand value.

    Parameters:
        y_shorthand (str): shorthand value for the y-axis

    Returns:
        alt.Y: axis object
    """

    return alt.Y(
        shorthand=y_shorthand,
        axis=alt.Axis(
            labelFontWeight="normal",
            title=y_shorthand[:-2].capitalize(),
            titleFontSize=10,
            titleFontWeight="bold",
        ),
    )


def create_stacked_bar_chart(
    data_grouped,
    data_ungrouped,
    x_shorthand,
    y_shorthand,
    grp_shorthand,
    custom_colors,
    custom_labels,
    title,
    subtitle="",
    rm_shorthand="",
    height=300,
    width=800,
):
    """Returns a layered stacked bar chart object with a rolling mean transformation applied.
    Delegates the task of configuring various chart features to a number of < configure_*() >
    functions.

    Parameters:
        data_grouped (list): list of dictionaries
        data_ungrouped (list): list of dictionaries
        x_shorthand (str): x-axis shorthand value
        y_shorthand (str): y-axis shorthand value
        grp_shorthand (str): group shorthand value
        custom_colors (list): list of custom colors
        custom_labels (dict): dictionary of custom labels
        title (str): chart title
        subtitle (str): chart subtitle
        rm_shorthand (str): shorthand value for the rolling mean
        height (int): chart height
        width (int): chart width

    Returns:
        alt.Chart: layered bar chart object
    """

    base = alt.Chart(alt.Data(values=data_grouped))
    bar = base.mark_bar().encode(
        x=configure_x_axis(x_shorthand),
        y=configure_y_axis(y_shorthand),
        color=configure_colors(grp_shorthand, custom_labels, custom_colors),
        order=alt.Order(grp_shorthand, sort="descending"),
        tooltip=alt.Tooltip(shorthand=[x_shorthand, y_shorthand]),
    )
    text = configure_bar_text(data_ungrouped, x_shorthand, y_shorthand, custom_colors[1])
    title = configure_title(title, subtitle)

    if rm_shorthand:
        line = configure_rolling_mean(data_ungrouped, x_shorthand, rm_shorthand, custom_colors[0])
        return alt.layer(bar, line, text).properties(title=title, height=height, width=width)
    else:
        return alt.layer(bar, text).properties(title=title, height=height, width=width)
