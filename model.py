import numpy as np
import json

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
    vrstica = 0
    for stolpec in range(len(matrika)):
        if matrika[vrstica][stolpec] == 0:
            vse_nic = 1    
            for ostale_vrstice in range(vrstica, len(matrika)):
                if matrika[ostale_vrstice][stolpec] !=  0:
                    matrika[vrstica], matrika[ostale_vrstice] = matrika[ostale_vrstice], matrika[vrstica]
                    vse_nic = 0
                    break
            if vse_nic == 1:
                continue
        p = matrika[vrstica][stolpec]
        for i in range(len(matrika)):    
            matrika[vrstica][i] = matrika[vrstica][i] / p
        for ostale_vrstice in range(vrstica + 1, len(matrika)):
            a = matrika[ostale_vrstice][stolpec]
            for ostali_stolpci in range(stolpec, len(matrika)):
                razlika = matrika[ostale_vrstice][ostali_stolpci] - (matrika[vrstica][ostali_stolpci] * a)
                if razlika < 1e-5:
                    matrika[ostale_vrstice][ostali_stolpci] = 0
                else:
                    matrika[ostale_vrstice][ostali_stolpci] = razlika
        vrstica += 1
    return matrika

def rang(matrika):
    rang = len(matrika)
    gauss = gaussova_eliminacija(matrika)
    for vrstica in gauss:
        if vrstica == [0] * len(gauss):
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
        return len(lastne) == len(lastne.real[abs(lastne.imag)<1e-3])
    
    def lastne_vrednosti(self):
        lastne = self.nicle().tolist()
        for i in range(len(lastne)):
            lastne[i] = round(lastne[i].real, 3)
        slovar = {}
        for vred in lastne:
            if vred in slovar.keys():
                slovar[vred] += 1
            else:
                slovar[vred] = 1
        return slovar

    def velikosti_celic(self, lastna_vrednost):
        matrika = []
        for vrstica in self.matrika:
            matrika.append(vrstica[:])
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
            print(rang1, rang2)
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
        if int(lastna_vrednost) == lastna_vrednost:
            lastna_vrednost = int(lastna_vrednost)
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
                for i in range(celice[velikost]):
                    celica = self.celica(vrednost, velikost)
                    for vrstica in celica:
                        zozitev.append([0] * polozaj_znotraj_zozitve + vrstica + [0] * (velikost_zozitve - (polozaj_znotraj_zozitve + len(vrstica))))
                    polozaj_znotraj_zozitve += velikost
            for vrstica in zozitev:
                jordanova.append([0] * polozaj + vrstica + [0] * (self.velikost - (polozaj + len(vrstica))))
            polozaj += len(zozitev)
        print(jordanova)
        return jordanova




class Jordanova:

    def __init__(self, datoteka):
        self.nabor = {}
        self.datoteka = datoteka

    def prost_id(self):
        if self.nabor.keys():
            return max(self.nabor.keys()) + 1
        else:
            return 0
    
    def nov_izracun(self, matrika):
        id_izracuna = self.prost_id()
        izracun = Izracun(matrika)
        self.nabor[id_izracuna] = izracun
        return id_izracuna

    def nalozi_iz_datoteke(self):
        with open(self.datoteka) as f:
            podatki = json.load(f)
        self.nabor = {}
        for id_izracuna, izracun in podatki.items():
            self.nabor[int(id_izracuna)] = (
                Izracun(izracun['matrika']))

    def zapisi_v_datoteko(self):
        podatki = {}
        for id_izracuna, izracun in self.nabor.items():
            podatki[id_izracuna] = {'matrika': izracun.matrika}
        with open(self.datoteka, 'w') as f:
            json.dump(podatki, f)
     




    



        



            





                    


            









