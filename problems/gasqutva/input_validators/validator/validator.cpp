#include "validator.h"

struct UF {
	vector<int> e;
	UF(int n) : e(n, -1) {}
	bool sameSet(int a, int b) { return find(a) == find(b); }
	int size(int x) { return -e[find(x)]; }
	int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
	bool join(int a, int b) {
		a = find(a), b = find(b);
		if (a == b) return false;
		if (e[a] > e[b]) swap(a, b);
		e[a] += e[b]; e[b] = a;
		return true;
	}
};

void run() {
    int nMax = Arg("nMax");

    int n = Int(2, nMax);
    Endl();
    for (int i = 0; i < n; ++i) {
        Int(0, 1000000000);
        Endl();
    }
    UF uf(n);
    for (int i = 0; i < n - 1; ++i) {
        int a = Int(1, n);
        Space();
        int b = Int(1, n);
        Endl();
        uf.join(a-1, b-1);
    }
    if(uf.size(0) != n) die("not connected");
    Eof();
}
