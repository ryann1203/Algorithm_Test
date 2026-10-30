from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin, 0))
    visited = [False for _ in range(len(words))]
    
    while queue:
        begin, d = queue.popleft()
        
        if begin == target:
            return d
        
        for idx, word in enumerate(words): 
            # words에서 같은 레벨인 애들은 queue에 같은 레벨 d+1로 담기도록!
            if not visited[idx]:
                cnt = 0
                for i in range(len(word)):
                    if begin[i] != word[i]:
                        cnt += 1
        
                if cnt == 1:
                    visited[idx] = True
                    queue.append((word, d+1))
    
    return 0