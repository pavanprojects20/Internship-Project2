import requests

url = "http://127.0.0.1:5000/login"

data = {
    "username": "admin",
    "password": "admin123"
}

response = requests.post(url, data=data)

print("Attack Sent")
print("Server Response:", response.text)
