def solution(clothes):
    answer = 1
    l = len(clothes)
    keys = {c[1] for c in clothes}
    dic = {key: [] for key in keys}

    for value, key in clothes:
        dic[key].append(value)
    
    print(dic)
    
    for key, value in dic.items():
        answer = answer * (len(value)+1)
        
        
    return answer - 1