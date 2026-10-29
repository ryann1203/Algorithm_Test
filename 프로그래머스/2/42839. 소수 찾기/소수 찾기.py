import itertools

def solution(numbers):
    answer = 0
    ans = set()
    arr = list(map(str, numbers))
    new_arr = []
    print(arr)
    
    for i in range(1, len(numbers)+1):
        ans.update(itertools.permutations(arr, i))
        
    for p in ans:
        new_arr.append("".join(p))
        if new_arr[-1][0] == '0':
            new_arr.pop()
    
    new_arr = list(map(int, new_arr))
    print(new_arr)
    
    for num in new_arr:
        flag = True
        for i in range(2, num):
            if num % i == 0: # 나누어 떨어진다면 소수가 아님.
                flag = False
                break
                
        if num != 1 and flag:
            answer += 1    
    
    return answer