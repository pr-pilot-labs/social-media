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


if len(os.sys.argv) == 1:
    print("Please provide a post file as an argument")
    exit()

post_file = os.sys.argv[1]
if post_file not in distribution_map:
    print("Invalid post file", post_file)
    exit()

selected_post_id = distribution_map[post_file]
print(f"Selected post: {post_file}")
read_article(selected_post_id)