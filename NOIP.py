import os
import time
import requests

class NOIP:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False
        self.cookies = None
        self.hostnames = []
    
    def login(self):
        """Log in to the NOIP website"""
        url = "https://my.noip.com/login"
        data = {
            "username": self.username,
            "password": self.password,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url, data=data, headers=headers)
        self.cookies = response.cookies
        self.logged_in = True
        
    def create_new_account(self, email, first_name, last_name):
        """Create a new NOIP account"""
        url = "https://my.noip.com/#!/signup"
        response = requests.get(url)
        csrf_token = response.text.split('csrf_token" value="')[1].split('"')[0]
        data = {
            "csrf_token": csrf_token,
            "email": email,
            "password": self.password,
            "first_name": first_name,
            "last_name": last_name,
            "signup": "Sign Up",
            "license_agreement": "on"
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            print("Account created successfully!")
        else:
            print("There was an error creating your account. Please try again.")
    
    def create_new_hostname(self, hostname):
        """Create a new hostname on the NOIP website"""
        if not self.logged_in:
            self.login()
        url = "https://my.noip.com/#!/dynamic-dns"
        response = requests.get(url, cookies=self.cookies)
        csrf_token = response.text.split('csrf_token" value="')[1].split('"')[0]
        data = {
            "csrf_token": csrf_token,
            "hostname": hostname,
            "group_id": "",
            "ttl": "60",
            "submit": "Create Hostname"
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url, data=data, headers=headers, cookies=self.cookies)
        if response.status_code == 200:
            print(f"Hostname {hostname} created successfully!")
            self.hostnames.append(hostname)
        else:
            print("There was an error creating your hostname. Please try again.")
    
    def update_ip_address(self, hostname):
        """Update the IP address for a given hostname"""
        if not self.logged_in:
            self.login()
        url = "https://my.noip.com/#!/dynamic-dns"
        response = requests.get(url, cookies=self.cookies)
        csrf_token = response.text.split('csrf_token" value="')[1].split('"')[0]
        data = {
            "csrf_token": csrf_token,
            "host_id": "",
            "hostname": hostname,
            "myip": "",
            "offline": "",
            "submit": "Update Hostname"
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url, data=data, headers=headers, cookies=self.cookies)
        if response.status_code == 200:
            print(f"IP address updated successfully for {hostname}.")
        else:
            

            except requests.exceptions.RequestException as e:
            print("There was an error updating the IP address.")
            print(e)

