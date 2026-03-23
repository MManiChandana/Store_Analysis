import matplotlib.pyplot as plt
import seaborn as sns
import os

# create outputs folder automatically
os.makedirs("outputs", exist_ok=True)


# 1. SALES TREND (ALL STORES)
def plot_sales_trend(monthly_data):
    
    plt.figure(figsize=(12,6))
    
    for store in monthly_data['STORE_NBR'].unique():
        store_data = monthly_data[monthly_data['STORE_NBR'] == store]
        plt.plot(store_data['MONTH'].astype(str), store_data['total_sales'], alpha=0.2)
    
    plt.title("Sales Trend Across All Stores")
    plt.xticks(rotation=90)
    
    plt.savefig("outputs/sales_trend.png")
    plt.close()


# 2. TRIAL vs CONTROL (MOST IMPORTANT)
def plot_trial_vs_control(monthly_data, trial_store, control_store):
    
    trial = monthly_data[monthly_data['STORE_NBR'] == trial_store]
    control = monthly_data[monthly_data['STORE_NBR'] == control_store]
    
    plt.figure(figsize=(10,5))
    
    plt.plot(trial['MONTH'].astype(str), trial['total_sales'], label='Trial', linewidth=2)
    plt.plot(control['MONTH'].astype(str), control['total_sales'], label='Control', linewidth=2)
    
    plt.title(f"Store {trial_store} vs {control_store}")
    plt.legend()
    plt.xticks(rotation=90)
    
    plt.savefig(f"outputs/trial_vs_control_{trial_store}.png")
    plt.close()


#3. CUSTOMERS COMPARISON
def plot_customers(monthly_data, trial_store, control_store):
    
    trial = monthly_data[monthly_data['STORE_NBR'] == trial_store]
    control = monthly_data[monthly_data['STORE_NBR'] == control_store]
    
    plt.figure(figsize=(10,5))
    
    plt.plot(trial['MONTH'].astype(str), trial['customers'], label='Trial Customers')
    plt.plot(control['MONTH'].astype(str), control['customers'], label='Control Customers')
    
    plt.title(f"Customers Comparison {trial_store}")
    plt.legend()
    plt.xticks(rotation=90)
    
    plt.savefig(f"outputs/customers_{trial_store}.png")
    plt.close()


# 4. TRANSACTIONS PER CUSTOMER
def plot_transactions(monthly_data, trial_store, control_store):
    
    trial = monthly_data[monthly_data['STORE_NBR'] == trial_store]
    control = monthly_data[monthly_data['STORE_NBR'] == control_store]
    
    plt.figure(figsize=(10,5))
    
    plt.plot(trial['MONTH'].astype(str), trial['txn_per_customer'], label='Trial')
    plt.plot(control['MONTH'].astype(str), control['txn_per_customer'], label='Control')
    
    plt.title(f"Transactions per Customer {trial_store}")
    plt.legend()
    plt.xticks(rotation=90)
    
    plt.savefig(f"outputs/transactions_{trial_store}.png")
    plt.close()


# 5. BEFORE vs AFTER BAR CHART
def plot_before_after(monthly_data, trial_store):
    
    trial = monthly_data[monthly_data['STORE_NBR'] == trial_store]
    
    pre = trial[trial['MONTH'] < '2019-02']
    post = trial[trial['MONTH'] >= '2019-02']
    
    labels = ['Before', 'After']
    values = [pre['total_sales'].mean(), post['total_sales'].mean()]
    
    plt.figure()
    plt.bar(labels, values)
    
    plt.title(f"Before vs After - Store {trial_store}")
    
    plt.savefig(f"outputs/before_after_{trial_store}.png")
    plt.close()


# 6. HEATMAP (ADVANCED)
def plot_heatmap(monthly_data):
    
    pivot = monthly_data.pivot(index='STORE_NBR', columns='MONTH', values='total_sales')
    
    plt.figure(figsize=(12,6))
    sns.heatmap(pivot, cmap='coolwarm')
    
    plt.title("Sales Heatmap")
    
    plt.savefig("outputs/heatmap.png")
    plt.close()