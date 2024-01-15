#include <iostream>
#include <string>
using namespace std;

int k;
string w, l;
bool same;
bool have[26]; //해당 알파벳이 리트를 가지고 있을때
string Leet[26];

void dfs(int widx, int lidx) { //현재 탐색중인 (원래단어 인덱스, 리트단어 인덱스)
	if (widx == w.length() && lidx == l.length()) { //탐색 완료시
		same = true;
		return;
	}
	if (lidx >= l.length()) return;

	int c = w[widx] - 'a';
	if (!have[c]) { //해당 알파벳의 리트를 할당하지 않았을때
		for (int i = 1; i <= k; i++) {
			//리트 할당
			Leet[c] = "\0";
			for (int j = 0; j < i; j++)
				Leet[c].push_back(l[lidx + j]);

			have[c] = true;
			dfs(widx + 1, lidx + i);
			have[c] = false;
			if (same) return;
		}
	}
	else { //해당 알파벳의 리트가 이미 존재할때
		for (int i = 0; i < Leet[c].length(); i++) //같은지 확인
			if (Leet[c][i] != l[lidx + i]) return;
		dfs(widx + 1, lidx + Leet[c].length());
	}
}

int main() {
	int T; cin >> T;
	for (int test = 0; test < T; test++) {
		//초기화 및 입력
		for (int i = 0; i < 26; i++) have[i] = false;
		same = false;
		cin >> k >> w >> l;

		dfs(0, 0);
		cout << same << "\n";
	}
}