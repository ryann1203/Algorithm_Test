def move(x, y, op, n, park):
    if op == "E":
        dx = 0; dy = 1
    elif op == "S":
        dx = 1; dy = 0
    elif op == "W":
        dx = 0; dy = -1
    elif op == "N":
        dx = -1; dy = 0
    
    old_x = x
    old_y = y
    
    for _ in range(int(n)):
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < len(park) and 0 <= ny < len(park[0]) and park[nx][ny] != "X":
            x = nx; y = ny;
            continue
        else:
            return ((old_x, old_y))
        
    return ((nx, ny))


def solution(park, routes):
    answer = [0, 0]
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x = i; y = j
                break
    
    for route in routes:
        (x, y) = move(x, y, route[0], route[2], park)
    
    answer[0] = x
    answer[1] = y
    
    return answer