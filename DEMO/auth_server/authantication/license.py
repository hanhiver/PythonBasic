"""
定义license的数据结构。
License内包含两个内含类：ServerLicense和ClientLicense
"""
import uuid # 用来生成特定license的ID. 
from Crypto.PublicKey import RSA 

class ServerLicense(object):
    def __init__(self, license_id:str, private_key:bytes, app_name:str, vender_name:str):
        self.license_id = license_id
        self.app_name = app_name
        self.vender_name = vender_name
        self.private_key = private_key
    
    def read(self, filepath:str):
        pass 

class ClientLicense(object):
    def __init__(self, license_id:str, public_key:bytes, app_name:str, vender_name:str):
        self.license_id = license_id
        self.app_name = app_name
        self.vender_name = vender_name
        self.public_key = public_key
    
    def read(self, filepath:str):
        pass 

class License(object):
    def __init__(self, app_name:str, vender_name:str):
        self.license_id = uuid.uuid5(uuid.NAMESPACE_DNS, app_name + ":" + vender_name)
        self.key = RSA.generate(2048)
        # 获取私钥
        self.private_key = self.key.export_key()
        # 获取对应的公钥
        self.public_key = self.key.publickey().export_key()
        self.server_license = ServerLicense(self.license_id, self.private_key, app_name, vender_name)
        self.client_license = ClientLicense(self.license_id, self.public_key, app_name, vender_name)

    

