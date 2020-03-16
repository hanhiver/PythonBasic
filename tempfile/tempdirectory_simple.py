import os
import tempfile

def main():
    td = tempfile.TemporaryDirectory()
    print("Temp folder: ", td.name)
    
    with open(td.name+"/tmp.txt", 'w') as fp:
        fp.write("This is my test. ")

    with open(td.name+"/tmp.txt", 'r') as out:
        lines = out.readlines()
        print(lines)

    td.cleanup()



if __name__ == '__main__':
    main()