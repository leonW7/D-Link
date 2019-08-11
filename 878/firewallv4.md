# D-Link SetIPv4FirewallSettings CMD Injection

Product: D-Link DIR-878(Refer: http://www.dlink.com.cn/home/product?id=2961&hid=27)

Version: The latest firmware -- 1.12(Download Link: http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-878)

![](imgs/2019-02-11-12-07-36.png)

Vulnerability Type: Command Injection

Institution: 360 ESG / Legendsec Information Technology(Beijing)Inc.

## Vulnerability Description

A command Injection vulnerability allows attackers to execute arbitrary OS commands via a crafted /HNAP1 POST request. This occurs when any HNAP API function triggers a call to the `twsystem` function with untrusted input from the request body for the `SetIPv4FirewallSettings` API function (need authentication).


In `/lib/librcm.so` binary.

**FIREWALL_FILTER_run** method:

![](imgs/2019-02-12-12-18-46.png)

![](imgs/2019-02-12-12-41-05.png)

## POC

`SrcIPv4AddressRangeStart`, `DestIPv4AddressRangeStart`, `SrcIPv4AddressRangeEnd`, `DestIPv4AddressRangeEnd` all these field is vulnerability.

![](imgs/2019-02-12-12-40-16.png)

![](imgs/2019-02-12-12-46-51.png)