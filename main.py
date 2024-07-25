import network
import time

def scan_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    print("Scanning for networks...")
    networks = wlan.scan()
    
    for net in networks:
        ssid = net[0].decode('utf-8')
        bssid = net[1]
        channel = net[2]
        RSSI = net[3]
        authmode = net[4]
        hidden = net[5]
        
        print("SSID:", ssid)
        print("BSSID:", ':'.join('%02x' % b for b in bssid))
        print("Channel:", channel)
        print("RSSI:", RSSI)
        print("Authmode:", authmode)
        print("Hidden:", hidden)
        print("")
    
    wlan.active(False)

# Run the scan
scan_wifi()

