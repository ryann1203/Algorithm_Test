def solution(players, m, k):
    result = 0
    server = 0
    dic = {}
    
    for idx, x in enumerate(players):
        # 이번턴이 빠져야 하는 애라면?
        if idx in dic:
            server -= dic[idx]
            
        if x >= m:
            if (x // m > server):
                result += x//m - server
                dic[idx+k] = x//m - server
                server = x // m
    
    return result