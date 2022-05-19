# def fib(n):
#     n1 = 0
#     n2 = 1
#     fibonacci = 0
#     if n == n1 or n == n2:
#         return n
#     else:
#         for i in range(n):
#             fibonacci = n1 + n2
#             n1, n2 = fibonacci, n1
#         return fibonacci


def pow(x, n, I, mult):
    if n == 0:
        return I
    elif n == 1:
        return x
    else:
        y = pow(x, n // 2, I, mult)
        y = mult(y, y)
        if n % 2:
            y = mult(y, x)
        return y


def matrix_multiple(A, B):
    BT = list(zip(*B))
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in BT] for row_a in A]


def fib(n):
    if n >= 0:
        F = pow([[1, 1], [1, 0]], n, [[1, 0], [0, 1]], matrix_multiple)
        return F[0][1]
    elif n < 0:
        F = pow([[1, 1], [1, 0]], abs(n), [[1, 0], [0, 1]], matrix_multiple)
        if n % 2:
            return F[0][1]
        else:
            return -F[0][1]


if __name__ == '__main__':
    print(fib(-7))
