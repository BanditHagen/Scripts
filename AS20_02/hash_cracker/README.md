**Description:**

Script that runs hashcat with configuration to decrypt MD5 hashes.


**use:**

sudo chmod +x hash_cracker.sh

"./hash_cracker.sh [file.txt] [mask]"

provide [file.txt] and [mask]("?d" for each number in "password")



**Example:** 

./hash_cracker.sh file.txt ?d?d?d?d?d?d?d?d

Checks hashes stored in "file.txt" where passwords consists of 8 numerics.   



**Requirements:**

Linux

Hashcat installed
