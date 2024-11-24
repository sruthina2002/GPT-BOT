import openai 

openai.api_key = "------------"
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break

        try:
            response = chat_with_gpt(user_input)
            print("Chatbot:", response)
        except openai.error.RateLimitError:
           print("Rate limit exceeded. Retrying after a delay...")
           time.sleep(10)  # Pause for 10 seconds before retrying