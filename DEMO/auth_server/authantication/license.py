"""
基础的加密解密函数封装。
提供如下功能调用：
客户运行端：
    1. 公钥加密信息。
    2. 公钥验证服务器端私钥签名信息。 
服务器端：
    1. 私钥解密信息。
    2. 私钥对传入信息进行签名。
"""
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class PublicCipher:
    """
    这个类包含对应的公钥创建的cipher，包含用公钥对信息进行加密和用公钥对信息进行验证的功能。
    一般来讲，这部分应该是在客户端处调用，生成用公钥加密后的信息和digest用来通信和校验。
    """
    def __init__(self, public_key:bytes):
        """
        根据提供的public_key初始化PublicCipher.
        """
        try:
            self.key = RSA.import_key(public_key)
            self.cipher = PKCS1_OAEP.new(self.key)
            self.verifier = pkcs1_15.new(self.key)
        except(ValueError, TypeError):
            print("导入公钥出错: %s" % public_key)

    def encrypt_message(self, msg:bytes) -> (bytes, SHA256.SHA256Hash):
        """
        对提供的msg用公钥进行加密。
        输出(加密后的信息，digest校验信息)
        """
        #msg_bytes = msg.encode(encoding="utf8")
        result = self.cipher.encrypt(msg)
        digest = SHA256.new(msg)
        return (result, digest)
    
    def verify_signature(self, sig:bytes, digest:SHA256.SHA256Hash) -> bool:
        """
        给定私钥签名后的信息和digest校验信息，验证信息是否为私钥持有端发送。
        如果校验成功，返回True，否则返回False. 
        """
        #sig_bytes = sig.encode(encoding="utf8")
        try:
            self.verifier.verify(digest, sig)
            return True
        except(ValueError, TypeError):
            return False


class PrivateCipher:
    """
    这个类包含对应的私钥创建的cipher，包含用私钥对信息进行解密和用私钥对信息进行签名的功能。
    一般来讲，这部分应该是在服务器端处调用，用私钥解密收到的信息和对返回的信息进行签名。
    """
    def __init__(self, private_key:bytes):
        """
        根据提供的private_key初始化PrivateCipher.
        """
        try:
            self.key = RSA.import_key(private_key)
            self.cipher = PKCS1_OAEP.new(self.key)
            self.signer = pkcs1_15.new(self.key)
        except(ValueError, TypeError):
            print("导入私钥出错: %s" % private_key)

    def decrypt_sign_message(self, msg:bytes) -> (bytes, bytes):
        """
        对收到的msg用私钥进行解密，同时用私钥对解密后的信息进行数字签名。
        输出(解密后的信息，数字签名信息)
        """
        signature = None
        #msg_bytes = msg.encode(encoding="utf8")
        #msg_bytes = bytes(msg, encoding="utf8")
        try:
            result = self.cipher.decrypt(msg)
        except(ValueError, TypeError):
            result = None
            return (result, signature)

        digest = SHA256.new(result)
        signature = self.signer.sign(digest)
        #result = result.decode(encoding="utf8")
        #signature = signature.decode(encoding="utf8")
        return (result, signature)





