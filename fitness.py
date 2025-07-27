from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1",
)

user_input = input("you :")

response = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a professional fitness and diet coach. "
                "Only answer questions related to fitness, diet, workouts, weight loss, muscle gain, and nutrition. "
                "If the user asks about anything else, respond with: "
                "'Sorry, I can only assist with fitness and diet-related topics.'"
            )
        },
        {"role": "user", "content": user_input}
    ]
)

print("Bot:", response.choices[0].message.content)

while True:
    user_input = input("you : ")
    if user_input.lower() == "quit":
        print("Bot :goodbye!!")
        break

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional fitness and diet coach. "
                    "Only answer questions related to fitness, diet, workouts, weight loss, muscle gain, and nutrition. "
                    "If the user asks about anything else, respond with: "
                    "'Sorry, I can only assist with fitness and diet-related topics.'"
                )
            },
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot:", response.choices[0].message.content)
