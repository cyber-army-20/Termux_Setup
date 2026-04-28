"""
Author :- Cyber Army
GitHub :- https://github.com/cyber-army-20
Facebook :- https://www.facebook.com/profile.php?id=61555946427371
Contact :- https://t.me/Cyber_Army_Chat_Bot
Through us, you can create 
all the Termux commands 
in your name or that 
of your group :- https://github.com/cyber-army-20/Termux_Command_Making
"""
#------------------------------- module  -----------------------------------------#
import os


#------------------------------- clear  -----------------------------------------#
def clear():
    os.system("clear")
#------------------------------- setup -----------------------------------------#
def main():
    clear()
    print (f'Allow the Button For Access the Storage in Termux')
    os.system("termux-setup-storage")
    os.system("termux-setup-storage -y")
    os.system("pkg update -y")
    os.system('pkg upgrade -y')
    install_pkg()
    install_module()
    time.sleep(1)
    print(f"All Setup Successful.")
#------------------------------- install PKG -----------------------------------------#
def install_pkg():
    print(f"Installing PKGs")
    for pkg in pkgs:
        os.system(f"pkg install {pkg} -y")
    print(f"All Pkg Install Successful")
#------------------------------- install module -----------------------------------------#
def install_module():
    print(f"Installing Modules")
    for module in modules:
        os.systen(f"pip install {module}")
    print(f"All Module Install Successful")

#------------------------------- last  -----------------------------------------#
if (__name__ == "__main__"):
    os.system("xdg-open https://t.me/Cyber_Army_Backup1")
    pkgs=["php","openssh","curl","figlet","nmap","java","ruby","zip","unzip","wget","tor","python2","espeak","rust","tur-repo"]
    modules=["bs4","faker","mechanize","httpx","requests","rich","Flask","fake_email","pyzipper","hashlib","bcrypt","httplib2","pycurl","user_agent","smtplib"]
    main()




