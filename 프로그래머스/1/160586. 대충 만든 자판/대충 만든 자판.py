def solution(keymap, targets):
    result = [0]*len(targets)
    key_list = [[0] for _ in range(len(keymap))]
    dic_key = {}
    
    for i, keys in enumerate(keymap):
        key_list[i] = list(keys)
    
    for keys in key_list:
        for j, value in enumerate(keys):
            if value in dic_key and dic_key[value] < j+1: 
                continue
            dic_key[value] = j+1
        
    for i, target in enumerate(targets):
        for j in range(len(target)):
            if target[j] in dic_key:
                result[i] += dic_key[target[j]]
            else:
                result[i] = -1
                break
    
    print(dic_key)
    return result