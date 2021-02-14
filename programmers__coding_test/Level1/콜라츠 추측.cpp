#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    long long answer = 0;
    long long n=num;
    int whilecount=0;
    while (n!=1){
        if (n%2==0){
            n/=2;
        }
        else{
            n=n*3+1;
        }
        answer++;
        whilecount++;
        if (whilecount>499) return -1;
    }
    return answer;
}
