from groq import Groq
client = Groq(api_key="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")

print("chatbot (Groq Streaming): Type 'quit','exit' or 'bye' to stop\n ")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("Exiting the chatbot. Goodbye!")
        break

    print(" chatbot: ", end="", flush=True)

    stream = client .chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input  }
        ],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

    print()  
