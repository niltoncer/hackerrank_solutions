def average(array):
    s = set(array)
    return float(sum(s))/len(s)


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)