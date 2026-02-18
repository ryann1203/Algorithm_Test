from collections import deque
def solution(priorities, location):
    deq = deque()
    cnt = 0
    max_val = max(priorities)
    
    for idx, val in enumerate(priorities):
        deq.append((idx, val))
    
    while deq:
        index, val = deq.popleft()
        if val == max_val:
            if index == location:
                answer = cnt + 1
                break
                
            max_val = max(d[1] for d in deq) # val값들 중 최댓값 다시 갱신
            cnt += 1
            continue
            
        else:
            deq.append((index, val))

    return answer