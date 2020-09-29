# 生成的key都是pkcs1类型的。 
import rsa

lens = 1024

(public_key, private_key) = rsa.newkeys(lens)
with open('public.pem', 'wb') as f:
    f.write(public_key.save_pkcs1())
with open('private.pem', 'wb') as f:
    f.write(private_key.save_pkcs1())