from aiogram import Router, F
from aiogram.types import CallbackQuery

from config import ADMIN_ID, BOT_USERNAME
from services.leads import get_all_leads
from referrals import REFERRALS

from services.leads import add_bonus

router = Router()


@router.callback_query(F.data == "all_leads")
async def all_leads(callback: CallbackQuery):

    if callback.from_user.id != ADMIN_ID:
        return

    leads = get_all_leads()

    if not leads:
        await callback.message.answer("Заявок пока нет.")
        return

    text = "<b>📋 Все заявки</b>\n\n"

    for lead in leads:

        text += (
            f"👤 {lead['full_name']}\n"
            f"🔗 {lead['username']}\n"
            f"🆔 {lead['telegram_id']}\n"
            f"👥 {lead['referral_name']}\n"
            f"🎁 {lead['discount']}%\n"
            f"🕒 {lead['created_at']}\n"
            "-------------------------\n"
        )

    await callback.message.answer(text)

@router.callback_query(
    F.data == "give_bonus_info"
)
async def give_bonus_info(
    callback: CallbackQuery
):

    if callback.from_user.id != ADMIN_ID:
        return

    await callback.message.answer(

        "Для начисления бонусов:\n\n"

        "Напишите команду:\n\n"

        "/bonus USER_ID СУММА\n\n"

        "Пример:\n"

        "/bonus 123456789 500"

    )

from aiogram.filters import Command
from services.leads import add_bonus
from config import ADMIN_ID


from aiogram.types import Message

@router.message(Command("bonus"))
async def bonus_command(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    try:
        args = message.text.split()

        user_id = int(args[1])
        amount = int(args[2])

        add_bonus(user_id, amount)

        await message.bot.send_message(
            user_id,
            f"🎁 Вам начислено {amount} бонусов!\n\n"
            "Проверьте баланс бонусов в боте."
        )

        await message.answer(
            f"✅ Начислено {amount} бонусов\n"
            f"Пользователь: {user_id}"
        )

    except Exception as e:
        print(e)
        await message.answer(
            "Использование:\n"
            "/bonus USER_ID СУММА"
        )
