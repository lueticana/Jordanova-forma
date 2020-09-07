import model, bottle

datoteka = 'nabor.json'

bottle.TEMPLATE_PATH.insert(0, 'views')

jordanova = model.Jordanova(datoteka)

SECRET = "JORDANOVA"

@bottle.get('/')
def zacetek():
    return bottle.template('zacetna_stran')

@bottle.get('/vnos_matrike/')    
def zahtevaj_vnos():
    velikost = int(bottle.request.query['velikost'])
    return bottle.template('vnos', velikost=velikost)

@bottle.get('/nov_izracun/<velikost:int>/')
def nov_izracun(velikost):
    matrika = []
    for vrstica in range(velikost):
        v = []
        for i in range(vrstica * velikost, (vrstica + 1) * velikost):
            vrednost = bottle.request.query[str(i)]
            try: 
                int(vrednost)
            except ValueError:
                return bottle.template('napacni_znaki')
            v.append(int(vrednost))
        matrika.append(v)
    jordanova.nalozi_iz_datoteke()
    id_izracuna = jordanova.nov_izracun(matrika)
    jordanova.zapisi_v_datoteko()
    bottle.response.set_cookie("id_izracuna", id_izracuna, path='/', secret=SECRET)
    return bottle.redirect('/jordanova/')

@bottle.get('/jordanova/')
def izpis():
    jordanova.nalozi_iz_datoteke()
    id_izracuna = bottle.request.get_cookie("id_izracuna", secret=SECRET)
    izracun = jordanova.nabor[id_izracuna]
    matrika = izracun.matrika
    if izracun.realne():
        koncna = izracun.jordanova()
        if len(koncna) != len(matrika):
            return bottle.template('napaka', matrika=matrika)
        for vrstica in koncna:
            if len(vrstica) != len(matrika):
                return bottle.template('napaka', matrika=matrika)
        return bottle.template('izpis', jordanova=koncna)
    else:
        return bottle.template('kompleksne_lastne', matrika=matrika)

bottle.run(reloader=True, debug=True)    