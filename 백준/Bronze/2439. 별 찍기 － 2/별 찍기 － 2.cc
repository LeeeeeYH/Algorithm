#include <iostream>
using namespace std;

int main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = N - i - 1; j > 0; j--)
			cout << " ";
		for (int j = 1; j <= i+1; j++)
			cout << "*";
		cout << endl;
	}
}