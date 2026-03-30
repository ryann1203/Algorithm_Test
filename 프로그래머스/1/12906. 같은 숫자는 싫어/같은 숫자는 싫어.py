def solution(arr):
    stack = [-1]
    for a in arr:
        if stack[-1] != a:
            stack.append(a)
    
    return stack[1:]