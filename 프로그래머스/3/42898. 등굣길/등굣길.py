def solution(m, n, puddles):
    dp = [[1] * n for _ in range(m)]
    
    for p in puddles:
        dp[p[0]-1][p[1]-1] = -1
        
        if p[0] == 1:
            for k in range(p[1], n):
                dp[0][k] = -1
                
        if p[1] == 1:
            for k in range(p[0], m):
                dp[k][0] = -1
        
    for i in range(1, m):
        for j in range(1, n):
            if dp[i][j] == -1:
                continue
            
            if dp[i-1][j] == -1 or dp[i][j-1] == -1:
                if dp[i-1][j] == -1:
                    dp[i][j] = dp[i][j-1]
                    
                if dp[i][j-1] == -1:
                    dp[i][j] = dp[i-1][j]
                    
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

                
    if dp[m-1][n-1] == -1:
        return 0
    
    return dp[m-1][n-1] % 1000000007