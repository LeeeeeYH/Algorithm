#include <iostream>
#include <algorithm>
using namespace std;

int tri[504][504];
int dp[504][504];

int main()
{
	int n; cin >> n;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= i; j++)
			cin >> tri[i][j];
	

	dp[1][1] = tri[1][1];
	for (int i = 2; i <= n; i++) {
		dp[i][1] = dp[i-1][1] + tri[i][1];
		dp[i][i] = dp[i - 1][i - 1] + tri[i][i];
	}

	for (int i = 3; i <= n; i++)
		for (int j = 2; j < i; j++)
			dp[i][j] = max(dp[i - 1][j - 1] + tri[i][j], dp[i - 1][j] + tri[i][j]);

	int MAX = 0;
	for (int i = 1; i <= n; i++)
		MAX = max(MAX, dp[n][i]);
	cout << MAX;
}