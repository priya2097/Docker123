
import dash
import pandas as pd

import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from os import listdir
from os.path import isfile, join
import numpy as np
from plotly import graph_objs as go
import plotly_express as px

import pickle
import datetime
import pandas_datareader.data as web


infile = open("files/fraud_detection.pickle",'rb')
df = pickle.load(infile)
infile.close()
print(df)
print("the df shape ", df.shape)
print('#############################')
x1 = df[df['Original']==0]
original0_count = x1.shape[0]
print("the original=0 shape ", original0_count)
x2 = df[df['Original']==1]
original1_count = x2.shape[0]
print("the original=1 shape ", original1_count)

xx1 = x1[x1['yhat']==0]
yhat0_count = xx1.shape[0]
print("the original=0 & yhat=0 shape ", yhat0_count)
xx2 = x2[x2['yhat']==1]
yhat1_count = xx2.shape[0]
print("the original=1 & yhat=1 shape ", yhat1_count)


print('#############################')
y0 = df[df['yhat']==0]
y0_count = y0.shape[0]
print("the yhat=0 shape ", y0_count)
y1 = df[df['yhat']==1]

y1_count = y1.shape[0]
print("the yhat=1 shape ", y1_count)

# print(y1.shape)
x_labels=['0', '1']

# df.reset_index(inplace=True)
# df.set_index("ds", inplace=True)
# df = df.drop("index", axis=1)

# print(df.tail())


USERNAME_PASSWORD_PAIRS=[
    ['ajay','prodevans'],['priyag','prodevans'],['alekhya','prodevans'],['iventura','prodevans']
    ]
app=dash.Dash(
     __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)
auth=dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(children='Welcome to Iventura Platform',style={
    'textAlign': 'center',
    'color': colors['text']}),

    # html.Div(children='''
    #     Revenue Forecasting Line Graph
    # '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                # type 1
                go.Bar(x=x_labels, y=[original0_count,original1_count], name='Original', marker_color='crimson'),
                go.Bar(x=x_labels, y=[yhat0_count, yhat1_count],name='Yhat',marker_color='lightslategrey'),
                # type 2
                # go.Bar(x=x_labels, y=[original0_count,original1_count], name='Original', marker_color='crimson'),
                # go.Bar(x=x_labels, y=[y0_count, y1_count],name='Yhat',marker_color='lightslategrey')
            ],
            'layout': {
                'title': 'Credit Card Fraud Detection'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')


