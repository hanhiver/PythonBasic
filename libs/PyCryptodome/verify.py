from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# 需要签名的内容
data = b'Hello, PyCryptodome!'

# 获取签名的内容的HASH值。
digest = SHA256.new(data)
print("Digest: ", digest)

# 读取私钥
private_key = RSA.import_key(open('private_key.pem').read())
# 对HASH值使用私钥进行签名。也就是用私钥对HASH值进行加密。
signature = pkcs1_15.new(private_key).sign(digest)

# 添加错误
signature = signature.replace(signature[2:5], signature[10:13])

print("Signature: ", signature)

# 签名校验部分。
# 签名部分要传给签名校验部分三个信息：签名内容原文、摘要算法、HASH值签名结果
# 获取被签名的内容的HASH值。使用与签名部分一样的摘要算法计算
digest = SHA256.new(data)
# 读取公钥
public_key = RSA.import_key(open('public_key.pem').read())

# 进行签名校验。本质上就是使用公钥解密signature，看解密出来的值是否与digest相等
# 相等则校验通过，说明确实data确实原先的内容；不等则校验不通过，data或signature被篡改
# 可能有人会想，如果我先修改data然后再用自己的私钥算出signature，是不是可以完成欺骗？
# 答案是不能，因为此时使用原先的公钥去解signature，其结果不会等于digest
try:
    pkcs1_15.new(public_key).verify(digest, signature)
    print("签名正确！")
except(ValueError, TypeError):
    print("签名错误！")
    
