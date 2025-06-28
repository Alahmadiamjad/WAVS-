import os
from Web_Scanner import web_scan
import subprocess
from colorama import Fore


def nmap_scan():
    file_path = folder_path + "/nmap.txt"
    command = "nmap " + host + " -o " + file_path
    result = subprocess.check_output(command, shell=True)
    # subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # os.system(command)
    # f = open(file_path, 'r')
    # content = f.read()
    # if 'PORT' in content:
    if "PORT" in result.decode("utf-8"):
        print(Fore.WHITE + "\n******************************************************")  # In case of redirect
        print("The host seems live.")
        # f.close()
    else:
        print(file_path)
        print(Fore.WHITE + "\n******************************************************")  # In case of redirect
        print("The host doesn't seem live. Please check your input")
        exit()



def http_ports_grab(path):
    command = "awk '/http/' " + path + "/nmap.txt | awk '{print $1}' | grep -o '[0-9]\+' > " + path + "/http_ports.txt"
    os.system(command)
    http_open_ports = []
    with open(path + '/http_ports.txt') as my_file:
        for line in my_file:
            http_open_ports.append(line.rstrip('\n'))
    if http_open_ports == '':
        print(Fore.WHITE + "\n******************************************************")  # In case of redirect
        print('No web Ports seems open')
        exit()
    else:
        for i in http_open_ports:
            print(Fore.WHITE + "\n******************************************************")  # In case of redirect
            print("Open HTTP ports: " + i)
            web_scan(host, i, path)


def make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


if __name__ == '__main__':
    host = input("Please Enter URL or IP Address Without http/https:\n")
    # host = "testasp.vulnweb.com"
    print(Fore.WHITE + "\n******************************************************")  # In case of redirect
    print("Scanning " + host)
    folder_path = host + "_Enum"
    make_dir(folder_path)
    nmap_scan()
    http_ports_grab(folder_path)
