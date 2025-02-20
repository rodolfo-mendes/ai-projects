# OpenAI CLI

A simple CLI (command-line interface) application to interact with Open AI models.

AI Engineering is a lot about experimentation. Use this app to explore the completion API from Open AI. A few ideas so you can play along:

* Try different GPT models
* Test different developer messages and observe the behavior of the model
* Vary the temperature parameter and observe how the completions are affected
* Test different limits for the number of completion tokens  

## 0. Setup

This app is based on the [Open AI API for Text Generation](https://platform.openai.com/docs/guides/text-generation). Thus you need to signup
to Open AI API and generate an access key to send requests to the API. You may find detailed instructions on how to generate your API key on
this link: [https://platform.openai.com/docs/api-reference/authentication].

After generating you API key, save it to a local file in your computer.

**NOTE**: never save you API key into a versioned folder, even though you do not intend to commit or push the key.

After saving your API key, set the OPENAI_API_KEY environment variable, so the OpenAI SDK is able to attach the key to the requests. Run the following command:

```sh
export OPENAI_API_KEY=$(cat "$HOME/.openai/OPENAI_API_KEY.txt")
```

Or if you are a PowerShell user, run the following command to set your OPENAI_API_KEY environment variable:

```powershell
$env:OPENAI_API_KEY = Get-Content -Path "$HOME\.openai\OPENAI_API_KEY.txt"
```

## 1. Installing dependencies

As mentioned before, this app run on top of the [Open AI SDK](https://platform.openai.com/docs/guides/text-generation) for text generation.
Thus, in order to run the app you first need to install the necessary dependencies. Those are already listed in the [requirements.txt](./requirements.txt)
file, so you just need to run the following command to have them installed: 

```sh
pip install -r ./requirements.txt
```

### Virtual Environment

I highly recommend to create a project specific virtual environment before installing the project's dependencies. Please, check the 
[venv](https://docs.python.org/3/library/venv.html) documentation to learn how to create and activate a virtual environment.

## 2. Running the app

With everything in place, just run the command:

```sh
python main.py
```

and have fun chating with the GPT model.