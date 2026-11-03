def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        return False
    
    for ss in s:
        if ss.isalpha():
            return False
    
    return answer