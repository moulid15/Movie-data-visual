import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from collections import defaultdict

import py

app=dash.Dash()
#'x':[1940,1950,1960,1970,1980,1990,2000,2010,2020],
                       #'y':[10000,100000,1000000,10000000,100000000],
                       #'type':'line','name':'movies'
line2d=[]
d=[]
l=dict={}
l2=[]
count=0;
dic=[]
line2=[]
avg=dict={}
def avr(arg):
    l={}
    sum=0
    for i in arg:
        l1=arg[i]
        for j in l1:
            sum+=j
        l[i]=sum/len(l1)
        sum=0
    return l
with open('boxoffice.csv','r') as file:
    with open("updated_test.csv",'w') as file1:
        next(file)
        for line in file:
            file1.write(line)
with open("updated_test.csv",'r') as file2:
    for line in file2:
        l2=line.split(',')
        c=int(l2[-2])
        c2=int(l2[-1])
        line2.append(c)
        d.append(c2)

        # if c2 in l:
        #     l[c2].append(c)
        # else:
        #     l[c2]=[c]
avg=avr(l)
# for i in sorted(avg.keys()):
#     line2.append(

app.layout = html.Div(children=[
    html.H1(children='Moe plots'),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x':d,
                       'y':line2,
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
                              
