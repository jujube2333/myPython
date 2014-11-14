import GField as GF

class EC:
    # y^2 = x^3 + ax + b
    def __init__(s, a, b, p):
        assert 4 * a ** 3 + 27 * b ** 2 != 0
        s.e.GFp = GF.GF(p)
        s.e.a = s.e.GFp.e(a)
        s.e.b = s.e.GFp.e(b)
        s.e.z = (s.e.GFp.e(0), s.e.GFp.e(0))
        s.e.p = p

    class e:
        def __init__(s, v):
            assert s.__isValid(v)
            x, y = v
            s.v = (s.GFp.e(x), s.GFp.e(y))

        def __isValid(s, a):
            assert isinstance(a, tuple)
            x, y = a
            if isinstance(x, s.GFp.e) or isinstance(y, s.GFp.e):
                if a == s.z:
                    return True
            else:
                if a == (0, 0):
                    return True
            left = s.GFp.e(y) ** 2
            right = s.GFp.e(x) ** 3 + s.a * s.GFp.e(x) + s.b
            return left == right

        def __eq__(s, a):
            assert isinstance(a, EC.e)
            return s.v == a.v

        def __ne__(s, a):
            assert isinstance(a, EC.e)
            return s.v != a.v

        def __add__(s, a):
            assert isinstance(a, EC.e)
            if s.v == s.z:
                return a.v
            if a.v == s.z:
                return s.v
            x0, y0 = s.v
            x1, y1 = a.v
            if x0 == x1:
                if y0 == -y1:
                    return s.z
                m = (s.GFp.e(3) * x0 ** 2 + s.a) / (s.GFp.e(2) * y0)
            else:
                m = (y0 - y1) / (x0 - x1)
            x = m ** 2 - x0 - x1
            y = m * (x0 - x) - y0
            return EC.e((x, y))

        def __mul__(s, a):
            if a == 0:
                return s.z
            bit = map(int, bin(a).replace('0b', '')[1:])
            x = s
            for b in bit:
                x += x
                if b == 1:
                    x += s
            return x

        def __str__(s):
            return str(s.v)

        def __repr__(s):
            return repr(s.v)

class ECC(EC):
    def __init__(s, a, b, p):
        EC.__init__(s, a, b, p)

    def encrypt(s, e, M):
        return (EC.e(M) * e).v

    def decrypt(s, d, C):
        return (EC.e(C) * d).v

def main():
    ec = EC(3, 4, 7)
    print ec.e((0, 2)) == ec.e((0, 2))
    print ec.e((1, 1)) + ec.e((5, 2))
    print ec.e((5, 5)) + ec.e((5, 5))
    for i in range(8):
        print i, ec.e((0, 2)) * i
    ecc = ECC(3, 4, 7)
    print ecc.encrypt(2, (1, 1))
    print ecc.decrypt(3, (0, 2))

if __name__ == '__main__':
    main()
