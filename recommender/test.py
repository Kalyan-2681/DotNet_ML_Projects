import  requests

BASE = "http://127.0.0.1:8080/"

response = requests.get(BASE + "recommend")
print(response.json())