def solution(arr, k):
    answer = [100000]*2
    ans = 0
    j = 0
    min_len = float('inf')

    for i in range(len(arr)):
        while ans < k and j < len(arr):

            if ans < k:
                ans += arr[j]
                j += 1

        if ans == k:
            if min_len > j-i:
                min_len = j-i
                answer[0] = i
                answer[1] = j-1
        ans -= arr[i]
        
    return answer