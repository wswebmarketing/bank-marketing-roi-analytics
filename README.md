# Bank Marketing Strategic Segmentation Dashboard

Strategic analytics dashboard built with **Python + Dash** to identify profitable customer segments in bank marketing campaigns and simulate strategic budget allocation scenarios based on **ROI and expected profitability**.

This project demonstrates how **data analytics can support strategic marketing decisions**, improving campaign efficiency and maximizing profitability.

---

# Project Overview

Marketing campaigns often treat the customer base uniformly, allocating resources without considering the profitability potential of each segment.

This project applies **data segmentation, profitability modeling, and scenario simulation** to answer a key strategic question:

**Where should marketing investment be concentrated to maximize ROI?**

The solution builds a segmentation model that evaluates each customer segment based on:

* Conversion rate
* Expected revenue
* Expected cost
* Expected profit
* Return on Investment (ROI)

The result is a **strategic classification of segments** and a **simulation model for budget redistribution**.

---

# Analytical Model

Customer segments are created by combining key demographic and campaign variables:

* Age group
* Account balance quartile
* Education level
* Contact type

For each segment the model calculates:

* Conversion Rate
* Campaign Volume
* Average Campaign Effort
* Expected Revenue
* Expected Cost
* Expected Profit
* ROI

Segments are then classified into strategic categories:

| Category    | Interpretation              |
| ----------- | --------------------------- |
| Gold        | Highly profitable segments  |
| Strong      | Strong ROI segments         |
| Medium      | Moderate profitability      |
| Weak        | Low profitability           |
| Destructive | Segments that destroy value |

This classification supports **data-driven marketing prioritization**.

---

# Dashboard Features

The project includes an interactive dashboard built with **Dash + Bootstrap**.

Main components:

### Executive KPIs

* Average Expected Profit
* Average ROI
* Highest Segment Profit
* Percentage of Gold Segments

### Strategic Visualizations

* Distribution of segments by category
* Average profit by category

### Full Segmentation Table

Detailed breakdown of all segments including profitability metrics.

### Scenario Simulation

The simulation module compares two strategies:

**Uniform Distribution**

Marketing investment distributed proportionally across all segments.

**Strategic Allocation**

Investment concentrated in high-ROI segments.

Example distribution used:

* Gold → 70%
* Strong → 20%
* Medium → 10%
* Weak → 0%
* Destructive → 0%

The dashboard calculates:

* Expected profit under each scenario
* Absolute difference
* Growth percentage

---

# Tech Stack

Python
Pandas
Dash
Dash Bootstrap Components
Plotly

---

# Project Structure

```
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
```

---

# Portuguese Summary

Este projeto apresenta um **modelo estratégico de segmentação de clientes para campanhas de marketing bancário**.

A análise identifica segmentos com maior potencial de lucratividade utilizando métricas como:

* taxa de conversão
* receita esperada
* custo esperado
* lucro esperado
* ROI

Os segmentos são classificados em categorias estratégicas (Gold, Strong, Medium, Weak e Destructive) permitindo direcionar investimentos de marketing de forma mais eficiente.

Além da análise, o dashboard inclui uma **simulação de cenários**, comparando:

* distribuição uniforme de investimento
* alocação estratégica focada em segmentos de alto ROI.

---

# Author

Wellington César
MarTech Consultant
Strategic Marketing Consultant
Growth Architecture

WS – Web Marketing
