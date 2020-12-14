import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

raw_onfleet_data = pd.read_pickle('raw_onfleet_data_after_zoning.pkl')

raw_onfleet_data['startTime'] = pd.to_datetime(raw_onfleet_data['startTime'])
raw_onfleet_data['dates'] = raw_onfleet_data.startTime.dt.date
raw_onfleet_data['year'] = raw_onfleet_data.startTime.dt.year
raw_onfleet_data['week'] = raw_onfleet_data.startTime.dt.week
raw_onfleet_data['month'] = raw_onfleet_data.startTime.dt.month
raw_onfleet_data['day'] = raw_onfleet_data.startTime.dt.day


# print(raw_onfleet_data.columns)
df = raw_onfleet_data[['executorOrganization', 'workerName', 'dates', 'distance', 'week', 'day', 'month']]

print(df[['executorOrganization', 'week', 'workerName']])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

# print(df['week'])

app.layout = html.Div([
    dcc.Dropdown(
        id='week_slider',
        options=[{'label': i, 'value': i} for i in df['week'].unique()],
        value=df['week'].max(),
    ),
    dcc.Dropdown(
        id='company_slider',
        options=[{'label': i, 'value': i} for i in df['executorOrganization'].unique()],
        value='Sally Clarke',
    ),
    html.H3('Graph for Distance by each worker in week for client'),
    dcc.Graph(id = 'graph_with_slider'),
    html.H3('Graph for Number of riders by each worker in week for client'),
    dcc.Graph(id = 'graph_with_size'),
    html.H2('RIDER INFORMATION ON WEEKLY BASIS'),
    html.H3('Rider Distance per client on weekly basis'),
    dcc.Dropdown(
        id='worker_slider',
        options=[{'label': i, 'value': i} for i in df['workerName'].unique()],
        value='Adrian',
    ),
    dcc.Dropdown(
        id='week_slider_1',
        options=[{'label': i, 'value': i} for i in df['week'].unique()],
        value=df['week'].max(),
    ),
    dcc.Graph(id = 'worker_with_slider'),
    html.H3('Rider rides per client on weekly basis'),
    dcc.Graph(id = 'worker_with_slider_size'),
    html.H3('Total Distance travelled by rider'),
    dcc.Graph(id = 'total_distance_worker_weekly'),
    html.H3('Total rides travelled by rider'),
    dcc.Graph(id='total_rides_worker_weekly'),

])

@app.callback(
    Output('graph_with_slider', 'figure'),
    Output('graph_with_size', 'figure'),
    Output('worker_with_slider', 'figure'),
    Output('worker_with_slider_size', 'figure'),
    Output('total_distance_worker_weekly', 'figure'),
    Output('total_rides_worker_weekly', 'figure'),
    Input('week_slider', 'value'),
    Input('company_slider', 'value'),
    Input('worker_slider', 'value'),
    Input('week_slider_1', 'value'),
)
def update_figure(selected_week, selected_company, selected_worker, selected_worker_week):
    ### Graph for Distance by each worker in week for client
    df_1 = df[df['executorOrganization'] == selected_company]
    filtered_df = df_1[df_1['week'] == selected_week]
    filtered_df_1 = (filtered_df.groupby(['workerName']).sum())
    fig = px.bar(data_frame = filtered_df_1, x = filtered_df_1.index, y = 'distance')
    fig.update_layout(transition_duration = 500, height = 500, width = 600)

    ### Graph for Number of rides by each worker in week for client
    filtered_df_2 = (filtered_df.groupby(['workerName']).size())
    fig_1 = px.bar(data_frame = filtered_df_2, x = filtered_df_2.index, y = 0)
    fig_1.update_layout(transition_duration = 500, height = 500, width = 600)

    ### Rider Distance per client on weekly basis
    df_2 = df[df['workerName'] == selected_worker]
    filtered_df_2_2 = df_2[df_2['week'] == selected_worker_week]
    filtered_df_3_2 = (filtered_df_2_2.groupby(['executorOrganization']).sum())
    fig_2 = px.bar(data_frame=filtered_df_3_2, x=filtered_df_3_2.index, y='distance')

    ### Rider rides per client on weekly basis
    filtered_df_2_3 = df_2[df_2['week'] == selected_worker_week]
    filtered_df_3_3 = (filtered_df_2_3.groupby(['executorOrganization']).size())
    fig_3 = px.bar(data_frame=filtered_df_3_3, x=filtered_df_3_3.index, y= 0)

    ### Total Distance travelled by rider
    filtered_df_3_4 = (df_2.groupby(['week'])['distance'].sum())
    fig_4 = px.bar(data_frame=filtered_df_3_4, x=filtered_df_3_4.index, y='distance')

    ### Total rides travelled by rider
    filtered_df_3_5 = (df_2.groupby(['week'])['distance'].size())
    fig_5 = px.bar(data_frame=filtered_df_3_5, x=filtered_df_3_5.index, y='distance')
    return fig, fig_1, fig_2, fig_3, fig_4, fig_5


if __name__ == '__main__':
    app.run_server(debug = True)