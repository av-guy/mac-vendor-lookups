from scapy.all import srp, Ether, ARP
from mac_vendor_lookup import MacLookup

mac_lookup = MacLookup()
subnet = "192.168.1.0/24"


def show_mac_vendor(s, r):
    mac, ip = r.sprintf("%Ether.src% %ARP.psrc%").split()
    vendor = 'Not Defined'
    try:
        vendor = mac_lookup.lookup(mac.upper())
    except KeyError as e:
        pass
    if 'Observint' in vendor:
        return f'{vendor} - {mac} - {ip}'
    return None
        

if __name__ == "__main__":
    answers, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=subnet), timeout=2, verbose=True, iface="Ethernet")
    print(_, 'is unanswered')
    print(answers, 'is answers')
    answers.summary(lambda s, r: show_mac_vendor(s, r))
