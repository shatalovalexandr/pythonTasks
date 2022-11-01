def _find(x, y, setConnected):
    for i in setConnected:
        if x == i[1]:
            result = _find(i[1], y, setConnected)

    return result


if __name__ == '__main__':
    setConnected = []
    while True:
        x = input("Input two numbers: ").split()

        if set(x).issubset(['Q', 'q']):
            break
        if len(x) != 2:
            print("Must be two numbers!!!")
            continue
        setConnected.append(x)
        print(setConnected)
