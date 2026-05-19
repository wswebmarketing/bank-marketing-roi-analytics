import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
from services.analytics import(
    get_segments
)
'''
LIBS UTILIZADAS APENAS PARA DESENVOLVIMENTO E TESTES, NÃO SEÃO USADAS PARA DEPLOY
from pprint import pprint
from tabulate import tabulate
'''

segments = get_segments()

gold_count = (segments["category"] == "Gold").sum()

strong_count = (segments["category"] == "Strong").sum()

destructive_count = (segments["category"] == "Destructive").sum()

total_segments = len(segments)

category_distribution = (
    segments["category"]
    .value_counts()
    .reset_index()
)
category_distribution.columns = ["category", "count"]

fig_distribution = px.bar(
    category_distribution,
    x = "category",
    y = "count",
    color = "category",
    labels = {
        "category": "Categoria",
        "count": "Número de Clientes"
    }
)
fig_distribution.update_traces(textposition = "outside")
fig_distribution.update_layout(
    showlegend = False,
    font = dict(family = "inherit", size = 12),
    margin = dict(l = 10, r = 10, t = 40, b = 20)
)

profit_by_category = (
    segments
    .groupby("category")["expected_profit"]
    .mean()
    .reset_index()
    .round(2)
)

fig_profit = px.bar(
    profit_by_category,
    x = "category",
    y = "expected_profit",
    color = "category",
    labels = {
        "category": "Categoria",
        "expected_profit": "Lucro Médio ($)"
    }
)
fig_profit.update_traces(
    texttemplate = "%{text:.2f}",    
    textposition = "outside"
)
fig_profit.update_layout(
    showlegend = False,
    font = dict(family = "inherit", size = 12),
    margin = dict(l = 10, r = 10, t = 40, b = 20)
)

table_data = profit_by_category.to_dict("records")
table_columns = [
    {"name": col, "id": col}
    for col in profit_by_category.columns
]

dash.register_page(
    __name__,
    path = "/classificacao-estrategica",
    title = "Classificação Estratégica"
)

layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                [
                    html.H1(
                        "Classificação Estratégica de Segmentos",
                        className = "text-center fw-bold"
                    ),
                    html.Div(
                        [
                            html.P(
                                "Classificação dos segmentos com base na lucratividade esperada e no ROI.",
                                className = "text-justify"
                            )
                        ],
                        className = "p-3"
                    )
                ],
                width = 12
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H6(
                                    "Segmentos Gold",
                                    className = "text-center fw-bold"
                                ),
                                html.H3(
                                    f"{gold_count}",
                                    className = "card-text text-center fw-bold"
                                )
                            ]
                        )
                    ),
                    xs = 12, sm = 12, md = 3, lg = 3, xl = 3
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H6(
                                    "Segmentos Strong",
                                    className = "text-center fw-bold"
                                ),
                                html.H3(
                                    f"{strong_count}",
                                    className = "card-text text-center fw-bold"
                                )
                            ]
                        )
                    ),
                    xs = 12, sm = 12, md = 3, lg = 3, xl = 3
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H6(
                                    "Segmentos Destructive",
                                    className = "text-center fw-bold"
                                ),
                                html.H3(
                                    f"{destructive_count}",
                                    className = "card-text text-center fw-bold"
                                )
                            ]
                        )
                    ),
                    xs = 12, sm = 12, md = 3, lg = 3, xl = 3
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H6(
                                    "Total de Segmentos",
                                    className = "text-center fw-bold"
                                ),
                                html.H3(
                                    f"{total_segments}",
                                    className = "card-text text-center fw-bold"
                                )
                            ]
                        )
                    ),
                    xs = 12, sm = 12, md = 3, lg = 3, xl = 3
                )
            ],
            className = "g-4 p-2"
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5(
                                    "Distribuição dos Segmentos de Clientes",
                                    className = "text-center fw-bold"
                                ),
                                dcc.Graph(
                                    figure = fig_distribution,
                                    responsive = True,
                                    config = {
                                        "displayModeBar": False
                                    },
                                    style = {
                                        "width": "100%",
                                        "height": "400px"
                                    }
                                )
                            ]
                        )
                    ),
                    xs = 12, sm = 12, md = 6, lg = 6, xl = 6
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5(
                                    "Lucro Médio por Categoria",
                                    className = "text-center fw-bold"
                                ),
                                dcc.Graph(
                                    figure = fig_profit,
                                    responsive = True,
                                    config = {
                                        "displayModeBar": False
                                    },
                                    style = {
                                        "width": "100%",
                                        "height": "400px"
                                    }
                                )
                            ]
                        )
                    ),
                    xs = 12, sm = 12, md = 6, lg = 6, xl = 6
                )
            ],
            className = "g-4 p-2"
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                dash_table.DataTable(
                                    data = table_data,
                                    columns = table_columns,
                                    style_table = {
                                        "overflowX": "auto"
                                    },
                                    style_cell = {
                                        "textAlign": "center",
                                        "padding": "10px"
                                    },
                                    style_header = {
                                        "fontWeight": "bold"
                                    }
                                )
                            ]
                        )
                    ),
                    width = 12
                )
            ],
            className = "g-4 p-2"
        )
    ],
    className = "p-2 p-xs-2 p-sm-2 p-md-5 container"
)