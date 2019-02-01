# D-Link
Vulnerability for D-Link Router

Product: D-Link DIR-823G  (Refer: http://www.dlink.com.cn/home/product?id=2960)

Version: The latest firmware -- 1.02B03 (Download link: http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-823G)

![image](https://github.com/leonW7/D-Link/blob/master/4.png)

Vulnerability Type: Incorrect Access Control

Author: David Chen

Institution: 360 Enterprise Security Group

Vulnerability description
-------------------------
An issue was discovered in /bin/goahead on D-Link DIR-823G with the latest firmware 1.02B03. There is a incorrect access control problem allowing remote attackers to get sensitive information of all clients in WLAN without authentication via access a HNAP API named GetClientInfo. 

POC
-------------------------

Attacker just need to call a HNAP API GetClientInfo remotely and get all clients information in WLAN, such as IPAddresses, MacAddress, DeviceName, etc..

![image](https://github.com/leonW7/D-Link/blob/master/3-1.png)
![image](https://github.com/leonW7/D-Link/blob/master/3-2.png)

This PoC can result in a information disclosure.

P.S. Given the vendor's security, we only provide parts of this exploit.
