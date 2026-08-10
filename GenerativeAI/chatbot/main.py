from huggingface_hub import InferenceClient

from model.model import generate_response

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    response = generate_response(user_input)
    print("Bot:", response)