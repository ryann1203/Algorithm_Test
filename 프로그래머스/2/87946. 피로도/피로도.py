def dfs(start, dungeons, visited, i, cnt):
    # 일단 입장했으니 방문 처리
    visited[i] = True
    # 다시 던전을 돌아야 함.
    best = cnt
    
    for idx, d in enumerate(dungeons):
        # 다시 만족하는 거 발견
        if not visited[idx] and start >= d[0]:
            # 입장비만큼 차감
            result = dfs(start - d[1], dungeons, visited, idx, cnt+1)
            best = max(result, best)
            
            visited[idx] = False
    
    return best

def solution(k, dungeons):
    answer = -1
    check = 0
    start = k
    visited = [False for _ in range(len(dungeons))]
    
    for idx, d in enumerate(dungeons):
        # 안 갔고 입장료 만족하면 dfs 실행
        if not visited[idx] and start >= d[0]:
            check = dfs(start - d[1], dungeons, visited, idx, 1)
            visited[idx] = False
    
        # 더 큰 애가 최댓값
        answer = max(answer, check)
    
    return answer