import requests

link = "https://dolarhoje.com"

req = requests.get(link)

print('REQ: ', req)
print('TEXT', req.text)