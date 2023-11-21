#include <iostream>
#include <queue>
using namespace std;

int N;
int map[20][20];
queue<pair<pair<int, int>, int>> q; //<<x, y>, state>

bool right(int x, int y) {
	if (map[x][y + 1] == 0 && y + 1 < N) return true;
	else return false;
}
bool down(int x, int y) {
	if (map[x + 1][y] == 0 && x + 1 < N) return true;
	else return false;
}
bool diag(int x, int y) {
	if (map[x][y + 1] == 0 && map[x + 1][y] == 0 && map[x + 1][y + 1] == 0 && x + 1 < N && y + 1 < N) return true;
	else return false;
}

int main()
{
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> map[i][j];

	int x, y; //파이프앞부분 좌표
	int state; //상태 1:가로 2:세로 3:대각선
	int count = 0;
	q.push(make_pair(make_pair(0, 1), 1));
	while (!q.empty()) {
		x = q.front().first.first;
		y = q.front().first.second;
		state = q.front().second;
		q.pop();
		if (x == N - 1 && y == N - 1) {
			count++;
			continue;
		}

		if (state == 1) {
			if (right(x, y))
				q.push(make_pair(make_pair(x, y + 1), 1));
			if (diag(x, y))
				q.push(make_pair(make_pair(x + 1, y + 1), 3));
		}
		else if (state == 2) {
			if (down(x, y))
				q.push(make_pair(make_pair(x + 1, y), 2));
			if (diag(x, y))
				q.push(make_pair(make_pair(x + 1, y + 1), 3));
		}
		else if (state == 3) {
			if (right(x, y))
				q.push(make_pair(make_pair(x, y + 1), 1));
			if (down(x, y))
				q.push(make_pair(make_pair(x + 1, y), 2));
			if (diag(x, y))
				q.push(make_pair(make_pair(x + 1, y + 1), 3));
		}
	}

	cout << count;
}