#include <iostream>

using namespace std;

long long dp[101];
int t;
int main() {
	cin >> t;
	while (t != 0) {
		dp[0] = 0;
		dp[1] = 1;
		dp[2] = 1;
		for (int i = 3; i <= 100; i++) {
			dp[i] = dp[i - 2] + dp[i - 3];
		}
		int k;
		cin >> k;
		cout << dp[k] << "\n";
		t--;
	}
}