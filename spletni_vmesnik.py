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
    bottle.response.set_cookie("velikost", velikost, path='/', secret=SECRET)
    return bottle.template('vnos', velikost=velikost)

@bottle.get('/nov_izracun/')
def nov_izracun():
    velikost = bottle.request.get_cookie("velikost", secret=SECRET)
    matrika = []
    for vrstica in range(velikost):
        v = []
        for i in range(vrstica * velikost, (vrstica + 1) * velikost):
            v.append(int(bottle.request.query[str(i)]))
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
    if izracun.realne():
        koncna = izracun.jordanova()
        return bottle.template('izpis', jordanova=koncna)
    else:
        return bottle.template('kompleksne_lastne')

bottle.run(reloader=True, debug=True)    