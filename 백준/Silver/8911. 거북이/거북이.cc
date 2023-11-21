#include <iostream>
#include <string>
using namespace std;

int x, y, max_x, max_y, min_x, min_y;
int state; //1:북 2:동 3:남 4:서

void front();
void back();
void left();
void right();

int main() {
	int T; cin >> T;
	string s;
	char c;
	for (int a = 0; a < T; a++) {
		x = 0; y = 0;
		max_x = 0; max_y = 0; min_x = 0; min_y = 0;
		state = 1;
		cin >> s;
		for (int i = 0; i < s.length(); i++) {
			c = s[i];
			if (c == 'F') front();
			else if (c == 'B') back();
			else if (c == 'L') left();
			else if (c == 'R') right();
		}

		cout << (max_x - min_x) * (max_y - min_y) << "\n";
	}
}

void front()
{
	switch (state) {
	case 1:y++; 
		if (max_y < y) max_y = y;
		break;
	case 2:x++; 
		if (max_x < x) max_x = x; 
		break;
	case 3:y--; 
		if (min_y > y) min_y = y; 
		break;
	case 4:x--; 
		if (min_x > x) min_x = x; 
		break;
	}
}

void back()
{
	switch (state) {
	case 1:y--; 
		if (min_y > y) min_y = y; 
		break;
	case 2:x--; 
		if (min_x > x) min_x = x; 
		break;
	case 3:y++; 
		if (max_y < y) max_y = y;
		break;
	case 4:x++; 
		if (max_x < x) max_x = x; 
		break;
	}
}

void left()
{
	state--;
	if (state == 0) state = 4;
}

void right()
{
	state++;
	if (state == 5) state = 1;
}
