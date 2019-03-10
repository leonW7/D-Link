# D-Link DIR-816 Manager Interface InfoLeak
Vendor: D-Link

Product: [DIR-816](http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-816)

Firmware Version: The latest firmware [Rev.A2 1.10B05](http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-816)

![image](https://github.com/leonW7/D-Link/blob/master/7.PNG)

Vulnerability Type: Incorrect Access Control

Author: David Chen

Institution: 360 ESG Institute of Security Research (360ESGR)

Vulnerability description
-------------------------
An issue was discovered in the manager interface on D-Link DIR-816 devices with firmware 1.10B05. There is a incorrect access control problem allowing remote attackers to get sensitive informations without authentication.

POC
-------------------------

Step1: Attacker can visit /index.asp directly without authentication and get the maintain page in the manager interface of the router immediately. The Details are as blew:

![image](https://github.com/leonW7/D-Link/blob/master/8.png)

Step2: In the maintain page, attacker can get config informations and save into a file named config.img as bleow:

![image](https://github.com/leonW7/D-Link/blob/master/8-1.png)

Step3: Attacker can decode these base64-encoded objects, and get all informations including login account, password, and so on.

![image](https://github.com/leonW7/D-Link/blob/master/8-2.png)
