import math
n = int(input())
m = int(input())
max_d = 0
arr = [0] + list(map(int, input().split())) + [n]

for i in range(1, m+2):
    if i > 1 and i < m+1:
        if (arr[i] - arr[i-1]) / 2 > max_d:
            max_d = (arr[i] - arr[i-1]) / 2
    else:
        if arr[i] - arr[i-1] > max_d:
            max_d = arr[i] - arr[i-1]

print(math.ceil(max_d))