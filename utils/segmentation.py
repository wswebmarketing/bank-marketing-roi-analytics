import pandas as pd 

def build_segments_fixed(df): 
    """ Aplica transformações necessárias para análise estratégica. """ 
    revenue_per_conversion = 800 
    cost_per_contract = 5 
    return build_segments_parametrized( 
        df, 
        revenue_per_conversion, 
        cost_per_contract 
    ) 

def build_segments_parametrized( 
    df, 
    revenue_per_conversion, 
    cost_per_contact 
): 
    """ Modelo profissional parametrizável. Permite simulação estratégica real. """ 
    segments = ( 
        df 
        .groupby(["age_group", "balance_group", "education", "contact"]) 
        .agg( 
            conversion_rate = ("conversion", "mean"), 
            volume = ("conversion", "count"), 
            avg_campaign = ("campaign", "mean") 
        ) 
        .reset_index() 
    ) 

    #receita esperada 
    segments["revenue_expected"] = ( 
        segments["conversion_rate"] * revenue_per_conversion 
    )

    #custo esperado 
    segments["expected_cost"] = ( 
        segments["avg_campaign"] * cost_per_contact 
    )

    #lucro esperado 
    segments["expected_profit"] = ( 
        segments["revenue_expected"] - segments["expected_cost"] 
    )
     
    #ROI 
    segments["avg_roi"] = ( 
        segments["expected_profit"] / segments["expected_cost"] 
    ) 
    return segments 

def classify_segments(segments, thresholds = None): 
    """ Classifica segmentos com base em faixas de lucro esperado. 
    thresholds deve ser um dicionário no formato: 
    { "Gold": 100, "Strong": 60, "Medium": 40, "Weak": 20 } 
    Valores representam limite mínimo de lucro esperado. """ 
    if(thresholds is None): 
        thresholds = { "Gold": 100, "Strong": 60, "Medium": 40, "Weak": 20 } 
        
    def categorize(profit): 
        if(profit >= thresholds["Gold"]): 
            return "Gold" 
        elif(profit >= thresholds["Strong"]): 
            return "Strong" 
        elif(profit >= thresholds["Medium"]): 
            return "Medium" 
        elif(profit >= thresholds["Weak"]): 
            return "Weak" 
        else: return "Destructive"     
    segments["category"] = segments["expected_profit"].apply(categorize) 
    return segments