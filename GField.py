import GCD

class GF:
    def __init__(s, prime):
        s.v.p = prime

    def __str__(s):
        return "GF(%s)" % str(s.v.p)

    class v:
        def __init__(s, v):
            s.v = v.v if isinstance(v, GF(s.p).v) else v % s.p

        def __eq__(s, a):
            assert isinstance(a, GF(s.p).v)
            return s.v == a.v

        def __ne__(s, a):
            assert isinstance(a, GF(s.p).v)
            return s.v == a.v

        def __add__(s, a):
            assert isinstance(a, GF(s.p).v)
            return GF(s.p).v(s.v + a.v)

        def __sub__(s, a):
            assert isinstance(a, GF(s.p).v)
            return GF(s.p).v(s.v - a.v)

        def __mul__(s, a):
            assert isinstance(a, GF(s.p).v)
            return GF(s.p).v(s.v * a.v)

        def __invert__(s):
            x, _ = GCD.extEuclid(s.v, s.p)
            return GF(s.p).v(x)

        def __div__(s, a):
            assert isinstance(a, GF(s.p).v)
            return s * ~a

        def __pow__(s, a):
            return GF(s.p).v(pow(s.v, a, s.p))

        def __str__(s):
            return str(s.v)

        def __repr__(s):
            return "GF({0})#{1}".format(s.p, s.v)

def main():
    GF5 = GF(5)
    print GF5
    print GF5.v(3) + GF5.v(2)
    print GF5.v(3) - GF5.v(2)
    print GF5.v(3) * GF5.v(2)
    print ~GF5.v(2)
    print GF5.v(3) / GF5.v(2)
    print GF5.v(3) ** 3

if __name__ == '__main__':
    main()
