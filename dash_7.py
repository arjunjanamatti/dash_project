import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt

raw_onfleet_data = pd.read_pickle('raw_onfleet_data_after_zoning.pkl')

raw_onfleet_data['startTime'] = pd.to_datetime(raw_onfleet_data['startTime'])
raw_onfleet_data['dates'] = raw_onfleet_data.startTime.dt.date
raw_onfleet_data['year'] = raw_onfleet_data.startTime.dt.year
raw_onfleet_data['week'] = raw_onfleet_data.startTime.dt.week
raw_onfleet_data['month'] = raw_onfleet_data.startTime.dt.month
raw_onfleet_data['day'] = raw_onfleet_data.startTime.dt.day


df = raw_onfleet_data[['executorOrganization', 'workerName', 'dates', 'distance', 'week', 'day', 'month']]

available_workers = df['workerName'].unique()

unique_weeks = df['week'].unique()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)


app.layout = html.Div([
    # html.Div([
    #     html.Div([
    #         dcc.Dropdown(
    #             id = 'x_axis_column',
    #             options = [{'label': i, 'value':i} for i in available_workers],
    #             value = 'Adrian'
    #         )
    #     ])
    # ]),

    dcc.Graph(id = 'worker_graph'),
    dcc.Slider(
        id = 'week_slider',
        min=df['week'].min(),
        max=df['week'].max(),
        value=df['week'].min(),
        marks={str(week): str(week) for week in df['week'].unique()}
    ),
    dcc.Slider(
        id='day_slider',
        min=df['day'].min(),
        max=df['day'].max(),
        value=df['day'].min(),
        marks={str(week): str(week) for week in df['week'].unique()}
    ),
    dcc.Dropdown(
        id='x_axis_column',
        options=[{'label': i, 'value': i} for i in available_workers],
        value='Adrian'
    )
])
#
# print(available_workers)
#
# dff = df[df['workerName'] == available_workers[0]]
# print(dff.info())
#
# dff_1 = dff[dff['week'] == 31]
# print(dff_1[['executorOrganization', 'distance']])
#
# dff_2 = (dff_1.groupby(['executorOrganization']).sum())
#
# print(dff_2.columns)
#
# plt.bar(x = dff_2.index, height = dff_2['distance'],)
# plt.show()


@app.callback(
    Output('worker_graph', 'figure'),
    # Input('week_slider', 'value'),
    Input('x_axis_column', 'value')
)
def update_graph(x_axis_value):
    dff = df[df['workerName'] == x_axis_value]
    print(dff)
    # dff_1 = dff[dff['week'] == int(week_value)]
    # print(dff_1)
    filtered_df = (dff.groupby(['executorOrganization']).sum())
    print(filtered_df)
    fig = px.bar(data_frame = filtered_df, x = filtered_df.index, y = 'distance',),
    # fig.update_layout(transition_duration=500)
    print('REPEATING#####')
    # fig.update_xaxes(title = xaxis_column_name)

    return fig
# else:
#     # fig = px.imshow('no_data_available.png')
#     return []

if __name__ == '__main__':
    app.run_server(debug=True)
