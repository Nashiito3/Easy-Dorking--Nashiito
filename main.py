# doxxing tool google dorks based

import os
import datetime
from colorama import Fore
import dorks 
from simple_term_menu import TerminalMenu

print("\nThis tool has been coded by 0xStevenson")

print("\nProgram started at: " + str(datetime.datetime.now()))

print("\nIM NOT RESPONSABLE OF THE USES OF THIS TOOL. IT HAS BEEN MADE WITH EDUCATIONAL PURPOSES")

main_menu = ["[a] Custom google search", "[b] Gmail Dork", "[c] FTP Host", "[d] FTP Index Host", "[e] Camera Access", "[f] Camera Live Access", "[g] Password Pastebin Lookup", "[h] Admin passwords in .txt and similars", "[i] Sensitive passwords logs", "[j] Google Dorks Commands","[k] Google Hacking Database", "[q] quit"]

loop = True

while loop:
    choice = main_menu[TerminalMenu(main_menu).show()]

    if choice == Fore.GREEN + "[a] Custom google search":
        dorks.CustomLookup(self)

    elif choice == Fore.GREEN + "[b] Gmail Dork":
        dorks.Gmail(self)

    elif choice == Fore.GREEN +  "[c] FTP Host":
        dorks.FTP(self)

    elif choice == Fore.GREEN +  "[d] FTP Index Host":
        dorks.CFTP(self)
    
    elif choice == Fore.GREEN +  "[e] Camera Access":
        dorks.camera(self)

    elif choice == Fore.GREEN +  "[f] Camera Live Access":
        dorks.LiveCam(self)

    elif choice == Fore.GREEN +  "[g] Password Pastebin Lookup":
        dorks.Pass(self)

    elif choice == Fore.GREEN +  "[h] Admin passwords in .txt and similars":
        dorks.ExPass(self)

    elif choice == Fore.GREEN +  "[i] Sensitive passwords logs":
        dorks.Mpass(self)

    elif choice == Fore.GREEN + "[j] Google Dorks Commands":
        dorks.Commands(self)

    elif choice == Fore.GREEN +  "[k] Google Hacking Database":
        dorks.GoogleHackingDB(self)

    elif choice == Fore.RED +  "[q] quit":
        loop = False




