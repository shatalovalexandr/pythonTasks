def contains_duplicates(list_num):
    return len(list_num) != len(set(list_num))


def sum_of_digit(some_number):
    return (sum(int(i) for i in str(some_number))) if type(some_number) is int else 'Чё, самый умный?'


def largest_number(n):
    return 10 ** n - 1


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':

    print(factorial(5))

    print(largest_number(2))