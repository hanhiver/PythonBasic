def __init__():
    get_color()

def get_color():
    for front in [7, 0, 1, 2, 4, 5, 6, 3]:
        for background in [0, 1, 2, 4, 5, 6, 7, 3]:
            if front == background:
                continue
            else:
                str = '\'\\033[1;3' + '{}' + ';4{}m\','
                #str = '\\03' + '{}' +'[1;3' + '{}' + ';44m'
                #print(front, background)
                print(str.format(front, background), end = ' ')

if __name__ == '__main__':
    get_color()


        

