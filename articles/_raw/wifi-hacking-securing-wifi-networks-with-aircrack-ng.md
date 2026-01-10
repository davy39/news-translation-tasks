---
title: WiFi Hacking 101 – How to Secure Your Wifi Networks With Aircrack-NG
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-09-18T18:14:51.000Z'
originalURL: https://freecodecamp.org/news/wifi-hacking-securing-wifi-networks-with-aircrack-ng
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/wall.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: penetration testing
  slug: penetration-testing
- name: wifi
  slug: wifi
seo_title: null
seo_desc: 'Imagine a world without WiFi. We would still be using long wires of ethernet
  cables to connect to the internet.

  There is no debate about how much easier WiFi has made our lives. Now we can connect
  to the internet at coffee shops, subway stations, and...'
---

Imagine a world without WiFi. We would still be using long wires of ethernet cables to connect to the internet.

There is no debate about how much easier WiFi has made our lives. Now we can connect to the internet at coffee shops, subway stations, and almost anywhere we go.

However, WiFi is also a vulnerable network compared to the ethernet. Unless it is properly secured, it's easy to perform man-in-the-middle attacks using [tools like Wireshark](https://medium.com/manishmshiva/wireshark-a-walkthrough-of-the-best-packet-analyzer-in-the-world-9af0358ed9a1).

For example, if you are connected to a Starbucks network, anyone connected to that network can look at every other person’s network traffic. 

