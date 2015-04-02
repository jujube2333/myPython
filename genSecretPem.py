from pyasn1.codec.der import decoder, encoder
from pyasn1.type import univ, namedtype
import textwrap
from gcd import *

class SecretKey(univ.Sequence):
    componentType = namedtype.NamedTypes(
            namedtype.NamedType("offset", univ.Integer()),
            namedtype.NamedType("modulus", univ.Integer()),
            namedtype.NamedType("publicExponent", univ.Integer()),
            namedtype.NamedType("privateExponent", univ.Integer()),
            namedtype.NamedType("prime1", univ.Integer()),
            namedtype.NamedType("prime2", univ.Integer()),
            namedtype.NamedType("exponent1", univ.Integer()),
            namedtype.NamedType("exponent2", univ.Integer()),
            namedtype.NamedType("coefficient", univ.Integer()),
    );

def genSecretPem(fname, p, q, e):
    n = p * q
    phin = (p-1) * (q-1)
    d = extEuclid(e, phin)[0] % phin
    exp1 = d % (p-1)
    exp2 = d % (q-1)
    cof = (q-1) % p

    sk = SecretKey().setComponentByPosition(0, 0).setComponentByPosition(1, n).setComponentByPosition(2, e).setComponentByPosition(3, d).setComponentByPosition(4, p).setComponentByPosition(5, q).setComponentByPosition(6, exp1).setComponentByPosition(7, exp2).setComponentByPosition(8, cof)

    der = encoder.encode(sk)
    der = der.encode('base64')
    der = textwrap.fill(der, 0x40)

    with open(fname, 'w') as f:
        f.write('-----BEGIN RSA PRIVATE KEY-----\n')
        f.write(der)
        f.write('\n-----END RSA PRIVATE KEY-----\n')

