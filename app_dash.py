import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash import dash_table

import pandas as pd
import plotly.graph_objs as go

from scraping import scrapeo_opciones_y_futuros
from volatilidad import calcular_volatilidad

# --- 1. Scrapeo y cálculo de volatilidad
df_opciones, df_futuros = scrapeo_opciones_y_futuros()
df_resultado = calcular_volatilidad(df_opciones, df_futuros)

# --- 2. Inicialización de la app
app = dash.Dash(__name__)
server = app.server
app.title = "Skew de Volatilidad - MINI IBEX"

print("Columnas de df_resultado:", df_resultado.columns.tolist())
print(df_resultado.head())

# --- 3. Layout
vencimientos = sorted(df_resultado['FV'].dropna().unique())

app.layout = html.Div(
    style={'fontFamily': 'Segoe UI, sans-serif', 'backgroundColor': '#f5f6fa', 'padding': '30px'},
    children=[
        html.H1("📊 Skew de Volatilidad - MINI IBEX", style={
            'textAlign': 'center',
            'color': '#2f3640',
            'marginBottom': '30px'
        }),

        html.Div([
            html.Label("Selecciona vencimiento:", style={
                'fontWeight': 'bold',
                'marginBottom': '10px',
                'display': 'block'
            }),
            dcc.Dropdown(
                id='vencimiento-dropdown',
                options=[{'label': str(v), 'value': v} for v in vencimientos],
                value=vencimientos[0],
                style={'width': '100%', 'padding': '5px'}
            )
        ], style={
            'width': '25%',
            'margin': '0 auto 40px auto',
            'backgroundColor': '#ffffff',
            'padding': '20px',
            'borderRadius': '10px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'
        }),

html.Div([
    dcc.Graph(
        id='vol-skew-graph',
        config={'displayModeBar': False},  # Oculta barra de herramientas si quieres
        style={'height': '600px'}
    )
], style={
    'maxWidth': '900px',         # <--- LIMITA EL ANCHO DEL GRÁFICO
    'margin': '0 auto 30px auto',
    'backgroundColor': '#ffffff',
    'padding': '20px',
    'borderRadius': '10px',
    'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'
}),

        html.Details([
            html.Summary('📄 Ver datos usados en el gráfico', style={
                'fontWeight': 'bold',
                'cursor': 'pointer'
            }),
            html.Div(id='data-table', style={'marginTop': '20px'})
        ], style={
            'width': '90%',
            'margin': '0 auto',
            'backgroundColor': '#ffffff',
            'padding': '20px',
            'borderRadius': '10px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'
        })
    ]
)

# --- 4. Callbacks
@app.callback(
    Output('vol-skew-graph', 'figure'),
    Output('data-table', 'children'),
    Input('vencimiento-dropdown', 'value')
)
def update_graph(vencimiento_seleccionado):
    df_vto = df_resultado[df_resultado['FV'] == vencimiento_seleccionado]
    df_calls = df_vto[df_vto['put/call'] == 'Call'].dropna(subset=['σ'])
    df_puts = df_vto[df_vto['put/call'] == 'Put'].dropna(subset=['σ'])

    traces = []

    if not df_calls.empty:
        traces.append(go.Scatter(
            x=df_calls['strike'],
            y=df_calls['σ'],
            mode='lines+markers',
            name='Calls'
        ))

    if not df_puts.empty:
        traces.append(go.Scatter(
            x=df_puts['strike'],
            y=df_puts['σ'],
            mode='lines+markers',
            name='Puts'
        ))

    figure = {
        'data': traces,
        'layout': go.Layout(
            title=f'Skew de Volatilidad - Vencimiento {vencimiento_seleccionado}',
            xaxis={'title': 'Strike'},
            yaxis={'title': 'Volatilidad Implícita (%)'},
            hovermode='closest',
            template='plotly_white'
        )
    }

    tabla = html.Div([
        dcc.Markdown("#### Datos utilizados"),
        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in ['strike', 'put/call', 'ant', 'σ']],
            data=df_vto[['strike', 'put/call', 'ant', 'σ']].to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={
                'textAlign': 'center',
                'padding': '8px',
                'fontFamily': 'Segoe UI',
            },
            style_header={
                'backgroundColor': '#2f3640',
                'color': 'white',
                'fontWeight': 'bold'
            },
            style_data_conditional=[
                {
                    'if': {'column_id': 'σ'},
                    'backgroundColor': '#f0f9ff',
                }
            ],
            page_size=20
        )
    ])

    return figure, tabla

# --- 5. Ejecutar
if __name__ == '__main__':
    app.run(debug=True)
