import sys
from tools.internet import ci
from tools.modules import cd

def check():
    # Check if 'ci' is available
    if not ci:
        print("ERROR") #if ci is not available exit
        sys.exit()

    # Check if 'cd' is available
    if not cd:
        print("ERROR") #if cd is not available exit
        sys.exit()
check()


