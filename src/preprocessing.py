import pandas as pd

def load_and_prepare_data():
    data = pd.read_csv("data/QVI_data.csv")
    
    data['DATE'] = pd.to_datetime(data['DATE'], format='%d-%m-%Y')
    data['MONTH'] = data['DATE'].dt.to_period('M')
    
    monthly_data = data.groupby(['STORE_NBR', 'MONTH']).agg({
        'TOT_SALES': 'sum',
        'LYLTY_CARD_NBR': pd.Series.nunique,
        'TXN_ID': 'count'
    }).reset_index()
    
    monthly_data.columns = ['STORE_NBR', 'MONTH', 'total_sales', 'customers', 'transactions']
    monthly_data['txn_per_customer'] = monthly_data['transactions'] / monthly_data['customers']
    
    return monthly_data