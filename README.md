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

Import the `gpt4` class and create an instance with your OpenAI API token:

```python
from gpt4 import gpt4

model = gpt4("your_openai_api_token")
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
   
   # You can also specify a system prompt:
   model = gpt4(api_key, sys="You are a clever, creative AI assistant.")
   ```

### Single API Call

Send a prompt to the GPT-4 API and receive the response:

```python
response = model.call("prompt")

response = model.call("follow-up", temp=0.8) # temp is 0.5 by default
```

### Streaming API Call

Send a prompt to the GPT-4 API and stream the response chunks:

```python
import asyncio

async def handle_streaming(model, prompt):
    async for chunk in model.stream(prompt, temp=0.4):
        print(chunk)

asyncio.run(handle_streaming(model, "prompt"))
```

### Clear Chat History

Reset the chat history of the instance to its initial state:

```python
model.clear()
```
