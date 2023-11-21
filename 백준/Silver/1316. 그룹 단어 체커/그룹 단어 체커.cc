#include <iostream>
#include <string>
using namespace std;

bool check[26];
void clear();

int main()
{
	int N, count = 0, alpha;
	string word;
	cin >> N;
	for (int a = 0; a < N; a++)
	{
		cin >> word;
		word.append(" ");
		for (int i = 0; i <= word.length(); i++)
		{
			if (word[i] == ' ')
			{
				count++;
				break;
			}

			alpha = (int)word[i] - 'a';

			if (!check[alpha])
				check[alpha] = true;
			else
			{
				if (word[i - 1] != word[i])
					break;
			}
		}

		clear();
	}

	cout << count << endl;
}

void clear()
{
	for (int i = 0; i < 26; i++)
		check[i] = false;
}