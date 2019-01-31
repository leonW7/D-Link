# D-Link
Vulnerability for D-Link Router

Product: D-Link DIR-823G  (Refer: http://www.dlink.com.cn/home/product?id=2960)

Version: The latest firmware -- 1.02B03 (Download link: http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-823G)

Vulnerability Type: Command Injection

Institution: 360 Enterprise Security Group

Vulnerability description
-------------------------
Command Injection vulnerability on D-Link DIR-823G V 1.02B03 and earlier version allows attacker to execute arbitrary OS commands via a crafted /HNAP1 request. This occurs because one SOAP function named "GetNetworkTomographyResult" executes a system function with untrusted input.

![image](https://github.com/leonW7/D-Link/blob/master/5.png)


POC
-------------------------

First, attacker need to call "SetNetworkTomographySettings" fuction that setting domain name, as below:

![image](https://github.com/leonW7/D-Link/blob/master/1.png)

Second, attacker can call "GetNetworkTomographyResult" that executes OS commands embedded in domain name, this PoC can result in a RCE, as below:

![image](https://github.com/leonW7/D-Link/blob/master/2.png)

p.s.Given the vendor's security, we only provide parts of this exploit.
