#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2")

// competitive stuff
#pragma region
#include <bits/extc++.h>
#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define fastmap __gnu_pbds::gp_hash_table
#define endl '\n'

const int m = 1e9 + 7;

struct chash {  // large odd number for C
    const uint64_t C = ll(4e18 * acos(0)) | 71;
    ll operator()(ll x) const { return x * C; }
};

template <class T>
void printit(T& v) {
    for (auto& e : v) cerr << e << " ";
    cerr << endl;
}

#pragma endregion

vector<ull> sums;
fastmap<int, vector<int>, chash> graph;
vector<bool> v;
ull susdfs(int node, ull amount) {
    if (v[node]) return 0;
    v[node] = 1;
    ull s = 0;
    for (auto& i : graph[node]) s += susdfs(i, sums[i] + amount);

    return amount + s;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin.exceptions(cin.failbit);

    int N;
    cin >> N;
    sums = vector<ull>(N);
    for (int i = 0; i < N; ++i) {
        cin >> sums[i];
    }
    for (int i = 0; i < N - 1; ++i) {
        int j, k;
        cin >> j >> k;
        j--; k--;
        graph[j].push_back(k);
        graph[k].push_back(j);
    }

    ull best = 0;
    int student = -1;
    for (int i = 0; i < N; ++i) {
        v = vector<bool>(N, 0);
        ull a = susdfs(i, 100);
        if (best < a) {
            best = a;
            student = i;
        }
    }
    cout << student + 1 << endl;

    return 0;
}