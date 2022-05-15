def fib(n):
    n1 = 0
    n2 = 1
    fibonacci = 0
    if n == n1 or n == n2:
        return n
    else:
        for i in range(n):
            fibonacci = n1 + n2
            n1, n2 = fibonacci, n1
        return fibonacci


if __name__ == '__main__':
        n = input('Input int num:')
        print(fib(int(n)))
