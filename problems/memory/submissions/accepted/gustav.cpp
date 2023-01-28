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


int main(){
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    int n, k;
    cin >> n >> k;
    vi a(k);
    for(int i = 0; i < k; i++) cin >> a[i];
    sort(all(a));
    int ans = 0;
    for(int i = 0; i < k-1; i++){
        if(a[i] == a[i+1]){
            ans++;
            i++;
        }
    }
    if(ans == n-1) ans++;
    cout << ans << "\n";
}
