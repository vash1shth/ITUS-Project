import xlwings as xw
import sqlite3
# from revenue_data_udf import get_quarterly_data

@xw.func
def get_quarterly_data(accord_code: int, field: str, date: str) -> str:
    conn = sqlite3.connect('/Users/vanshikabakshi/Desktop/ITUS Project/revenue.db')
    date = date + " 00:00:00"
    cursor = conn.cursor()
    query = f"SELECT {field} FROM quarterly_revenue WHERE accord_code=? AND date=? LIMIT 1"
    cursor.execute(query, (accord_code, date))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 'N/A'

if __name__ == "__main__":
    output = get_quarterly_data(208763, "quarterly_revenue", "2022-03-31")
    print(output)

