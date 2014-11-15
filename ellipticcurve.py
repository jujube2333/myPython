import galoisfield as gf

class EC:
    # y^2 = x^3 + ax + b
    def __init__(self, a, b, p):
        assert 4 * a ** 3 + 27 * b ** 2 != 0
        self.elem.a = gf.GF(p).elem(a)
        self.elem.b = gf.GF(p).elem(b)
        self.elem.p = p
        self.elem.ZERO = (gf.GF(p).elem(0), gf.GF(p).elem(0))

    class elem:
        def __init__(self, v):
            assert self.__isValid(v)
            x, y = v
            self.v = (gf.GF.elem(x), gf.GF.elem(y))

        def __isValid(self, a):
            assert isinstance(a, tuple)
            x, y = a
            if isinstance(x, gf.GF.elem) or isinstance(y, gf.GF.elem):
                if a == self.ZERO:
                    return True
            else:
                if a == (0, 0):
                    return True
            left = gf.GF(self.p).elem(y) ** 2
            right = gf.GF(self.p).elem(x) ** 3 + self.a * gf.GF(self.p).elem(x) + self.b
            return left == right

        def __eq__(self, a):
            assert isinstance(a, EC.elem)
            return self.v == a.v

        def __ne__(self, a):
            assert isinstance(a, EC.elem)
            return s.v != a.v

        def __add__(self, a):
            assert isinstance(a, EC.elem)
            if self.v == self.ZERO:
                return a.v
            if a.v == self.ZERO:
                return self.v
            x0, y0 = self.v
            x1, y1 = a.v
            if x0 == x1:
                if y0 == -y1:
                    return self.ZERO
                m = (gf.GF(self.p).elem(3) * x0 ** 2 + self.a) / (gf.GF(self.p).elem(2) * y0)
            else:
                m = (y0 - y1) / (x0 - x1)
            x = m ** 2 - x0 - x1
            y = m * (x0 - x) - y0
            return EC.elem((x, y))

        def __mul__(self, a):
            if a == 0:
                return self.ZERO
            bit = map(int, bin(a).replace('0b', '')[1:])
            x = self
            for b in bit:
                x += x
                if b == 1:
                    x += self
            return x

        def __str__(self):
            return str(self.v)

        def __repr__(self):
            return repr(self.v)

class ECC(EC):
    def __init__(self, a, b, p):
        EC.__init__(self, a, b, p)

    def encrypt(self, e, M):
        return (EC.elem(M) * e).v

    def decrypt(self, d, C):
        return (EC.elem(C) * d).v

def main():
    ec = EC(3, 4, 7)
    print ec.elem((0, 2)) == ec.elem((0, 2))
    print ec.elem((1, 1)) + ec.elem((5, 2))
    print ec.elem((5, 5)) + ec.elem((5, 5))
    for i in range(8):
        print i, ec.elem((0, 2)) * i
    ecc = ECC(3, 4, 7)
    print ecc.encrypt(2, (1, 1))
    print ecc.decrypt(3, (0, 2))

if __name__ == '__main__':
    main()
