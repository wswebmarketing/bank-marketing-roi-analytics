import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
from services.analytics import(
    get_segments
)
from pprint import pprint
from tabulate import tabulate

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
    text = "count",
    title = "Distribuição dos Segmentos de Clientes",
    color = "category",
    labels = {
        "category": "Categoria",
        "count": "Número de Clientes"
    }
)
fig_distribution.update_traces(textposition = "outside")
fig_distribution.update_layout(showlegend = False)

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
    text = "expected_profit",
    title = "Lucro Médio por Categoria",
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
fig_profit.update_layout(showlegend = False)

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
                    html.P(
                        "Classificação dos segmentos com base na lucratividade esperada e no ROI.",
                        className = "text-justify mt-3"
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
            className = "p-5"
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                    figure = fig_distribution
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
                                dcc.Graph(
                                    figure = fig_profit
                                )
                            ]
                        )
                    ),
                    xs = 12, sm = 12, md = 6, lg = 6, xl = 6
                )
            ],
            className = "p-5"
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
            className = "p-5"
        )
    ],
    className = "container p-5"
)