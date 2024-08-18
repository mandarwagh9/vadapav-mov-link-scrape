import os

def get_html(url):
    # Replace with the actual implementation
    import requests
    response = requests.get(url)
    return response.text

def append_to_file(file, text):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(text + '\n')

def join_url(base, path):
    from urllib.parse import urljoin
    return urljoin(base, path)

def clear_file(file):
    open(file, 'w').close()

def get_input(prompt):
    return input(prompt)
