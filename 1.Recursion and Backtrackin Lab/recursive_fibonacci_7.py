def calc_fib(num):
    if num <=1:
        return 1
    return calc_fib(num-1) + calc_fib(num-2)


def iterative_fib(num):
    fib0=1
    fib1=1
    res = 0
    for _ in range(num-1):
        res = fib0 + fib1
        fib0,fib1 = fib1,res
    return res
n=int(input())
print(iterative_fib(n))