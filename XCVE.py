import urllib.request
import urllib.error
import re

XVSIN = input("\n#  SEARCH (XAMFRA) : ")
print("""    ╔═══════════════╗\n    ║     RESULT    ║\n    ╚═══════════════╝\n""")
XVSINP = XVSIN.replace(" ", "+")
CVSURL = 'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword='+XVSINP
REQCVE = urllib.request.Request(CVSURL)
REQCVE.add_header('User-Agent', 'Mozilla/7000.0 XAMFRA')
REQCVE.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
REQCVE.add_header('Accept-Language', 'en-US,en;q=0.8')
REQTCV = urllib.request.urlopen(REQCVE, timeout=10)
CVRESP = REQTCV.read()
REQTCV.close()
CVEID = re.findall('<a href="/cgi-bin/cvename.cgi\?name=(.*?)">', str(CVRESP))
CVEDE = re.findall('<td valign="top">(.*?)</td>', str(CVRESP))
for XCVE in range(len(CVEID)):
  print(str("[+] "+CVEID[XCVE]+" \n\nDescription:\n\n"+CVEDE[XCVE]+"\n\n------------------------------\n\n"))