import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def run_analysis():
    try:
        # Load data from the root directory
        data = pd.read_excel('/app/Data.xlsx')
        logging.debug("Data loaded successfully:")
        logging.debug(data.head())  # Print the first few rows of data for debugging
        
        # Perform analysis
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
        logging.error(f"Error during analysis: {e}")
        return {'error': str(e)}
