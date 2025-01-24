import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
import pandas as pd
from lasku import avgVarErr
show = True
data = np.loadtxt('potentiaali.dat')
print(f"Mittaukset: \n\n{pd.DataFrame(data, columns=['Etäisyys', 'Mittaus1', 'Mittaus2', 'Mittaus3'])}\n")

mittaukset = [data[:,1], data[:,2], data[:,3]]
laskut = avgVarErr(mittaukset, 6)
# Jännite
avg = laskut[0]  # Keskiarvo jokaiselle mittaukselle
err = laskut[2]  # Virhe jokaiselle keskiarvolle (kait)
# Etäisyys
dis = data[:,0]
def malli(x,a):
    # Delta V = E*s
    return e*x
sov, cov = opt.curve_fit(malli, dis, avg, sigma=err)
sovfuc = sov[0]*dis

# Lasketaan virherajat
e_err = np.sqrt(cov[0][0])
sovfuc_min = (sov[0] - e_err) * dis
sovfuc_max = (sov[0] + e_err) * dis

print(f"""Lasketut arvot: \n\n{pd.DataFrame(list(zip(dis,avg,err,sovfuc)), columns=['Etäisyys', 'Keskiarvo', 'Virhe', 'Sovitus'])}\n
Sovitus:     a*s (a={sov[0]})
Kovarianssi: {cov[0][0]}""")

###################################3
fig = plt.figure()
fig.tight_layout()
plt.xlim([0,18])  # Nuppien kokonaisetäisyys cm (keskikohta siis 9cm)
plt.ylim([0,10])  # Jännitelähteen jännite

# Sovitus
plt.plot(dis, sovfuc, label='Sovitus')

# Virheraja-kuvaajat
plt.plot(dis, sovfuc_min, 'r--', label='Virhe minimi')
plt.plot(dis, sovfuc_max, 'g--', label='Virhe maksimi')

# Mittauspisteet
plt.errorbar(dis, avg, yerr=err, fmt='.', label='Mittauspisteet')
plt.grid(True)
plt.xlabel('Etäisyys (cm)')
plt.ylabel('Jännite (V)')
plt.legend()

if show:
    plt.show()
    fig.savefig("potentiaali.png")
