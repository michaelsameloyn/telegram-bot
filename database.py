import sqlite3

# ==========================================
# DATABASE
# ==========================================

conn = sqlite3.connect(
    "crm.db",
    check_same_thread=False
)

conn.row_factory = sqlite3.Row

cur = conn.cursor()
