# ============================================================
# ANALYSIS MODULE
# ============================================================


import pandas as pd
import numpy as np
from scipy.stats import pearsonr



def get_missing_report(df: pd.DataFrame) -> str:
    """Returns a formatted report of missing values per column."""
    print("  Generating missing value report...")
    report = df.isnull().sum()
    report = report[report > 0].sort_values(ascending=False)
    
    if report.empty:
        return "  No missing values detected."
    
    report_str = "\n".join([f"  - {col}: {count}" for col, count in report.items()])
    return report_str


def summary_statistics(df: pd.DataFrame):
    """
    1. Statistical summaries: mean, median, variance, std deviation, min, max, unique count.
    """
    print("\n## 1. Calculating Summary Statistics (Imperative Sequence)...")
    
  
    numeric_df = df.select_dtypes(include=np.number)
    
    if numeric_df.empty:
        print("  [WARN] No numeric columns found for full statistical summaries.")
    else:
       
        stats = pd.DataFrame()
        
        print("  > Calculating central tendencies and dispersion...")
       
        stats['count'] = numeric_df.count()
        stats['mean'] = numeric_df.mean()
        stats['median'] = numeric_df.median()
        stats['variance'] = numeric_df.var()
        stats['std_dev'] = numeric_df.std()
        stats['min'] = numeric_df.min()
        stats['max'] = numeric_df.max()

        print("\n--- Summary Statistics Results (Numeric Columns) ---")
        print(stats.round(2).to_string())
        print("--------------------------------------------------")

   
    print("  > Calculating Unique Value Counts for all columns...")
    unique_counts = df.apply(lambda x: len(x.unique()))
    
    print("\n--- Unique Value Counts per Column ---")
    print(unique_counts.to_string())
    print("--------------------------------------")


def correlation_analysis(df: pd.DataFrame, col1: str, col2: str):
    """
    2. Correlation, trend detection: Pearson correlation coefficient and interpretation.
    """
    print(f"\n## 2. Running Correlation Analysis for '{col1}' and '{col2}' (Imperative)...")
    
    
    if col1 not in df.columns or col2 not in df.columns:
        print(f"  [ERROR] Columns '{col1}' or '{col2}' not found in the dataset.")
        return
        
    if not (pd.api.types.is_numeric_dtype(df[col1]) and pd.api.types.is_numeric_dtype(df[col2])):
        print("  [ERROR] Correlation requires both columns to be numeric.")
        return

   
    cleaned_data = df[[col1, col2]].dropna()
    x = cleaned_data[col1]
    y = cleaned_data[col2]
    
    if len(x) < 2:
        print("  [WARN] Not enough non-missing data points for correlation calculation.")
        return

    
    correlation_coefficient, p_value = pearsonr(x, y)
    
   
    interpretation = "No Significant Linear Trend."
    r = correlation_coefficient
    
    if r >= 0.9:
        interpretation = "Very Strong Positive Trend."
    elif r > 0.7:
        interpretation = "Strong Positive Trend."
    elif r > 0.3:
        interpretation = "Moderate Positive Trend."
    elif r > 0.0:
        interpretation = "Weak Positive Trend."
    elif r <= -0.9:
        interpretation = "Very Strong Negative Trend."
    elif r < -0.7:
        interpretation = "Strong Negative Trend."
    elif r < -0.3:
        interpretation = "Moderate Negative Trend."
    elif r < 0.0:
        interpretation = "Weak Negative Trend."

    print(f"\n--- Correlation Results ({col1} vs {col2}) ---")
    print(f"  Pearson Coefficient (r): {correlation_coefficient:.4f}")
    print(f"  Interpretation: {interpretation}")
    print("---------------------------------------------")


def dataset_overview(df: pd.DataFrame):
    """
    3. Dataset summary: number of rows, columns, data types, missing-value overview.
    """
    print("\n## 3. Generating Dataset Overview (Imperative Steps)...")
    
    
    num_rows, num_cols = df.shape 
    print(f"  > Number of Rows (Records): {num_rows}")
    print(f"  > Number of Columns (Features): {num_cols}")
    
   
    print("\n--- Data Types per Column ---")
    print(df.dtypes.to_string())
    
   
    print("\n--- Missing Value Overview ---")
    missing_report = get_missing_report(df)
    print(missing_report)
    print("---------------------------------")


def detect_outliers(df: pd.DataFrame, column: str):
    """
    4. Outlier detection using the IQR method. Prints the number of outliers.
    """
    print(f"\n## 4. Detecting Outliers in Column '{column}' using IQR (Imperative)...")
    
    if column not in df.columns:
        print(f"  [ERROR] Column '{column}' not found in the dataset.")
        return
        
    if not pd.api.types.is_numeric_dtype(df[column]):
        print(f"  [ERROR] Outlier detection requires column '{column}' to be numeric.")
        return

   
    data = df[column].dropna()
    if data.empty:
        print("  [WARN] Column is empty after dropping NaNs. Cannot detect outliers.")
        return

    
    Q1 = data.quantile(0.25) 
    Q3 = data.quantile(0.75) 
    IQR = Q3 - Q1            
    
   
    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)
    
   
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    num_outliers = len(outliers)
    
    
    print("\n--- IQR Outlier Detection Results ---")
    print(f"  Q1 (25th percentile): {Q1:,.2f}")
    print(f"  Q3 (75th percentile): {Q3:,.2f}")
    print(f"  IQR (Q3 - Q1): {IQR:,.2f}")
    print(f"  Lower Bound: {lower_bound:,.2f}")
    print(f"  Upper Bound: {upper_bound:,.2f}")
    print(f"  Number of Outliers Detected: **{num_outliers}** ({(num_outliers / len(data) * 100):.2f}%)")
    
    if num_outliers > 0:
        print("  Sample Outliers:")
        print(outliers.head(5).to_string())
    
    print("-------------------------------------")



if __name__ == '__main__':
  
    print("=============================================================")
    print("       STARTING analyze_data.py DEMONSTRATION")
    print("=============================================================")
    
    
    data = {
        'Sales': [100.0, 150.5, 95.2, 1000.0, 120.0, 110.5, 130.0, 100.0, np.nan, 140.0],
        'Cost': [50.0, 70.0, 45.0, 450.0, 60.0, 55.0, 65.0, 50.0, 70.0, np.nan],
        'Region': ['East', 'West', 'East', 'Central', 'West', 'East', 'West', 'East', 'Central', 'West'],
        'Is_Seasonal': [True, False, True, True, False, True, False, True, False, True],
        'Order_Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', 
                                     '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
                                     pd.NaT, '2023-01-10']),
        'Notes': ['A', 'B', None, 'D', 'E', 'F', 'G', 'H', 'I', 'J'] 
    }
    test_df = pd.DataFrame(data)

   
    df_to_analyze = test_df.copy()

    
    dataset_overview(df_to_analyze)

   
    summary_statistics(df_to_analyze)
    
   
    correlation_analysis(df_to_analyze, 'Sales', 'Cost')
    
    
    detect_outliers(df_to_analyze, 'Sales')
    
    print("\n=============================================================")
    print("          ANALYSIS MODULE DEMONSTRATION COMPLETE")
    print("=============================================================")