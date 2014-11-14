import GCD

class GF:
    def __init__(s, prime):
        s.e.p = prime

    def __str__(s):
        return "GF(%s)" % str(s.e.p)

    class e:
        def __init__(s, v):
            s.v = v.v if isinstance(v, GF.e) else v % s.p

        def __eq__(s, a):
            assert isinstance(a, GF.e)
            return s.v == a.v

        def __ne__(s, a):
            assert isinstance(a, GF.e)
            return s.v == a.v

        def __add__(s, a):
            assert isinstance(a, GF.e)
            return GF.e(s.v + a.v)

        def __neg__(s):
            return GF.e(-s.v)

        def __sub__(s, a):
            assert isinstance(a, GF.e)
            return GF.e(s.v - a.v)

        def __mul__(s, a):
            assert isinstance(a, GF.e)
            return GF.e(s.v * a.v)

        def __invert__(s):
            x, _ = GCD.extEuclid(s.v, s.p)
            return GF.e(x)

        def __div__(s, a):
            assert isinstance(a, GF.e)
            return s * ~a

        def __pow__(s, a):
            return GF.e(pow(s.v, a, s.p))

        def __str__(s):
            return str(s.v)

        def __repr__(s):
            return repr(s.v)

def main():
    GF5 = GF(5)
    print GF5
    print GF5.e(3) + GF5.e(2)
    print GF5.e(3) - GF5.e(2)
    print GF5.e(3) * GF5.e(2)
    print ~GF5.e(2)
    print GF5.e(3) / GF5.e(2)
    print GF5.e(3) ** 3

if __name__ == '__main__':
    main()
