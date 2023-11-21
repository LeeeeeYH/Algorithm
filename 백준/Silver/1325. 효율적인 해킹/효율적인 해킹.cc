#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int M, N;
vector<int> v[10004], res;
queue<int> q;
bool check[10004];

int main() {
	cin >> N >> M;
	int A, B;
	while (M--) {
		cin >> A >> B;
		v[B].push_back(A);
	}

	int tmp, cnt, MAX = 0;
	for (int i = 1; i <= N; i++) {
		cnt = 1;
		check[i] = true;
		q.push(i);
		while (!q.empty()) {
			tmp = q.front();
			q.pop();

			for (int j = 0; j < v[tmp].size(); j++) {
				if (!check[v[tmp][j]]) {
					check[v[tmp][j]] = true;
					q.push(v[tmp][j]);
					cnt++;
				}
			}
		}
		if (cnt > MAX) {
			MAX = cnt;
			res.clear();
			res.push_back(i);
		}
		else if (cnt == MAX)
			res.push_back(i);

		for (int i = 1; i <= N; i++) check[i] = false;
	}

	for (int i = 0; i < res.size(); i++) {
		cout << res[i] << " ";
	}
}