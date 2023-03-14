from google.oauth2 import service_account
from firebase_admin import messaging
import requests

class CloudController:
    def __init__(self, noip_address):
        self.noip_address = noip_address

    def execute_command(self, command):
        print(f"Sending command '{command}' to {self.noip_address} using Google Cloud Base...")
        
        # Authenticate with the Google Cloud Platform using a service account key
        credentials = service_account.Credentials.from_service_account_file('service-account-key.json')

        # Initialize Firebase Cloud Messaging
        messaging.initialize_app(credentials=credentials)

        # Define the message to send to the device
        message = messaging.Message(
            data={
                'command': command,
            },
            token=self.get_fcm_token(),
        )

        # Send the message to the device via Firebase Cloud Messaging
        response = messaging.send(message)
        print(f"Message ID: {response}")
        
    def get_fcm_token(self):
        # Get the FCM token associated with the device's NOIP address
        url = f"https://api.noip.com/managed-dns/v2/hosts/{self.noip_address}/tokens"
        response = requests.get(url)
        if response.ok:
            fcm_token = response.json()['tokens'][0]['token']
            return fcm_token
        else:
            print(f"Failed to get FCM token for {self.noip_address}")
            return None
