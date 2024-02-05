import os
from dotenv import load_dotenv
from openai import OpenAI
from woocommerce import API

# Load environmental vairables

load_dotenv()

# OpenAI API settings

openai = OpenAI(
    '''
    By default, it looks for an "OPENAI_API_KEY" variable in the environment,
    which should be written in the .env file.
    If you also want to use a non-default OpenAI Organization,
    uncomment the next line and write the ID in the .env file.
    '''
    # organization = os.getenv('OPENAI_ORGANIZATION_ID')
)

# Function to test connection

def generate_text(role, prompt):
    completion = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {
                'role': 'system',
                'content': role,
            },
            {
                'role': 'user',
                'content': prompt,
            }
        ],
    )
    return completion.choices[0].message.content

# WooCommerce API settings

wc = API(
    url = os.getenv('WOO_WEBSITE_URL'),
    consumer_key = os.getenv('WOO_CONSUMER_KEY'),
    consumer_secret = os.getenv('WOO_CONSUMER_SECRET'),
    wp_api = True,
    version = 'wc/v3'
)

# Some initial test

role = input('Tell AI the role you expect it to play: ')
prompt = input('Write a prompt to generate a response: ')

print(generate_text(role, prompt))
print(wc.get('').json())

