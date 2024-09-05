import chainlit as cl
from dotenv import load_dotenv
from openai import AsyncOpenAI
from src.llm import ask_order, messages
from src.user_issue import UserIssue

load_dotenv()
client = AsyncOpenAI()
cl.instrument_openai()

user_issue = UserIssue()

@cl.on_message
async def on_message(message: cl.Message):
    messages.append({"role": "user", "content": message.content})

    global user_issue
    response, user_issue = ask_order(messages)

    if response:
        messages.append({"role": "assistant", "content": response})

    if response:
        await cl.Message(
            content=response,
        ).send()
    else:
        actions = [
            cl.Action(name="Chat support team", value="Chat support team", description="Click me!")
        ]

        await cl.Message(content="Press the button and we will redirect you to the support team", actions=actions).send()

@cl.action_callback("Chat support team")
async def on_action(action):
    await cl.Message(content=f"Hi! This is {action.name}\nIssue: {user_issue.issue_type}\nDetails: {user_issue.details}").send()
    await action.remove()