from datetime import datetime

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram import F
from aiogram.types import CallbackQuery

from config import ADMIN_ID

from keyboards import (
    user_keyboard,
    admin_keyboard
)

from referrals import REFERRALS

from services.leads import add_lead

from referrals import (
    REFERRALS,
    generate_partner_code
)

from services.leads import (
    add_lead,
    get_bonus_balance,
    become_partner
)

from config import (
    ADMIN_ID,
    BOT_USERNAME
)

router = Router()

@router.message(CommandStart())
async def start(message: Message, command: CommandStart):

    user = message.from_user

    username = (
        f"@{user.username}"
        if user.username
        else "нет"
    )

    referral_code = None
    referral_name = "Без реферала"
    discount = 0

    # ==========================
    # Проверяем параметр start
    # ==========================

    if command.args:

        code = command.args.lower()

        if code in REFERRALS:

            ref = REFERRALS[code]

            if ref["active"]:

                referral_code = code

                referral_name = ref["name"]

                discount = ref["discount"]

    created_at = datetime.now().strftime(
        "%d.%m.%Y %H:%M"
    )

    # ==========================
    # Сохраняем пользователя
    # ==========================

    add_lead(

        telegram_id=user.id,

        username=username,

        full_name=user.full_name,

        referral_code=referral_code,

        referral_name=referral_name,

        discount=discount,

        created_at=created_at

    )

    # ==========================
    # Если это админ
    # ==========================

    if user.id == ADMIN_ID:

        await message.answer(

            "🛠 Панель администратора",

            reply_markup=admin_keyboard

        )

        return

    # ==========================
    # Уведомление администратора
    # ==========================

    admin_text = (

        "🟢 Новая заявка\n\n"

        f"👤 Имя: {user.full_name}\n"

        f"🔗 Username: {username}\n"

        f"🆔 ID: {user.id}\n"

        f"👥 Реферал: {referral_name}\n"

        f"🎁 Скидка: {discount}%\n"

        f"🕒 Время: {created_at}"

    )

    await message.bot.send_message(

        ADMIN_ID,

        admin_text

    )

    # ==========================
    # Ответ пользователю
    # ==========================

    if discount:

        await message.answer(

            f"🎉 Ваша персональная скидка {discount}% успешно применена!",

            reply_markup=user_keyboard

        )

    else:

        await message.answer(

            "Добро пожаловать!",

            reply_markup=user_keyboard

        )
