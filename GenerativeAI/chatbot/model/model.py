import os
from huggingface_hub import InferenceClient

HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN:
    print("HF_TOKEN is set")
else:
    raise ValueError("HF_TOKEN is NOT set")

client = InferenceClient(
    api_key=HF_TOKEN
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]


def generate_response(user_input):
    messages.append({
        "role": "user",
        "content": user_input
    })

    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=messages
    )

    response = completion.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": response
    })

    return response
