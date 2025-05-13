#!/usr/bin/env python3
import subprocess
import requests
from bs4 import BeautifulSoup

def nmap_scan(target):
    # Run nmap to find web servers
    result = subprocess.run(['nmap', '-p80,443,8080,8443', '-sV', target], 
                          capture_output=True, text=True)
    return result.stdout

def crawl_website(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        forms = soup.find_all('form')
        logins = [f for f in forms if 'login' in str(f).lower()]
        return logins
    except:
        return []

def test_sqli(url, form):
    # Implement SQLi testing logic
    pass

def brute_force_ssh(host):
    # Implement SSH brute force with hydra or similar
    pass

def main():
    target = input("Enter target IP/host: ")
    scan_results = nmap_scan(target)
    
    if 'http' in scan_results.lower():
        print("[+] Web server detected")
        login_forms = crawl_website(f"http://{target}")
        
        if login_forms:
            print("[+] Login forms found")
            for form in login_forms:
                test_sqli(f"http://{target}", form)
    
    if 'ssh' in scan_results.lower():
        print("[+] SSH service detected")
        brute_force_ssh(target)

if __name__ == "__main__":
    main()
