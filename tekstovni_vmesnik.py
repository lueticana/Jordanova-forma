import model

def kompleksne_nicle(izracun):
    return f"Lastne vrednosti matrike niso realne. Ta program deluje samo za matrike, katerih lastne vrednosti so realne." 

def izpis_jordanove(izracun):
    return izracun.jordanova()

def zahtevaj_vnos():
    vnos = input('Vpisite matriko:')
    vnos = vnos.split()
    velikost = int(len(vnos) ** (1/2))
    vmesni_korak = []
    matrika = []
    for i in vnos:
        vmesni_korak.append(float(i))
    for i in range(0, len(vnos), velikost):
        matrika.append(vmesni_korak[i:(i + velikost)])
    return matrika

def pozeni_vmesnik():
    izracun = model.nov_izracun(zahtevaj_vnos())
    if izracun.realne():
        print(izpis_jordanove(izracun))
    else:
        print(kompleksne_nicle)

pozeni_vmesnik()