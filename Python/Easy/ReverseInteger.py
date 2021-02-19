"""
https://leetcode.com/problems/reverse-integer/
"""

x = -123


if str(x).startswith("-"):
    x = x[1:]
    print("-{0}".format(int(str(x)[::-1])))
else:
    print(int(str(x)[::-1]))