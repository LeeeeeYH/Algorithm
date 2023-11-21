#include <iostream>
#include <algorithm>
using namespace std;
#define INF 987654321;

int area[104];
int road[104][104];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	//입력
	int n, m, r; cin >> n >> m >> r;
	for (int i = 1; i <= n; i++) cin >> area[i];
	//길행렬 초기화
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			road[i][j] = INF;
	for (int i = 1; i <= n; i++)
		road[i][i] = 0;
	//입력
	int ss, ee, ww;
	for (int i = 0; i < r; i++) {
		cin >> ss >> ee >> ww;
		road[ss][ee] = ww;
		road[ee][ss] = ww;
	}
	//floydwarshall
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				road[i][j] = min(road[i][j], road[i][k] + road[k][j]);

	int tmp, MAX = 0;
	for (int i = 1; i <= n; i++) {
		tmp = 0;
		for (int j = 1; j <= n; j++) {
			if (road[i][j] <= m)
				tmp += area[j];
		}
		MAX = max(MAX, tmp);
	}
	cout << MAX;
}