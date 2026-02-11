from app.services.etl_service import (
    extract_sales,
    transform_sales,
    load_sales,
    build_financial_summary
)

def run():
    sales = extract_sales()
    sales_clean = transform_sales(sales)
    load_sales(sales_clean)

    summary = build_financial_summary()
    print("ETL completed successfully")
    print(summary)

if __name__ == "__main__":
    run()
