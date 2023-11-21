#include <iostream>
#include <string>
using namespace std;
#define MAX 1000004

char c;
int length;
string str, boom;
char res[MAX];

bool com(int idx) {
	int right = true;
	for (int i = 0; i < length; i++) {
		if (res[idx - i] != boom[length - 1 - i]) {
			right = false;
			break;
		}
	}
	if (right) return true;
	else return false;
}

int main() {
	cin >> str >> boom;
	length = boom.length();
	c = boom[length - 1]; //터뜨릴 문자열의 마지막문자
	int idx = 0;

	for (int i = 0; i < str.length(); i++) {
		res[idx] = str[i];
		if (i >= length - 1 && str[i] == c)
			if (com(idx)) 
				idx -= length;
		idx++;
	}

	if (idx == 0) cout << "FRULA";
	else {
		for (int i = 0; i < idx; i++)
			cout << res[i];
	}
}