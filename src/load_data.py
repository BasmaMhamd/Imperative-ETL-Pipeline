# ============================================================
# LOADER MODULE
# ============================================================
# This file contains all functions responsible for LOADING data.
# Team members should implement the following:
#
# 1. load_csv(path)
#    - Reads CSV file using pandas.
#    - Returns a DataFrame.
#    - Must handle errors (file not found, bad encoding).
#
# 2. load_json(path)
#    - Reads JSON file into pandas.
#    - Handles both dict-style JSON and list-style JSON.
#
# 3. load_sql(connection_string, query)
#    - Establish SQL connection using sqlite3 or SQLAlchemy.
#    - Executes query and returns DataFrame.
#    - Must close the connection (imperative resource handling).
#
# 4. detect_file_type_and_load(path)
#    - Auto-detect .csv/.json/.xlsx and call the right loader.
#
# NOTE:
# - Do not use functional chaining. Write it step-by-step.
# - Validate file exists before loading.
# - Return None and print error if loading fails.
# ============================================================
