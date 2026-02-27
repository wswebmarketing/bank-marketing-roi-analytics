import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from services.analytics import(
    get_segments,
    executive_resume
)
import pprint
import pandas as pd
import plotly.express as px

print(get_segments())
pprint.pprint(executive_resume())

#gráfico utilizado apenas para desenvolvimento da paǵina
df_placeholder = pd.DataFrame({
    "category": ["Gold", "Strong", "Medium", "Weak", "Destructive"],
    "avg_profit": [120, 70, 48, 27, 14]
})

fig_placeholder = px.bar(
    df_placeholder,
    x = "category",
    y = "avg_profit",
    title = "Lucro Médio por Categoria",
    color = "category",
    template = "plotly"
)

dash.register_page(
    __name__,
    path = "/",
    title = "Home"
)

layout = html.Div(
    className = "p-5 container",
    children = [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            "Segmentação Estratégica de Clientes Bancários",
                            className = "fw-bold text-center"
                        ),
                        html.Div(
                            [
                                html.P(
                                    "Modelo analítico orientado a ROI (Retorno Sobre Investimento) para redistribuição estratégica de orçamento e maximização do lucro.",
                                    className = "text-justify"
                                )        
                            ],
                            className = "p-3",
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5(
                                    "Visão geral de performance",
                                    className = "fw-bold text-center"
                                ),
                                dcc.Graph(
                                    figure = fig_placeholder
                                )
                            ]
                        )
                    )
                )
            ]
        )
    ]
)

