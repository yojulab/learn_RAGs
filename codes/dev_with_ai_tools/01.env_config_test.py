import os
from dotenv import load_dotenv

load_dotenv()

print(f'load OPENAI_API_KEY : {os.getenv('OPENAI_API_KEY')}')