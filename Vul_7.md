# D-Link DIR-816 Manager Interface Auth Bypass
**Vendor**: D-Link

**Product**: [DIR-816](http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-816)

**Firmware Version**: The latest firmware [Rev.A2 1.10B05](http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-816)

![image](https://github.com/leonW7/D-Link/blob/master/7.PNG)

**Vulnerability Type**: Incorrect Access Control

**Author**: David Chen

**Institution**: Technology Research Institute of Legendsec at Qi’anxin Group

Vulnerability description
-------------------------
An issue was discovered in the web manager interface on D-Link DIR-816 devices with firmware 1.10B05. There is a incorrect access control problem allowing remote attackers to visit manager interface without authentication, via visit /index.asp directly.

POC
-------------------------

Attacker can visit /index.asp directly and manager the router immediately. The Details are as blew:

Normal manager interface:

![image](https://github.com/leonW7/D-Link/blob/master/7-2.png)

Attacker can visit http://192.168.0.1/index.asp without authentication，and manager this router as admin:
![image](https://github.com/leonW7/D-Link/blob/master/7-3.png)
