import numpy as np
velikost = len(matrika)

KOMPLEKSNE = 'lastne vrednosti niso realne'
REALNE = 'lastne vrednosti so realne'

class Jordanova:

    def __init__(self, matrika):
        self.matrika = matrika

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

    def determinanta(matrika):
        if len(matrika) == 1:
            det = matrika[0][0]
        else:
            det = 0
            for stolpec in range(len(matrika)):
                nova_matrika = []
                for i in range(1, len(matrika)):
                    nova_matrika.append(matrika[i][:stolpec] + matrika[i][stolpec + 1:])
                det = det + (-1)**(stolpec) * matrika[0][stolpec] * determinanta(nova_matrika)
        return det

    def priprava(self):
        priprava = []
        for vrstica in range(len(self.matrika)):
            nova_vrstica = []
            for stolpec in range(len(self.matrika)):
                if vrstica == stolpec:
                    nova_vrstica.append([self.matrika[vrstica][stolpec], -1])
                else:
                    nova_vrstica.append([self.matrika[vrstica][stolpec]])
            priprava.append(nova_vrstica)
        return priprava




    def karakteristicni(matrika):
        if len(matrika) == 1:
            det = matrika[0][0]
        else:
            det = []
            for stolpec in range(len(matrika)):
                nova_matrika = []
                for i in range(1, len(matrika)):
                    nova_matrika.append(matrika[i][:stolpec] + matrika[i][stolpec + 1:])
                det = sestevanje_polinomov(det, (-1)**(stolpec) * mnozenje_polinomov(matrika[0][stolpec], karakteristicni(nova_matrika)))
        return det

    def nicle():
        kar = karakteristicni()
        kar.reverse()
        return np.roots(kar)

    def realne():
        lastne = nicle()
        return len(lastne) == len(lastne.real[abs(lastne.imag)<1e-5])
    
    def lastne_vrednosti():
        lastne = nicle().tolist()
        for i in len(lastne):
            lastne[i] = round(lastne[i], 3) * (-1)
        slovar = {}
        for vred in lastne:
            if vred in slovar.keys():
                slovar[vred] += 1
            else:
                slovar[vred] = 1
        return slovar

    def stevilo_celic():
        lastne = lastne_vrednosti()
        for vred in lastne.items():
            if lastne[vred] == 1:
                return 1
            else:
                geom veckr = st stevilo_celic

    def dim():


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




                    


            









