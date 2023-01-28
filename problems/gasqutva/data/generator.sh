#!/usr/bin/env bash

. ../../../testdata_tools/gen.sh

use_solution gustav.cpp

compile gen.py

samplegroup
limits nMax=20
sample 1

group group1 60
limits nMax=100
tc 1
tc g1_01 gen N=2 type=rnd
tc g1_02 gen N=3 type=rnd
tc g1_03 gen N=4 type=rnd
tc g1_04 gen N=5 type=rnd
tc g1_05 gen N=6 type=rnd
tc g1_06 gen N=100 type=rnd
tc g1_07 gen N=100 type=rnd
tc g1_08 gen N=100 type=star
tc g1_09 gen N=100 type=starline

group group2 40
limits nMax=100000
include_group group1
tc g2_01 gen N=10000 type=rnd
tc g2_02 gen N=100000 type=rnd
tc g2_03 gen N=100000 type=rnd
tc g2_04 gen N=100000 type=line
tc g2_05 gen N=100000 type=line
tc g2_06 gen N=100000 type=star
tc g2_07 gen N=100000 type=star
tc g2_08 gen N=100000 type=starline
tc g2_09 gen N=100000 type=starline
