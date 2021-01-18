import webbrowser
import os
from ipaddress import ip_address
from whatsmyip.ip import get_ip
from whatsmyip.providers import GoogleDnsProvider
print("Pleas Install *whatsmyip* module using this command ==> pip install whatsmyip")
uname = os.getlogin()
print ("<=="+uname+"==>"+"Welcome In Sequretek")

print ("Your Public IP is ==>"+ get_ip(GoogleDnsProvider))

def IPAddress(IP: str) -> str: 
    return "This IP is ==> Private" if (ip_address(IP).is_private) else "This IP is ==> Public"

print("Insert URL To Check")
url = input(int())

if __name__ == '__main__' :  
   
    # Public IP 
    print(IPAddress(url))
    
url_2 = ["https://www.abuseipdb.com/check/","https://talosintelligence.com/reputation_center/lookup?search=","https://www.ipqualityscore.com/ip-reputation-check/lookup/",
         "https://www.ipligence.com/ip-address?ip="]
#for link in url_2:
    #webbrowser.open_new_tab(link+url)

print ("Done")
