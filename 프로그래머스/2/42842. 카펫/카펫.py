def solution(brown, yellow):
    answer = []
    arr = []
    i = 1
    while i * i <= yellow:
        if yellow % i == 0:
            arr.append((i, yellow // i))
            
            if (i+2)*(yellow // i + 2) == brown + yellow:
                answer.append(yellow // i + 2)
                answer.append(i + 2)
                break            
        i += 1
    
    return answer