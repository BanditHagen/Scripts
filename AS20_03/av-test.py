#!/usr/bin/env python3
import platform
import sys
import time

#  EICAR-testfile contains a string that will trigger antivirus software. String is harmless and safe to use for testing.
def virus_testfile():
    eicar_str = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"  # EICAR test string
    with open("eicar_testfile.txt", "w") as file_output:  # Create a file to write the EICAR test string
        file_output.write(eicar_str)  # Write the EICAR test string to the file
    print("[EICAR test file created]")

def clear_screen(time_delay):  # Function to clear the console screen after a delay
    time.sleep(time_delay)
    print("\033c")

def banner_intro(width,text):   # Function to display a banner with specified width and text
    print(f"=" * width, f"=={text}==", "=" * width, sep="\n")
    
def warning(input): # Function to handle user confirmation
    if input.lower() in ['y', 'yes']:
        print("[Authorization confirmed]")
        return True
    else:
        print("[Authorization Denied]")
        return False

eicar_str = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"  # EICAR test string that should match the one in the file. String is harmless and safe to use for testing.

if __name__ == "__main__": 
    banner_intro(29,"#Booting antivirus test#")
    clear_screen(2)  # Clear the console screen

    if platform.system() == "Windows":  # Check if the OS is Windows, if not terminate the script
        sys.exit(f"[WARNING]: Script is intended for Windows OS only.\n[Current OS]: {platform.version()}\nTerminating Script.")
        
    else:
        banner_intro(23,"OS Checkup Complete")
        clear_screen(2)  # Clear the console screen
    
    # Display warning message to the user
    print("[WARNING]: This action may trigger your antivirus software. Do not proceed in a production environment with central logging or monitoring without proper authorization!.\n**Verification of antivirus functionality will be performed by creating and attempting to read an EICAR test file.**\n")
    print(f"[Current OS]: {platform.version()}")    # Display the current OS version
    if warning(input("Do you wish to proceed? (y/n): ")):  # Prompt user for confirmation
        
        clear_screen(2)  # Clear the console screen
        banner_intro(30,"#Creating EICAR test file#")
        
        try:    # Attempt to create the EICAR test file
            time.sleep(2)
            virus_testfile()
            clear_screen(3)  # Clear the console screen
            
            try:    # Attempt to read the EICAR test file
                with open("eicar_testfile.txt", "r") as f:
                    content = f.read()  # Read the content of the file
                    if content == eicar_str:    # Verify if the content matches the EICAR test string, if found antivirus is not working as expected.
                        print("[EICAR test file verified]")
                        clear_screen(3)
                        banner_intro(34,"Antivirus malfunction detected")
                        time.sleep(2)
                        sys.exit("[WARNING]: Testfile did not trigger\nantivirus properly.\nPlease check your settings.")
                    else:  # If file found but content does not match, file may have been modified or altered.
                        sys.exit("[EICAR test file mismatch]\nFile has been modified or altered.\nTerminating script.")

            except FileNotFoundError:   # Handle case where file is not found = Antivirus is working as expected, terminate script.
                print("[EICAR test file not found]")
                clear_screen(3)
                banner_intro(29,"Antivirus Action Detected")
                time.sleep(2)
                print("Antivirus is functioning properly.")
                sys.exit("Terminating script.")

        except Exception as e:  # Handle any exceptions that occur during file creation, print error and terminate script.
            print(f"An error occurred: {e}")
            time.sleep(2)
            sys.exit("Script terminated.")

    else:   # User opted not to proceed, terminate script.
        clear_screen(2)
        sys.exit("Script terminated.")
