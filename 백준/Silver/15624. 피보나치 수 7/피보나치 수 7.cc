#include <iostream>
using namespace std;

#define mod 1000000007
int dp[1000004];

int main() {
	int n; cin >> n;
	dp[0] = 0; dp[1] = 1;
	for (int i = 2; i <= n; i++)
		dp[i] = (dp[i - 2] + dp[i - 1]) % mod;

	cout << dp[n];
}