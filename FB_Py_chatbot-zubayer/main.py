from fbchat import Client, log
from fbchat.models import *


import data

class Jarvis(Client):
    
    def onMessage(self,author_id=None,message_object=None,thread_id=None,thread_type=ThreadType.USER, **kwargs):

        self.markAsRead(author_id)

        log.info("Message {} from {} in {}".format(message_object,thread_id,thread_id))
        
        msgText = message_object.text

        reply = 'Thanks for the messege'

        if author_id != self.uid:
            self.send(Message(text=reply),thread_id=thread_id,thread_type=thread_type)

        self.markAsDelivered(author_id,thread_id)

Client = Jarvis(data.email,data.password)
Client.listen()