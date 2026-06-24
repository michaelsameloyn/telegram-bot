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

    cur.execute(
        """
        SELECT telegram_id
        FROM leads
        WHERE telegram_id=?
        """,
        (telegram_id,)
    )

    exists = cur.fetchone()

    if exists:

        cur.execute(
            """
            UPDATE leads
            SET
                username=?,
                full_name=?
            WHERE telegram_id=?
            """,
            (
                username,
                full_name,
                telegram_id
            )
        )

    else:

        cur.execute(
            """
            INSERT INTO leads(
                telegram_id,
                username,
                full_name,
                referral_code,
                referral_name,
                discount,
                created_at
            )
            VALUES(?,?,?,?,?,?,?)
            """,
            (
                telegram_id,
                username,
                full_name,
                referral_code,
                referral_name,
                discount,
                created_at
            )
        )

    conn.commit()


def get_all_leads():

    cur.execute(
        """
        SELECT *
        FROM leads
        ORDER BY id DESC
        """
    )

    return cur.fetchall()


def get_bonus_balance(user_id):

    cur.execute(
        """
        SELECT bonuses
        FROM leads
        WHERE telegram_id=?
        """,
        (user_id,)
    )

    row = cur.fetchone()

    if row:
        return row["bonuses"]

    return 0


def become_partner(user_id, code):

    cur.execute(
        """
        UPDATE leads
        SET
            is_partner=1,
            personal_ref_code=?,
            referral_percent=10
        WHERE telegram_id=?
        """,
        (
            code,
            user_id
        )
    )

    conn.commit()


def add_bonus(user_id, amount):

    cur.execute(
        """
        UPDATE leads
        SET bonuses = bonuses + ?
        WHERE telegram_id=?
        """,
        (
            amount,
            user_id
        )
    )

    conn.commit()


def get_partner_by_code(code):

    cur.execute(
        """
        SELECT *
        FROM leads
        WHERE personal_ref_code=?
        """,
        (code,)
    )

    return cur.fetchone()
