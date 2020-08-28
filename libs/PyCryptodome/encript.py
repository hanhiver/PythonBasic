from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP

# 要加密的内容
data = b'Hello, PyCryptodome!'
print('原始字符串内容： ', data)

# 从文件中读取公钥
public_key = RSA.import_key(open('/tmp/public_key.pem').read())

# 实例化加密套件
cipher = PKCS1_OAEP.new(public_key)

# 加密
encrypted_data = cipher.encrypt(data)

# 添加错误
#encrypted_data = encrypted_data.replace(encrypted_data[2:5], encrypted_data[10:13])

# 输出加密后的内容
print('公钥加密后的内容： ', encrypted_data)

# 从文件中读取私钥
private_key = RSA.import_key(open('/tmp/private_key.pem').read())

# 实例化加密套件
cipher = PKCS1_OAEP.new(private_key)

# 解密，如无意外，data为原文
try:
    decrypted_data = cipher.decrypt(encrypted_data)
    # 输出解密后的内容
    print('私钥解密后的内容： ', decrypted_data)
except(ValueError, TypeError):
    print('数据传输出错，解密失败！')




