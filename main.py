# -*- coding: utf-8 -*-

# SETUP MONITOR MODE:
# http://pharos.ece.utexas.edu/wiki/index.php/How_to_Measure_the_Received_Signal_Strength_of_WiFi_Beacons

# sudo iw phy phy1 interface add moni0 type monitor
# sudo ifconfig moni0 up

import fileinput

def find_channel(line):
    mhz = "MHz"
    channel = line.find(mhz.upper())
    if(channel >= 0):
        return line[channel-5:channel-1]
    return ""

def get_rss(line):
    db = "dB"
    rss_exists = line.find(db.upper())
    if(rss_exists >= 0):
        return line[rss_exists-3:rss_exists+len(db)]
    return ""

def find_probe(line):
    probe = "Probe"
    probe_req = line.find(probe.upper())
    if(probe_req >= 0):
        return True
    return False

def find_probe_request(line):
    probe = "Probe Request"
    probe_req = line.find(probe.upper())
    if(probe_req >= 0):
        return True
    return False

def find_mac_source(line, mac):
    source = "SA:" + mac
    mac_exists = line.find(source)
    if(mac_exists >= 0):
        return True
    return False 

def get_mac_source(line):
    mac_length = 20
    mac_source = line.find("SA:")
    if(mac_source >= 0):
        return line[mac_source:mac_source+mac_length]
    return ""

def get_mac_destination(line):
    mac_length = 20
    mac_source = line.find("DA:")
    if(mac_source >= 0):
        return line[mac_source:mac_source+mac_length]
    return ""


def print_data(line):
    data = line.split(" ")
    date = data[0]
    time = data[1]
    
    rss = get_rss(line)
    mac_source = get_mac_source(line)
    mac_dest = get_mac_destination(line)
    
    print(date + " " + time + " " + rss + " " + mac_source + " " + mac_dest)

def main():
    
    target_mac = "2C:54:CF:FB:4C:C8"
    #target_mac = "C4:0A:CB:5C:25:41"

    try:
        while(True):
            for line in fileinput.input():
                l = line.upper()
                if(find_mac_source(l, target_mac)):
                    print_data(l)
    except KeyboardInterrupt:
        print("Program stopped by user")

main();
