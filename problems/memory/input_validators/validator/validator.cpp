#include "validator.h"

#include <cstring>
#include <string>

void run() {
	int n = Int(1, 100000);
	Space();
	int k = Int(0, 2 * n);
	Endl();
	int cards[200001];
	memset(cards, 0, sizeof(cards));
	for (int i = 0; i < k; ++i) {
		int c = Int(1, n);
		cards[c]++;
		if (cards[c] > 2) die("Too many of card " + to_string(c));
		if (i < k - 1) Space();
	}
	Endl();
	Eof();
}
