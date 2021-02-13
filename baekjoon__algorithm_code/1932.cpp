#include <iostream>

using namespace std;

int n;
int triangle[501][501];
int ans = -1;

int main() {
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			cin >> triangle[i][j];
		}
	}
	int sum = 0;	
	for (int i = 2; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			if (j == 1) triangle[i][j] += triangle[i - 1][j];
			else if (j == n) triangle[i][j] += triangle[i - 1][j-1];
			else triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1]);
		}
	}
	for (int j = 1; j <= n; j++) {
		ans = max(triangle[n][j], ans);
	}
	cout << ans;
	return 0;
}