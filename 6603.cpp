#include <cstdio>
#include <iostream>
#pragma warning (disable:4996)
using namespace std;

int k;
int visit[13];
int arr[13];

void go(int idx, int cnt) {
	if (cnt == 6) {
		for (int i = 0; i <6; i++) {
			cout << visit[i] << " ";
		}
		cout << "\n";
		return;
	}
	for (int i = idx; i < k; i++) {
		visit[cnt] = arr[i];
		go(i+1, cnt + 1);
	}
}

int main() {
	while (1) {
		cin >> k;
		if (k == 0) {
			return 0;
		}
		for (int i = 0; i < k; i++) {
			cin >> arr[i];
		}
		go(0, 0);
		cout << "\n";
	}
}