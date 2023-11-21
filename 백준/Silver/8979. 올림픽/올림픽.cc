#include <iostream>
using namespace std;

int main()
{
	int N, K, in, grade = 1, gold, silver, bronze;
	cin >> N >> K;
	
	int **chart;
	chart = new int*[N];
	for (int i = 0; i < N; i++)
		chart[i] = new int[4];

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			cin >> in;
			chart[i][j] = in;
			if (chart[i][0] == K)
			{
				if (j == 1)
					gold = in;
				if (j == 2)
					silver = in;
				if (j == 3)
					bronze = in;
			}
		}
	}
	
	for (int i = 0; i < N; i++)
	{
		if (chart[i][0] != K)
		{
			if (chart[i][1] > gold)
				grade++;
			else if (chart[i][1] == gold)
			{
				if (chart[i][2] > silver)
					grade++;
				else if (chart[i][2] == silver)
				{
					if (chart[i][3] > bronze)
						grade++;
				}
			}
		}
	}

	cout << grade;
}