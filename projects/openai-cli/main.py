# An CLI app for Open AI chat.

from openai import OpenAI

import os

# check if the API key is set
if 'OPENAI_API_KEY' not in os.environ:
    print('Please set the OPENAI_API_KEY environment variable.')
    exit(1)

# A greetings message from the app
def greetings():
    print('Welcome to Open AI CLI app.')
    print('Type your message and press enter to chat with the AI (type BYE to exit the app).')

# Ask a question to the AI
def ask_question(question, client, messages=[]):
    if len(messages) == 0:
        messages.append({
            "role": "developer",
            "content": "You are a helpful and kind assistant helping me with my programming questions."
        })

    messages.append({
        "role": "user",
        "content": question
    })

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        n=1,
        temperature=1.5,
        max_completion_tokens=100,
        messages=messages
    )

    answer_message = completion.choices[0].message
    messages.append(answer_message)

    return answer_message.content, messages

# main loop function
def main():
    client = OpenAI()
    messages = []

    greetings()

    while True:
        question = input('You: ')
        if question == '':
            continue
        
        if question == 'BYE':
            print('Farewell!')
            break

        answer, messages = ask_question(question, client, messages)
        print('AI:', answer)

if __name__ == '__main__':
    main()