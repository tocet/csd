#https://www.python-httpx.org/
import httpx

response = httpx.get("http://ip.jsontest.com/")
print(response.json())

#h2 package is required
client = httpx.Client(http2=True)
response = client.get("http://ip.jsontest.com/")
print(response.http_version)

response = client.post('https://httpbin.org/post', data = {"car" : "Kia", "mode" : "Sportage","year" : 2022})
print(response)