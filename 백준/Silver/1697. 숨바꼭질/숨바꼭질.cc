#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k; // n이랑 k 선언하고 입력받음

    const int MAX = 100000;

    // 방문 여부 저장
    // front() : 첫 번째 원소 반환
    // 파이썬은 큐에 2개 append할 때 (()) 이렇게 쓰는데
    // c++은 ({}) 이렇게 쓴다.
    vector<bool> visited(MAX+1, false);

    queue<pair<int, int>> q; // 큐에는 현재 위치, 걸린 시간 저장

    q.push({n, 0}); // 시작점 넣기
    visited[n] = true;

    while (!q.empty()) {
        int now = q.front().first;
        int dist = q.front().second;
        q.pop();

        if (now == k) {
            cout << dist << '\n';
            break;
        }

        int next1 = now - 1;
        int next2 = now + 1;
        int next3 = now * 2;

        // now - 1
        if (next1 >= 0 && next1 <+ MAX & !visited[next1]) {
            visited[next1] = true;
            q.push({next1, dist + 1});
        }

        // now + 1
        if (next2 >= 0 && next2 <= MAX && !visited[next2]) {
            visited[next2] = true;
            q.push({next2, dist + 1});
        }

        // now * 2
        if (next3 >= 0 && next3 <= MAX && !visited[next3]) {
            visited[next3] = true;
            q.push({next3, dist + 1});
        }
    }

    return 0;
}