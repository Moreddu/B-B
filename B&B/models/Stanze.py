from google.appengine.ext import ndb

class Stanza(ndb.Model):
    """
    abbiamo definito delle tabelle (stanza_id, nome, piano, numero ecc) e tramite la libreria importata di google
    app engine (ndb è la libreria) utiizziamo le sue classi. quindi stanza_id conterrà stringhe, ecc ecc
    """

    stanza_id = ndb.StringProperty(required=True)
    nome_stanza = ndb.StringProperty(required=True)
    numero = ndb.IntegerProperty()
    piano = ndb.StringProperty()
    tipologia = ndb.StringProperty()
    prezzo = ndb.FloatProperty()
    immagine = ndb.BlobProperty()
    immagine_mimetype = ndb.StringProperty()

