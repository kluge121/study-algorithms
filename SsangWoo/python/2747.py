# 피보나치

total = 0


def fibonachi(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = b, a + b
    return b

print(fibonachi(int(input())))
