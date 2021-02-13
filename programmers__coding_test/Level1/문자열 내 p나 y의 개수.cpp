#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int count=0;
    for (int i=0; i<s.length(); i++){
        if(s.at(i)=='p'||s.at(i)=='P'){
            count++;
            continue;
        }
        if(s.at(i)=='y'||s.at(i)=='Y'){
            count--;
            continue;
        }
    }
    if(count!=0){
        answer=false;
    }
    return answer;
}
