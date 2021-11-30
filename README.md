# MAC Vendor Lookup

This script performs an ARP request and does a vendor lookup for each MAC address in the ARP table.
Windows users **MUST** have [Nmap](https://nmap.org/npcap/) or [Winpcap](https://www.winpcap.org/) installed
for this to work. Tested using Python 3.10 on Windows 10. Running this script inside of IDLE will produce
an error -- run the script from PowerShell or the command line instead.

## Setting Up

1. `` git clone https://github.com/av-guy/mac-vendor-lookups.git ``
2. `` cd mac-vendor-lookups ``
3. `` virtualenv venv ``
4. `` cd venv/Scripts/activate ``
5. `` pip install -r requirements.txt ``
6. `` python main.py ``

### Please Note

This is pre-programmed to scan the `192.168.1.0/24` subnet. You can modify this subnet by accessing
the `main.py` file and changing the subnet on line 5 to whatever you would like.