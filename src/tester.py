import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html

from src.scraper import ret

app=dash.Dash()
line2d=[]
d=[]
l=dict={}
l=ret()
print(l)
app.layout = html.Div(children=[
    html.H1(children='Moe plots'),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x':list(l.keys()),
                       'y':list(l.values()),
                       'type':'line','name':'movies' }
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
                              
