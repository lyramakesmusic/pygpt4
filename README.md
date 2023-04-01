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

Keep your OpenAI API token secure and avoid accidentally committing it to version control. You can use the `python-dotenv` library to load the token from an environment file:

1. Install the `python-dotenv` library:

   ```bash
   pip install python-dotenv
   ```

2. Create a `.env` file in your project's root directory and add your OpenAI API token:

   ```
   OPENAI_API_KEY=your_openai_api_token
   ```

3. In your Python script, load the token using `python-dotenv` and create an instance of the `gpt4` class:

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
response = model.call("prompt", temp=0.4)
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
