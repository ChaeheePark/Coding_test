#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    
    vector<int> score={0,0,0};
    vector<int> first={1,2,3,4,5};
    vector<int> second={2,1,2,3,2,4,2,5};
    vector<int> third={3,3,1,1,2,2,4,4,5,5};
    for (int i=0; i<answers.size(); i++){
        if (answers[i]==first[i%5]){
            score[0]++;
        }
        if (answers[i]==second[i%8]){
            score[1]++;
        }
        if (answers[i]==third[i%10]){
            score[2]++;
        }
    }
    vector<int> answer;
    
    int s=*max_element(score.begin(),score.end());
  
    for(int i = 0; i< 3; i++) {
        if(score[i] == s) answer.push_back(i+1);
    }
    return answer;
}
