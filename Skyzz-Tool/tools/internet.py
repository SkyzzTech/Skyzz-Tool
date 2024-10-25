import os
import sys
from time import sleep
import time

JAUNE = "\033[33m"
ROUGE = "\033[31m"
VERT = "\033[32m"
RESET = "\033[0m"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_with_typing_effect(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

def ci():
    try:
        result = os.system("ping -c 1 google.com > /dev/null 2>&1" if os.name != 'nt' else "ping -n 1 google.com > NUL 2>&1")
        return result == 0
    except:
        return False
    
if not ci():
    print_with_typing_effect(f"{ROUGE}No internet connection detected. Please check your connection{RESET}")
    time.sleep(3)
    sys.exit(1)
else:
    clear_screen()
    sleep(0.5)
    print_with_typing_effect(f"{VERT}Internet connection found!{RESET}")
    sleep(0.5)
    print_with_typing_effect("Please wait...")
    sleep(2)
    clear_screen()

if __name__ == "__main__":
    ci()
