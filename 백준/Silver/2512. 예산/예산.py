n = int(input())
arr = list(map(int, input().split()))
m = int(input())
ans = 0
avg = m // n

arr.sort()
for i in range(n):
    # 현재 상한액 후보
    current_limit = m // (n - i)

    # 요청액이 상한액 후보보다 작다면
    if arr[i] <= current_limit:
        m -= arr[i]  # 요청한 만큼 다 주고 남은 돈 갱신

    # 요청액이 상한액 후보보다 크다면
    else:
        ans = current_limit  # 상한액 후보만큼 받는다.
        m = 0
        break

else:  # 요청액 다 줬는데 m이 남았다면
    ans = arr[-1]  # 가장 큰 요청액이 답

print(ans)