#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    leng = len(sys.argv)
    add = 0
    if leng == 1:
        print('0')
    elif leng > 1:
        for i in range(1, leng):
            add += int(sys.argv[i])
        print('{}'.format(add))
