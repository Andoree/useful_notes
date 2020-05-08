#
import random


def modular_exponentiation(a, b, n):
    c = 0
    d = 1
    b = bin(b)[2:]
    for i in range(len(b)):
        c = 2 * c
        d = (d * d) % n
        if int(b[i]) == 1:
            c = c + 1
            d = (d * a) % n
    return d


def witness(a, n):
    t = 1
    square_t = 2
    u = 0
    while u * (2 ** t) != n - 1:
        u = ((n - 1) // square_t)
        if u % 2 == 0:
            break
        t += 1
        square_t *= 2
        pass
    x0 = modular_exponentiation(a, u, n)
    x_new = 0
    for i in range(1, t + 1):
        x_new = (x0 * x0) % n
        if x_new == 1 and x0 != 1 and x0 != n - 1:
            return True
        x0 = x_new
    if x_new != 1:
        return True
    return False
    # for i in range(1, t):


def miller_rabin(n, s):
    # True, если составное
    unique_a = set()
    for j in range(s):
        a = random.randint(1, n - 1)
        flag = a in unique_a
        while flag:
            a = random.randint(1, n - 1)
            flag = a in unique_a
        unique_a.add(a)
        if witness(a, n):
            return True
    return False


if __name__ == '__main__':
    s = 20
    n = 997661
    res = miller_rabin(n, s)
    if res:
        print(f'Составное: {n}')
    else:
        print(f'Вероятно, простое: {n}')
