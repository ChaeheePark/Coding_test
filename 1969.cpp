#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
#pragma warning (disable : 4996)

int main() {
	int n, m;
	cin >> n >> m;
	char dna[1000][50];
	int i, j, k;
	int diff = 0;
	char res[50];
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			cin >> dna[i][j];
		}
	}
	for (j = 0; j < m; j++) {
		int tmp[4] = { 0, };
		for (i = 0; i < n; i++) {
			if ('A' == dna[i][j]) tmp[0]++;
			else if ('C' == dna[i][j]) tmp[1]++;
			else if ('G' == dna[i][j]) tmp[2]++;
			else tmp[3]++;
		}
		int max = 0;
		int maxidx = -1;
		for (k = 0; k < 4; k++) {
			if (max < tmp[k]) {
				max = tmp[k];
				maxidx = k;
			}
		}
		if (maxidx == 0) res[j] = 'A';
		else if (maxidx == 1) res[j] = 'C';
		else if (maxidx == 2) res[j] = 'G';
		else res[j] = 'T';
		for (k = 0; k < n; k++) {
			if (res[j] != dna[k][j]) {
				diff++;
			}
		}
	}
	for (i = 0; i < m; i++) printf("%c", res[i]);
	cout << '\n' << diff;
	return 0;
}
