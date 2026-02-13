# mid값 = "가장 인접한 두 공유기 사이의 거리"
# low (최소 거리) = 1 (가장 가까운 두 집 사이의 최소 거리)
# high (최대 거리) = 맨 끝 집과 맨 첫 집 사이의 거리

n, m = map(int, input().split())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())

arr.sort()

#low와 high는 간격 mid의 최소, 최댓값.
low = 1; high = arr[-1] - arr[0];

# "간격이 mid일 때 몇 대 설치 가능할까?" 라는 질문을 매번 새롭게 던지는 과정.
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
        
    else: #cnt가 m보다 큼. 즉 공유기를 충분히 설치함. -> 간격을 더 늘려보자!
        answer = mid
        low = mid + 1
        
print(answer)