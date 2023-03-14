import firebase_admin
from firebase_admin import credentials, auth

class NOIP:
    def __init__(self):
        # Load the Firebase service account key
        cred = credentials.Certificate('path/to/serviceAccountKey.json')
        firebase_admin.initialize_app(cred)

    def get_FCM_token(self, user_id):
        # Get the user's FCM token
        user = auth.get_user(user_id)
        return user.tokens.get('firebase')['token']
