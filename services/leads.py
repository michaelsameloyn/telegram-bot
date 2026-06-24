from database import cur, conn


def add_lead(
    telegram_id,
    username,
    full_name,
    referral_code,
    referral_name,
    discount,
    created_at
):

    cur.execute("""

    INSERT OR REPLACE INTO leads(

        telegram_id,

        username,

        full_name,

        referral_code,

        referral_name,

        discount,

        created_at

    )

    VALUES(

        ?,?,?,?,?,?,?

    )

    """, (

        telegram_id,

        username,

        full_name,

        referral_code,

        referral_name,

        discount,

        created_at

    ))

    conn.commit()


def get_all_leads():

    cur.execute("""

    SELECT *

    FROM leads

    ORDER BY id DESC

    """)

    return cur.fetchall()
