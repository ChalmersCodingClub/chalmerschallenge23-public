#!/usr/bin/env bash
USE_SCORING=0
. ../../../testdata_tools/gen.sh

use_solution loke.py

compile gen.py

sample 1

tc_manual ../manual_tests/m1.in
tc t01 gen
tc t02 gen
tc t03 gen
tc t04 gen
tc t05 gen
tc t06 gen
tc t07 gen
tc t08 gen
tc t09 gen
tc t10 gen
tc t11 gen
tc t12 gen
tc t13 gen
tc t14 gen
tc t15 gen
tc t16 gen
tc t17 gen
tc t18 gen
tc t19 gen
tc t20 gen
tc t21 gen
tc t22 gen
tc t23 gen
tc t24 gen
tc t25 gen
tc t26 gen
tc t27 gen
tc t28 gen
tc t29 gen
tc t30 gen
tc t31 gen
tc t32 gen
tc t33 gen
tc t34 gen
tc t35 gen
tc t36 gen
tc t37 gen
tc t38 gen
tc t39 gen
tc t40 gen
tc t41 gen
tc t42 gen
tc t43 gen
tc t44 gen
tc t45 gen
tc t46 gen
tc t47 gen
tc t48 gen
tc t49 gen
tc t50 gen
