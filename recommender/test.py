import  requests

BASE = "http://127.0.0.1:8080/"

response = requests.post(BASE + "helloworld")
print(response.json())