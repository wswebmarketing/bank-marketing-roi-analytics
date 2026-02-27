from services.data_loader import load_bank_data
import pandas as pd
from tabulate import tabulate
from utils.segmentation import(
    build_segments_fixed,
    classify_segments
)
from utils.preprocessing import preprocess_data
from utils.simulation import(
    simulate_uniform,
    simulate_strategic,
    compare_scenarios
)
from pprint import pprint

def get_segments():
    """
    Executa o pipeline completo:
    - carrega dados
    - constrói segmentos
    - classifica
    """
    df = load_bank_data()
    df = preprocess_data(df)
    segments = build_segments_fixed(df)
    segments = classify_segments(segments)
    print(f"{tabulate(segments, headers = "keys", tablefmt = "grid")}\n")
    return segments

def executive_resume():
    #Implementa a lógica do backend para a página Home consumir esses dados
    segments = get_segments()
    total_segments = segments.shape[0]
    print(f"{total_segments}\n")

    gold_count = segments[segments["category"] == "Gold"].shape[0]
    print(f"{gold_count}\n")

    destructive_count = segments[segments["category"] == "Destructive"].shape[0]
    print(f"{destructive_count}\n")

    roi_gold = (
        segments[segments["category"] == "Gold"]["avg_roi"].mean()
        if gold_count > 0 else 0
    )
    print(f"{roi_gold}\n")

    return {
        "total_segments": total_segments,
        "gold_count": gold_count,
        "destructive_count": destructive_count,
        "roi_gold": roi_gold 
    }

def profit_by_category():
    #calcula o lucro médio para cada categoria de clientes
    segments = get_segments()
    print(f"{segments}")

    df_category = (
        segments
        .groupby("category")
        .agg(
            avg_profit = ("expected_profit", "mean")
        )
        .reset_index()
        .sort_values(by = "avg_profit", ascending = False)
    )
    print(f"{df_category}")
    return df_category

def execute_simulations(base_size = 100000):
    #Função responsável por realizar as simulações de acordo com a base de clientes do banco
    segments = get_segments()

    uniform = simulate_uniform(segments, base_size)
    print(f"{uniform}\n")

    strategic_distribution = {
        "Gold": 0.7,
        "Strong": 0.2,
        "Medium": 0.1,
        "Weak": 0,
        "Destructive": 0
    }

    strategic = simulate_strategic(
        segments,
        base_size,
        strategic_distribution
    )
    print(f"{strategic}\n")
    print(f"{compare_scenarios(uniform, strategic)}\n")
    return f"{compare_scenarios(uniform, strategic)}"