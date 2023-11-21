#include <iostream>
using namespace std;

int main()
{
	int N;
	cin >> N;

	int all = 0, i = 1;
	while (1)
	{
		all += i;
		if (all >= N)
			break;
		i++;
	}

	all -= i;

	if (i % 2 == 0)
		cout << N - all << "/" << (i + 1) - (N - all) << endl;
	else
		cout << (i + 1) - (N - all) << "/" << N - all << endl;
}