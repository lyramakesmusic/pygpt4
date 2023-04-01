import openai

class gpt4:
    def __init__(self, token, sys_msg="You are a clever, creative AI assistant."):
        self.hist = [{"role": "system", "content": sys_msg}]
        openai.api_key = token

    def call(self, prompt, temp=0.1):
        self.hist.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.hist,
            temperature=temp,
        )
        text_output = response.choices[0]['message']['content'].strip()
        self.hist.append({"role": "assistant", "content": text_output})

        return text_output

    async def stream(self, prompt, temp=0.1):
        self.hist.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.hist,
            temperature=temp,
            stream=True,
        )
        acc_text = ''
        async for chunk in response:
            if 'role' in chunk['choices'][0]['delta']:
                continue
            chunk = chunk['choices'][0]['delta']['content']
            acc_text += chunk
            yield chunk

        self.hist.append({"role": "assistant", "content": ""})

    def clear(self):
        self.hist = [{"role": "system", "content": self.hist[0]["content"]}]

# init multiple users with optional custom system prompts
# user1 = gpt4(token)
# user2 = gpt4(token, "optional system prompt")

# call the api, get response
# response1 = user1.call("prompt", temp=0.4)
# response2 = user1.call("followup")
# user1.clear()

# you can also stream responses
# async for chunk in user2.stream(prompt, temp=0.4):
#   print(f"{user2}: {chunk}")
