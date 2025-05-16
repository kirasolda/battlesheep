import requests


def make_request():
    url = "http://192.168.100.23:8000/message"
    payload = {"message": "Hello from the client!"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
