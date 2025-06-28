import requests
from bs4 import BeautifulSoup
from colorama import Fore

# Define the URL of the web page to parse
# url = 'http://testasp.vulnweb.com/Search.asp'

def XSS_Checker(extracted_url, domain):
# Send a GET request to the URL and parse the response with BeautifulSoup
    response = requests.get(extracted_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first form in the response
    form = soup.find('form')
    if form is not None:
        # Get the action attribute and method of the form
        action = form.get('action')
        method = form.get('method')

        # Find all input fields in the form
        input_fields = form.find_all('input')

        # Create a dictionary to store the values to be submitted with the form
        form_data = {}

        # Insert text in the input fields and check for XSS vulnerability
        for input_field in input_fields:
            # Get the name of the input field
            input_name = input_field.get('name')
            input_type = input_field.get('type')

            # Check if the input field has a name attribute
            if input_name is not None and input_type == "text":
                # Check for XSS vulnerability by inserting a script tag in the input field
                form_data[input_name] = '<script>alert(1);</script>'

                # Submit the form with the specified data
                if method == 'post':
                    # Submit the form using a POST request
                    response = requests.post(f'{domain}/{action}', data=form_data)
                elif method == 'get':
                    # Build the URL with the form data as query parameters
                    query_params = '&'.join([f'{key}={value}' for key, value in form_data.items()])
                    uurl = f'{action}?{query_params}'

                    # Submit the form using a GET request
                    response = requests.get(f'{domain}/{uurl}')

                # Check if the injected script tag is present in the response
                if '<script>alert(1);</script>' in response.text:
                    print(Fore.RED +f'XSS vulnerability found in {extracted_url} at {input_name} field\n')



def obtain_urlsForXSS(domain, dom):
    url_list = []
    print(Fore.WHITE + "\n******************************************************")
    print("Scanning all the pages extracted for XSS")
    dom=dom.split(':')[0]
    with open(f'{dom}_Enum/extracted_links.txt') as my_file:
        for line in my_file:
            url_list.append(line.rstrip('\n'))
        for i in url_list:
            XSS_Checker(i, domain)
