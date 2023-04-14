# pygpt4

A minimal Python wrapper for OpenAI's GPT-4 API, handling chat history and supporting both standard calls and streaming responses.

## Installation

Clone the repository and install the library locally:

```bash
git clone https://github.com/lyramakesmusic/pygpt4.git
cd pygpt4
pip install -e .
```

## Usage

Import `gpt4` and create an instance with your OpenAI API token:

```python
from gpt4 import gpt4

model = gpt4(api_key)
   
# You can optionally specify a system prompt:
model = gpt4(api_key, sys="You are a clever, creative AI assistant.")
```

To securely manage your OpenAI API token, use the `dotenv` library (install with `pip install python-dotenv`). Create a `.env` file in your project's root directory with your token: 

`OPENAI_API_KEY=your_openai_api_token`

   ```python
   from gpt4 import gpt4
   from dotenv import load_dotenv
   import os

   load_dotenv()
   api_key = os.getenv("OPENAI_API_KEY")

   model = gpt4(api_key)
   ```

### Single API Call

Send a prompt to the GPT-4 API and receive the response:

```python
response = model.call("prompt")

# temp is 0.1 by default
response = model.call("follow-up", temp=1.0)
```

### Streaming API Call

Send a prompt to the GPT-4 API and stream the response chunks:

```python
# model.stream() is a generator function
for chunk in model.stream(prompt, temp=0.4):
    print(chunk)
```

### Clear Chat History

Reset the chat history of the instance to its initial state:

```python
model.clear()
```

### Multiple Users

Instead of adding complexity by making this wrapper handle multiple users, you can simply create a separate instance for each user:

```python
user1 = gpt4(api_key, sys="You are a kind, helpful chatbot.")
user2 = gpt4(api_key, sys="You are a sarcastic, angry chatbot.")

user1.call("user 1's session")
user2.call("user 2's session")
```

### Other models

If gpt4 is overkill for your task (too expensive), you can pass "model" to the chat call:

```python
response = model.call("prompt", model="gpt-3.5-turbo")
```
