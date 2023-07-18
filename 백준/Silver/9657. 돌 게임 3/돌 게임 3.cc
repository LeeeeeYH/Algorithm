#include <iostream>
using namespace std;

bool dp[1004]; //SK이면 true, CY이면 false

int main() {
	int N; cin >> N;
	dp[1] = dp[3] = dp[4] = true;
	for (int i = 5; i <= N; i++) {
		if (dp[i - 1] && dp[i - 3] && dp[i - 4])
			dp[i] = false;
		else dp[i] = true;
	}

	if (dp[N]) cout << "SK";
	else cout << "CY";
}