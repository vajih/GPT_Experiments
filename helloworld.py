#You should have setup IDE. 
#install openai, on your terminal command line write 'pip3 install openai'
import openai

# Set up your OpenAI API credentials. Get your ChatGPT API from your ChatGPT account
openai.api_key = 'YOUR_API_KEY'

# Interact with ChatGPT
def chat_with_gpt(prompt, max_tokens=100):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Provide the initial prompt
prompt = input("Enter a prompt: ")

# Chat with GPT using the prompt
response = chat_with_gpt(prompt)
print(response)
