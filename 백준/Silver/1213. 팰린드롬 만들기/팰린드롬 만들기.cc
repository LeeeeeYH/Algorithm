#include <iostream>
#include <string>
using namespace std;

int alp[26];

int main() {
	bool solo = false;
	char soloc;
	string name, res; cin >> name;
	for (int i = 0; i < name.length(); i++)
		alp[name[i] - 'A']++;

	for (int i = 0; i < 26; i++) {
		if (alp[i] % 2 != 0 && !solo) {
			solo = true;
			soloc = (char)('A' + i);
		}
		else if (alp[i] % 2 != 0 && solo) {
			cout << "I'm Sorry Hansoo";
			return 0;
		}
		for (int j = 0; j < alp[i] / 2; j++) res += (char)('A' + i);
	}
	if (solo) res += soloc;
	for (int i = res.length() - 1 - solo; i >= 0; i--)
		res += res[i];
	cout << res;
}