import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

df = pd.read_csv('drop_df_1.csv')

print(df.columns)

fig = px.bar(data_frame = df, x = 'executorOrganization', y = 'amount_of_money', barmode = 'group', color = 'count')

app.layout = html.Div(
    children = [
        html.H1(children = 'Customer Financial Details'),

        html.Div(children = '''
        Financial details of customers
        '''),

        dcc.Graph(
            id = 'example_graph',
            figure = fig
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug = True)