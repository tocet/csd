#https://pypi.org/project/requests/
import requests as rq

response = rq.get('http://time.jsontest.com')
print(response)

print(response.json())

if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found.")

response = rq.post('https://httpbin.org/post', data = {"car" : "Kia", "mode" : "Sportage","year" : 2022})
print(response)