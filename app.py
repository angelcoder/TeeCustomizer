import chainlit as cl
from dotenv import load_dotenv
from openai import AsyncOpenAI
from src.llm import ask_order, messages

load_dotenv()
client = AsyncOpenAI()
cl.instrument_openai()

@cl.on_message
async def on_message(message: cl.Message):
    messages.append({"role": "user", "content": message.content})
    response = ask_order(messages)
    messages.append({"role": "assistant", "content": response})

    await cl.Message(
        content=response,
    ).send()
