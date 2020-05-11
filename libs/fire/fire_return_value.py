import fire 

def hello(name):
    return 'Hello, {name}!'.format(name=name)

def fail(name):
    print("Failed! ", name)
    return 

def pp(name):
    print("PP: ", name)
    return 

if __name__ == '__main__':
    result = fire.Fire()
    print("RESULT: ", result)
