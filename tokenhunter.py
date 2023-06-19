import requests as reqs
import json
from dotenv import load_dotenv
import os

load_dotenv()

headers = {
    "PRIVATE-TOKEN": os.getenv('PRIVATE-TOKEN'),
}

response = reqs.get(os.getenv('URL') + '/api/v4/personal_access_tokens', headers=headers)

print(response.status_code)
print(response.text)