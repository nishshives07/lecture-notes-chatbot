from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

messages = []

print("Paste your notes:")
notes = input()

# summary
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": f"Summarize:\n{notes}"}]
)

print("\nSummary:\n", response.choices[0].message.content)

messages.append({"role": "system", "content": notes})

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    messages.append({"role": "user", "content": user})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        print("Bot:", reply)

        messages.append({"role": "assistant", "content": reply})

    except:
        print("Error, try again")
