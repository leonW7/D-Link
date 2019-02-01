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
An issue was discovered on D-Link DIR-823G devices with firmware through 1.02B03. A command Injection vulnerability allows attackers to execute arbitrary OS commands via shell metacharacters in a crafted /HNAP1 request. This occurs when the entry point function of HNAP calls the system function with an untrusted input that is from request body directly. Consequently, an attacker can execute any command remotely when they control this input. The details are as below:

![image](https://github.com/leonW7/D-Link/blob/master/2-1.png)

The v4 variable is from request body, and when system function is called, input variable str3 is a string formed as this pattern "echo v4 >/var/hnaplog", so if someone can control the input of v4, they will execute any command.

POC
-------------------------

Attacker just need to call any HNAP API fuction remotely that is formed with request body embedded OS commands. For example, you can call "GetDeviceSettingsset" API and set request body as ’`/bin/telnetd`’:

![image](https://github.com/leonW7/D-Link/blob/master/2-2.png)
![image](https://github.com/leonW7/D-Link/blob/master/2-3.png)

This PoC can result in a RCE that opens telnet service at router as below:

![image](https://github.com/leonW7/D-Link/blob/master/2-4.png)

p.s.Given the vendor's security, we only provide parts of this exploit.
