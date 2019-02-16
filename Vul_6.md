# D-Link SetWLanRadioSettings Guest-WiFi Enable
Vulnerability for D-Link Router

Product: D-Link DIR-823G  (Refer: http://www.dlink.com.cn/home/product?id=2960)

Version: The latest firmware -- 1.02B03 (Download link: http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-823G)

![image](https://github.com/leonW7/D-Link/blob/master/4.png)

Vulnerability Type: Incorrect Access Control

Author: David Chen

Institution: 360 Enterprise Security Group

Vulnerability description
-------------------------
An issue was discovered in /bin/goahead on D-Link DIR-823G devices with firmware 1.02B03. There is incorrect access control allowing remote attackers to enable the Guest WiFi on router with no password default, without authentication, via the SetWLanRadioSettings HNAP API.  

POC
-------------------------

Attacker should call a HNAP API SetWanSettings remotely and enable Guest WiFi on router immediately. Attacker just need to send a POST request as below:

Headers:

![image](https://github.com/leonW7/D-Link/blob/master/5-1.png)

Body:
![image](https://github.com/leonW7/D-Link/blob/master/5-2.png)

This PoC can enable Guest WiFi with no password default after exploit:

![image](https://github.com/leonW7/D-Link/blob/master/5-4.png)

P.S. Given the vendor's security, we only provide parts of this exploit.
