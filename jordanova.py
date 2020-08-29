import model, bottle

jordanova = model.Jordanova()

@bottle.get('/')
def index():
    return bottle.template('index')

@bottle.post('/zacni/')
def nov_izracun():
    id_matrike = jordanova.nov_izracun('1 7 4 4')
    bottle.response.set_cookie("id_matrike", id_matrike, path='/', secret=SECRET)  
    bottle.redirect('/matrika/')

@bottle.get('/matrika/')
def zacetek():
    id_matrike = bottle.request.get_cookie("id_matrike", secret=SECRET)
    matrika = jordanova.matrike[id_matrike]
    return bottle.template('matrika', matrika=matrika, id_matrike=id_matrike)

bottle.run(reloader=True, debug=True)    