import model

def kompleksne_nicle(izracun):
    return f"Lastne vrednosti matrike niso realne. Ta program deluje samo za matrike, katerih lastne vrednosti so realne." 

def izpis_jordanove(izracun):
    return izracun.jordanova()

def zahtevaj_vnos():
    matrika = input('Vpisite matriko:')
    return matrika

def pozeni_vmesnik():
    izracun = model.nov_izracun(zahtevaj_vnos())
    if izracun.realne():
        print(izpis_jordanove(izracun))
    else:
        print(kompleksne_nicle)

pozeni_vmesnik()