#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int mini=*min_element(arr.begin(),arr.end());
    for (int i=0; i<arr.size(); i++){
        if(arr[i]!=mini){
            answer.push_back(arr[i]);
        }
    }
    return answer;
}
