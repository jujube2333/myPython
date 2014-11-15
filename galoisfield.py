import gcd

class GF:
    def __init__(self, p):
        self.elem.p = p

    def __str__(self):
        return "GF(%s)" % str(self.elem.p)

    class elem:
        def __init__(self, v):
            self.v = v.v if isinstance(v, GF.elem) else v % self.p

        def __eq__(self, a):
            assert isinstance(a, GF.elem)
            return self.v == a.v

        def __ne__(self, a):
            assert isinstance(a, GF.elem)
            return self.v == a.v

        def __add__(self, a):
            assert isinstance(a, GF.elem)
            return GF.elem(self.v + a.v)

        def __neg__(self):
            return GF.elem(-self.v)

        def __sub__(self, a):
            assert isinstance(a, GF.elem)
            return GF.elem(self.v - a.v)

        def __mul__(self, a):
            assert isinstance(a, GF.elem)
            return GF.elem(self.v * a.v)

        def __invert__(self):
            x, _ = gcd.extEuclid(self.v, self.p)
            return GF.elem(x)

        def __div__(self, a):
            assert isinstance(a, GF.elem)
            return self * ~a

        def __pow__(self, a):
            return GF.elem(pow(self.v, a, self.p))

        def __str__(self):
            return str(self.v)

        def __repr__(self):
            return repr(self.v)

def main():
    GF5 = GF(5)
    print GF5
    print GF5.elem(3) + GF5.elem(2)
    print GF5.elem(3) - GF5.elem(2)
    print GF5.elem(3) * GF5.elem(2)
    print ~GF5.elem(2)
    print GF5.elem(3) / GF5.elem(2)
    print GF5.elem(3) ** 3

if __name__ == '__main__':
    main()
