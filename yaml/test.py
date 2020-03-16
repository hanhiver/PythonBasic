import yaml
import sys

print("Hello, YAML!")
print(yaml.__version__)

#f = open(sys.argv[1], 'r')
f = open('./test.yaml', 'r')
cont = f.read()
f.close()

x = yaml.load(cont, Loader=yaml.FullLoader)
x['image'] = "MYIMAGE"

# x = yaml.safe_load(cont)
print(x)

with open('./out.yaml', 'w',  encoding='utf-8') as file: 
    yaml.dump(x, file)


