import plotly.graph_objects as go
import plotly.express as px


def plotMultiLine(datapoints, title, xlabel, ylabel, names, template="plotly_dark", line_colors=['#f63366', '#128866']):
    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel), template=template)
    fig = go.Figure(layout=layout)

    for datapoint, color, name in zip(datapoints, line_colors, names):
        fig.add_trace(go.Line(x=datapoint.index,
                              y=datapoint.values, line_color=color, name=name))
    return fig
