#include <cstdio>
#include <iostream>
#include <vector>
#pragma warning (disable:4996)
using namespace std;

int N, M;
vector<int> v;
int visit[9];
	
void input() {
	cin >> N >> M;
}

void go(int cnt) {
	if (cnt == M) {
		for (int i = 0; i < v.size(); i++) {
			cout << v[i] << " ";
		}
		cout << "\n";
		return;
	}
	for (int i = 1; i <= N; i++) {
		if (!visit[i]) {
			v.push_back(i);
			visit[i] = true;
			go(cnt + 1);
			visit[i] = false;
			v.pop_back();
		}
	}
}
int main() {
	input();
	go(0);
}