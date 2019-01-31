# D-Link
Vulnerability for D-Link Router

Product: D-Link DIR-823G  (Refer: http://www.dlink.com.cn/home/product?id=2960)

Version: The latest firmware -- 1.02B03 (Download link: http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-823G)

![image](https://github.com/leonW7/D-Link/blob/master/4.png)

Vulnerability Type: Command Injection

Author: David Chen

Institution: 360 Enterprise Security Group

Vulnerability description
-------------------------
Command Injection vulnerability on D-Link DIR-823G V 1.02B03 and earlier version allows attacker to execute arbitrary OS commands via a crafted /HNAP1 request. This occurs because one SOAP function named "GetNetworkTomographyResult" executes system function with an untrusted input parameter "Address". The details are as below:

![image](https://github.com/leonW7/D-Link/blob/master/5.png)

The str2 variable is from "Address" parameter, and the str variable is a string formed as this pattern "ping str2 -c %d -w %d -s %d  > /tmp/ping.txt 2>>/tmp/ping.txt", so if someone can control the input of str2, they will execute any command.

POC
-------------------------

First, attacker need to call "SetNetworkTomographySettings" fuction that setting "Address" value. For example, you can set value as ";ps":

![image](https://github.com/leonW7/D-Link/blob/master/1.png)
![image](https://github.com/leonW7/D-Link/blob/master/6.png)

Second, attacker can call "GetNetworkTomographyResult" that executes OS commands embedded in "Address" parameter, this PoC can result in a RCE that executes a "ps" command at router as below:

![image](https://github.com/leonW7/D-Link/blob/master/22.png)

p.s.Given the vendor's security, we only provide parts of this exploit.
