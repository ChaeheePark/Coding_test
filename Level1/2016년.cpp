#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    vector<string> d={"FRI","SAT","SUN","MON","TUE","WED","THU"}; //1월1일이 금요일이므로
    vector<int> day={0,31,29,31,30,31,30,31,31,30,31,30,31};
    
    int days=0;
    int i;
    for(i=1; i<a; i++){
        days+=day[i];
    }
    days+=b;
    return d[(days-1)%7];
}
