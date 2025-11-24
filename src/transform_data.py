# ============================================================
# TRANSFORMATION MODULE (Imperative Version)
# ============================================================
# This file handles data transformations before analysis.
# Team members must implement:
#
# 1. filter_rows(df, condition)
#    - Imperative filtering logic.
#    - Example: filter_rows(df, df['sales'] > 1000)
#
# 2. add_new_column(df, name, function)
#    - Add a new column based on row-by-row updates.
#    - Use for loops, not df.apply().
#
# 3. standardize_date_column(df, column)
#    - Convert string → datetime
#    - Handle invalid formats imperatively.
#
# 4. aggregate_data(df, group_by_col, agg_col, method)
#    - Example: group by region and sum sales.
#    - Use pandas groupby but assign results imperatively.
#
# 5. sort_data(df, column, ascending=True)
#    - Sort the dataset based on a specific column.
#
# ============================================================
