import pandas as pd

def run_analysis():
    try:
        # Load data
        print("Reading data...")
        data = pd.read_excel('Data.xlsx')
        print(data.head())
        
        # Perform analysis (e.g., calculate mean)
        mean_value = data['value'].mean()
        median_value = data['value'].median()
        sum_metric1 = data['metric1'].sum()
        sum_metric2 = data['metric2'].sum()

        return {
            'mean': mean_value,
            'median': median_value,
            'sum_metric1': sum_metric1,
            'sum_metric2': sum_metric2
        }
    except Exception as e:
        print(f"Error: {e}")
        return {}
