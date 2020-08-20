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

    def determinanta(matrika):
        if len(matrika) == 1:
            det = matrika[0][0]
        else:
            det = 0
            for vrstica in range(len(matrika)):
                for stolpec in range(len(matrika)):
                    nova_matrika = []
                    for i in range(len(matrika)):
                        if i == vrstica:
                            pass
                        else:
                            nova_matrika.append(matrika[i][:stolpec] + matrika[i][stolpec + 1:])
                        det = det + (-1)**(i + stolpec) * matrika[i][stolpec] * determinanta(nova_matrika)
        return det