def dfs(visited, dic, val, ans, tickets):
    # 모든 티켓을 사용했으면 완료
    if len(ans) == len(tickets) + 1:
        return True

    for i, next in enumerate(dic[val]):
        if not visited[val][i]:
            visited[val][i] = True
            ans.append(next)

            if dfs(visited, dic, next, ans, tickets):
                return True

            # 이 경로로 모든 티켓을 사용할 수 없다면 되돌리기
            ans.pop()
            visited[val][i] = False

    return False


def solution(tickets):
    sets = set()

    for val in tickets:
        for items in val:
            sets.add(items)

    dic = {s: [] for s in sets}
    visited = {s: [] for s in sets}

    for val in tickets:
        dic[val[0]].append(val[1])
        visited[val[0]].append(False)

    # 알파벳 순서가 앞선 경로부터 탐색
    for key in dic:
        dic[key].sort()

    ans = ["ICN"]
    dfs(visited, dic, "ICN", ans, tickets)

    return ans