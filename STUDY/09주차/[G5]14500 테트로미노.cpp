#include<iostream>
using namespace std;
int n, m;
int ans;
int a[501][501];
int max(int a, int b){
	return a > b ? a : b;
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			cin >> a[i][j];

	for (int i = 1; i <= n; i++){
		for (int j = 1; j <= m; j++){
			if (j + 3 <= m)
				ans = max(ans, a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i][j + 3]);
			if (i + 3 <= n)
				ans = max(ans, a[i][j] + a[i + 1][j] + a[i + 2][j] + a[i + 3][j]);
			if (i + 1 <= n && j + 1 <= m)
				ans = max(ans, a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1]);
			if (i + 2 <= n && j + 1 <= m){
				ans = max(ans, a[i][j] + a[i + 1][j] + a[i + 2][j] + max(a[i][j + 1], max(a[i + 1][j + 1], a[i + 2][j + 1])));
				ans = max(ans, a[i][j + 1] + a[i + 1][j + 1] + a[i + 2][j + 1] + max(a[i][j], max(a[i + 1][j], a[i + 2][j])));
				ans = max(ans, a[i][j] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j + 1]);
				ans = max(ans, a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1] + a[i + 2][j]);
			}
			if (i + 1 <= n && j + 2 <= m){
				ans = max(ans, a[i][j] + a[i][j + 1] + a[i][j + 2] + max(a[i + 1][j], max(a[i + 1][j + 1], a[i + 1][j + 2])));
				ans = max(ans, a[i + 1][j] + a[i + 1][j + 1] + a[i + 1][j + 2] + max(a[i][j], max(a[i][j + 1], a[i][j + 2])));
				ans = max(ans, a[i][j + 1] + a[i][j + 2] + a[i + 1][j] + a[i + 1][j + 1]);
				ans = max(ans, a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 1][j + 2]);
			}
		}
	}
	cout << ans;
}