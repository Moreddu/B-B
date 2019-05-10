import uuid

from google.appengine.ext import ndb

from models.Stanze import Stanza

def getAllStanze():
    stanze = Stanza().query().fetch()
    return stanze

"""
dentro query() inserisco la query equivalente al select di sql(select * from Stanza, ad esempio). 
"""
def getStanza(stanza_id):
    stanza = Stanza().query(Stanza.stanza_id==stanza_id).fetch(1)
    return stanza


def insertStanza(form):
    try:
        stanza = Stanza()
        stanza.stanza_id = str(uuid.uuid4())
        stanza.nome_stanza = form('nome_stanza')
        stanza.prezzo = form('prezzo')
        stanza.numero = form('numero')
        stanza.piano = form('piano')
        stanza.put()
        return "Stanza creata"
    except Exception as e:
        print (str(e))
        return "Aggiornamento non completato"

def editStanza(stanza_id, form):
    try:
        stanza = Stanza().query(Stanza.stanza_id==stanza_id).fetch(1)[0]
        stanza.nome_stanza = form('nome_stanza')
        stanza.prezzo = form('prezzo')
        stanza.numero = form('numero')
        stanza.piano = form('piano')
        stanza.put()
        return "Aggiornamento completato"
    except Exception as e:
        print(str(e))
        return "Aggiornamento non completato"

def deleteStanza(stanza_id):
    try:
        """
        per eliminare la stanza ricerco con la query la stanza da eliminare, in seguito ottengo la key di quell'entità, 
        key che ottengo con un metodo dal datastore. in seguito gli dico di eliminare l'entità identificata con quella key.
         con google datastore si elimina cosi, è una procedura standard
        """
        Stanza.query(Stanza.stanza_id== stanza_id).fetch(1, keys_only=True)[0].get().key.delete()
        return "Stanza eliminata"
    except Exception as e:
        print(str(e))
        return "Eliminazione non riuscita"

def deleteAllStanza():
    try:
        """
        delete_multi è un metodo di app engine, ci permette di eliminare molte entità,
         cerchiamo tutte le stanze con query vuota(perche le vogliamo tutte) ci facciamo restituire le keys e eliminiamo
         tutte quelle stanze
         """
        ndb.delete_multi(Stanza.query().fetch(keys_only=True))
        return "tutte le stanze sono state eliminate"
    except Exception as e:
        print(str(e))
        return "Eliminazione non riuscita"
