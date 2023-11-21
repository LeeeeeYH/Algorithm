#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {ios::sync_with_stdio(false); cin.tie(0);
	queue<int> q;
	string s;
	int N, in; cin >> N;
	for (int a = 0; a < N; a++) {
		cin >> s;
		if (s == "push") {
			cin >> in;
			q.push(in);
		}
		else if (s == "pop") {
			if (q.empty()) cout << -1 << "\n";
			else {
				cout << q.front() << "\n";
				q.pop();
			}
		}
		else if (s == "size")
			cout << q.size() << "\n";
		else if (s == "empty")
			cout << q.empty() << "\n";
		else if (s == "front") {
			if (q.empty()) cout << -1 << "\n";
			else cout << q.front() << "\n";
		}
		else if (s == "back")
			if (q.empty()) cout << -1 << "\n";
			else cout << q.back() << "\n";
	}
}