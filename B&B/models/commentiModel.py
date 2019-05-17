from google.appengine.ext import ndb

class Commento(ndb.Model):
    commento_id= ndb.StringProperty(required=True)
    guest_name= ndb.StringProperty()
    guest_email=ndb.IntegerProperty(required=True)
    guest_picture=ndb.StringProperty()
    test=ndb.StringProperty()
    datetime=ndb.DateTimeProperty(auto_now=True)