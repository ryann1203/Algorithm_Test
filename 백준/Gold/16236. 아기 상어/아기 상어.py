from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 상어의 초기 위치 찾기 및 빈칸 처리
startx, starty = 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            startx, starty = i, j
            arr[i][j] = 0 # 상어가 있던 자리는 이제 빈칸입니다.

def bfs(sx, sy, size):
    # ★ 매번 호출될 때마다 visited와 q를 새로 만들어야 합니다.
    q = deque([(sx, sy, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    cand = []

    while q:
        x, y, dist = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 이동 가능한 경우: 상어 크기보다 작거나 같을 때
                if arr[nx][ny] <= size:
                    visited[nx][ny] = True
                    
                    # 먹을 수 있는 경우: 0보다 크고 상어 크기보다 작을 때
                    if 0 < arr[nx][ny] < size:
                        cand.append((dist + 1, nx, ny))
                    # 단순히 지나가는 경우
                    else:
                        q.append((nx, ny, dist + 1))

    # 우선순위: 거리 -> 위(nx) -> 왼쪽(ny) 순으로 정렬하여 반환
    return sorted(cand)

# 메인 루프
total_time = 0
eat_count = 0
cur_size = 2

while True:
    fish_list = bfs(startx, starty, cur_size)
    
    # 먹을 수 있는 물고기가 없으면 종료
    if not fish_list:
        break

    # 가장 우선순위가 높은 물고기 선택
    dist, nx, ny = fish_list[0]
    
    # 상어의 상태 및 지도 정보 갱신
    total_time += dist
    eat_count += 1
    arr[nx][ny] = 0
    
    # 먹은 개수가 현재 크기와 같으면 사이즈업
    if eat_count == cur_size:
        cur_size += 1
        eat_count = 0

    # ★ 다음 BFS를 시작할 상어 위치 갱신
    startx, starty = nx, ny
    
print(total_time)