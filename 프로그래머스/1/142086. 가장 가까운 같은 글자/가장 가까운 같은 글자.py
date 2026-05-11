def solution(s):
    answer = [-1 for i in range(len(s))]
    for i in range(len(s)):
        for j in range(i, -1, -1):
            if (i != j) and (s[i] == s[j]):
                answer[i] = i - j
                break
    
    return answer