# DIR-823G SetWanSettings DNS-Hijack
Vulnerability for D-Link Router

Product: D-Link DIR-823G  (Refer: http://www.dlink.com.cn/home/product?id=2960)

Version: The latest firmware -- 1.02B03 (Download link: http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-823G)

![image](https://github.com/leonW7/D-Link/blob/master/4.png)

Vulnerability Type: Incorrect Access Control

Author: David Chen

Institution: Technology Research Institute of Legendsec at Qi’anxin Group

Vulnerability description
-------------------------
An issue was discovered in /bin/goahead on D-Link DIR-823G with latest firmware 1.02B03. There is a incorrect access control problem allowing remote attackers to hijack DNS of all clients in WLAN without authentication via access a HNAP API named SetWanSettings.  

POC
-------------------------

Attacker should call a HNAP API SetWanSettings remotely and set DNS server of router immediately. Attacker just need to send a POST request as below:

Headers:

![image](https://github.com/leonW7/D-Link/blob/master/5-1.png)

Body:
![image](https://github.com/leonW7/D-Link/blob/master/5-2.png)

This PoC can result in a change of DNS server as below, you can see that the DNS server is set to "192.168.3.1" after exploit:

Before exploit:
![image](https://github.com/leonW7/D-Link/blob/master/5-3.png)

After exploit:
![image](https://github.com/leonW7/D-Link/blob/master/5-4.png)

P.S. Given the vendor's security, we only provide parts of this exploit.
