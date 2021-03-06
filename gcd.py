#! /usr/bin/env python

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# ax + by = 1
def extEuclid(a, b):
    if b == 0:
        x = 1
        y = 0
    else:
        q = a / b
        x0, y0 = extEuclid(b, a % b)
        x = y0
        y = x0 - q * y0
    return x, y

# a = x mod m, b = x mod n
def tnReminder(m, n, a, b):
    v, w = extEuclid(m, n)
    x = m * v * b + n * w * a
    return x % (m * n)
