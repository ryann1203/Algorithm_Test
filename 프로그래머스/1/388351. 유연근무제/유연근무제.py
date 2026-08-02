def solution(schedules, timelogs, startday):
    result = 0
    
    for j in range(len(schedules)):
        flag = True
        for i in range(7):
            day = (startday + i) % 7
            if day == 6 or day == 0:
                continue
            
            hour = schedules[j] // 100
            minute = schedules[j] % 100
            test = schedules[j] + 10
            
            if minute + 10 >= 60:
                minute += 10
                minute -= 60
                hour += 1
                test = hour*100 + minute
                
                if hour >= 24 :
                    test = minute
                
            if timelogs[j][i] > test : 
                flag = False
        
        if flag : result += 1
    
    return result