#include <iostream>
using namespace std;
int exist[100];

int main()
{
	int A, B, C, result = 0;
	int min[6];
	cin >> A >> B >> C;
	for (int i = 0; i < 6; i++)
		cin >> min[i];

	for (int i = min[0]; i < min[1]; i++)
		exist[i]++;
	for (int i = min[2]; i < min[3]; i++)
		exist[i]++;
	for (int i = min[4]; i < min[5]; i++)
		exist[i]++;

	for (int i = 0; i < 100; i++)
	{
		if (exist[i] == 1)
			result += A;
		else if (exist[i] == 2)
			result += 2 * B;
		else if (exist[i] == 3)
			result += 3 * C;
	}
	cout << result << endl;
}