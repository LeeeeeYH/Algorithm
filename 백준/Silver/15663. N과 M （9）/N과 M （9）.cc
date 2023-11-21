#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int num[10];
bool visit[10];
int res[10];

void dfs(int cnt) {
	if (cnt == M) {
		for (int i = 0; i < M; i++) {
			cout << res[i] << " ";
		}
		cout << "\n";
		return;
	}
	int tmp = 0;
	for (int i = 0; i < N; i++) {
		if (!visit[i] && num[i] != tmp) {
			visit[i] = true;
			tmp = num[i];
			res[cnt] = num[i];
			dfs(cnt + 1);
			visit[i] = false;
		}
	}
}

int main()
{
	cin >> N >> M;
	for (int i = 0; i < N; i++)
		cin >> num[i];

	sort(num, num + N);
	dfs(0);
}