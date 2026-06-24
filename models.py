from database import cur, conn

# ==========================================
# USERS TABLE
# ==========================================

from database import cur, conn

cur.execute("""
CREATE TABLE IF NOT EXISTS leads (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    telegram_id INTEGER UNIQUE,

    username TEXT,

    full_name TEXT,

    referral_code TEXT,

    referral_name TEXT,

    discount INTEGER,

    created_at TEXT,

    bonuses INTEGER DEFAULT 0,

    referral_percent INTEGER DEFAULT 10,

    is_partner INTEGER DEFAULT 0,

    personal_ref_code TEXT
)
""")

conn.commit()
