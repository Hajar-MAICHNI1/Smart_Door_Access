
import pyodbc

# --- SQL Connection Setup ---
def get_connection():
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-AT7A8MF\\SQLEXPRESS;"
        "Database=RFID;"
        "UID=sa;"
        "PWD=azerty;"
    )

    return conn
