def solution(n, times):
    answer = 0
    times.sort()
    low = 1
    total = 0
    high = times[-1]*n
    
    while low <= high:
        mid = (low+high) // 2
        total = 0
        
        for t in times:
            total += mid // t
        
        if total >= n:
            high = mid - 1 # 더 짧은 시간도 가능한지 확인
            answer = mid
        else:
            low = mid + 1
    
    return answer