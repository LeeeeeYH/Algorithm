#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int absheap[200004];
int heaplen = 0;
void push(int x);
int pop(int x);


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int N, in;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> in;
		if (in != 0) push(in);
		else {
			if (heaplen > 0)	cout << pop(in) << "\n";
			else cout << 0 << "\n";
		}
	}
}

void push(int x)
{
	heaplen++;
	int len = heaplen;
	absheap[len] = x;
	while (1) {
		if (len != 1) {
			if (abs(x) < abs(absheap[len / 2]))	{
				swap(absheap[len], absheap[len / 2]);
				len /= 2;
			}
			else if (abs(x) == abs(absheap[len / 2])) {
				if (x < absheap[len / 2]) {
					swap(absheap[len], absheap[len / 2]);
					len /= 2;
				}
				else break;
			}
			else break;
		}
		else break;
	}
}

int pop(int x)
{
	int res = absheap[1];
	absheap[1] = absheap[heaplen];
	heaplen--;

	int par = 1;
	int chi;
	while (1) {
		if (abs(absheap[par * 2]) < abs(absheap[par * 2 + 1])) chi = par * 2;
		else if(abs(absheap[par * 2]) > abs(absheap[par * 2 + 1]))chi = par * 2 + 1;
		else {
			if (absheap[par * 2] < absheap[par * 2 + 1]) chi = par * 2;
			else chi = par * 2 + 1;
		}

		if (chi > heaplen || abs(absheap[chi]) > abs(absheap[par])) break;
		if (abs(absheap[chi]) == abs(absheap[par])) {
			if (absheap[chi] > absheap[par]) break;
		}

		swap(absheap[chi], absheap[par]);
		par = chi;
	}
	return res;
}