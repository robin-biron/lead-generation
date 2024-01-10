def query_chat_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or the latest available model
        prompt=prompt,
        max_tokens=100  # Adjust as needed
    )
    return response.choices[0].text.strip()
