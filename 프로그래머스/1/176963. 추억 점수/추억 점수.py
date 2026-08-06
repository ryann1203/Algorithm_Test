def solution(name, yearning, photo):
    result = [0 for i in range(len(photo))]
    dic = {}
    
    for index, names in enumerate(name):
        dic[names] = yearning[index]
        
    for index, arr in enumerate(photo):
        for val in arr:
            if val in dic:
                result[index] += dic[val]
                
    return result