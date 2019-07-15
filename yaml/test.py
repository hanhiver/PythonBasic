import yaml
import os

print("Hello, YAML!")
print(yaml.__version__)

file_path = os.path.dirname(__file__)
print(file_path)

filename_path = os.path.split(os.path.relpath(__file__))[0]
print(filename_path)

f = open('./test.yaml', 'r')
cont = f.read()

x = yaml.load(cont, Loader = yaml.FullLoader)
#x = yaml.safe_load(cont)
print(x)

