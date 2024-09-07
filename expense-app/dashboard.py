import pandas as pd
import plotly.graph_objs as go
import dash
import dash_html_components as html
import dash_core_components as dcc

data=pd.read_csv('gapminder.csv')

app=dash.Dash()
#app.layout=html.H1(children="My first Dashboard",style={'color':'red','text-align':'center'})

app.layout=html.Div([
    html.Div(
        children=[
            html.H1("My First Dashboard",style={'color':'red','text-align':'center','margin-bottom':'5px'})
            ],
        style={'border':'1px black solid','float':'left','width':'100%','height':'50px'}),
    html.Div(
        children=[
            dcc.Graph(id='scatter-plot',
                     figure={
                         'data':[go.Scatter(x=data['pop'],y=data['gdpPercap'],mode='markers')],
                        'layout':go.Layout(title='Scatter Plot')
                              
                     })
            ],
        style={'border':'1px black solid','float':'left','width':'49.5%'}),
    html.Div(
        children=[
                dcc.Graph(id='box-plot',
                          figure={
                         'data':[go.Box(x=data['gdpPercap'])],
                        'layout':go.Layout(title='Boxplot')
                              
                     }
                          )
            ],
        style={'border':'1px black solid','float':'left','width':'49.5%'})
])
if __name__=='__main__':
    app.run_server()