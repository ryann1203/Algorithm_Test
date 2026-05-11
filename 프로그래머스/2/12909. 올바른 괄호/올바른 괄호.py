def solution(s):
    flag = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(1)
        elif i == ')':
            if not stack: return False
            if stack[-1] == 1: stack.pop()
        
    if stack: flag = False
    return flag