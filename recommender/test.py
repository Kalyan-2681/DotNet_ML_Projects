import  requests

BASE = "http://127.0.0.1:8080/"

response = requests.get(BASE + "recommend/cust_id")
print(response.json())