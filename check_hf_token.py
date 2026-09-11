# This function's only goal is to check if the Hugging Face token set inside environment variables is correct. 
# Type `uv run check_token.py` inside virtual environment terminal and wait for the answer.
# The code come from HF documentation.
def check_hf_token():
    import os
    import requests

    API_URL = "https://router.huggingface.co/v1/chat/completions"
    headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "How many 'G's in 'huggingface'?"
            }
        ],
        "model": "openai/gpt-oss-120b:fastest",
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.json()["choices"][0]["message"])

check_hf_token()