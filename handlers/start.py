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

@router.message(F.text.startswith("/bonus"))
async def bonus_command(
    message: Message
):

    if message.from_user.id != ADMIN_ID:
        return

    try:

        parts = message.text.split()

        user_id = int(parts[1])

        amount = int(parts[2])

        add_bonus(
            user_id,
            amount
        )

        await message.answer(

            f"✅ Пользователю {user_id}\n"
            f"начислено {amount} бонусов"

        )

    except:

        await message.answer(

            "Использование:\n"
            "/bonus USER_ID СУММА"

        )
        
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

    balance = get_bonus_balance(
    user.id
)
    admin_text = (

        "🟢 Новая заявка\n\n"

        f"👤 Имя: {user.full_name}\n"

        f"🔗 Username: {username}\n"

        f"🆔 ID: {user.id}\n"

        f"💰 Бонусов: {balance}\n"

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

@router.callback_query(
    F.data == "bonus_balance"
)
async def bonus_balance(
    callback: CallbackQuery
):

    balance = get_bonus_balance(
        callback.from_user.id
    )

    await callback.message.answer(

        f"💰 Ваш баланс бонусов:\n\n"
        f"{balance} бонусов"

    )

    await callback.answer()

@router.callback_query(
    F.data == "join_referral"
)
async def join_referral(
    callback: CallbackQuery
):

    user = callback.from_user

    code = generate_partner_code(
        user.id
    )

    become_partner(
        user.id,
        code
    )

    referral_link = (

        f"https://t.me/"
        f"{BOT_USERNAME}"
        f"?start={code}"

    )

    balance = get_bonus_balance(
        user.id
    )

    await callback.message.answer(

        "🎉 Вы стали участником реферальной программы!\n\n"

        f"🔗 Ваша ссылка:\n{referral_link}\n\n"

        "👤 Пользователь получит скидку 10% "
        "на первый заказ.\n\n"

        "💰 Вы получите 300 бонусов "
        "после его заказа от 3000 ₽.\n\n"

        "✅ Бонусами можно оплатить "
        "до 100% следующих заказов.\n\n"

        "📊 Ваш процент по программе: 10%\n\n"

        f"💰 Ваш баланс: {balance} бонусов"

    )

    await callback.message.bot.send_message(

        ADMIN_ID,

        "🤝 Новый партнёр\n\n"

        f"👤 {user.full_name}\n"

        f"🔗 @{user.username}\n"

        f"🆔 {user.id}\n\n"

        f"💰 Бонусов: {balance}\n"

        "📊 Процент: 10%"

    )

    await callback.answer()

