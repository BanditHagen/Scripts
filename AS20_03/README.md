**Antivirus Test**

This script is designed to test antivirus on Windows OS.

**Function**

When script is run and authorized, a testfile will be created in current folder containing a string designed to trigger antivirus software.
(String is harmless and made solely for triggering)

**Requirements:**

- Windows OS
- Antivirus software, ex Windows Defender
- Authorization if needed

**Disclosure**

This script may trigger your antivirus software. Do not proceed in a production environment with central logging, monitoring or active XDR without proper authorization! Ignoring this could result in alarm triggering, blockage or SOC/NOC notifications.

**Script Flow**

1. Check if OS is Windows
   - If NO: Exit with error message
   - If YES: Continue

2. Show banner and warning message

3. Request user authorization
   - If NO: Exit (denied)
   - If YES: Continue

4. Create EICAR test file

5. Wait 2-3 seconds for antivirus response

6. Try to read the file back
   - If FileNotFoundError: SUCCESS (AV detected and removed it)
   - If file exists with matching content: FAILURE (AV not detecting)

7. Report result and exit

**Usage**

On Windows, run the script with Python:

```cmd
python av-test.py
```

Or in PowerShell:

```powershell
python av-test.py
```

**Expected Output**

- If antivirus is working: File is detected and removed, script reports success
- If antivirus is not working: File remains, script reports malfunction
