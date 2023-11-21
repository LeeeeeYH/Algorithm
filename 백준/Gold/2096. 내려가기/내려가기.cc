//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//int map[100004][3];
//int dp1[100004][3]; //max
//int dp2[100004][3]; //min
//
//int main()
//{
//	int N; cin >> N;
//	for (int i = 1; i <= N; i++)
//		for (int j = 0; j < 3; j++)
//			cin >> map[i][j];
//
//	for (int i = 0; i < 3; i++) dp1[1][i] = dp2[1][i] = map[1][i];
//
//	for (int i = 2; i <= N; i++) {
//		dp1[i][0] = max(dp1[i - 1][0], dp1[i - 1][1]) + map[i][0];
//		dp1[i][1] = max({ dp1[i - 1][0], dp1[i - 1][1], dp1[i - 1][2] }) + map[i][1];
//		dp1[i][2] = max(dp1[i - 1][1], dp1[i - 1][2]) + map[i][2];
//
//		dp2[i][0] = min(dp2[i - 1][0], dp2[i - 1][1]) + map[i][0];
//		dp2[i][1] = min({ dp2[i - 1][0], dp2[i - 1][1], dp2[i - 1][2] }) + map[i][1];
//		dp2[i][2] = min(dp2[i - 1][1], dp2[i - 1][2]) + map[i][2];
//	}
//	cout << max({ dp1[N][0], dp1[N][1], dp1[N][2] }) << " " << min({ dp2[N][0], dp2[N][1], dp2[N][2] });
//}

#include <iostream>
#include <algorithm>
using namespace std;

int map[3];
int dp1[2][3]; //max
int dp2[2][3]; //min

int main()
{
	int N; cin >> N;
	int in;
	for (int i = 0; i < 3; i++) {
		cin >> in;
		dp1[0][i] = dp2[0][i] = in;
	}


	for (int i = 0; i < N - 1; i++)
		for (int j = 0; j < 3; j++) {
			cin >> map[j];

			if (i % 2 == 0) {
				dp1[1][0] = max(dp1[0][0], dp1[0][1]) + map[0];
				dp1[1][1] = max({ dp1[0][0], dp1[0][1], dp1[0][2] }) + map[1];
				dp1[1][2] = max(dp1[0][1], dp1[0][2]) + map[2];
				dp2[1][0] = min(dp2[0][0], dp2[0][1]) + map[0];
				dp2[1][1] = min({ dp2[0][0], dp2[0][1], dp2[0][2] }) + map[1];
				dp2[1][2] = min(dp2[0][1], dp2[0][2]) + map[2];
			}
			else {
				dp1[0][0] = max(dp1[1][0], dp1[1][1]) + map[0];
				dp1[0][1] = max({ dp1[1][0], dp1[1][1], dp1[1][2] }) + map[1];
				dp1[0][2] = max(dp1[1][1], dp1[1][2]) + map[2];
				dp2[0][0] = min(dp2[1][0], dp2[1][1]) + map[0];
				dp2[0][1] = min({ dp2[1][0], dp2[1][1], dp2[1][2] }) + map[1];
				dp2[0][2] = min(dp2[1][1], dp2[1][2]) + map[2];
			}
		}

	if(N%2==0)
		cout << max({ dp1[1][0], dp1[1][1], dp1[1][2] }) << " " << min({ dp2[1][0], dp2[1][1], dp2[1][2] });
	else
		cout << max({ dp1[0][0], dp1[0][1], dp1[0][2] }) << " " << min({ dp2[0][0], dp2[0][1], dp2[0][2] });
	
	
}