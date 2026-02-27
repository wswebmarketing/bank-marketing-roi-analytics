import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path = "/segmentacao-bancaria",
    title = "Segmentação Bancária"
)

layout = html.Div(
    children = [
        html.H1("Página de segmentação bancária!")
    ]
)