def solution(n, w, num):
    answer = 0
    
    # 0-based index로 변환
    idx = num - 1
    row = idx // w
    
    # num이 위치한 열(col) 계산 (0 ~ w-1)
    if row % 2 == 0:
        col = idx % w
    else:
        col = (w - 1) - (idx % w)
        
    # row층부터 시작해서 (num 자기 자신 포함) 위로 올라가며 상자 존재 여부 확인
    # total_rows = (n - 1) // w
    for r in range(row, ((n - 1) // w) + 1):
        # r번째 층에서 col 위치에 있는 상자의 0-based index 계산
        if r % 2 == 0:
            box_idx = r * w + col
        else:
            box_idx = r * w + (w - 1 - col)
            
        # 해당 상자 번호(+1)가 전체 상자 개수 n 이하이면 카운트
        if box_idx + 1 <= n:
            answer += 1
            
    return answer