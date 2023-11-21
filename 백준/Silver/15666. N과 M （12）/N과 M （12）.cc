#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int num[10];
int res[10];

void dfs(int id, int cnt) {
	if (cnt == M) {
		for (int i = 0; i < M; i++) {
			cout << res[i] << " ";
		}
		cout << "\n";
		return;
	}
	int tmp = 0;
	for (int i = id; i < N; i++) {
		if (num[i] != tmp) {
			tmp = num[i];
			res[cnt] = num[i];
			dfs(i, cnt + 1);
		}
	}
}

int main()
{
	cin >> N >> M;
	for (int i = 0; i < N; i++)
		cin >> num[i];

	sort(num, num + N);
	dfs(0, 0);
}