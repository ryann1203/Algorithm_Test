def func(word, count, answer, arr):
    i = 0
    while (''.join(answer) != word) :
        # i = 전 answer의 마지막항의 arr에서의 인덱스.
        if i == 4:
            i = 0        
        
        # 마지막이 U라면, 그리고 길이가 5라면
        if len(answer) == 5 and answer[-1] == 'U': # U로부터 2칸 더 뒤로 가야함.
            while answer[-1] == 'U':
                answer.pop()
        
            i = arr.index(answer.pop()) # 바꿔야하는 애 index 알아내기.  
            # U 다 빼내고 나왔으면 U 전 애를 다음 알파벳 넣기.
            answer.append(arr[i%4 +1]) # 그리고 그 다음 친구를 넣어야 함.
    
        # 여긴 이제 마지막이 U가 아니고, 길이가 5인 경우.
        elif len(answer) == 5 and answer[-1] != 'U':
            answer.pop() # 하나 빼고
            answer.append(arr[i+1])
        
        # 그냥 일반적인 경우 채울 때. 길이 5 아니고, 끝도 U 아닐 때. 
        # 즉 길이가 5가 아니라는거는 다시 A부터 채운다.
        else:
            answer.append(arr[0])
            
        i = arr.index(answer[-1])
        count += 1
        
    return count
 
    

def solution(word):
    count = 1
    answer = ['A']
    arr = ['A', 'E', 'I', 'O', 'U']
    
    count = func(word, count, answer, arr)
    
    return count