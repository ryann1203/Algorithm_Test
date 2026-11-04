from collections import deque

def findmin(q, l):  # 그 개수만큼 묶어서 리턴한다.
    cnt = 1
    new_ans = ''
    for idx, a in enumerate(q):
        if idx == 0:
            prev = a
            continue
            
        elif prev == a:
            cnt += 1
            prev = a
        
        else: # 이제 다른게 나왔다 !
            if cnt > 1:
                new_ans += str(cnt)+prev
            else:
                new_ans += prev
                
            cnt = 1
            prev = a
            
        if idx == len(q)-1:
            if cnt > 1:
                new_ans += str(cnt)+a
            else:
                new_ans += a
    
    return new_ans      
    

def solution(s):
    answer = 0
    min_ans = 100000000
    l = len(s)
    
    if l == 1: 
        return 1
    
    for i in range(1, l//2+1): # i는 자를 기준 개수.
        ss = deque(s)
        q = deque()
        
        while ss:
            new = ''
            for j in range(i): # 그 개수만큼 묶어서 new에 더한다.
                if ss:
                    new += ss.popleft()
            
            q.append(new)
        
        val = findmin(q, l) # 이제 여기 묶인 배열에서 여기의 길이를 구해야함
        min_ans = min(len(val), min_ans)
        
    return min_ans