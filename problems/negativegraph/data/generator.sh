#!/usr/bin/env bash
USE_SCORING=0
. ../../../testdata_tools/gen.sh

use_solution loke_reduced_bellman_ford.py

compile gen.py
compile chain.py

sample 1

tc_manual ../manual_tests/m1.in
tc_manual ../manual_tests/m2.in
tc_manual ../manual_tests/m3.in
tc_manual ../manual_tests/m4.in
tc t01 gen nmax=100 kind=complete completefrac=0.2
tc t02 gen nmax=100 kind=complete completefrac=0.2
tc t03 gen nmax=100 kind=complete completefrac=0.2
tc t04 gen nmax=100 kind=complete completefrac=0.5
tc t05 gen nmax=100 kind=complete completefrac=0.5
tc t06 gen nmax=100 kind=complete completefrac=0.5
tc t07 gen nmax=100 kind=complete completefrac=0.9
tc t08 gen nmax=100 kind=complete completefrac=0.9
tc t09 gen nmax=100 kind=complete completefrac=0.9
tc t10 gen nmax=100 kind=oneline extraedgemax=1
tc t11 gen nmax=100 kind=oneline extraedgemax=2
tc t12 gen nmax=100 kind=oneline extraedgemax=10
tc t13 gen nmax=100 kind=oneline extraedgemax=10
tc t14 gen nmax=100 kind=oneline extraedgemax=10
tc t15 gen nmax=100 kind=oneline extraedgemax=100
tc t16 gen nmax=100 kind=oneline extraedgemax=100
tc t17 gen nmax=100 kind=oneline extraedgemax=1000
tc t18 gen nmax=100 kind=oneline extraedgemax=1000
tc t19 gen nmax=100 kind=oneline
tc t20 gen nmax=100 kind=oneline
tc t21 gen nmax=100 kind=oneline
tc t22 gen nmax=100 kind=oneline
tc t23 gen nmax=100 kind=oneline
tc t24 gen nmax=100 kind=oneline
tc t25 gen nmax=100 kind=oneline
tc t26 gen nmax=100 kind=twoline extraedgemax=1
tc t27 gen nmax=100 kind=twoline extraedgemax=2
tc t28 gen nmax=100 kind=twoline extraedgemax=10
tc t29 gen nmax=100 kind=twoline extraedgemax=10
tc t30 gen nmax=100 kind=twoline extraedgemax=10
tc t31 gen nmax=100 kind=twoline extraedgemax=100
tc t32 gen nmax=100 kind=twoline extraedgemax=100
tc t33 gen nmax=100 kind=twoline extraedgemax=1000
tc t34 gen nmax=100 kind=twoline extraedgemax=1000
tc t35 gen nmax=100 kind=twoline
tc t36 gen nmax=100 kind=twoline
tc t37 gen nmax=100 kind=twoline
tc t38 gen nmax=100 kind=twoline
tc t39 gen nmax=100 kind=twoline
tc t40 gen nmax=100 kind=twoline
tc t41 gen nmax=100 kind=twoline
tc t42 gen kind=complete completefrac=0.1
tc t43 gen kind=complete completefrac=0.1
tc t44 gen kind=complete completefrac=0.1
tc t45 gen kind=complete completefrac=0.5
tc t46 gen kind=complete completefrac=0.5
tc t47 gen kind=complete completefrac=0.5
tc t48 gen kind=complete completefrac=0.9
tc t49 gen kind=complete completefrac=0.9
tc t50 gen kind=complete completefrac=0.9
tc t51 gen kind=oneline extraedgemax=1
tc t52 gen kind=oneline extraedgemax=2
tc t53 gen kind=oneline extraedgemax=10
tc t54 gen kind=oneline extraedgemax=10
tc t55 gen kind=oneline extraedgemax=10
tc t56 gen kind=oneline extraedgemax=100
tc t57 gen kind=oneline extraedgemax=100
tc t58 gen kind=oneline extraedgemax=1000
tc t59 gen kind=oneline extraedgemax=1000
tc t60 gen kind=oneline
tc t61 gen kind=oneline
tc t62 gen kind=oneline
tc t63 gen kind=oneline
tc t64 gen kind=oneline
tc t65 gen kind=oneline
tc t66 gen kind=oneline
tc t67 gen kind=twoline extraedgemax=1
tc t68 gen kind=twoline extraedgemax=2
tc t69 gen kind=twoline extraedgemax=10
tc t70 gen kind=twoline extraedgemax=10
tc t71 gen kind=twoline extraedgemax=10
tc t72 gen kind=twoline extraedgemax=100
tc t73 gen kind=twoline extraedgemax=100
tc t74 gen kind=twoline extraedgemax=1000
tc t75 gen kind=twoline extraedgemax=1000
tc t76 gen kind=twoline
tc t77 gen kind=twoline
tc t78 gen kind=twoline
tc t79 gen kind=twoline
tc t80 gen kind=twoline
tc t81 gen nmax=10 kind=twoline extraedgemax=1
tc t82 gen nmax=10 kind=twoline extraedgemax=2
tc t83 gen nmax=10 kind=twoline extraedgemax=3
tc t84 gen nmax=10 kind=twoline extraedgemax=4
tc t85 gen nmax=10 kind=twoline extraedgemax=10
tc t86 gen nmax=10 kind=twoline extraedgemax=20
tc t87 gen nmax=10 kind=twoline extraedgemax=40
tc t88 gen nmax=10 kind=twoline extraedgemax=80
tc c0 chain
tc c1 chain
tc c2 chain
tc c3 chain
tc c4 chain
tc c5 chain
