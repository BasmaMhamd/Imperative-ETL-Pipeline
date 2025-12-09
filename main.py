from src import load_data, show_data_info, auto_handle_missing
from src.visualize_data import plot_bar, plot_line, plot_histogram
import pandas as pd


df = load_data("csv", "data/raw/dirty_cafe_sales.csv")

show_data_info(df, "Original Data")

df_cleaned = auto_handle_missing(df)

show_data_info(df_cleaned, "Cleaned Data")


# 3. Convert columns to correct types

# Numeric columns
df_cleaned["Quantity"] = pd.to_numeric(df_cleaned["Quantity"], errors="coerce")
df_cleaned["Price Per Unit"] = pd.to_numeric(df_cleaned["Price Per Unit"], errors="coerce")
df_cleaned["Total Spent"] = pd.to_numeric(df_cleaned["Total Spent"], errors="coerce")

# Datetime column
df_cleaned["Transaction Date"] = pd.to_datetime(df_cleaned["Transaction Date"], errors="coerce")

# Handle any new missing values created by type conversion
df_cleaned = auto_handle_missing(df_cleaned)

show_data_info(df_cleaned, "Cleaned & Typed Data")


# 4. Define visualization tasks

tasks = [
    {"type": "bar", "x": "Location", "y": "Total Spent"},
    {"type": "line", "x": "Transaction Date", "y": "Total Spent"},
    {"type": "hist", "col": "Total Spent", "bins": 10}
]


# 5. Execute visualizations imperatively

for task in tasks:
    if task["type"] == "bar":
        if task["x"] in df_cleaned.columns and task["y"] in df_cleaned.columns:
            print(f"[INFO] Plotting Bar Chart: {task['y']} by {task['x']}")
            plot_bar(df_cleaned, x_col=task["x"], y_col=task["y"])

    elif task["type"] == "line":
        if task["x"] in df_cleaned.columns and task["y"] in df_cleaned.columns:
            df_sorted = df_cleaned.sort_values(task["x"])
            print(f"[INFO] Plotting Line Chart: {task['y']} over {task['x']}")
            plot_line(df_sorted, x_col=task["x"], y_col=task["y"])

    elif task["type"] == "hist":
        if task["col"] in df_cleaned.columns:
            print(f"[INFO] Plotting Histogram: {task['col']}")
            plot_histogram(df_cleaned, col=task["col"], bins=task.get("bins", 10))

print("\n[INFO] All visualizations completed and saved in 'plots/' folder.")