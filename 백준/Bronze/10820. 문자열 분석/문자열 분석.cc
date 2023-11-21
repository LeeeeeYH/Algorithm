#include <iostream>
#include <string>
using namespace std;

int main()
{
	while (1)
	{
		string sen;
		getline(cin, sen);
		if (sen.size() == 0)
			break;

		int small = 0, big = 0, num = 0, nul = 0;

		for (int i = 0; i < sen.length(); i++)
		{
			char a = sen[i];
			if (a >= 'a'&&a <= 'z')
				small++;
			else if (a >= 'A'&&a <= 'Z')
				big++;
			else if (a >= '0'&&a <= '9')
				num++;
			else if (a == ' ')
				nul++;
		}
		cout << small << " " << big << " " << num << " " << nul << endl;
	}
}