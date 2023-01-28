#include "validator.h"
#include <cmath>

#define sz(v) int(v.size())

void run() {
	int n = Int(2, 100000);
	Space();
	int m = Int(2, 100000);
	Space();
	int k = Int(0, 50);
	Space();
	int a = Int(0, n - 1);
	Space();
	int b = Int(0, n - 1);
	Endl();
	int cnt = 0;
	for (int i = 0; i < m; ++i) {
		Int(0, n - 1);
		Space();
		Int(0, n - 1);
		Space();
		int x = Int(-1000000000, 1000000000);
		if(x<0) cnt++;
		Endl();
	}
	if(cnt != k) die("wrong number of negative edges");
	Eof();
}
