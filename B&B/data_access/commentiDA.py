import uuid
from models.commentiModel import Commento

def getAllCommenti():
    comm = Commento().query().fetch()
    return comm

def insertCommento(msg, user_info):
    try:
        comm = Commento()
        comm.commento_id = str(uuid.uuid4())
        comm.guest_email = user_info['email']
        comm.gest_name = user_info['name']
        comm.guest_picture = user_info['picture']
        comm.testo= msg
        comm.put()
        return "Commento inserito"
    except Exception as e:
        print(str(e))
        return "Commento non creato"
    