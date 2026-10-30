def solution(participant, completion):
    answer = ''
    dic = {p : 0 for p in participant}
    com = {c : 0 for c in completion}
        
    for p in participant:
        dic[p] += 1
        
    for c in completion:
        com[c] += 1
        
    for p in participant:
        if p not in com or com[p] != dic[p]:
            return p