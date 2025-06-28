import os
from urllib3.exceptions import InsecureRequestWarning
from colorama import Fore
import requests
from crawler import WebCrawler
import XSS_checker

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}


# Nikto Scan
def nikto_scan(target):
    nikto_commad = "nikto -host " + target
    print(Fore.WHITE + "\n******************************************************")
    print("Scanning with Nikto....!")
    os.system(nikto_commad)


def crawler(targetUrl, path):
    wc = WebCrawler()
    hrefLink = wc.extract_links(targetUrl)
    WebCrawler.print_links(hrefLink, targetUrl, path)


# Web Scanning Start
def web_scan(host, port, folder_path):
    print(Fore.GREEN + "Scanning Web on " + port)
    target = host + ":" + port
    try:
        url = "http://" + target
        r = requests.get(url, headers, allow_redirects=True)  # Request to Server
        if r.status_code != 200:  # Checking Response Code
            if r.status_code == 301:
                print(Fore.BLUE + "Skipping....! Website redirects to " + r.url)
                print(Fore.WHITE + "\n******************************************************")  # In case of redirect
            else:
                print("Website not working properly")
                print(Fore.WHITE + "\n******************************************************")  # In case of someother port

        # If everything is fine
        else:
            crawler(url, folder_path)
            XSS_checker.obtain_urlsForXSS(url, target)
            nikto_scan(target)


    except:
        try:
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)  # SSL Security Warning Bypass
            url = "https://" + target
            r = requests.get(url, headers, verify=False, allow_redirects=True)  # Request to Server
            if r.status_code != 200:  # Checking Response Code
                if r.status_code == 301:
                    print(Fore.BLUE + "Skipping....! Website redirects to " + r.url)
                    print(Fore.WHITE + "\n******************************************************")  # In case of redirect
                else:
                    print("Website not working properly")
                    print(Fore.WHITE + "\n******************************************************")  # In case of someother port

            # If everything is fine
            else:
                crawler(url, folder_path)
                XSS_checker.obtain_urlsForXSS(url, target)
                nikto_scan(target)


        except Exception as e:
            print(Fore.WHITE + "\n******************************************************")  # In case of redirect
            print(f'[-] ERROR: {e}')
