#include<bits/stdc++.h>
using namespace std;
int n, m;
long long w[105], v[105], f[105][100005];
int main(){
	ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
	cin >> n >> m;
	int sum = 0;
	for( int i = 1; i <= n; i++){
		cin >> w[i] >> v[i];
		sum += v[i];
	}
	memset(f, 60, sizeof(f));
	f[0][0] = 0;
	for( int i = 1; i <= n + 1; i++){
		for( int j = 0; j <= sum + 1; j++){
			if( v[i] <= j){
				f[i][j] =  min(f[i - 1][j - v[i]] + w[i], f[i - 1][j]);
			}
			else{
				f[i][j] = f[i - 1][j];
			}
		}
	}
	int ans = -2;
	for( int i = 0; i <= sum + 1; i++){
		if(f[n][i] <= m){
			ans = max(ans, i);
		}
	}
	cout << ans;
}
