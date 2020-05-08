import os
import tempfile

def main():
    fp = tempfile.NamedTemporaryFile(delete=False)
    fp.write(b"This is my test. ")
    fn = fp.name
    print(fp.name)
    fp.close()


    with open(fp.name, 'r') as out:
        lines = out.readlines()
        print(lines)
    


if __name__ == '__main__':
    main()