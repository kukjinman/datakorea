import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

class fcmapi:
    def __init__(self, key_path):
        cred = credentials.Certificate(f'{key_path}')
        firebase_admin.initialize_app(cred)

    def send_message(self, title, body):
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body
            ),
            data={
                'subtitle': '부제목',
                'screen': '4',
            },
            topic="test",
        )
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)