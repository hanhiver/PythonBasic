import pathlib

p = pathlib.Path('.')
dirs = [x for x in p.iterdir() if x.is_dir()]
print(dirs)

print()

pp = pathlib.PurePath('/usr/local')
print(pp)

cuda = pp / 'cuda'
print(cuda)
print(bytes(cuda))

hosts = pathlib.PurePath('/etc/hosts')
with open(hosts, 'r') as hfile:
    lines = hfile.readlines()

print(lines)
