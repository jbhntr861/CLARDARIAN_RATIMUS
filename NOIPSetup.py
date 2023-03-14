class NOIPSetup:
    def __init__(self):
        self.username = input("Enter your NOIP username: ")
        self.password = input("Enter your NOIP password: ")
        self.hostname = input("Enter the hostname you want to use (e.g. mysite.ddns.net): ")
        self.ip = None
        self.set_ip()

    def set_ip(self):
        try:
            self.ip = requests.get('https://api.ipify.org').text
            print(f"Current IP address is {self.ip}.")
        except requests.exceptions.RequestException as e:
            print("There was an error getting the IP address.")
            print(e)

    def create_noip_account(self):
        try:
            res = requests.post('https://dynupdate.no-ip.com/nic/update', auth=(self.username, self.password), params={'hostname': self.hostname, 'myip': self.ip})
            if 'good' in res.text:
                print(f"Account created and IP address updated successfully for {self.hostname}.")
            else:
                print("There was an error creating the account or updating the IP address.")
                print(res.text)
        except requests.exceptions.RequestException as e:
            print("There was an error creating the account or updating the IP address.")
            print(e)

if __name__ == "__main__":
    noip_setup = NOIPSetup()
    noip_setup.create_noip_account()