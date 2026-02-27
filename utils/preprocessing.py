import pandas as pd

def preprocess_data(df):
    """
    Aplica transformações necessárias
    para análise estratégica.
    """
    #Faixas etárias
    df["age_group"] = pd.cut(
        df["age"],
        bins = [18, 25, 35, 45, 55, 65, 100],
        labels = ["18-25", "26-35", "36-45", "46-55", "56-65", "65+"]
    )
    #Quartis de saldo
    df["balance_group"] = pd.qcut(
        df["balance"],
        4,
        labels = ["Q1", "Q2", "Q3", "Q4"]
    )
    #Conversão binária
    df["conversion"] = df["y"].map({"yes": 1, "no": 0})
    return df