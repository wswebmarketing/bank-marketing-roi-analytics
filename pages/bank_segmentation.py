import dash
from dash import html, dcc, Output, Input, callback, dash_table
import dash_bootstrap_components as dbc
from services.analytics import(
    get_segments,
    executive_resume
)
from utils.simulation import(
    simulate_uniform,
    simulate_strategic,
    compare_scenarios
)
#LIBS UTILIZADAS APENAS PARA DESENVOLVIMENTO
'''from tabulate import tabulate
from pprint import pprint'''
import pandas as pd
import plotly.express as px

segments = get_segments()
resume = executive_resume()

avg_profit = round(segments["expected_profit"].mean(), 2)

avg_roi = round(segments["avg_roi"].mean(), 2)

max_profit = round(segments["expected_profit"].max(), 2)

percent_gold = round(
    (resume["gold_count"] / resume["total_segments"]) * 100
, 2)

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
    color = "category",
    title = "Distribuição Estratégica dos Segmentos",
    labels = {
        "category": "Categoria",
        "count": "Frequência"
    }
)
fig_distribution.update_traces(textposition = "outside"),
fig_distribution.update_layout(showlegend = False)

profit_by_category = (
    segments
    .groupby("category")["expected_profit"]
    .mean()
    .reset_index()
)

fig_profit = px.bar(
    profit_by_category,
    x = "category",
    y = "expected_profit",
    text = "expected_profit",
    color = "category",
    title = "Lucro Médio por Categoria",
    labels = {
        "category": "Categoria",
        "expected_profit": "Lucro Esperado ($)"
    }
)
fig_profit.update_traces(
    texttemplate = "%{text:.2f}",
    textposition = "outside"
)
fig_profit.update_layout(showlegend = False)

table_data = segments.round(2).to_dict("records")
table_columns = [{"name": col, "id": col} for col in segments.columns]

dash.register_page(
    __name__,
    path = "/segmentacao-bancaria",
    title = "Segmentação Bancária"
)

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            "Segmentação Estratégica de Clientes",
                            className = "fw-bold text-center"
                        ),
                        html.P(
                            "Modelo analítico baseado em lucratividade esperada e ROI para redistribuição estratégica de orçamento.",
                            className = "text-justify mt-3"
                        )
                    ],
                    width = 12
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H6(
                                    "Lucro Médio Geral",
                                    className = "text-center fw-bold"
                                ),
                                html.H3(
                                    f"${avg_profit:,.2f}",
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
                                    "ROI Médio Geral",
                                    className = "text-center fw-bold"
                                ),
                                html.H3(
                                    f"{avg_roi:,.2f}",
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
                                    "Maior Lucro por Segmento",
                                    className = "text-center fw-bold"
                                ),
                                html.H3(
                                    f"${max_profit:,.2f}",
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
                                    "Percentual de Segmentos Gold sobre o total",
                                    className = "text-center fw-bold"
                                ),
                                html.H3(
                                    f"{percent_gold:,.2f}%",
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
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5(
                                        "Distribuição por Categoria",
                                        className = "text-center fw-bold"
                                    ),
                                    dcc.Graph(
                                        figure = fig_distribution
                                    )
                                ]
                            )
                        )
                    ],
                    xs = 12, sm = 12, md = 6, lg = 6, xl = 6
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5(
                                        "Lucro Médio por Categoria",
                                        className = "text-center fw-bold"
                                    ),
                                    dcc.Graph(
                                        figure = fig_profit
                                    )
                                ]
                            )
                        )
                    ],
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
                                html.H5(
                                    "Detalhamento Completo dos Segmentos",
                                    className = "fw-bold text-center"
                                ),
                                dash_table.DataTable(
                                    data = table_data,
                                    columns = table_columns,
                                    page_size = 15,
                                    style_table = {
                                        "overflowY": "auto"
                                    },
                                    style_cell = {
                                        "textAlign": "center"
                                    },
                                    style_header = {
                                        "textAlign": "center",
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
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4(
                                        "Simulação de Cenários",
                                        className = "fw-bold text-center"
                                    ),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Label(
                                                        "Tamanho da Base",
                                                        className = "text-center fw-bold mb-2"
                                                    ),
                                                    dbc.Input(
                                                        id = "input_base_size",
                                                        type = "number",
                                                        value = 100000,
                                                        min = 1000,
                                                        step = 1000
                                                    ),
                                                    dbc.Button(
                                                        "Simular",
                                                        id = "simulate_button",
                                                        color = "primary",
                                                        className = "mt-2 mb-4 w-100"
                                                    )
                                                ],
                                                xs = 12, sm = 12, md = 4, lg = 4, xl = 4
                                            )
                                        ]
                                    ),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.H5(
                                                        id = "result_uniform",
                                                        className = "text-center fw-bold"
                                                    )
                                                ],
                                                xs = 12, sm = 12, md = 3, lg = 3, xl = 3
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H5(
                                                        id = "result_strategic",
                                                        className = "text-center fw-bold"
                                                    )
                                                ],
                                                xs = 12, sm = 12, md = 3, lg = 3, xl = 3
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H5(
                                                        id = "result_difference",
                                                        className = "text-center fw-bold"
                                                    )
                                                ],
                                                xs = 12, sm = 12, md = 3, lg = 3, xl = 3
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H5(
                                                        id = "result_growth",
                                                        className = "text-center fw-bold"
                                                    )
                                                ],
                                                xs = 12, sm = 12, md = 3, lg = 3, xl = 3
                                            )
                                        ]
                                    )
                                ]
                            )
                        )
                    ],
                    width = 12
                )
            ],
            className = "p-5"
        )
    ],
    className = "container p-5"
)

@callback(
    Output("result_uniform", "children"),
    Output("result_strategic", "children"),
    Output("result_difference", "children"),
    Output("result_growth", "children"),
    Input("simulate_button", "n_clicks"),
    Input("input_base_size", "value")
)

def run_simulation(n_clicks, base_size):
    if(not n_clicks):
        return "", "", "", ""
    
    distribution = {
        "Gold": 0.7,
        "Strong": 0.2,
        "Medium": 0.1,
        "Weak": 0,
        "Destructive": 0
    }

    uniform_profit = simulate_uniform(segments, base_size)
    
    strategic_profit = simulate_strategic(segments, base_size, distribution)
    
    comparison = compare_scenarios(uniform_profit, strategic_profit)

    return(
        f"Lucro Uniforme: ${comparison["uniform_profit"]}",
        f"Lucro Estratégico: ${comparison["strategic_profit"]}",
        f"Diferença: ${comparison["difference"]}",
        f"Crescimento: {comparison["growth_percentual"]}%"
    )