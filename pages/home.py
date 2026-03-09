import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from services.analytics import(
    get_segments,
    executive_resume
)
#LIBS UTILIZADAS APENAS PARA DESENVOLVIMENTO
'''from pprint import pprint
from tabulate import tabulate'''
import pandas as pd
import plotly.express as px

segments = get_segments()
resume = executive_resume()

#gráfico utilizado apenas para desenvolvimento da paǵina
'''df_placeholder = pd.DataFrame({
    "category": ["Gold", "Strong", "Medium", "Weak", "Destructive"],
    "avg_profit": [120, 70, 48, 27, 14]
})'''

category_distribution = (
    segments["category"]
    .value_counts()
    .reset_index()
)
category_distribution.columns = ["category", "count"]

order = ["Gold", "Strong", "Medium", "Weak", "Destructive"]
category_distribution["category"] = pd.Categorical(
    category_distribution["category"],
    categories = order,
    ordered = True
)
category_distribution = category_distribution.sort_values("category")

fig = px.bar(
    category_distribution,
    x = "category",
    y = "count",
    title = "Distribuição Estratégica dos Segmentos",
    color = "category",
    text = "count",
    template = "plotly"
)
fig.update_traces(textposition = "outside")
fig.update_layout(showlegend = False)

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
                                html.H6(
                                    "Total de Segmentos",
                                    className = "fw-bold text-center"
                                ),
                                html.H3(
                                    f"{resume["total_segments"]}",
                                    className = "fw-bold card-text text-center"
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
                                    "Segmentos Gold",
                                    className = "fw-bold text-center"
                                ),
                                html.H3(
                                    f"{resume["gold_count"]}",
                                    className = "fw-bold card-text text-center"
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
                                    "ROI Médio Gold",
                                    className = "fw-bold text-center"
                                ),
                                html.H3(
                                    f"{resume["roi_gold"]:,.2f}",
                                    className = "fw-bold card-text text-center"
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
                                    "Segmentos Destrutivos",
                                    className = "fw-bold text-center"
                                ),
                                html.H3(
                                    f"{resume["destructive_count"]}",
                                    className = "fw-bold card-text text-center"
                                )
                            ]
                        )
                    ),
                    xs = 12, sm = 12, md = 3, lg = 3, xl = 3
                )
            ],
            className = "p-3"
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
                                    figure = fig
                                )
                            ]
                        )
                    )
                )
            ],
            className = "p-3"
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5(
                                        "Segmentação Completa",
                                        className = "fw-bold text-center"
                                    ),
                                    html.P(
                                        "Visualização técnica detalhada de todos os segmentos.",
                                        className = "card-text text-justify"
                                    ),
                                    dbc.Button(
                                        "Ver detalhes",
                                        color = "primary",
                                        href = "/segmentacao-bancaria",
                                        className = "w-100 mt-3"
                                    )
                                ]
                            )
                        )
                    ],
                    xs = 12, sm = 12, md = 4, lg = 4, xl = 4
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5(
                                        "Classificação Estratégica",
                                        className = "fw-bold text-center"
                                    ),
                                    html.P(
                                        "Análise categorizada por potencial de lucro.",
                                        className = "card-texttext-justify"
                                    ),
                                    dbc.Button(
                                        "Ver classificação",
                                        color = "primary",
                                        href = "/classificacao-estrategica",
                                        className = "w-100 mt-3"
                                    )
                                ]
                            )
                        )
                    ],
                    xs = 12, sm = 12, md = 4, lg = 4, xl = 4
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5(
                                        "Simulação de Cenários",
                                        className = "fw-bold text-center"
                                    ),
                                    html.P(
                                        "Projeções financeiras sob diferentes estratégias.",
                                        className = "card-text text-justify"
                                    ),
                                    dbc.Button(
                                        "Ver cenários",
                                        color = "primary",
                                        href = "/simulacao-cenarios",
                                        className = "w-100 mt-3"
                                    )
                                ]
                            )
                        )
                    ],
                    xs = 12, sm = 12, md = 4, lg = 4, xl = 4
                )
            ],
            className = "p-3"
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4(
                                        "Conclusão Estratégica",
                                        className = "text-center fw-bold"
                                    ),
                                    html.P(
                                        "A análise demonstra a necessidade de realocação imediata de orçamento para segmentos Gold e Strong, evitando desperdício de capital em segmentos destrutivos. A aplicação de um modelo estratégico gera crescimento significativo de ROI.",
                                        className = "card-text text-justify"
                                    )
                                ]
                            )
                        )
                    ]
                )
            ],
            className = "p-3"
        )
    ]
)

