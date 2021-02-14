#include <string>
#include <vector>
using namespace std;

string solution(string new_id) {
    
    //1단계
    for (int i=0; i<new_id.size(); i++){
        new_id[i]=tolower(new_id[i]);
    }
    
    //2단계
    for(int i = 0; i < new_id.size(); ) {
        if ((new_id[i] >= 'a' && new_id[i] <= 'z') || (new_id[i] >= '0' && new_id[i] <= '9')|| new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.'){
            i++;
            continue;
        }
        new_id.erase(i, 1);
    }
    
    //3단계
    for(int i=0; i<new_id.size();){
       if (new_id[i] == '.' && new_id[i - 1] == '.'){
            new_id.erase(i,1);
            continue;
        }
        else i++;
    }
    
    //4단계
    if (new_id.size()>=1){
        if(new_id[0]=='.'){
        new_id.replace(0,1,"");
        }
        if(new_id[new_id.size()-1]=='.'){
            new_id.replace(new_id.size()-1,1,"");
        }
    }
     
    
    //5단계
    if (new_id.size()<=0){
        new_id='a';
    }
    
    //6단계
    if (new_id.size()>=16){
        new_id.erase(15,new_id.size()-15);
    }
    if (new_id[14]=='.'){
        new_id.erase(14,1);
    }
    
    //7단계
    int t= new_id.size();
    if (new_id.size()<=2){
        while(new_id.size()!=3){
            new_id+=new_id.back();
        }
    }
    
    return new_id;
}
