def dfs(begin, target, words, ans, d):
    print(ans)
    l = len(begin)
    
    for w in words: # w는 이제 새로 보려는 애.
        cnt = 0
        cnt2 = 0
        
        if w in ans:
            continue
        
        for i in range(l):
            if w[i] != begin[i]: 
                # 하나씩 돌면서 같나 안 같나 확인. 다만 기존 경로에 없어야함.
                cnt += 1
            
            if begin[i] != target[i]: 
                # 하나씩 돌면서 같나 안 같나 확인. 다만 기존 경로에 없어야함.
                cnt2 += 1
        
        if cnt2 == 1: # target이랑 하나만 다름.
            return d+1
                
        if cnt == 1: # 다른게 하나라면 dfs 실행할 가치가 있다.
            ans.append(w)
            result = dfs(w, target, words, ans, d+1)
                # 이제 비교하는건 w가 됨.
                # 이쪽으로 가는게 정답이라면 True를 반환할 것,
                # 정답이 아니라면 False 반환할 것. 
                # -> 그러면 지금 출발점에서 하나 다른 애를 또 찾아야함.
                
            if result : # result 값이 있다면 result 반환(깊이 반환)
                return result
            
            else: # result False면 다른 길로.
                continue
        
        else: # 1도 아니고 0도 아니면 2개 이상 다름, 
              # 다음 애 더 탐색해봐야함.
              # 만약 마지막이라면 이 길 아니므로 다시 백한다.
                
            if d > 0 and words.index(w) == -1: 
                # 시작점 넘음, 끝까지 옴.
                # ans에서 잘못된 길이므로 pop한다.
                ans.pop()
                return False

def solution(begin, target, words):
    ans = []
    if target not in words:
        return 0
    
    answer = dfs(begin, target, words, ans, 0)
    
    return answer