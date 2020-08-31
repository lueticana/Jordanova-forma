import model, bottle

bottle.TEMPLATE_PATH.insert(0, 'views')

jordanova = model.Jordanova()
SECRET = "JORDANOVA"

@bottle.get('/')
def zacetek():
    return bottle.template('zacetna_stran')

@bottle.get('/vnos_matrike/')
def zahtevaj_vnos():
    #id_izracuna = bottle.request.get_cookie("id_izracuna", secret=SECRET)
    velikost = int(bottle.request.query['velikost'])
    return bottle.template('vnos', velikost=velikost)

@bottle.post('/nov_izracun/')
def nova_igra():
    matrika =  bottle.request.query['matrika']
    #velikost = 2
    #for i in range(velikost ** 2):
    #    matrika += bottle.request.query[str(i)]
    id_izracuna = jordanova.nov_izracun(matrika)
    bottle.response.set_cookie("id_izracuna", id_izracuna, path='/', secret=SECRET)
    bottle.redirect(f'/jordanova/')

@bottle.get('/jordanova/')
def izpis():
    id_izracuna = bottle.request.get_cookie("id_izracuna", secret=SECRET)
    izracun = jordanova.nabor[id_izracuna]
    koncna = izracun.jordanova()
    return bottle.template('izpis', jordanova=koncna)

#@bottle.get()
#def zacetek():
#    #id_matrike = bottle.request.get_cookie("id_matrike", secret=SECRET)
#    matrika = jordanova.matrike[id_matrike]
#    return bottle.template('matrika', matrika=matrika, id_matrike=id_matrike)

bottle.run(reloader=True, debug=True)    