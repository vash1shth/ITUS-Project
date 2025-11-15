# import sqlite3
# import os
# import time
# import configparser
# from functools import lru_cache
# import logging
# from logging.handlers import RotatingFileHandler

# # Configuration Loader
# def load_config():
#     config = configparser.ConfigParser()
#     config_paths = [
#         os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini"),
#         os.path.join(os.getcwd(), "config.ini"),
#     ]
#     for cp in config_paths:
#         if os.path.exists(cp):
#             print(f"Loading config from: {cp}")
#             config.read(cp)
#             if "DATABASE" in config:
#                 return config
#     raise FileNotFoundError("config.ini not found in script or working directory")

# CONFIG = load_config()
# DB_PATH = CONFIG["DATABASE"].get("db_path", "revenue.db")
# TABLE_NAME = CONFIG["DATABASE"].get("table_name", "quarterly_revenue")

# print(f"Database Path: {DB_PATH}")
# print(f"Database exists: {os.path.exists(DB_PATH)}")
# print(f"Table Name: {TABLE_NAME}")

# ALLOWED_FIELDS = {
#     "quarterly_revenue", "company_name", "sector", "mcap_category", "date", "accord_code"
# }

# print(f"'quarterly_revenue' allowed field? {'quarterly_revenue' in ALLOWED_FIELDS}")

# # Logging Setup
# LOG_FILE = "query_log.txt"
# logger = logging.getLogger("revenue_udf")
# logger.setLevel(logging.INFO)
# if not logger.handlers:
#     handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3)
#     formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
#     handler.setFormatter(formatter)
#     logger.addHandler(handler)

# def log_call(func_name, params, start, success=True, msg=""):
#     elapsed = (time.perf_counter() - start) * 1000
#     status = "SUCCESS" if success else "FAIL"
#     logger.info(f"{func_name} | params={params} | time_ms={elapsed:.2f} | {status} | {msg}")

# def get_connection():
#     if not os.path.exists(DB_PATH):
#         raise FileNotFoundError(f"Database not found at path: {DB_PATH}")
#     conn = sqlite3.connect(DB_PATH)
#     print(f"Database connection established to: {DB_PATH, conn}")
#     conn.row_factory = sqlite3.Row
#     return conn

# def _is_allowed_field(field):
#     return field in ALLOWED_FIELDS

# def _friendly_error(e):
#     return f"ERROR: {type(e).__name__}: {e}"

# @lru_cache(maxsize=2048)
# def _cached_single_lookup(accord_code, field, date):
#     start = time.perf_counter()
#     date = date + " 00:00:00"
#     params = {"accord_code": accord_code, "field": field, "date": date}
#     print(f"Parameters for _cached_single_lookup: {params}")
#     try:
#         print(f"Checking if field allowed: {field}")
#         if not _is_allowed_field(field):
#             raise ValueError(f"Field '{field}' not allowed.")
#         with get_connection() as conn:
#             cur = conn.cursor()
#             query = f"SELECT {field} FROM {TABLE_NAME} WHERE accord_code=? AND date=? LIMIT 1"
#             print(f"Executing SQL: {query} with params ({accord_code}, {date})")
#             cur.execute(query, (accord_code, date))
#             row = cur.fetchone()
#             print(f"SQL query result row: {row}")
#             if row is None:
#                 print("No data found for given parameters.")
#                 log_call("_cached_single_lookup", params, start, False, "No data")
#                 return None
#             val = row[field]
#             print(f"Data found: {val}")
#             log_call("_cached_single_lookup", params, start, True)
#             return val
#     except Exception as e:
#         print(f"Exception in _cached_single_lookup: {e}")
#         log_call("_cached_single_lookup", params, start, False, str(e))
#         raise

# def get_quarterly_data(accord_code, field, date):
#     start = time.perf_counter()
#     params = {"accord_code": accord_code, "field": field, "date": date}
#     print(f"Parameters for get_quarterly_data: {params}")
#     try:
#         accord_code = int(accord_code)
#         print(f"Getting quarterly data for accord_code={accord_code}, field={field}, date={date}")
#         if not _is_allowed_field(field):
#             print(f"Field '{field}' not allowed")
#             return f"ERROR: Field '{field}' not allowed."
#         value = _cached_single_lookup(accord_code, field, date)
#         log_call("get_quarterly_data", params, start, True)
#         if value is None:
#             print("Returned value is None, returning 'N/A'")
#             return "N/A"
#         print(f"Successfully retrieved value: {value}")
#         return value
#     except Exception as e:
#         print(f"Exception in get_quarterly_ {e}")
#         log_call("get_quarterly_data", params, start, False, str(e))
#         return _friendly_error(e)

# if __name__ == "__main__":
#     # Test fetching quarterly_revenue for accord_code 208763 and date "2022-03-31"
#     result = get_quarterly_data(208763, "quarterly_revenue", "2022-03-31")
#     print(f"Final result: {result}")


from revenue_data_udf import get_quarterly_data

out = get_quarterly_data(208763, "quarterly_revenue", "2022-03-31")
print(out)