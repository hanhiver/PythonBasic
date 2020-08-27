import requests
import json

client_id = '谢谢谢谢'
client_secret = '非常感谢'
r = requests.post('http://localhost:8080', json={"client_id": client_id, "client_secret": client_secret})
code = json.loads(r.content)["code"]
print(code)
#code可以正常获取

headers = {'Content-Type': 'multipart/form-data'}
payload = {"client_id":client_id,'client_secret':client_secret, 'grant_type' : 'authorization_code', 'code' : code}
r = requests.post("http://localhost:8080/oauth2/access_token/", headers=headers, data=payload)
print(r.content)