import string

def solution(s, skip, index):
    answer = ''
    my_list = ''
    
    for ch in string.ascii_lowercase:
        if ch not in skip:
            my_list += ch
    
    print(my_list)
    l = len(my_list)
    
    for letter in s:
        for j in range(l):
            if my_list[j] == letter:
                answer += my_list[(j+index) % l]
    
    return answer