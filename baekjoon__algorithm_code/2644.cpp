#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
using namespace std;
#pragma warning (disable : 4996)

vector<int> graph[101];
bool visit[101];
int n, p1, p2, m;
int x, y;
int curr;
int dist[101];

void input() {
	cin >> n >> p1 >> p2 >> m;
	for (int i = 1; i <= m; i++) {
		cin >> x >> y;
		graph[x].push_back(y);
		graph[y].push_back(x);
	}
	if (p1 > p2) {
		int temp = p1;
		p1 = p2;
		p2 = temp;
	}
	for (int i = 1; i <= n; i++) sort(graph[i].begin(), graph[i].end());
}

void bfs(int num) {
	queue<int> q;
	dist[num] = 0; 
	q.push(num);
	while (!q.empty()) {
		curr = q.front(); 
		q.pop();
		for (int i = 0; i < graph[curr].size(); i++) {
			int next = graph[curr][i]; 
			if (dist[next] == -1) {
				dist[next] = dist[curr] + 1;
				q.push(next);
			}
		}
	}
}

int main() {
	input();
	memset(dist, -1, sizeof(dist));
	bfs(p1);
	if (dist[curr] != 0) {
		cout << dist[p2];
	}
	else {
		cout << "-1";
	}
}