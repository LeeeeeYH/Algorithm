#include <iostream>
#include <queue>
#include <functional>
using namespace std;

priority_queue<int> MaxH;
priority_queue<int, vector<int>, greater<int>> MinH;

int main() {ios::sync_with_stdio(false); cin.tie(0);
	int N, in, tmp; cin >> N;

	cin >> in;
	MaxH.push(in);
	cout << MaxH.top() << "\n";

	for (int a = 1; a < N; a++) {
		cin >> in;
		MaxH.push(in);
		if (MaxH.size() >= MinH.size() + 2) {
			MinH.push(MaxH.top());
			MaxH.pop();
		}
		if (MaxH.top() > MinH.top()) {
			tmp = MaxH.top();
			MaxH.pop();
			MaxH.push(MinH.top());
			MinH.pop();
			MinH.push(tmp);
		}
		cout << MaxH.top() << "\n";
	}
}