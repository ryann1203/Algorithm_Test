def solution(message, spoiler_ranges):
    answer = 0
    start = 0
    while start < len(message) and message[start] == " ":
        start += 1
    
    arr = list(message.split()) # 단어들 나눠서 저장
    
    
    lenarr = [[0] for _ in range(len(arr))] # 단어마다 범위 인덱스 저장
    dic = {m: [] for m in arr}
    visited = {key: False for key in dic}
    
    # 딕셔너리 생성
    for idx, mes in enumerate(arr):
        if idx == 0:
            lenarr[idx] = [start, start + len(mes)-1]
            check = lenarr[idx][1]
            
        else:
            if len(mes) == 1:
                lenarr[idx] = [check+2, check+2]
            
            else:
                lenarr[idx] = [check+2, check+2 + len(mes)-1]
            
            check = lenarr[idx][1]
    
    for idx in range(len(arr)):
        dic[arr[idx]].append(lenarr[idx]) 
    
    # message가 이제 spolier와 겹치나 안 겹치나 확인.
    for s in spoiler_ranges:
        
        for key, values in dic.items():
            # dic의 val들에 대해 s의 범위가 겹치는가?
            for v in values:
                if (s[0] <= v[1] <= s[1]) or (s[0] <= v[0] and v[1] <= s[1]) or (s[0] <= v[0] <= s[1]) or (v[0] <= s[0] and s[1] <= v[1]) :
                    
                    # 이 val에 대한 key의 길이가 1보다 크면 중요단어 아님.
                    if not visited[key] and len(dic[key]) == 1 :
                        visited[key] = True
                        answer += 1
                        
                    elif not visited[key] and len(dic[key]) > 1:
                        cnt = 0
                        
                        for vals in dic[key]:
                            for ss in spoiler_ranges:
                                if (ss[0] <= vals[1] <= ss[1]) or (ss[0] <= vals[0] and vals[1] <= ss[1]) or (ss[0] <= vals[0] <= ss[1]) or (vals[0] <= ss[0] and ss[1] <= vals[1]) :
                                    cnt += 1 # 범위 겹치면 + 1
                                    break

                        if cnt == len(dic[key]):
                            answer += 1
                            visited[key] = True
                    
    
    return answer