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

// KACTL Hopcroft Karp

bool dfs(int a, int L, vector<vi>& g, vi& btoa, vi& A, vi& B) {
	if (A[a] != L) return 0;
	A[a] = -1;
	for (int b : g[a]) if (B[b] == L + 1) {
		B[b] = 0;
		if (btoa[b] == -1 || dfs(btoa[b], L + 1, g, btoa, A, B))
			return btoa[b] = a, 1;
	}
	return 0;
}

int hopcroftKarp(vector<vi>& g, vi& btoa) {
	int res = 0;
	vi A(g.size()), B(btoa.size()), cur, next;
	for (;;) {
		fill(all(A), 0);
		fill(all(B), 0);
		/// Find the starting nodes for BFS (i.e. layer 0).
		cur.clear();
		for (int a : btoa) if(a != -1) A[a] = -1;
		rep(a,0,sz(g)) if(A[a] == 0) cur.push_back(a);
		/// Find all layers using bfs.
		for (int lay = 1;; lay++) {
			bool islast = 0;
			next.clear();
			for (int a : cur) for (int b : g[a]) {
				if (btoa[b] == -1) {
					B[b] = lay;
					islast = 1;
				}
				else if (btoa[b] != a && !B[b]) {
					B[b] = lay;
					next.push_back(btoa[b]);
				}
			}
			if (islast) break;
			if (next.empty()) return res;
			for (int a : next) A[a] = lay;
			cur.swap(next);
		}
		/// Use DFS to scan for augmenting paths.
		rep(a,0,sz(g))
			res += dfs(a, 0, g, btoa, A, B);
	}
}


int n, k;
vi a;
vvi h;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
	cin >> n >> k;
    a = vi(k);
    vi ind(k+1);
    for(int i = 0; i < k; i++){
        cin >> a[i];
        ind[i+1] = ind[i]+a[i];
    }
    h = vvi(n, vi(k));
    vi hs;
    map<int, set<pi>> hset;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < k; j++){
            cin >> h[i][j];
            if(!hset.count(h[i][j])){
                hs.push_back(h[i][j]);
            }
            hset[h[i][j]].insert({i,j});
        }
    }
    sort(all(hs));

    int ans = inf;
    int lo = 0, hi = 0;
    vvi g(n);
    while(1){
        vi btoa(n, -1);
        if(hopcroftKarp(g, btoa) == n){
            ans = min(ans, hs[hi-1]-hs[lo]);

            for(pi x : hset[hs[lo]]){
                for(int i = ind[x.second]; i < ind[x.second+1]; i++)
                    g[x.first].erase(find(all(g[x.first]), i));
            }

            lo++;
            if(lo == sz(hs)) break;
        }
        else{
            if(hi == sz(hs)) break;
            for(pi x : hset[hs[hi]]){
                for(int i = ind[x.second]; i < ind[x.second+1]; i++)
                    g[x.first].push_back(i);
            }
            hi++;
        }
    }

    cout << ans << endl;
}
