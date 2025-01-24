import numpy as np
import zlib
data = b'x\x9c\xed\x93\xbbn\xc30\x0cEw\x7f\xc5\xdd\xbc\xe4\'\x02\x14(\xb2t\r:\xca\x16m\xab\x96\xc9@\x8f\x18\xfe\xfbRJ\xfap\xf7\x0eA\xbb\x19\xa2tt\xc8+\x9f\xa9\r\x04\x16\xc4\x14\x0c\x8f\x14"\x92\xc0\xcb\x95\x9aW\xc9\x98YV\xa4\x89\x10\xb2\xa7\x08\xc3\x16Q`\x05\xa7\xe6\x88!{\x8f^\x96\xc5\xa5\x858\xb5\x11\xebd\x12N\xed\xa2G\x1c\xcf\x8e[\xc8P9\xabdo\xb9M\x18)\x95b\xc4\x10dQ\xde\x06Q|\xc0\x98\xb7\xe6\x84\xb7\x1c\x13V\xc3l\x90H\xe1\x9b\x1e\x9d\xd4\xa0 \x07"\xefxl\x9e%%\x83\xc5\xccT\xcb\x99\xadJ\'5k^\xe8ZHR\x8e\x8f\xeez\xaf_v\xeb^\xef/\xcbVV\xde\x15Bf\x98 \x8a\xab]Z\x8a\x14\xea\xd6\xdd\xae\xcfk\xfb\xb0\xed\n\xd1l\xfa%\xb6\xdbh\xb7^\xdb\xd0k\x1dU\xec\x94\xef\xd03\xb5*X\xc6\xcb \xd3O\xf71\x0c\x12\xca\x80\xbdh\xa3:\xb7\x80\x89L(\x93\xed\x88\xd4\xaf\xd7\xb1\x8e\x07t\xb9BJrI4\xbai+\xa1\x15\x05\x97\x9a\x13Gg\xe9\x80\x95\xd0)\xf4\x16a\t\xe6\x832\x8aB \xac\x0e_\xf9\x8ef\xb9\x19\xae\xf5A\xdc\xe4/\xfe\x86<\xea\xba\x1bj\xdf&\xce\xd0\x9d?Cy\x92\x12nmv\xa1\xefn\x9d\x96m\xb5#z\xa8\x80\x1e\xc9\xf5\xa1\x1e\xd3_\xfa\xcb\xff]\x7f\xc5\xf5\x1d\xe7:`\x1e'

class WrongL(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
def avgVarErr(values, acc):
    # Laskee jokaisen mittauksen arvon keskiarvon.
    # Ottaa argumentiksi arvot, jossa on ties kuinka monen mittauksen edestä listoja.
    # Esim. [[1,2,3], [4,5,6],[7,8,9]]
    # Jokaisen jäsenen on oltava yhtä pitkiä (muuten jollekin mittaukselle ei voi laskea keskiarvoa).
    l = len(values[0])
    p = len(values) # Mittausten määrä
    # Check
    for i in values:
        if len(i) != l:
            raise WrongL(f"Listan pituus on epähyvä: {i}")
        else:
            pass
    ret = []
    # Flipperiino
    # i indeksi
    for i in range(l):
        items = []
        for k in values:
            items.append(k[i].item())
        ret.append(items)
    mean = []
    var = []
    err = []
    for i, arvo in enumerate(ret):
        mean.append(np.round(np.mean(arvo), acc).item())
        var.append(np.round(np.var(arvo), acc).item())
        err.append(np.round(np.sqrt(var[i])/np.sqrt(p), acc).item())
    return mean, var, err
if __name__ == "__main__":
    print(f"Tätä tiedostoa ei ole tarkoitettu ajettavaksi.\n{str(zlib.decompress(data)).replace("\\n", "\n")}")
# Älä aja tätä tiedostoa :)
