def solution(id_list, report, k):
    answer = []
    hashdict = {} # 누가 누구에게 신고당했는지 기록한다.
    count = {} # 각 유저가 최종적으로 받을 결과 메일의 개수를 저장한다.
    for i, name in enumerate(id_list):
        hashdict[name] = set() # 여러 이름을 담을 수 있도록 초기화를 set으로
        count[name] = 0 # count dict에 name을 key로 해서 0 저장
    
    for r in report:
        rep, reped = r.split()
        hashdict[reped].add(rep) # 신고받은 사람의 dict에 신고자 저장
            
    for i in id_list:
        if len(hashdict[i]) >= k: # i 이름이 k번 이상 신고 받았으면
            for h in hashdict[i]: # i가 key인 hashdict의 신고자목록 동안
                count[h] += 1 # 신고자가 key인 hashdict에 값 1 추가
            
    answer = list(count.values()) # 그렇게 추가된 count를 list로 변환
    return answer