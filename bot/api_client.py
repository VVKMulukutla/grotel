
from .config import GROQ_API_KEY
from groq import Groq

def fetch_data_from_groq(input, model):

    client = Groq(api_key=GROQ_API_KEY)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": input,
            }
        ],
        model = model or "mixtral-8x7b-32768",
    )

    return chat_completion.choices[0].message.content
    
