import os
import json
import platform
import subprocess
import time
from time import sleep
import sys

JAUNE = "\033[33m"
ROUGE = "\033[31m"
VERT = "\033[32m"
BLEU = "\033[34m"
RESET = "\033[0m"


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_with_typing_effect(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

def cd():
    def getmodules():
        with open(os.path.join(os.path.dirname(__file__), 'json/startup.json')) as f:
            return json.load(f)['modules']

    print_with_typing_effect(JAUNE + "Checking dependencies..." + RESET)

    dependencies = getmodules()

    def check_dependencies():
        missing_dependencies = []
        for dependency in dependencies:
            try:
                __import__(dependency)
            except ImportError:
                print_with_typing_effect(f"{ROUGE}{dependency} is not installed.{RESET}")
                missing_dependencies.append(dependency)

        return missing_dependencies

    sleep(1.5)

    missing_dependencies = check_dependencies()

    if missing_dependencies:
        for dependency in missing_dependencies:
            print_with_typing_effect(f"Installing {dependency}...")
            sleep(1)
            try:
                if platform.system() == 'Windows':
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])
                else:
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])
                print_with_typing_effect(f"{VERT}Successfully installed {dependency}.{RESET}")
            except subprocess.CalledProcessError:
                print_with_typing_effect(f"{ROUGE}Failed to install {dependency}.{RESET}")
            input("press enter to access the Skyzz-Tool...")
            pass
    else:
        clear_screen()
        print_with_typing_effect(f"{BLEU}All dependencies are already installed.{RESET}")
        time.sleep(2)
        pass

if __name__ == "__main__":
    cd()
