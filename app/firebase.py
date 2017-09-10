from pyfcm import FCMNotification
from .config import *

def send_message(text):
    push_service = FCMNotification(api_key=FIREBASE_KEY)

    data_message = {
        "Nick" : "Mario",
        "body" : "great match!",
        "Room" : "PortugalVSDenmark"
    }

    #result = push_service.notify_topic_subscribers(topic_name="global", message_body=text)
    result = push_service.notify_single_device(registration_id=USER_ID, message_body=text, data_message=data_message)
    print result
