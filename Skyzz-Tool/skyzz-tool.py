# Copyright 2024 SkyzzTech
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



from tools.internet import ci
from tools.modules import cd
import os
import subprocess
import sys
import time
import nmap
import requests
import re
import ipaddress
import random
import string



def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

ci()
cd()
clear_screen()


YELLOW = "\033[33m"
RED = "\033[31m"
GREEN = "\033[32m"
PURPLE = "\033[35m"
PINK = "\033[35m"
BLUE = "\033[34m"
RESET = "\033[0m"

sc = nmap.PortScanner()


def print_with_typing_effect(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  

def main():
    
    print(PURPLE + """███████╗██╗  ██╗██╗   ██╗███████╗███████╗  ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔════╝██║ ██╔╝╚██╗ ██╔╝╚══███╔╝╚══███╔╝  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████╗█████╔╝  ╚████╔╝   ███╔╝   ███╔╝█████╗██║   ██║   ██║██║   ██║██║     ███████╗
╚════██║██╔═██╗   ╚██╔╝   ███╔╝   ███╔╝ ╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
███████║██║  ██╗   ██║   ███████╗███████╗     ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝\n
Create by Skyzz --> https://github.com/SkyzzTech 
Inspired By YureiNox --> https://github.com/YureiNox""" + RESET)

    while True:
        n = input("\n[1] IP Info\n[2] Port Scanner\n[3] Vulnerabilities Scanner\n[4] Ip Site Finder\n[5] Github Email Grabber\n[6] Discord Nitro Finder\n[7] Leave\n\nSelect a Number: ")
        if n == '1':
            ipinfo()
        elif n == '2':
            nmap_scan()
        elif n == '3':
            print_with_typing_effect(PURPLE + """********************** Welcome To Vulnerabilities Scanner **********************\n********************************************************************************""" + RESET)
            ip = input(PURPLE + "Enter Target IP:" + RESET)
            scan_vulnerabilities(ip)
        elif n == '4':
            scan_ip_site()
        elif n == '5':
            github_mail()    
        elif n == '6':
            verify_nitro_codes()
        elif n == '7':
            print("""Thank you for use Skyzz-Tools!\n\nFollow me on https://github.com/SkyzzTech""")
            input("\n\nPress enter to exit...")
            break
        else:
            print_with_typing_effect(RED + "ERROR: Please Choose a Number Between 1 and 6" + RESET)
            time.sleep(1)
        clear_screen()
        main()
 

def is_valid_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def ipinfo():
    print_with_typing_effect(PURPLE + """********************** Welcome To IPinfo **********************\n***************************************************************""" + RESET)

    ip_address = input(PURPLE + "Enter Target IP:" + RESET)

    if not is_valid_ip(ip_address):
        print_with_typing_effect(RED + "ERROR: Please Enter a Valid IP." + RESET)
        time.sleep(1)
        clear_screen()
        main()


    print_with_typing_effect(YELLOW + "Loading, Please Wait", 0.01)
    clear_screen()
    token = "611514109bebb7"
    url = f"https://ipinfo.io/{ip_address}?token={token}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print_with_typing_effect( RESET + BLUE + "\nIP Address Information: ")
            print_with_typing_effect(RESET + f"IP Address: {data.get('ip')}")
            print_with_typing_effect(f"Approximate City: {data.get('city')}")
            print_with_typing_effect(f"Region: {data.get('region')}")
            print_with_typing_effect(f"Approximate Postal Code: {data.get('postal')}")
            print_with_typing_effect(f"Country: {data.get('country')}")
            print_with_typing_effect(f"Access Provider: {data.get('org')}")
            print_with_typing_effect(f"Approximate Location: {data.get('loc')}" + RESET)
        else:
            print_with_typing_effect("Error During Query: " + str(response.status_code))
    except Exception as e:
        print_with_typing_effect("An error occurred: " + str(e))

    input(BLUE + "\nPress Enter To Return To The Main Menu..." + RESET)
    clear_screen()
    main()

def nmap_scan():
    print_with_typing_effect (PURPLE + """********************** Welcome To Port Scanner **********************\n*********************************************************************""" + RESET)

    ip = input(PURPLE + "Enter Target IP:" + RESET)

    if not is_valid_ip(ip):
        print_with_typing_effect(RED + "ERROR: Please Enter a Valid IP." + RESET)
        time.sleep(1)
        clear_screen()
        main()


    print_with_typing_effect(YELLOW + "Loading, Please Wait", 0.01)
    
    try:
        result = sc.scan(ip, arguments='-sS -sV -Pn')
        print_with_typing_effect(RESET + "\nResults of open ports with services and version")
        for port, info in result['scan'].get(ip, {}).get('tcp', {}).items():
            state = info['state']
            service_name = info['name']
            service_version = info.get('version', 'Unknown')
            print_with_typing_effect(f"Port {port}: {state} ({service_name}, Version: {service_version})")
    except Exception as e:
        print_with_typing_effect("An error occurred during the scan: " + str(e))

    input(BLUE + "\nPress Enter To Return To The Main Menu..." + RESET)
    clear_screen()
    main()

def scan_vulnerabilities(ip):
    if not is_valid_ip(ip):
        print_with_typing_effect("Enter a Valid IP address.")
        input(BLUE + "\nPress Enter To Return To The Main Menu..." + RESET)
        clear_screen()
        main()

    print_with_typing_effect(YELLOW + "Loading, Please Wait", 0.01)

    try:
        result = sc.scan(ip, arguments='--script vuln')
        print_with_typing_effect("\nVulnerabilities Were Found:")
        for port, info in result['scan'].get(ip, {}).get('tcp', {}).items():
            print_with_typing_effect(f"\nPort {port}:")
            if 'script' in info:
                for script_id, script_output in info['script'].items():
                    print_with_typing_effect(f"  - Script: {script_id}")
                    print_with_typing_effect(f"    Result: {script_output}")
            else:
                print_with_typing_effect("No Vulnerabilities Found.")
    except Exception as e:
        print_with_typing_effect("An error occurred during the vulnerability scan: " + str(e))

    input(BLUE + "\nPress Enter To Return To The Main Menu..." + RESET)
    clear_screen()
    main()

def scan_ip_site():
    print_with_typing_effect(PURPLE + """********************** Welcome To Ip Site Finder **********************\n***********************************************************************""" + RESET)

    hostname = input(PURPLE + "Enter The Site Address:" + RESET)

    print_with_typing_effect(YELLOW + "Loading, Please Wait", 0.01)
  
    result = subprocess.run(["ping", "-c", "1", hostname], capture_output=True, text=True)

    ip_address = re.search(r'(\d+\.\d+\.\d+\.\d+)', result.stdout)

    if ip_address:
        print_with_typing_effect(RESET + "The IP Address Of The Site Is " + ip_address.group(0))
    else:
        print_with_typing_effect(YELLOW + "Loading, Please Wait", 0.01) 

        print_with_typing_effect(RED + "ERROR, IP Address Not Found")

    input(BLUE + "\nPress Enter To Return To The Main Menu...") 
    clear_screen()
    main()



def github_mail():
    usr = input('Enter account pseudo: ')
    api_url_base = f"https://api.github.com/users/{usr}/events/public"

    response = requests.get(api_url_base)
    if response.status_code == 200:
        data = response.json()
        emails = []
       
        for event in data:
            if 'payload' in event and 'commits' in event['payload']:
                for commit in event['payload']['commits']:
                    if 'author' in commit and 'email' in commit['author']:
                        emails.append(commit['author']['email'])
       
        if emails:
            print("Email Found :")
            for email in set(emails):  
                print(email)
        else:
            print("No Email Found.")
    else:
        print('Error fetching data')

    input("Press Enter to return to the main menu...")
    os.system('cls' if os.name == 'nt' else 'clear')
    clear_screen()
    main()


def generate_nitro_code():
    """Generates a random Nitro code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def verify_nitro_codes():
    print_with_typing_effect(PURPLE + "********************** Welcome To Discord Nitro Finder **********************\n****************************************************************************""" + RESET)
    
    num = input("How many codes do you want to generate and verify? ")

    try:
        num = int(num)
    except ValueError:
        print(RED + "ERROR: Please enter a valid number." + RESET)
        time.sleep(1)
        clear_screen()
        main()

    if num <= 0:
        print(RED + "ERROR: Please enter a number greater than zero." + RESET)
        time.sleep(1)
        clear_screen()
        main()

    valid_codes = []
    file_name = "Nitro_Codes.txt"
    with open(file_name, "w", encoding='utf-8') as f:
        for _ in range(num):
            nitro_code = generate_nitro_code()
            url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro_code}?with_application=false&with_subscription_plan=true"
            gift_link = f"https://discord.gift/{nitro_code}"

            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(GREEN + " VALID | {}".format(gift_link))
                    valid_codes.append(nitro_code)
                    f.write(f"{gift_link} | VALID\n")
                else:
                    print(BLUE + " INVALID | {} | {}".format(gift_link, nitro_code))
                    f.write(f"{gift_link} | INVALID\n")
            except requests.RequestException as e:
                print("Error during the request: {}".format(e))
                f.write(f"{gift_link} | REQUEST ERROR\n")

    if valid_codes:
        print(f"{len(valid_codes)} valid Nitro codes saved in '{file_name}'.")
    else:
        print("No valid codes found.")
        os.remove(file_name)

    input(BLUE + "\nPress Enter to return to the main menu...")
    clear_screen()
    main()





if __name__ == '__main__':
    main()