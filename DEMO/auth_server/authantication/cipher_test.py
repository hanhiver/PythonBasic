import unittest
import os
import json
import pickle

from cipher import PublicCipher, PrivateCipher

# 提前pip install pycryptodome
from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


class TestCipher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试前准备工作，生成公钥私钥对。
        """
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
        """
        清理之前生成的公钥私钥对资源。
        """
        os.remove("/tmp/private_key.pem")
        os.remove("/tmp/public_key.pem")

    def test_encrypt_decrypt_mssage(self):
        message = b'Hello, this is a Test. '
        encripted_msg, digest = self.public_cipher.encrypt_message(message)
        resumed_msg, signature = self.private_cipher.decrypt_sign_message(encripted_msg)
        self.assertEqual(message, resumed_msg)
        self.assertEqual(True, self.public_cipher.verify_signature(signature, digest))

    def test_encrypt_decrypt_obj(self):
        d = {'time':'2020.08.31 15:30:01',
             'app_name':'miaoxiu', 
             'end_user':'yinglou1'}
        message = json.dumps(d).encode(encoding="utf8")
        encripted_msg, digest = self.public_cipher.encrypt_message(message)
        resumed_msg, signature = self.private_cipher.decrypt_sign_message(encripted_msg)
        resumed_d = json.loads(resumed_msg.decode(encoding="utf8"))
        self.assertEqual(d, resumed_d)
        self.assertEqual(True, self.public_cipher.verify_signature(signature, digest))

if __name__ == '__main__':
    unittest.main()

    
