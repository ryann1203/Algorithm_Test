import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())

arr.sort()
low = 1; high = arr[-1] - arr[0];

while low <= high:
    last_pos = arr[0]
    cnt = 1
    mid = (low+high) // 2

    for a in arr:
        if a - last_pos >= mid:
            last_pos = a
            cnt += 1

    if cnt < m:
        high = mid - 1
        
    else:
        answer = mid
        low = mid + 1
        
print(answer)