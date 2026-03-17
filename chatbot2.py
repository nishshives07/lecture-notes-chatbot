import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = []

def summarize(notes):
    prompt = f"""
    Summarize these lecture notes.
    Give:
    - Title
    - 3-5 key points
    - Action items

    Notes:
    {notes}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def chat(user_input):
    global messages

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        return reply

    except:
        return "⚠️ Error! Try again."


print("📘 Paste your lecture notes:")
notes = input()

# Step 1: Summary
summary = summarize(notes)
print("\n📌 Summary:\n", summary)

# Store notes
messages.append({
    "role": "system",
    "content": f"These are the notes:\n{notes}"
})

print("\n💬 Ask questions (type 'exit' to stop):")

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    # simple unrelated check
    if "weather" in user.lower():
        print("🤖 Ask only about your notes.")
        continue

    reply = chat(user)
    print("Bot:", reply)

