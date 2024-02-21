#include <iostream>
#include <algorithm>
using namespace std;

int N;
int ls[50];
int summ;
int dp[50][884][884];

int recur(int cur, int a, int b) {
    if (a > 883 || b > 883) return -2501;
    if (cur == N) {
        int c = summ - a - b;
        if (c <= a && c <= b) return c;
        return -2501;
    }

    if (dp[cur][a][b] == -1) {
        dp[cur][a][b] = max(recur(cur + 1, a + ls[cur], b),
                             max(recur(cur + 1, a, b + ls[cur]),
                             recur(cur + 1, a, b)));
    }
    return dp[cur][a][b];
}

int main() {
    cin >> N;
    for (int i = 0; i < N; ++i)
        cin >> ls[i];

    summ = 0;
    for (int i = 0; i < N; ++i)
        summ += ls[i];

    for (int i = 0; i < 50; ++i)
        for (int j = 0; j < 884; ++j)
            for (int k = 0; k < 884; ++k)
                dp[i][j][k] = -1;
    
    cout << recur(0, 0, 0);
    return 0;
}