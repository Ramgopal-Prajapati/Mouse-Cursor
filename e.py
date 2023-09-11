import openai

# Set your OpenAI API key
openai.api_key = "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"
#sk-vyn7yHZqzL40HOqE1YhJT3B1bkFJEnczoZ89orQRE92rdSSv
def get_ai_response(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=50  # Limit the response length
    )
    return response.choices[0].text.strip()

def main():
    print("AI Assistant: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI Assistant: Goodbye!")
            break
        prompt = f"You: {user_input}\nAI Assistant:"
        ai_response = get_ai_response(prompt)
        print("AI Assistant:", ai_response)

if __name__ == "__main__":
    main()
