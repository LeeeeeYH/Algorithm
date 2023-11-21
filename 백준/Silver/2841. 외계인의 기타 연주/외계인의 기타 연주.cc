#include <iostream>
#include <stack>
using namespace std;

stack<int> s[7];

int main() {
	int N, P, cnt = 0; cin >> N >> P;
	int line, flat;
	for (int i = 1; i <= 6; i++) s[i].push(0);

	while (N--) {
		cin >> line >> flat;
		if (s[line].top() < flat) {
			s[line].push(flat);
			cnt++;
		}
		else if(s[line].top() > flat) {
			while (s[line].top() > flat) {
				s[line].pop();
				cnt++;
			}
			if (s[line].top() < flat) {
				s[line].push(flat);
				cnt++;
			}
		}
	}
	cout << cnt;
}