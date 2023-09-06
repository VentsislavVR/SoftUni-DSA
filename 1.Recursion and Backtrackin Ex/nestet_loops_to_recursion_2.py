def nestet_loops(idx, arr):
    if idx >=n:
        print(*arr)
        return
    for num in range(1,n+1):
        arr[idx]=num
        nestet_loops(idx+1,arr)


n = int(input())
arr = [None] * n
nestet_loops(0, arr)
