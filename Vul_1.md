# D-Link
Vulnerability for D-Link Router

Product: D-Link DIR823G  (Refer: http://www.dlink.com.cn/home/product?id=2960)

Version: The latest firmware -- 1.02B03 (Download link: http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-823G)

Vulnerability Type: Command Injection

Institution: 360 Enterprise Security Group

Vulnerability description
-------------------------
Command Injection vulnerability on Shenzhen Tenda Ac9 V15.03.05.19(6318)_CN(AC9), V15.03.06.44_CN(AC7), V15.03.06.23_CN(AC10) and earlier devices allows attackers to execute arbitrary OS commands via a crafted goform/setUsbUnload request . This occurs because the " formsetUsbUnload" function executes a dosystemCmd function with untrusted input

![image](https://github.com/zsjevilhex/iot/blob/master/route/tenda/tenda-01/image.png)


POC
-------------------------

![image](https://github.com/zsjevilhex/iot/blob/master/route/tenda/tenda-01/poc.jpeg)

This PoC can result in a Dos. 


p.s.Given the vendor's security, we only provide parts of the URL.
