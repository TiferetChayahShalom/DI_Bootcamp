# LIVE DEMO — Exploring the Response object
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# 1. Status code — did it work?
print("Status code:", response.status_code)  # 200 = OK
print()

# 2. The JSON data — as a Python dict!
data = response.json()
print("Type:", type(data))    # <class 'dict'>
print("Name:", data["name"])  # Leanne Graham
print("Email:", data["email"])
print("City:", data["address"]["city"])  # nested!
print()

# 3. Raw text — for debugging
print("Raw text (first 100 chars):", response.text[:100])
