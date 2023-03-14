import socket

class Listener:
    def __init__(self, noip):
        self.noip = noip

    def listen(self):
        # Get the IP address for the NOIP hostname
        try:
            ip_address = socket.gethostbyname(self.noip.hostname)
        except socket.gaierror:
            print(f"Error: Could not resolve hostname {self.noip.hostname}. Please check your NOIP settings and try again.")
            return

        # Create a socket object and try to connect to the APK
        try:
            s = socket.socket()
            s.connect((ip_address, self.noip.port))
        except ConnectionRefusedError:
            print(f"Error: Could not connect to {self.noip.hostname}. Please check that the APK is running and that your firewall is not blocking the connection.")
            return

        # Connection successful
        print(f"Connected to {self.noip.hostname} ({ip_address}) on port {self.noip.port}. You can now send commands to the APK.")
        while True:
            # Listen for data from the APK
            data = s.recv(1024)
            if not data:
                break

            # Process the data
            command = data.decode("utf-8").strip()
            print(f"Received command: {command}")

        # Close the socket when finished
        s.close()