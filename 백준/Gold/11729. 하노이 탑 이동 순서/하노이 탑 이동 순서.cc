#include <iostream>
#include <cmath>
using namespace std;

void move(int start, int end, int h)
{
	if (h == 1)
	{
		cout << start << " " << end << "\n";
		return;
	}
	else
	{
		move(start, 6 - start - end, h - 1);
		move(start, end, 1);
		move(6 - start - end, end, h - 1);
	}
}

int main()
{
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int N;
	cin >> N;
	cout << (int)pow((double)2, N) - 1 << "\n";
	move(1, 3, N);
}