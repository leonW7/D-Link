# D-Link
Vulnerability for D-Link Router

Product: D-Link DIR823G  (Refer http://www.dlink.com.cn/home/product?id=2960)

Version: The latest firmware -- 1.02B03 (http://support.dlink.com.cn/ProductInfo.aspx?m=DIR-823G)

Vulnerability Type: Command Injection

Institution: 360 Enterprise Security Group

Vulnerability description
-------------------------
I found a buffer overflow vulnerability in the router's web server--httpd. When processing the page parameters for a post request, the value is directly sprintf to a local variable placed on the stack, which overrides the return address of the function, causing buffer overflow.
The details are shown below:

![image](https://github.com/zsjevilhex/iot/blob/master/route/tenda/tenda-03/image.png)


POC
-------------------------

![image](https://github.com/zsjevilhex/iot/blob/master/route/tenda/tenda-03/poc.jpeg)

This PoC can result in a Dos. 


p.s.Given the vendor's security, we only provide parts of the URL.
