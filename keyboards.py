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
        ],

        [
            InlineKeyboardButton(
                text="💰 Баланс бонусов",
                callback_data="bonus_balance"
            )
        ],

        [
            InlineKeyboardButton(
                text="🤝 Присоединиться к реферальной программе",
                callback_data="join_referral"
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
        ],
        
        [
            InlineKeyboardButton(
                text="💰 Начислить бонусы",
                callback_data="give_bonus_info"
            )
        ]

    ]

)
