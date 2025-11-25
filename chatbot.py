import requests

API_KEY = "your_api_key_here"  # Replace with your actual API key securely
MODEL = "deepseek/deepseek-chat"

messages = []

print("Chatbot Memory Mode Activated 🤖\n")
while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Chatbot: Bye 😘")
        break

    messages.append({"role": "user", "content": user})

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": messages
        }
    )

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        print(f"Chatbot: {reply}")
        messages.append({"role": "assistant", "content": reply})
    else:
        print(f"Error {response.status_code}: {response.text}")
    reply = r.json()["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    print("Chatbot:", reply, "\n")
