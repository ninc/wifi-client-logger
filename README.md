# wifi-client-logger
Picking up RSS and MAC addresses of wifi trafic using tcpdump and a TP-LINK TL-WN722N wifi adapter.

##Setup the adapter for use:
See for more info: http://pharos.ece.utexas.edu/wiki/index.php/How_to_Measure_the_Received_Signal_Strength_of_WiFi_Beacons

####Setup adapter in monitor mode
$ sudo iw phy phy0 interface add moni0 type monitor
$ sudo ifconfig moni0 up

####Use tcpdump to log signal data
$ sudo tcpdump -n -e -tttt -vvv -i moni0 -s 0 -w moni0.dump "link[0] == 0x80"

Parse the result with the wifi-client-logger

$ sudo tcpdump -nettvvv -s 0 -r moni0.dump | python main.py

####Tear down adapter
$ sudo iw dev moni0 del


#TODO
1. Make sure the data can be captured live
2. Port to raspberry pi
