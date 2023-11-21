#include <iostream>
using namespace std;

#define mod 1000000009
long long dp[100004][4];

int main() {
	int T, n; cin >> T;

	dp[1][1] = 1, dp[2][2] = 1;
	dp[3][1] = 1, dp[3][2] = 1, dp[3][3] = 1;
	for (int i = 4; i <= 100000; i++) {
		dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % mod;
		dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % mod;
		dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % mod;
	}

	for (int a = 0; a < T; a++) {
		cin >> n;
		cout << (dp[n][1] + dp[n][2] + dp[n][3]) % mod << "\n";
	}
}