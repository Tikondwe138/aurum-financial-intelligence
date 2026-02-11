import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
RAW_DATA = BASE_DIR / "data" / "raw"
PROCESSED_DATA = BASE_DIR / "data" / "processed"


def extract_sales() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "sales.csv", parse_dates=["date"])


def extract_expenses() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "expenses.csv", parse_dates=["date"])


def extract_products() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA / "products.csv")


def transform_sales(sales: pd.DataFrame) -> pd.DataFrame:
    sales["month"] = sales["date"].dt.to_period("M").astype(str)
    return sales


def load_sales(sales: pd.DataFrame):
    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)
    sales.to_csv(PROCESSED_DATA / "sales_clean.csv", index=False)


def build_financial_summary():
    sales = extract_sales()
    expenses = extract_expenses()

    monthly_sales = sales.groupby(sales["date"].dt.to_period("M"))["revenue"].sum()
    monthly_expenses = expenses.groupby(expenses["date"].dt.to_period("M"))["amount"].sum()

    summary = pd.concat([monthly_sales, monthly_expenses], axis=1).fillna(0)
    summary.columns = ["revenue", "expenses"]
    summary["profit"] = summary["revenue"] - summary["expenses"]

    summary.reset_index(inplace=True)
    summary.rename(columns={"date": "month"}, inplace=True)

    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)
    summary.to_csv(PROCESSED_DATA / "financial_summary.csv", index=False)

    return summary
