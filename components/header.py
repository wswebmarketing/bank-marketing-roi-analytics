import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

def header():
    nav_links = [
        dbc.NavLink(
            page["title"],
            href=page["path"],
            active="exact",
            className = "mx-2"
        )
        for page in dash.page_registry.values()
    ]        

    return html.Div(
        children = [
            dcc.Location(id="url"),

            # Bootstrap Theme dinâmico
            html.Link(
                id="theme-link",
                rel="stylesheet"
            ),

            # Font Awesome
            html.Link(
                rel="stylesheet",
                href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
            ),
            html.Header(
                children = [
                    dbc.Navbar(
                        id = "navbar",
                        color = "light",
                        expand = "md",
                        dark = False,
                        children = [
                            dbc.Container(
                                children = [
                                    dbc.NavbarBrand(
                                        href="/",
                                        children = [
                                            html.Img(
                                                id = "logo",
                                                src = "assets/logo-ws-web-marketing-preto.png"
                                            )
                                        ]
                                    ),
                                    dbc.NavbarToggler(id = "navbar-toggler", n_clicks = 0),
                                    dbc.Collapse(
                                        dbc.Nav(
                                            children = [
                                                *nav_links,
                                                dbc.Nav(
                                                    children = [
                                                        html.I(
                                                            className = "fa-solid fa-sun m-1", 
                                                            id = "theme-icon"
                                                        ),
                                                        dbc.Switch(
                                                            id = "theme-switch",
                                                            value = False
                                                        )
                                                    ],
                                                    className = "d-flex align-items-center"
                                                )
                                            ],
                                            className = "ms-auto",
                                            navbar = True
                                        ),
                                        id = "navbar-collapse",
                                        is_open = False,
                                        navbar = True
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )

@callback(
    Output("navbar-collapse", "is_open"),
    Input("navbar-toggler", "n_clicks"),
    Input("navbar-collapse", "is_open")
)

def toggle_navbar(n, is_open):
    if(n):
        return(not is_open)
    return is_open