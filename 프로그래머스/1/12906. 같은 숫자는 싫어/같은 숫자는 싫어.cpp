#include <vector>
#include <stack>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> stack;
    stack.push_back(-1);
    for(auto a : arr) {
        if (stack.back() != a){
            stack.push_back(a);
        }
    }
    
    return vector<int>(stack.begin()+1, stack.end());
}