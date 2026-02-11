# app/services/kpi_engine.py

import pandas as pd

def calculate_profit_margin(df: pd.DataFrame) -> float:
    revenue = df["revenue"].sum()
    costs = df["cost"].sum()
    if revenue == 0:
        return 0.0
    return round((revenue - costs) / revenue * 100, 2)
