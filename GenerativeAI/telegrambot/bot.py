import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()

logging.basicConfig(level=logging.INFO)

telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
hf_token = os.getenv("HF_TOKEN")

bot = Bot(token=telegram_token)
dp = Dispatcher()

client = InferenceClient(
    provider="auto",
    api_key=hf_token
)


@dp.message(Command("start", "help"))
async def start(message: Message):
    await message.answer(
        "Hello! I'm your AI bot. Ask me anything!"
    )


@dp.message()
async def chat(message: Message):

    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": message.text
        }
    ]

    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=messages,
        max_tokens=500,
    )

    response = completion.choices[0].message.content

    await message.answer(response)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())