def solution(pbook):
    answer = True
    pbook.sort()
    for i in range(len(pbook)):
        if i == len(pbook)-1: return True
        if pbook[i+1].startswith(pbook[i]):
            return False