from collections import deque

n, m = map(int, input().split())
arr = [i for i in range(100001)]
visited = [False]*(100001)

def bfs(arr, n, m):
    q = deque()
    visited[n] = True
    q.append((n, 0))
    
    while q:
        new, dist = q.popleft()
        visited[new] = True

        if new == m :
            print(dist)
            break

        if new-1 >=0 and new-1 < 100001 and not visited[new-1]:
            visited[new-1] = True
            q.append((new-1, dist+1))
        
        if new+1 >=0 and new+1 < 100001 and not visited[new+1]:
            visited[new+1] = True
            q.append((new+1, dist+1))
            
        if 2 * new >=0 and 2 * new < 100001 and not visited[2 * new]:
            visited[2*new] = True
            q.append((2 * new, dist+1))

bfs(arr, n, m)