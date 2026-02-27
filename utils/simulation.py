import pandas as pd

def simulate_uniform(segments, base_size):
    """
    Distribui a base proporcionalmente ao volume real.
    """
    avg_profit_by_category = (
        segments
        .groupby("category")["expected_profit"]
        .mean()
    )
    volume_by_category = (
        segments
        .groupby("category")["expected_profit"]
        .sum()
    )
    proportion = volume_by_category / volume_by_category.sum()
    total_profit = sum(
        proportion[c] * base_size * avg_profit_by_category[c]
        for c in avg_profit_by_category.index
    )
    return total_profit

def simulate_strategic(segments, base_size, distribution):
    """
    Distribuição estratégica definida manualmente.

    distribuicao exemplo:

    {
        "Gold": 0.7,
        "Strong": 0.2,
        "Medium": 0.1,
        "Weak": 0,
        "Destructive": 0
    }
    """
    avg_profit_by_category = (
        segments
        .groupby("category")["expected_profit"]
        .mean()
    )
    total_profit = sum(
        distribution.get(c, 0) * base_size * avg_profit_by_category[c]
        for c in avg_profit_by_category.index
    )
    return total_profit
    
def compare_scenarios(uniform_profit, strategic_profit):
    """
    Retorna diferença absoluta e percentual.
    """
    difference = strategic_profit - uniform_profit
    if(uniform_profit == 0):
        percentual = 0
    else:
        percentual = (difference / uniform_profit) * 100
    return {
        "uniform_profit": round(float(uniform_profit), 2),
        "strategic_profit": round(float(strategic_profit), 2),
        "difference": round(float(difference), 2),
        "growth_percentual": round(float(percentual), 2)
    }