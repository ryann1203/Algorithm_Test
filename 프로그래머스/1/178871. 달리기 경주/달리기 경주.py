from collections import deque

def solution(play, callings):
    answer = []
    dic = {}
    
    for idx, p in enumerate(play):
        dic[p] = idx
    
    for call in callings:
        # dic[call] = idx 나타냄
        # play = 실제 순서(정답)
        # dic = 이름 -> 인덱스
        
        call_pos = dic[call] #call의 원래 위치 저장
        name = play[call_pos-1] #call 앞에 있는 애의 이름
        
        play[dic[call]-1], play[dic[call]] = play[dic[call]], play[dic[call]-1] # 실제 추월 상황 반영
        
        dic[call] -= 1 # 순위 저장도 업데이트
        dic[name] += 1      

    answer = play
    return answer