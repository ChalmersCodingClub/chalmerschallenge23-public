#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<pi> vpi;
typedef vector<vi> vvi;
const int inf = 0x3f3f3f3f;
const ll linf = 1234567890123456789;
const ll mod = 1000000007;
#define all(x) x.begin(), x.end()
#define debug(x) cerr << #x << " = " << (x) << endl
#define sz(x) ((int)(x).size())
#define rep(i, a, b) for(int i = (a); i < int(b); i++)
#define trav(x, a) for(auto& x : a)

int n, k;
int a1, a2;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
	cin >> n >> k;
    cin >> a1 >> a2;
    vvi h(n, vi(k));
    map<int, set<int>> hs;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < k; j++){
            cin >> h[i][j];
            hs[h[i][j]].insert(i);
        }
    }

    auto lo = hs.begin(), hi = hs.begin();
    int ans = inf;
    int c[4] = {n,0,0,0};
    while(1){
        if(c[0]==0 && c[1]<=a1 && c[2]<=a2){
            hi--;
            ans = min(ans, hi->first-lo->first);
            for(int p : lo->second){
                c[(h[p][0]>=lo->first && h[p][0]<=hi->first) | ((h[p][1]>=lo->first && h[p][1]<=hi->first)<<1)]--;
                c[(h[p][0]>lo->first && h[p][0]<=hi->first) | ((h[p][1]>lo->first && h[p][1]<=hi->first)<<1)]++;
            }
            hi++;
            lo++;
        }
        else{
            if(hi == hs.end()) break;
            for(int p : hi->second){
                c[(h[p][0]>=lo->first && h[p][0]<hi->first) | ((h[p][1]>=lo->first && h[p][1]<hi->first)<<1)]--;
                c[(h[p][0]>=lo->first && h[p][0]<=hi->first) | ((h[p][1]>=lo->first && h[p][1]<=hi->first)<<1)]++;
            }
            hi++;
        }
    }
    cout << ans << "\n";
}
