import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from collections import defaultdict

app=dash.Dash()
#'x':[1940,1950,1960,1970,1980,1990,2000,2010,2020],
                       #'y':[10000,100000,1000000,10000000,100000000],
                       #'type':'line','name':'movies'
line2d=[]
d=dict()
l=[]
count=0;
with open('boxoffice.csv','r') as file:
    with open("updated_test.csv",'w') as file1:
        next(file)
        for line in file:
            file1.write(line)
with open("updated_test.csv",'r') as file2:
    for line in file2:
        lines=line.split(',');
        if lines[-1] in d.keys():
            d[lines[-1]].append(lines[-2])
        else:
            d[lines[-1]]=[lines[-2]]
#d1=d
#print(d1.values())
for i in sorted(d.keys()):
    l.append(i)
    for g in d[i]:
        line2d.append(g)
#print(l)

    
app.layout = html.Div(children=[
    html.H1(children='Dash Tutorials'),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x':l,
                       'y':line2d,
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
                              
