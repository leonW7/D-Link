# DIR-823G SetWLanRadioSettings Guest-WiFi Enable
Vulnerability for D-Link Router

Product: D-Link DIR-823G  (Refer: http://www.dlink.com.cn/home/product?id=2960)

Version: The latest firmware -- 1.02B03 (Download link: http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-823G)

![image](https://github.com/leonW7/D-Link/blob/master/4.png)

Vulnerability Type: Incorrect Access Control

Author: David Chen

Institution: Technology Research Institute of Legendsec at Qi’anxin Group

Vulnerability description
-------------------------
An issue was discovered in /bin/goahead on D-Link DIR-823G devices with firmware 1.02B03. There is incorrect access control allowing remote attackers to enable a Guest WiFi on router with no password default, without authentication, via the SetWLanRadioSettings HNAP API.  

POC
-------------------------

Attacker should call a HNAP API SetWLanRadioSettings remotely and enable a Guest WiFi on router immediately. Attacker just need to send a POST request setting some parameters such as RadioID,Enabled.., The Details are as blew:

Headers:

![image](https://github.com/leonW7/D-Link/blob/master/6-1.png)

Body:
![image](https://github.com/leonW7/D-Link/blob/master/6-2.png)

This PoC can enable an Guest WiFi on 2.4GHz named "D-Link_DIR-823G_Guest" with no password default as bleow:

![image](https://github.com/leonW7/D-Link/blob/master/6-3.png)

P.S. Given the vendor's security, we only provide parts of this exploit.
