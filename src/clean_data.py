# ============================================================
# CLEANING MODULE
# ============================================================
# Team members must implement missing-value handling functions.
#
# 1. remove_missing(df)
#    - Removes rows with ANY missing values.
#    - Prints how many rows removed.
#
# 2. fill_missing(df, fill_values)
#    - Fills NA using user-provided defaults.
#    - Example: {'age': 0, 'city': 'Unknown'}
#
# 3. auto_handle_missing(df)
#    - Automatically detect column type:
#         - Numerical → fill with mean or median
#         - Categorical → fill with mode (most frequent)
#         - Date columns → fill with earliest or latest date
#    - If type unknown → print warning.
#
# 4. get_missing_report(df)
#    - Returns a summary:
#         column name | number of missing values | percentages
#
# ============================================================
