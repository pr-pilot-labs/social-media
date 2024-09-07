import os
import webbrowser
from pathlib import Path

import requests
import json

from dotenv import load_dotenv

load_dotenv()

# API headers including the DEV API key
headers_dev = {
    "Content-Type": "application/json",
    "api-key": os.getenv('DEVTO_API_KEY'),
}

distribution_map = json.loads(Path('distribution.json').read_text())


def read_article(article_id):
    response = requests.get(
        url=f'https://dev.to/api/articles/{article_id}',
        headers=headers_dev
    )

    # Check if the request was successful
    if response.status_code == 200:
        print("Article updated successfully!")
        result = response.json()
        print(result['body_markdown'])
        print('URL:', result['url'])
    else:
        print(f"Failed to update article. Status code: {response.status_code}")
        print("Response:", response.json())


for i, post_file in enumerate(distribution_map.keys()):
    print(f"{i + 1}. {post_file}")

post_number = int(input("Select a post to publish: ")) - 1
selected_post = list(distribution_map.keys())[post_number]
print(f"Selected post: {selected_post}")
article_id = distribution_map[selected_post]
read_article(article_id)