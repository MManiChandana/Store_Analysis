import numpy as np
import pandas as pd

def calculate_similarity(monthly_data, trial_store):
    
    trial = monthly_data[monthly_data['STORE_NBR'] == trial_store]
    control_data = monthly_data[~monthly_data['STORE_NBR'].isin([77,86,88])]
    
    results = []
    
    for store in control_data['STORE_NBR'].unique():
        
        control = monthly_data[monthly_data['STORE_NBR'] == store]
        
        merged = pd.merge(trial, control, on='MONTH', suffixes=('_trial','_control'))
        
        if len(merged) < 6:
            continue
        
        corr_sales = merged['total_sales_trial'].corr(merged['total_sales_control'])
        corr_customers = merged['customers_trial'].corr(merged['customers_control'])
        
        score = np.nanmean([corr_sales, corr_customers])
        
        results.append((store, score))
    
    results = sorted(results, key=lambda x: x[1], reverse=True)
    
    return results[0]