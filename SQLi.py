import subprocess
from colorama import Fore

# Execute the command
def sqli_check(username_input, password_input, login_url):
    print(Fore.WHITE + "\n******************************************************")  # In case of redirect
    print("Scanning the Login Form for SQL Injection")
    url = login_url
    command = "sqlmap -u '" + url + "' --data '{}=admin&{}=123' --batch".format(username_input,password_input)
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # print(command)

    # Read the output in real-time
    injection_detected = False
    while True:
        if proc.poll() is not None:  # Check if the process has terminated
            break

        line = proc.stdout.readline().decode('utf-8').strip()
        if not line:
            continue

        # Check for "might be injectable" in the output
        if "might be injectable" in line or "the back-end DBMS" in line:
            print(Fore.RED + "The Login Form seems to be vulnerable to SQL Injection")
            injection_detected = True
            proc.terminate()
            break

    if not injection_detected:
        print("SQL Injection was not found in Login Form")

