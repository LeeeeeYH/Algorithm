#include <iostream>
#include <string>
using namespace std;

int queue[10004];

int main()
{
	int N, fro = 0, las = 0;
	string in;

	cin >> N;
	for (int a = 0; a < N; a++) {
		cin >> in;

		if (in == "push") {
			cin >> queue[las];
			las++;
		}
		else if (in == "pop") {
			if (las - fro > 0) {
				cout << queue[fro] << "\n";
				fro++;
			}
			else cout << -1 << "\n";
		}
		else if (in == "size") cout << las - fro << "\n";
		else if (in == "empty") {
			if (las - fro == 0) cout << 1 << "\n";
			else cout << 0 << "\n";
		}
		else if (in == "front") {
			if (las - fro > 0) cout << queue[fro] << "\n";
			else cout << -1 << "\n";
		}
		else if (in == "back") {
			if (las - fro > 0) cout << queue[las - 1] << "\n";
			else cout << -1 << "\n";
		}
	}
}