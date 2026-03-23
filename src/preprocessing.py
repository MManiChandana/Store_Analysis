import pandas as pd

def load_and_prepare_data_with_eda(file_path="data/QVI_data.csv"):
    data = pd.read_csv(file_path)
    print(data.head(), "\n")

    print("===== Data Info =====")
    print(data.info(), "\n")
    print("===== Numeric Summary =====")
    print(data.describe(), "\n")

    # Unique Values (Categorical)
    cat_cols = data.select_dtypes(include='object').columns
    print("===== Categorical Columns Unique Values =====")
    for col in cat_cols:
        print(f"{col} - {data[col].nunique()} unique values")
        print(data[col].value_counts().head(10))
        print("\n")

    # Missing Values
    print("===== Missing Values Per Column =====")
    print(data.isnull().sum(), "\n")
    data.fillna(method='ffill', inplace=True)

    # Duplicates Check
    print(f"===== Duplicate Rows: {data.duplicated().sum()} =====\n")
    data.drop_duplicates(inplace=True)

    # Date Transformation
    data['DATE'] = pd.to_datetime(data['DATE'], format='%d-%m-%Y')
    data['MONTH'] = data['DATE'].dt.to_period('M')

    # Monthly Aggregation
    monthly_data = data.groupby(['STORE_NBR', 'MONTH']).agg({
        'TOT_SALES': 'sum',
        'LYLTY_CARD_NBR': pd.Series.nunique,
        'TXN_ID': 'count'
    }).reset_index()

    # Rename columns and calculate transactions per customer
    monthly_data.columns = ['STORE_NBR', 'MONTH', 'total_sales', 'customers', 'transactions']
    monthly_data['txn_per_customer'] = monthly_data['transactions'] / monthly_data['customers']

    print("===== Sample of Aggregated Monthly Data =====")
    print(monthly_data.head())

    return monthly_data