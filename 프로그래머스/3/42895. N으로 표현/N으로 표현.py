def solution(N, number):
    if number == N: return 1

    answer = -1
    dp = [[0] for _ in range(9)]
    
    # dp[k] = N을 k번 써서 만들 수 있는 수들의 집합.
    dp[1] = [N]
    dp[2] = [10*N + N, N+N, N-N, N/N, N*N]
    
    if number in dp[2]: 
        return 2
    
    for i in range(3, 9):
        dp[i][0] = int(str(N)*i)
        
        for k in range(1, i):
            sets = set()
            for d in dp[k]:
                for ds in dp[i-k]:
                    sets.add(d + ds)
                    sets.add(d - ds)
                    sets.add(ds - d)
                    sets.add(d * ds)
                    if ds:
                        sets.add(d // ds)
                    if d:
                        sets.add(ds // d)
            
            dp[i].extend(list(sets))
            
            if number in dp[i] :
                answer = i
                return answer
    
    
    return answer