Unless you use a [VPN](https://us.norton.com/internetsecurity-privacy-what-is-a-vpn.html) or the website uses HTTPS, your data (including passwords and credit card details) will be visible to the entire network.

If you are working for a company, chances are they use a WiFi network, too. Have you wondered how secure it is? Do you know if someone in the parking lot is connected to your network and capturing your company’s confidential data?

With tools like Wireshark and Aircrack, you can perform security audits of your WiFi networks. While Wireshark can help you watch what is happening on your network, Aircrack is more of an offensive tool that lets you attack and gain access to WiFi networks.

Thinking like an attacker has always been the best way to defend against a network. By learning how to work with Aircrack, you will be able to understand the exact steps an attacker would take to gain access to your network. You can then perform security audits of your own network to make sure it is not vulnerable. 

> **_A quick sidenote: I am in no way encouraging the use of illegal offensive tools. This tutorial is purely educational and is meant to help you defend your networks better._**

Before we look at Aircrack in detail, here are a few terms you should know.

* **Access Point** — The WiFi network that you want to connect to.
* **SSID** — The name of the access point. For example, “Starbucks”.
* **Pcap file** — Packet capture file. Contains captured packets on a network. The common format for tools including Wireshark and Nessus.
* **Wired Equivalent Privacy (WEP)** — Security algorithm for wireless networks.
* **Wi-Fi Protected Access (WPA & WPA2)** — Stronger security algorithm compared to WEP.
* **IEEE 802.11** — [Wireless Local Area Network (LAN) protocol](https://en.wikipedia.org/wiki/IEEE_802.11).
* **Monitor mode** — Capturing the network packets in the air without connecting to a router or access point.

[I recently wrote a post on the top 100 terms you should know as a penetration tester](https://medium.com/manishmshiva/penetration-testing-100-terms-you-need-to-know-a723c38cd8c8). You can check it out if you are interested.

## What is Aircrack-NG?

Aircrack is a software suite that helps you attack and defend wireless networks. 

Aircrack is not a single tool, but a whole collection of tools, each of which performs a specific function. These tools include a detector, packet sniffer, WEP/WPA cracker, and so on.

The main purpose of Aircrack is to capture the packets and read the hashes out of them in order to crack the passwords. Aircrack supports almost all the latest wireless interfaces.

Aircrack is open-source, and can work on Linux, FreeBSD, macOS, OpenBSD, and Windows platforms.

The ‘NG’ in Aircrack-ng stands for “new generation”. Aircrack-ng is an updated version of an older tool called Aircrack. [Aircrack also comes pre-installed in Kali Linux](https://tools.kali.org/wireless-attacks/aircrack-ng).

### WiFi Adapter

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1.jpeg)

Before we start working with Aircrack, you will need a WiFi adapter. Aircrack only works with a wireless network interface controller whose driver supports raw monitoring mode and can sniff 802.11a, 802.11b, and 802.11g traffic.

Typical wifi adapters (usually built-in with your computer) don't have the ability to monitor traffic from other networks. You can only use them to connect to a WiFi access point.

With an Aircrack compatible wifi adapter, you can enable the ‘monitor mode’ with which you can sniff traffic from networks you are not connected to. You can then use that captured data to crack the password of that network.

[Check out the list of WiFi adapters that are compatible with Kali Linux here](https://www.kalilinux.in/2020/07/wifi-adapter-kali-linux-2020.html).

## Aircrack Tools

Now that you know what you can do with Aircrack, let’s look at each of its tools.

### Airmon-ng

Airmon-ng is a script that puts your network interface card into monitor mode. Once this is enabled, you should be able to capture network packets without needing to connect or authenticate with an access point.

You can use the command `airmon-ng` to list the network interfaces and `airmon-ng start <interface name>` to start an interface in monitor mode.

```
# airmon-ng start wlan0

  PID Name
  718 NetworkManager
  870 dhclient
 1104 avahi-daemon
 1105 avahi-daemon
 1115 wpa_supplicant

PHY	Interface	Driver		Chipset

phy0	wlan0		ath9k_htc	Atheros Communications, Inc. AR9271 802.11n
		(mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon)
		(mac80211 station mode vif disabled for [phy0]wlan0
```

In the above example, you can see that the network interface `wlan0` has been turned into `wlan0mon` — meaning the monitor mode has been enabled for it.

### Airodump-ng

Airodump-ng is a packet capture utility that captures and saves raw data packets for further analysis. If you have a GPS receiver connected to your computer, airodump-ng can fetch the coordinates of the access points as well.

After enabling monitor mode using airmon-ng, you can start capturing packets using airodump. Running the command `airodump-ng` will list the available access points. The ESSID (or SSID) is the name of the wireless network. 

```
# airodump-ng
CH  9 ][ Elapsed: 1 min ][ 2007-04-26 17:41 ][ WPA handshake: 00:14:6C:7E:40:80
                                                                                                            
 BSSID              PWR RXQ  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID
                                                                                                            
 00:09:5B:1C:AA:1D   11  16       10        0    0  11  54.  OPN              NETGEAR                         
 00:14:6C:7A:41:81   34 100       57       14    1   9  11e  WEP  WEP         bigbear 
 00:14:6C:7E:40:80   32 100      752       73    2   9  54   WPA  TKIP   PSK  teddy                             
                                                                                                            
 BSSID              STATION            PWR   Rate   Lost  Packets  Notes  Probes
                                
 00:14:6C:7A:41:81  00:0F:B5:32:31:31   51   36-24    2       14
 (not associated)   00:14:A4:3F:8D:13   19    0-0     0        4           mossy 
 00:14:6C:7A:41:81  00:0C:41:52:D1:D1   -1   36-36    0        5
 00:14:6C:7E:40:80  00:0F:B5:FD:FB:C2   35   54-54    0       99           teddy
```

### Aircrack-ng

Once you have captured enough packets using airodump-ng, you can crack the key using aircrack-ng. Aircrack uses statistical, brute force, and dictionary attacks to break the WEP / WPA key.

```
Aircrack-ng 1.4


                 [00:00:03] 230 keys tested (73.41 k/s)


                         KEY FOUND! [ biscotte ]


    Master Key     : CD D7 9A 5A CF B0 70 C7 E9 D1 02 3B 87 02 85 D6 
                     39 E4 30 B3 2F 31 AA 37 AC 82 5A 55 B5 55 24 EE 

    Transcient Key : 33 55 0B FC 4F 24 84 F4 9A 38 B3 D0 89 83 D2 49 
                     73 F9 DE 89 67 A6 6D 2B 8E 46 2C 07 47 6A CE 08 
                     AD FB 65 D6 13 A9 9F 2C 65 E4 A6 08 F2 5A 67 97 
                     D9 6F 76 5B 8C D3 DF 13 2F BC DA 6A 6E D9 62 CD 

    EAPOL HMAC     : 52 27 B8 3F 73 7C 45 A0 05 97 69 5C 30 78 60 BD

```

It is important to note that you need enough packets in order to crack the key. Also, aircrack-ng uses sophisticated algorithms to crack the keys from the network packets. 

If you are interested in learning more about how Aircrack does this, [this would be a good starting point](https://www.aircrack-ng.org/doku.php?id=aircrack-ng).

### Aireplay-ng

Aireplay-ng is used to create artificial traffic on a wireless network. Aireplay can either capture traffic from a live network or use the packets from an existing Pcap file to inject it into a network.

With aireplay-ng, you can perform attacks such as fake authentication, packet injection, caffe-latte attack, and so on.

The Cafe Latte attack allows you to obtain a WEP key from a client device. You can do this by capturing an [ARP packet](https://erg.abdn.ac.uk/users/gorry/course/inet-pages/arp.html) from the client, manipulating it, and then sending it back to the client.

The client will then generate a packet that can be captured by airodump-ng. Finally, aircrack-ng can be used to crack the WEP key form that modified packet.

### Airbase-ng

Airbase-ng is used to convert an attacker’s computer into a rogue access point for others to connect to. 

Using Airbase, you can pretend to be a legitimate access point and perform man-in-the-middle attacks on devices that connect to your system.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/2.png)

This attack is also called the “**Evil Twin Attack**”. Assuming you are in Starbucks trying to connect to their Wifi, an attacker can create another access point with the same name (usually with better signal strength) making you think that the access point belongs to Starbucks.

It is hard for regular users to differentiate between a legitimate access point and a rogue access point. So the evil twin attack remains one of the most dangerous wireless attacks we encounter today.

In addition to these, there are a few more tools for you to use in the Aircrack arsenal.

* **Packetforge-ng** — Used to create encrypted packets for injection.
* **Airdecap-ng —**  Decrypts WEP/WPA encrypted capture files after you crack the key with aircrack-ng. This will give you access to usernames, passwords, and other sensitive data.
* **Airolib-ng —**  Stores pre-computed WPA/WPA2 passphrases in a database. Used with aircrack-ng while cracking passwords.
* **Airtun-ng —**  Creates virtual tunnel interfaces.

## Summary

The world is a more connected place, thanks to WiFi. We enjoy the benefits of WiFi almost every single day. With all its benefits, it is also a vulnerable network capable of exposing our private information, if we are not careful.

Hope this article helped you understand WiFi security and Aircrack in detail. To learn more about Aircrack, [check out their official wiki](https://www.aircrack-ng.org/doku.php).

_Loved this article?_ [**_Join my Newsletter_**](http://tinyletter.com/manishmshiva) _and get a summary of my articles and videos sent to your email every Monday. You can also [**find my blog here**](https://medium.com/manishmshiva)._

