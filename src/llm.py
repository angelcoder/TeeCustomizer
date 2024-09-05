import json
from openai import OpenAI
from src.prompt import system_instruction
from src.user_issue import UserIssue, functions, handle_user_issue

client = OpenAI()

messages = [
    {"role": "system", "content": system_instruction}
]

def ask_order(messages, model="gpt-4", temperature=0):

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        functions=functions,
        function_call="auto"
    )

    user_issue = UserIssue()
    # Check the response from the API
    if response.choices[0].message.function_call:
        function_name = response.choices[0].message.function_call.name
        function_arguments = response.choices[0].message.function_call.arguments

        if function_name == "handle_user_issue":
            function_arguments = json.loads(function_arguments)

            issue_type = function_arguments.get("issue_type", None)
            details = function_arguments.get("details", None)

            user_issue.set_issue_type(issue_type)
            user_issue.set_details(details)

            handle_user_issue(user_issue)

    return response.choices[0].message.content, user_issue
