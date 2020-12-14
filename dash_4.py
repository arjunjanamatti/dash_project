import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = pd.read_csv('drop_df_1.csv')
df = (df.sort_values(by='amount_of_money', ascending = False))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

fig = px.scatter(data_frame = df.iloc[:10, :], x = 'count', y = 'amount_of_money', size = 'amount_of_money', color = 'executorOrganization', size_max = 60)

app.layout = html.Div([
    html.H1(children = 'Top 10 Customers based on Income'),
    dcc.Graph(
        id = 'scatter_plot',
        figure = fig
    )
])

if __name__ == '__main__':
    app.run_server(debug = True)