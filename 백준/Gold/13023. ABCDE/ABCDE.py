import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]
visited = [False for _ in range(node+1)]
depth = 1
ans = 0

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, depth):
    global ans
    if depth == 5:
        print(1)
        exit()

    for neighbor in graph[v]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(neighbor, depth+1)
            visited[neighbor] = False # dfs 끝나고 다시 돌아오는 지점에서 
            # 다시 False로 바꿈. 그래야 다른 경로에서도 이 노드를 지나감

for i in range(node): # 모든 노드를 한번씩 시작점으로 잡아서 DFS 실행.
    depth = 1 
    if not visited[i]:
        visited[i] = True
        dfs(i, depth)
        visited[i] = False
        
print(0)