import GField as GF

class EC:
    z = 0
    # y^2 = x^3 + ax + b
    def __init__(s, a, b, p):
        assert 4 * a ** 3 + 27 * b ** 2 != 0
        s.a = a
        s.b = b
        s.p = p
        s.GFp = GF.GF(p)

    def isValid(s, a):
        if a == EC.z:
            return True

        assert isinstance(a, tuple)
        x, y = a
        left = s.GFp.v(y) ** 2
        right = s.GFp.v(x) ** 3 + s.GFp.v(s.a) * s.GFp.v(x) + s.GFp.v(s.b)
        return left == right

    def at(s, x):
        y = s.GFp.v(x) ** 3 + s.GFp.v(s.a) * s.GFp.v(x) + s.GFp.v(s.b)
        for i in range(s.p):
            if pow(i, i ,s.p) == y:
                y = i
                return s.GFp.v(y), s.GFp.v(-y)
        return None

ec = EC(3, 4, 7)
print ec.isValid((0, 2))
