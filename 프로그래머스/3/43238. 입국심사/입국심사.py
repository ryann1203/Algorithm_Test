def solution(n, times):
    answer = 0
    times.sort()
    high = times[-1]*n
    low = 1
    
    while low <= high:
        mid = (high + low) // 2
        total = 0
        
        for i in range(len(times)):
            total += mid // times[i]
            
            if total >= n : break
        
        if total < n:
            low = mid + 1
        else:
            high = mid -1
            answer = mid
    
    return answer