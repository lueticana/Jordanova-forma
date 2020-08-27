import numpy as np

KOMPLEKSNE = 'lastne vrednosti niso realne'

def mnozenje_polinomov(p, r):
    dolzina = (len(p) - 1) + (len(r) - 1) + 1
    produkt = [0] * dolzina
    for i in range(len(p)):
        for j in range(len(r)):
            print(produkt, p ,r )
            produkt[i + j] += p[i] * r[j]
    return produkt

def sestevanje_polinomov(p, r):
    krajsi = min(p, r, key=len)
    daljsi = max(p, r, key=len)
    for i in range(len(krajsi)):
        daljsi[i] += krajsi[i]
    return daljsi

def gaussova_eliminacija(matrika):
    for pozicija in range(len(matrika)):
        if matrika[pozicija][pozicija] == 0:
            vse_nic = 1    
            for vrstica in range(pozicija, len(matrika)):
                if matrika[vrstica][pozicija] !=  0:
                    matrika[pozicija], matrika[vrstica] = matrika[vrstica], matrika[pozicija]
                    vse_nic = 0
                    break
            if vse_nic == 1:
                continue
        p = matrika[pozicija][pozicija]
        for i in range(len(matrika)):    
            matrika[pozicija][i] = matrika[pozicija][i] / p
        for vrstica in range(pozicija + 1, len(matrika)):
            a = matrika[vrstica][pozicija]
            for stolpec in range(pozicija, len(matrika)):    
                matrika[vrstica][stolpec] = matrika[vrstica][stolpec] - (matrika[pozicija][stolpec] * a)
    return matrika

def rang(matrika):
    rang = len(matrika)
    for vrstica in gaussova_eliminacija(matrika):
        if vrstica == [0] * len(matrika):
            rang -= 1
    return rang

def mnozenje_matrik(a, b):
    A = np.array(a)
    B = np.array(b)
    return np.matmul(A, B). tolist()


class Izracun:

    def __init__(self, matrika):
        self.matrika = matrika
        self.velikost = len(matrika)

    def priprava(self, matrika=None):
        if matrika == None:
            matrika = self.matrika
        priprava = []
        for vrstica in range(len(matrika)):
            nova_vrstica = []
            for stolpec in range(len(matrika[vrstica])):
                if vrstica == stolpec:
                    nova_vrstica.append([matrika[vrstica][stolpec], -1])
                else:
                    nova_vrstica.append([matrika[vrstica][stolpec]])
            priprava.append(nova_vrstica)
        return priprava

    def karakteristicni(self, matrika=None):
        if matrika == None:
            matrika = self.matrika
        matrika_pripravljena = self.priprava(matrika)
        if len(matrika_pripravljena) == 1:
            det = matrika_pripravljena[0][0]
        else:
            det = []
            for stolpec in range(len(matrika_pripravljena[0])):
                nova_matrika = []
                for i in range(1, len(matrika_pripravljena)):
                    nova_matrika.append(matrika[i][:stolpec] + matrika[i][stolpec + 1:])
                print(nova_matrika)
                det = sestevanje_polinomov(det, (-1)**(stolpec) * mnozenje_polinomov(matrika_pripravljena[0][stolpec], self.karakteristicni(nova_matrika)))
        return det

    def nicle(self):
        kar = self.karakteristicni()
        kar.reverse()
        return np.roots(kar)

    def realne(self):
        lastne = self.nicle()
        return len(lastne) == len(lastne.real[abs(lastne.imag)<1e-5])
    
    def lastne_vrednosti(self):
        lastne = self.nicle().tolist()
        for i in range(len(lastne)):
            lastne[i] = round(lastne[i], 3) * (-1)
        slovar = {}
        for vred in lastne:
            if vred in slovar.keys():
                slovar[vred] += 1
            else:
                slovar[vred] = 1
        return slovar

    def stevilo_celic(self, lastna_vrednost):
        matrika = self.matrika[:]
        for i in range(self.velikost):
            matrika[i][i] = matrika[i][i] - lastna_vrednost
        return rang(matrika)

    def velikosti_celic(self, lastna_vrednost):
        matrika = self.matrika[:]
        for i in range(self.velikost):
            matrika[i][i] = matrika[i][i] - lastna_vrednost
        vektorji = []
        rang1 = rang(matrika)
        vektorji.append(rang1)
        zmnozena = mnozenje_matrik(matrika, matrika)
        rang2 = rang(zmnozena)
        while rang2 > rang1:
            vektorji.append(rang2)
            rang1 = rang2
            zmnozena = mnozenje_matrik(matrika, zmnozena)
            rang2 = rang(zmnozena)
        velikost = len(vektorji)
        celice = {velikost : vektorji[-1]}
        for i in range(2, len(vektorji) + 1):
            velikost -= 1
            celice[velikost] = vektorji[-i] - vektorji[-(i - 1)]
        return celice

    def celica(self, lastna_vrednost, velikost):
        celica = []
        for i in range(velikost):
            if i == velikost - 1:
                celica.append([0] * i + [lastna_vrednost])
            else:
                celica.append([0] * i + [lastna_vrednost] + [1] + [0] * (velikost - (i + 2)))
        return celica
        
    def jordanova(self):
        jordanova = []
        lastne = self.lastne_vrednosti()
        polozaj = 0
        for vrednost in lastne.keys():
            zozitev = []
            celice = self.velikosti_celic(vrednost)
            polozaj_znotraj_zozitve = 0
            velikost_zozitve = lastne[vrednost]
            for velikost in celice.keys():
                celica = self.celica(vrednost, velikost)
                for vrstica in celica:
                    zozitev.append([0] * polozaj_znotraj_zozitve + vrstica + [0] * (velikost_zozitve - (polozaj + len(vrstica))))
                polozaj_znotraj_zozitve += velikost
            for vrstica in zozitev:
                jordanova.append([0] * polozaj + vrstica + [0] * (self.velikost - (polozaj + len(vrstica))))
            polozaj += len(zozitev)
        return jordanova

def nov_izracun(matrika):
    izracun = Izracun(matrika)
    return izracun



        



            





                    


            









