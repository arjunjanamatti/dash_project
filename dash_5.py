import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.layout = html.Div(
    children = [
        html.H6 ('Change value in the input box to see callbacks in output section!!!'),
        html.Div(children = ['Input',
                             dcc.Input(id = 'input_value', value = 'input value', type = 'text')]),
        html.Br(),
        html.Div(id = 'output_value')
    ])

@app.callback(
    Output(component_id = 'output_value', component_property = 'children'),
    Input(component_id = 'input_value', component_property = 'value')
)

def update_output_div(input_value):
    return 'Output: {}'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug = True)