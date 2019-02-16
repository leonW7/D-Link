# D-Link GetNetworkTomographyResult CMD Injection
Vulnerability for D-Link Router

Product: D-Link DIR-823G  (Refer: http://www.dlink.com.cn/home/product?id=2960)

Version: The latest firmware -- 1.02B03 (Download link: http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-823G)

![image](https://github.com/leonW7/D-Link/blob/master/4.png)

Vulnerability Type: Command Injection

Author: David Chen

Institution: 360 Enterprise Security Group

Vulnerability description
-------------------------
An issue was discovered on D-Link DIR-823G devices with firmware through 1.02B03. A command Injection vulnerability allows attackers to execute arbitrary OS commands via shell metacharacters in a crafted /HNAP1 request. This occurs when the GetNetworkTomographyResult function calls the system function with an untrusted input parameter named Address. Consequently, an attacker can execute any command remotely when they control this input. The details are as below:

![image](https://github.com/leonW7/D-Link/blob/master/5.png)

The str2 variable is from "Address" parameter, and the str variable is a string formed as bleow:
#### ping str2 -c %d -w %d -s %d  > /tmp/ping.txt 2>>/tmp/ping.txt
so if someone can control the input of str2, they will execute any command.

POC
-------------------------

Step1: Attacker need to call "SetNetworkTomographySettings" fuction that setting "Address" value. For example, you can set value as ";ps":

![image](https://github.com/leonW7/D-Link/blob/master/11.png)
![image](https://github.com/leonW7/D-Link/blob/master/666.png)

Step2: Attacker should call "GetNetworkTomographyResult" that executes OS commands embedded in "Address" parameter, this PoC can result in a RCE that executes a "ps" command at router as below:

![image](https://github.com/leonW7/D-Link/blob/master/222.png)

P.S. Given the vendor's security, we only provide parts of this exploit.
