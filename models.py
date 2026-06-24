from database import cur, conn

# ==========================================
# USERS TABLE
# ==========================================

cur.execute("""
CREATE TABLE IF NOT EXISTS leads (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    telegram_id INTEGER UNIQUE,

    username TEXT,

    full_name TEXT,

    referral_code TEXT,

    referral_name TEXT,

    discount INTEGER,

    created_at TEXT

)
""")

conn.commit()
