# 简介
## 模块名：接收各个Termux传来的IP数据

## 实现过程

> 1. 基于 Flask 实现一个简单WEB 服务
> 2. `/data` 接收Post请求，存储Termux发来的IP数据
> 3. `/ip/<device>` 接收GET/POST请求，返回对应设备的ipv6地址，若没有上传过则返回err
