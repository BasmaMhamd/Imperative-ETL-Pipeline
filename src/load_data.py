import pandas as pd
import json
import sqlite3
from typing import Union

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file imperatively.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] CSV loaded successfully: {file_path}")
        return df
    except FileNotFoundError:
        print(f"[ERROR] CSV file not found: {file_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"[ERROR] Failed to load CSV: {e}")
        return pd.DataFrame()


def load_json(file_path: str) -> pd.DataFrame:
    """
    Load data from a JSON file imperatively.
    """
    try:
        df = pd.read_json(file_path)
        print(f"[INFO] JSON loaded successfully: {file_path}")
        return df
    except FileNotFoundError:
        print(f"[ERROR] JSON file not found: {file_path}")
        return pd.DataFrame()
    except ValueError as e:
        print(f"[ERROR] Failed to parse JSON: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"[ERROR] Failed to load JSON: {e}")
        return pd.DataFrame()


def load_sql(db_path: str, query: str) -> pd.DataFrame:
    """
    Load data from a SQL database (SQLite) imperatively.
    """
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(query, conn)
        conn.close()
        print(f"[INFO] SQL query executed successfully: {db_path}")
        return df
    except sqlite3.Error as e:
        print(f"[ERROR] SQL error: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"[ERROR] Failed to load SQL data: {e}")
        return pd.DataFrame()


def load_data(source_type: str, path_or_query: str) -> pd.DataFrame:
    """
    Unified function to load data based on type: 'csv', 'json', 'sql'
    """
    source_type = source_type.lower()
    if source_type == 'csv':
        return load_csv(path_or_query)
    elif source_type == 'json':
        return load_json(path_or_query)
    elif source_type == 'sql':
        return load_sql(path_or_query, "SELECT * FROM sales")  # default table
    else:
        print(f"[ERROR] Unsupported source type: {source_type}")
        return pd.DataFrame()
