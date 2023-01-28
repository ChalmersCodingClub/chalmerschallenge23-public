#!/usr/bin/env python3

longest = 0
pub = ""
for _ in range(int(input())):
    p, k, t = input().split()
    if (int(k)+1) * int(t) >= longest:
        longest = (int(k)+1) * int(t)
        pub = p
print(pub, longest)
