#!/usr/bin/env bash

. ../../../testdata_tools/gen.sh

use_solution gustav.cpp

compile gen.py

samplegroup
limits nMax=10 kMax=10
sample 1

group group1 50
limits nMax=75 kMax=2
tc 1
tc g1_1 gen n=5 k=2 hMax=10
tc g1_2 gen n=75 k=2 hMax=10
tc g1_3 gen n=75 k=2 hMax=1000000
tc g1_4 gen n=75 k=2 hMax=1000000000
tc g1_5 gen n=75 k=2 hMax=1000000000
tc g1_6 gen n=75 k=2 hMax=1000000000
tc g1_7 gen n=10 k=2 hMax=1000000000
tc g1_8 gen n=2 k=2 hMax=1000000000

group group2 50
limits nMax=75 kMax=75
include_group group1
tc g2_1 gen n=5 k=3 hMax=1
tc g2_2 gen n=5 k=3 hMax=1000000000
tc g2_3 gen n=75 k=3 hMax=1000000000
tc g2_4 gen n=5 k=5 hMax=1000000000
tc g2_5 gen n=75 k=75 hMax=1000000000
tc g2_6 gen n=75 k=75 hMax=1000000000
tc g2_7 gen n=75 k=75 hMax=1000000000
tc g2_8 gen n=75 k=75 hMax=1
tc g2_9 gen n=75 k=20 hMax=1000000000
tc g2_10 gen n=75 k=20 hMax=1000000000
tc g2_11 gen n=75 k=20 hMax=1
tc g2_12 gen n=75 k=68 hMax=1000000000
tc g2_13 gen n=75 k=70 hMax=1
tc g2_14 gen n=75 k=73 hMax=1000000000
tc g2_15 gen n=75 k=74 hMax=1000000000
tc g2_16 gen n=75 k=26 hMax=10
tc g2_17 gen n=75 k=67 hMax=100
tc g2_18 gen n=5 k=3 hMax=10
tc g2_19 gen n=75 k=30 hMax=10
tc g2_20 gen n=75 k=68 hMax=100
