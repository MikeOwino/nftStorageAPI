import http.client

conn = http.client.HTTPSConnection("api.nft.storage")
payload = ''
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer <API HERE>',
}
conn.request("GET", "/?before=2020-07-27T17%253A32%253A28Z&limit=10%0A", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))