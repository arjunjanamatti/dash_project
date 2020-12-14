from plotly import graph_objs as go
import ipywidgets as w
from IPython.display import display
import pandas as pd

df = pd.DataFrame()
df['category'] = ['G1', 'G1', 'G1', 'G1','G1', 'G1','G1', 'G2', 'G2', 'G2', 'G2', 'G2', 'G2', 'G2']
df['date'] = ['2012-04-01', '2012-04-05', '2012-04-09', '2012-04-11', '2012-04-16', '2012-04-23', '2012-04-30',
          '2012-04-01', '2012-04-05', '2012-04-09', '2012-04-11', '2012-04-16', '2012-04-23', '2012-04-30']
df['col1'] = [54, 34, 65, 67, 23, 34, 54, 23, 67, 24, 64, 24, 45, 89]
df['col2'] = round(df['col1'] * 0.85)

x  = 'date'
y1 = 'col1'
y2 = 'col2'

trace1 = {
    'x': df[x],
    'y': df[y1],
    'type': 'scatter',
    'mode': 'lines',
    'name':'col 1',
    'marker': {'color': 'blue'}
}

trace2={
    'x': df[x],
    'y': df[y2],
    'type': 'scatter',
    'mode': 'lines',
    'name':'col 2',
    'marker': {'color': 'yellow'}
}

data = [trace1, trace2]

# Create layout for the plot
layout=dict(
    title='my plot',
    xaxis=dict(
        title='Date',
        type='date',
        tickformat='%Y-%m-%d',
        ticklen=5,
        titlefont=dict(
            family='Old Standard TT, serif',
            size=20,
            color='black'
        )
    ),
    yaxis=dict(
        title='values',
        ticklen=5,
        titlefont=dict(
            family='Old Standard TT, serif',
            size=20,
            color='black'
            )
        )

    )

# Here's the new part

fig = go.FigureWidget(data=data, layout=layout)

def update_fig(change):
    aux_df = df[df.category.isin(change['new'])]
    with fig.batch_update():
        for trace, column in zip(fig.data, [y1, y2]):
            trace.x = aux_df[x]
            trace.y = aux_df[column]

drop = w.Dropdown(options=[
    ('All', ['G1', 'G2']),
    ('G1', ['G1']),
    ('G2', ['G2']),
])
drop.observe(update_fig, names='value')

display(w.VBox([drop, fig]))