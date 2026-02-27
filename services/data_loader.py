import pandas as pd


def load_bank_data(path = "data/bank-full.csv"):
    try:
        """
        Carrega a base de dados original do banco.
        Não aplica regra de negócio.
        Apenas leitura estruturada.
        """
        df = pd.read_csv(path, sep = ";")
        return df
    except OSError as error:
        print("Erro ao carregar a base de dados!")
        print(f"Erro: {error}")