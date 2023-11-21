#include <iostream>
#include <vector>
using namespace std;

#define mod 1000
typedef long long ll;
typedef vector<vector<ll>> mat;

mat operator*(mat &a, mat &b) {
	ll size = a.size();
	mat res(size, vector<ll>(size));
	for (ll i = 0; i < size; i++) {
		for (ll j = 0; j < size; j++) {
			for (ll k = 0; k < size; k++)
				res[i][j] += a[i][k] * b[k][j];
			res[i][j] %= mod;
		}
	}
	return res;
}

mat pow(mat a, ll n) {
	ll size = a.size();
	mat res(size, vector<ll>(size));
	for (ll i = 0; i < size; i++)
		res[i][i] = 1;		//단위행렬

	while (n > 0) {
		if (n % 2 == 1) res = res * a;
		n /= 2;
		a = a * a;
	}
	return res;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	ll N, B; cin >> N >> B;
	mat A(N, vector<ll>(N));
	mat res(N, vector<ll>(N));
	for (ll i = 0; i < N; i++)
		for (ll j = 0; j < N; j++)
			cin >> A[i][j];

	res = pow(A, B);
	for (ll i = 0; i < N; i++) {
		for (ll j = 0; j < N; j++)
			cout << res[i][j] << " ";
		cout << "\n";
	}
}