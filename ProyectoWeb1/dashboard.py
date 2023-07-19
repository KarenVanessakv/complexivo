import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('data.csv', delimiter = ';')


pv = pd.pivot_table(df, index=['Name'], columns=["Status"], values=['Quantity'], aggfunc=sum, fill_value=0)

trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'entregada')], name='Entregada')
trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pendiente')], name='Pendiente')
trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'enviada')], name='Enviada')


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Reporte de Ventas de mi tienda virtual'),
    html.Div(children='''Reporte de Ventas.'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3],
            'layout':
            go.Layout(title='Estado de envio de clientes', barmode='stack')
        })
])


if __name__ == '__main__':
    app.run_server(debug=True)