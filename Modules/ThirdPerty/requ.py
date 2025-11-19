import requests

data=requests.get("https://fakestoreapi.com/products")
# print(data)

jsonData=data.json()
print(jsonData)
