import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

line2d=[]

df=pd.read_csv('boxoffice.csv')
with open('boxoffice.csv','r') as file:
          for line in file:
              lines=line.split(',');
              lines.remove(lines[0])
              line2d.append(lines)
line2d.remove(line2d[0])
def generate_table(dataframe, max_rows=10):
    return html.Bar(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(max(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
style={'background':'black','color':'white'},
children=[
    html.H3(style={'background-color':'white', 'color':'black'},children='US Movie Gross'),
    generate_table(df)
])
if __name__ == '__main__':
    app.run_server(debug=True)
