import http.client

conn = http.client.HTTPSConnection("api.nft.storage")
payload = ''
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer <API HERE>',
}
conn.request("GET", "/bafkreidivzimqfqtoqxkrpge6bjyhlvxqs3rhe73owtmdulaxr5do5in7u", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))