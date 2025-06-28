import os
import requests
import re
from urllib.parse import urljoin
import sys
from Login_brute import Login_bruteforce
from colorama import Fore


class WebCrawler:

    def __init__(self):
        self.response = None

    def extract_links(self, url):
        try:
            self.response = requests.get(url)
            linkList = re.findall('(?:href=")(.*?)"', self.response.content.decode('utf8'))
            return linkList

        except Exception as e:
            print(f'[-] ERROR: {e}')


    def print_links(href_link, target_url, folder_path):
        try:
            url_extracted = []
            login_urls = []
            for link in href_link:
                link = urljoin(target_url, link)
                if link.startswith(target_url):             # saving extracted links in an array
                    url_extracted.append(link)
                    url_extracted = list(dict.fromkeys(url_extracted))
                    if "login" in link or "Login" in link or "signin" in link:  # check for login page
                        print("Login found: " + link)
                        login_urls.append(link)
                        login_urls = list(dict.fromkeys(login_urls))
                        wc = Login_bruteforce(link, target_url)
                        wc.Captcha_check()
            if len(login_urls) == 0:
                print("No Login pages found")

            with open(folder_path + "/extracted_links.txt", "w") as outfile:
                outfile.write("\n".join(set(url_extracted)))
                outfile.close()
            print(Fore.WHITE + "\n******************************************************")
            print('[+] Following Links were extracted...')
            f = open(folder_path + "/extracted_links.txt", 'r')
            content = f.read()
            print(content)
            f.close()
            # print(url_extracted)

        except Exception as e:
            print(f'[-] ERROR: {e}')
            sys.exit(0)

