# ITUS Project – Revenue Data Automation & Analysis
A Python-based automation system designed to process, analyze, and manage quarterly revenue data using Excel, custom UDFs, and an SQLite backend. This project streamlines revenue calculations, ensures data consistency, and provides a reproducible workflow for organizational reporting.

# Features
 1. Automated Revenue Processing
Cleans and validates revenue datasets
Performs calculations: totals, quarterly comparisons, differences
Converts messy Excel inputs into structured tables
 2. Excel Integration (UDFs)
Custom Python functions exposed inside Excel
Supports both .xlsx and macro-enabled .xlsm workflows
Great for hybrid Excel–Python automation
 3. SQLite Database Support
Stores raw and processed revenue data
Maintains logs of SQL operations
Ensures durability and reproducibility
 4. Logging & Monitoring
Logs all queries and errors (query_log.txt, queries.log)
Useful for debugging and auditing

# ITUS Project/
│
├── revenue_data_udf.py            # Python UDF for Excel revenue functions
├── db_data.py                     # SQLite DB operations
├── excel.py                       # Excel automation (openpyxl/xlwings)
├── test.py                        # Testing scripts
├── revenue.db                     # SQLite database
├── config.ini                     # Configuration file
│
├── revenue_data_udf.xlsx          # Excel workbook linked to UDF
├── revenue_data_udf.xlsm          # Macro-enabled version
├── itus_1.xlsx                    # Main revenue dataset
├── Book1.xlsx / Book3.xlsx        # Sample datasets
├── test_excel.xlsx / test_excel.xlsm
│
├── queries.log                    # Log of all SQL operations
├── query_log.txt
│
├── Internship (quarterly_revenue).docx  # Project documentation
└── __pycache__/                   # Auto-generated Python cache files

# Technologies Used
Languages & Tools
Python 3.8+
Excel (with macro support)
SQLite
Logging framework

# Libraries Used
pandas
openpyxl
xlwings
configparser
sqlite3 (built-in)
logging

# Configure the Project
Edit the config.ini file to adjust:
Database path
Excel file references
Logging preferences

# License
This project is intended for academic and internship use.
Adapt or extend freely as needed.
