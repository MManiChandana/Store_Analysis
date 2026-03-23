from preprocessing import load_and_prepare_data
from similarity import calculate_similarity
from visualization import plot_trial_vs_control

# Step 1: Load data
monthly_data = load_and_prepare_data()
print("Total Stores:", monthly_data['STORE_NBR'].nunique())
# Step 2: Find control stores
control_77 = calculate_similarity(monthly_data, 77)
control_86 = calculate_similarity(monthly_data, 86)
control_88 = calculate_similarity(monthly_data, 88)

print("Store 77 Control:", control_77)
print("Store 86 Control:", control_86)
print("Store 88 Control:", control_88)

# Step 3: Plot
from visualization import *

# generate all visuals
plot_sales_trend(monthly_data)

plot_trial_vs_control(monthly_data, 77, 41)
plot_trial_vs_control(monthly_data, 86, 229)
plot_trial_vs_control(monthly_data, 88, 178)

plot_customers(monthly_data, 77, control_77[0])
plot_customers(monthly_data, 86, control_86[0])
plot_customers(monthly_data, 88, control_88[0])

plot_transactions(monthly_data, 77, control_77[0])
plot_transactions(monthly_data, 86, control_86[0])
plot_transactions(monthly_data, 88, control_88[0])

plot_before_after(monthly_data, 77)
plot_before_after(monthly_data, 86)
plot_before_after(monthly_data, 88)


plot_heatmap(monthly_data)