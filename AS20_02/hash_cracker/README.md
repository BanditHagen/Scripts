Description:
Script that runs hashcat with configuration to decrypt MD5 hashes.

use:
"./hash_cracker.sh [file.txt] [mask]" to run from Linux terminal.
provide [file.txt] and [mask]("?d" for each number in "password")

Example: ./hash_cracker.sh file.txt ?d?d?d?d?d?d?d?d
= checks hashes stored in "file.txt" where passwords consists of 8 numerics.   
