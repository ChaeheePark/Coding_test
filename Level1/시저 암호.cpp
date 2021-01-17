#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    string answer = "";
    for(int i=0; i<s.size(); i++){
        if (s[i]==' '){
            answer+=' ';
            continue;
        }
        if (s[i]<='z' && s[i]>='a'){
            if  (s[i]+n>'z'){
                int temp=s[i]+n-'z';
                s[i]='a'-1+temp;
                answer+=s[i];
            }
            else{
                answer+=s[i]+n;
            }
        }
        if(s[i]<='Z' && s[i]>='A'){
            if (s[i]+n>'Z'){
                int temp=s[i]+n-'Z';
                s[i]='A'-1+temp;
                answer+=s[i];
             }
            else{
                answer+=s[i]+n;
            }
        } 
        
        
    }
    return answer;
}
