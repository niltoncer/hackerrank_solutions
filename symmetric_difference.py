M = int(input())
arr_m = set(map(int,list(input().split(' ', M - 1))))
N = int(input())
arr_n = set(map(int,list(input().split(' ', N - 1))))

arr_result = list(arr_n.difference(arr_m)) + list(arr_m.difference(arr_n))
arr_result.sort()
for _ in arr_result:
    print(_)



