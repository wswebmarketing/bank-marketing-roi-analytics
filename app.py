import dash
from dash import Dash, html, callback, Output, Input
from components.header import header
import dash_bootstrap_components as dbc

LIGHT_THEME = dbc.themes.FLATLY
DARK_THEME = dbc.themes.CYBORG

app = Dash(
    __name__,
    use_pages = True,
    suppress_callback_exceptions = True,
)

app.layout = html.Div([
    header(),
    html.Div(
        dash.page_container,
        id = "page-container"
    )
])

@callback(
    Output("theme-link", "href"),
    Output("theme-icon", "className"),
    Output("navbar", "color"),
    Output("navbar", "dark"),
    Output("logo", "src"),
    Output("page-container", "className"),
    Input("theme-switch", "value")
)

def update_theme(toggle):
    if(toggle):
        return(
            DARK_THEME, 
            "fa-solid fa-moon text-white me-2",
            "dark",
            True,
            "assets/logo-ws-web-marketing-branco.png",
            "text-white"
        )
    return(
        LIGHT_THEME, 
        "fa-solid fa-sun text-warning me-2",
        "light",
        False,
        "assets/logo-ws-web-marketing-preto.png",
        "text-dark"
    )

if(__name__ == "__main__"):
    app.run(debug = True)