import os

from dotenv import load_dotenv

a = load_dotenv()

print(os.getenv('DEBUG', 'true'))
print(os.environ.get('DEBUG', 'true'))
print(os.environ)