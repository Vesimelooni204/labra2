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
