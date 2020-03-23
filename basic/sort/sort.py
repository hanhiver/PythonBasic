def main():
    with open('./test.txt') as file:
        lines = file.readlines()

    def comp(str):
        if str.split()[1].strip() == 'apm':
            return True
        else:
            return False

    lines.sort(key=comp)
    for line in lines:
        print(line)

if __name__ == '__main__':
    main()

