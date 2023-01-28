#include "validator.h"
#include <bits/stdc++.h>
using namespace std;

void run() {
    int nMax = Arg("nMax");
    int kMax = Arg("kMax");

    int N = Int(2, nMax);
    Space();
    int K = Int(2, min(kMax, N));
    Endl();
    long long sum = 0;
    for(int i = 0; i < K; i++){
        int a = Int(1, nMax);
        sum += a;
        if(i != K-1) Space();
    }
    if(sum != N) die("wrong sum");
    Endl();
    for(int i = 0; i < N; i++){
        for(int j = 0; j < K; j++){
            Int(1, 1000000000);
            if(j != K-1) Space();
        }
        Endl();
    }
    Eof();
}
