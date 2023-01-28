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
#define debug(x) cerr << (#x) << " = " << (x) << endl
#define sz(x) ((int)(x).size())
#define rep(i, a, b) for(int i = a; i < (b); ++i)

struct edge{
    ll to;
    ll nm;
    ll sm;
};

int n;
vl a;
vector<vector<edge>> adj;
ll totsum;

pair<ll, ll> dfs(int u, int p){
    ll csm = a[u], cnm = 1;
    for(edge& e : adj[u]){
        if(e.to != p){
            tie(e.sm, e.nm) = dfs(e.to, u);
            csm += e.sm;
            cnm += e.nm;
        }
    }
    for(edge& e : adj[u]){
        if(e.to == p){
            e.sm = totsum - csm;
            e.nm = n - cnm;
        }
    }
    return {csm, cnm};
}

ll dfs2(int u, int p, ll pr){
    ll r = pr+a[u];
    for(edge& e : adj[u]){
        if(e.to == p) continue;
        r += dfs2(e.to, u, pr+a[u]);
    }
    return r;
}

ll best = -1;
ll beststart = -1;

void dfs3(int u, int p, ll sc){
    if(sc > best || (sc == best && u < beststart)){
        beststart = u;
        best = sc;
    }
    for(edge& e : adj[u]){
        if(e.to == p) continue;
        dfs3(e.to, u, sc-a[e.to]*e.nm+a[u]*(n-e.nm));
    }
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    cin >> n;
    a = vl(n);
    for(int i = 0; i < n; i++) cin >> a[i];
    totsum = accumulate(all(a), 0ll);
    adj.resize(n);
    for(int i = 0; i < n-1; i++){
        int u, v;
        cin >> u >> v;
        u--,v--;
        adj[u].push_back(edge{v, 0, 0});
        adj[v].push_back(edge{u, 0, 0});
    }

    dfs(0, -1);

    ll sc = dfs2(0, -1, 100-a[0]);
    dfs3(0, -1, sc);
    cout << beststart + 1 << endl;
}
