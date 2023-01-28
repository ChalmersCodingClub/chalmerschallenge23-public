#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pii;
typedef vector<ll> vi;
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define sz(x) (int)(x).size()

const ll MOD = 1e9 + 7;

vi gen_primes(ll limit) {
    vector<bool> isprime(limit, true);
    isprime[0] = false;
    isprime[1] = false;
    vi primes;
    for(ll p = 2; p < limit; p++) {
        if (!isprime[p]) {
            continue;
        }
        primes.push_back(p);
        for(ll r = p*p; r < limit; r += p) {
            isprime[r] = false;
        }
    }
    return primes;
}

ll powmod(ll b, ll e) {
    ll ret = 1;
    while (e > 0) {
        if (e & 1) {
            ret = (ret * b) % MOD;
        }
        e >>= 1;
        b = (b * b) % MOD;
    }
    return ret;
}

vi PRIMES;

ll highest(ll n) {
    ll ret = 1;
    while (n % 3 != 0) {
        ret = (ret * 2) % MOD;
        n -= 2;
    }
    ret = (ret * powmod(3, n/3)) % MOD;
    return ret;
}

ll lowest(ll N) {
    // DP[n] = (logsum, x%MOD)
    // of lowest solution s(x) = n
    // using the primes we have iterated through
    vector<long double> logsum(N+1, 1e9);
    vi xmod(N+1);
    // x=1, prime factor sum = 0, logsum=0
    logsum[0] = 0;
    xmod[0] = 1;
    trav(p, PRIMES) {
        rep(n, 0, N+1-p) {
            if (logsum[n] + log2(p) < logsum[n+p]) {
                logsum[n+p] = logsum[n] + log2(p);
                xmod[n+p] = (xmod[n] * p) % MOD;
            }
        }
    }
    return xmod[N];
}

int main() {
    cin.sync_with_stdio(0); cin.tie(0);
    cin.exceptions(cin.failbit);
    int N; cin >> N;
    assert(2 <= N);
    assert(N <= 50'000);
    assert(powmod(2, 0) == 1);
    assert(powmod(2, 1) == 2);
    assert(powmod(2, 2) == 4);
    assert(powmod(2, 3) == 8);
    PRIMES = gen_primes(N+1);
    cout << lowest(N) << " " << highest(N) << endl;
}
