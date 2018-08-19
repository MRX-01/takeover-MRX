import requests
import argparse
import re
import os

RED = "\033[1;31m"
GREEN = "\033[1;32;0m"
OKBLUE = "\033[94m"
WHITE = "\033[0;37m"

parser = argparse.ArgumentParser(description="Subdomain Takeover Scanner")
parser.add_argument(
	'-l',
	'--list',
	default='',
	help='python3 subdomain.py [-l, --list] file contain list of domains'
)

args = parser.parse_args()
domainList = args.list

print("""
MMMMMMMM               MMMMMMMM                 RRRRRRRRRRRRRRRRR                    XXXXXXX       XXXXXXX
M:::::::M             M:::::::M                 R::::::::::::::::R                   X:::::X       X:::::X
M::::::::M           M::::::::M                 R::::::RRRRRR:::::R                  X:::::X       X:::::X
M:::::::::M         M:::::::::M                 RR:::::R     R:::::R                 X::::::X     X::::::X
M::::::::::M       M::::::::::M                   R::::R     R:::::R                 XXX:::::X   X:::::XXX
M:::::::::::M     M:::::::::::M                   R::::R     R:::::R                    X:::::X X:::::X
M:::::::M::::M   M::::M:::::::M                   R::::RRRRRR:::::R                      X:::::X:::::X
M::::::M M::::M M::::M M::::::M ---------------   R:::::::::::::RR   ---------------      X:::::::::X
M::::::M  M::::M::::M  M::::::M -:::::::::::::-   R::::RRRRRR:::::R  -:::::::::::::-      X:::::::::X
M::::::M   M:::::::M   M::::::M ---------------   R::::R     R:::::R ---------------     X:::::X:::::X
M::::::M    M:::::M    M::::::M                   R::::R     R:::::R                    X:::::X X:::::X
M::::::M     MMMMM     M::::::M                   R::::R     R:::::R                 XXX:::::X   X:::::XXX
M::::::M               M::::::M                 RR:::::R     R:::::R                 X::::::X     X::::::X
M::::::M               M::::::M                 R::::::R     R:::::R                 X:::::X       X:::::X
M::::::M               M::::::M                 R::::::R     R:::::R                 X:::::X       X:::::X
MMMMMMMM               MMMMMMMM                 RRRRRRRR     RRRRRRR                 XXXXXXX       XXXXXXX

                |--------------------------------------------------------------------|
                |    coded by Hazem Hisham                                           |
                |    FB account <<>> https://www.facebook.com/human.script.01 <<>>   |
                |    date 8/18/2018                                                  |
                |    github <<>> https://github.com/MRX-01 <<>>                      |
                |--------------------------------------------------------------------|
 
""")

if len(str(domainList)) > 0:
	if os.path.isfile(domainList):
		readWords = open(domainList, 'r')

	else:
		exit("{}File Not Found Unable To Load Targets".format(RED))	
	
	print("{}[+] Loading Targets.... [+]\033[94m\n".format(WHITE))			
	subdomainList = []
	vuln = []
	valid= []	
	validUrls = open('not-vulnerble.txt', 'a')
	Takeover = open('subdomain-Vulnerable.txt', 'a')

	for words in readWords:
		if not words.isspace():
			words = words.rstrip()
			words = words.replace("https://", "")
			words = words.replace("http://", "")
			words = words.replace("https://www.", "")
			words = words.replace("http://www.", "")
			words = words.replace("/", "")
			words = "http://{}".format(words)
			subdomainList.append(words)
			validUrls.write("{}\n".format(words))
	
	validUrls.close()
	readWords.close()

	if len(subdomainList) > 0:
		print(WHITE,"\n[!] Total {} Targets Loaded wait..[!]\033[94m".format(len(subdomainList)))
		print("{}[!] Checking For Subdomain Takeover..... [!]\n\033[94m".format(WHITE))
		
		VulnContents = ["<strong>Trying to access your account", "Use a personal domain name", "The request could not be satisfied", "Sorry, We Couldn't Find That Page", "Fastly error: unknown domain","The feed has not been found", "You can claim it now at", "Publishing platform","There isn't a GitHub Pages site here","No settings were found for this company","Heroku | No such app", "<title>No such app</title>","You've Discovered A Missing Link. Our Apologies!", "Sorry, couldn&rsquo;t find the status page","NoSuchBucket","Sorry, this shop is currently unavailable","<title>Hosted Status Pages for Your Company</title>", "data-html-name=\"Header Logo Link\"","<title>Oops - We didn't find your site.</title>","class=\"MarketplaceHeader__tictailLogo\"","Whatever you were looking for doesn't currently exist at this address", "The requested URL was not found on this server", "The page you have requested does not exist", "This UserVoice subdomain is currently available!", "but is not configured for an account on our platform", "<title>Help Center Closed | Zendesk</title>", "Sorry, We Couldn't Find That Page Please try again"]

		for domain in subdomainList:
			print("{}[-] Checking {} [-]\033[94m".format(WHITE, domain))		
			try:
				subDoamin = requests.get("{}".format(domain.rstrip()), timeout=5).text
				for VulnContent in VulnContents:
					if VulnContent in subDoamin:
						print("{}    Good news : Vulnerable {}\033[94m <-----<<<\n".format(GREEN, domain))
						vuln.append(domain)
						valid.append(domain)
						Takeover.write("{}\n".format(domain))

				if not domain in vuln:
					print("{}  -- Not Vulnerable {}\033[94m --\n".format(OKBLUE, domain))
					valid.append(domain)
					
			except:
					print(RED,"!! Timeout => {}\033[94m \n".format(domain.rstrip()))			
		

		print("\n".join(valid))
		Takeover.close()				
else:
    print('''
-h && --help
-l && --list
''')
