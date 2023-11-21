#include <iostream>
#include <queue>
using namespace std;

int edge[1001][1001];
bool visit[1001], visit2[1001];
int N, M, V, f, s;
int tmp;
queue<int> Q;

void DFS(int node);

int main()
{
	cin >> N >> M >> V;
	for (int i = 0; i < M; i++)
	{
		cin >> f >> s;
		edge[f][s] = 1;
		edge[s][f] = 1;
	}

	DFS(V);

	cout << endl;

	Q.push(V);
	cout << V << " ";
	visit2[V] = true;

	while (!Q.empty())
	{
		tmp = Q.front();
		Q.pop();
		for (int i = 1; i <= N; i++)
		{
			if (edge[tmp][i] == 1 && visit2[i] == false)
			{
				visit2[i] = true;
				Q.push(i);
				cout << i << " ";
			}
		}
	}
}

void DFS(int node)
{
	visit[node] = true;
	cout << node << " ";
	for (int i = 1; i <= N; i++)
	{
		if (edge[node][i] == 1 && visit[i] == false)
			DFS(i);
	}
}
