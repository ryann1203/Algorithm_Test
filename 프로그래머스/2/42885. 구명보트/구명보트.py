def solution(people, limit):
    answer = 0
    limit2 = limit
    visited = [False]*len(people)
    people.sort()
    i = 0
    j = len(people)-1
    
    while True:
        if i > j:
            break
            
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
            answer += 1
            continue
            
        else:
            j -= 1
            answer += 1
            continue             
        
    return answer