"""                                                  ╔════════╗
                                                     ║EGYPTIAN║
                                                     ╚║║║║║║║║╝
╔════════════════════╗  //////\
║~  Google Search Py ║ ║/////  \
║~  copyright © 2021 ║//////    \
║~  Auther : XAR     ║║║║║║║ ╔╗ ║              _Version_ 1.0.0
║~  Contact With US  ╚╚╚╚╚╚╚═╝╚═╝═════════════════════════════╗
║~  Discord: https://discord.gg/kz4Y5fa9x9                    ║
║~  https://www.youtube.com/channel/UCwJLxZbiR1tT0OikfAHAk1Q  ║
╚═════════════════════════════════════════════════════════════╝

Pro
"""
import urllib.request
import urllib.error
import re
import os

# Project Data
__author__      = "AhmedAbdelaziz.Reda"
__copyright__   = "Copyright 2020-2021"
__version__     = "2.0.0"

class XCVE:
	def __init__(XAMFRA):
		XAMFRA.__author__      = "AhmedAbdelaziz.Reda"
		XAMFRA.__copyright__   = "Copyright 2020-2021"
		XAMFRA.__version__     = "2.0.0"

	def XXCLS(XAMFRA):     # TO CLEAR THE SCREEN
		os.system('cls' if os.name=='nt' else 'clear')
	
	def XCVE(XAMFRA): # MAIN FUNCTION
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

	def XCAB(XAMFRA):
		print("""
 ########################### ABOUT US ############################
 #                                                               #
 # [1][WE LOVE TO GO DEEP IN ANY THING ]                         #
 # [2][WE THINK BEFORE HOW TO HACK SOMETHING HOW IT WORKS]       #
 #                                                               #
 # <WE FOCUS TO GET ANY NEW INFORMATION IN CYBER SECURITY FIELD> #
 # <AND MAKE THE COMMUNITY HAVE KNOWLEDGE ABOUT ALL THESE THINGS>#
 #                                                               #
 # Discord: discord.gg/kz4Y5fa9x9                                #
 #                                                               #
 *****************************************************************
""")
	def XCBA(XAMFRA):
		print("""
 ##################################
 #   TOOL FOR SEARCH ABOUT CVE    #
 #       --- OPTION ----          #
 #   A   #-----> About Us         #
 #   B   #-----> Show Banner      #
 #   C   #-----> CLEAR SCREEN     #
 #   S   #-----> SEARCH ABOUT CVE #
 ##################################
""")
#===============================================================================================

if __name__ == '__main__':
	XCSC = XCVE()
	XCSC.XXCLS()
	print("""
 ##################################
 #   TOOL FOR SEARCH ABOUT CVE    #
 #       --- OPTION ----          #
 #   A   #-----> About Us         #
 #   B   #-----> Show Banner      #
 #   C   #-----> CLEAR SCREEN     #
 #   S   #-----> SEARCH ABOUT CVE #
 ##################################
""")
	while True:
		XCOMMANDER = input("\n XCVE #>")
		if XCOMMANDER == "A" or XCOMMANDER == "a":
			XCSC.XCAB()
		elif XCOMMANDER == "B" or XCOMMANDER == "b":
			XCSC.XCBA()
		elif XCOMMANDER == "C" or XCOMMANDER == "c":
			XCSC.XXCLS()
		elif XCOMMANDER == "S" or XCOMMANDER == "s":
			XCSC.XCVE()
		else:
			print("\n# can't To Understand This command .\n# IF you Can to contact with us and\n# tell us about this error.\n#\n# Discord: discord.gg/kz4Y5fa9x9\n")
