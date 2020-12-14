import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('drop_df_1.csv')

fig = px.bar(data_frame = df, x = 'executorOrganization', y = 'amount_of_money', barmode = 'group', color = 'count')

fig.update_layout(
    plot_bgcolor = colors['background'],
    paper_bgcolor = colors['background'],
    font_color = colors['text']
)

app.layout = html.Div(style = {'backgroundColor': colors['background']},
                      children = [
                          html.H1(
                            children = 'Customer Financial Details',
                            style = {
                                'textAlign': 'center',
                                'color': colors['text']
                            }),
                          html.Div(
                              children = '''This is trial with new style on the background''',
                              style = {
                                  'textAlign': 'center',
                                  'color': colors['text']
                              }),

                          dcc.Graph(
                              id = 'example_graph_2',
                              figure = fig
                          )
                      ])

if __name__ == '__main__':
    app.run_server(debug = True)