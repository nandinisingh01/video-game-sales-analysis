import plotly.graph_objects as go

def plotBar(datapoints, title = "default title", xlabel = "xlabel", ylabel="ylabel"):
    
    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)
    
    fig.add_trace(go.Bar(x=datapoints.index, y=datapoints.values))
    return fig