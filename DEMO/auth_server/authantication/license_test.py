import unittest
import os

from license import PublicCipher, PrivateCipher

# 提前pip install pycryptodome
from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


class TestLicense(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        key = RSA.generate(2048)

        # 提取私钥并存入文件以备测试
        private_key = key.export_key()
        with open("/tmp/private_key.pem", "wb") as outfile:
            outfile.write(private_key)

        # 提取公钥并存入文件以备测试
        public_key = key.publickey().export_key()
        with open("/tmp/public_key.pem", "wb") as outfile:
            outfile.write(public_key)

        cls.public_cipher = PublicCipher(public_key)
        cls.private_cipher = PrivateCipher(private_key)
    
    @classmethod
    def tearDownClass(cls):
        os.remove("/tmp/private_key.pem")
        os.remove("/tmp/public_key.pem")

    def test_encrypt_decrypt_mssage(self):
        message = b'Hello, this is a Test. '
        encripted_msg, digest = self.public_cipher.encrypt_message(message)
        resumed_msg, signature = self.private_cipher.decrypt_sign_message(encripted_msg)
        self.assertEqual(message, resumed_msg)
        print("Message transfer test OK. ")
        self.assertEqual(True, self.public_cipher.verify_signature(signature, digest))
        print("Message signature test OK. ")

if __name__ == '__main__':
    unittest.main()

    
