# TODO from datetime import

def calc_fact(n):
    if n == 1:
        return n

    return n * calc_fact(n - 1)


n = int(input())
print(calc_fact(n))

res = 1
for i in range(1, n + 1):
    res *= i
print(res)
