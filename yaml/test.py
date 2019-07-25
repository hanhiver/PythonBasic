import yaml
import sys

print("Hello, YAML!")
print(yaml.__version__)

f = open(sys.argv[1], 'r')
cont = f.read()

x = yaml.load(cont, Loader = yaml.FullLoader)
#x = yaml.safe_load(cont)
print(x)

