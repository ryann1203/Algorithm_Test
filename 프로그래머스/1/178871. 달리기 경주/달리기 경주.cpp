#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

vector<string> solution(vector<string> play, vector<string> callings) {
    map<string, int> mymap;
    int call_idx;
    string front_name;
    
    for ( int i = 0; i < play.size(); i++) {
        string name = play[i];
        mymap[name] = i; 
        // map에 name을 인덱스, i를 val로 저장
    }
    
    for(auto c : callings) {
        call_idx = mymap[c]; // c의 위치
        front_name = play[call_idx - 1]; // c 앞에 있는 애의 이름
        swap(play[call_idx], play[call_idx - 1]); // 실제 play 배열도 업데이트
        
        mymap[c]--, mymap[front_name]++;
        
    }
    
    
    return play;
}