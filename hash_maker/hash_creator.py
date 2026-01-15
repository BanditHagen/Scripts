#!/usr/bin/env python3

"""
=== Password and Hash Generator ===
Generates random numeric passwords based on user input and calculates their MD5 hashes.
"""

import time
import random
import hashlib

def generate_random_number_string():
    
    # Använder random.choice för att välja siffror (hyfasd randomisering)
    # Skapar en någorlunda enhetlig fördelning över alla möjliga 10-siffriga kombinationer
    return ''.join(random.choice("0123456789") for X in range(PWD_LGT))

def md5_hash(text):
    # encode() konverterar sträng till bytes, vilket krävs av hashlib
    # hexdigest() returnerar hash-värdet som en hexadecimal sträng
    return hashlib.md5(text.encode()).hexdigest()

def main():
    """
    Main function starts here.
    """
    # printas när input är mottagen:
    print("=" * 65)
    print(f"\t\t===| MD5 Hash Generator |===")
    print("=" * 65)
    print(f"Created {NO_PASS} randomized {PWD_LGT}-numbered MD5 hashes:\n")
    
    # Generera och visa lösenorden med deras hash-värden
    for i in range(NO_PASS):
        # Generera ett slumpmässigt lösenord med fast längd
        password = generate_random_number_string()
        
        # Beräkna MD5-hashen för lösenordet
        hash_value = md5_hash(password)
        
        # Formatera och visa resultatet med sekventiell numrering
        print(f"{i+1:2d}. Password: {password}  →  MD5: {hash_value}")
    
    # Säkerhetsvarning påpekar att MD5 är osäkert.
    print("\n" + "=" * 65)
    print(f"⚠️  MD5 encryption should not be used for secure applications.")
    print("=" * 65)

# Användarinmatning för lösenordslängd och antal lösenord + design
print(f":" * 40)
print(f"Provide input to start generating")
print(f":" * 40, end="\n")
PWD_LGT = int(input(f"Provide lenght of password in integer → "))  # Längd på lösenordet efterfrågas.
NO_PASS = int(input(f"Privide number of passwords in integer → ")) # antal lösen att genereras efterfrågas.

# Standard Python idiom för att kontrollera om skriptet körs direkt.
if __name__ == "__main__":
    main()
