import subprocess
# This script is only designed for use with Windows Command Prompt and is incompatible with other shells and operating systems

def network_diagnostics(): # Run basic network diagnostics
    print("\nNetwork diagnostics")
    
    # Ping test to check internet connectivity
    print("\n[1] Testing internet connectivity...")
    result = subprocess.run(['ping', '-n', '4', '8.8.8.8'], capture_output=True, text=True)
    print(result.stdout or result.stderr)
    
    # Check local network configuration
    print("\n[2] Checking local network connection...")
    try:
        ipconfig = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True)
        print(ipconfig.stdout)
    except Exception as e:
        print(f"Error: {e}")
    
    
    # DNS resolution test with nslookup
    print("\n[3] Testing DNS resolution...")
    try:
        nslookup = subprocess.run(['nslookup', 'google.com'], capture_output=True, text=True)
        print(nslookup.stdout)
    except Exception as e:
        print(f"DNS error: {e}")
    
def system_info(): # Display basic system information
    print("\n=== System information ===")
    try:
        print("\n[System info]")
        subprocess.run(['systeminfo'], shell=True)

        print("\n[Disk info]")
        subprocess.run(['wmic', 'diskdrive', 'get', 'size,model,status'], shell=True)

        print("\n[Windows updates]")
        subprocess.run(['wmic', 'qfe', 'list', 'brief'], shell=True)
    except Exception as e:
        print(f"Error gathering system info: {e}")

def quick_fixes(): # Suggest common quick fixes
    print("\nCommon quick fixes")
    print("1. Restart the computer")
    print("2. Check all cables and connections")
    print("3. Verify power supply to all peripherals")
    print("4. Try a different browser/application")
    print("5. Clear browser cache (Ctrl+Shift+Delete)")
    print("6. Check for operating system updates")
    print("7. Check for driver updates")

def main_menu(): # Display the main menu
    print("Basic Windows Diagnostic Toolkit")
    print("\n1. Network diagnostics")
    print("\n2. System information")
    print("\n3. Common quick fixes")
    print("\n4. Exit")
    
    choice = input("\nEnter your choice, from 1 to 4: ")
    return choice

def main():
    while True:
        choice = main_menu()
        match choice: # Handle user menu selection
            case '1':
                network_diagnostics()
            case '2':
                system_info()
            case '3':
                quick_fixes()
            case '4':
                print("\nClosing diagnostic toolkit...")
                break
            case _:
                print("\nInvalid input, please try again.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()