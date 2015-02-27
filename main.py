# -*- coding: utf-8 -*-


# SETUP MONITOR MODE:
# http://pharos.ece.utexas.edu/wiki/index.php/How_to_Measure_the_Received_Signal_Strength_of_WiFi_Beacons

# sudo iw phy phy1 interface add moni0 type monitor
# sudo ifconfig moni0 up

import fileinput



# 2015-02-27 16:35:44.828071 380232742us tsft 1.0 Mb/s 2412 MHz 11g -53dB signal [bit 29] Retry 314us BSSID:00:22:b0:ab:d8:3a DA:44:74:6c:52:ab:e0 SA:00:22:b0:ab:d8:3a Probe Response (Stora Visatter) [1.0* 2.0* 5.5* 11.0* Mbit] CH: 6, PRIVACY


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
    
    ninc_g3_mac = "2C:54:CF:FB:4C:C8"

    try:
        while(True):
            for line in fileinput.input():
                l = line.upper()
                channel = find_channel(l)
                if(channel != "2412" and channel != ""):
                    print(channel)

                # if(find_mac_source(l, ninc_g3_mac)):
                    # print_data(l)
                    # print(l)
                   # return
    except KeyboardInterrupt:
        print("Program stopped by user")

main();
