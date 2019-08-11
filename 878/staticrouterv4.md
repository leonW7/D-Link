# D-Link SetStaticRoute CMD Injection

Product: D-Link DIR-878(Refer: http://www.dlink.com.cn/home/product?id=2961&hid=27)

Version: The latest firmware -- 1.12(Download Link: http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-878)

![](imgs/2019-02-11-12-07-36.png)

Vulnerability Type: Command Injection

Institution: 360 ESG / Legendsec Information Technology(Beijing)Inc.

## Vulnerability Description

A command Injection vulnerability allows attackers to execute arbitrary OS commands via a crafted /HNAP1 POST request. This occurs when any HNAP API function triggers a call to the system function with untrusted input from the request body for the `SetStaticRouteIPv4Settings` API function (need authentication).


In `/bin/rc` library:

**sub_4429D4** method:

![](imgs/2019-02-12-11-38-14.png)


Almost all of the field in xml body (`IPAddress, NetMask, Gateway and Metric`) is not correctly checked in before execute `twsystem` method.


## POC

**SetStaticRouteIPv4Settings**

![](imgs/2019-02-12-10-27-04.png)


![](imgs/2019-02-12-10-27-50.png)