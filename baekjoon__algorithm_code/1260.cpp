#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;
#pragma warning (disable:4996)

vector<int> graph[1001];
int n, m, v;
bool visit[1001];
int dist[1001];
void input() {
	cin >> n >> m >> v;
	int n1, n2;
	for (int i = 1; i <= m; i++) {
		cin >> n1 >> n2;
		graph[n2].push_back(n1);
		graph[n1].push_back(n2); // ����⿬��
	}
	for (int i = 1; i <= n; i++) {
		sort(graph[i].begin(), graph[i].end());
	}
}

void dfs(int num) {
	visit[num] = true; //ó�� ���� node�� �׻� visit=true
	cout << num << " ";
	for (int i = 0; i < graph[num].size(); i++) {
		int next = graph[num][i];
		if (!visit[next]) dfs(next);
	}
}

void bfs(int num) {
	queue<int> q;
	dist[num] = 0; //ó�� node�� ����� node ���� �Ÿ�
	q.push(num);
	while (!q.empty()) {
		int curr = q.front(); //curr�� front�� ���� �ű�
		cout << curr << " ";
		q.pop(); //�Ǿ��� �� pop
		for (int i = 0; i < graph[curr].size(); i++) {
			int next = graph[curr][i]; //curr
			if (dist[next] == -1) {
				dist[next] = dist[curr] + 1;
				q.push(next); //next�� ���� ������!
			}
		}
	}
}

int main() {
	input();
	dfs(v);
	cout << "\n";
	memset(dist, -1, sizeof(dist));
	bfs(v);
	return 0;
}
