
if __name__ == '__main__':
    x, y = input("Input two numbers: ").split()
    x, y = int(x), int(y)
    while True:
        if x % y != 0:
            x, y = y, x % y
        else:
            break

    print(y)
