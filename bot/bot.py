import asyncio

from aiogram import Router, Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder


def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Let's Click!", web_app=WebAppInfo(
            url="https://federalx.run.place/"
        )
    )
    return builder.as_markup()

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply(
        "Click! Click! Click!",
        reply_markup=webapp_builder()
    )


async def main() -> None:
    bot = Bot(
        "7346195773:AAFu3yjWgvyhD76BloqKowvesFXReITfbTE",
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
