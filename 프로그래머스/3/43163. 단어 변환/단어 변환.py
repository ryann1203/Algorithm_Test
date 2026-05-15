from collections import deque
def bfs(target, words, visited, queue, n):
    
    while queue:
        s, d = queue.popleft()
        
        for i, word in enumerate(words):
            cnt = 0
            for j in range(n):
                if word[j] != s[j]:
                    cnt += 1
            if cnt == 1 and not visited[i]: 
                if word == target: return d+1
                queue.append([word, d+1])
                visited[i] = True
    return 0

def solution(begin, target, words):
    n = len(begin)
    answer = 0
    queue = deque()
    visited = [False for _ in range(len(words))]   
    # 맨 첨에 시작할 애 고르기
    for i, word in enumerate(words):
        cnt = 0
        for j in range(n):
            if word[j] != begin[j]:
                cnt += 1
        if cnt == 1: 
            if word == target: return 1
            queue.append([word, 1])
            visited[i] = True
            
    print(queue)
    answer = bfs(target, words, visited, queue, n)

    return answer