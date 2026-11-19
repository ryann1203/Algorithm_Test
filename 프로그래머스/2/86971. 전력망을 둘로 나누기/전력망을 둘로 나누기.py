import copy

def dfs(dic2, start, visited2, cnt):
    for nodes in dic2[start]:
        if not visited2[nodes]:
            visited2[nodes] = True

            cnt += dfs(dic2, nodes, visited2, 1)
            
    return cnt
    
    

def solution(n, wires):
    answer = 1000000
    dic = {i:[] for i in range(1, n+1)}
    visited = [False for _ in range(n+1)]
    
    # dic 세팅
    for w in wires:
        dic[w[0]].append(w[1])
        dic[w[1]].append(w[0])

    
    for key, val in dic.items():
        
        # 하나 돌 때마다 dic2에서 없애보기
        for idx, vals in enumerate(val):
            # 반복 한 번 할 때마다 다시 복사. 
            dic2 = copy.deepcopy(dic)
            visited2 = copy.deepcopy(visited)
            
            dic2[key].remove(vals)
            dic2[vals].remove(key)
            
            # dfs 탐색 시작할 시작.
            start = key
            visited2[start] = True
            cnts = dfs(dic2, start, visited2, 1)
            
            answer = min(answer, abs(cnts - (n - cnts)))
        
    
    return answer