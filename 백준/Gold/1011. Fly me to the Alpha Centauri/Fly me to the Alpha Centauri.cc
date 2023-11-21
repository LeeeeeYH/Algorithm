//#include <iostream>
//using namespace std;
//
//int main()
//{
//	int T, x, y, rise, count;
//	cin >> T;
//	for (int a = 0; a < T; a++)
//	{
//		rise = 1;
//		count = 1;
//		cin >> x >> y;
//		int d = y - x;
//		for (double i = 1.5; rise < d; i += (double)1 / 2)
//		{
//			rise += (int)i;
//			count++;
//		}
//		cout << count << endl;
//	}
//}

//#include <iostream>
//using namespace std;
//
//int main()
//{
//	int T, x, y, rise, count;
//	cin >> T;
//	for (int a = 1; a <= T; a++)
//	{
//		rise = 1;
//		count = 1;
//		int d = a;
//		for (double i = 1.5; rise < d; i += (double)1 / 2)
//		{
//			rise += (int)i;
//			count++;
//		}
//		cout << count << endl;
//	}
//}

#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int a = 0; a < T; a++)
	{
		long double x, y, d;
		cin >> x >> y;
		d = y - x;
		long double i = 1;
		while (1)
		{
			if (i*i > d)
				break;
			i++;
		}
		if ((i - 1)*(i - 1) == d)
			cout << 2 * i - 3 << endl;
		else if ((i*i + (i - 1)*(i - 1)) / 2 >= d)
			cout << 2 * (i - 1) << endl;
		else
			cout << 2*(i-1)+1<<endl;
	}
}