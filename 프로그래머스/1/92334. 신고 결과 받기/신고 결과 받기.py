def solution(id_list, report, k):
    answer = []
    hashdict = {}
    count = {}
    for i, name in enumerate(id_list):
        hashdict[name] = set()
        count[name] = 0
    
    for r in report:
        rep, reped = r.split()
        hashdict[reped].add(rep)
            
    for i in id_list:
        if len(hashdict[i]) >= k:
            for h in hashdict[i]:
                count[h] += 1
            
    answer = list(count.values())
    return answer