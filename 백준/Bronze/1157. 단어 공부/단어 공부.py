str = input().upper()
str_set = list(set(str)) # 중복 없는 리스트
arr = []

for s in str_set: # ex. a,b,c
    cnt_num = str.count(s) # 문자열에서 set의 문자들 개수를 str에서 각각 셈.
    arr.append(cnt_num) # arr에 각각의 개수를 넣음. 
                        # 즉, arr의 인덱스는 str_set의 s 순서와 동일.
    
if arr.count(max(arr)) >= 2: # str_set[arr.index(max(arr))]
    print("?")
else:
    print(str_set[arr.index(max(arr))])
