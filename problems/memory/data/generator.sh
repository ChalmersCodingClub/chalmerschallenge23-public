#!/usr/bin/env bash
. ../../../testdata_tools/gen.sh

use_solution gustav.cpp

compile gen.py

samplegroup
sample 1
sample 2

group full 100
tc 1
tc 2
tc t01 gen N=10 K=11
tc t02 gen N=10 K=1
tc t03 gen N=10 K=0
tc t04 gen N=10 K=16
tc t05 gen N=10 K=18
tc t06 gen N=10 K=19
tc t07 gen N=10 K=20
tc t08 gen N=1 K=0
tc t09 gen N=1 K=1
tc t10 gen N=1 K=2
tc t11 gen N=2 K=0
tc t12 gen N=2 K=1
tc t13 gen N=2 K=2
tc t14 gen N=2 K=3
tc t15 gen N=2 K=4
tc t16 gen N=100000 K=0
tc t17 gen N=100000 K=100
tc t18 gen N=100000 K=1000
tc t19 gen N=100000 K=100000
tc t20 gen N=100000 K=199000
tc t21 gen N=100000 K=199998
tc t22 gen N=100000 K=199999
tc t23 gen N=100000 K=200000
