import numpy as np

KOMPLEKSNE = 'lastne vrednosti niso realne'

def mnozenje_polinomov(p, r):
    dolzina = (len(p) - 1) + (len(r) - 1) + 1
    produkt = [0] * dolzina
    for i in range(len(p)):
        for j in range(len(r)):
            produkt[i + j] += p[i] * r[j]
    return produkt

def sestevanje_polinomov(p, r):
    krajsi = min(p, r, key=len)
    daljsi = max(p, r, key=len)
    for i in range(len(krajsi)):
        daljsi[i] += krajsi[i]
    return daljsi

def gaussova_eliminacija(m):
    matrika = []
    for vrstica in m:
        matrika.append(vrstica[:])
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
    gauss = gaussova_eliminacija(matrika)
    for vrstica in gauss:
        if vrstica == [0] * len(matrika):
            rang -= 1
    return rang

def mnozenje_matrik(a, b):
    A = np.array(a)
    B = np.array(b)
    return np.matmul(A, B). tolist()

def predznak(stevilo, polinom):
    for i in range(len(polinom)):
        polinom[i] = polinom[i] * stevilo
    return polinom


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
            matrika = self.priprava()
        if len(matrika) == 1:
            det = matrika[0][0]
        else:
            det = []
            for stolpec in range(len(matrika)):
                nova_matrika = []
                for i in range(1, len(matrika)):
                    nova_matrika.append(matrika[i][:stolpec] + matrika[i][stolpec + 1:])
                det = sestevanje_polinomov(det, predznak((-1)**(stolpec), mnozenje_polinomov(matrika[0][stolpec], self.karakteristicni(nova_matrika))))
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
            lastne[i] = round(lastne[i], 3)
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
        jedra = []
        rang1 = rang(matrika)
        jedra.append(self.velikost - rang1)
        zmnozena = mnozenje_matrik(matrika, matrika)
        rang2 = rang(zmnozena)
        while rang2 < rang1:
            jedra.append(self.velikost - rang2)
            rang1 = rang2
            zmnozena = mnozenje_matrik(matrika, zmnozena)
            rang2 = rang(zmnozena)
        for i in range(1, len(jedra)):
            jedra[-i] = jedra[-i] - jedra[-(i + 1)]
        velikost = len(jedra)
        celice = {velikost : jedra[-1]}
        for i in range(2, len(jedra) + 1):
            velikost -= 1
            celice[velikost] = jedra[-i] - jedra[-(i - 1)]
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



        



            





                    


            









