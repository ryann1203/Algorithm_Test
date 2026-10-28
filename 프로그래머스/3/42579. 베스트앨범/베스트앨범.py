def solution(genres, plays):
    answer = []
    dic = {g : [] for g in genres}
    sumdic = {}
    
    for i, gen in enumerate(genres):
        dic[gen].append(plays[i]) # dic 각각의 요소 집어넣기    
    for key in dic:
        sumdic[key] = sum(dic[key]) # 합계 기준 정렬        
        
    # sorted(정렬대상, key=lambda 요소: 정렬_기준)
    sumdic = dict(sorted(sumdic.items(), key = lambda x : x[1], reverse = True))
    
    for key in sumdic: # 이제 sumdic 안의 key들을 돌며
        dic[key] = sorted(dic[key], reverse = True)
        ans1 = plays.index(dic[key][0])
        answer.append(ans1) #젤 재생수 많은애의 plays 배열의 idx
        
        if len(dic[key]) > 1: # 2개 이상인지 확인
            if dic[key][0] == dic[key][1]: # 같은 값이 있다면 그 다음부터
                answer.append(plays.index(dic[key][1], ans1 + 1))
            
            else:
                answer.append(plays.index(dic[key][1]))
    
    return answer