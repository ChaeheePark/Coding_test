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
		graph[n1].push_back(n2); // 양방향연결
	}
	for (int i = 1; i <= n; i++) {
		sort(graph[i].begin(), graph[i].end());
	}
}

void dfs(int num) {
	visit[num] = true; //처음 시작 node는 항상 visit=true
	cout << num << " ";
	for (int i = 0; i < graph[num].size(); i++) {
		int next = graph[num][i];
		if (!visit[next]) dfs(next);
	}
}

void bfs(int num) {
	queue<int> q;
	dist[num] = 0; //처음 node와 연결된 node 간의 거리
	q.push(num);
	while (!q.empty()) {
		int curr = q.front(); //curr로 front의 값을 옮김
		cout << curr << " ";
		q.pop(); //맨앞의 값 pop
		for (int i = 0; i < graph[curr].size(); i++) {
			int next = graph[curr][i]; //curr
			if (dist[next] == -1) {
				dist[next] = dist[curr] + 1;
				q.push(next); //next의 값이 앞으로!
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
