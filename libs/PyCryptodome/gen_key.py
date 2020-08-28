# 提前pip install pycryptodome
from Crypto.PublicKey import RSA

key = RSA.generate(2048)

# 提取私钥并存入文件
private_key = key.export_key()
with open("/tmp/private_key.pem", "wb") as outfile:
    outfile.write(private_key)

# 提取公钥并存入文件
public_key = key.publickey().export_key()
with open("/tmp/public_key.pem", "wb") as outfile:
    outfile.write(public_key)

