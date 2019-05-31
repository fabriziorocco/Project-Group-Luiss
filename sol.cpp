#pragma GCC optimize("Ofast")
#include <bits/stdc++.h>
// Function that implements Dijkstra's single source shortest path algorithm
// for a graph represented using adjacency matrix representation
using namespace std;
vector<long long int> enGraph[123456];
long long int curNodo;

int main() {
	FILE* fin = fopen("input.txt", "r");
	FILE* fout = fopen("output.txt", "w");
	long long int N, V;
	fscanf(fin, "%lli %lli", &N, &V);
	long long int startNodo = 0;
	long long int endNodo = N-1;
	long long int a, b;
	for (int i = 0; i < V; i++) {
		fscanf(fin, "%lli %lli", &a, &b);
		enGraph[a].push_back(b);
		enGraph[b].push_back(a);
	}
	vector<bool> visited;
	visited.resize(N);
	vector<long long int> cost;
	cost.resize(N);
	memset(&cost[0], -1, N*sizeof(long long int));
	cost[startNodo] = 0;

	queue<long long int> q;
	q.push(startNodo);
	while ((!q.empty()) && (cost[endNodo] == -1)) {
		curNodo = q.back();
		q.pop();
		for (auto e : enGraph[curNodo]) {
			if (visited[e])
				continue;
			cost[e] = cost[curNodo] + 1;
			q.push(e);
			visited[e] = 1;
		}
	}
	fprintf(fout, "%lli\n", cost[endNodo]);
}
