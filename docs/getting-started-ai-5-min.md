# Getting Started with AI Engineering in 5 Minutes

Artificial Intelligence (AI) is revolutionizing software engineering, and OpenAI provides powerful tools to integrate AI into your applications. This tutorial will guide you through setting up and running a simple command-line application (CLI) that connects to OpenAI's API and simulates a chat conversation.

You will:

- Clone a GitHub repository containing a ready-to-use CLI app.
- Install dependencies and configure your OpenAI API key.
- Run the application and chat with an AI model.

By the end of this guide, you'll have a functional AI-powered chatbot running in your terminal!

## 1. Clone the Project Repository

First, download the project code from GitHub. Open a terminal and run:

```sh
git clone https://github.com/rodolfo-mendes/ai-projects.git
cd ai-projects/projects/openai-cli
```

This will fetch the latest version of the project and navigate to the correct directory.

## 2. Set Up Your OpenAI API Key

To interact with OpenAI's API, you need an API key. Follow these steps:

1. Sign up or log in to [OpenAI](https://platform.openai.com/).
2. Generate an API key by visiting the [API Key Management](https://platform.openai.com/account/api-keys) page.
3. Store the API key securely (avoid sharing it or committing it to version control).

Set the key as an environment variable:

**Linux/macOS:**

```sh
export OPENAI_API_KEY="your-api-key-here"
```

**Windows (PowerShell):**

```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
```

Your OpenAI SDK will now authenticate requests using this key.

## 3. Install Dependencies

The project uses Python and requires the OpenAI SDK. Install the dependencies by running:

```sh
pip install -r requirements.txt
```

For best practice, create a virtual environment before installing:

```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

This ensures project-specific package isolation.

## 4. Understanding the Code in `main.py`

The `main.py` file contains the logic for the CLI chatbot. Let's break it down:

### API Key Validation

The script checks if the `OPENAI_API_KEY` environment variable is set. If not, it prompts the user to set it and exits:

```python
def validate_openai_api_key():
    if 'OPENAI_API_KEY' not in os.environ:
        print('Please set the OPENAI_API_KEY environment variable.')
        exit(1)
```

### Greeting Message

The chatbot welcomes the user and provides interaction instructions:

```python
def greetings():
    print('Welcome to Open AI CLI app.')
    print('Type your message and press enter to chat with the AI (type BYE to exit the app).')
```

### Chat Handling

The `ask_question()` function sends user input to OpenAI's API and appends responses to maintain context:

```python
def ask_question(question, client, messages=[]):
    if len(messages) == 0:
        messages.append({
            "role": "developer",
            "content": "You are a helpful and kind assistant helping 
               me with my programming questions."
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
```

### Message Roles and Context Management

The application uses three types of messages:

- **Developer:** Sets the initial context or persona for the AI. In this app, it defines the AI as a helpful programming assistant.
- **User:** Represents user inputs (questions and commands).
- **Assistant:** Captures the AI's responses.

The `messages` variable maintains the conversation's context by storing each message in order. This allows the AI to generate contextually relevant answers, creating a conversational flow.

### Main Loop

The script continuously prompts the user for input and prints AI responses until the user types `BYE` to exit:

```python
def main():
    validate_openai_api_key()
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
```

## 5. Run the CLI Application

Now, start the chatbot by running:

```sh
python main.py
```

You'll see a welcome message:

```
Welcome to Open AI CLI app.
Type your message and press enter to chat with the AI (type BYE to exit the app).
```

Start chatting by typing a message and pressing Enter. Example:

```
You: How can I optimize a database query?
AI: Indexing the columns used in WHERE clauses can speed up queries...
```

To exit, type `BYE`.

## 6. Experiment with AI Parameters

This application is a great playground to explore OpenAI’s models. Try:

- Changing the GPT model in `main.py` (`gpt-4o-mini` → `gpt-3.5-turbo`, etc.).
- Adjusting temperature values (`1.5` → `0.7`) to control response randomness.
- Modifying system messages to shape the assistant’s behavior.

## Conclusion

In just few minutes, you’ve: ✅ Set up a Python CLI chatbot powered by OpenAI. ✅ Run AI conversations directly from your terminal. ✅ Learned how to tweak AI responses for different use cases.

Now, keep experimenting and integrating AI into your own applications!

