# Bank Marketing Strategic Segmentation Dashboard

## Live Demo

Access the deployed analytical dashboard

[https://bank-marketing-roi-analytics.onrender.com]

## Profitability-Oriented Customer Intelligence

Analytical dashboard designed to identify high-value customer segments in marketing campaigns and optimize budget allocation through profitability and ROI analysis

This project combines customer segmentation, profitability modelling, and scenario simulation to support data-driven marketing decisions and improve campaign efficiency.

# [PT]

## Resumo

Este projeto apresenta uma solução analítica de segmentação estratégica de clientes voltada para campanhas de marketing.

O objetivo é identificar segmentos com maior potencial de lucratividade e otimizar a distribuição de investimentos com base em métricas de desempenho e retorno financeiro.

A análise integra:

- segmentação de clientes;
- modelagem de lucratividade;
- análise de ROI;
- simulação de cenários;
- visualização interativa.

## Objetivo Estratégico

Campanhas de marketing frequentemente distribuem investimentos de forma uniforme, sem considerar o potencial de retorno de cada segmento.

Este projeto busca responder uma questão estratégica central:

### Onde o investimento de marketing deve ser concentrado para maximizar ROI e lucratividade?

A solução cria um modelo analítico capaz de classificar segmentos de clientes com base em:

- taxa de conversão;
- receita esperada;
- custo esperado;
- lucro esperado;
- retorno sobre investimento (ROI)

O resultado é uma estrutura de priorização orientada a dados.

## Modelo Analítico

Os segmentos foram construídos combinando variáveis relevantes relacionadas ao perfil do cliente e comportameneto de campanha:

- faixa etária;
- quartil de saldo financeiro;
- nível educacional;
- tipo de contato.

Para cada segmento o sistema calcula:

- taxa de conversão;
- volume de campanhas;
- esforço médio da campanha;
- receita esperada;
- custo esperado;
- lucro esperado;
- ROI.

## Classificação Estratégica dos segmentos

Os segmentos são classificados em categorias analíticas:

| Categoria | Interpretação |
|:---:|:---:|
| Gold | Segmentos altamente lucrativos |
| Strong | Segmentos com forte retorno |
| Medium | Rentabilidade moderada |
| Weak | Baixa rentabilidade |
| Destructive | Segmentos que destroem valor|

Essa classificação permite direcionar investimentos de forma mais eficiente.

## Funcionalidades do Dashboard

O dashboard foi desenvolvido com foco em inteligência analítica e experiÊncia de uso.

### KPIs Executivos

- lucro médio esperado;
- ROI médio;
- maior lucro por segmento;
- percentual de segmentos Gold.

## Visualizações Estratégicas

- distribuição de segmentos por categoria;
- lucro médio por categoria;
- distribuição analítica dos segmentos.

## Tabela Completa de Segmentação

Visualização detalhada contendo:

- métricas financeiras;
- métricas de conversão;
- classificação estratégica;
- indicadores de rentabilidade.

## Simulação de Cenários

O projeto inclui um módulo de simulação para comparação de estratégias de investimento.

### Distribuição Uniforme

Investimento distribuído proporcionalmente entre todos os segmentos.

### Alocação Estratégica

Investimento concentrado em segmentos com maior ROI.

### Exemplo de distribuição:

- Gold → 70%
- Strong → 20%
- Medium → 10%
- Weak → 0%
- Destructive → 0%

O sistema calcula:

- lucro esperado;
- diferença absoluta;
- crescimento percentual;
- impacto financeiro da estratégia.

## Estrutura Analítica do Projeto

O projeto foi organizado em módulos para melhorar:

- escalabilidade;
- manutenção;
- separação de responsabilidades;
- evolução futura.

### Estrutura

project
│
├── data
│   └── bank-full.csv
│
├── services
│   ├── data_loader.py
│   └── analytics.py
│
├── utils
│   ├── preprocessing.py
│   ├── segmentation.py
│   └── simulation.py
│
├── components
│   └── header.py
│
├── pages
│   ├── home.py
│   └── bank_segmentation.py
│
├── assets
│
└── app.py

## Responsividade e Experiência de Uso

O dashboard foi ajustado para diferentes dispositivos e resoluções, priorizando:

- legibilidade analítica;
- organização visual;
- responsividade dos gráficos;
- experiência mobile;
- clareza na interpretação dos dados.

## Tecnologias Utilizadas

- Python
- Pandas
- Dash
- Plotly
- Dash Bootstrap Components

## Deployment

This dashboard is publicity deployed using Render.

Production deployment includes:

- responsive analytical interface;
- cloud deployment architecture;
- product dependency management;
- scalable dashboard structure;
- responsive visualization system.

## Roadmap de Evolução

Possíveis evoluções futuras:

- modelagem preditiva de conversão;
- clusterização avançada;
- integração com APIs;
- análises preditivas de ROI;
- inteligência orientada à retenção.

## Sobre a WS - Web Marketing

A WS - Web Marketing atua na interseção entre marketing, dados e tecnologia (MarTech), desenvolvendo soluções analíticas voltadas para inteligência de mercado, crescimento sustentável e tomada de decisão baseada em dados.

Este projeto representa um case de Marketing Analytics orientado à lucratividade e otimização de campanhas.

# [EN]

## Summary

This project presents a strategic customer segmentation solution focused on marketing campaign profitability optimization.

The dashboard identifies high-value customer segments and supports investment allocation decisions through ROI and profitability analysis.

The solution combines:

- customer segmentation;
- profitability modeling;
- ROI analysis;
- scenario simulation;
- interactive visualization.

## Strategic Objective

Marketing campaigns often distribute investments uniformly without considering the profitability potential of each segment.

This project aims to answer a key business question:

**Where should marketing investment be concentrated to maximize ROI and profitability?**

The solution builds an analytical model capable of classifying customer segments based on:

- conversion rate;
- expected revenue;
- expected cost;
- expected profit;
- return on investment (ROI).

The result is a data-driven prioritization framework.

## Analytical Model

Customer segments were created by combining relevant campaign and demographic variables:

- age group;
- financial balance quartile;
- education level;
- contact type.

For each segment the system calculates:

- conversion rate;
- campaign volume;
- average campaign effort;
- expected revenue;
- expected cost;
- expected profit;
- ROI.

## Strategic Segment Classification

Segments are classified into analytical categories:

| Category | Interpretation |
|:---:|:---:|
| Gold | Highly profitable segments |
| Strong | High ROI segments |
| Medium | Moderate profitability |
| Weak | Low profitability |
| Destructive | Value-destroying segment |

This classification supports more efficient investment allocation.

## Dashboard Features

The dashboard was designed focusing on analytical intelligence and user experience.

**Executive KPIs**

- average expected profit;
- average ROI;
- highest segment profit;
- percentage of Gold Segments.

## Strategic Visualizations

- segment distribution by category;
- average profit by category;
- analytical segment distribution.

## Complete Segmentation Table

Detailed analytical table including:

- financial metrics;
- conversion metrics;
- strategic classification;
- profitability indicators.

## Scenario Simulation

The project includes a scenario simulation module for comparing investment allocation strategies.

### Uniform Distribution

Marketing investment distributed proportionally across all segments.

### Strategic Allocation

Investment concentrated in higher ROI segments.

**Example allocation:**

- Gold → 70%
- Strong → 20%
- Medium → 10%
- Weak → 0%
- Destructive → 0

The system calculates:

- expected profit;
- absolute difference;
- growth percentage;
- financial impact.

## Responsiveness and User Experience

The dashboard was optimized for different devices and resolutions, prioritizing:

- analytical readability;
- visual organization;
- responsive charts;
- mobile experience;
- clarity in data interpretation.

## Techonlogies Used

- Python
- Pandas
- Dash
- Plotly
- Dash Bootstrap Components

## Future Roadmap

Possible future improvements:

- predictive conversion modeling;
- advanced clustering;
- API integrations;
- predictive ROI analysis;
- retention-oriented intelligence.

## About WS - Web Marketing

WS - Web Marketing operates at the intersection of marketing, data, and technology (MarTech), developing analytical solutions focused on market intelligence, sustainable growth, and data-driven decision-making.

This repository represents a Marketing Analytics showcase project focused on profitability optimization and campaign intelligence.

## How to Run

```bash
pip install -r requirements.txt
python app.py
```