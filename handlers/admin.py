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


@router.callback_query(F.data == "referrals")
async def referrals(callback: CallbackQuery):

    if callback.from_user.id != ADMIN_ID:
        return

    text = "<b>👥 Все рефералы</b>\n\n"

    # ВАЖНО: правильный отступ (у тебя тут была ошибка)
    bot_name = BOT_USERNAME

    for code, data in REFERRALS.items():

        text += (

    f"👤 {data['name']}\n"

    f"📊 Скидка: {data['discount']}%\n"

    f"🔑 Код: {code}\n"

    f"🔗 https://t.me/{BOT_USERNAME}?start={code}\n\n"

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
