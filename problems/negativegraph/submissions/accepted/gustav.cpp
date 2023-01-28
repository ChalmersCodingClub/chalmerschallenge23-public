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

int n, m, k;
int from, to;
vector<map<int, ll>> adj, adj2;
set<int> interesting;

void dijkstra(int start){
    priority_queue<pair<ll,int>> pq;
    pq.emplace(0, start);
    vi visited(n);
    while(sz(pq)){
        ll d;
        int u;
        tie(d, u) = pq.top();
        pq.pop();
        if(visited[u]) continue;
        visited[u] = 1;
        if(interesting.count(u)){
            if(!adj2[start].count(u)) adj2[start][u] = -d;
        }
        for(auto x : adj[u]){
            if(x.second < 0) continue;
            pq.emplace(d-x.second, x.first);
        }
    }
}

int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    cin >> n >> m >> k;
    cin >> from >> to;
    adj.resize(n);
    adj2.resize(n);
    for(int i = 0; i < m; i++){
        int u, v, c;
        cin >> u >> v >> c;
        if(adj[u].count(v)) adj[u][v] = min(adj[u][v], (ll)c);
        else adj[u][v] = c;
        if(c<0){
            interesting.insert(u);
            interesting.insert(v);
            adj2[u][v] = adj[u][v];
        }
    }
    interesting.insert(from);
    interesting.insert(to);

    for(auto p : interesting){
        dijkstra(p);
    }

    map<int, ll> dist;
    dist[from] = 0;
    for(int i = 0; i < 4*sz(interesting)+1; i++){
        int upd = 0;
        for(int j : interesting){
            if(!dist.count(j)) continue;
            for(auto x : adj2[j]){
                if(dist.count(x.first)){
                    if(dist[j]+x.second < dist[x.first]){
                        dist[x.first] = dist[j]+x.second;
                        if(x.first==to) upd = 1;
                    }
                }
                else{
                    dist[x.first] = dist[j]+x.second;
                    if(x.first==to) upd = 1;
                }
            }
        }
        if(i == 4*sz(interesting) && upd && dist.count(to)){
            cout << "NEGATIVE INFINITY" << endl;
            return 0;
        }
    }
    if(!dist.count(to)){
        cout << "POSITIVE INFINITY" << endl;
    }
    else
        cout << dist[to] << endl;
}
