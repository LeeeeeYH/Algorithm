#include <iostream>
#include <algorithm>
using namespace std;

int dp[100004];

int main() {
	int N; cin >> N;
	dp[0] = 0, dp[1] = 1;
	for (int i = 2; i <= N; i++) {
		dp[i] = dp[i - 1] + 1;
		for (int j = 2; i - j * j >= 0; j++)
			dp[i] = min(dp[i], dp[i - j * j] + 1);
	}
	cout << dp[N];
}