import ipaddress as ip
import subprocess
import os 
import json
from dotenv import load_dotenv

def ping_ip(ip):
    """
    hihiih on ping les ip hihihihi
    """
    try: 
        output = subprocess.check_output(f"ping -n 1 -w 1 {ip}", stderr=subprocess.STDOUT, universal_newlines=True)
        return "TTL=" in output
    
    except subprocess.CalledProcessError:
        return False

def scan_network(network):
    """
    oulalala faudrait pas scanner ce villain reseau quand meme hihihi
    """
    return [str(ip) for ip in ip.IPv4Network(network) if ping_ip(str(ip))]

def main():
    """
    oupsie
    """
    load_dotenv()
    
    network = os.getenv("NETWORK_RANGE")
    active_ips = scan_network(network)
    ip_dict = {i + 1: ip for i, ip in enumerate(active_ips)}

    chemin = "results/real"
    if not os.path.exists(chemin):
        os.makedirs(chemin)
    with open(os.path.join(chemin, "ips.json"), "w") as f:
        json.dump(ip_dict, f, indent=4)

    print("Scan terminé")

if __name__ == "__main__":  
    main()