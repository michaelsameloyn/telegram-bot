from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from config import CONTACT_URL

# ==========================================
# USER
# ==========================================

user_keyboard = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(
                text="🛒 Сделать заказ",
                url=CONTACT_URL
            )
        ]

    ]

)

# ==========================================
# ADMIN
# ==========================================

admin_keyboard = InlineKeyboardMarkup(

    inline_keyboard=[

        [
            InlineKeyboardButton(
                text="📋 Все заявки",
                callback_data="all_leads"
            )
        ],

        [
            InlineKeyboardButton(
                text="👥 Рефералы",
                callback_data="referrals"
            )
        ]

    ]

)
