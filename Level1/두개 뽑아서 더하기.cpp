#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    int i,j;
    vector<int> answer;
    int size=numbers.size();
    for (i=0; i<size-1; i++){
        for(j=i+1; j<size; j++){
            answer.push_back(numbers[i]+numbers[j]);
        }
    }
    sort(answer.begin(),answer.end());
    answer.erase(unique(answer.begin(),answer.end()),answer.end());
    return answer;
}
