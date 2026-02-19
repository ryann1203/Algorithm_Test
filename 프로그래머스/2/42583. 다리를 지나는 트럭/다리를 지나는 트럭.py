from collections import deque

def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge = deque([0]*bridge_length)
    wait = deque(truck_weights)
    cur_weight = 0
    
    while bridge:
        cur_weight -= bridge.popleft()
        cnt += 1
        if not wait:
            if cur_weight == 0:
                break
            continue
        
        if len(bridge) < bridge_length:
            if wait[0] + cur_weight <= weight:
                new = wait.popleft()
                cur_weight += new
                bridge.append(new)
            else:
                bridge.append(0)
    
    return cnt