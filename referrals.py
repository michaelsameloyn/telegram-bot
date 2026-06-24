"""
===========================================
РЕФЕРАЛЬНАЯ СИСТЕМА

Чтобы добавить нового реферала,
просто добавьте новую запись по аналогии.

Ключ словаря используется в ссылке:

https://t.me/YourBot?start=ivan

где

ivan -> код реферала
===========================================
"""

REFERRALS = {

    "ivan": {
        "name": "Иван",
        "discount": 5,
        "active": True
    },

    "alex": {
        "name": "Александр",
        "discount": 5,
        "active": True
    },

    "telegram": {
        "name": "Telegram",
        "discount": 5,
        "active": True
    }

}


import hashlib


SECRET_KEY = "SUPER_SECRET_2026"

cur.execute("""
SELECT is_partner
FROM leads
WHERE telegram_id=?
""", (user.id,))

row = cur.fetchone()

if row and row["is_partner"] == 1:

    await callback.message.answer(
        "✅ Вы уже участвуете в реферальной программе."
    )

    return

def generate_partner_code(user_id):

    return hashlib.sha256(
        f"{user_id}{SECRET_KEY}".encode()
    ).hexdigest()[:16]
