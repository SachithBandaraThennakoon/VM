from openai import OpenAI
from app.mind.master_prompt import MASTER_SYSTEM_PROMPT

client = OpenAI()

def call_master_llm(user_input, context_prompt):
    messages = [
        {"role": "system", "content": MASTER_SYSTEM_PROMPT},
        {"role": "system", "content": context_prompt},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.4  # calm, stable responses
    )

    return response.choices[0].message.content
