### 12 LLDP

#### 12.1 概述

LLDP（Link Layer Discovery Protocol，链路层发现协议）是由IEEE 802.1AB定义的一种链路层发现协议。通过LLDP协议
能够进行拓扑的发现及掌握拓扑的变化情况。LLDP将设备的本地信息组织成TLV的格式（Type/Length/Value，类型/长度/值）
封装在LLDPDU（LLDP data unit，链路层发现协议数据单元）中发送给邻居设备，同时它将邻居设备发送的LLDPDU以MIB
（Management Information Base，管理信息库）的形式存储起来，提供给网络管理系统访问。

通过LLDP，网络管理系统可以掌握拓扑的连接情况，比如设备的哪些端口与其它设备相连接，链路连接两端的端口的速率、
双工是否匹配等，管理员可以根据这些信息快速地定位及排查故障。

一台支持LLDP协议的锐捷交换机产品，当对端设备是支持LLDP协议的锐捷交换机产品，或支持LLDP-MED协议的终端设
备的时候，该产品可以发现邻居信息。

 支持LLDP协议的锐捷交换机产品。

 支持LLDP-MED协议的终端设备。

**协议规范**

 IEEE 802.1AB 2005：Station and Media Access Control Connectivity Discovery

 ANSI/TIA- 1057 ：Link Layer Discovery Protocol for Media Endpoint Devices

#### 12.2 典型应用

典型应用 场景描述
利用LLDP查看拓扑连接情况 网络拓扑中有若干交换机设备、MED设备、NMS设备。
利用LLDP进行错误检测 网络拓扑中有直连的两台交换机设备，错误配置信息将显示。

###### 12.2.1 利用 LLDP 查看拓扑连接情况

**应用场景**

网络拓扑中有若干交换机设备、MED设备、NMS设备。

以下图为例，LLDP功能默认打开，不需要再进行配置。

 Switch A和Switch B可以互相发现对方是自己的邻居设备。

 Switch A在端口Gi 0/1上可以发现邻居MED设备IP-Phone。


配置指南 LLDP

 NMS（Network Management System，网络管理系统）能够访问Switch A的邻居设备信息。

图 12 - 1

【注释】 锐捷交换机产品Switch A和Switch B、IP-Phone都支持LLDP和LLDP-MED。
交换机端口上LLDP的工作模式为TxRx。
LLDP报文的发送时间参数采用缺省值，即发送时间间隔为 30 秒、传输LLDP报文的延迟时间为 2 秒。

**功能部属**

 在交换机中运行LLDP协议，实现邻居发现。

 在交换机中运行SNMP协议，实现网络管理系统获取和设置交换机中的LLDP相关信息。

###### 12.2.2 利用 LLDP 进行错误检测

**应用场景**

网络拓扑中有直连的两台交换机设备，错误配置信息将显示。

以下图为例，LLDP功能默认打开，LLDP错误检测功能缺省打开，不需要再进行配置。

 管理员在对Switch A进行VLAN配置、端口速率双工配置、聚合端口配置和端口MTU配置时，如果配置的信息与相连
接的邻居设备Switch B的配置不匹配，将提示相应的错误信息。反之亦然。

图 12 - 2

【注释】 两台锐捷交换机产品Switch A和Switch B都支持LLDP协议。
交换机端口上LLDP的工作模式为TxRx。
LLDP报文的发送时间参数采用缺省值，即发送时间间隔为 30 秒、传输LLDP报文的延迟时间为 2 秒。

**功能部属**


配置指南 LLDP

 在交换机中运行LLDP协议，实现邻居发现，并检测两端的交换机直接接口的配置信息是否错误。

#### 12.3 功能详解

**基本概念**

######  LLDPDU

LLDPDU是指封装在LLDP报文中的协议数据单元，它由一系列的TLV封装而成。这些TLV集合包括了三个固定的TLV加上
一系列可选的TLVs和一个End Of TLV组成。LLDPDU的具体格式如图所示：

图 12 - 3 LLDPDU格式

其中：

 M表示是固定的TLV。

 在LLDPDU中，Chassis ID TLV、Port ID TLV、Time To Live TLV和End Of LLDPDU TLV是必须携带的，而其它类型
的TLV是可选携带。

######  LLDP 报文封装格式

LLDP报文支持两种封装格式：Ethernet II和SNAP（Subnetwork Access Protocols，子网访问协议）。

其中Ethernet II格式封装的LLDP报文如图所示：

图 12 - 4 Ethernet II格式封装的LLDP报文

其中：

 Destination Address：目的MAC地址，为LLDP的组播地址 01 - 80 - C2- 00 - 00 - 0E。

 Source Address：源MAC地址，为设备的端口MAC地址。

 Ethertype：以太网类型，为0x88CC。

 LLDPDU：LLDP协议数据单元。

 FCS：帧校验序列。

SNAP格式封装的LLDP报文如图所示：

图 12 - 5 SNAP格式封装的LLDP报文


配置指南 LLDP

其中：

 Destination Address：目的MAC地址，为LLDP的组播地址 01 - 80 - C2- 00 - 00 - 0E。

 Source Address：源MAC地址，为设备的端口MAC地址。

 SNAP-encoded Ethertype：SNAP封装的以太网类型，为AA-AA- 03 - 00 - 00 - 00 - 88 - CC.。

 LLDPDU：LLDP协议数据单元。

 FCS：帧校验序列。

######  TLV

LLDPDU中封装的TLV可以分成二个大类：

 基本管理TLV

 组织定义TLV

基本管理TLV是一组用于网络管理的基础TLV集合。组织定义TLV是由标准组织和其它机构定义的TLV，比如IEEE 802.1
组织、IEEE 802.3组织分别定义了各自的TLV集合。

1. 基本管理TLV

基本管理TLV集合包含了两种类型的TLV：固定TLV和可选TLV。固定TLV是指该TLV信息必须包含在LLDPDU中发布，
可选TLV是指根据需要确定TLV是否包含在LLDPDU中发布。

基本管理TLV的内容见表：

```
TLV类型 TLV说明 在LLDPDU中用法
End Of LLDPDU TLV LLDPDU的结束标志，占用 2 个字节 固定
Chassis ID TLV 用于标识设备，通常用MAC地址表示 固定
Port ID TLV 用于标识发送LLDPDU的端口 固定
Time To Live TLV
本地信息在邻居设备上的存活时间，当收到TTL为 0
的TLV时，此时需要删除掉对应的邻居信息。
固定
Port Description TLV 发送LLDPDU的端口描述符 可选
System Name TLV 描述设备的名称 可选
System Description TLV 设备描述信息，包括硬件/软件版本、操作系统等信息 可选
System Capabilities TLV 描述设备的主要功能，例如桥接、路由、中继等功能 可选
Management Address TLV
管理地址，同时包含了接口号和OID（Object Identifier，
对象标识）。
可选
```

### 锐捷交换机系列产品LLDP协议支持基本管理TLV的发布。

2. 组织定义TLV

不同的组织（例如IEEE 802.1、IEEE 802.3、IETF或者设备供应商）定义特定的TLV信息去通告设备的特定信息。TLV格式
中通过OUI（Organizationally Unique Identifier，组织唯一标识符）字段来区分不同的组织。


配置指南 LLDP

 组织定义TLV属于可选的TLV集合，根据用户的实际需要在LLDPDU中发布。目前比较常见的组织定义TLV有以下三
种： IEEE 802.1组织定义的TLV

IEEE 802.1组织定义的TLV见表：

```
TLV类型 TLV说明
```

Port VLAN ID TLV (^) 端口的VLAN标识符
Port And Protocol VLAN ID TLV 端口的协议VLAN标识符
VLAN Name TLV 端口的VLAN名称
Protocol Identity TLV 端口支持的协议类型

### 锐捷交换机系列产品LLDP协议，不支持发送Protocol Identity TLV，但支持接收该类型的TLV。

 IEEE 802.3组织定义的TLV

IEEE 802.3组织定义的TLV见表：

```
TLV类型 TLV说明
MAC/PHY Configuration//Status TLV 端口的速率双工状态、是否支持并使能自动协商功能
Power Via MDI TLV 端口的供电能力
Link Aggregation TLV 端口的链路聚合能力及当前的聚合状态
Maximum Frame Size TLV 端口所能传输的最大的帧的大小
```

### 锐捷交换机系列产品LLDP协议支持IEEE 802.3组织定义的TLV的发布。

 LLDP-MED TLV

LLDP-MED以IEEE 802.1AB LLDP协议为基础，它扩展了LLDP，使用户能够更方便地部署VoIP（Voice Over IP，基于IP
的语音传输）网络及进行故障检测。它提供了网络配置策略、设备发现、以太网供电管理和目录管理等应用，满足了节约成本、
有效地管理和易于部署方面的需求，简化了语音设备地部署。

LLDP-MED定义的TLV见表：

TLV类型 TLV说明

LLDP-MED Capabilities TLV 设备是否支持LLDP-MED、LLDPDU中封装的LLDP-MED TLV类型以及当前设
备的类型（网络连接设备或终端）

Network Policy TLV 通告端口的VLAN的配置、支持的应用类型（如语音或视频）、二层的优先级信息
等
Location Identification TLV 定位标识终端设备。在网络拓扑收集等应用中能够精确地定位出终端设备
Extended Power-via-MDI TLV 提供了更高级的供电管理
Inventory – Hardware Revision TLV MED设备的硬件版本

Inventory – Firmware Revision TLV (^) MED设备的固件版本
Inventory – Software Revision TLV (^) MED设备的软件版本
Inventory – Serial Number TLV (^) MED设备的序列号
Inventory – Manufacturer Name TLV MED设备的制造商的名称


配置指南 LLDP

Inventory – Model Name TLV (^) MED设备的模块名称
Inventory – Asset ID TLV (^) MED设备的资产标识符，用于目录管理和资产跟踪

### 锐捷交换机系列产品LLDP协议支持LLDP-MED定义的TLV的发布。^

**功能特性**

功能特性 作用
LLDP工作模式 配置LLDP报文收发的模式。
LLDP报文的传输机制 直连支持LLDP协议的交换机设备可发送LLDP报文给对方。
LLDP报文的接收机制 直连支持LLDP协议的交换机设备可接收对方发送的LLDP报文。

###### 12.3.1 LLDP 工作模式

配置LLDP工作模式，能够使交换机收发LLDP报文的方式发生变化。

**工作原理**

LLDP提供了三种工作模式：

 TxRx：既发送也接收LLDPDU。

 Rx Only：只接收不发送LLDPDU。

 Tx Only：只发送不接收LLDPDU。

当端口的LLDP工作模式发生变化时，端口将对协议状态机进行初始化操作，通过配置端口初始化的延迟时间，可以避免由于
工作模式频繁改变而导致端口不断地进行初始化操作。

**相关配置**

######  配置 LLDP 工作模式

缺省情况下，接口上的工作模式为TxRx。

使用lldp mode命令可以改变接口上的工作模式。

必须在接口上配置工作模式为TxRx才能使LLDP协议报文收发功能正常。若接口工作模式配置为Rx Only，那么设备只能接
收LLDP报文，但无法发送LLDP报文；若接口工作模式配置为Tx Only，那么设备只能发送LLDP报文，但无法接收LLDP
报文；若借口工作模式关闭，将不再收发LLDP报文。

###### 12.3.2 LLDP 报文的传输机制

LLDP报文的传输能让对端设备发现其邻居设备的存在，当取消LLDP传输模式或端口被管理Shutdown的时候，能够通告给
对端设备其邻居信息不再有效。


配置指南 LLDP

**工作原理**

LLDP工作在TxRx或Tx Only模式时，会周期性的发送LLDP报文。当本地设备的信息发生变化时，会立即发送LLDP报文。
为了避免本地信息的频繁变化引起的频繁发送LLDP报文，在发送完一个LLDP报文后需要延迟一定的时间后再发往下一个
LLDP报文。该延迟时间可以手工配置。
LLDP提供了两种报文类型：

 标准LLDP报文：包含了本地设备的管理和配置信息。

 Shutdown通告报文：当取消了LLDP的传输模式或者端口被管理Shutdown时，将触发LLDP Shutdown通告报文的发
送。Shutdown通告报文由Chassis ID TLV、Port ID TLV、Time To Live TLV和End OF LLDP TLV组成。其中Time To Live
TLV中TTL等于 0 。当设备收到LLDP Shutdown通告报文时，将认为邻居信息已经不再有效并立即删除邻居信息。

当LLDP工作模式由关闭或Rx转变为TxRx或Tx，或者发现新邻居时（即收到新的LLDP报文且本地尚未保存该邻居信息），
为了让邻居设备尽快学习到本设备的信息，将启动快速发送机制。快速发送机制调整LLDP报文的发送周期为 1 秒，并连续发
送一定数量的LLDP报文。

**相关配置**

######  配置 LLDP 工作模式

缺省情况下，接口上的工作模式为TxRx。

使用lldp mode txrx和lldp mode tx命令可以使LLDP报文传输功能打开，使用lldp mode rx和no lldp mode命令可以使
LLDP报文传输功能关闭。

必须在接口上配置工作模式为TxRx或Tx Only才能使LLDP的报文传输功能正常。若接口工作模式配置为Rx Only，那么设
备只能接收LLDP报文，但无法发送LLDP报文。

######  配置 LLDP 报文的发送延迟时间

缺省情况下，LLDP报文的发送延迟时间为 2 秒。

使用lldp timer tx-delay命令可以修改LLDP报文的发送延迟时间。

延迟时间配置过小，本地信息的频繁变化引起的频繁发送LLDP报文；配置值太大，本地信息的变化可能不能使发送LLDP报
文。

######  配置 LLDP 报文的发送时间间隔

缺省情况下，LLDP报文的发送时间间隔为 30 秒。

使用lldp timer tx-interval命令可以修改LLDP报文的发送时间间隔。

配置值太小，则会使LLDP发送频率过高；配置值太大，则可能会使对端设备不能及时发现本地设备。

######  配置允许发布的 TLV 类型

缺省情况下，接口上允许发布除 Location Identification TLV 之外的所有类型的TLV。

使用lldp tlv-enable命令可以改变允许发布的TLV类型。


配置指南 LLDP

增加或减少发送的LLDP报文中LLDPDU的对应TLV字段。

######  配置 LLDP 快速发送报文的个数

缺省情况下，LLDP快速发送报文的个数为 3 个。

使用lldp fast-count命令可以改变LLDP快速发送报文的个数。

改变快速发送机制下快速发送报文的个数。

###### 12.3.3 LLDP 报文的接收机制

LLDP报文的接收能够发现邻居设备的存在以及何时应该老化邻居信息。

**工作原理**

LLDP工作在TxRx或RxOnly模式时，能够接收LLDP报文。当设备收到LLDP报文时，会进行有效性检查。通过报文校验
后，判断是新的邻居信息还是已经存在的邻居信息更新，并将邻居信息保存在本地设备。同时根据报文中TTL TLV的值设置邻
居信息在本地设备的存活时间。如果收到TTL TLV的值为 0 ，表示需要立即老化掉该邻居信息。

**相关配置**

######  配置 LLDP 工作模式

缺省情况下，接口上的工作模式为TxRx。

使用lldp mode txrx和lldp mode rx命令可以使LLDP报文接收功能打开，使用lldp mode tx和no lldp mode命令可以使
LLDP报文接收功能关闭。

必须在接口上配置工作模式为TxRx或Rx Only才能使LLDP的报文接收功能正常。若接口工作模式配置为Tx Only或关闭，
那么设备只能发送LLDP报文，但无法接收LLDP报文。

#### 12.4 配置详解

配置项 配置建议 & 相关命令

配置LLDP功能

### 可选配置。用于打开或关闭全局和接口的LLDP功能。^

```
lldp enable 打开LLDP功能
no lldp enable 关闭LLDP功能
```

配置LLDP工作模式

### 可选配置。用于配置LLDP报文收发模式。^

```
lldp mode {rx | tx | txrx } 配置LLDP工作模式
no lldp mode 关闭LLDP工作模式
```

### 配置允许发布的TLV类型 可选配置。用于配置允许发布的TLV类型。


配置指南 LLDP

```
lldp tlv-enable 配置允许发布的TLV类型
no lldp tlv-enable 取消发布指定的TLV类型
```

配置LLDP报文中发布管理地
址

### 可选配置。用于配置LLDP报文中发布。^

```
lldp management-address-tlv [ip-address] 配置LLDP报文中发布管理地址
no lldp management-address-tlv 取消管理地址的发布
```

配置快速发送LLDP报文的个
数

### 可选配置。用于配置快速发送LLDP报文的个数。^

```
lldp fast-count value 配置快速发送LLDP报文的个数
no lldp fast-count 恢复缺省快速发送LLDP报文个数
```

配置TTL乘数和LLDP报文发
送时间间隔

### 可选配置。用于配置TTL乘数和LLDP报文发送时间间隔。^

```
lldp hold-multiplier value 配置TTL乘数
```

no lldp hold-multiplier (^) 恢复缺省TTL乘数
lldp timer tx-interval seconds (^) 配置LLDP报文发送时间间隔
no lldp timer tx-interval 恢复缺省LLDP报文发送时间间隔
配置LLDP报文的发送延迟时
间

### 可选配置。用于配置LLDP报文的发送延迟时间。^

```
lldp timer tx-delay seconds 配置LLDP报文的发送延迟时间
no lldp timer tx-delay 恢复缺省LLDP报文的发送延迟时间
```

配置端口初始化的延迟时间

### 可选配置。用于配置端口初始化的延迟时间。^

```
lldp timer reinit-delay seconds 配置端口初始化的延迟时间
no lldp timer reinit-delay 恢复缺省端口初始化的延迟时间
```

配置LLDP Trap功能

### 可选配置。用于配置LLDP Trap功能。^

```
lldp notification remote-change enable 打开LLDP Trap功能
no lldp notification remote-change enable 关闭LLDP Trap功能
lldp timer notification-interval 配置发送LLDP Trap信息的时间间隔
no lldp timer notification-interval 恢复缺省发送LLDP Trap信息的时间间隔
```

配置LLDP错误检测功能

### 可选配置。用于配置LLDP错误检测功能。^

lldp error-detect (^) 打开LLDP错误检测功能
no lldp error-detect (^) 关闭LLDP错误检测功能
配置LLDP报文封装格式

### 可选配置。用于配置LLDP报文封装格式。^

lldp encapsulation snap (^) 配置LLDP报文的封装格式为SNAP
no lldp encapsulation snap 配置LLDP报文的封装格式为Ethernet II
配置LLDP Network Policy策
略

### 可选配置。用于配置LLDP Network Policy策略。^

```
lldp network-policy profile profile-num 配置LLDP Network Profile策略
no lldp network-policy profile profile-num 删除LLDP Network Profile策略
```

配置指南 LLDP

配置设备的普通地址信息

### 可选配置。用于配置设备的普通地址信息。^

```
{ country | state | county | city | division |
neighborhood | street-group |
leading-street-dir | trailing-street-suffix |
street-suffix | number |
street-number-suffix | landmark |
additional-location-information | name |
postal-code | building | unit | floor | room |
type-of-place | postal-community-name |
post-office-box | additional-code } ca-word
```

```
配置设备的普通地址信息
```

```
no { country | state | county | city | division
| neighborhood | street-group |
leading-street-dir | trailing-street-suffix |
street-suffix | number |
street-number-suffix | landmark |
additional-location-information | name |
postal-code | building | unit | floor | room |
type-of-place | postal-community-name |
post-office-box | additional-code } ca-word
```

```
删除设备的普通地址信息
```

配置设备的紧急电话号码信
息

### 可选配置。用于配置设备的紧急电话号码信息。^

```
lldp location elin identifier id elin-location
tel-number 配置设备的紧急电话号码信息^
no lldp location elin identifier id 删除设备的紧急电话号码信息
```

配置兼容友商邻居发现功能

### 可选配置。用于配置设备兼容友商邻居发现功能。^

```
lldp compliance vendor 打开兼容友商邻居发现功能
```

```
no lldp compliance vendor 关闭兼容友商邻居发现功能
```

配置获取全局LLDP管理地址
的类型

### 可选配置。用于配置获取全局LLDP管理地址的类型。^

```
lldp management-address-tlv global-ip
type {interface | loopback} 配置LLDP报文中发布的管理地址使用类型^
no lldp management-address-tlv global-ip
type
```

```
LLDP报文中发布的管理地址使用类型恢复到
缺省配置
```

###### 12.4.1 配置 LLDP 功能

**配置效果**


配置指南 LLDP

 打开或关闭LLDP的功能。

**注意事项**

 如果要求接口上LLDP功能生效，则要同时开启全局和该接口上的LLDP功能。

**配置方法**

 可选配置。

 可对全局或接口下配置LLDP功能。

**检验方法**

显示LLDP的状态信息。

 检查全局LLDP功能是否开启。

 检查接口下LLDP功能是否开启。

**相关命令**

######  打开 LLDP 功能

```
【命令格式】 lldp enable
【参数说明】 -
【命令模式】 全局模式、接口模式
【使用指导】 需要全局打开LLDP开关，接口的LLDP功能才生效。
```

######  关闭 LLDP 功能

```
【命令格式】 no lldp enable
【参数说明】 -
【命令模式】 全局模式、接口模式
【使用指导】 -
```

**配置举例**

######  关闭 LLDP 功能

```
【配置方法】 关闭全局LLDP功能。
Ruijie(config)#no lldp enable
```

```
【检验方法】 显示LLDP全局状态信息。
Ruijie(config)#show lldp status
```

配置指南 LLDP

```
Global status of LLDP: Disable
```

**常见错误**

 接口已开启LLDP功能，但是全局没有开启LLDP功能，此时接口下的LLDP功能还是不能生效。

 端口学习到的邻居个数限制在 5 个，即端口最多只能学习到 5 个邻居。

 如果邻居设备不支持LLDP，但是邻居设备下连的设备支持LLDP，由于邻居设备可能会转发LLDP的报文，这样，端口
可能会学习到非直连的设备的信息。

###### 12.4.2 配置 LLDP 工作模式

**配置效果**

 配置接口的LLDP的工作模式为TxRx，则该接口可发送和接收报文。

 配置接口的LLDP的工作模式为Tx，则该接口只能发送报文，不能接收报文。

 配置接口的LLDP的工作模式为Rx，则该接口只能接收报文，不能发送报文。

 关闭接口的LLDP工作模式，则该接口不能接收和发送报文。

**注意事项**

 LLDP运行在实际的物理接口上（对于AP口，则实际是运行在AP成员口上）。堆叠口，VSL口不支持LLDP。

**配置方法**

 可选配置。

 用户可根据实际需要将工作模式修改为Tx或Rx模式。

**检验方法**

显示接口下LLDP的状态信息。

 检查接口下LLDP的工作模式是否和配置的相同。

**相关命令**

######  配置 LLDP 工作模式

```
【命令格式】 lldp mode { rx | tx | txrx }
【参数说明】 rx：表示只接收不发送LLDPDU
```

配置指南 LLDP

```
tx：表示只发送不接收LLDPDU
txrx：表示即发送又接收LLDPDU
【命令模式】 接口模式
【使用指导】 接口LLDP功能生效的前提是全局使能了LLDP且接口LLDP的工作模式处于tx、rx或txrx。
```

######  关闭 LLDP 工作模式

```
【命令格式】 no lldp mode^
【参数说明】 -
【命令模式】 接口模式
【使用指导】 关闭接口的LLDP工作模式，此时接口不再发送和接收LLDP报文。
```

**配置举例**

######  配置 LLDP 工作模式

【配置方法】 接口下配置LLDP的工作模式为Tx模式。
Ruijie(config)#interface gigabitethernet 0/1
Ruijie(config-if-GigabitEthernet 0/1)#lldp mode tx

【检验方法】 显示LLDP在接口下的状态信息。
Ruijie(config-if-GigabitEthernet 0/1)#show lldp status interface gigabitethernet 0/1^
Port [GigabitEthernet 0/1]
Port status of LLDP : Enable
Port state : UP
Port encapsulation : Ethernet II
Operational mode : TxOnly
Notification enable : NO
Error detect enable : YES
Number of neighbors : 0
Number of MED neighbors : 0

**常见配置错误**

-

###### 12.4.3 配置允许发布的 TLV 类型

**配置效果**

 用户可以通过配置运行发布的TLV类型，使发送LLDP报文中LLDPDU的内容改变。


配置指南 LLDP

**注意事项**

 配置基本管理TLV、IEEE 802.1组织定义TLV、IEEE 802.3组织定义TLV时，如果指定all参数，将发布该类型的所有
可选TLV。

 配置LLDP-MED TLV时，如果指定all参数，将发布除 Location Identification TLV 之外的所有类型的 LLDP-MED TLV。

 配置允许发布LLDP-MED Capability TLV时，需要先配置允许发布LLDP 802.3 MAC/PHY TLV；取消发布LLDP 802.3
MAC/PHY TLV时，需要先取消发布LLDP-MED Capability TLV

 配置LLDP-MED TLV时，必须配置允许发布LLDP-MED Capability TLV，才可以配置允许发布LLDP-MED其它类型的
TLV。取消发布LLDP-MED TLV，必须先取消发布LLDP-MED其它类型的TLV，才允许取消发布LLDP-MED Capability
TLV。当设备下联IP电话，若IP电话支持LLDP-MED，则可以通过配置network policy TLV下发策略给IP电话
 如果设备缺省支持DCBX功能，缺省情况下端口上不允许发布IEEE 802.3 TLV及 LLDP-MED TLV

**配置方法**

 可选配置。

 用户可根据实际需要在某接口下配置允许发布的TLV类型。

**检验方法**

显示端口上可发布的TLV配置信息。

 检查接口下允许发布的TLV是否和配置的一致。

**相关命令**

######  配置 LLDP 允许发布的 TLV

```
【命令格式】 lldp tlv-enable { basic-tlv { all | port-description | system-capability | system-description |
system-name } |dot1-tlv { all | port-vlan-id | protocol-vlan-id [ vlan-id ] | vlan-name [ vlan-id ] } |dot3-tlv
{ all | link-aggregation | mac-physic | max-frame-size | power } | med-tlv { all | capability | inventory |
location { civic-location | elin } identifier id | network-policy profile [ profile-num ] |
power-over-ethernet } }
【参数说明】 basic-tlv：基本管理TLV
port-description：表示Port Description TLV
system-capability：表示System Capabilities TLV
system-description：表示System Description TLV
system-name：表示System Name TLV
dot1-tlv：802.1组织定义的TLV
port-vlan-id：表示Port VLAN ID TLV
protocol-vlan-id：表示Port And Protocol VLAN ID TLV
```

配置指南 LLDP

```
vlan-id：表示端口协议VLAN ID，配置范围为： 1 - 4094
vlan-name：表示VLAN Name TLV
vlan-id：表示指定VLAN名称对应的VLAN ID，配置范围为： 1 - 4094
dot3-tlv：802.3组织定义的TLV
link-aggregation：表示Link Aggregation TLV
mac-physic：表示MAC/PHY Configuratioin/Status TLV
max-frame-size：表示Maximum Frame Size TLV
power：表示Power Via MDI TLV
med-tlv：LLDP MED TLV
capability：表示LLDP-MED Capabilities TLV
inventory：表示目录管理TLV，包括硬件版本、固件版本、软件版本、序列号、制造产商名称、模块名称和
资产标识符等
location：表示Location Identification TLV
civic-location：表示封装网络连接设备的普通地址信息
elin：表示封装紧急电话号码信息
id：表示配置的策略ID，配置范围为： 1 - 1024
network-policy：表示Network Policy TLV
profile-num：Network Policy策略ID，配置范围为： 1 - 1024
power-over-ethernet：表示Extended Power-via-MDI TLV
【命令模式】 接口模式
【使用指导】
```

######  取消发布指定的 TLV 类型

```
【命令格式】 no lldp tlv-enable {basic-tlv { all | port-description | system-capability | system-description |
system-name } | dot1-tlv { all | port-vlan-id | protocol-vlan-id | vlan-name } | dot3-tlv { all |
link-aggregation | mac-physic | max-frame-size | power } | med-tlv { all | capability | inventory |
location { civic-location | elin } identifier id | network-policy profile [ profile-num ] |
power-over-ethernet } }
【参数说明】 basic-tlv：基本管理TLV
port-description：表示Port Description TLV
system-capability：表示System Capabilities TLV
system-description：表示System Description TLV
system-name：表示System Name TLV
dot1-tlv：802.1组织定义的TLV
port-vlan-id：表示Port VLAN ID TLV
protocol-vlan-id：表示Port And Protocol VLAN ID TLV
vlan-name：表示VLAN Name TLV
dot3-tlv：802.3组织定义的TLV
link-aggregation：表示Link Aggregation TLV
mac-physic：表示MAC/PHY Configuratioin/Status TLV
```

配置指南 LLDP

```
max-frame-size：表示Maximum Frame Size TLV
power：表示Power Via MDI TLV
med-tlv：LLDP MED TLV
capability：表示LLDP-MED Capabilities TLV
inventory：表示目录管理TLV，包括硬件版本、固件版本、软件版本、序列号、制造产商名称、模块名称和
资产标识符等
location：表示Location Identification TLV
civic-location：表示封装网络连接设备的普通地址信息
elin：表示封装紧急电话号码信息
id：表示配置的策略ID，配置范围为： 1 - 1024
network-policy：表示Network Policy TLV
profile-num：Network Policy策略ID，配置范围为： 1 - 1024
power-over-ethernet：表示Extended Power-via-MDI TLV
【命令模式】 接口模式
【使用指导】
```

**配置举例**

######  配置 LLDP 允许发布的 TLV

【配置方法】 配置取消发布IEEE 802.1组织定义的Port And Protocol VLAN ID TLV
Ruijie(config)#interface gigabitethernet 0/1
Ruijie(config-if-GigabitEthernet 0/1)#no lldp tlv-enable dot1-tlv protocol-vlan-id

【检验方法】 显示LLDP在接口下的TLV配置信息。
Ruijie(config-if-GigabitEthernet 0/1)#show lldp tlv-config interface gigabitethernet 0/1
LLDP tlv-config of port [GigabitEthernet 0/1]
NAME STATUS DEFAULT

------------------------------ ------ -------

Basic optional TLV:
Port Description TLV YES YES
System Name TLV YES YES
System Description TLV YES YES
System Capabilities TLV YES YES
Management Address TLV YES YES

```
IEEE 802.1 extend TLV:
Port VLAN ID TLV YES YES
Port And Protocol VLAN ID TLV NO YES
VLAN Name TLV YES YES
```

配置指南 LLDP

```
IEEE 802.3 extend TLV:
MAC-Physic TLV YES YES
Power via MDI TLV YES YES
Link Aggregation TLV YES YES
Maximum Frame Size TLV YES YES
```

```
LLDP-MED extend TLV:
Capabilities TLV YES YES
Network Policy TLV YES YES
Location Identification TLV NO NO
Extended Power via MDI TLV YES YES
Inventory TLV YES YES
```

**常见配置错误**

-

###### 12.4.4 配置 LLDP 报文中发布管理地址

**配置效果**

 配置接口下LLDP报文中的发布管理地址，可使管理地址TLV发生改变。

 取消管理地址发布将使LLDP报文中的管理地址按缺省情况下选取。

**注意事项**

 LLDP运行在实际的物理接口上（对于AP口，则实际是运行在AP成员口上）。堆叠口，VSL口不支持LLDP。

**配置方法**

 可选配置。

 在接口下配置LLDP报文发布的管理地址。

**检验方法**

显示本地设备接口下的LLDP信息。

 检查本地设备接口下的LLDP信息是否和配置的相同。

**相关命令**


配置指南 LLDP

######  配置 LLDP 报文中发布的管理地址

```
【命令格式】 lldp management-address-tlv [ ip-address ]
【参数说明】 ip-address：LLDP报文中发布的管理地址
【命令模式】 接口模式
【使用指导】 缺省情况下，LLDP报文发布管理地址。发布的管理地址为端口允许通过的最小VLAN的IPv4地址，如果该
VLAN未配置IPv4地址，则继续查找下一个允许通过的最小VLAN，直到找到IPv4地址为止。
如果未找到IPv4地址，则查找端口允许通过的最小VLAN的IPv6地址。
如果仍未找到IPv6地址，则采用本机地址127.0.0.1作为管理地址发布。
```

######  取消管理地址的发布

```
【命令格式】 no lldp management-address-tlv
【参数说明】 -
【命令模式】 接口模式
【使用指导】 缺省情况下，LLDP报文发布管理地址。发布的管理地址为端口允许通过的最小VLAN的IPv4地址，如果该
VLAN未配置IPv4地址，则继续查找下一个允许通过的最小VLAN，直到找到IPv4地址为止。
如果未找到IPv4地址，则查找端口允许通过的最小VLAN的IPv6地址。
如果仍未找到IPv6地址，则采用本机地址127.0.0.1作为管理地址发布。
```

**配置举例**

######  配置 LLDP 报文中发布的管理地址

【配置方法】 在接口下配置LLDP报文发布的管理地址为192.168.1.1
Ruijie(config)#interface gigabitethernet 0/1
Ruijie(config-if-GigabitEthernet 0/1)#lldp management-address-tlv 192.168.1.1

【检验方法】 查看对应接口下相应的配置信息
Ruijie(config-if-GigabitEthernet 0/1)#show lldp local-information interface GigabitEthernet 0/1^
Lldp local-information of port [GigabitEthernet 0/1]
Port ID type : Interface name
Port id : GigabitEthernet 0/1
Port description : GigabitEthernet 0/1

```
Management address subtype : ipv4
Management address : 192.168.1.1
Interface numbering subtype : ifIndex
Interface number : 1
Object identifier :
```

```
802.1 organizationally information
Port VLAN ID : 1
```

配置指南 LLDP

```
Port and protocol VLAN ID(PPVID) : 1
PPVID Supported : YES
PPVID Enabled : NO
VLAN name of VLAN 1 : VLAN0001
Protocol Identity :
```

```
802.3 organizationally information
Auto-negotiation supported : YES
Auto-negotiation enabled : YES
PMD auto-negotiation advertised : 1000BASE-T full duplex mode, 100BASE-TX full duplex mode,
100BASE-TX half duplex mode, 10BASE-T full duplex mode, 10BASE-T half duplex mode
Operational MAU type : speed(100)/duplex(Full)
PoE support : NO
Link aggregation supported : YES
Link aggregation enabled : NO
Aggregation port ID : 0
Maximum frame Size : 1500
```

```
LLDP-MED organizationally information
Power-via-MDI device type : PD
Power-via-MDI power source : Local
Power-via-MDI power priority :
Power-via-MDI power value :
Model name : Model name
```

**常见配置错误**

-

###### 12.4.5 配置快速发送 LLDP 报文的个数

**配置效果**

 改变快速发送机制下LLDP报文发送的个数。

**注意事项**

 -

**配置方法**


配置指南 LLDP

 可选配置。

 在全局配置模式下配置快速发送LLDP报文个数。

**检验方法**

显示全局LLDP的状态信息。

 检查LLDP快速发送个数是否和配置的相同。

**相关命令**

######  配置快速发送 LLDP 报文的个数

```
【命令格式】 lldp fast-count value
【参数说明】 value：LLDP快速发送报文的个数，缺省为 3 个，可配置的范围为 1 - 10
【命令模式】 全局模式
【使用指导】 -^
```

######  恢复缺省快速发送 LLDP 报文个数

```
【命令格式】 no lldp fast-count
【参数说明】 -
【命令模式】 全局模式
【使用指导】 -
```

**配置举例**

######  配置快速发送 LLDP 报文的个数

【配置方法】 全局配置模式下配置快速发送LLDP报文的个数为 5 个
Ruijie(config)#lldp fast-count 5

【检验方法】 显示全局LLDP的状态信息。
Ruijie(config)#show lldp status
Global status of LLDP : Enable
Neighbor information last changed time :
Transmit interval : 30s
Hold multiplier : 4
Reinit delay : 2s
Transmit delay : 2s
Notification interval : 5s
Fast start counts : 5


配置指南 LLDP

**常见配置错误**

-

###### 12.4.6 配置 TTL 乘数和 LLDP 报文发送时间间隔

**配置效果**

 改变TTL乘数的值。

 改变LLDP报文发送时间间隔。

**注意事项**

-

**配置方法**

 可选配置。

 全局配置模式下进行配置。

**检验方法**

显示接口下LLDP的状态信息。

 检查接口下LLDP的工作模式是否和配置的相同。

**相关命令**

######  配置 TTL 乘数

```
【命令格式】 lldp hold-multiplier value
【参数说明】 value：TTL乘数，缺省为 4 ，配置范围为 2 - 10
【命令模式】 全局模式
【使用指导】 LLDP报文中Time To Live TLV的值=TTL乘数×报文发送时间间隔+1。因此，通过调整TTL乘数可以控制本
设备信息在邻居设备的存活时间。
```

######  恢复缺省 TTL 乘数

```
【命令格式】 no lldp hold-multiplier
【参数说明】 -
【命令模式】 全局模式
```

配置指南 LLDP

```
【使用指导】 LLDP报文中Time To Live TLV的值=TTL乘数×报文发送时间间隔+1。因此，通过调整TTL乘数可以控制本
设备信息在邻居设备的存活时间。
```

######  配置 LLDP 报文发送时间间隔

```
【命令格式】 lldp timer tx-interval seconds
【参数说明】 seconds：LLDP报文的发送时间间隔，可配置范围为 5 - 32768
【命令模式】 全局模式
【使用指导】 -
```

######  恢复缺省 LLDP 报文发送时间间隔

```
【命令格式】 no lldp timer tx-interval
【参数说明】 -^
【命令模式】 全局模式
【使用指导】 -
```

**配置举例**

######  配置 LLDP 工作模式

【配置方法】 配置TTL乘数为 3 ，LLDP报文的发送间隔为 20 秒，此时，本地设备信息在邻居设备的存活时间为 61 秒
Ruijie(config)#lldp hold-multiplier 3
Ruijie(config)#lldp timer tx-interval 20

【检验方法】 显示全局LLDP状态信息。
Ruijie(config)#lldp hold-multiplier 3
Ruijie(config)#lldp timer tx-interval 20
Ruijie(config)#show lldp status
Global status of LLDP : Enable
Neighbor information last changed time :
Transmit interval : 20s
Hold multiplier : 3
Reinit delay : 2s
Transmit delay : 2s
Notification interval : 5s
Fast start counts : 3

**常见配置错误**

-


配置指南 LLDP

###### 12.4.7 配置 LLDP 报文的发送延迟时间

**配置效果**

 改变LLDP报文的发送延迟时间。

**注意事项**

-

**配置方法**

 可选配置。

 用户可根据实际需要在全局配置模式下进行配置。

**检验方法**

显示全局LLDP的状态信息。

 检查LLDP报文的发送延迟时间是否和配置的相同。

**相关命令**

######  配置 LLDP 报文的发送延迟时间

```
【命令格式】 lldp timer tx-delay seconds
【参数说明】 seconds：LLDP报文的发送延迟时间，可配置范围为 1 - 8192
【命令模式】 全局模式
【使用指导】 当本地信息发生变化时，会立即向邻居设备发送LLDP报文。为了避免本地信息频繁变化引起的频繁地发送
LLDP报文，可以配置LLDP报文的发送延迟时间来限制LLDP报文的频繁发送。
```

######  恢复缺省的 LLDP 报文的发送延迟时间

```
【命令格式】 no lldp timer tx-delay
【参数说明】 -
【命令模式】 全局模式
【使用指导】 当本地信息发生变化时，会立即向邻居设备发送LLDP报文。为了避免本地信息频繁变化引起的频繁地发送
LLDP报文，可以配置LLDP报文的发送延迟时间来限制LLDP报文的频繁发送。
```

**配置举例**

######  配置 LLDP 报文的发送延迟时间


配置指南 LLDP

【配置方法】 配置发送LLDP报文的延迟时间为 3 秒
Ruijie(config)#lldp timer tx-delay 3

【检验方法】 查看全局LLDP状态信息
Ruijie(config)#show lldp status
Global status of LLDP : Enable
Neighbor information last changed time :
Transmit interval : 30s
Hold multiplier : 4
Reinit delay : 2s
Transmit delay : 3s
Notification interval : 5s
Fast start counts : 3

**常见配置错误**

-

###### 12.4.8 配置端口初始化的延迟时间

**配置效果**

 改变端口初始化的延迟时间。

**注意事项**

 -

**配置方法**

 可选配置。

 用户可根据实际需要对端口状态机初始化的延迟时间进行配置。

**检验方法**

显示全局LLDP的状态信息。

 检查全局LLDP的端口初始化的延迟时间是否和配置的相同。

**相关命令**


配置指南 LLDP

######  配置端口初始化的延迟时间

```
【命令格式】 lldp timer reinit-delay seconds
【参数说明】 seconds：端口初始化的延迟时间，配置范围为 1 - 10 秒
【命令模式】 全局模式
【使用指导】 为了避免端口的工作模式的频繁变化引起的频繁地初始化状态机，可以配置端口初始化的延迟时间。
```

######  恢复缺省端口初始化的延迟时间

```
【命令格式】 no lldp timer reinit-delay
【参数说明】 -^
【命令模式】 全局模式
【使用指导】 为了避免端口的工作模式的频繁变化引起的频繁地初始化状态机，可以配置端口初始化的延迟时间。
```

**配置举例**

######  配置端口初始化的延迟时间

【配置方法】 配置端口初始化的延迟时间为 3 秒，并显示LLDP的状态信息。
Ruijie(config)#lldp timer reinit-delay 3

【检验方法】 显示全局LLDP的状态信息。
Ruijie(config)#show lldp status
Global status of LLDP : Enable
Neighbor information last changed time :
Transmit interval : 30s
Hold multiplier : 4
Reinit delay : 3s
Transmit delay : 2s
Notification interval : 5s
Fast start counts : 3

**常见配置错误**

-

###### 12.4.9 配置 LLDP Trap 功能

**配置效果**

 改变发送LLDP Trap信息的时间间隔。


配置指南 LLDP

**注意事项**

-

**配置方法**

######  打开 LLDP Trap 功能

 可选配置。

 接口配置模式下进行配置。

######  配置发送 LLDP Trap 信息的时间间隔

 可选配置。

 全局配置模式下进行配置。

**检验方法**

显示LLDP的状态信息。

 检查LLDP Trap功能是否打开。

 检查发送LLDP Trap信息的时间间隔和配置的相同。

**相关命令**

######  打开 LLDP Trap 功能

```
【命令格式】 lldp notification remote-change enable
【参数说明】 -^
【命令模式】 接口模式
【使用指导】 通过配置Trap功能，可以将本地设备的LLDP信息（例如发现新邻居、检测到与邻居的通信链路故障等信息）
发送给网管服务器，管理员可以根据此信息监控网络的运行状况。
```

######  关闭 LLDP Trap 功能

```
【命令格式】 no lldp notification remote-change enable
【参数说明】 -^
【命令模式】 接口模式
【使用指导】 通过配置Trap功能，可以将本地设备的LLDP信息（例如发现新邻居、检测到与邻居的通信链路故障等信息）
发送给网管服务器，管理员可以根据此信息监控网络的运行状况。
```

######  配置发送 LLDP Trap 信息的时间间隔

```
【命令格式】 lldp timer notification-interval seconds
```

配置指南 LLDP

```
【参数说明】 seconds：配置发送LLDP Trap信息的时间间隔，缺省的时间间隔是 5 秒，可配置的范围是 5 - 3600
【命令模式】 全局模式
【使用指导】 为了防止LLDP Trap信息的频繁发送，可以配置发送LLDP Trap的时间间隔。在这段时间间隔内，检测到LLDP
信息变化，将发送Trap给网管服务器。
```

######  恢复缺省的发送 LLDP Trap 信息的时间间隔

```
【命令格式】 no lldp timer notification-interval^
【参数说明】 -
【命令模式】 全局模式
【使用指导】 为了防止LLDP Trap信息的频繁发送，可以配置发送LLDP Trap的时间间隔。在这段时间间隔内，检测到LLDP
信息变化，将发送Trap给网管服务器。
```

**配置举例**

######  打开 LLDP Trap 功能及配置发送 LLDP Trap 信息的时间间隔

【配置方法】 使能LLDP Trap功能，并配置LLDP Trap信息的发送时间间隔为 10 秒。
Ruijie(config)#lldp timer notification-interval 10
Ruijie(config)#interface gigabitethernet 0/1
Ruijie(config-if-GigabitEthernet 0/1)#lldp notification remote-change enable

【检验方法】 显示LLDP的状态信息。
Ruijie(config-if-GigabitEthernet 0/1)#show lldp status
Global status of LLDP : Enable
Neighbor information last changed time :
Transmit interval : 30s
Hold multiplier : 4
Reinit delay : 2s
Transmit delay : 2s
Notification interval : 10s

Fast start counts : 3
------------------------------------------------------------

Port [GigabitEthernet 0/1]
------------------------------------------------------------

Port status of LLDP : Enable
Port state : UP
Port encapsulation : Ethernet II
Operational mode : RxAndTx
Notification enable : YES
Error detect enable : YES
Number of neighbors : 0
Number of MED neighbors : 0


配置指南 LLDP

**常见配置错误**

-

###### 12.4.10 配置 LLDP 错误检测功能

**配置效果**

 LLDP错误检测功能打开，当LLDP检测到错误时，将打印LOG信息提示管理员。

 配置LLDP错误检测功能，错误检测包括链路两端的VLAN配置检测、端口状态检测、端口聚合配置检测、MTU配置检
测及环路检测

**注意事项**

-

**配置方法**

 可选配置。

 用户可根据实际需要在接口模式下进行配置，打开或关闭LLDP错误检测功能。

**检验方法**

显示接口下LLDP的状态信息。

 检查接口下LLDP错误检测功能是打开还是关闭，与实际配置是否一致。

**相关命令**

######  打开 LLDP 错误检测功能

```
【命令格式】 lldp error-detect^
【参数说明】 -
【命令模式】 接口模式
【使用指导】 LLDP错误检测功能是依靠链路两端的设备交互LLDP报文中的特定的TLV信息进行的，为了保证检测功能的
正确运行，需要设备发布正确的TLV信息。
```

######  关闭 LLDP 错误检测功能

```
【命令格式】 no lldp error-detect
【参数说明】 -
```

配置指南 LLDP

```
【命令模式】 接口模式
【使用指导】 LLDP错误检测功能是依靠链路两端的设备交互LLDP报文中的特定的TLV信息进行的，为了保证检测功能的
正确运行，需要设备发布正确的TLV信息。
```

**配置举例**

######  打开 LLDP 错误检测功能

【配置方法】 打开LLDP在接口GI 0/1下的错误检测功能。
Ruijie(config)#interface gigabitethernet 0/1
Ruijie(config-if-GigabitEthernet 0/1)#lldp error-detect

【检验方法】 显示LLDP在接口下的状态信息。
Ruijie(config-if-GigabitEthernet 0/1)#show lldp status interface gigabitethernet 0/1
Port [GigabitEthernet 0/1]
Port status of LLDP : Enable
Port state : UP
Port encapsulation : Ethernet II
Operational mode : RxAndTx
Notification enable : NO
Error detect enable : YES
Number of neighbors : 0
Number of MED neighbors : 0

**常见配置错误**

-

###### 12.4.11 配置 LLDP 报文封装格式

**配置效果**

 改变LLDP报文的封装格式。

**注意事项**

-

**配置方法**


配置指南 LLDP

 可选配置。

 用户可根据实际需要在接口下改变LLDP报文的封装格式。

**检验方法**

显示接口下LLDP的状态信息。

 检查接口下LLDP报文封装格式是否和配置的相同。

**相关命令**

######  配置 LLDP 报文的封装格式为 SNAP

```
【命令格式】 lldp encapsulation snap
【参数说明】 -
【命令模式】 接口模式
【使用指导】
```

### 为了保证本地设备和邻居设备的正常通信，需要将LLDP报文配置成相同的封装格式。^

######  恢复缺省的 LLDP 报文的封装格式，即为 Ethernet II

```
【命令格式】 no lldp encapsulation snap^
【参数说明】 -
【命令模式】 接口模式
【使用指导】
```

### 为了保证本地设备和邻居设备的正常通信，需要将LLDP报文配置成相同的封装格式。^

**配置举例**

######  配置 LLDP 报文的封装格式为 SNAP

【配置方法】 配置LLDP报文的封装格式为SNAP。
Ruijie(config)#interface gigabitethernet 0/1
Ruijie(config-if-GigabitEthernet 0/1)#lldp encapsulation snap

【检验方法】 显示LLDP在接口下的状态信息。
Ruijie(config-if-GigabitEthernet 0/1)#show lldp status interface gigabitethernet 0/1
Port [GigabitEthernet 0/1]
Port status of LLDP : Enable
Port state : UP
Port encapsulation : Snap
Operational mode : RxAndTx
Notification enable : NO
Error detect enable : YES


配置指南 LLDP

```
Number of neighbors : 0
Number of MED neighbors : 0
```

**常见配置错误**

-

###### 12.4.12 配置 LLDP Network Policy 策略

**配置效果**

 改变LLDP Network Policy策略。

 当设备下联IP电话，若IP电话支持LLDP-MED，则可以通过配置Network Policy TLV下发策略给IP电话，由IP电话
修改语音流Tag和QOS。在设备上，除配置上述策外，还需要配置步骤为：1.使能Voice VLAN功能，把连接IP电话的
端口静态加入Voice VLAN；2.把连接IP电话的端口配置为QOS信任口（推荐使用信任DSCP模式）；3.如果在此端口
上同时开启了1X认证，则还需要配置一条安全通道，允许Voice VLAN内的报文通过。若IP电话不支持LLDP-MED，
则必须使能Voice VLAN功能，并将话机MAC地址手动配置到Voice VLAN OUI列表中。

 QOS信任模式的配置方法请参见《IP QOS》章节；Voice VLAN的配置方法请参见《Voice VLAN》章节；安全通道的配
置方法请参见《ACL》章节。

**注意事项**

-

**配置方法**

 可选配置。

 用户可根据实际需要配置LLDP Network Policy策略。

**检验方法**

显示本地设备的LLDP network-policy配置策略信息。

 检查LLDP Network Policy策略是否和配置的相同。

**相关命令**

######  配置 LLDP Network Profile 策略

```
【命令格式】 lldp network-policy profile profile-num
```

配置指南 LLDP

```
【参数说明】 profile-num：LLDP network-policy策略的标识，范围为： 1 - 1024
【命令模式】 全局模式
【使用指导】 使用此命令进入LLDP network-policy配置模式，使用此命令时需要指定策略ID。
进入LLDP network-policy配置模式后，可使用{ voice | voice-signaling } vlan命令配置具体的network-policy
策略。
```

######  删除 LLDP Network Profile 策略

```
【命令格式】 no lldp network-policy profile profile-num
【参数说明】 profile-num：LLDP network-policy策略的标识，范围为： 1 - 1024
【命令模式】 接口模式
【使用指导】 使用此命令进入LLDP network-policy配置模式，使用此命令时需要指定策略ID。
进入LLDP network-policy配置模式后，可使用{ voice | voice-signaling } vlan命令配置具体的network-policy
策略。
```

**配置举例**

######  配置 LLDP Network Profile 策略

【配置方法】 配置接口 1 发布的LLDP报文中Network Policy TLV策略为 1 ：voice应用类型vlan id是 3 ，cos是 4 ，
dscp是 6 。
Ruijie#config
Ruijie(config)#lldp network-policy profile 1
Ruijie(config-lldp-network-policy)# voice vlan 3 cos 4
Ruijie(config-lldp-network-policy)# voice vlan 3 dscp 6
Ruijie(config-lldp-network-policy)#exit
Ruijie(config)# interface gigabitethernet 0/1
Ruijie(config-if-GigabitEthernet 0/1)# lldp tlv-enable med-tlv network-policy profile 1

【检验方法】 显示本地设备的LLDP network-policy配置策略信息。

network-policy information:
--------------------------

network policy profile :1
voice vlan 3 cos 4
voice vlan 3 dscp 6

**常见配置错误**

-


配置指南 LLDP

###### 12.4.13 配置设备的普通地址信息

**配置效果**

 设备的地址信息发生变化。

**注意事项**

-

**配置方法**

 可选配置。

 用户可根据实际需要配置设备的普通地址信息。

**检验方法**

显示本地设备的LLDP普通地址信息。

 检查LLDP普通地址信息是否和配置的相同。

**相关命令**

######  配置设备的普通地址信息

```
【命令格式】 配置LLDP普通地址信息。用户可以使用no选项删除地址信息。
{ country | state | county | city | division | neighborhood | street-group | leading-street-dir |
trailing-street-suffix | street-suffix | number | street-number-suffix | landmark |
additional-location-information | name | postal-code | building | unit | floor | room | type-of-place |
postal-community-name | post-office-box | additional-code } ca-word
【参数说明】 country：国家代码， 2 个字符。china：CH
state：地址信息CA类型为 1
county：CA类型为 2
city：CA类型为 3
division：CA类型为 4
neighborhood：CA类型为 5
street-group：CA类型为 6
leading-street-dir：CA类型为 16
trailing-street-suffix：CA类型为 17
street-suffix：CA类型为 18
number：CA类型为 19
```

配置指南 LLDP

```
street-number-suffix：CA类型为 20
landmark：CA类型为 21
additional-location-information：CA类型为 22
name：CA类型为 23
postal-code： CA类型为 24
building：CA类型为 25
unit：CA类型为 26
floor：CA类型为 27
room：CA类型为 28
type-of-place：CA类型为 29
postal-community-name：CA类型为 30
post-office-box：CA类型为 31
additional-code：CA类型为 32
ca-word： 地址信息
【命令模式】 LLDP Civic Address配置模式
【使用指导】 进入LLDP Civic Address配置模式后，配置LLDP普通地址信息。
```

######  删除设备的普通地址信息

```
【命令格式】 no { country | state | county | city | division | neighborhood | street-group | leading-street-dir |
trailing-street-suffix | street-suffix | number | street-number-suffix | landmark |
additional-location-information | name | postal-code | building | unit | floor | room | type-of-place |
postal-community-name | post-office-box | additional-code }
【参数说明】 -
【命令模式】 LLDP Civic Address配置模式
【使用指导】 进入LLDP Civic Address配置模式后，配置LLDP普通地址信息。
```

######  配置设备类型信息

```
【命令格式】 device-type device-type
【参数说明】 device-type：设备类型，缺省为 1 ，取值范围为 0 - 2
0 表示设备类型为DHCP Server
1 表示设备类型为Switch
2 表示设备类型为LLDP MED终端
【命令模式】 LLDP Civic Address配置模式
【使用指导】 进入LLDP Civic Address配置模式后，配置LLDP普通地址中设备类型信息。
```

######  恢复设备类型信息

```
【命令格式】 no device-type
【参数说明】 -
【命令模式】 LLDP Civic Address配置模式
【使用指导】 进入LLDP Civic Address配置模式后，恢复LLDP普通地址中设备类型信息为缺省值。
```

配置指南 LLDP

**配置举例**

######  配置设备的普通地址信息

【配置方法】 配置设备接口 1 的地址为：交换机设备，地址是国家：CH，城市：Fuzhou，邮编： 350000 。
Ruijie#config
Ruijie(config)#lldp location civic-location identifier 1
Ruijie(config-lldp-civic)# country CH
Ruijie(config-lldp-civic)# city Fuzhou
Ruijie(config-lldp-civic)# postal-code 350000

【检验方法】 显示设备接口 1 的LLDP普通地址信息。

civic location information:^
--------------------------

Identifier :1
country :CH
device type :1
city :Fuzhou
postal-code :350000

**常见配置错误**

-

###### 12.4.14 配置设备的紧急电话号码信息

**配置效果**

 更改设备的紧急电话号码信息。

**注意事项**

-

**配置方法**

 可选配置。

 用户可根据实际需要配置设备的紧急电话号码信息。


配置指南 LLDP

**检验方法**

显示本地设备的紧急电话号码信息。

 检查本地设备的紧急电话号码信息是否和配置的相同。

**相关命令**

######  配置设备的紧急电话号码信息

```
【命令格式】 lldp location elin identifier id elin-location tel-number
【参数说明】 id：表示紧急电话号码信息的配置标识号，范围为： 1 - 1024
tel-number：表示紧急电话号码，范围： 10 – 25 字节
【命令模式】 全局模式
【使用指导】 使用此命令来配置紧急电话号码信息。
```

######  删除设备的紧急电话号码信息

```
【命令格式】 no lldp location elin identifier id
【参数说明】 id：表示紧急电话号码信息的配置标识号，范围为： 1 - 1024
【命令模式】 全局模式
【使用指导】 -
```

**配置举例**

######  配置设备的紧急电话号码信息

【配置方法】 配置设备接口 1 的紧急电话号码为： 085285555556 。
Ruijie#config
Ruijie(config)#lldp location elin identifier 1 elin-location 085283671111

【检验方法】 显示设备接口 1 的紧急电话号码信息。

elin location information:
-------------------------

Identifier :1
elin number :085283671111

**常见配置错误**

-


配置指南 LLDP

###### 12.4.15 配置兼容友商邻居发现功能

**配置效果**

 打开或关闭兼容友商邻居发现功能。

**注意事项**

-

**配置方法**

 可选配置。

 全局下配置兼容友商邻居发现功能。

**检验方法**

显示LLDP的状态信息。

 检查全局兼容友商邻居发现功能是否开启。

**相关命令**

######  打开兼容友商邻居发现功能

```
【命令格式】 lldp compliance vendor
【参数说明】 -^
【命令模式】 全局模式
【使用指导】
```

######  关闭兼容友商邻居发现功能

```
【命令格式】 no lldp compliance vendor
【参数说明】 -
【命令模式】 全局模式
【使用指导】 -^
```

**配置举例**

######  配置兼容友商邻居发现功能

```
【配置方法】 配置兼容友商邻居发现功能。
```

配置指南 LLDP

```
Ruijie(config)# lldp compliance vendor
```

```
【检验方法】 显示LLDP全局状态信息。
Ruijie(config)#show lldp status
Global status of LLDP : Enable
Global vendor compliance : YES
```

**常见错误**

-

###### 12.4.16 配置获取全局 LLDP 管理地址的类型

**配置效果**

 配置获取全局LLDP管理地址的类型，可使管理地址的选取顺序发生改变。

 配置获取全局LLDP管理地址的类型恢复到缺省配置将使LLDP报文中的管理地址按缺省情况下选取。

**注意事项**

 LLDP运行在实际的物理接口上（对于AP口，则实际是运行在AP成员口上）。堆叠口，VSL口不支持LLDP。

**配置方法**

 可选配置。

 全局配置获取全局LLDP管理地址的类型。

**检验方法**

 显示本地设备接口下的LLDP管理地址信息。

 检查本地设备接口下的LLDP管理地址信息是否按照配置的使用类型顺序获取。

**相关命令**

######  配置获取全局 LLDP 管理地址的类型

```
【命令格式】 lldp management-address-tlv global-ip type^ {interface^ |^ loopback}^
【参数说明】 interface：LLDP报文中发布的管理地址使用接口下的IP地址
```

(^) loopback **：** LLDP报文中发布的管理地址使用Loopback口下的IP地址


配置指南 LLDP

```
【命令模式】 全局配置模式
【使用指导】 缺省情况下，对于端口上发布的管理地址，LLDP获取的顺序按优先级从高到低依次为：LLDP管理地址配置，
Mgmt口IP地址配置，SVI口IP地址配置（路由口使用自身的IP地址），本机地址127.0.0.1，最后是系统
MAC地址
使用该命令配置获取全局LLDP管理地址类型为Interface后，获取的顺序按优先级从高到低依次为：LLDP
管理地址配置，SVI口IP地址配置（路由口使用自身的IP地址），本机地址127.0.0.1，最后是系统MAC地
址
使用该命令配置获取全局LLDP管理地址类型为Loopback后，获取的顺序按优先级从高到低依次为：LLDP
管理地址配置，Loopback口IP地址配置，SVI口IP地址配置（路由口使用自身的IP地址），本机地址127.0.0.1，
最后是系统MAC地址
```

######  配置获取全局 LLDP 管理地址的类型恢复缺省

```
【命令格式】 {no | default} lldp management-address-tlv global-ip
【参数说明】 -
【命令模式】 全局配置模式
```

【使用指导】 (^) 缺省情况下，对于端口上发布的管理地址，LLDP获取的顺序按优先级从高到低依次为：LLDP管理地址配置，
Mgmt口IP地址配置，SVI口IP地址配置（路由口使用自身的IP地址），本机地址127.0.0.1，最后是系统
MAC地址
使用该命令配置获取全局LLDP管理地址类型为Interface后，获取的顺序按优先级从高到低依次为：LLDP
管理地址配置，SVI口IP地址配置（路由口使用自身的IP地址），本机地址127.0.0.1，最后是系统MAC地
址
使用该命令配置获取全局LLDP管理地址类型为Loopback后，获取的顺序按优先级从高到低依次为：LLDP
管理地址配置，LOOPBACK口IP地址配置，SVI口IP地址配置（路由口使用自身的IP地址），本机地址
127.0.0.1，最后是系统MAC地址
**配置举例**

######  配置获取全局 LLDP 管理地址的类型

【配置方法】 配置获取全局LLDP管理地址的类型为Interface
Ruijie(config)#lldp management-address-tlv global-ip type interface

【检验方法】 先配置Mgmt口的IP地址，然后查看LLDP的本地配置信息，此时使用的是Mgmt口的IP地址
Ruijie(config)#show lldp local-information int gi1/0/1

LLDP local-information of port [TenGigabitEthernet 1/0/1]
----------------------------------------------------------------------------

Port ID type : Interface name
Port ID : TenGigabitEthernet 1/0/1
Port description : TenGigabitEthernet 1/0/1

```
Management address subtype : ipv4
```

配置指南 LLDP

```
Management address : 172.30.32.217
Interface numbering subtype : ifIndex
Interface number : 8194
Object identifier :
```

```
802.1 organizationally information
Port VLAN ID : 1
Port and protocol VLAN ID(PPVID) : 0
PPVID Supported : YES
PPVID Enabled : NO
VLAN name of VLAN 1 : VLAN0001
Protocol Identity :
然后配置获取全局LLDP管理地址的类型为Interface，查看LLDP的本地配置信息，此时使用的是SVI口的
IP地址
Ruijie(config)# lldp management-address-tlv global-ip type interface
Ruijie(config)#show lldp local-information int gi1/0/1
LLDP local-information of port [TenGigabitEthernet 1/0/1]
----------------------------------------------------------------------------
Port ID type : Interface name
Port ID : TenGigabitEthernet 1/0/1
Port description : TenGigabitEthernet 1/0/1
```

```
Management address subtype : ipv4
Management address : 172.30.32.2 35
Interface numbering subtype : ifIndex
Interface number : 4097
Object identifier :
```

```
802.1 organizationally information
Port VLAN ID : 1
Port and protocol VLAN ID(PPVID) : 0
PPVID Supported : YES
PPVID Enabled : NO
VLAN name of VLAN 1 : VLAN0001
Protocol Identity :
然后配置LLDP报文发布的管理地址使用类型为Loopback，查看LLDP的本地配置信息，此时使用的是Mgmt
口的IP地址，新建Loopback口，并且配置IP地址，查看LLDP的本地配置信息，此时使用的是Loopback
口的IP地址
Ruijie(config)# lldp management-address-tlv global-ip type loopback
```

配置指南 LLDP

```
Ruijie(config)#show lldp local-information int gi1/0/1
LLDP local-information of port [TenGigabitEthernet 1/0/1]
----------------------------------------------------------------------------
Port ID type : Interface name
Port ID : TenGigabitEthernet 1/0/1
Port description : TenGigabitEthernet 1/0/1
```

```
Management address subtype : ipv4
Management address : 7.1.1.1
Interface numbering subtype : ifIndex
Interface number : 16385
Object identifier :
```

```
802.1 organizationally information
Port VLAN ID : 1
Port and protocol VLAN ID(PPVID) : 0
PPVID Supported : YES
PPVID Enabled : NO
VLAN name of VLAN 1 : VLAN0001
Protocol Identity :
```

**常见配置错误**

-

#### 12.5 监视与维护

**清除各类信息**

### 在设备运行过程中执行clear命令，可能因为重要信息丢失而导致业务中断。^

作用 命令
清除LLDP的统计信息。 clear lldp statistics^ [^ interface interface-name^ ]^
清除LLDP的邻居信息。 clear lldp table [ interface interface-name ]

**查看运行情况**

作用 命令


配置指南 LLDP

显示本地设备的LLDP信息，这些信息
将被组织成TLV发送给邻居设备。

```
show lldp local-information [ global | interface interface-name ]
```

显示本地设备的LLDP普通地址信息
或者紧急电话号码信息。

show lldp location { civic-location | elin-location } { identifier id | interface
interface-name | static }
显示邻居设备的LLDP信息。 show lldp neighbors [ interface interface-name ] [ detail ]
显示本地设备的LLDP network-policy
配置策略信息

```
show lldp network-policy { profile [ profile-num ] | interface interface-name }
```

显示LLDP的统计信息。 show lldp statistics [ global | interface interface-name ]
显示LLDP的状态信息。 show lldp status [ interface interface-name ]
显示端口上可发布的TLV配置信息。 show lldp tlv-config [interface interface-name ]

**查看调试信息**

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。

作用 命令
打开LLDP错误处理的调试开关。 debug lldp error
打开LLDP事件处理的调试开关。 debug lldp event^
打开LLDP热备份处理的调试开关。 debug lldp ha
打开LLDP报文接收的调试开关。 debug lldp packet
打开LLDP状态机相关的调试开关。 debug lldp stm


配置指南 QINQ

### 13 QINQ

#### 13.1 概述

QinQ技术是指在用户报文进入服务提供商网络之前封装上一个服务提供商网络的公网VLAN Tag，而把用户报文中的私网用户
VLAN Tag当做数据，使报文带着两层VLAN Tag穿越服务提供商网络。
在城域网中需要大量的VLAN来隔离用户，IEEE 802.1Q协议仅支持的 4094 个VLAN远远不能满足需求。通过QinQ技术双
层Tag封装，在服务提供商网络中报文只根据公网上分配的唯一外层VLAN Tag传播，这样不同的私网用户VLAN可以重复使
用，实际上扩大了用户可利用的VLAN Tag数量，同时提供一种简单的二层VPN功能。
下图显示了双Tag添加的过程：边界设备的入口称为dot1q-tunnel port或简称tunnel port，所有进入边界设备的帧都被当作是
Untagged 帧，而不管它实际上是Untagged还是已经带802.1Q Tag头的帧，都被封装上服务商的Tag，VLAN号为Tunnel port
的缺省VLAN。

图 13 - 1 外Tag封装

**协议规范**

 IEEE 802.1ad

#### 13.2 典型应用

典型应用 场景描述
基于端口的基本QinQ实现二层VPN 企业A、B的数据在传送至对端时可以保留原有VLAN信息，同时两个企业相同VLAN
编号的数据在服务提供商网络中传输时不会产生冲突。
基于C-TAG的灵活QinQ实现二层
VPN和业务流管理

```
可以根据不同业务VLAN分配更灵活的外Tag，一方面可以实现二层VPN；另一方面
实现带宽上网、IPTV等多种业务的有效区分和实行不同的QOS服务策略，比基本QinQ
更为灵活。
```

```
配置指南 QINQ
```

```
基于ACL的灵活QinQ实现二层VPN
和业务流管理
```

```
根据ACL对下连用户的宽带上网、IPTV等多种业务进行区分，通过灵活QinQ以便针
对不同业务流实行不同的QOS服务策略。
VLAN-MAPPING 实现不同业务的
```

###### VLAN聚合

```
用户的不同业务（PC、IPTV、VOIP）分别采用不同的VLAN进行部署，在园区网上进
行VLAN汇聚，将由多个VLAN发送的不同用户的相同业务采用同一个VLAN进行发
送，节约VLAN资源。
基于QinQ实现二层协议透传：BPDU
和GVRP
```

```
处于不同地域的客户网络A和B可以跨越服务提供商网络进行MSTP统一生成树计算
或VLAN部署，而不影响服务商网络。
```

###### 13.2.1 基于端口实现二层 VPN 业务

**应用场景**

```
服务提供商为企业A和企业B提供VPN：
 在公网上企业A和企业B属于不同的VLAN，各自通过所属的公网VLAN通信。
 企业A和企业B内的VLAN对公网来说是透明的，企业A和企业B内的用户VLAN可以重复使用并且不冲突。
 Tunnel会对用户数据报文再封装一层Native VLAN的VLAN Tag。在公网中用户数据报文以Native VLAN传播，不影响
不同企业用户网络的VLAN使用，并实现简单的二层VPN。
图 13 - 2
```

【注释】 Customer A1和Customer A2、Customer B1和Customer B2分别为企业用户A、企业用户B所在网络的边缘设
备。
Provider A和Provider B为服务提供商网络边缘设备，企业A和企业B通过提供商边缘设备接入公网。
企业A使用的办公网络VLAN范围为VLAN 1- 100 。
企业B使用的办公网络VLAN范围为VLAN 1- 200 。

**功能部属**

```
 下连用户网络的数据无需区分，在服务提供商边缘设备上启用基本QinQ即能二层VPN的需求。
 交换机(包括锐捷交换机)普遍的TPID值是0x8100，但存在部分厂商的交换机TPID值采用的不是0x8100，这时需在在
服务提供商网络边缘设备Uplink接口上将TPID值调整为与第三方设备一样的值。
```

配置指南 QINQ

 在提供商网络边缘设备Tunnel口上设置cos的优先级复制和优先级映射功能，并设置cos的QOS策略(详见QOS策略
配置文档)，使用户数据报文享用不同的QOS策略。

###### 13.2.2 基于 C-Tag 的灵活 QinQ 实现二层 VPN 和业务流管理

**应用场景**

基本QinQ只能将用户数据报文封装一层Native VLAN的外Tag，即外层Tag的封装依赖于Tunnel口的Native VLAN。灵活
QinQ提供根据用户报文的Tag(即C-Tag)来灵活封装服务提供商(ISP)的外Tag(即S-Tag)，以便更灵活实现VPN透传和业务流
QOS策略。
 宽带上网、IPTV业务都是城域网的所承载业务的重要部分，城域网服务商网络针对不同业务流划分VLAN来区分管理，
并提供针对这些VLAN或cos设置了QOS策略服务。可以在服务商边缘设备上运用基于C-Tag的QinQ将用户的业务流
封装相关的VLAN，在透传的同时利用服务商网络的QOS策略进行保障性传输。
 企业分公司之间实现了统一的VLAN规划，重要业务和一般业务分别在不同的VLAN范围内，企业网可以利用基于C-Tag
的灵活QinQ透传公司内部的业务，又能利用服务商网络的QOS策略优先保障重要业务的数据传输。
如下图所示，城域网内用户端设备通过小区的楼道交换机汇聚，宽带上网、IPTV业务通过分配不同的VLAN进行区分，分别
享用不同的QOS服务策略。
 在公网中，宽带上网和IPTV的不同业务流以不同的VLAN传播，实现用户业务的透传。
 ISP网络针对VLAN或者cos设置了QOS策略，在服务商边缘设备上可以针对用户业务封装对应的VLAN或设置cos，
使得用户业务在ISP网络中优先传输。
 可以通过优先级映射或优先级复制灵活改变用户业务报文的cos值，灵活运用服务商网络中的QOS服务策略。

图 13 - 3

【注释】 CE1和CE2为连接用户网络的边缘设备，PE1和PE2为提供商服务网络边缘设备。
CE1和CE2设备上VLAN 1- 100 为用户宽带上网业务流，VLAN 101- 200 为用户IPTV业务流。
PE1和PE2设备上配置Tunnel口和VLAN映射以区分不同的业务数据。

**功能部属**

 在服务商网络边缘设备PE1和PE2连接用户网络设备的接口（如本例PE1和PE2的G0/1）上配置基于C-Tag的灵活
QinQ，实现业务流的划分和透传。


```
配置指南 QINQ
```

```
 如果ISP网络基于VLAN或cos设定了QOS策略，在PE1和PE2设备上将用户业务流映射到相关的VLAN、或通过优
先级映射和优先级复制修改报文的cos值，以便用户网络的业务流能使用ISP网络的QOS策略保障传输。
```

###### 13.2.3 基于 ACL 的灵活 QinQ 实现二层 VPN 和业务流管理

**应用场景**

```
用户网络不是根据VLAN而是根据MAC、IP、或协议类型等来划分业务流、或者用户网络存在大量老式的低端网络接入设备，
无法通过VLAN ID对业务流进行有效的区分时，这时无法根据C-Tag为用户网络封装外层Tag用以透传和实施QOS策略。
ACL可以根据MAC、IP、协议类型等来划分业务流，灵活QinQ借助于ACL来区分不同业务添加和修改外层Tag，从而针对
不同业务数据实现VPN和QOS服务策略。
以下图为例，PE1和PE2根据ACL划分的业务流分配不同的VLAN实现用户业务透传，如果ISP网络中针对不同业务提供了
不同的QOS服务策略，则可以保障一些业务的优先传输。
 不同业务数据被封装不同的外层VLAN Tag，企业数据可以实现透传，企业分公司之间能够互访。
 通过封装不同的VLAN或设置报文的cos值，利用ISP网络针对VLAN或cos实施的QOS策略优先保障相应业务的数
据传输。
图 13 - 4
```

【注释】 CE1和CE2为用户网络的边缘设备，PE1和PE2为提供商服务网络边缘设备。
PE1和PE2设备上基于ACL进行流分类：acl1识别PPPOE协议类型业务流，acl2识别IPTV(IPOE)协议类型业
务流。
PE1和PE2设备上配置Tunnel口，并针对不同的ACL识别的业务流设置外Tag策略。

**功能部属**

```
 服务商网络边缘设备（PE1和PE2）上配置ACL，用于区分和规划不同的业务数据。
 在服务商网络边缘设备连接用户网络的的接口（本例为PE1和PE2G0/1口）上，配置基于ACL的灵活QinQ功能，对
用户业务进行区分及分流。
 如果ISP网络基于VLAN或cos设定了QOS策略，在PE1和PE2设备上将用户业务流映射到相关的VLAN、或通过优
先级映射和优先级复制修改报文的cos值，以便用户网络的业务流能使用ISP网络的QOS策略保障传输。
```

```
配置指南 QINQ
```

###### 13.2.4 基于 VLAN-MAPPING 实现不同业务的聚合

**应用场景**

###### 在一个园区网络环境中区分不同家庭用户的不同业务流。

```
 家庭的不同业务，采用不同的VLAN进行部署；为了方便部署，不同家庭的网关设备，相同业务采用相同VLAN。
 不同家庭的相同业务采用相同VLAN，需要对不同家庭的相同业务报文之间需要进行隔离，不能产生混淆。
 从园区交换机发出去的不同家庭的相同业务报文采用同一个VLAN进行发送，以便节省 VLAN资源。
图 13 - 5
```

【注释】 PC、IPTV、VOIP分别区分用户的不同业务。
Switch A和 Switch B均为不同用户的网关设备。
Switch C为楼道交换机。
Switch D为园区交换机。

**功能部属**

```
 在家庭网关设备上，PC业务使用VLAN 10，IPTV业务使用VLAN 11，VoIP业务使用VLAN 12，即不同业务采用不同
的VLAN，用以区分不同的业务数据。
 在楼道交换机（在本例中的Switch D）用户网关连接的接口配置VLAN映射，将不同用户的不同业务数据映射到不同的
VLAN，实现区分不同用户的业务数据。
 在园区交换机上将不通的业务数据映射到不同的VLAN，实现不同业务的区分。
 通过以上部署，整体上不同家庭用户的不同业务数据能实现明确的识别而不混淆。
```

```
配置指南 QINQ
```

###### 13.2.5 基于 QinQ 实现二层协议透传： BPDU 和 GVRP

**应用场景**

```
在一个网络中，用户网络之间的二层协议报文不对运营商网络产生影响。
 用户网络中的二层协议报文对运营商网络是透明的，可以从用户一端网络传到用户另一端网络，对运营商网络不产
生影响。
图 13 - 6
```

【注释】 Customer S1和Customer S2为用户的两端网络边缘设备。
Provider S1和Provider S1为运营商网络的边缘设备。
Provider S1和Provider S1设备上配置全局二层协议透传功能，并在端口GI 0/1和GI 0/10开启二层协议透传功能。

**功能部属**

```
 在服务提供商边缘设备（本例为Provider S1/Provider S2）连接用户网络的边缘设备的接口上，配置用户所需要透传的二
层协议功能，实现用户网络的二层协议报文透明传输，而不影响运营商的网络配置和拓扑。
 根据用户需要配置stp协议透传功能，实现用户网络的BPDU报文在运营商网络进行隧道传输，使跨地域的用户网络跨
越服务提供商网络统一生成树计算。
 根据用户需要配置GVRP协议透传功能，实现用户网络的GVRP报文透传，实现跨网络的用户网络的动态VLAN配置。
```

#### 13.3 功能详解

**基本概念**

######  基本QinQ


配置指南 QINQ

基本QinQ功能，将接口模式设置为dot1q-tunnel并配置一个Native VLAN，报文从这个接口进来会被封装一层外层Tag为
Native VLAN的Tag。基本QinQ基于端口为报文封装Native VLAN，不能区分从端口进来的各种流，也不能灵活选择VLAN
来封装，不够灵活。

######  灵活QinQ

灵活QinQ主要有两种：基于C-Tag（Client VLAN Tag）的灵活QinQ和基于ACL的灵活QinQ。
基于C-Tag的灵活QinQ，根据用户的VLAN来封装外层Tag，用以区分不同类型的流和实现透传。
基于ACL的灵活QinQ，ACL策略能区分不同的业务流，基于ACL可以针对不同的流封装不同的VLAN实现透传。

######  TPID

以太网帧Tag包含四个字段：TPID(Tag Protocol Identifier，标签协议标志)、 User Priority、CFI、VLAN ID。
对于TPID值，缺省采用IEEE802.1Q协议规定的0x8100。也有部分厂商设备的TPID值为0x9100或其他值，为了和第三方
设备兼容，提供TPID值的设置，使得报文转发出去时TPID值与第三方设备兼容。

######  优先级映射和优先级复制

以太网帧Tag的User Priority默认为 0 ，为普通流。为了保证一些报文优先处理和传输，用户可以设置这个字段。这个字段值
对应QOS策略中的cos值，可以通过配置基于cos的QOS策略保证业务的优先先。
优先级复制：如果用户报文的VLAN Tag设置了用户优先级cos值，运营商网络中针对这个cos值设置了QOS优先级策略，
那么可以将用户报文VLAN Tag的cos值复制给外层Tag的cos，保证用户报文在运营商网络中沿用用户VLAN的优先级传输。
优先级映射：运营商网络针对多个的cos值设置了不同的QOS策略，对应不同的业务流服务。为了保证用户业务在运营商网
络享有优先传输的特性，可以根据用户报文VLAN Tag的cos值设置外层Tag的cos值。

######  二层协议透传

STP报文和GVRP报文进入运营商网络可能会影响网络的拓扑，而跨服务商网络的用户网络希望在统一内部拓扑的同时又不
影响服务商网络的拓扑。为了不影响运营商网络的拓扑，将用户网络的STP报文和GVRP报文在运营商网络透传，运营商网
络就不会被用户网络影响。

**功能特性**

功能特性 作用
基本QINQ 配置端口为dot1q-tunnel口，指明端口输出报文是否需要带Tag。
灵活QINQ 根据规则为不同的数据流打上不同的外层VLAN Tag。

VLAN-MAPPING (^) 将用户报文中的私网VLAN Tag 替换为公网的VLAN Tag，再按照同样的规则将VLAN Tag 恢复为
原有的用户私网VLAN Tag，使报文正确到达目的地。
TPID设置 对于TPID值，缺省采用IEEE802.1Q协议规定的0x8100。而某些厂商的设备将报文外层Tag的
TPID值设置为0x9100或其他值。为了和这些设备兼容，提供了基于端口的报文TPID可配置功能。
MAC地址复制 采用基于ACL的灵活QinQ时， 交换机学到的mac的vid是native vlan的。故当采用基于数据流
的vlan转换时，当报文从对端回来时候，就会发生无法查询到mac地址而泛洪的情况，此时可将
native vlan的mac地址复制到外层Tag所在的vlan中。
二层协议透传 实现用户网络之间二层协议报文的传输而又不对运营商网络产生影响。


配置指南 QINQ

优先级复制 服务商网络中基于用户VLAN Tag的User Priority设置了QOS优先级策略，可以通过优先级复制，
使外层VLAN Tag沿用用户VLAN的优先级策略。
优先级映射 添加外层VLAN Tag时，可以通过优先级映射，根据内层VLAN Tag的User Priority设置外层Tag
的User Priority，使报文封装外层Tag后能利用网络的QOS优先级策略。

###### 13.3.1 基本 QINQ

基本QinQ能简单实现二层VPN功能。实现简单，但外层VLAN Tag封装方式不够灵活。

**工作原理**

端口配置成tunnel口后，当该端口接收到报文，设备会为该报文打上tunnel口缺省VLAN 的VLAN Tag。如果接收到的已经
是带有VLAN Tag的报文，该报文就封装成为双Tag的报文；如果接收到的是不带VLAN Tag 的报文，该报文就封装成带有端
口缺省VLAN Tag 的报文。

###### 13.3.2 灵活 QINQ

灵活QinQ可以为不同的数据流打上不同的外层VLAN Tag，外层VLAN Tag封装方式灵活。

**工作原理**

灵活QINQ根据用户VLAN Tag、MAC地址、IP协议、源地址、目的地址、优先级、或应用程序的端口号等信息的不同，封
装不同的外层Tag。借助以上各种分类方法，实现不同用户、不同业务、不同优先级的报文进行外层VLAN Tag封装。
当前，在配置上可以使用的具体策略有：

 根据内层VLAN Tag添加外层VLAN Tag；

 根据外层VLAN Tag修改外层VLAN Tag；

 根据内层VLAN Tag修改外层VLAN Tag；

 根据内、外层VLAN Tag修改外层VLAN Tag；

 利用ACL，根据ACL添加外层VLAN Tag；

 利用ACL，根据ACL修改外层VLAN Tag；

 利用ACL，根据ACL修改内层VLAN Tag；

###### 13.3.3 VLAN-MAPPING

**工作原理**

VLAN Mapping 根据设置将用户报文中的私网VLAN Tag 替换为公网的VLAN Tag，使其用户报文按照公网的网络规划进行传
输。在报文被发送回用户私网时，再按照映射关系将VLAN Tag 恢复为原有的用户私网VLAN Tag，使报文正确到达目的地。
VLAN mapping支持以下两种映射关系：

 一对一VLAN mapping：将报文Tag的VID修改为另一个指定的Tag的VID。


配置指南 QINQ

 多对一VLAN mapping：将来自多个VLAN的报文Tag的VID修改为同一个Tag的VID。

######  一对一 VLAN mapping 的实现方式一

如下图所示：一对一VLAN MAPPING主要用在楼道交换机处，以用不同的VLAN承载不同用户的相同业务，以区分不同的用
户。
图 13 - 7

 对于上行数据流，通过在上图所示的下行端口上配置输入方向的VLAN映射策略，将原来的VLAN Tag 映射为新的VLAN
Tag。

 对于下行数据流，通过在上图所示的上行端口上配置输出方向的VLAN映射策略，将报文的VLAN Tag 映射到原来的
VLAN Tag。

######  一对一 VLAN mapping 的实现方式二

图 13 - 8

 对于上行数据流，通过在上图所示的下行端口上配置输入方向的VLAN映射策略，将原来的VLAN Tag 映射为新的VLAN
Tag。

 对于下行数据流，通过在上图所示的上行端口上配置输入方向的VLAN映射策略，将报文的VLAN Tag 映射到原来的
VLAN Tag。

###### 13.3.4 TPID 设置

**工作原理**

以太网帧Tag包含四个字段：TPID(Tag Protocol Identifier，标签协议标志)、 User Priority、CFI、VLAN ID。对于TPID值，
缺省采用IEEE802.1Q协议规定的0x8100。而某些厂商的设备将报文外层Tag的TPID值设置为0x9100或其他值。为了和这
些设备兼容，提供了基于端口的报文TPID可配置功能。用户可自行配置端口的TPID值，那么这些端口在转发报文时，会将
报文的外层Vlan Tag中的TPID替换为用户设定的值，以达到不同厂商之间TPID兼容。


配置指南 QINQ

###### 13.3.5 MAC 地址复制

**工作原理**

采用基于ACL的灵活QinQ时，交换机学到的mac的vid是native vlan的。使用该策略封装外层VLAN Tag时，当报文从对
端回来时带的VLAN是外Tag的VLAN，就会发生在外层VLAN内无法查询到mac地址而泛洪的情况。

图 13 - 9

如上图所示，交换机和用户网络相连端口是dot1q-tunnel port，且在该端口上配置Native vlan是 4 ，并且配置基于ACL策略
的QinQ对源MAC为A的报文封装外层Tag为VLAN 5。当交换机收到用户网络vlan 3且源MAC为A的报文后，为其添加
VLAN 5 的外层Tag，同时由于接收端口的native VLAN是VLAN 4 ，MAC-A将被学习到VLAN 4 中。当响应报文返回时，由
于其外层Tag的VLAN是VLAN 5 ，将在VLAN 5 中查找MAC-A，但是MAC-A并没有被学习到VLAN 5 中，此报文将被泛洪。
为此，可以将Native VLAN的mac地址复制到外层Tag所在的VLAN中，解决从公网返回的报文被持续泛洪的问题。同样，
也可以将外层Tag所在VLAN的mac地址复制到Native VLAN，解决从用户网络发往公网的报文被持续泛洪的问题。

###### 13.3.6 二层协议透传

**工作原理**

为了实现用户网络之间二层协议报文的传输而又不对运营商网络产生影响，可以使用二层报文透传功能。当用户网络中二层协
议报文进入提供商网络边缘设备时，将目的MAC地址改成私有地址在运营商网络中转发，到了另外一端边缘设备后，再将目
的mac地址改成公有地址回到另一端用户网络，以达到二层协议报文在运营商网络透传的效果。

###### 13.3.7 优先级复制

**工作原理**


配置指南 QINQ

如果用户VLAN Tag的User Priority（即cos）设置了值，而服务商网络中针对该cos设置了QOS优先级策略，可以在封装外
层Tag的时候把外层VLAN Tag的cos值设置为和内层VLAN Tag一样的值，这样就可以使用户的报文既能透传又能使用服务
商网络提供的QOS优先级策略。

###### 13.3.8 优先级映射

**工作原理**

服务商网络中针对一些cos设置了QOS优先级策略，在封装外层Tag的时候按照用户报文的重要性和优先级性，根据用户的
内层VLAN Tag的cos指定外层VLAN Tag的cos值，使报文封装外层VLAN Tag后能享用服务商网络的QOS策略。

#### 13.4 产品说明

```
S6000E支持全局配置^4 个tpid值，除0x8100外其他^3 个可配置为任意值。^
```

#### 13.5 配置详解

配置项 配置建议 & 相关命令

基本QinQ配置

### 必须配置。^

```
switchport mode dot1q-tunnel 接口设置成 dot1q-tunnel port。
switchport dot1q-tunnel allowed vlan { [ add ]
tagged vlist | [ add ] untagged vlist | remove vlist }
```

```
添加Tunnel口的许可vlan，可以指定
外层VLAN和用户VLAN以Tag或
UnTag形式加入Tunnel口
switchport dot1q-tunnel native vlan VID 设置dot1q-tunnel口的缺省vlan。
```

配置基于C-Tag 的灵活
QinQ功能

### 启用该功能必须配置，此功能必须依赖基本QinQ配置，灵活QinQ功能比基本QinQ功能

```
优先级高
```

```
dot1q outer-vid VID register inner-vid v_list
配置基于内部Tag添加外部Tag的
VID策略。
```

配置基于ACL的灵活QinQ
功能

### 启用该功能必须配置，此功能必须依赖基本QinQ配置，灵活QinQ功能比基本QinQ功能

```
优先级高
```

```
traffic-redirect access-group acl nested-vlan VID in
配置基于数据流添加外部Tag的VID
策略。
```

配置VLAN-MAPPING功能

### 必须配置，开启VLAN-MAPPING功能^

###### vlan-mapping-in vlan cvlan remark svlan

```
配置输入方向的一对一vlan
mapping功能。它将从端口输入报文
的Customer VLAN ID修改为指定的
Server VLAN ID。
```

配置指南 QINQ

###### vlan-mapping-out vlan svlan remark cvlan

```
配置输出方向的一对一vlan
mapping功能。它将从端口输出报文
的Server VLAN ID 修改回指定的
Customer VLAN ID。
```

```
vlan-mapping-in vlan cvlan-list remark svlan
```

```
配置输入方向的多对一vlan
mapping功能。它可同时将输入的多
个Customer VLAN ID修改为同一个
指定的Server VLAN ID。
```

配置TPID

### 可选配置，用于兼容不同厂商的TPID^

```
frame-tag tpid tpid
```

```
设置帧Tag中的TPID。如果想设置为
0x9100。那么直接输入frame-tag
tpid 9100。注意默认是 16 进制。该
功能需要在出口配置才能生效。
```

配置MAC地址复制

### 可选配置，用于解决基于ACL中MAC地址策略的QinQ功能防报文泛洪^

```
mac-address-mapping x source-vlan src-vlan-list
destination-vlan dst-vlan-id
```

```
将接口在源vlan中学习到的动态地址
复制到目的vlan中。
```

配置外层和内层VLAN Tag
修改策略

### 可选配置，用于根据网络拓扑适当调整运营商网络中数据报的外层Tag和内层Tag^

```
dot1q relay-vid VID translate local-vid v_list
配置基于外部Tag修改外层Tag的
VID策略。
dot1q relay-vid VID translate inner-vid v_list 配置基于内部Tag修改外层Tag的
VID策略。
dot1q new-outer-vlan VID translate old-outer-vlan
vid inner-vlan v_list
```

```
配置基于外层Tag + 内层Tag修改外
部Tag的修改外层VID策略。
traffic-redirect access-group acl outer-vlan VID in 配置基于ACL修改外层Tag的VID策
略。
traffic-redirect access-group acl inner-vlan VID out
配置基于ACL修改内层Tag的VID策
略。
```

配置优先级复制和优先级映
射

### 可选配置，用于沿用用户网络中用户数据的优先级策略^

```
inner-priority-trust enable
```

```
复制内层Tag(C-Tag)的priority字段
值到外层Tag的 priority 字段值
(S-Tag)。
```

### 可选配置，用于根据外层Tag设置用户数据的优先级策略^

```
dot1q-Tunnel cos inner-cos-value remark-cos
outer-cos-value
```

```
根据内层Tag(C-Tag)的priority字段
值设置外层Tag的priority 字段值
(S-Tag)。
```

配置二层协议透传

### 可选配置，用于透传MSTP和GVRP协议报文，满足用户网络的拓扑而不影响运营商网络

```
的拓扑^
l2protocol-tunnel stp 配置全局使能STP协议报文透传功能。
```

l2protocol-tunnel stp enable (^) 在接口上使能STP协议报文透传功能。


配置指南 QINQ

```
l2protocol-tunnel gvrp
配置全局使能GVRP协议报文透传功
能。
l2protocol-tunnel gvrp enable 在接口上使能GVRP协议报文透传功
能。
l2protocol-tunnel{STP|GVRP}tunnel-dmac
mac-address 配置相应协议的透传地址。^
```

### QinQ配置有如下限制：^

### 路由口不能设置为Tunnel Port。^

### 配置为Tunnel的端口不能再启用802.1x功能。^

### 配置为Tunnel的端口不能再启用端口安全功能。^

### 配置Tunnel Port作为RSPAN的源口时，外部TAG中的VID等于RSPAN VLAN的报文视为监控数据流。^

### 对于应用在Tunnel Port上的ACL，若要匹配用户TAG中的VID，需要使用inner关键词。^

### 请将与服务商网络相连的用户网络的出口也配置为Uplink口，如果在用户网络中配置了QinQ端口的服务商Tag的TPID

```
值，那么用户网络出口的Uplink口的服务商Tag的TPID值也需要配置为相同值。^
```

### 接口的MTU 值默认为^1500 字节。当为报文加上外层VLAN Tag 后，报文的长度会增加^4 个字节，建议用户适当增加

```
运营商网络中各接口的MTU值，至少为 1504 字节。
```

### 在设备上配置了QinQ口之后，若要在设备开启igmp snooping，需要使用SVGL共享模式，否则igmp snooping在QinQ

```
口上将无法正常工作。
```

### 若某个报文同时匹配两个或两个以上数据流策略的规则，且数据流策略未指明优先级时，只执行其中一条策略。建议指定

```
优先级。
```

###### 13.5.1 基本 QINQ 配置

**配置效果**

 基于端口的QINQ策略，实现二层VPN功能。

**注意事项**

 建议不要将服务商网络中trunk口的native vlan设置为tunnel口的缺省vlan，因为trunk口会剥去VID为其native vlan
的Tag。

**配置方法**

######  配置端口模式为 dot1q-tunnel 口

 必须配置，把端口模式设置为dot1q-tunnel口。

 在端口模式下使用switchport mode dot1q-tunnel命令让端口变成dot1q-tunnel口。

【命令格式】 switchport mode dot1q-tunnel
【参数说明】 -
【缺省配置】 缺省不是tunnel口
【命令模式】 接口配置模式


配置指南 QINQ

【使用指导】 -

######  设置 dot1q-tunnel 口的 native vlan

 必须配置。
 配置端口的native vlan为供应商网络的vlan。
 配置native vlan后，该端口并没有真正加入端口。还必须将native vlan必须以untag形式加入该端口的许可列表。

 在端口模式下使用switchport dot1q-tunnel native vlan VID命令，设置dot1q-tunnel口的缺省vlan。

 如果native vlan是以untag形式加入许可列表，端口的输出报文是不带Tag；如果native vlan是以Tag形式加入许可列
表，端口的输出报文会打上native vlan的Tag。所以为了保证上下行报文的通信，必须将端口的native vlan以untag形
式加入端口的VLAN许可列表中。

【命令格式】 switchport dot1q-tunnel native vlan VID
【参数说明】 VID：指定的native vlan，范围为： 1 - 4094 ，缺省为 1
【缺省配置】 默认为VLAN 1
【命令模式】 接口配置模式
【使用指导】 Native vlan设置成供应商网络的vlan。

######  添加 dot1q-tunnel 口的许可 vlan

 必须配置.。
 配置native vlan后，必须将native vlan以untag形式加入端口的vlan的许可列表。
 对于基于端口的QinQ功能，用户网络的VLAN无需加入Tunnel口的VLAN许可列表。
 灵活QinQ需要根据实际情况，将用户网络的VLAN以Tag或者UNTag形式加入端口的VLAN许可列表。

 在端口模式下使用switchport dot1q-tunnel allowed vlan { [ add ] tagged vlist | [ add ] untagged vlist | remove vlist }
命令配置。端口收到响应VLAN的报文是会根据设置情况加Tag和剥离Tag。

【命令格式】 switchport dot1q-tunnel allowed vlan { [ add ] tagged vlist | [ add ] untagged vlist | remove vlist }
【参数说明】 v_list：端口允许通过的vlan列表
【缺省配置】 默认端口以UNTag形式加入VLAN 1，其它VLAN未加入
【命令模式】 接口配置模式
【使用指导】 通过配置该命令，可增加/删除dot1q-tunnel口的许可vlan，并指明输出是带Tag还是untag。
对于基本QINQ功能，仅需要将端口的native vlan以untag形式加入端口的许可列表。

**检验方法**

查看配置为dot1q-tunnel端口信息：。
 检查设备端口dot1q-tunnel是否打开和dot1q-tunnel端口配置信息是否正确。

**配置举例**

### 以下配置举例，仅介绍QINQ相关的配置。^

######  配置基本 QinQ ，实现二层 VPN


配置指南 QINQ

【网络环境】
图 13 - 10

```
【配置方法】  在服务提供商网络边缘设备上配置tunnel口，将用户网络的边缘设备连接在该端口上。
 设置tunnel口的native vlan，并将native vlan以untag形式加入端口的VLAN许可列表。
 在用户网络根据用户需求配置用户VLAN。
```

### 开启QinQ功能的设备会为用户报文封装其他VLAN的外层Tag，不会按报文中原始的VLAN进行转发，

```
因此不需要在服务提供商网络设备上配置用户VLAN
```

### 交换机的TPID一般采用IEEE802.1Q中规定的0x8100，存在部分第三方设备的TPID采用其它值，网

```
络中存在该类型设备时，需要在连接该设备的出口上设置TPID值，以便兼容。
```

### 当边缘设备连接服务商网络的上链口或服务提供商设备之间相互连接的的接口为Trunk port、Hybrid port

```
的时候，请避免将Trunk port或Hybrid port的Native vlan设置为tunnel口的缺省vlan。因为当报文从
Trunk port或Hybrid port输出时，会被剥去VID为其Native vlan的Tag。
Provider A 第一步，创建服务商VLAN 10、 20 用于区别两个企业的数据
ProviderA#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
ProviderA(config)#vlan 10
ProviderA(config-vlan)#exit
ProviderA(config)#vlan 20
ProviderA(config-vlan)#exit
第二步，在连接企业A网络的接口上启用基本QinQ功能，使用VLAN10对企业A网络的数据进行隧道传输。
ProviderA(config)#interface gigabitEthernet 0 /1
ProviderA(config-if-GigabitEthernet 0 /1)#switchport mode dot1q-tunnel
ProviderA(config-if-GigabitEthernet 0 /1)#switchport dot1q-tunnel native vlan 10
ProviderA(config-if-GigabitEthernet 0 /1)#switchport dot1q-tunnel allowed vlan add untagged 10
第三步，在连接企业B网络的接口上启用基本QinQ功能，使用VLAN20对企业B网络的数据进行隧道传输。
ProviderA(config)#interface gigabitEthernet 0 / 2
ProviderA(config-if-GigabitEthernet 0 / 2 )#switchport mode dot1q-tunnel
ProviderA(config-if-GigabitEthernet 0 / 2 )#switchport dot1q-tunnel native vlan 20
ProviderA(config-if-GigabitEthernet 0 / 2 )#switchport dot1q-tunnel allowed vlan add untagged 20
第四步，配置Uplink口
ProviderA(config)# interface gigabitEthernet 0 /5
```

配置指南 QINQ

```
ProviderA(config-if-GigabitEthernet 0 /5)#switchport mode uplink
第五步，在Uplink口上调整输出报文的TPID值为第三方设备可识别的值，如0x9100
ProviderA(config-if-GigabitEthernet 0 / 5 )#frame-tag tpid 9100
第六步，配置Provider B，与Provider A类似，这里不再赘述。
```

【检验方法】 从Customer A1发送一个VLAN 100、目的MAC为Customer A2用户 2 的MAC的报文，从Provider A出来
报文被打上tunnel口的外层Tag，到达Customer A2的报文是用户原有的VLAN 100。
 查看Tunnel口的配置是否正确。
 查看需要的TPID值设置是否正确。
Provider A ProviderA#show running-config
interface GigabitEthernet 0 / 1
switchport mode dot1q-tunnel
switchport dot1q-tunnel allowed vlan add untagged 10
switchport dot1q-tunnel native vlan 10
spanning-tree bpdufilter enable
！
interface GigabitEthernet 0 / 2
switchport mode dot1q-tunnel
switchport dot1q-tunnel allowed vlan add untagged 20
switchport dot1q-tunnel native vlan 20
spanning-tree bpdufilter enable
!
interface GigabitEthernet 0/5
switchport mode uplink
frame-tag tpid 0x9100
ProviderA#show interfaces dot1q-tunnel

```
========Interface Gi 0 / 1 ========
Native vlan: 10
Allowed vlan list:1,10,
Tagged vlan list:
```

```
========Interface Gi 0 / 2 ========
Native vlan: 20
Allowed vlan list:1,20,
Tagged vlan list:
ProviderA#show frame-tag tpid
Ports Tpid
------- -------------
Gi 0 / 5 0x9100
```

配置指南 QINQ

Provider B Provider B设备上的配置验证同Provider A的类似，请参考上文Provider A的配置验证过程，此处不再
重复描述。

**常见错误**

 没有将tunnel口的native vlan以untag形式加入端口的VLAN许可列表里面。
 存在第三方设备的TPID值不是默认的0x8100，在连接第三方设备的出口上未设置TPID，导致报文无法被第三方设备识
别。

###### 13.5.2 配置基于 C-Tag 的灵活 QinQ 功能

**配置效果**

 根据用户VLAN（C-Tag）为用户报文灵活封装外层VLAN Tag（S-Tag），实现企业用户数据的二层VPN和业务流优先传
输管理。

**注意事项**

 必须依赖基本QinQ配置。
 灵活QINQ的一些规则，由于有些芯片的限制，会出现一些产品的支持情况和限制。
 如果需要沿用用户网络VLAN Tag优先级，可以通过配置优先级复制功能，使用户报文封装外层Tag后仍沿用用户Tag
的优先级。
 如果运营商网络中需要用户数据包采用外层VLAN Tag的优先级和优先级传输，还需要配置优先级复制功能将外层Tag
的cos设置为指定值。

**配置方法**

######  配置基于内部 Tag 添加外部 Tag 的 VID 策略

 必须执行此配置项。
 网络环境中，对dot1q-tunnel端口上收到的报文，需要能根据内层Tag的VID修改外层Tag的VID。按照该命令功能，
可以通过指定内部VLAN添加与内部VID相同的外部VID，并将出口加入该VLAN的UnTag端口集中，可以实现从出口
输出的为原始内部Tag报文。

### 基于数据流的VID变更策略表优先于基于端口和C-Tag的VID变更策略表生效。^

### 当AP口添加或者删除成员口时，AP上配置的VID添加策略或修改策略会被删除，需要重新配置。建议用户配置完AP 成

```
员后，再在AP上进行VID策略配置。
```

### 在Tunnel port上必须允许外层Tag VLAN(包括Native VLAN)通过，同时接入公网的接口也必须允许这些VLAN报文通

```
过。
```

【命令格式】 dot1q outer-vid VID register inner-vid v_list
【参数说明】 -^
【缺省配置】 策略表空
【命令模式】 接口配置模式


配置指南 QINQ

【使用指导】 -

**检验方法**

企业分公司之间规划VLAN内用户能互通。
 企业分公司的VLAN内的用户能实现二层VPN。

 能通过添加外Tag、优先级复制或优先级映射等实现不同业务的优先级传输策略。

###### 配置举例

### 下面配置举例，仅介绍与灵活QinQ相关配置^

######  基于 C-Tag 灵活实现二层 VPN 及业务流管理

【网络环境】
图 13 - 11

【配置方法】  在服务商网络边缘设备PE1和PE2连接用户网络边缘设备的接口配置为Tunnel口。
 根据用户网络中的业务数据VLAN在Tunnel口上配置外层Tag添加策略。
 如果ISP网络提供了基于VLAN的 QOS优先级策略，可以将重要业务或质量要求较高的业务流的外层
Tag封装为相关QOS策略对应的VLAN。
 如果ISP网络提供了基于cos的 QOS优先级策略，如果QOS策略对应的cos是用户VLAN Tag的cos
值，可以通过优先级复制将用户VLAN Tag的cos复制给外层VLAN Tag的cos，使报文封装外层Tag
后能沿用用户VLAN Tag的优先级策略。
 如果ISP网络提供了基于cos的QOS优先级策略，还可以通过优先级映射，根据用户VLAN Tag的cos
值设定外层VLAN Tag的cos值为QOS策略对应的cos值，使得报文封装外层Tag后能使用优先级策
略。

PE1 (^) 第一步，配置透传VLAN
PE1#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
PE1(config)#vlan 100
PE1(config-vlan)#exit
PE1(config)#vlan 200
PE1(config-vlan)#exit
第二步， 在接入交换机的下联口上配置基于C-Tag添加外层VLAN Tag的灵活QinQ功能
配置Gi 0/1接口类型为Tunnel port


配置指南 QINQ

```
PE1(config)#interface gigabitEthernet 0/1
PE1(config-if)# switchport mode dot1q-tunnel
将服务商VLAN101,201加入到Tunnel port许可VLAN列表，并配置对端报文返回至Tunnel port输出时剥离
服务商Tag
PE1(config-if)# switchport dot1q-tunnel allowed vlan add untagged 10 0 ,20 0
配置从Tunnel port输入的vlan 1 - 10 0 (C-tag)的数据帧在服务商网络中传输打上vlan 10 0 (S-tag)的标签
PE1(config-if)# dot1q outer-vid 10 0 register inner-vid 1 - 100
配置从Tunnel port输入的vlan 101 - 200 (C-tag)的数据帧在服务商网络中传输打上vlan 200 (S-tag)的标签
PE1(config-if)# dot1q outer-vid 200 register inner-vid 101 - 200
第三步，将连接服务商网络的接入公网的接口配置Uplink口
PE1(config)# interface gigabitEthernet 0 / 2
PE1(config-if-GigabitEthernet 0 / 2 )#switchport mode uplink
```

PE2 和PE1上配置类似，这里就不再赘述

【检验方法】 (^) 确认配置是否正确，关注点：下连接口类型是否为dot1q-tunnel，外层Tag VLAN是否已加入接口的许可VLAN
列表，接口上的映射策略是否正确，uplink口是否设置正确。
确认VLAN映射策略是否正确。
PE1 PE1#show running-config interface gigabitEthernet 0/1
interface GigabitEthernet 0/1
switchport mode dot1q-tunnel
switchport dot1q-tunnel allowed vlan add untagged 10 0 ,20 0
dot1q outer-vid 10 0 register inner-vid 1- 200
dot1q outer-vid 20 0 register inner-vid 101 - 200
spanning-tree bpdufilter enable
！
第二步，确认基于C-Tag添加TAG的映射策略；关注点：内外层VLAN标签映射关系是否正确。
PE1#show registration-table
Ports Type Outer-VID Inner-VID-list

------ ---------- ---------- --------------

Gi 0 /1 Add-outer 1 00 1 - 200
Gi 0 /1 Add-outer 20 0 101 - 200

###### 13.5.3 配置基于 ACL 的灵活 QinQ 功能

**配置效果**

 根据用户网络的流特征基于ACL进行分类，对用户报文灵活封装外层VLAN Tag（S-Tag），便于运营商网络不同用户业
务的管理。

**注意事项**


配置指南 QINQ

 必须依赖QinQ基本配置。
 灵活QINQ的一些规则，由于有些芯片的限制，会出现一些产品的支持情况和限制。
 如果需要沿用用户网络VLAN Tag优先级，可以通过配置优先级复制功能，使用户报文封装外层Tag后仍沿用用户Tag
的优先级。
 如果运营商网络中需要用户数据包采用外层VLAN Tag的优先级和优先级传输，还需要配置优先级复制功能将外层Tag
的cos设置为指定值。

### 基于ACL的VID变更策略比基于端口和C-Tag的VID变更策略优先级高。^

### 当ACL被删除时，与此ACL相关的策略会被自动删除。^

### 当dot1q-tunnel口收到^ >= 2层Tag的报文时，无法采用基于流的匹配规则来添加外层Tag。^

### 若某个报文同时匹配两个或两个以上数据流添加VID策略，且数据流策略未指明优先级时，只执行其中一条策略。建议

```
指定优先级。
```

### 在Tunnel port上必须允许外层Tag VLAN(包括Native VLAN)通过，同时接入公网的接口也必须允许^

这些VLAN报文通过。

**配置方法**

######  配置基于数据流添加外部Tag的VID策略。

 必须执行此配置项。
 网络环境中，对dot1q-tunnel端口的输入报文，有时需要能够由报文内容的不同，转发时为报文添加外部Tag指定不同
的VID。
【命令格式】 traffic-redirect access-group acl nested-vlan VID in
【参数说明】 -
【缺省配置】 策略表空
【命令模式】 接口配置模式
【使用指导】 -

**检验方法**

企业分公司之间业务内用户能互通，并且还可以通过VPLS相关配置能使特定业务数据得到较高的传输优先级
 企业分公司相同业务的用户能实现二层VPN。
 能通过添加外Tag、优先级复制或优先级映射等实现不同业务的优先级传输策略。

###### 配置举例

### 下面配置举例，仅介绍与灵活QinQ相关配置^

######  基于 ACL 灵活实现二层 VPN 及业务流管理


配置指南 QINQ

【网络环境】
图 13 - 12

【配置方法】  在服务商网络边缘设备PE1和PE2连接用户网络边缘设备的接口配置为Tunnel口。
 在PE1和PE2设备上配置ACL策略，区分用户网络不同的业务流。
 根据ACL区分的业务流在Tunnel口上配置外层Tag添加策略。
 如果ISP网络提供了基于VLAN的 QOS优先级策略，可以将重要业务或质量要求较高的业务流的外层
Tag封装为相关QOS策略对应的VLAN。
 如果ISP网络提供了基于cos的QOS优先级策略，并且用户网络的报文带Tag，那么可以通过优先级
映射和优先级复制设定外层Tag的cos值，使用户报文封装外层Tag后使用QOS优先级策略。
PE1 第一步，创建用与区分流的ACL，PPPOE协议类型0x8863/0x886 4 ，匹配IPOE协议类型0x 0800
PE1#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
PE1(config)# expert access-list extended acl1
PE1(config-exp-nacl)# permit 0x8863 any any
PE1(config-exp-nacl)# permit 0x886 4 any any
PE1(config-exp-nacl)#exit
PE1(config)# expert access-list extended acl2
PE1(config-exp-nacl)#permit 0x 0800 any any
第二步，创建服务商VLAN 10 0 、 200 ,用于区分用户数据。
PE#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
PE1(config)#vlan 100
PE1(config-vlan)#exit
PE1(config)#vlan 200
PE1(config-vlan)#exit
第三步，在接入交换机的下联口上配置基于ACL添加外层VLAN Tag的灵活QinQ功能
配置Gi 0/1接口类型为Tunnel port
PE1(config)#interface gigabitEthernet 0/1
PE1(config-if)# switchport mode dot1q-tunnel
将服务商VLAN 100 ,20 0 加入到Tunnel port许可VLAN列表，并配置当对端报文返回至Tunnel port输出时剥
离服务商网络Tag
PE1(config-if)#switchport dot1q-tunnel allowed vlan add untagged 100 , 200


配置指南 QINQ

```
配置从Tunnel port输入的匹配ACL1的数据帧在服务商网络中传输打上vlan 101(S-tag)的标签
PE1(config-if)# traffic-redirect access-group acl1 nested-vlan 100 in
配置从Tunnel port输入的匹配ACL2的数据帧在服务商网络中传输打上vlan 200 (S-tag)的标签
PE1(config-if)# traffic-redirect access-group acl1 nested-vlan 200 in
第三步，将连接服务商网络的接入公网的接口配置Uplink口
PE1(config)# interface gigabitEthernet 0 / 2
PE1(config-if-GigabitEthernet 0 / 2 )#switchport mode uplink
```

【检验方法】 (^) 企业分公司之间业务内用户能互通，用户相关业务能得到优先级保障。
 企业分公司的VLAN内的用户能实现二层VPN。
 确认ACL的配置是否正确。
 业务的优先级正确。
 确认配置是否正确：下连接口类型是否为dot1q-tunnel，外层Tag VLAN是否已加入接口的许可VLAN
列表，接口上的映射策略是否正确等。
PE1 (^) 第一步,查看Tunnl配置是否正确
Ruijie#show running-config interface gigabitEthernet 0/1
interface GigabitEthernet 0/1
switchport mode dot1q-tunnel
switchport dot1q-tunnel allowed vlan add untagged 10 0 ,20 0
traffic-redirect access-group acl1 nested-vlan 10 0 in
traffic-redirect access-group acl2 nested-vlan 20 0 in
spanning-tree bpdufilter enable
!
第二步，确认基于C-Tag添加TAG的映射策略；关注点：内外层VLAN标签映射关系是否正确。
PE1#show traffic-redirect
Ports Type VID Match-filter

------- ---------- ----- ------------

Gi 0 /1 Nested-vid 101 acl1
Gi 0 /1 Nested-vid 201 acl2
**常见错误**
 ACL策略没有配置。
 ACL策略是根据MAC地址来划分流，没有配置MAC地址复制功能，存在报文泛洪情况。

###### 13.5.4 配置 VLAN-MAPPING 功能

**配置效果**


配置指南 QINQ

 将在用户私有网络中传输的报文VLAN Tag替换为公网传输使用的VLAN Tag，使其按照公网的VLAN规划进行传输。

**注意事项**

 只能在access、trunk、hybrid或uplink端口上配置。

### 配置^ VLAN mapping情况下，送CPU的报文VLAN ID为修改之后的VLAN ID。^

### 建议用户不要在同一端口上同时配置VLAN映射和灵活QinQ。^

**配置方法**

######  配置一对一 VLAN mapping

 1:1模式下必须配置，配置1:1 vlan映射规则。

 在TRUNK、UPLINK等端口上配置vlan-mapping-in vlan CVID remark SVID、vlan-mapping-out vlan SVID remark CVID
可开启VLAN-MAPPING 1： 1 功能。

###### 【命令格式】 vlan-mapping-in^ vlan^ src-vlan-list remark^ dest-vlan^

【参数说明】 src-vlan-list：只包含一个Customer VLAN，用户网络所在的VLAN。
dest-vlan：Service VLAN，服务商网络所在的VLAN.
【缺省配置】
【命令模式】 接口配置模式
【使用指导】 配置输入方向的一对一vlan mapping功能。

###### 【命令格式】 vlan-mapping-out vlan src-vlan remark dest-vlan

【参数说明】 src-vlan：Service VLAN，服务商网络所在的VLAN。
dest-vlan：Customer VLAN，用户网络所在的VLAN。
【缺省配置】
【命令模式】 接口配置模式
【使用指导】 配置输出方向的一对一vlan mapping功能。

**检验方法**

查看VLAN-MAPPING配置：。
 show interfaces[ intf-id ] vlan-mapping 查看VLAN-MAPPING配置信息是否正确。

###### 配置举例

### 下面配置举例，仅介绍与VLAN_MAPPING相关配置。^

######  基于 VLAN-MAPPING 实现不同业务的聚合


配置指南 QINQ

【网络环境】

```
图 13 - 13
```

【配置方法】 (^)  配置家庭网关 1 及家庭网关 2 ：
第一步，创建家庭网关中不同业务的原始VLAN。
Ruijie#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)#vlan range 10- 12
Ruijie(config-vlan-range)#exit
第二步，配置连接PC、IPTV、VOIP话机的端口属性，假设连接端口分别为Gi 0/2、Gi 0/3、Gi 0/4。
Ruijie(config)#interface gigabitEthernet 0 / 2
Ruijie(config-if-GigabitEthernet 0 / 2 )#switchport access vlan 10
Ruijie(config-if-GigabitEthernet 0 / 2 )#exit
Ruijie(config)#interface gigabitEthernet 0 / 3
Ruijie(config-if-GigabitEthernet 0 / 3 )#switchport access vlan 11
Ruijie(config-if-GigabitEthernet 0 / 3 )#exit
Ruijie(config)#interface gigabitEthernet 0 / 4
Ruijie(config-if-GigabitEthernet 0 / 4 )#switchport access vlan 12
Ruijie(config-if-GigabitEthernet 0 / 4 )#exit
第四步，配置上行端口为Uplink口
Ruijie(config)# interface gigabitEthernet 0 / 1
Ruijie(config-if-GigabitEthernet 0 / 1 )#switchport mode uplink
 配置楼道交换机，在楼道交换机上完成报文的1:1 VLAN映射：
第一步，创建家庭网关中不同业务的原始VLAN与映射后VLAN。
Ruijie#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)#vlan range 10- 12


配置指南 QINQ

```
Ruijie(config-vlan-range)#exit
Ruijie(config)#vlan range 100- 102
Ruijie(config-vlan-range)#exit
Ruijie(config)#vlan range 200- 202
Ruijie(config-vlan-range)#exit
第二步，针对家庭网关 1 ，在下行端口上配置1:1 输入/输出方向的VLAN映射策略。
Ruijie(config)#interface gigabitEthernet 0 / 2
Ruijie(config-if-GigabitEthernet 0 / 2 )#switchport mode uplink
Ruijie(config-if-GigabitEthernet 0/2)#vlan-mapping-in vlan 10 remark 100
Ruijie(config-if-GigabitEthernet 0/2)#vlan-mapping-in vlan 11 remark 101
Ruijie(config-if-GigabitEthernet 0/2)#vlan-mapping-in vlan 12 remark 102
Ruijie(config-if-GigabitEthernet 0/2)#vlan-mapping-out vlan 100 remark 10
Ruijie(config-if-GigabitEthernet 0/2)#vlan-mapping-out vlan 101 remark 11
Ruijie(config-if-GigabitEthernet 0/2)#vlan-mapping-out vlan 102 remark 12
第三步，针对家庭网关 2 ，在下行端口上配置1:1输入/输出方向的VLAN映射策略。
Ruijie(config)#interface gigabitEthernet 0 / 3
Ruijie(config-if-GigabitEthernet 0/3)#switchport mode uplink
Ruijie(config-if-GigabitEthernet 0/3)#vlan-mapping-in vlan 10 remark 200
Ruijie(config-if-GigabitEthernet 0/3)#vlan-mapping-in vlan 11 remark 201
Ruijie(config-if-GigabitEthernet 0/3)#vlan-mapping-in vlan 12 remark 202
Ruijie(config-if-GigabitEthernet 0/3)#vlan-mapping-out vlan 200 remark 10
Ruijie(config-if-GigabitEthernet 0/3)#vlan-mapping-out vlan 201 remark 11
Ruijie(config-if-GigabitEthernet 0/3)#vlan-mapping-out vlan 202 remark 12
第四步，配置上行端口为Uplink口
Ruijie(config)# interface gigabitEthernet 0 / 1
Ruijie(config-if-GigabitEthernet 0 / 1 )#switchport mode uplink
```

【检验方法】 (^)  查看楼道交换机的1:1 VLAN映射规则配置。
Ruijie#show interfaces vlan-mapping
Ports type Status Service-Vlan Customer-Vlan-list

----------- ----- --------- ----------- ----------------

Gi0/ 2 in active 100 10
Gi0/ 2 in active 101 11
Gi0/ 2 in active 102 12
Gi0/ 2 out active 100 10
Gi0/ 2 out active 101 11
Gi0/ 2 out active 102 12
Gi0/ 3 in active 200 10
Gi0/ 3 in active 201 11
Gi0/ 3 in active 202 12
Gi0/ 3 out active 200 10


配置指南 QINQ

```
Gi0/ 3 out active 201 11
Gi0/ 3 out active 202 12
```

**常见错误**

 无。

###### 13.5.5 配置 TPID

**配置效果**

 实现服务商网络设备 Tag中的 TPID值，兼容第三方设备的不同TPID值。

**注意事项**

 如果服务商网络边缘设备接入服务商网络的接口连接的第三方设备的TPID值不是IEEE 802.1Q默认的0x8100，则需要
在该接口上设备TPID值。

### 不允许将tpid指定为如下知名类型0x0806(ARP)、0x0200(PUP)、0x8035(RARP)、0x0800(IP)、0x86DD(IPv6)、

```
0x8863/0x8864(PPPoE)、0x8847/0x8848(MPLS)、0x8137(IPX/SPX)、0x8000(IS-IS)、0x8809(LACP)、0x888E(802.1x)、
0x88A7(集群)、0x0789(我司保留)。
```

**配置方法**

 如果存在第三方设备的TPID值不是0x8100，必须在连接第三方设备的接口上设置TPID。

 TPID设置支持基于端口和基于全局配置，以基于端口配置为例：

```
在端口模式下配置frame-tag tpid 0x 9100 ，可修改TPID值为0x9100。TPID值的限制见1.4.5节。
```

【命令格式】 frame-tag tpid tpid
【参数说明】 tpid:新的TPID值
【缺省配置】 默认TPID值为0x8100
【命令模式】 接口配置模式
【使用指导】 第三方设备的TPID值不是0x8100时，在连接第三方设备的接口上设置该值。

**检验方法**

查看TPID是否设置成功。

**配置举例**

######  配置端口的 TPID 值。

```
【配置方法】  配置端口的TPID值。
Ruijie(config)# interface gigabitethernet 0/1
Ruijie(config-if)# frame-tag tpid 9100
```

配置指南 QINQ

```
【检验方法】  查看接口上的TPID值。
Ruijie# show frame-tag tpid interfaces gigabitethernet 0/1
Port tpid
------- -------------
Gi0/1 0x9100
```

**常见错误**

 无

###### 13.5.6 配置 MAC 地址复制

**配置效果**

 当一个端口学习到动态地址时，将其从一个vlan复制到另一个vlan中。
 在基于ACL的灵活QinQ划分业务流时，如果ACL规则是根据MAC地是来划分流，避免可能存在的报文泛洪的问题。

**注意事项**

### 关闭VLAN 间MAC 地址复制功能后，系统将删除目的VLAN 中通过该功能学到的其他VLAN 的所有MAC 地址表项。^

### VLAN 间MAC 地址复制功能在一个端口下对某个目的VLAN 只能配置一次。如果需要修改，必须先删除之前的配置，

```
然后再重新进行配置。
```

### 不能和share vlan共用；不能将地址复制到动态VLAN中。^

### 每个端口最多只能配置^8 个目的VLAN。即使端口不在指定的目的VLAN中，该功能也会生效。^

### 地址复制不能在host/promiscuous口上配置，不能在打开端口安全，镜像的目的口，打开1x功能的端口上配置。^

### 只复制动态地址；静态地址不复制；地址表已满时，不复制；开启功能前，源地址已经存在的mac地址不复制。^

### 复制地址的优先级比动态地址高，比其它类型地址的优先级低。^

### 当MAC地址老化时候，由其复制出来的地址也要相应老化；当MAC地址被删除时，由其复制出来的地址也将被自动删

```
除。^
```

### 不支持热备，故当发生主从切换后，建议用户关闭复制功能，再重新打开。^

### 用户不能手工删除通过VLAN间MAC地址复制功能获得的MAC地址表项，如果确实需要删除该表项，可以通过关闭

```
VLAN间MAC地址复制功能实现。
```

**配置方法**

######  配置 MAC 地址复制

 如果需要避免报文泛洪，则应该执行此配置项，将MAC地址从一个vlan复制到另一个vlan。


配置指南 QINQ

 在TRUNK下配置mac-address-mapping <1-8> source-vlan src-vlan-list destination-vlan dst-vlan-id,可开启MAC地址
复制功能。src-vlan-list、dst-vlan-id为VLAN的取值范围。

【命令格式】 mac-address-mapping x source-vlan src-vlan-list destination-vlan dst-vlan-id
【参数说明】 x：MAC地址复制索引号，只能配置<1-8>。
src-vlan-list：源vlan列表。
dst-vlan-id：目的vlan列表。
【缺省配置】 MAC地址复制功能未开启
【命令模式】 接口配置模式
【使用指导】 -^

**检验方法**

 查看指定VLAN的MAC地址是否正确的复制到另一个VLAN。

**配置举例**

######  配置 MAC 地址复制功能。

```
【配置方法】  配置MAC地是复制功能。
Ruijie(config)# interface gigabitethernet 0/1
Ruijie(config-if)# switchport mode trunk
Ruijie(config-if)#mac-address-mapping 1 source-vlan 1 - 3 destination-vlan 5
【检验方法】  查看端口上配置是否生效。
 发送源VLAN的报文，查看设备上该报文的源MAC也有一份学在目的VLAN上。
Ruijie# show interfaces mac-address-mapping
Ports destination-VID Source-VID-list
----------------------------------------------
Gi0/1 5 1- 3
```

**常见错误**

 见注意事项。

###### 13.5.7 配置外层和内层VLAN Tag修改策略

**配置效果**

 根据实际组网需求修改外层Tag或内层Tag。

**注意事项**

### 基于ACL的VID变更策略比基于端口和C-Tag的VID变更策略优先级高。^


配置指南 QINQ

### 当ACL被删除时，与此ACL相关的策略会被自动删除。^

### 修改策略只能在Access、Trunk、Hybrid、Uplink口上起作用。^

### 修改策略主要是针对服务商网络中需要调整内外层Tag的需求。^

### 若某个报文同时匹配两个或两个以上数据流添加VID策略，且数据流策略未指明优先级时，只执行其中一条策略。建议

```
指定优先级。
```

**配置方法**

######  配置基于内层 Tag 修改外部 Tag 的 VID 策略

 可选配置。

 如果需要灵活的根据内层Tag的VID修改外部Tag的VID，则必须执行此配置项。

 对Access，Trunk，Hybrid，Uplink端口的输入报文，有时需要根据报文内部Tag中的不同VID，将外部 Tag的VID修
改为不同的VID值。
【命令格式】 dot1q relay-vid VID translate inner-vid v_list
【参数说明】 VID：修改后的外部tag中的 vid。
v_list：输入报文内层vid列表。
【缺省配置】 策略表空
【命令模式】 接口模式
【使用指导】 -

######  配置基于外层 Tag + 内层 Tag 的 VID 修改外层 VID 策略

 可选配置。

 如果需要灵活的根据内外层Tag的VID修改外部Tag的VID，则必须执行此配置项。

 对Access，Trunk，Hybrid，Uplink端口的输入报文，有时需要根据报文内部Tag的VID + 报文外部Tag的VID，将外
部 Tag的VID修改为不同的值。
【命令格式】 dot1q new-outer-vlan new-vid translate old-outer-vlan vid inner-vlan v_list
【参数说明】 new-vid：输入报文修改后的新外层Tag VID
vid：输入报文修改前的外层Tag VID。
v_list：输入报文内层vid列表。
【缺省配置】 策略表空
【命令模式】 接口模式
【使用指导】 -

######  配置基于外层 Tag 修改外层 Tag 的 VID 策略

 可选配置。

 如果需要灵活的根据外层Tag的VID修改外部Tag的VID，则必须执行此配置项。


配置指南 QINQ

 网络环境中，对Access，Trunk，Hybrid，Uplink端口的输入报文，有时需要能够由报文外部Tag中的不同VID，指定在
转发时修改为不同的外部Tag的VID。

【命令格式】 dot1q relay-vid VID translate local-vid v_list
【参数说明】 VID：修改后的外部tag中的 vid。
v_list：输入报文外层vid列表。
【缺省配置】 策略表空
【配置模式】 接口配置模式
【使用指导】 -

######  配置基于 ACL 的内部 vid 修改策略表

 可选配置。

 对Access，Trunk，Hybrid，Uplink端口的输出报文，有时需要能够由报文内容修改内层Tag的VID。

 需要先配置ACL设置区分数据流。

```
【命令格式】 traffic-redirect access-group^ acl^ inner-vlan^ vid^ out^
【参数说明】 acl：用于匹配流的acl。
vid：修改后的报文内层vid。
【缺省配置】 策略表空
【命令模式】 接口模式
【使用指导】 -^
```

######  配置基于 ACL 的外部 vid 修改策略表

 可选配置。

 对Access，Trunk，Hybrid，Uplink端口的输出报文，有时需要能够由报文内容修改外层Tag的VID。

 需要先配置ACL设置区分数据流。

```
【命令格式】 traffic-redirect access-group acl outer-vlan vid in
【参数说明】 acl：用于匹配流的acl。
vid：修改后的外层vid。
【缺省配置】 策略表空
【命令模式】 接口模式
【使用指导】 -
```

###### 检验方法

###### 查看端口上Tag修改策略是否生效，端口收到报文后是否依据策略修改报文的Tag。

**配置举例**

######  配置基于外层 Tag 修改外层 Tag 的 VID 策略


配置指南 QINQ

```
【配置方法】  根据实际组网需求在接口上配置内层Tag和外层Tag修改策略。
 这里仅针对基于Tag和基于流各列举一中VID的修改策略，其它策略配置类就不一一列举了。具体言之
和功能作用详见上。
第一种：基于外VLAN Tag修改外VLAN Tag。
Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if)# switchport mode trunk
Ruijie(config-if)# dot1q relay-vid 100 translate local-vid 10- 20
第二种：基于流的外层VLAN tag修改策略。
Ruijie# configure terminal
Ruijie(config)# ip access-list standard 2
Ruijie(config-acl-std)# permit host 1.1.1.1
Ruijie(config-acl-std)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if)# switchport mode trunk
Ruijie(config-if)# traffic-redirect access-group 2 outer-vlan 3 in
【检验方法】  查看接口上配置是否生效。
 报文的Tag是否是依据配置策略进行修改。
```

**常见配置错误**

 无

###### 13.5.8 配置优先级映射和优先级复制

**配置效果**

 如果服务商网络基于用户的VLAN Tag的User Priority值设置了QOS策略，通过配置优先级复制，可以使外层Tag具有
与内层Tag一样的优先级策略。

 如果服务商网络基于用户的VLAN Tag的User Priority值设置了QOS策略，通过配置优先级映射，可以设置外层Tag为
服务商提供的User Priority值。

**注意事项**

### 只有dot1q-tunnel端口允许配置用户Tag的优先级复制，其优先级高于信任模式的QOS，低于基于数据流的QOS。^

### 优先级复制与优先级映射功能不能在同一接口上同时打开。^

### 只有dot1q-tunnel端口允许配置用户Tag的优先级映射，其优先于QOS生效。^

### 如果没有配置信任模式，即trust none，则优先级映射的配置不生效；如果配置的信任模式和配置的映射不匹配，也不生

```
效。
```

配置指南 QINQ

**配置方法**

 两种配置都必须依赖Tunnel口。

 如果需要利用服务商网络为用户VLAN Tag提供的QOS策略，则优先级复制功能必须配置。

 如果需要根据用户的VLAN Tag设置外层VLAN Tag的User Priority，灵活应用QOS优先级策略，则必须配置优先级映
射策略。

 在dot1q-tunnel口下配置inner-priority-trust enable，可开启优先级复制功能。

 在dot1q-tunnel口下配置dot1q-Tunnel cos inner-cos-value remark-cos outer-cos-value，可开启优先级映射功能。

 inner-cos-value、outer-cos-value取值范围为 0 – 7 。

### 在未配置优先级映射的情况下，使用以下优先级映射：^

【命令格式】 inner-priority-trust enable
【参数说明】 -
【缺省配置】 优先级复制功能不开启
【命令模式】 接口配置模式
【使用指导】 -^

【命令格式】 dot1q-Tunnel cos inner-cos-value remark-cos outer-cos-value
【参数说明】 inner-cos-value：内部Tag的cos值。
outer-cos-value：外部Tag的cos值。
【缺省配置】 默认空配置
【命令模式】 接口配置模式
【使用指导】 -

**检验方法**

 查看端口上优先级映射或优先级复制功能是否生效。

```
show inner-priority-trust interfaces type intf-id和show interfaces type intf-id remark
```

**配置举例**

######  配置优先级映射、优先级复制。


配置指南 QINQ

```
【配置方法】  为了能够维持报文的优先级，需要在Tunnel口上，将用户报文的内层Tag的优先级复制到外层Tag中。
 为了能够在Tunnel口上实现对报文优先级的灵活控制，可以根据报文的内层优先级的不同，为报文封装
Tag时候标记上不同优先级的外层标签。
配置优先级映射
Ruijie(config)# interface gigabitethernet 0/1
Ruijie(config-if)#mls qos trust cos
Ruijie(config-if)# inner-priority-trust enable
Ruijie(config)# end
配置优先级复制
Ruijie(config)# interface gigabitethernet 0/ 2
Ruijie(config-if)#dot1q-Tunnel cos 3 remark-cos 5
```

```
【检验方法】  查看端口上的优先级配置
查看Tunnel口上的优先级复制关系：
```

```
查看Tunnel口上优先级映射关系：
Ruijie# show interface gigabitethernet 0/1 remark
Ports Type From value To value
查看Tunnel口上优先级复制开关是否打开：
Ruijie# show inner-priority-trust interfaces gigabitethernet 0/1
Port inner-priority-trust
------ -------------------
Gi0/1 enable
```

```
查看Tunnel口上优先级映射关系：
Ruijie# show interfaces gigabitethernet 0/1 remark
Ports Type From value To value
------------ ----------- ----------- --------
Gi0/1 Cos-To-Cos 3 5
```

**常见配置错误**

######  见注意事项。

###### 13.5.9 配置二层协议透传

**配置效果**

 实现二层协议透传，保证用户网络的拓扑并且对服务商网络不产生影响。


配置指南 QINQ

**注意事项**

### 未启STP协议时，还需再配置bridge-frame forwarding protocol bpdu才能透传STP协议报文。^

### 当全局使能协议透传后，接口上使能协议透传时候才有效。当接口上协议透传功能生效时候，该接口不参与该协议计算。

```
若透传口收到目的MAC为特殊组播地址的报文， 则表示组网出现错误，将直接丢弃该报文。
```

**配置方法**

######  STP 协议报文透传设置

 需要透传STP协议的BPDU报文，必须配置。
 必须全局和接口下均开启STP协议透传功能。

 在全局模式下，全局开始STP透传：l2protocol-tunnel stp

 在端口模式下，开启端口STP透传：l2protocol-tunnel stp enable

【命令格式】 l2protocol-tunnel stp
【参数说明】 -
【缺省配置】 缺省关闭
【命令模式】 全局模式
【使用指导】 -^

【命令格式】 l2protocol-tunnel stp enable
【参数说明】 -
【缺省配置】 缺省关闭
【命令模式】 接口配置模式
【使用指导】 -

######  GVRP 协议报文透传设置

 需要透传GVRP协议报文，必须配置。

 必须全局和接口下均开启GVRP协议透传功能。

 在全局模式下，全局开始STP透传：l2protocol-tunnel gvrp

 在端口模式下，开启端口STP透传：l2protocol-tunnel gvrp enable

【命令格式】 l2protocol-tunnel gvrp
【参数说明】 -
【缺省配置】 缺省关闭
【命令模式】 全局模式
【使用指导】 -^

【命令格式】 l2protocol-tunnel gvrp enable
【参数说明】 -^
【缺省配置】 缺省关闭


配置指南 QINQ

【命令模式】 接口配置模式
【使用指导】 -^

######  配置透传地址

 可选配置。
 配置对应协议的透传地址.。
【命令格式】 l2protocol-tunnel { stp | gvrp } tunnel-dmac mac-address
【参数说明】 mac-address：设置的协议报文的透传地址。
【缺省配置】 缺省使用的透传地址前三字节为01d0f8，后 3 字节为(stp： 000005 ，gvrp：000006)
【命令模式】 接口配置模式
【使用指导】

### 其中STP报文可选地址范围：01d0.f800.^0005 、^011 a.a^900.^0005 、^010 f.e^200.^0003 、^0100.^0 ccd.cdd0、

```
0100. 0 ccd.cdd1、 0100. 0 ccd.cdd2；其中GVRP报文可选地址范围为：01d0.f800. 0006 、 011 a.a 900. 0006 。
```

### 当未配置透传地址时，缺省使用的地址前三字节为01d0f8，后^3 字节为(stp：^000005 ，gvrp：000006)。^

**检验方法**

查看透传相关配置是否正确：。
 show l2protocol-tunnel stp 、show l2protocol-tunnel gvrp查看配置信息是否正确。

**配置举例**

这里仅举例配置STP协议报文透传配置，GVRP协议透传配置类似就不再赘述。

######  透传 STP 协议的 BPDU 报文

【网络环境】
图 13 - 14

```
【配置方法】
 在服务器边缘设备上全局和接口下均开启STP协议透传功能。
 STP协议透传功能必须以设备能转发STP协议报文为前提，所以必须全局开启STP协议转发功能。
```

配置指南 QINQ

```

```

Provider S1 (^) 第一步，开启STP协议转发功能。
bridge-frame forwarding protocol bpdu
第二步，创建用来透传协议报文的的VLAN
ProviderS1#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
ProviderS1(config)#vlan 200
ProviderS1(config-vlan)#exit
第三步，在连接用户网络的接口上开启基本QinQ功能，使用VLAN200对用户网络的数据进行隧道传输
ProviderS1(config)#interface gigabitEthernet 0 /1
ProviderS1(config-if-GigabitEthernet 0 /1)#switchport mode dot1q-tunnel
ProviderS1(config-if-GigabitEthernet 0 /1)#switchport dot1q-tunnel native vlan 200
第四步，在连接用户网络的接口上开启STP协议透传功能
ProviderS1(config-if-GigabitEthernet 0 /1)#l2protocol-tunnel stp enable
ProviderS1(config-if-GigabitEthernet 0 /1)#exit
第五步，全局开启STP协议透传功能
ProviderS1(config)#l2protocol-tunnel stp
第六步，配置uplink port
ProviderS1(config)# interface gigabitEthernet 0 /5
ProviderS1(config-if-GigabitEthernet 0 /5)#switchport mode uplink
Provider S2 Provider S2设备上的配置验证同Provider S1的类似，请参考上文Provider S1的配置验证过程，此处不再
重复说明。
【检验方法】 第一步，验证STP协议透传功能是否全局使能并在接口上开启。
ProviderS1#show l2protocol-tunnel stp
L2protocol-tunnel: Stp Enable
GigabitEthernet 0/1 l2protocol-tunnel stp enable
第二步，确认Tunnel口的配置是否正确，关注点：接口类型是否为dot1q-tunnel，外层Tag VLAN是否为Native
VLAN且其是否已加入接口的许可VLAN列表，服务商网络边缘设备上链口的类型是否为Uplink。
ProviderS1#show running-config
interface GigabitEthernet 0 /1
switchport mode dot1q-tunnel
switchport dot1q-tunnel allowed vlan add untagged 200
switchport dot1q-tunnel native vlan 200
l2protocol-tunnel stp enable
spanning-tree bpdufilter enable
！
interface GigabitEthernet 0 /5
switchport mode uplink


配置指南 QINQ

**常见错误**

 需要透传STP协议报文时，未全局开启STP协议转发功能，导致STP协议无法透传。
 透传协议报文时，没有在全局和接口上开启全局透传使能，导致无法透传。

#### 13.6 监视与维护

**清除各类信息**

无

**查看运行情况**

作用 命令
显示接口的dot1q-tunnel是否打开 show dot1q-tunnel^ [^ interfaces^ intf-id^ ]^
显示dot1q-tunnel口配置 show interfaces dot1q-tunnel
显示基于协议的dot1q-tunnel端口vid
添加策略表
show registration-table [ interfaces intf-id ]

显示基于协议access,trunk,hybrid端口
vid修改策略表
show translation-table [ interfaces intf-id ]

显示接口的vlan mapping show interfaces [ intf-id ] vlan-mapping
显示基于数据流的vid变更或添加策略
表
show traffic-redirect [ interfaces intf-id ]

显示接口tpid的配置 show frame-tag tpid interfaces [ intf-id ]
显示优先级复制配置 show inner-priority-trust
显示优先级映射的配置 show interface intf-name remark
显示MAC地址复制配置 show mac-address-mapping
显示二层透传配置 show l2protocol-tunnel { gvrp | stp }

**查看调试信息**

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。

作用 命令
打开QINQ的调试开关。 debug bridge qinq^


配置指南 ERPS

### 14 ERPS

#### 14.1 概述

ERPS（Ethernet Ring Protection Switching，以太环网保护切换协议）为ITU开发的一种环网保护协议，也称G.8032。它是
一个专门应用于以太环网的链路层协议。它在以太环网完整时能够防止数据环路引起的广播风暴，而当以太环网上一条链路断
开时能迅速恢复环网上各个节点之间的通信。

目前，解决二层网络环路问题的技术还有STP。STP应用比较成熟，但其收敛的时间比较长（秒级）。ERPS是专门应用于以
太环网的链路层协议，二层收敛性能达50ms以内，具有比STP 更快的收敛速度。

**协议规范**

 ITU-T G.8032/Y.1344: Ethernet ring protection switching

#### 14.2 典型应用

典型应用 场景描述
单环保护 网络拓扑中只有一个环。
相切环保护 网络拓扑中的两个环共用一台设备。
相交环保护 网络拓扑中有两个或两个以上的环共用一条链路。

###### 14.2.1 单环保护

**应用场景**

网络拓扑中只有一个环网需要保护的应用场景。

以下图为例，网络拓扑中只有一个环；有且仅有一个RPL owner节点；有且仅有一条RPL链路；所有节点需具有相同的R-APS

VLAN。

 环网中所有设备都需要支持ERPS功能。
 环网中的设备之间的链路必须直连，不能有中间设备。

图 14 - 1


配置指南 ERPS

【注释】 环中的四台设备均为汇聚交换机。

**功能部属**

 所有的节点在物理拓扑上以环的方式连接。

 环路保护协议通过阻塞RPL链路，确保不会成环(Loop)。如上图所示，Node1和Node2间的链路为RPL链路。

 对相邻节点间的每条链路进行故障检测。

###### 14.2.2 相切环保护

**应用场景**

网络拓扑中两个共用一台设备的环网需要保护的应用场景。

以下图为例，网络拓扑中的两个环共用一台设备；每个环有且仅有一个RPL owner节点，每个环有且仅有一条RPL链路；不

同环需具有不同的R-APS VLAN。

 环网中所有设备都需要支持ERPS功能。
 环网中的设备之间的链路必须直连，不能有中间设备。

图 14 - 2


配置指南 ERPS

【注释】 环中的设备均为汇聚交换机。

**功能部属**

 所有的节点在物理拓扑上以环的方式连接。

 环路保护协议通过阻塞每个环的RPL链路，确保不会成环(Loop)。

 对相邻节点间的每条链路进行故障检测。

###### 14.2.3 相交环保护

**应用场景**

网络拓扑中有两个或两个以上的环共用一条链路（相交的两个节点间必须直连，不能再有其它节点）。

以下图为例，网络拓扑中有四个环；每个环有且仅有一个RPL owner节点，每个环有且仅有一条RPL链路；不同环需具有不

同的R-APS VLAN。

 环网中所有设备都需要支持ERPS功能。
 环网中的设备之间的链路必须直连，不能有中间设备。

图 14 - 3


配置指南 ERPS

【注意】 环中的设备均为汇聚交换机。

**功能部属**

 所有的节点在物理拓扑上以环的方式连接。

 环路保护协议通过阻塞每个环的RPL链路，确保不会成环(Loop)。

 对相邻节点间的每条链路进行故障检测。

#### 14.3 功能详解

**基本概念**

######  以太环

以太环分为普通以太环和以太子环：

 **普通以太环：** 是一个环形连接的以太网网络拓扑。

 **以太子环：** 以太子环为非闭环拓扑，它通过相交节点挂接在其它环或网络上，和相交节点间归属于其它环或网络的通道一
起形成闭环拓扑。

每个以太环（不论是普通以太环还是以太子环）都有以下两种状态：

 Idle **状态** ：整个环网物理链路是连通的。

 Protection **状态** ：环网中某处物理链路断开。

######  链路与通道


配置指南 ERPS

 RPL **（** Ring Protection Link **，环保护链路）** ：每个以太环（不论是普通以太环还是以太子环）都有且仅有一条RPL。当
以太环处于Idle状态时，RPL链路处于阻塞状态，不转发数据报文，以避免形成环路。如图 2 所示，Node1与Node4
间的链路为以太环ERPS1的RPL链路，Node4阻塞RPL端口（RPL链路对应的端口）；Node4与Node5间的链路为
以太环ERPS2的RPL链路，Node5阻塞RPL端口。

 **子环链路** ：在相交环当中，归属于子环，由子环控制的链路。如图 3 所示，假设ERPS1是普通以太环，ERPS2是以太
子环，则Node 4 与Node5间的链路及Node3与Node5间的链路为子环ERPS2的链路，其它链路归属于普通以太环
ERPS1。

### Node3与Node4间的链路属于普通以太环ERPS1，不属于以太子环ERPS2，不受ERPS2的控制。^

 R-APS **（** Ring Auto Protection Switching **，自动环保护切换）** virtual channel：在相交环中，相交节点间，用于传输
子环协议报文，但不属于子环的通路被称为子环的R-APS虚拟通道。如图 3 所示，由于Node1阻塞RPL链路，子环ERPS2
的协议报文在以太环ERPS1中，通过Node3与Node4间的直连链路传播，则Node3与Node4间的直连通路就被称为
子环ERPS2的R-APS虚拟通道。

######  节点

以太环上的每台设备都称为一个节点。

对于某个特定的以太环而言，节点的角色分为下列几种：

 RPL owner **节点：** 紧挨着RPL链路，在以太环无故障的情况下，负责阻塞RPL链路，防止网络出现环路的节点。每个
以太环（不论是普通以太环还是以太子环）都有且仅有一个RPL owner节点。如图 2 所示，Node1为以太环ERPS1的
RPL owner节点；Node6为以太子环ERPS2的RPL owner节点。

 **非** RPL owner **节点：** 以太环上除RPL owner节点外的其它节点。如图 2 所示，除Node1和Node6外的其它节点，被
称为各个环的非RPL owner节点。

对于全局（指不针对某个特定的以太环）而言，节点的角色分为下列几种：

 **相交节点：** 在相交以太环中，同时属于多个环的节点被称为相交节点。如图 3 所示，Node3与Node4被称为相交节点。

 **非相交节点：** 在相交以太环中，只属于某个以太环的节点被称为非相交节点。如图 3 所示，如Node2被称为非相交节点。

######  VLAN

ERPS中有两种类型的VLAN，一种是R-APS VLAN，另一种是数据VLAN。

 R-APS VLAN **：** R-APS VLAN 用来传递ERPS协议报文。设备上接入ERPS环的端口都属于R-APS VLAN，且只有接
入ERPS环的端口可加入此VLAN。不同环的R-APS VLAN必须不同。R-APS VLAN的接口上不允许配置IP 地址。

 **数据** VLAN **：** 与R-APS VLAN 相对，数据VLAN 用来传输数据报文。数据VLAN 中既可包含ERPS环端口，也可包含
非ERPS环端口。

### 不同ERPS环的R-APS VLAN必须配置成不同，否则可能导致协议工作异常。因不同ERPS环的报文通过R-APS VLAN

```
来区分。
```

######  ERPS 协议报文


配置指南 ERPS

ERPS协议报文（也称R-APS报文）的类型有SF报文、NR报文、(NR,RB)报文和Flush报文四种，其作用分别如下：

 SF **（** Signal Fail **）报文** ：当节点的自身链路down 时，发送该报文通知其它节点。

 NR **（** No Request **）报文** ：当节点的自身链路从故障中恢复时，发送该报文通知RPL owner节点。

 （NR **，** RB) **（** No Request **，** RPL Blocked **）报文** ：由RPL owner发送，当ERPS环上的所有设备均无故障时，RPL owner
会周期性发送此报文。

 Flush **报文** ：在相交环当中，由相交节点发送，用于将子环拓扑的变化通知子环所挂接的以太环上的其它设备。

######  ERPS 定时器

ERPS协议的定时器有Holdoff timer、Guard timer和WTR timer三种，及其作用分别如下：

 Holdoff timer **定时器** ：该定时器用于防止由于链路的间歇性故障，导致ERPS不断进行拓扑切换。配置了此定时器之后，
当检测到链路故障时，ERPS不立即执行拓扑切换，而是等定时器超时之后，如果确认链路仍故障，才执行拓扑切换。

 Guard timer **定时器** ：该定时器用于防止设备接收到过时的R-APS消息。当设备检测到链路从故障中恢复时，对外发送
链路恢复的消息报文，并启动guard定时器。在guard定时器超时之前，除指示子环拓扑变化的flush报文外，其它的报
文都将被直接丢弃，不进行处理。

 WTR **（** Wait-to-restore **）** timer **定时器** ：此定时器只对RPL owner设备有效，对其它设备无效。该定时器主要用于防止
RPL owner对环网的状态产生误判。当RPL owner检测到故障恢复时，不立即执行拓扑切换，而是等WTR定时器超时
之后，如果确认以太环的确已从故障中恢复，才执行拓扑切换。如果在WTR定时器超时之前又再次检测到环网故障，则
取消WTR定时器，不再执行拓扑切换。

**功能特性**

功能特性 作用
环网保护 防止数据环路引起的广播风暴，而当以太环网上一条链路断开时能迅速恢复环网上各个节点之间的通
信。
负载均衡 同一个环网上配置多个以太环，不同以太环发送不同VLAN的流量实现流量的负载分担，即不同VLAN
的流量沿不同的路径进行转发。

###### 14.3.1 环网保护

防止数据环路引起的广播风暴，而当以太环网上一条链路断开时能迅速恢复环网上各个节点之间的通信。

**工作原理**

######  正常状态

 所有的节点在物理拓扑上以环的方式连接。

 环路保护协议通过阻塞RPL链路，确保不会成环(Loop)。

 对相邻节点间的每条链路进行故障检测。


配置指南 ERPS

######  链路故障

 与故障相邻的节点检测到故障。

 与故障链路相临的节点对故障链路进行阻塞，并使用SF（Signal Fail）报文向环上的其他节点报告故障。

 R-APS(SF)消息触发RPL拥有节点打开RPL端口。R-APS(SF)消息还触发所有的节点更新各自MAC 表项和ARP/ND 表
项，然后节点进入保护状态（Protection）。

######  链路恢复

 当故障恢复时，故障相邻的节点继续保持阻塞状态，并发送NR（No Request）报文，表示没有本地故障。

 当RPL拥有节点收到第一个R-APS(NR)消息后，开始启动WTR定时器。

 当WTR timer耗尽后，RPL拥有节点阻塞RPL，并发送（NR，RB)（No Request，RPL Blocked）报文。

 其他节点收到这个消息后，更新各自MAC 表项和ARP/ND 表项，发送NR（No Request）报文的那个节点停止周期性
发送报文，并打开原先阻塞的端口。

 环网又恢复到了最初的正常状态。

**相关配置**

######  配置 R-APS VLAN

缺省情况下，设备没有配置R-APS VLAN。

使用erps raps-vlan命令可以配置ERPS的R-APS VLAN，该VLAN作为ERPS环的管理VLAN，用于传输ERPS报文。

######  配置 ERPS 环

在R-APS VLAN模式下，使用rpl-port命令可以配置相应R-APS VLAN的ERPS环。

######  配置 RPL 链路和 RPL owner 节点

在R-APS VLAN模式下，使用rpl-port指定相应RPL链路和RPL owner节点。

###### 14.3.2 负载均衡

同一个物理环网上配置多个以太环，不同以太环发送不同VLAN的流量实现流量的负载分担，即不同VLAN 的流量沿不同的
路径进行转发。

**工作原理**

在同一个环网中，可能同时存在多个VLAN 的数据流量，ERPS可以实现流量的负载分担，即不同VLAN 的流量沿不同的路
径进行转发。

图 14 - 4 单环负载分担


配置指南 ERPS

通过在同一个物理环网上配置多个以太环，不同以太环发送不同VLAN（称为保护VLAN）的流量，实现不同VLAN的数据流
量在该环网中的拓扑不同，从而达到负载分担的目的。

如图 4 所示，一个物理环网对应了两个以太环，两个以太环保护的VLAN不同，Node1为ERPS 1 的RPL owner，Node 3 为
ERPS 2 的RPL owner。通过配置，可以实现不同VLAN分别阻塞不同的链路，从而实现单环的负载分担。

**相关配置**

######  配置以太环保护 VLAN

###### 在R-APS VLAN模式下，使用protected-instance可以配置对应所需要保护的VLAN集合，以实现负载均衡的功能。

#### 14.4 配置详解

配置项 配置建议 & 相关命令

单环配置（基础功能）

### 全局模式，必选配置。^

```
erps enable 打开ERPS功能
erps raps-vlan 配置以太环的R-APS VLAN
```

### R-APS VLAN模式，必选配置。^

```
ring-port 配置ERPS环
rpl-port 配置RPL owner
```

state enable (^) 使能指定的R-APS环

### 相切环配置 以单环配置为基础的相交切场景应用。

相交环配置

### 以单环配置为基础，在R-APS VLAN模式下，可选配置。^

```
associate sub-ring raps-vlan 配置关联以太子环
sub-ring tc-propagation enable 使能子环拓扑变化通告
```

配置指南 ERPS

### 负载均衡配置 以单环配置为基础，在R-APS VLAN模式下，可选配置。^

```
protected-instance 配置以太环保护VLAN
```

### ERPS配置修改 以单环配置为基础，在R-APS VLAN模式下，可选配置。^

```
timer 修改定时器参数
```

###### 14.4.1 单环配置（基本功能）

**配置效果**

 单环为ERPS协议的基本场景，是其它场景应用的基础。

 建立ERPS单环拓扑，实现数据链路的冗余备份。

 ERPS环网内链路发生故障，可迅速进行链路切换。

**注意事项**

 只能配置一个RPL owner节点，且只能配置一条RPL链路。

 所有节点须具有相同的R-APS VLAN环。

 加入ERPS环的端口必须是trunk口；当端口加入ERPS环之后，不再允许修改端口的trunk属性。

 配置ERPS环的端口不管ERPS环有没有使能，都不参与STP计算。在配置ERPS环过程中，需要保证环端口关闭STP

```
计算情况下不存在环路。
```

 ERPS和RERP、REUP不共用端口。

**配置方法**

######  配置以太环的 R-APS VLAN

 全局模式下，必选配置。

 须在ERPS环每台交换机配置相同的以太环R-APS VLAN，用于传输ERPS协议报文。

######  配置 ERPS 环端口

 R-APS VLAN模式下，必选配置。

 将组成环的对应端口，配置为ERPS环端口。

######  配置 RPL owner 端口

 R-APS VLAN模式下，必选配置。

 每个ERPS环有且仅有一个设备配置为RPL owner节点，该节点控制需要阻断的端口。


配置指南 ERPS

######  使能指定的 R-APS 环

 R-APS VLAN模式下，必选配置。

 须在每台交换机上相同的R-APS VLAN下使能。

######  打开 ERPS 全局功能

 全局模式下，必选配置。

 在ERPS环上每台交换机打开ERPS全局功能。

**检验方法**

 在各个节点上执行show erps命令，确认配置。

**相关命令**

######  配置以太环的 R-APS VLAN

```
【命令格式】 erps raps-vlan vlan-id
【参数说明】 vlan-id：R-APS VLAN ID
【命令模式】 全局模式
【使用指导】 只有同时使能全局ERPS协议和指定环的ERPS协议之后，指定环的ERPS协议才真正开始运行。
```

######  配置 ERPS 环

```
【命令格式】 ring-port^ west^ {interface-name1^ | virtual-channel }^ east^ { interface-name2^ | virtual-channel}^
【参数说明】 interface-name1：West port的名称；
interface-name2：East port的名字；
virtual-channel ： 将端口指定为虚拟链路上的端口
【命令模式】 R-APS VLAN模式
【使用指导】 R-APS VLAN必须是设备上未被使用的VLAN，VLAN 1不能被设置为 R-APS VLAN。
不同设备的同一个以太环需配置相同的R-APS VLAN。
如果要在一台未配置ERPS功能的设备上透传ERPS协议报文，应保证该设备上只有接入ERPS环的那两个
端口允许该ERPS环所对应R-APS VLAN报文通过，而其它端口都不允许其通过；否则，其它VLAN 的报文
可能通过透传进入R-APS VLAN，从而对ERPS环产生冲击。
```

######  配置 RPL owner 端口

```
【命令格式】 rpl-port { west | east } rpl-owner
【参数说明】 west：指定west对应的端口为rpl-owner
east ：指定east对应的端口为rpl-owner
【命令模式】 R-APS VLAN模式^
【使用指导】 每个环需要且仅能配置一条RPL链路和一个RPL owner节点。
```

######  使能指定的 R-APS 环

```
【命令格式】 state enable
```

配置指南 ERPS

```
【参数说明】 -
【命令模式】 R-APS VLAN模式^
【使用指导】 只有同时使能全局ERPS协议和指定环的ERPS协议之后，指定环的ERPS协议才真正开始运行。
```

######  打开 ERPS 全局功能

```
【命令格式】 erps enable
【参数说明】 -^
【命令模式】 全局模式
【使用指导】 只有同时使能全局ERPS协议和指定环的ERPS协议之后，指定环的ERPS协议才真正开始运行。
```

**配置举例**

```
【网络环境】
```

【配置方法】 (^)  进入特权模式，配置R-APS VLAN。
 配置以太环端口的链路模式。
 进入R-APS VLAN模式，配置加入以太环，参于ERPS协议计算的端口。
 指定RPL owner端口。
 使能指定环的ERPS功能。
 使能全局ERPS功能。
Node1 (^) # 进入特权模式
Ruijie# configure terminal

# 配置R-APS VLAN

Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# exit

# 配置以太环端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-gigabitEthernet 0/1)# switchport mode trunk


配置指南 ERPS

```
Ruijie(config-if-gigabitEthernet 0/1)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if-gigabitEthernet 0/2)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/2)# exit
# 进入erps配置模式。
Ruijie(config)# erps raps-vlan 4093
# 配置加入以太环，参于ERPS协议计算的端口。
Ruijie(config-erps 4093)# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2
# 使能指定环的ERPS功能。
Ruijie(config-erps 4093)# state enable
# 使能全局ERPS功能。
Ruijie(config-erps 4093)# exit
Ruijie(config)# erps enable
Node2 Node2的配置同Node1。
Node3 Node3的配置同Node1。
```

Node4 (^) # 进入特权模式
Ruijie# configure terminal

# 配置R-APS VLAN

Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# exit

# 配置以太环端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-gigabitEthernet 0/1)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/1)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if-gigabitEthernet 0/2)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/2)# exit

# 进入erps配置模式。

Ruijie(config)# erps raps-vlan 4093

# 配置加入以太环，参于ERPS协议计算的端口。

Ruijie(config-erps 4093)# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2

# 指定RPL owner端口。


配置指南 ERPS

```
Ruijie(config-erps 4093)# rpl-port east rpl-owner
# 使能指定环的ERPS功能。
Ruijie(config-erps 4093)# state enable
Ruijie(config-erps 4093)# exit
# 使能全局ERPS功能。
Ruijie(config)# erps enable
```

```
【检验方法】 在各个节点上执行show erps命令，确认配置。以面以Node1和Node4节点为例
```

Node1 (^) Ruijie# show erps
ERPS Information
Global Status : Enabled

Link monitored by : Not Oam
--------------------------------------------

R-APS VLAN : 4093
Ring Status : Enabled
West Port : Gi 0/1 (Forwardin)
East Port : Gi 0/2 (Forwardin)
RPL Port : None
Protected VLANs : ALL
RPL Owner : Enabled
Holdoff Time : 0 milliseconds
Guard Time : 500 milliseconds
WTR Time : 2 minutes
Current Ring State : Idle
Associate R-APS VLAN :
Node4 (^) Ruijie# show erps
ERPS Information
Global Status : Enabled

Link monitored by : Not Oam
--------------------------------------------

R-APS VLAN : 4093
Ring Status : Enabled


配置指南 ERPS

```
West Port : Gi 0/1 (Forwardin)
East Port : Gi 0/2 (Blocking)
RPL Port : East Port
Protected VLANs : ALL
RPL Owner : Enabled
Holdoff Time : 0 milliseconds
Guard Time : 500 milliseconds
WTR Time : 2 minutes
Current Ring State : Idle
Associate R-APS VLAN :
```

**常见错误**

 已使能R-APS环，但是全局没有开启ERPS功能，此时ERPS功能还是不能生效；

 环里配置了多个RPL owner节点；

 环的节点所配置的R-APS VLAN不同。

###### 14.4.2 相切环配置

**配置效果**

 以单环为基础，两个ERPS单环共用一台设备的相切环，实现相交环的数据链路冗余备份。

 相交的ERPS环内链路发生故障，可迅速进行链路切换。

**注意事项**

 相切环的配置与单环配置基本一致，仅需在相切节点上关联两个ERPS环。

 只能配置一个RPL owner节点，且只能配置一条RPL链路。

 所有节点须具有相同的R-APS VLAN环。

 加入ERPS环的端口必须是trunk口；当端口加入ERPS环之后，不再允许修改端口的trunk属性。

 配置ERPS环的端口不管ERPS环有没有使能，都不参与STP计算。在配置ERPS环过程中，需要保证环端口关闭STP

```
计算情况下不存在环路。
```

 ERPS和RERP、REUP不共用端口。


配置指南 ERPS

**配置方法**

 与单环配置方法一致，仅需在相切节点上关联两个ERPS环。

**检验方法**

 在各个节点上执行show erps命令，确认配置。

**相关命令**

 与单环配置命令一致。

**配置举例**

```
【网络环境】
```

【配置方法】 (^)  进入特权模式，配置R-APS VLAN。
 配置以太环端口的链路模式。
 进入R-APS VLAN模式，配置加入以太环，参于ERPS协议计算的端口。
 指定RPL owner端口。
 使能指定环的ERPS功能。
 使能全局ERPS功能。
Node1 (^) # 进入特权模式 。
Ruijie# configure terminal

# 配置R-APS VLAN 4093 。

Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# exit

# 配置以太环端口的链路模式。


配置指南 ERPS

```
Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-gigabitEthernet 0/1)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/1)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if-gigabitEthernet 0/2)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/2)# exit
# 进入ERPS配置模式。
Ruijie(config)# erps raps-vlan 4093
# 配置加入以太环，参于ERPS协议计算的端口
Ruijie(config-erps 4093)# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2
# 使能指定环的ERPS功能
Ruijie(config-erps 4093)# state enable
Ruijie(config-erps 4093)# exit
# 使能全局ERPS功能。
Ruijie(config)# erps enable
Node2 Node2的配置同Node1。
```

Node3 (^) Ruijie# configure terminal

# 配置R-APS VLAN 4093

Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# exit

# 配置以太环端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-gigabitEthernet 0/1)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/1)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if-gigabitEthernet 0/2)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/2)# exit

# 进入ERPS配置模式

Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2
Ruijie(config-erps 4093)# state enable
Ruijie(config-erps 4093)# exit


配置指南 ERPS

```
# 配置R-APS VLAN 100
Ruijie(config)# erps raps-vlan 100
Ruijie(config-erps 100)# exit
Ruijie(config)# interface gigabitEthernet 0/ 3
Ruijie(config-if-gigabitEthernet 0/3)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/3)# exit
Ruijie(config)# interface gigabitEthernet 0/ 4
Ruijie(config-if-gigabitEthernet 0/4)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/4)# exit
# 进入ERPS配置模式
Ruijie(config)# erps raps-vlan 100
Ruijie(config-erps 100)# ring-port west gigabitEthernet 0/ 3 east gigabitEthernet 0/ 4
Ruijie(config-erps 100)# state enable
Ruijie(config-erps 4093)# exit
Ruijie(config)# erps enable
```

Node4 (^) Ruijie# configure terminal

# 配置R-APS VLAN 4093

Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# exit

# 配置以太环端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-gigabitEthernet 0/1)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/1)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if-gigabitEthernet 0/2)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/2)# exit

# 进入ERPS配置模式

Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2

# 指定RPL owner端口。

Ruijie(config-erps 4093)# rpl-port east rpl-owner


配置指南 ERPS

```
Ruijie(config-erps 4093)# state enable
Ruijie(config-erps 4093)# exit
Ruijie(config)# erps enable
```

Node5 (^) Ruijie# configure terminal

# 配置R-APS VLAN 100

Ruijie(config)# erps raps-vlan 100
Ruijie(config-erps 100)# exit

# 配置以太环端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-gigabitEthernet 0/1)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/1)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if-gigabitEthernet 0/2)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/2)# exit

# 进入ERPS配置模式

Ruijie(config)# erps raps-vlan 100
Ruijie(config-erps 100)# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2
Ruijie(config-erps 100)# state enable
Ruijie(config-erps 100)# exit
Ruijie(config)# erps enable
Node6 (^) Ruijie# configure terminal

# 配置R-APS VLAN 100

Ruijie(config)# erps raps-vlan 100
Ruijie(config-erps 100)# exit

# 配置以太环端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-gigabitEthernet 0/1)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/1)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if-gigabitEthernet 0/2)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/2)# exit


配置指南 ERPS

```
# 进入ERPS配置模式
Ruijie(config)# erps raps-vlan 100
Ruijie(config-erps 100)# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2
# 指定RPL owner端口。
Ruijie(config-erps 100)# rpl-port east rpl-owner
Ruijie(config-erps 100)# state enable
Ruijie(config)# erps enable
```

【检验方法】 (^) # 在各个节点上执行show erps命令，确认配置。以面以Node3节点为例，举例说明：
(^) Ruijie# show erps
ERPS Information
Global Status : Enabled

Link monitored by : Not Oam
--------------------------------------------

R-APS VLAN : 100
Ring Status : Enabled
West Port : Gi 0/3 (Forwarding)
East Port : Gi 0/4 (Forwarding)
RPL Port : None
Protected VLANs : ALL
RPL Owner : Disabled
Holdoff Time : 0 milliseconds
Guard Time : 500 milliseconds
WTR Time : 2 minutes
Current Ring State : Idle

Associate R-APS VLAN :
--------------------------------------------

R-APS VLAN : 4093
Ring Status : Enabled
West Port : Gi 0/1 (Forwarding)
East Port : Gi 0/2 (Forwarding)
RPL Port : East Port


配置指南 ERPS

```
Protected VLANs : ALL
RPL Owner : Disabled
Holdoff Time : 0 milliseconds
Guard Time : 500 milliseconds
WTR Time : 2 minutes
Current Ring State : Idle
Associate R-APS VLAN :
```

**常见错误**

 已使能R-APS环，但是全局没有开启ERPS功能，此时ERPS功能还是不能生效。

 环里配置了多个RPL owner节点。

 同一环的节点所配置的R-APS VLAN不同

###### 14.4.3 相交环配置

**配置效果**

 多个ERPS环共用链路，实现相交环的数据链路冗余备份。

 任意一个ERPS环内链路发生故障，都可迅速进行链路切换

**注意事项**

 每个ERPS环只允许配置一个RPL owner节点，且只能配置一条RPL链路。

 同一ERPS环内节点须具有相同的R-APS VLAN环。

 以太环的所有节点须关联上其子环。

 加入ERPS环的端口必须是trunk口；当端口加入ERPS环之后，不再允许修改端口的trunk属性。

 配置ERPS环的端口不管ERPS环有没有使能，都不参与STP计算。在配置ERPS环过程中，需要保证环端口关闭STP

```
计算情况下不存在环路。
```

 ERPS和RERP、REUP不共用端口。

**配置方法**

在单环配置的基础上，增加如下配置：


配置指南 ERPS

######  使能子环拓扑变化通告

 R-APS VLAN模式下，可选配置。

 在相交环的相交节点上须配置使能子环的拓扑变化通告。

 子环的拓扑发生变化时，如果相交节点间的链路处于故障状态或阻塞状态，相交节点将发送报文通知子环所关联的其它以
太环上的节点进行拓扑更新。

######  关联以太子环

 R-APS VLAN模式下，可选配置。

 在相交环主环的各节点须配置关联对应的以太子环。

 配置关联关系是为了使子环的协议报文可以在其它以太环中传播。

**检验方法**

 在各个节点上执行show erps命令，确认配置。

**相关命令**

######  使能子环拓扑变化通告

```
【命令格式】 sub-ring tc-propagation enable
【参数说明】 -^
【命令模式】 R-APS VLAN模式
【使用指导】 只需要在相交环的相交节点上配置此命令。
```

######  关联以太子环

```
【命令格式】 associate sub-ring raps-vlan vlan-list
【参数说明】 vlan-list：子环的R-APS VLAN
【命令模式】 R-APS VLAN模式
【使用指导】 需要在以太环的所有节点上配置该命令，使其子环的ERPS协议报文可以在该以太环中传播。
配置关联关系主要是为了使子环的协议报文可以在其它以太环中传播，用户也可以采用VLAN模块提供的配
置命令，配置VLAN及端口与VLAN的关系，以使子环的协议报文可以在其它以太环中传播，且不会泄露到
用户网络。
```

**配置举例**


配置指南 ERPS

```
【网络环境】
```

【配置方法】 (^)  进入特权模式，配置R-APS VLAN。
 配置以太环端口的链路模式。
 进入R-APS VLAN模式，配置加入以太环，参于ERPS协议计算的端口。
 指定RPL owner端口。
 使能指定环的ERPS功能。
 以太环的节点关联以太子环。
 相交节点上使能子环的拓扑变化通告。
 使能全局ERPS功能。
Node1 (^) # 进入特权模式
Ruijie# configure terminal

# 配置R-APS VLAN 4093

Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# exit

# 配置以太环端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-gigabitEthernet 0/1)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/1)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if-gigabitEthernet 0/2)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/2)# exit


配置指南 ERPS

```
# 进入erps配置模式。
Ruijie(config)# erps raps-vlan 4093
# 配置加入以太环，参于ERPS协议计算的端口。
Ruijie(config-erps 4093)# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2
# 指明RPL链路所在的端口和RPL owner。
Ruijie(config-erps 4093)# rpl-port east rpl-owner
# 使能指定环的ERPS功能。
Ruijie(config-erps 4093)# state enable
# 使能全局ERPS功能。
Ruijie(config-erps 4093)# exit
Ruijie(config)# erps enable
# 配置子环ERP4的R-APS VLAN
Ruijie(config)# erps raps-vlan 300
Ruijie(config-erps 300)# exit
# 配置ERP4环端口的链路模式。
Ruijie(config)# interface gigabitEthernet 0/ 5
Ruijie(config-if-gigabitEthernet 0/5)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/5)# exit
# 进入ERPS配置模式。
Ruijie(config)# erps raps-vlan 300
# 配置加入以太环，参于ERPS协议计算的端口。
Ruijie(config-erps 300)# ring-port west gigabitEthernet 0/ 5 east virtual-channel
# 使能ERP4的ERPS功能。
Ruijie(config-erps 300)# state enable
# ERPS1关联ERPS2、ERPS3、ERPS4。
Ruijie(config-erps 300)# exit
Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# associate sub-ring raps-vlan 100,200,300
```

Node2 (^) # 进入特权模式
Ruijie# configure terminal

# 配置R-APS VLAN 4093


配置指南 ERPS

```
Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093 )# exit
# 配置以太环端口的链路模式。
Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-gigabitEthernet 0/1)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/1)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if-gigabitEthernet 0/2)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/2)# exit
# 进入erps配置模式。
Ruijie(config)# erps raps-vlan 4093
# 配置加入以太环，参于ERPS协议计算的端口。
Ruijie(config-erps 4093)# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2
# 使能指定环的ERPS功能。
Ruijie(config-erps 4093)# state enable
# 使能全局ERPS功能。
Ruijie(config-erps 4093)# exit
Ruijie(config)# erps enable
# ERPS1关联ERPS2、ERPS3、ERPS4。
Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# associate sub-ring raps-vlan 100,200,300
```

Node3 (^) # Node3需要在Node2配置的基础上，再配置以下命令：

# 进入特权模式

Ruijie# configure terminal

# 配置子环ERPS2的R-APS VLAN

Ruijie(config)# erps raps-vlan 100
Ruijie(config-erps 100)# exit

# 配置ERPS2环端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/ 3
Ruijie(config-if-gigabitEthernet 0/ 3 )# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/ 3 )# exit


配置指南 ERPS

```
# 进入ERPS配置模式。
Ruijie(config)# erps raps-vlan 100
# 配置加入以太环，参于ERPS协议计算的端口。
Ruijie(config-erps 100)# ring-port west virtual-channel east gigabitEthernet 0/ 3
# 使能ERPS2的ERPS功能。
Ruijie(config-erps 100)# state enable
# 配置子环ERPS3的R-APS VLAN
Ruijie(config)# erps raps-vlan 200
Ruijie(config-erps 200)# exit
# 配置ERPS3环端口的链路模式。
Ruijie(config)# interface gigabitEthernet 0/ 4
Ruijie(config-if-gigabitEthernet 0/4)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/4)# exit
# 进入ERPS配置模式。
Ruijie(config)# erps raps-vlan 200
# 配置加入以太环，参于ERPS协议计算的端口。
Ruijie(config-erps 200)# ring-port west virtual-channel east gigabitEthernet 0/ 4
# 使能ERP2的ERPS功能。
Ruijie(config-erps 200)# state enable
# 关联以太子环ERPS2、ERPS3和ERPS4。
Ruijie(config-erps 200)# exit
Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# associate sub-ring raps-vlan 100,200,300
```

Node4 (^) # Node4需要在Node2配置的基础上，再配置以下命令：

# 进入特权模式

Ruijie# configure terminal

# 配置子环ERPS2的R-APS VLAN

Ruijie(config)# erps raps-vlan 100
Ruijie(config-erps 100)# exit

# 配置ERPS2环端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/ 3


配置指南 ERPS

```
Ruijie(config-if-gigabitEthernet 0/3)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/3)# exit
# 进入ERPS配置模式。
Ruijie(config)# erps raps-vlan 100
# 配置加入以太环，参于ERPS协议计算的端口。
Ruijie(config-erps 100)# ring-port west virtual-channel east gigabitEthernet 0/ 3
# 使能ERPS2的ERPS功能。
Ruijie(config-erps 100)# state enable
# 配置子环ERPS3的R-APS VLAN
Ruijie(config)# erps raps-vlan 200
Ruijie(config-erps 200)# exit
# 配置ERPS3环端口的链路模式。
Ruijie(config)# interface gigabitEthernet 0/ 4
Ruijie(config-if-gigabitEthernet 0/4)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/4)# exit
# 进入ERPS配置模式。
Ruijie(config)# erps raps-vlan 200
# 配置加入以太环，参于ERPS协议计算的端口。
Ruijie(config-erps 200)# ring-port west virtual-channel east gigabitEthernet 0/ 4
# 使能ERPS3的ERPS功能。
Ruijie(config-erps 200)# state enable
# 配置子环ERPS4的R-APS VLAN
Ruijie(config-erps 200)# exit
Ruijie(config)# erps raps-vlan 300
Ruijie(config-erps 300)# exit
# 配置ERPS4环端口的链路模式。
Ruijie(config)# interface gigabitEthernet 0/ 5
Ruijie(config-if-gigabitEthernet 0/ 5 )# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/ 5 )# exit
# 进入ERPS配置模式。
Ruijie(config)# erps raps-vlan 300
# 配置加入以太环，参于ERPS协议计算的端口。
```

配置指南 ERPS

```
Ruijie(config-erps 300)# ring-port west virtual-channel east gigabitEthernet 0/ 5
# 使能ERPS4的ERPS功能。
Ruijie(config-erps 300)# state enable
# 关联普通以太子环ERPS2、ERPS3和ERPS4。
Ruijie(config-erps 300)# exit
Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps4093)# associate sub-ring raps-vlan 100,200,300
```

Node5 (^) # 进入特权模式
Ruijie# configure terminal

# 配置R-APS VLAN

Ruijie(config)# erps raps-vlan 100
Ruijie(config-erps 100)# end

# 配置以太环端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-gigabitEthernet 0/1)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/1)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if-gigabitEthernet 0/2)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/2)# exit

# 进入ERPS配置模式。

Ruijie(config)# erps raps-vlan 100

# 配置加入以太环，参于ERPS协议计算的端口。

Ruijie(config-erps 100 )# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2

# 指明RPL链路所在的端口和RPL owner。

Ruijie(config-erps 100)# rpl-port east rpl-owner

# 使能指定环的ERPS功能。

Ruijie(config-erps 100)# state enable

# 使能全局ERPS功能。

Ruijie(config-erps 100)# exit
Ruijie(config)# erps enable
Node6 (^) # Node6的配置基本同Node 5 ，只是需将R-APS VLAN改为VLAN 200。


配置指南 ERPS

Node7 (^) # Node7的配置基本同Node 5 ，只是需将R-APS VLAN改为VLAN 300。
【检验方法】 (^) # 在各个节点上执行show erps命令，确认配置。以面以Node3节点为例，举例说明：
(^) Ruijie# show erps
ERPS Information
Global Status : Enabled

Link monitored by : Not Oam
--------------------------------------------

R-APS VLAN : 100
Ring Status : Enabled
West Port : Virtual Channel
East Port : Gi 0/3 (Forwarding)
RPL Port : None
Protected VLANs : ALL
RPL Owner : Disabled
Holdoff Time : 0 milliseconds
Guard Time : 500 milliseconds
WTR Time : 2 minutes
Current Ring State : Idle

Associate R-APS VLAN :
--------------------------------------------

R-APS VLAN : 200
Ring Status : Enabled
West Port : Virtual Channel
East Port : Gi 0/4 (Forwarding)
RPL Port : None
Protected VLANs : ALL
RPL Owner : Disabled
Holdoff Time : 0 milliseconds
Guard Time : 500 milliseconds
WTR Time : 2 minutes
Current Ring State : Idle


配置指南 ERPS

```
Associate R-APS VLAN :
--------------------------------------------
R-APS VLAN : 4093
Ring Status : Enabled
West Port : Gi 0/1 (Forwarding)
East Port : Gi 0/2 (Blocking)
RPL Port : East Port
Protected VLANs : ALL
RPL Owner : Disabled
Holdoff Time : 0 milliseconds
Guard Time : 500 milliseconds
WTR Time : 2 minutes
Current Ring State : Idle
Associate R-APS VLAN : 100,200,300
```

**常见错误**

 已使能R-APS环，但是全局没有开启ERPS功能，此时ERPS功能还是不能生效。

 一个ERPS环里配置了多个RPL owner节点。

 同一个ERPS环的节点所配置的R-APS VLAN不同

 主环的节点未关联其对应的以太子环。

###### 14.4.4 负载均衡配置

**配置效果**

 在ERPS环内控制数据流走向，实现数据的负载均衡。

 当负载均衡的环网内链路发生故障，可迅速将流量切换到正常的链路上。

**注意事项**

 配置负载均衡功能前，先进入MST 配置模式，配置vlan与instance关系。

 配置负载均衡功能时，需要将设备所有数据VLAN填加进ERPS的保护VLAN中，否则未保护VLAN可引起网络环路。

 加入ERPS环的端口必须是trunk口；当端口加入ERPS环之后，不再允许修改端口的trunk属性。


配置指南 ERPS

 配置ERPS环的端口不管ERPS环有没有使能，都不参与STP计算。在配置ERPS环过程中，需要保证环端口关闭STP

```
计算情况下不存在环路。
```

 ERPS和RERP、REUP不共用端口。

**配置方法**

在单环配置的基础上，增加如下配置：

######  配置以太环所保护的 VLAN

 全局模式下，可选配置。

 当配置负载均衡功能时，须指定以太环所保护的VLAN。

**检验方法**

 在各个节点上执行show erps命令，确认配置。

**相关命令**

######  配置以太环所保护的 VLAN

```
【命令格式】 protected-instance instance-id-list
【参数说明】 instance-id-list：该以太环所保护的实例
【命令模式】 R-APS VLAN模式
【使用指导】 以太环所保护的实例对应的VLAN即为该以太环的保护VLAN
```

**配置举例**

```
【网络环境】
```

【配置方法】 (^)  进入特权模式，配置R-APS VLAN。
 配置以太环端口的链路模式。
 配置以太环保护的VLAN。


配置指南 ERPS

```
 进入R-APS VLAN模式，配置加入以太环，参于ERPS协议计算的端口。
 指定RPL owner端口。
 使能指定环的ERPS功能。
 使能全局ERPS功能。
```

Node1 (^) # 进入特权模式
Ruijie# configure terminal

# 配置以太环ERPS 1 ：

# 配置以太环ERPS1的端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-gigabitEthernet 0/1)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/1)# exit
Ruijie(config)# interface gigabitEthernet 0/ 2
Ruijie(config-if-gigabitEthernet 0/2)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/2)# exit

# 配置以太环ERPS1的保护VLAN、端口和RPL。

Ruijie(config)# spanning-tree mst configuration
Ruijie(config-mst)# instance 1 vlan 1 - 2000
Ruijie(config-mst)# exit
Ruijie(config)# erps raps-vlan 100
Ruijie(config-erps 100)# protected-instance 1
Ruijie(config-erps 100 )# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2
Ruijie(config-erps 100)# rpl-port west rpl-owner

# 配置以太环ERPS 2 ：

# 配置加入以太环ERPS2，参于ERPS协议计算的端口。

Ruijie(config)# spanning-tree mst configuration
Ruijie(config-mst)# instance 2 vlan 2001 - 4094
Ruijie(config-mst)# exit
Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# protected-instance 2
Ruijie(config-erps 4093 )# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 2

# 使能指定环的ERPS功能和全局ERPS功能。


配置指南 ERPS

```
Ruijie(config-erps 4093)# state enable
Ruijie(config-erps 4093)# exit
Ruijie(config)# erps enable
```

Node2 (^) # 除不需要配置RPL的命令外，Node2上的其它配置命令同Node1。
Node3 (^) # 除配置RPL的命令外，Node3上的其它配置命令同Node1。

# Node3上不配置以太环ERPS1的RPL，则是配置以太环ERPS2的RPL：

Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# rpl-port east rpl-owner
Node4 (^) Node4上的配置命令同Node2。
【检验方法】 (^) # 在各个节点上执行show erps命令，确认配置。以面以Node1节点为例，举例说明：
Node1 (^) Ruijie# show erps
ERPS Information
Global Status : Enabled

Link monitored by : Not Oam
--------------------------------------------

R-APS VLAN : 200
Ring Status : Enabled
West Port : Gi 0/1 (Blocking)
East Port : Gi 0/2 (Forwarding)
RPL Port : West Port
Protected VLANs : 1- 2000
RPL Owner : Enabled
Holdoff Time : 0 milliseconds
Guard Time : 500 milliseconds
WTR Time : 2 minutes
Current Ring State : Idle

Associate R-APS VLAN :
--------------------------------------------

R-APS VLAN : 4093
Ring Status : Enabled


配置指南 ERPS

```
West Port : Gi 0/1 (Forwarding)
East Port : Gi 0/2 (Blocking)
RPL Port : West Port
Protected VLANs : 2001- 4094
RPL Owner : Enabled
Holdoff Time : 0 milliseconds
Guard Time : 500 milliseconds
WTR Time : 2 minutes
Current Ring State : Idle
Associate R-APS VLAN :
```

**常见错误**

 已使能R-APS环，但是全局没有开启ERPS功能，此时ERPS功能还是不能生效。

 一个ERPS环里配置了多个RPL owner节点。

 同一个ERPS环的节点所配置的R-APS VLAN不同

###### 14.4.5 ERPS 配置修改

**配置效果**

 当ERPS环拓扑变化时，实现配置的平滑切换。

**注意事项**

 为了避免修改配置的过程中出现环路，在修改设备erps配置时，请先shutdown该环上的其中一个erps端口，配置完成

```
后再no shutdown；
```

 所有节点须具有相同的R-APS VLAN环。

 若只修改ERPS定时器，则可不关注此章节，直接修改配置。

**配置方法**

shutdown环上的其中一个erps端口，并关闭该环ERPS功能后，参照单环配置，同时可指定如下可选配置：

######  配置 holdoff-time 、 guard-time 、 wtr-time 等定时器

 R-APS VLAN模式下，可选配置。


配置指南 ERPS

 可根据实际应用需求，在R-APS VLAN模式下直接配置。

**检验方法**

 在各个节点上执行show erps命令，确认配置。

**相关命令**

######  配置 holdoff-time 、 guard-time 、 wtr-time 等定时器

```
【命令格式】 timer { holdoff-time interval 1 | guard-time interval 2 | wtr-time interval 3 }
【参数说明】 interval 1 ：Holdoff定时器的值，单位为 100 毫秒，缺省值为 0 ，范围是 0 - 100
interval 2 ：Guard定时器的值，单位为 10 毫秒，缺省值为 50 ，范围是 1 - 200
interval 3 ：WTR定时器的值，单位为分钟，缺省值为 2 ，范围是 1 - 12
【命令模式】 R-APS VLAN模式^
【使用指导】
 Holdoff timer：该定时器用于防止由于链路的间歇性故障，导致ERPS不断进行拓扑切换。配置了此定
时器之后，当检测到链路故障时，ERPS不立即执行拓扑切换，而是等定时器超时之后，如果确认链路
仍故障，才执行拓扑切换。
 Guard timer：该定时器用于防止设备接收到过时的R-APS消息。当设备检测到链路从故障中恢复时，
对外发送链路恢复的消息报文，并启动guard定时器。在guard定时器超时之前，除指示子环拓扑变化
的flush报文外，其它的报文都将被直接丢弃，不进行处理。
 WTR（Wait-to-restore）timer：此定时器只对RPL owner设备有效，对其它设备无效。该定时器主要用
于防止RPL owner对环网的状态产生误判。当RPL owner检测到故障恢复时，不立即执行拓扑切换，
而是等WTR定时器超时之后，如果确认以太环的确已从故障中恢复，才执行拓扑切换。如果在WTR定
时器超时之前又再次检测到环网故障，则取消WTR定时器，不再执行拓扑切换。
```

**配置举例**

```
【网络环境】
```

【配置方法】 (^)  环中已有ERPS的配置，由于物理拓扑变化，切换ERPS端口。
 shutdown环上的一条链路，并配置切换后端口的链路模式。


配置指南 ERPS

```
 进入R-APS VLAN模式，关闭指定环的ERPS功能。
 重新配置参于ERPS协议端口
 使能该环的ERPS功能。
 修改ERPS定时器
```

Node1 (^) # 进入特权模式
Ruijie# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.

# 进入接口模式，shutdown环上的一条链路，避免环路

Ruijie(config)# interface gigabitEthernet 0/ 1
Ruijie(config-if-gigabitEthernet 0/1)# shutdown
Ruijie(config-if-gigabitEthernet 0/1)# exit

# 配置以太环端口的链路模式。

Ruijie(config)# interface gigabitEthernet 0/ 3
Ruijie(config-if-gigabitEthernet 0/3)# switchport mode trunk
Ruijie(config-if-gigabitEthernet 0/3)# exit

# 进入ERPS配置模式。

Ruijie(config)# erps raps-vlan 4093

# 关闭环ERPS功能。

Ruijie(config-erps 4093)# no state enable
#删除之前的环配置。
Ruijie(config-erps 4093)# no ring-port

# 重新配置参于ERPS协议计算的端口，将gi 0/2改为gi 0/3。

Ruijie(config-erps 4093)# ring-port west gigabitEthernet 0/1 east gigabitEthernet 0/ 3

# 开启环ERPS功能。

Ruijie(config-erps 4093)# state enable
Node4 (^) # 进入特权模式
Ruijie# configure terminal

# 进入erps配置模式，直接修改定时器

Ruijie(config)# erps raps-vlan 4093
Ruijie(config-erps 4093)# timer wtr-time 1
【检验方法】 等待一分钟，ERPS环稳定恢复Idle后，在Node1和Node4节点上执行show erps命令，确认配置。


配置指南 ERPS

Node1 (^) Ruijie# show erps
ERPS Information
Global Status : Enabled

Link monitored by : Not Oam
--------------------------------------------

R-APS VLAN : 4093
Ring Status : Enabled
West Port : Gi 0/1 (Forwardin)
East Port : Gi 0/3 (Forwardin)
RPL Port : None
Protected VLANs : ALL
RPL Owner : Enabled
Holdoff Time : 0 milliseconds
Guard Time : 500 milliseconds
WTR Time : 2 minutes
Current Ring State : Idle
Associate R-APS VLAN :
Node4 (^) Ruijie# show erps
ERPS Information
Global Status : Enabled

Link monitored by : Not Oam
--------------------------------------------

R-APS VLAN : 4093
Ring Status : Enabled
West Port : Gi 0/1 (Forwardin)
East Port : Gi 0/2 (Blocking)
RPL Port : East Port
Protected VLANs : ALL
RPL Owner : Enabled
Holdoff Time : 0 milliseconds
Guard Time : 500 milliseconds


配置指南 ERPS

```
WTR Time : 1 minutes
Current Ring State : Idle
Associate R-APS VLAN :
```

**常见错误**

 配置修改后，未使能R-APS环或未将之前shutdown的端口no shutdown。

#### 14.5 监视与维护

**清除各类信息**

作用 命令

- -

**查看运行情况**

作用 命令
查看设备的ERPS配置及状态。 show erps [ global | raps_vlan vlan-id [ sub_ring ] ]


# 配置指南-IP 地址及应用

本分册介绍 IP 地址及应用配置指南相关内容，包括以下章节：

1. IP地址与服务
2. ARP
3. IPv6
4. DHCP
5. DHCPv6
6. DNS
7. FTP-Server
8. FTP Client
9. TFTP-Server
10. TUNNEL
11. 网络通信检测工具
12. TCP
13. 软件IPv4/v6快转


配置指南 IP地址与服务

### 1 IP 地址与服务

#### 1.1 概述

因特网协议（Internet Protocol，IP）使用逻辑虚拟的地址将数据包从源方发送到目的方，即IP地址。在网络层，路由设备使
用IP地址完成数据包转发。

### 以下仅针对IPv4地址进行介绍。^

**协议规范**

 RFC 1918 ：AddressAllocationforPrivateInternets

 RFC 1166 ：Internet Numbers

#### 1.2 典型应用

典型应用 场景描述
配置IP地址通信 两个网络使用同一个交换机接口进行通信

###### 1.2.1 配置 IP 地址通信

**应用场景**

交换机连接一个局域网，局域网分为两个网段：172.16.1.0/24和172.16.2.0/24。要求两个网段的计算机都可以通过交换机和
因特网通信，并且两个网段的计算机之间可以互相通信。

图 1 - 1 IP地址配置范例


配置指南 IP地址与服务

**功能部属**

 在vlan1口上配置两个ip地址，一个主ip地址，一个从ip地址。

 在172.16.1.0/24网段中的主机上配置网关为172.16.1.1，在172.16.2.0/24网段中的主机上配置网关为172.16.2.1。

#### 1.3 功能详解

**基本概念**

######  IP 地址

IP地址由 32 位二进制组成，为了书写和描述方便，一般用十进制表示。十进制表示时，分为四组，每组 8 位，范围从0~255，
组之间用“.”号隔开，比如“192.168.1.1”就是用十进制表示的IP地址。

IP地址顾名思义，自然是IP层协议的互连地址。 32 位的IP地址由两个部分组成： 1 ）网络部分； 2 ）本地地址部分。根据网
络部分的头几个比特位的值，目前使用中的IP地址可以划分成四大类。

A类地址，最高比特位为“ 0 ”，有 7 个比特位表示网络号， 24 个比特位表示本地地址。这样总共有 128 个A类网络。

图 1 - 2

B类地址，前两个最高比特位为“ 10 ”，有 14 个比特位表示网络号， 16 个比特位表示本地地址。这样总共有16,348个B类网
络。

图 1 - 3

C类地址，前三个最高比特位为“ 110 ”，有 21 个比特位表示网络号， 8 个比特位表示本地地址。这样总共有2,097,152个C
类网络。

图 1 - 4

D类地址，前四个最高比特位为“ 1110 ”，其余比特位为组播地址。

图 1 - 5


配置指南 IP地址与服务

### 前四个最高比特位为“^1111 ”的地址是不允许分配的，这些地址称为E类地址，属于保留地址。^

在建设网络过程中，进行IP地址规划时，一定要根据建设网络的性质进行IP地址分配。如果建设的网络需要与互联网连接，
则需要到相应的机构申请分配IP地址。中国地区可以向中国互联网信息中心（CNNIC）申请，负责IP地址分配的最终机构为
国际互联网名字与编号分配公司（ICANN, Internet Corporation for Assigned Names and Numbers）。如果建设的网络为内部
私有网络，就不需要申请IP地址，但是也不能随便分配，最好分配专门的私有网络地址。

下表为保留与可用的地址列表：

类别 地址空间 状态

A类网络

0.0.0.0~0.255.255.255 (^) 保留
1.0.0.0~126. 255. 255. (^255) 可用
127.0.0.0~127.255.255.255 (^) 保留
B类网络
128.0.0.0~191.254. 255. 255 可用
191.255.0.0~191.255.255.255 保留
C类网络
192.0.0.0~192.0.0.255 保留
192.0.1.0~223.255.254. 255 可用
223.255.255.0~223.255.255. 255 保留
D类网络 224.0.0.0~239.255.255.255 组播地址
E类网络
240.0.0.0~255.255.255.254 (^) 保留
255.255.255.255 (^) 广播地址
其中专门有三个地址块提供给私有网络，这些地址是不会在互联网中使用的，如果分配了这些地址的网络需要连接互联网，则
需要将这些IP地址转换成有效的互联网地址。下表为私有网络地址空间，私有网络地址由RFC 1918文档定义：
类别 地址空间 状态
A类网络 10.0.0.0~10.255.255.255 1 个A类网络
B类网络 172.16.0.0~172.31.255.255 16 个B类网络
C类网络 192.168.0.0~192.168.255.255 256 个C类网络
关于IP地址、TCP/UDP端口及其它编码的分配情况，请参考RFC 1166文档。

######  子网掩码

网络掩码也是一个 32 比特的数值，标识着该IP地址的哪几个比特为网络部分。网络掩码中，值为“1”的比特对应的IP地址比
特位就是网络部分，值为“0”的比特对应的IP地址比特位就是主机地址部分。如A类网络对应的网络掩码为“255.0.0.0”。您可
以利用网络掩码对一个网络进行子网划分，子网划分就是将主机地址部分的一些比特位也作为网络部分，缩小主机容量，增加
网络的数量，这时的网络掩码就称为子网掩码。

######  广播报文


配置指南 IP地址与服务

广播报文是指目标地址为某个物理网络上所有主机的数据包。锐捷产品支持两种类型广播报文： 1 ）定向广播，是指数据包接
收者为一个指定网络的所有主机，目标地址的主机部分全为“ 1 ”； 2 ）淹没广播，是指数据包接收者为所有网络的主机，目标
地址 32 比特位全为“ 1 ”。

######  ICMP 报文

ICMP是（Internet Control Message Protocol）Internet控制报文协议。它是TCP/IP协议族的一个子协议，用于在IP主机、
网络设备之间传递控制消息，主要用于网络出现异常的时候通知相应设备。

######  TTL

TTL（Time-To-Live），生存时间。指定数据包被路由器丢弃之前允许通过的网段数量。它是IP协议报文中的一个值，它告诉
网络，数据包在网络中的时间是否太长而应被丢弃。

**功能特性**

功能特性 作用
IP地址 用于配置接口IP地址，该接口才允许运行IP协议。
广播报文处理 设置IP广播地址，转发处理定向广播报文。
发送ICMP报文 控制ICMP协议报文的收发。
控制ICMP差错报文
的发送速率

```
防止拒绝服务攻击。
```

IP MTU 用于配置接口IP报文的最大传输单元。
IP TTL 用于配置单播报文和广播报文的TTL。
IP源路由 用于对接收报文的源路由进行检查。
IP地址池 用于ppp协商为对端分配ip地址

###### 1.3.1 IP 地址

接口获取IP地址有以下方式：

(1) 手工配置IP地址。

(2) 利用DHCP协议获取IP地址。

(3) 通过PPP协商获得IP地址。

这几种方式是互斥的，配置新的获取IP地址方式时会覆盖通过原有方式获取的IP地址。

### 利用DHCP协议获取IP地址请参见“DHCP”章节，以下仅介绍其他三种获取IP地址的方式。^

######  配置接口 IP 地址

一个设备只有配置了IP地址，才可以接收和发送IP数据包，接口配置了IP地址，说明该接口允许运行IP协议。

######  接口配置多个 IP 地址


配置指南 IP地址与服务

锐捷产品可以支持一个接口配置多个IP地址，其中一个为主IP地址，其余全部为次IP地址。次IP地址的配置理论上没有数
目限制，但是次IP地址与主IP以及次IP地址之间必须属于不同网络。在网络建设中，会经常使用到次IP地址，通常在以下
情况下应该考虑使用次IP地址：

 一个网络没有足够多的主机地址。例如，现在一般局域网需要一个C类网络，可分配 254 台主机。但是当局域网主机超
过 254 台时，一个C类网络将不够分配，有必要分配另一个C类网络地址。这样设备就需要连接两个网络，所以就需要
配置多个IP地址。

 许多旧的网络是基于第二层的桥接网络，没有进行子网的划分。次IP地址的使用可以使该网络很容易升级到基于IP层的
路由网络。对于每个子网，设备都配置一个IP地址。

 一个网络的两个子网被另外一个网络隔离开，可以创建一个被隔离网络的子网，通过配置次IP地址的方式，将隔离的子
网连接起来。一个子网不能在设备的两个或两个以上接口出现。

######  配置通过 PPP 协商获取 IP 地址

### 本命令只在点对点接口上支持。^

通过此配置，点对点接口可以通过PPP协商接受对端为自己分配的IP地址。

**相关配置**

######  配置接口一个或多个 IP 地址

 缺省情况接口没有配置IP地址。

 通过ip address命令配置接口IP地址。

 配置后根据冲突检测即可使用该IP地址进行通信。

 通过ip address ip-address masksecondary可以配置多个次IP地址。

###### 1.3.2 广播报文处理

**工作原理**

广播分两种，全广播，即IP地址为255.255.255.255，由于会被路由器禁止传输，所以也叫本地网络广播。另一种是所有的主
机位都为 1 的广播，例如：192.168.1.255/24，这种广播，通过配置是可以被转发的。

如果IP网络设备转发淹没广播（一般指目标IP地址为全“ 1 ”的广播报文），可能会引起网络的超负载，严重影响网络的运行，
这种情况称为广播风暴。设备提供了一些办法能够将广播风暴限制在本地网络，阻止其继续扩张。但对于桥和交换机等基于二
层网络设备，将转发和传播广播风暴。

解决广播风暴最好的办法就是给每个网络指定一个广播地址，这就是定向广播，这要求使用广播报文的IP协议尽可能应用定
向广播而不是淹没广播进行数据传播。

关于广播问题的详细描述，请参见RFC 919和RFC 922。


配置指南 IP地址与服务

IP定向广播报文是指目标地址为某个IP子网广播地址的IP报文，如目标地址为172.16.16.255的报文就称为定向广播报文。
但是产生该报文的节点又不是目标子网的成员。

没有与目标子网直连的设备接收到IP定向广播报文，跟转发单播报文一样处理定向广播报文。当定向广播报文到达直连该子
网的设备后，设备将把定向广播报文转换为淹没广播报文（一般指目标IP地址为全“ 1 ”的广播报文），然后以链路层广播方
式发送给目标子网上的所有主机。

**相关配置**

######  配置 IP 广播地址

 缺省情况下接口IP广播地址为255.255.255.255。

 如果需要定义其它地址的广播报文，可以在接口下配置ip broadcast-address命令。

######  允许转发定向广播

 缺省情况接口不允许转发定向广播。

 用户可以在指定的接口上，通过ip directed-broadcast命令配置接口允许转发定向广播，这样该接口就可以转发到直连
网络的定向广播了。该命令只影响定向广播报文在目标子网的传输，而不影响其它定向广播报文的正常转发。

 在接口上，用户还可以通过定义访问控制列表来控制转发某些定向广播。当定义了访问列表时，只有符合访问列表中定义
的定向广播才会被转发。

###### 1.3.3 发送 ICMP 报文

**工作原理**

######  ICMP 协议不可达消息

当设备接收到目标为自己的非广播报文，但是该数据包中采用了设备不能处理的IP协议，设备就向源地址发送ICMP协议不
可达消息。另外，如果设备由于不知道路由而不能转发数据包时，也会发送ICMP主机不可达消息。

######  ICMP 重定向消息

路由有时会不够优化，使得设备从一个接口接收到的数据包，还要从该接口发送出去。如果设备将数据包从接收接口重新发送
出去，设备就会给数据源发送一个ICMP重定向消息，告诉数据源到该目标地址的网关为同一子网上的另外一台设备。这样数
据源就会将后续的数据包按照最佳的路径进行发送。

######  ICMP 掩码应答消息

网络设备有时需要知道互联网上某个子网的子网掩码，为了获取该信息，网络设备可以发送ICMP掩码请求消息，接收到ICMP
掩码请求消息的网络设备就会发送掩码应答消息。

######  TTL 超时消息

设备转发IP报文时，如果报文的TTL超时了，设备需要向源端回应一个TTL超时的差错报文。


配置指南 IP地址与服务

为了防止被其他设备traceroute到，进而遭受到攻击，可以关闭TTL超时差错报文的发送功能。关闭该功能后，设备收到TTL
超时的报文，将不再回应TTL超时差错报文。

######  时间戳查询

RFC 792 要求系统收到ICMP时间戳查询时，需要返回系统的当前时间。

为了防止攻击者通过该协议获取到系统的时间，从而攻击到一些基于时间认证的协议，可以关闭时间戳查询功能。关闭该功能
后，设备收到时间戳查询报文直接丢弃，不再应答。

**相关配置**

######  启用 ICMP 协议不可达消息

 缺省情况接口启用ICMP协议不可达消息功能。

 可通过[no] ip unreachables命令关闭或启用该功能。

######  启用 ICMP 重定向消息

 缺省情况接口启用ICMP协议重定向消息功能。

 可通过[no]ip redirects命令关闭或启用该功能。

######  启用 ICMP 掩码应答消息

 缺省情况接口启用ICMP掩码应答消息功能。

 可通过[no]ip mask-reply命令关闭或启用该功能。

######  启用 TTL 超时消息

 缺省情况启用TTL超时消息功能。

 可通过全局模式下的[no] ip ttl-expires enable命令关闭或启用该功能。

######  启用时间戳查询功能

 缺省情况启用ICMP时间戳查询功能。

 可通过全局模式下的[no] ip icmp timestamp命令关闭或启用该功能。

###### 1.3.4 控制 ICMP 差错报文的发送速率

**工作原理**

为了防止拒绝服务攻击，对ICMP差错报文的发送速率进行限制，采用令牌桶算法。


配置指南 IP地址与服务

如果IP报文需要分片，但是IP首部的不可分片位被设置了，设备会向源IP地址发送编号为 4 的ICMP目的不可达报文，这
种ICMP差错报文的主要用途是路径MTU发现。为了防止其它ICMP差错报文太多导致发不出编号为 4 的ICMP目的不可达
报文，从而导致路径MTU发现功能失效，对编号为 4 的ICMP目的不可达报文和其它ICMP差错报文分别限速。

**相关配置**

######  配置 IP 首部不可分片位触发的 ICMP 目的不可达报文的发送速率

 缺省速率是 100 毫秒 10 个。

 可通过ip icmp error-interval DF配置发送速率。

######  配置其它 ICMP 差错报文的发送速率

 缺省速率是 100 毫秒 10 个。

 可通过ip icmp error-interval配置发送速率。

###### 1.3.5 IP MTU

**工作原理**

如果一个IP报文超过IP MTU的大小，RGOS软件就会对报文进行拆分。所有在同一物理网段上的设备，其互联接口的IP MTU
一定要一致。锐捷产品允许调整接口的链路MTU值，而且接口的链路MTU的变化会引起接口的IP MTU的变化，接口的IP MTU
会自动与接口的链路MTU保持一致。但是反之不行，如果调整了接口的IP MTU值，接口的链路MTU不会跟着改变。

**相关配置**

######  设置 IP MTU

 缺省情况接口IP MTU为 1500 。

 可通过ip mtu设置IP包最大传输单元(MTU）。

###### 1.3.6 IP TTL

**工作原理**

IP数据包从源地址向目的地址经过路由器间传播，设置一个TTL数值，每过一个路由器TTL值就减一，当减到零的时候，路
由器就把这个包丢掉，这样可以防止无用的包在网络上无限传播下去，浪费网络带宽。

**相关配置**

######  设置 IP TTL


配置指南 IP地址与服务

 缺省情况接口IP TTL为 64 。

 可通过ip ttl设置接口的IP TTL值。

###### 1.3.7 IP 源路由

**工作原理**

锐捷产品支持IP源路由。当设备接收到IP数据包时，会对IP报头的严格源路由、宽松源路由和记录路由等选项进行检查，这
些选项在RFC 791中有详细描述。如果检测到该数据包启用了其中一个选项，就会执行响应的动作；如果检测到无效的选项，
就会给数据源发送一个ICMP参数问题消息，然后丢弃该数据包。

开启IP源路由，在IP数据报选项中增加源路由选项，可用于测试某特定网络的吞吐率，也可以是数据报绕开出错的网络。然
而，可能会导致诸如源地址欺骗(Source Address Spoofing)、IP欺骗(IP Spoofing)等的网络攻击。

**相关配置**

######  配置 IP 源路由

 缺省情况开启IP源路由功能。

 可通过ip source-route开启或关闭该功能。

#### 1.4 配置详解

配置项 配置建议&相关命令

### 配置接口IP地址

```
必须配置。用于配置ip地址，允许接口运行IP协议。
ip address 手工配置接口IP地址
```

配置广播报文处理方式

### 可选配置。用于设置IP广播地址，允许转发定向广播报文。^

```
ip broadcast-address 配置IP广播地址
ip directed-broadcast 允许转发定向广播
```

配置发送ICMP报文

### 可选配置。用于控制ICMP协议报文的收发。^

```
ip unreachables 启用ICMP协议不可达和主机不可达消息
ip redirects 启用ICMP重定向消息
```

ip mask-reply (^) 启用掩码应答消息
ip ttl-expires enable 启用发送TTL超时差错报文功能
ip icmp timestamp 启用时间戳查询功能

### 配置ICMP差错报文的发送速 可选配置。


配置指南 IP地址与服务

率
ip icmp error-interval DF
配置IP首部不可分片位触发的ICMP目的不
可达报文的发送速率
ip icmp error-interval 配置其它ICMP差错报文和ICMP重定向报文
的发送速率

### 设置IP MTU 可选配置。用于配置接口IP报文的最大传输单元。^

```
ip mtu 设置MTU值
```

### 设置IP TTL 可选配置。用于配置单播报文和广播报文的TTL。^

```
ip ttl 设置TTL值
```

### 配置IP源路由 可选配置。用于配置对接收报文的源路由进行检查。^

```
ip source-route 启用IP源路由
```

###### 1.4.1 配置接口 IP 地址

**配置效果**

通过配置接口IP地址实现IP网络通信。

**注意事项**

 -

**配置方法**

######  手工配置接口 IP 地址

 必须配置。

 在三层接口模式下配置。

######  配置通过 PPP 协商获取接口 IP 地址

 可选配置。

 如果点对点接口上没有配置IP地址，且需要通过PPP协商获取IP地址时配置。

 在三层接口模式下配置。

**检验方法**

通过show ip interface可以看到配置的地址生效


配置指南 IP地址与服务

**相关命令**

######  手工 配置接口 IP 地址

```
【命令格式】 ip address ip-address network-mask [ secondary ]
【参数说明】 ip-address： 32 个比特位IP地址， 8 位一组，以十进制方式表示，组之间用点隔开。
network-mask： 32 个比特位网络掩码，“ 1 ”表示掩码位，“ 0 ”表示主机位。每 8 位一组，以十进制方式表示，
组之间用点隔开。
secondary：表示配置的次IP地址。
【命令模式】 接口模式
【使用指导】 -^
```

**配置举例**

######  给接口配置 IP 地址

【配置方法】 在接口GigabitEthernet 0/0配置ip地址192.168.23.110 255.255.255.0
Ruijie#configure terminal
Ruijie(config)#interface gigabitEthernet 0/0
Ruijie(config-if-GigabitEthernet 0/0)# no switchport
Ruijie(config-if-GigabitEthernet 0/0)#ip address 192.168.23.1 10 255.255.255.0
【检验方法】 使用show ip interface可以看到接口GigabitEthernet 0/0添加地址成功
Ruijie# show ip interface gigabitEthernet 0/ 0
GigabitEthernet 0/0
IP interface state is: UP
IP interface type is: BROADCAST
IP interface MTU is: 1500
IP address is:
192.168.23.1 10 /24 (primary)

###### 1.4.2 配置广播报文处理方式

**配置效果**

配置接口广播地址为0.0.0.0，并允许转发定向广播报文。

**注意事项**

-


配置指南 IP地址与服务

**配置方法**

######  配置 IP 广播地址

 可选配置，有些老的主机可能只认0.0.0.0的广播地址，此时需要配置接口的广播地址为0.0.0.0。

 在三层接口模式下配置。

######  允许转发定向广播

 可选配置，向处在一个广播域的全部主机发送广播，但是发送者并不处在这个广播域内，此时需要配置允许转发定向广播。

 在三层接口模式下配置。

**检验方法**

通过show running-config interface可以看到配置生效

**相关命令**

######  配置 IP 广播地址

```
【命令格式】 ip broadcast-address ip-address^
【参数说明】 ip-address：IP网络的广播地址。
【命令模式】 接口模式
【使用指导】 目前IP广播报文的目标地址一般为全“ 1 ”，表示为255.255.255.255。RGOS软件可以通过定义产生其它IP
地址的广播报文，而且可以同时接收全“ 1 ”以及自己定义的广播包。
```

######  允许转发定向广播

```
【命令格式】 ip directed-broadcast [ access-list-number ]
【参数说明】 access-list-number：访问列表号，范围从 1 - 199 ， 1300 - 2699 。如果定义了访问列表号，只有匹配该访问列
表的IP定向广播报文才转换。
【命令模式】 接口模式
【使用指导】 如果在接口上配置了no ip directed-broadcast，RGOS将丢弃接收到的直连网络的定向广播报文。
```

**配置举例**

【配置方法】
在设备端口gigabitEthernet 0/1配置IP广播报文的目标地址为0.0.0.0，启用定向广播的转发。
Ruijie#configure terminal
Ruijie(config)#interface gigabitEthernet 0/1
Ruijie(config-if-GigabitEthernet 0/ 1 )# no switchport
Ruijie(config-if-GigabitEthernet 0/1)#ip broadcast-address 0.0.0.0
Ruijie(config-if-GigabitEthernet 0/1)#ip directed-broadcast


配置指南 IP地址与服务

【检验方法】 使用show ip interface可以看到接口GigabitEthernet 0/ 1 配置成功
Ruijie#show running-config interface gigabitEthernet 0/1
ip directed-broadcast
ip broadcast-address 0.0.0.0

###### 1.4.3 配置发送 ICMP 报文

**配置效果**

启用接口ICMP协议不可达消息，ICMP重定向消息以及掩码应答消息。

**注意事项**

-

**配置方法**

######  启用 ICMP 协议不可达消息

 缺省开启ICMP协议不可达消息。

 可选配置，通过no ip unreachables禁止该功能。

 在三层接口模式下配置。

######  启用 ICMP 重定向消息

 缺省开启ICMP重定向消息。

 可选配置，通过no ip redirects禁止该功能。

 在三层接口模式下配置。

######  启用 ICMP 掩码应答消息

 缺省开启ICMP掩码应答消息。

 可选配置，通过no ip mask-reply禁止该功能。

 在三层接口模式下配置。

######  启用 TTL 超时消息

 缺省开启TTL超时消息。

 可选配置，通过no ip ttl-expires enable禁止该功能。

 在全局模式下配置。

######  启用时间戳查询


配置指南 IP地址与服务

 缺省开启时间戳查询功能。

 可选配置，通过no ip icmp timestamp禁止该功能。

 在全局模式下配置。

**检验方法**

通过show ip interface可以看到配置生效。

通过show running-config可以看到TTL超时消息是否关闭。

通过show running-config可以看到时间戳查询功能是否关闭。

**相关命令**

######  启用 ICMP 协议不可达消息

```
【命令格式】 ip unreachables
【参数说明】 -
【命令模式】 接口模式
【使用指导】 -
```

######  启用 ICMP 重定向消息

```
【命令格式】 ip redirects
【参数说明】 -^
【命令模式】 接口模式
【使用指导】 -^
```

######  启用 ICMP 掩码应答消息

```
【命令格式】 ip mask-reply^
【参数说明】 -
【命令模式】 接口模式
【使用指导】 -
```

######  关闭 TTL 超时消息

```
【命令格式】 no ip ttl-expires enable
【参数说明】 -^
【命令模式】 全局模式
【使用指导】 -
```

######  关闭时间戳查询

```
【命令格式】 no ip icmp timestamp^
【参数说明】 -
```

配置指南 IP地址与服务

```
【命令模式】 全局模式
【使用指导】 -^
```

**配置举例**

【配置方法】 在设备端口gigabitEthernet 0/1启用ICMP协议不可达消息，ICMP重定向消息以及ICMP掩码应答消息功能。
Ruijie#configure terminal
Ruijie(config)# no ip ttl-expires enable
Ruijie(config)# no ip icmp timestamp
Ruijie(config)#interface gigabitEthernet 0/1
Ruijie(config-if-GigabitEthernet 0/ 1 )# no switchport
Ruijie(config-if-GigabitEthernet 0/1)# ip unreachables
Ruijie(config-if-GigabitEthernet 0/1)# ip redirects
Ruijie(config-if-GigabitEthernet 0/1)# ip mask-reply
【检验方法】 使用show ip interface可以看到接口GigabitEthernet 0/ 1 配置成功
Ruijie#show running-config | include ip ttl-expires enable
no ip ttl-expires enable
Ruijie#show running-config | include ip icmp timestamp
no ip icmp timestamp
Ruijie#show ip interface gigabitEthernet 0/ 1
GigabitEthernet 0/ 1
ICMP mask reply is: ON
Send ICMP redirect is: ON
Send ICMP unreachabled is: ON

###### 1.4.4 配置 ICMP 报文差错报文的发送速率

**配置效果**

配置ICMP差错报文的发送速率。

**注意事项**

-

**配置方法**

######  配置 IP 首部不可分片位触发的 ICMP 目的不可达报文的发送速率


配置指南 IP地址与服务

 可选配置。

 在全局模式下配置。

######  配置其它 ICMP 差错报文的发送速率

 可选配置。

 在全局模式下配置。

**检验方法**

执行show running-config可以看到配置生效。

**相关命令**

######  配置 IP 首部不可分片位触发的 ICMP 目的不可达报文的发送速率

```
【命令格式】 ip icmp error-interval DF milliseconds [bucket-size]^
【参数说明】 milliseconds：令牌桶的刷新周期，取值范围0~2147483647，缺省值为 100 ，单位为毫秒。取值为 0 时，表
示不限制ICMP 差错报文的发送速率。
bucket-size：令牌桶中容纳的令牌数，取值范围1~200，缺省值为 10 。
【命令模式】 全局模式
【使用指导】 为了防止拒绝服务攻击，对ICMP差错报文的发送速率进行限制，采用令牌桶算法。
如果IP报文需要分片，但是IP首部的不可分片位被设置了，设备会向源IP地址发送编号为 4 的ICMP目的
不可达报文，这种ICMP差错报文的主要用途是路径MTU发现。为了防止其它ICMP差错报文太多导致发不
出编号为 4 的ICMP目的不可达报文，从而导致路径MTU发现功能失效，对编号为 4 的ICMP目的不可达报
文和其它ICMP差错报文分别限速。
因为定时器的精度是 10 毫秒，建议用户把令牌桶的刷新周期配置成 10 毫秒的整数倍。如果令牌桶的刷新周
期大于,0小于 10 ，实际生效的刷新周期是 10 毫秒，例如配置 5 毫秒 1 个，实际效果是 10 毫秒 2 个；如果令
牌桶的刷新周期不是 10 毫秒的整数倍，实际生效的刷新周期自动换算成 10 毫秒的整数倍，例如配置 15 毫秒
3 个，实际效果是 10 毫秒 2 个。
```

######  配置其它 ICMP 差错报文的发送速率

```
【命令格式】 ip icmp error-interval milliseconds [bucket-size]
【参数说明】 milliseconds：令牌桶的刷新周期，取值范围0~2147483647，缺省值为 100 ，单位为毫秒。取值为 0 时，表
示不限制ICMP 差错报文的发送速率。
bucket-size：令牌桶中容纳的令牌数，取值范围1~200，缺省值为 10 。
【命令模式】 全局模式
【使用指导】 为了防止拒绝服务攻击，对ICMP差错报文的发送速率进行限制，采用令牌桶算法。
因为定时器的精度是 10 毫秒，建议用户把令牌桶的刷新周期配置成 10 毫秒的整数倍。如果令牌桶的刷新周
期大于,0小于 10 ，实际生效的刷新周期是 10 毫秒，例如配置 5 毫秒 1 个，实际效果是 10 毫秒 2 个；如果令
牌桶的刷新周期不是 10 毫秒的整数倍，实际生效的刷新周期自动换算成 10 毫秒的整数倍，例如配置 15 毫秒
3 个，实际效果是 10 毫秒 2 个。
```

配置指南 IP地址与服务

**配置举例**

【配置方法】 配置IP首部不可分片位触发的ICMP目的不可达报文的发送速率为 1 秒 100 个，配置其它ICMP差错报文的
发送速率为 1 秒 10 个。
Ruijie(config)# ip icmp error-interval DF 1000 100
Ruijie(config)# ip icmp error-interval 1000 10
【检验方法】 执行show running-config可以看到配置生效
Ruijie#show running-config | include ip icmp error-interval
ip icmp error-interval 1000 10
ip icmp error-interval DF 1000 100

###### 1.4.5 配置 IP MTU

**配置效果**

调整IP包最大传输单元。

**注意事项**

-

**配置方法**

 可选配置，所有在同一物理网段上的设备，当互联接口的IP MTU不一致时需要配置为一致。

 在三层接口模式下配置。

**检验方法**

通过show ip interface可以看到配置生效

**相关命令**

######  配置 IP MTU

```
【命令格式】 ip mtubytes
【参数说明】 bytes：IP包最大传输单元，以字节为单位，范围68~1500。
【命令模式】 接口模式
【使用指导】 -^
```

配置指南 IP地址与服务

**配置举例**

【配置方法】 将gigabitEthernet 0/1接口的IP MTU值设为 512 字节
Ruijie#configure terminal
Ruijie(config)#interface gigabitEthernet 0/1
Ruijie(config-if-GigabitEthernet 0/ 1 )# no switchport
Ruijie(config-if-GigabitEthernet 0/1)#ip mtu 512
【检验方法】 使用show ip interface可以看到接口GigabitEthernet 0/ 1 配置成功
Ruijie# show ip interface gigabitEthernet 0/1
IP interface MTU is: 512

###### 1.4.6 配置 IP TTL

**配置效果**

###### 修改接口的IP TTL值。

**注意事项**

-

**配置方法**

 可选配置。

 在三层接口模式下配置。

**检验方法**

通过show run-config可以看到配置生效

**相关命令**

######  配置 IP TTL

```
【命令格式】 ip ttl value
【参数说明】 value：TTL值，取值范围是0~255。
【命令模式】 全局模式
【使用指导】 -^
```

配置指南 IP地址与服务

**配置举例**

【配置方法】  配置本机发送的单播报文的缺省TTL值为 100 。
Ruijie#configure terminal
Ruijie(config)#ip ttl 100
【检验方法】 通过show run-config可以看到配置生效
Ruijie#show running-config
ip ttl 100

###### 1.4.7 配置 IP 源路由

**配置效果**

###### 开启或关闭IP源路由信息的处理功能。

**注意事项**

-

**配置方法**

 缺省情况下开启IP源路由功能。

 可选配置，通过no ip source-route可关闭IP源路由功能。

**检验方法**

通过show run-config可以看到配置生效。

**相关命令**

######  配置 IP 源路由

```
【命令格式】 ip source-route^
【参数说明】 -
【命令模式】 全局模式
【使用指导】 -
```

**配置举例**


配置指南 IP地址与服务

【配置方法】  关闭了IP源路由信息的处理功能。
Ruijie#configure terminal
Ruijie(config)#no ip source-route
【检验方法】 通过show run-config可以看到配置生效
Ruijie#show running-config
no ip source-route

#### 1.5 监视与维护

**清除各类信息**

-

**查看运行情况**

作用 命令
显示接口IP信息 show ip interface [interface-typeinterface-number | brief]
显示IP报文统计值 show ip packet statistics [total | interface-name]
显示协议栈IP报文收发统计信息 show ip packet queue

**查看调试信息**

-


配置指南 ARP

### 2 ARP

#### 2.1 概述

在局域网中，每个IP网络设备都有两个地址： 1 ）本地地址，由于它包含在数据链路层的帧头中，更准确地说应该是数据链路
层地址，但实际上对本地地址进行处理的是数据链路层中的MAC子层，因此习惯上称为MAC地址，MAC地址在局域网上代
表着IP网络设备； 2 ）网络地址，在互联网上代表着IP网络设备，同时它也说明了该设备所属的网络。

局域网上两台IP设备之间需要通信，必须要知道对方的 48 比特的MAC地址。根据IP地址来获知MAC地址的过程称为地址
解析。地址解析的方式有两类： 1 ）地址解析协议（ARP）； 2 ）代理地址解析协议（Proxy ARP）。关于ARP 、Proxy ARP，
分别在RFC 826，RFC 1027文档中描述。

ARP(Address Resolution Protocol，地址解析协议)是用来绑定MAC地址和IP地址的，以IP地址作为输入，ARP能够知道其
关联的MAC地址。一旦知道了MAC地址，IP地址与MAC地址对应关系就会保存在设备的ARP缓存中。有了MAC地址，
IP设备就可以封装链路层的帧，然后将数据帧发送到局域网上去。缺省配置下，以太网上IP和ARP的封装为Ethernet II类型。

**协议规范**

 RFC826：An Ethernet Address Resolution Protocol

 RFC1027：Using ARP to implement transparent subnet gateways

#### 2.2 典型应用

典型应用 场景描述
在局域网内提供地址解析协议服务 在同一网段中，主机学习其他设备的MAC地址，需要用到地址解析协议。
使用代理ARP实现透明的子网网关 通过代理地址解析服务，允许主机在不知道另一个网络是否存在的情况下和另一网络内
的主机直接通讯。

###### 2.2.1 在局域网内提供地址解析协议服务

**应用场景**

###### 在所有IPv4局域网内，都需要用到ARP协议。

 主机需要通过ARP协议来学习其他设备的MAC地址，只有学到MAC地址后，主机才可以和其他设备通信。

图 2 - 1


配置指南 ARP

【注释】 A为路由器
B为交换机，作为用户主机网段的网关。
C、D、E为用户主机

**功能部属**

 在局域网内运行ARP协议，实现IP地址和MAC地址的映射。

###### 2.2.2 使用代理 ARP 实现透明的子网网关

**应用场景**

###### 在不同的IPv4局域网内，实现透明的子网网关。

 通过在设备上配置代理ARP的功能，实现不同网段内主机的直接通讯。

图 2 - 2

【注释】 A为路由器，连接两个局域网
B、C为用户主机，不配置默认网关，在不同的子网

**功能部属**

 在子网网关上运行代理ARP功能，可以帮助没有路由信息的主机获得其它子网IP地址的MAC地址。


配置指南 ARP

#### 2.3 功能详解

**功能特性**

功能特性 作用
静态ARP 用户手工指定IP地址和MAC地址的映射，防止设备学到错误的ARP表项而影响网络。
ARP属性设置 用户指定ARP表项的超时时间、ARP请求重传次数和间隔、未解析ARP表项数上限。
可信任ARP 防止ARP欺骗。
免费ARP 检测IP地址冲突，以及让外围设备更新本机的ARP。
代理ARP 代理应答请求其他设备的ARP请求。
本地代理ARP 代理应答一台设备请求子网内的其他设备的ARP请求
ARP可信检测 通过NDU（邻居不可达探测），保证学习的ARP表项正确。
ARP防IP报文攻击 通过设置触发ARP设丢弃表项的IP报文个数，触发设置丢弃表项到硬件，来防止未知名单播报文大量
送CPU对CPU造成冲击。
抑制往认证VLAN发
送ARP请求

```
通过设置抑制往认证vlan发送广播arp请求报文，可以减少网络中arp广播报文的数量，改善网络环
境
```

###### 2.3.1 静态 ARP

静态ARP包括手工配置的静态ARP和认证下发的静态ARP。手工配置的静态ARP优先级大于认证下发的静态ARP。静态
ARP能够防止设备学到错误的ARP表项而影响网络。

**工作原理**

静态ARP，设备不会再去主动更新ARP表项，并且永久存在。

设备转发三层报文时，以太头部的目的MAC地址将采用静态配置的MAC地址来封装。

**相关配置**

######  配置静态 ARP

手工配置的静态ARP，在全局模式下，使用arp [vrf name] ip-address mac-address type命令配置静态ARP表项。缺省情况
下用户没有配置任何静态ARP表项。用户可以将静态ARP表项绑定到不同的VRF下，也可以绑定在全局VRF下。ARP封
装只支持Ethernet II类型，用arpa表示。

###### 2.3.2 ARP 属性设置

用户指定ARP表项的超时时间、ARP请求重传次数和间隔、未解析ARP表项数上限、接口ARP学习数量限制、单板ARP
学习数量限制。


配置指南 ARP

**工作原理**

######  ARP 超时设置

ARP超时设置只对动态学习到的IP地址和MAC地址映射起作用。当一个ARP表项超时后，设备会发送单播ARP请求报文
探测对方是否在线，假如能收到对方的ARP应答，则说明对方仍在线，该ARP表项不会删除，否则会删除该ARP表项。

超时时间设置得越短，ARP缓冲中保存的映射表就越真实，但是ARP消耗网络带宽也越多。

######  ARP 请求重传时间间隔和次数

IP地址解析成MAC地址时连续发送ARP请求的时间间隔和次数。时间间隔越短，解析速率更快。次数越多，解析成功率更

###### 大，但是ARP消耗网络带宽也越多。

######  未解析 ARP 表项的数量限制

在局域网中可能存在对网关的攻击，扫描网段，使网关生成大量未解析的ARP表项，从而使网关无法正常学习主机的MAC地
址。为了防止这种攻击，用户可以配置未解析ARP表项的数量限制。

######  接口 ARP 学习数量限制

改成通过配置指定接口的用户ARP表项个数，灵活控制ARP表项资源的按需分配，防止表项资源浪费。

**相关配置**

######  ARP 超时设置

在接口模式下，使用命令arp timeout seconds配置ARP的超时时间。默认情况下超时时间为 3600 秒，用户可以根据实际情

###### 况重新调整。

######  ARP 请求重传时间间隔和次数

 在全局模式下，使用命令arp retry interval seconds配置ARP的重传时间间隔。默认情况下超时时间为 1 秒，用户可
以根据实际情况重新调整。

######  在全局模式下，使用命令arp retry times number配置ARP的重传次数。默认情况下可以连续发送 5 次，用户可以根据

###### 实际情况重新调整。

######  未解析 ARP 表项的数量限制

在全局模式下，使用命令arp unresolve number配置ARP的未解析表项数。默认为arp容量的最大值，用户可以根据实际情
况重新调整。

######  接口 ARP 学习数量限制

在接口模式下，使用命令arp cache interface-limit limit配置接口ARP的学习数量限制。默认不限制接口上ARP学习的数量，
用户可以根据实际情况重新调整。此数量限制包含静态ARP。


配置指南 ARP

###### 2.3.3 可信任 ARP

**工作原理**

可信任ARP作为一类特殊ARP，添加在交换机端的ARP表中，用于防止ARP欺骗。可信任ARP同时具有静态ARP和动态
ARP两者的特征，其优先级高于动态ARP表项、并且低于静态ARP表项。可信任ARP具有类似于动态ARP的老化机制，
在ARP老化时主动发送ARP请求报文探测主机是否存在，如果主机有应答则代表主机还是活动的，那么就更新ARP的老化
时间，否则删除ARP表项。可信任ARP具有静态ARP的相关特征，即不会通过学习ARP报文动态更新ARP表项的MAC、
接口等相关字段。

可信任ARP是GSN客户端用户认证上线时，认证服务端通过接入交换机获取用户真实的IP-MAC关联信息，并根据用户的网
关信息，在网关交换机上添加的。该过程对于网络管理员来说是透明的，不会对网络管理员的原有网络管理产生任何影响。

综上所述，因为可信任ARP来源真实有效，且不会被ARP报文动态更新，所以可以有效的防止针对网关的ARP欺骗。

**相关配置**

######  配置可信任 ARP 功能

 全局模式下，使用命令service trustedarp打开可信任arp功能，缺省情况下该功能是关闭的。

 全局模式下，使用命令arp trusted user-vlan vid1 translated-vlan vid2实现VLAN转换，缺省情况下没有任何VLAN
转换。如果服务器下发的VLAN和可信任ARP表项生效的VLAN不同，则用户需要配置VLAN转换。

 全局模式下，使用命令arp trusted aging允许可信任ARP老化。缺省情况下可信任ARP表项不允许老化。

 全局模式下，使用命令arp trusted number设置可信任ARP表项的容量。缺省情况下为总容量的一半，用户可以根据
实际情况更改容量。

###### 2.3.4 免费 ARP

**工作原理**

免费ARP报文是一种特殊的ARP报文，该报文的发送端IP地址和目标IP地址都是本机IP地址。免费ARP的主要用途有：

1. IP地址冲突检测。当设备收到免费ARP报文后，如果发现报文中的IP地址和自己的IP地址相同，向发送免费ARP报
   文的设备返回一个ARP应答，告诉该设备IP地址冲突。
2. 当接口的MAC地址变化时，发送免费ARP通知其它设备更新ARP表项。

设备具有免费ARP报文学习功能。当设备收到免费ARP报文时，设备判断是否存在和免费ARP报文源IP地址对应的动态
ARP表项，如果存在，根据免费ARP报文中携带的信息更新ARP表项。

**相关配置**


配置指南 ARP

######  配置免费 ARP

接口模式下，使用命令arp gratuitous-send interval seconds [number]允许接口定时发送免费ARP请求报文。缺省情况下接
口上该功能是关闭的。一般在该接口充当下联设备网关时，需要开启这个功能，定时更新使下联设备的网关mac，防止他人冒

###### 充网关。

###### 2.3.5 代理 ARP

**工作原理**

设备的代理ARP功能可以帮助没有路由信息的主机，获得其它子网IP地址的MAC地址。比如设备接收到一个ARP请求，
ARP请求的发送者IP地址与目标IP地址不属于同一网段，而设备又知道所请求IP地址的路由，设备就会发送ARP响应，响
应的MAC地址为设备自身的以太网MAC地址，这个过程就是代理ARP的功能。

**相关配置**

######  配置代理 ARP

 接口模式下，使用命令ip proxy-arp开启代理ARP功能。

 缺省情况下路由器上开启了代理ARP功能，而交换机上关闭了代理ARP功能。

###### 2.3.6 本地代理 ARP

**工作原理**

本地ARP代理指的是同一个VLAN内的代理，这里头的VLAN指的是普通VLAN或者Sub VLAN。

设备开启本地代理ARP功能后，可以帮助主机获得子网内其他主机的MAC地址。比如在设备开启端口保护的情况下，不同端
口下的用户被二层隔离，在开启本地ARP代理功能后，设备接收到一个ARP请求，就会代理发送ARP响应，响应的MAC
地址为设备自身的以太网MAC地址，这样不同的主机之间的通信靠三层路由来实现。这个过程就是本地代理ARP的功能。

**相关配置**

######  配置本地代理 ARP

 接口模式下，使用命令local-proxy-arp开启本地代理ARP功能。

 缺省情况下关闭本地代理ARP功能。

 该命令只在SVI口上支持。


配置指南 ARP

###### 2.3.7 ARP 可信检测

**工作原理**

该命令用于防止arp欺骗导致无用的arp表项过多占用设备资源。在三层接口开启arp可信检测功能后，从该接口上收到arp
请求报文：

1. 如果对应表项不存在，则创建动态arp表项，并经过 1 到 5 秒的一个随机时间后进入NUD（邻居不可达探测），即将新学
   习的arp表项设置为老化状态并单播arp请求，在老化时间内收到对端arp更新，则保存表项，否则直接删除该表项。
2. 如果对应arp表项已经存在，则不进行NUD探测逻辑。
3. 如果已有的动态arp表项的MAC地址被更新，也走NUD探测逻辑。
   该功能由于在ARP学习过程中增加了一个严格确认的过程，所以开启该功能会影响到ARP的学习性能。

关闭该功能后，arp表项的学习和更新不再走NUD逻辑。

**相关配置**

######  配置 ARP 可信检测

接口模式下，使用命令arp trust-monitor enable命令开启ARP可信检查功能，缺省情况下没有开启该功能。

###### 2.3.8 ARP 防 IP 报文攻击

**工作原理**

在收到未解析的IP报文时，交换机设备不能够进行硬件转发，需要把报文送CPU进行地址解析，如果此类报文大量送CPU，
就会对CPU造成冲击，影响交换机其它业务的运行。

开启ARP防IP报文攻击后，在ARP请求期间，交换机CPU会统计收到的目的IP命中该ARP表项的报文个数，当这个个数
等于配置的个数时，会设置一个丢弃表项到硬件，后续硬件收到所有该目的IP的报文都不会送CPU；在地址解析完成时，更
新上述表项为转发状态，使得交换机能够对该目的IP的报文进行硬件转发。

**相关配置**

######  配置 ARP防IP报文攻击

 全局模式下，使用命令arp anti-ip-attack配置触发ARP丢弃表项的IP报文个数。

 缺省情况下，在 3 个目的IP地址相同的未知名单播报文送CPU后，就会设置丢弃表项。


配置指南 ARP

###### 2.3.9 抑制往认证 VLAN 发送 ARP 请求

**工作原理**

在网关认证模式下， SuperVLAN下的所有子VLAN默认都是认证VLAN，认证VLAN下的认证用户需要在认证后才能上网。
用户认证后会在设备上生成静态ARP表项，因此设备访问认证用户时，不需要往认证VLAN发送ARP请求。若设备需要访问
免认证VLAN下的用户时，只需要往免认证VLAN发送ARP请求。

在网关认证模式下，设备默认开启了抑制往认证VLAN发送ARP请求的功能。如果设备需要访问认证VLAN下的免认证用户，
需要关闭该功能。

**相关配置**

######  配置抑制往认证 VLAN 发送 ARP 请求

 接口模式下，使用命令arp suppress-auth-vlan-req开启抑制往认证VLAN发送ARP请求功能。

 缺省情况下开启抑制往认证VLAN发送ARP请求功能。

#### 2.4 配置详解

配置项 配置建议&相关命令

### 配置静态ARP

```
可选配置，用于IP地址和MAC地址的静态绑定。
```

arp (^) 定义静态ARP
配置ARP属性

### 可选配置，用于指定ARP表项的超时时间、ARP请求重传次数和间隔、未解析ARP表项

```
数上限、接口ARP学习数量限制
arp timeout 配置ARP超时时间
arp retry interval 配置ARP请求重传时间间隔
arp unresolve 配置未解析ARP表项的数量限制
arp cache interface-limit 配置接口ARP学习数量限制
```

配置可信任ARP

### 可选配置，用于防止ARP欺骗。^

```
service trustedarp 启用可信任ARP功能
```

arp trusteduser-vlan (^) 添加可信任ARP时进行VLAN转换
arp trusted aging (^) 允许可信任ARP老化
arp trusted 调整可信任ARP的容量

### 配置免费ARP 可选配置，用于检测IP地址冲突，以及让外围设备更新本机的ARP。^

```
arp gratuitous-send interval 开启定时发送免费ARP的功能
```

配置指南 ARP

### 配置代理ARP 可选配置，用于代理应答请求不同子网内其他设备的ARP请求。^

```
ip proxy-arp 开启代理ARP功能。
```

### 配置本地代理ARP

```
可选配置，用于代理应答请求子网内其他设备的ARP请求。
local-proxy-arp 开启本地代理ARP功能。
```

### 配置ARP可信检测 可选配置，用于发送单播ARP请求确认，以保证学习ARP表项正确性。^

```
arp trusted-monitor enable 开启ARP可信检测功能
```

### 配置ARP防IP报文攻击 可选配置，防止IP报文大量送CPU对CPU造成冲击。^

```
arp anti-ip-attack 配置触发ARP设丢弃表项的IP报文个数。
```

配置抑制往认证VLAN发送
ARP请求

### 可选配置，用于抑制往认证VLAN发送ARP请求。^

```
arp suppress-auth-vlan-req 开启抑制往认证VLAN发ARP请求功能。
```

###### 2.4.1 配置静态 ARP

**配置效果**

用户手工指定IP地址和MAC地址的映射，防止设备学到错误的ARP表项而影响网络。

**注意事项**

对于三层交换机，配置完静态ARP表项后，交换机必须在学习到该静态ARP表项的MAC地址对应的物理端口后才能进行正
常的三层路由。

**配置方法**

######  配置静态 ARP

 可选配置

 在汇聚设备上，可以通过静态绑定上联设备的IP和MAC地址的映射，防止设备因受到ARP攻击而更改掉上联设备的
ARP表项的MAC地址，导致网络异常。

 在全局模式下配置

**检验方法**

使用命令show running-config查看命令是否生效，或使用命令show arp static查看是否成功创建了静态ARP缓存表。

**相关命令**


配置指南 ARP

######  配置静态 ARP

```
【命令格式】 arp [vrf name | oob] ip-address mac-address type
【参数说明】 vrf name：指定VRF实例，name参数是VRF实例的名称。
oob：为MGMT口配置静态ARP。
ip-address：与MAC地址对应的IP地址，分为四组十进制表示的数值，组之间用点隔开。
mac-address：数据链路层地址， 48 个比特位组成。
type：ARP封装类型。对于以太网接口，关键字为arpa。
【命令模式】 全局模式
【使用指导】 RGOS使用ARP缓冲表，根据 32 个比特位IP地址查找 48 个比特位的MAC地址。
由于大多数主机支持动态ARP解析，所以通常不需要配置静态ARP映射。利用clear arp-cache命令可以删
除动态学习到的ARP映射。
```

**配置举例**

【网络环境】

(^) 【注释】 A为路由器
B为交换机，作为用户主机网段的网关。
C、D、E为用户主机^
【配置方法】 在设备B上配置静态ARP表项，静态绑定设备A的IP和MAC地址映射。
Ruijie(config)#arp 192.168.23.1 00D0.F822.334B arpa
【检验方法】 通过show arp static命令可查看静态ARP表项：
Ruijie(config)#show arp static
Protocol Address Age(min) Hardware Type Interface
Internet 192.168.23. 1 <static> 00D0.F822.334B arpa
1 static arp entries exist.
**常见配置错误**
 静态绑定的MAC地址错误。


配置指南 ARP

###### 2.4.2 配置 ARP 属性

**配置效果**

用户指定ARP表项的超时时间、ARP请求重传次数和间隔、未解析ARP表项数上限、接口ARP学习数量限制、单板ARP
学习数量限制。

**注意事项**

###### 无

**配置方法**

######  ARP 超时设置

 可选配置

 局域网中如果用户上下线较频繁，则可以将ARP超时时间设置小一点，可以将无效的ARP表项尽早删除。

 在接口模式下配置

######  ARP 请求重传时间间隔和次数

 可选配置

 在网络带宽资源不足时，可以将重传时间间隔配大，次数配小，以减少网络带宽的消耗。

 在全局模式下配置

######  未解析 ARP 表项的数量限制

 可选配置

 在网络带宽资源不足时，可以将未解析ARP表项的数量配小，以减少网络带宽的消耗。

 在全局模式下配置

######  接口 ARP 学习数量限制

 可选配置

 在接口模式下配置

**检验方法**

使用命令show arp timeout可以查看所有接口的老化超时时间。

使用命令show running-config查看ARP请求重传时间间隔和次数、未解析ARP表项是数量限制、接口ARP学习数量限制、

###### 单板ARP学习数量限制命令是否生效。


配置指南 ARP

**相关命令**

######  ARP 超时设置

```
【命令格式】 arp timeout seconds
【参数说明】 seconds：超时时间，以秒为计算单位，默认值为 3600 ，范围 0 - 2147483 。
【命令模式】 接口模式
【使用指导】 ARP超时设置只对动态学习到的IP地址和MAC地址映射起作用。超时时间设置得越短，ARP缓存中保存的
映射表就越真实，但是ARP消耗网络带宽也越多，所以需要权衡利弊。除非有特别的需要，否则一般不需要
配置ARP超时时间。
```

######  ARP 请求重传时间间隔和次数

```
【命令格式】 arp retry interval seconds
【参数说明】 seconds ： <1-3600>,ARP请求的重传时间可以设置为1~3600秒，默认值为 1 秒。
【配置模式】 全局模式
【使用指导】 当发现本设备有频繁的向外发送ARP请求，引起网络繁忙等其它问题时，可以将ARP请求的重传时间设置
长一点，一般不要超过动态ARP表项的老化时间。
```

######  未解析 ARP 表项的数量限制

```
【命令格式】 arp unresolve number
【参数说明】 number：未解析ARP表项的最大个数，取值范围为< 1 - 8192 >。默认值为 8192 。
【配置模式】 全局模式
【使用指导】 当发现ARP缓存表中出现大量未解析表项，并且一段时间后还没有消失时，可以用此命令限制未解析表项的
个数。
```

######  接口 ARP 学习数量限制

```
【命令格式】 arp cache interface-limit limit
【参数说明】 limit：指定接口所能学习的ARP数量最大限制，包括静态配置和动态学习的ARP，取值范围为 0 - 设备支持的
ARP表项容量， 0 表示不限制接口ARP学习数量。
【配置模式】 接口模式
【使用指导】 限制接口的ARP学习数量，可防止恶意的ARP攻击，让设备生成大量的ARP表项，占用过多的表项资源。
配置的值必须不小于当前接口已经学习到的ARP表项数量，否则配置不生效。该限制受限于设备支持的ARP
容量。
```

**配置举例**


配置指南 ARP

【网络环境】

(^) 【注释】 A为路由器
B为交换机，作为用户主机网段的网关。
C、D、E为用户主机^
【配置方法】  配置接口GigabitEthernet 0/1下的ARP超时时间为 60 秒
 配置接口GigabitEthernet 0/1下的ARP学习数量限制为 300
 配置ARP请求重传时间间隔为 3 秒
 配置ARP请求重传次数为 4 次
 配置未解析ARP表项数量限制为 4096
 配置slot 1 subslot 2的ARP学习数量限制为 1000
Ruijie(config)#interface gigabitEthernet 0/1
Ruijie(config-if-GigabitEthernet 0/1)#arp timeout 60
Ruijie(config-if-GigabitEthernet 0/1)#arp cache interface-limit 300
Ruijie(config-if-GigabitEthernet 0/1)#exit
Ruijie(config)#arp retry interval 3
Ruijie(config)#arp retry times 4
Ruijie(config)#arp unresolve 4096
【检验方法】  通过show arp timeout查看接口的老化时间
 通过show running-config查看ARP请求重传时间间隔和次数、未解析ARP表项是数量限制、接口
ARP学习数量限制
Ruijie#show arp timeout
Interface arp timeout(sec)

---------------------- ----------------

GigabitEthernet 0/1 60
GigabitEthernet 0/2 3600
GigabitEthernet 0/4 3600
GigabitEthernet 0/5 3600
GigabitEthernet 0/7 3600
VLAN 100 3600
VLAN 111 3600
Mgmt 0 3600
Ruijie(config)# show running-config


配置指南 ARP

```
arp unresolve 4096
arp retry times 4
arp retry interval 3
!
interface GigabitEthernet 0/1
arp cache interface-limit 300
```

**常见配置错误**

无

###### 2.4.3 配置可信任 ARP

**配置效果**

###### 可以有效的防止针对网关的ARP欺骗。

**注意事项**

###### 可信任ARP只在交换机上支持。

**配置方法**

 如果需要部署GSN方案，则应该执行此配置项。

 部署GSN全局安全网络解决方案时，需要配置开启可信任ARP功能。

 在全局模式下配置

**检验方法**

使用show arp trusted命令查看可信ARP表项；

使用show running命令查看可信任ARP的相关配置是否生效。

**相关命令**

######  启用可信任 ARP 功能

```
【命令格式】 service trustedarp
【参数说明】 -
【命令模式】 全局模式
```

配置指南 ARP

```
【使用指导】 设备的可信任ARP功能是一种防止ARP欺骗的功能，作为GSN方案的一部分，需要和GSN方案一起使用。
```

######  添加可信任 ARP 时进行 VLAN 转换

```
【命令格式】 arp trusteduser-vlan vid1 translated-vlan vid2
【参数说明】 vid1：服务器设置的VID
vid2：转换后的VID
【配置模式】 全局模式
【使用指导】 要使此命令生效，首先启用可信任ARP功能。只有在服务器下发的VLAN和可信任ARP生效的VLAN不同
时，才需要配置此命令。
```

######  查看交换机上的可信任 ARP

```
【命令格式】 show arp trusted^ [ip [mask]]^
【参数说明】 ip：IP地址，显示指定IP地址的ARP表项；如果指定trusted关键字，则只显示可信任ARP表项，否则显
示非可信任ARP表项。
mask：显示IP子网内的ARP表项; 如果指定trusted关键字，则只显示可信任ARP表项，否则显示非可信
任ARP表项。
【配置模式】 特权模式
【使用指导】 -
```

######  删除交换机上的可信任 ARP

```
【命令格式】 clear arp trusted [ip [mask]]
【参数说明】 ip：IP地址，显示指定IP地址的ARP表项；如果指定trusted关键字，则只显示可信任ARP表项，否则显
示非可信任ARP表项。
mask：显示IP子网内的ARP表项; 如果指定trusted关键字，则只显示可信任ARP表项，否则显示非可信
任ARP表项。
【配置模式】 特权模式
【使用指导】 执行clear arp trusted会删除交换机上的所有的可信ARP，可能导致用户不能上网。
一般情况下使用clear arp trusted ip删除指定的可信任ARP表项。
```

######  允许可信任 ARP 老化

```
【命令格式】 arp trusted aging
【参数说明】 -^
【配置模式】 全局模式
【使用指导】 使用该命令后可信任ARP开始老化，老化时间和动态ARP老化时间相同。老化时间可以通过接口模式下arp
timeout命令设置。
```

######  调整可信任 ARP 的容量

```
【命令格式】 arp trusted number
【参数说明】 number：取值范围最小为 10 ，最大为对应产品arp容量减去 1024 ，缺省可信arp的最大表项数为arp总容
量的一半。
【配置模式】 全局模式
```

配置指南 ARP

```
【使用指导】 要使此命令生效，首先启用可信任ARP功能。可信任ARP表项和其它表项共享内存，如果可信任表项占用
过多，可能导致动态ARP表项空间不够。一般按需设置，不要设置得太大。
```

**配置举例**

【网络环境】

【注释】 A为路由器
B为交换机，作为用户主机网段的网关。
C、D、E为用户主机^
【配置方法】  开启可信任ARP功能
 配置VLAN转换
 配置可信任ARP表项运行老化
 配置可信任ARP表项的容量为 1024
Ruijie(config)#service trustedarp
Ruijie(config)#arp trusted user-vlan 2 - 9 translated-vlan 10
Ruijie(config)#arp trusted aging
Ruijie(config)#arp trusted 1024
【检验方法】  通过 **show running-config** 查看上面的配置是否生效
Ruijie(config)# show running-config
service trustedarp
arp trusted user-vlan 2 - 9 translated-vlan 10
arp trusted aging
arp trusted 1024

**常见配置错误**

 可信任ARP功能未开启，导致ARP表项下发失败

###### 2.4.4 配置免费 ARP

**配置效果**


配置指南 ARP

接口定时发送免费ARP报文。

**注意事项**

无

**配置方法**

 可选配置

 设备做用户网关时，为了防止因为ARP欺骗导致其他用户学习到错误的网关MAC后会一直上不了网，需要在接口上开
启免费ARP功能。

######  在接口模式下配置

**检验方法**

使用show running-config interface [name]查看是否配置成功。

**相关命令**

######  开启定时发送免费 ARP 的功能

```
【命令格式】 arp gratuitous-send intervalseconds [number]
【参数说明】 seconds：发送免费ARP请求的时间间隔，单位秒，取值范围<1-3600>。
number：发送免费ARP请求的数量，缺省值是 1 ，取值范围<1-100>。
【命令模式】 接口模式
【使用指导】 当设备的网络接口作为下联设备的网关时，如果下联设备中有冒充网关的行为，则可以在此接口配置定时发送
免费ARP请求，公告自己才是真正的网关。
```

**配置举例**

【网络环境】

(^) 【注释】 A为路由器


配置指南 ARP

B为交换机，作为用户主机网段的网关。
C、D、E为用户主机^
【配置方法】 配置GigabitEthernet 0/0口发送免费ARP功能，频率为每 5 秒发送一个免费ARP请求报文。
Ruijie(config-if-GigabitEthernet 0/0)#arp gratuitous-send interval 5
【检验方法】 使用show running-config interface命令查看配置是否生效
Ruijie#sh running-config interface gigabitEthernet 0/0

```
Building configuration...
Current configuration : 127 bytes
!
interface GigabitEthernet 0/0
duplex auto
speed auto
ip address 30.1.1.1 255.255.255.0
arp gratuitous-send interval 5
```

**常见配置错误**

无

###### 2.4.5 配置代理 ARP

**配置效果**

设备代理应答非本机的ARP请求报文。

**注意事项**

三层交换机缺省关闭代理ARP功能，路由器缺省开启代理ARP功能。

**配置方法**

 可选配置。

 没有路由信息的主机需要获得其它子网IP地址的MAC地址，设备需要开启代理ARP功能，代理应答ARP。

 在接口模式下配置

**检验方法**

###### 使用show ip interface [name]命令查看是否配置成功。


配置指南 ARP

**相关命令**

######  开启代理 ARP 功能

```
【命令格式】 ip proxy-arp
【参数说明】 -^
【命令模式】 接口模式
【使用指导】 -^
```

**配置举例**

【网络环境】

【注释】 A为路由器
B为交换机，作为用户主机网段的网关。
C、D、E为用户主机^
【配置方法】 配置GigabitEthernet 0/0口开启代理ARP功能
Ruijie(config-if-GigabitEthernet 0/0)#ip proxy-arp
【检验方法】 使用show ip interface命令查看是否配置成功
Ruijie#show ip interface gigabitEthernet 0/0
GigabitEthernet 0/0
IP interface state is: DOWN
IP interface type is: BROADCAST
IP interface MTU is: 1500
IP address is:
No address configured
IP address negotiate is: OFF
Forward direct-broadcast is: OFF
ICMP mask reply is: ON
Send ICMP redirect is: ON
Send ICMP unreachable is: ON
DHCP relay is: OFF
Fast switch is: ON


配置指南 ARP

```
Help address is: 0.0.0.0
Proxy ARP is: ON
ARP packet input number: 0
Request packet : 0
Reply packet : 0
Unknown packet : 0
TTL invalid packet number: 0
ICMP packet input number: 0
Echo request : 0
Echo reply : 0
Unreachable : 0
Source quench : 0
Routing redirect : 0
```

**常见配置错误**

无

###### 2.4.6 配置本地代理 ARP

**配置效果**

设备代理应答子网内非本机的ARP请求报文。

**注意事项**

只在SVI口下支持。

**配置方法**

 可选配置。

 在开启端口保护时，如果有需要VLAN内的主机通信，则需要配置本地ARP代理。

 在接口模式下配置

**检验方法**

###### 使用show run interface [name]命令查看是否配置成功。

**相关命令**


配置指南 ARP

######  开启本地代理 ARP 功能

```
【命令格式】 local-proxy-arp
【参数说明】 -
【命令模式】 接口模式
【使用指导】 -
```

**配置举例**

【网络环境】

【注释】 A为路由器
B为交换机，作为用户主机网段的网关。
C、D、E为用户主机^
【配置方法】 配置VLAN 1口开启代理ARP功能
Ruijie(config-if-VLAN1)#local-proxy-arp
【检验方法】 使用show ip interface命令查看是否配置成功
Ruijie#show running-config interface vlan 1

```
Building configuration...
Current configuration : 53 bytes
```

```
interface VLAN 1
ip address 192 .1 68 .1.2 255.255.255.0
local-proxy-arp
```

**常见配置错误**

无


配置指南 ARP

###### 2.4.7 配置 ARP 可信检测

**配置效果**

开启arp可信检测功能，在收到arp请求报文后，如果对应表项不存在，进入NUD（邻居不可达探测）。如果已有的动态arp
表项的MAC地址被更新，马上走NUD探测逻辑，起到防止arp攻击的作用。

**注意事项**

该功能由于在ARP学习过程中增加了一个严格确认的过程，所以开启该功能会影响到ARP的学习性能。

**配置方法**

 可选配置。

 如果有要求严格学习ARP表项的需求时，设备上可以开启arp可信功能，设备在收到arp请求报文后，如果之前不存在
对应arp表项，则需要发送单播ARP请求报文，在确认对端真实存在后才学习ARP表项，否则不学习ARP表项。在arp
表项的mac地址发生了变化后，马上走NUD探测，防止arp欺骗。

 在接口模式下配置

**检验方法**

###### 使用show running-config interface [name] 查看是否配置成功。

**相关命令**

######  开启 ARP 可信检测功能

```
【命令格式】 arp trust-monitor enable
【参数说明】 -^
【命令模式】 接口模式
【使用指导】
```

### 开启该功能，如果对应arp表项已经存在，且mac地址没发生更新，则不进行NUD探测逻辑。^

### 开启该功能，如果已有的动态arp表项的mac地址被更新，则马上走NUD探测逻辑。^

### 关闭该功能后，arp表项的学习和更新不需要NUD过程。^

**配置举例**


配置指南 ARP

【网络环境】

(^) 【注释】 A为路由器
B为交换机，作为用户主机网段的网关。
C、D、E为用户主机^
【配置方法】 配置GigabitEthernet 0/0口开启ARP可信检测功能
Ruijie(config-if-GigabitEthernet 0/0)#arp trust-monitor enable
【检验方法】 使用show running-config interface查看是否配置是否生效
Ruijie#show running-config interface gigabitEthernet 0/0
Building configuration...
Current configuration : 184 bytes
!
interface GigabitEthernet 0/0
duplex auto
speed auto
ip address 30.1.1.1 255.255.255.0
arp trust-monitor enable
**常见配置错误**
无

###### 2.4.8 配置 ARP 防 IP 报文攻击

**配置效果**

交换机CPU收到配置个数的目的IP命中该ARP表项的报文时，后续所有该目的IP的报文都不会送CPU。

**注意事项**

只在交换机产品上支持。


配置指南 ARP

**配置方法**

 可选配置。

 在交换机产品上，默认情况下，在 3 个未知名单播报文送CPU后设置丢弃表项。通过过此命令用户可以针对具体网络环
境调整这个参数，也可以关闭该功能。

 在全局模式下配置。

**检验方法**

###### 使用show run命令查看是否配置成功。

**相关命令**

######  配置ARP防IP报文攻击

```
【命令格式】 arp anti-ip-attack num
【参数说明】 num：设置触发ARP设丢弃表项的IP报文个数，取值范围<0-100>。
0 表示关闭ARP防IP报文攻击功能。缺省值为 3 。
【命令模式】 全局模式
```

【使用指导】 (^) 如果硬件路由资源比较充分，arpanti-ip-attack num可以设置得小一些。在硬件路由资源比较紧张的情
况下，要优先满足正常路由的使用，可以将arpanti-ip-attack num设置得比较大，或者关闭该功能。
**配置举例**
【网络环境】
(^) 【注释】 A为路由器
B为交换机，作为用户主机网段的网关。
C、D、E为用户主机^
【配置方法】 在设备B上配置ARP防IP报文攻击。
Ruijie(config)#arp anti-ip-attack 10
【检验方法】 使用show running-config查看配置是否生效


配置指南 ARP

Ruijie#show running-config

```
Building configuration...
Current configuration : 53 bytes
arp anti-ip-attack 10
```

**常见配置错误**

无

###### 2.4.9 配置抑制往认证 VLAN 发送 ARP 请求

**配置效果**

设备不往认证VLAN发送ARP请求报文。

**注意事项**

只在SVI口下支持。

**配置方法**

 可选配置。

 在开启网关认证模式下，设备默认不往认证VLAN发送ARP请求报文。若需要往认证VLAN发送ARP请求，使用该命
令的no形式取消该功能。

 在接口模式下配置

**检验方法**

###### 使用show run interface [name]命令查看是否配置成功。

**相关命令**

######  抑制往认证 VLAN 发送 ARP 请求

```
【命令格式】 arp suppress-auth-vlan-req
【参数说明】 -
【命令模式】 接口模式
【使用指导】 -^
```

配置指南 ARP

**配置举例**

【网络环境】

【注释】 A为路由器
B为交换机，作为用户主机网段的网关。
C、D、E为用户主机^
【配置方法】 配置VLAN 2口关闭抑制往认证VLAN发送ARP请求的功能。
Ruijie(config-if-VLAN2)#no arp suppress-auth-vlan-req
【检验方法】 使用show running-config interface [name]查看配置是否生效
Ruijie#show running-config interface vlan 2

```
Building configuration...
Current configuration : 53 bytes
```

```
interface VLAN 2
ip address 192 .1 68 .1.2 255.255.255.0
no arp suppress-auth-vlan-req
```

**常见配置错误**

无

#### 2.5 监视与维护

**清除各类信息**

### 在设备运行过程中执行clear命令，可能因为重要信息丢失而导致业务中断。^

作用 命令


配置指南 ARP

清除动态ARP表项。在网关认证模式
下，不会删除认证VLAN下的动态
ARP表项。

```
clear arp-cache
```

**查看运行情况**

作用 命令

显示ARP表。

show arp[detail][interface-type interface-number|[vrfvrf-name] [ip [mask] |
mac-address | static| complete | incomplete ]| subvlan {subvlan-number | min-max
min_value max_value}]
显示ARP表 show ip arp[vrf vrf-name]
显示可信任ARP表 show arp^ [detail] trusted^ [ip^ [mask]]^
显示ARP表项相应计数 show arp counter^
显示动态ARP表项的老化时间 show arp timeout^

**查看调试信息**

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。^

作用 命令
显示ARP报文的收发情况 debug arp
显示ARP表项的创建删除情况 debug arp event


配置指南 IPv6

### 3 IPv6

#### 3.1 概述

随着Internet的迅速增长以及IPv4地址空间的逐渐耗尽，IPv4的局限性就越来越明显。对新一代互联网络协议（Internet Protocol
Next Generation - IPng）的研究和实践已经成为热点，Internet工程任务工作小组(IETF)的IPng工作组确定了IPng的协议规
范，并称之为"IP版本6"（IPv6），该协议的规范在RFC2460中有详细的描述。

IPv6 **的主要特点**

######  更大的地址空间

地址长度由IPv4的 32 位扩展到 128 位，约有2^128个地址，IPv6采用分级地址模式，支持从Internet核心主干网到企业内
部子网等多级子网地址分配方式。

######  简化了报头格式

新IPv6报文头的设计原则是力图将报文头开销降到最低，因此将一些非关键性字段和可选字段从报文头中移出，放到扩展的
报文头中，虽然IPv6地址长度是IPv4的四倍，但报头仅为基本IPv4首部的两倍。改进的IPv6报文头在设备转发时拥有更高
的效率，例如IPv6报文头中没有校验和，IPv6设备在转发中不需要去处理分片(分片由发起者完成)。

######  高效的层次寻址及路由结构

IPv6采用聚合机制，定义非常灵活的层次寻址及路由结构，同一层次上的多个网络在上层设备中表示为一个统一的网络前缀，
这样可以显著减少设备必须维护的路由表项，这也大大降低了设备的选路和存储开销。

######  简单的管理：即插即用

通过实现一系列的自动发现和自动配置功能，简化网络节点的管理和维护。比如邻接节点发现（Neighbor Discovery）、最大传
输单元发现（MTU Discovery）、路由器通告（Router Advertisement）、路由器请求（Router Solicitation）、节点自动配置
（Auto-configuration）等技术就为即插即用提供了相关的服务。特别要提到的是IPv6支持全状态和无状态两种地址配置方式，
在IPv4中，动态主机配置协议DHCP实现了主机IP地址及其相关配置的自动设置，IPv6承继IPv4的这种自动配置服务，并
将其称为全状态自动配置(Stateful Autoconfiguration)（参见DHCPv6）。除了全状态自动配置，IPv6还采用了一种被称为无状
态自动配置（Stateless Autoconfiguration）的自动配置服务。在无状态自动配置过程中，主机自动获得链路本地地址、本地设
备的地址前缀以及其它一些相关的配置信息。

######  安全性

IPSec是IPv4的一个可选扩展协议，但是在IPv6中它是IPv6的一个组成部分，用于提供IPv6的安全性。目前，IPv6实现了
认证头（Authentication Header，AH）和封装安全载荷（Encapsulated Security Payload，ESP）两种机制。前者实现数据的
完整性及对IP包来源的认证，保证分组确实来自源地址所标记的节点；后者提供数据加密功能，实现端到端的加密。

######  更好的 QoS 支持


配置指南 IPv6

IPv6包头的新字段定义了数据流如何识别和处理。IPv6包头中的流标识（Flow Label）字段用于识别数据流身份，利用该字段，
IPv6允许用户对通信质量提出要求。设备可以根据该字段标识出同属于某一特定数据流的所有包，并按需对这些包提供特定的
处理。

######  用于邻居节点交互的新协议

IPv6的邻居发现协议（Neighbor Discovery Protocol）使用一系列IPv6控制信息报文（ICMPv6）来实现相邻节点（同一链路
上的节点）的交互管理。邻居发现协议以及高效的组播和单播邻居发现报文替代了以往基于广播的地址解析协议ARP、ICMPv4
路由器发现等报文。

######  可扩展性

IPv6特性具有很强的可扩展性，新特性可以添加在IPv6包头之后的扩展包头中。不像IPv4，包头最多只能支持 40 字节的可
选项，IPv6扩展包头的大小仅受到整个IPv6包最大字节数的限制。

**协议规范**

 RFC4291 - IPVersion6AddressingArchitecture.

 RFC2460 - Internet Protocol, Version 6 (IPv6) Specification

 RFC4443 - Internet Control Message Protocol (ICMPv6)for the Internet Protocol Version 6 (IPv6) Specification

 RFC4861 - Neighbor Discovery for IP version 6 (IPv6)

 RFC4862 - IPv6 Stateless Address Autoconfiguration

 RFC5059 - Deprecation of Type 0 Routing Headers in IPv6

#### 3.2 典型应用

典型应用 场景描述
IPv6地址通讯 两台PC使用IPv6地址进行通信

###### 3.2.1 IPv6 地址通讯

**应用场景**

如下图所示，主机 1 和主机 2 可以通过IPv6地址进行通信。

图 3 - 1


配置指南 IPv6

**功能部属**

###### 主机可以使用无状态地址自动配置也可以使用DHCPv6分配地址，配置完地址后，即可以使用IPv6地址进行通讯。

#### 3.3 功能详解

**功能特性**

功能特性 作用
IPv6地址格式 IPv6的地址格式使其具有更大的地址空间，及灵活的表示方法。
IPv6地址类型 IPv6通过地址标识来区分其网络应用。
IPv6包头结构 IPv6通过简化固定报头、扩展选项报头，提高了设备处理数据包的速度，也提高了其转发性能。
IPv6路径MTU发现 主机动态的发现并调整发送数据路径上的MTU的大小，节省了路由器的资源，提高了IPv6网络的效
率。
IPv6邻居发现 完成路由器发现、前缀发现、参数发现、地址自动配置、地址解析（相当于ARP）、确定下一跳、邻居
不可达检测、地址冲突检测和重定向。
IPv6源路由 用来指定报文经过哪些中间节点到达目的地址，类似于IPv4的宽松源路由选项和宽松记录路。
控制ICMPv6差错报
文的发送速率

```
防止拒绝服务攻击。
```

IPv6 HOP-LIMIT 防止无用的单播报文在网络上无限传播下去，浪费网络带宽
抑制往认证vlan发送
广播NS报文

```
网关认证模式下，设备抑制往认证VLAN发送广播NS请求的功能
```

MGMT口支持缺省网
关

```
给MGMT口配置缺省网关，为MGMT口生成一条默认路由
```

###### 3.3.1 IPv6 地址格式

IPv6地址格式IPv6地址的基本表达方式是X : X : X : X : X : X : X : X，其中X是一个 4 位十六进制整数(16位)。每一个数字
包含 4 个比特，每个整数包含 4 个十六进制数字，每个地址包括 8 个整数，一共 128 位。下面是一些合法的IPv6地址：

2001:ABCD:1234:5678:AAAA:BBBB:1200:2100

800 : 0 : 0 :0 : 0 : 0 : 0 : 1


配置指南 IPv6

1080 : 0 : 0 : 0 : 8 : 800 : 200C : 417A

这些整数是十六进制整数，其中A到F表示的是 10 到 15 。地址中的每个整数都必须表示出来，但起始的 0 可以不必表示。某
些IPv6地址中可能包含一长串的0 (就像上面的第二和第三个例子一样)。当出现这种情况时，允许用“：：”来表示这一长串的 0 。
即地址800 : 0 : 0 : 0 : 0 : 0 : 0 : 1可以被表示为：800 :: 1

这两个冒号表示该地址可以扩展到一个完整的 128 位地址。在这种方法中，只有当 16 位组全部为 0 时才会被两个冒号取代，
且两个冒号在地址中只能出现一次。

在IPv4和IPv6的混合环境中还有一种混合的表示方法。IPv6地址中的最低 32 位可以用于表示IPv4地址，该地址可以按照
一种混合方式表达，即X : X : X : X : X : X : d. d. d. d，其中X表示一个1 6位整数，而d表示一个 8 位的十进制整数。例如，
地址0 : 0 : 0 : 0 : 0 : 0 : 192 .168. 20. 1 就是一个合法的IPv6地址。使用简写的表达方式后，该地址也可以表示为：: : 192 .168.

20. 1。典型代表是IPv4兼容IPv6地址和IPv4映射IPv6地址，IPv4兼容IPv6地址前 96 比特是 0 ，表示法为“::A.B.C.D”，
    例如“::1.1.1.1”，目前IPv4兼容地址已被废除；IPv4映射IPv6地址表示法为“::FFFF:A.B.C.D”，用于把IPv4地址表示为
    IPv6地址，如把IPv4地址“1.1.1.1”映射到IPv6地址“::FFFF:1.1.1.1”。

由于IPv6地址被分成两个部分：子网前缀和接口标识符，因此可以按照类似CIDR地址的方式被表示为一个带额外数值的地
址，其中该数值指出了地址中有多少位是代表网络部分(网络前缀)，即IPv6节点地址中指出了前缀长度，该长度与IPv6地址
间以斜杠区分，例如：12AB::CD30:0:0:0:0/60，这个地址中用于选路的前缀长度为 60 位。

**相关配置**

######  配置 IPv6 地址

 缺省情况接口没有配置IPv6地址。

 可通过ipv6 address命令配置接口IPv6地址。

 配置后根据冲突检测即可使用该IPv6地址进行通信。

###### 3.3.2 IPv6 地址类型

RFC 4291 定义了三种IPv6地址类型：

 单播(Unicast)：单个接口的标识符。送往一个单播地址的包将被传送至该地址标识的接口上。

 组播(Multicast)：一组接口(一般属于不同节点)的标识符。送往一个组播地址的包将被传送至加入该组播地址的所有接口
上。

 泛播(Anycast)：一组接口的标识符。送往一个泛播地址的包将被传送至该地址标识的接口之一(根据选路协议选择“最近”
的一个)。

### 在IPv6中已经没有定义广播地址。^

下面逐一介绍这几类地址：

######  单播地址（ Unicast Addresses ）


配置指南 IPv6

单播地址分为未指定地址、环回地址、链路本地地址、站点本地地址和全球单播地址。目前，站点本地地址被废除了，除了未
指定地址、环回地址和链路本地地址以外的单播地址，都是全球单播地址。

 未指定地址

未指定地址是0:0:0:0:0:0:0:0，通常简写为::，常见的两个用途是：

3. 若主机启动时没有单播地址，则以未指定地址作为源地址，发送路由器请求，从网关获取前缀信息，从而自动生成单播地
   址。
4. 给主机配置IPv6地址时，检测地址是否和同网段其它主机的地址冲突，则以未指定地址作为源地址发送邻居请求（相当
   于免费ARP）。

 环回地址

环回地址是0:0:0:0:0:0:0:1，通常简写为:: 1 ，相当于IPv4地址127.0.0.1，一般在节点给自身发报文时使用。

 链路本地地址

链路本地地址的格式如下：

图 3 - 2

链路本地地址用于单个网络链路上给主机编号。前缀的前 10 位标识的地址即链路本地地址。设备永远不会转发源地址或者目
的地址带有链路本地地址的报文。该地址的中间 54 位置成 0 。后 64 位表示接口标识符，地址空间的这部分允许单个网络连接
多达（ 2 的 64 次方减 1 ）个主机。

 站点本地地址

站点本地地址的格式如下：

图 3 - 3

站点本地地址可以用在站点内传送数据，设备不会将源地址或者目的地址带有站点本地地址的报文转发到Internet上，即这样
的包只能在站点内转发，而不能把包转发到站点外去。站点可以理解为一个公司的局域网，这种地址类似于IPv4的私有地址，
如192.168.0.0/16。RFC3879已经废除了站点本地地址。对于新的实现，不再支持该前缀，统一视为全球单播地址；对于已
经实现和部署的，可以继续用这个前缀。

 全球单播地址

全球单播地址格式如下：

图 3 - 4


配置指南 IPv6

全球单播地址中有一类地址是嵌入IPv4地址的IPv6地址，用于IPv4节点和IPv6节点互通，分为IPv4兼容IPv6地址和IPv4
映射IPv6地址两种。

IPv4兼容IPv6地址格式（IPv4-compatible IPv6 address）

图 3 - 5

IPv4映射IPv6地址格式（IPv4-mapped IPv6 address）

图 3 - 6

IPv4兼容IPv6地址主要是用在自动隧道上，这类节点既支持IPv4也支持IPv6，IPv4兼容IPv6地址通过IPv4设备以隧道方
式传送IPv6报文，目前IPv4兼容IPv6地址已被废除。而IPv4映射IPv6地址则被IP6节点用于访问只支持IPv4的节点，例
如当一个IPv4/IPv6主机的IPv6应用程序请求解析一个主机名字(该主机只支持IPv4)时，那么名字服务器内部将动态生成IPv4
映射的IPv6地址返回给IPv6应用程序。

######  组播地址（ Multicast Addresses ）

IPv6组播的地址格式如下：

| 8 | 4 | 4 | 112 bits |

+--------+----+----+---------------------------------------------+

|11111111|flgs|scop| group ID |

+--------+----+----+---------------------------------------------+

地址格式中的第 1 个字节为全“1”代表是一个组播地址。

 标志字段：

由 4 个比特位组成。目前只指定了第 4 位，该位用来表示该地址是由Internet编号机构指定的知名的组播地址，还是特定场合
使用的临时组播地址。如果该标志位为“0”，表示该地址为知名组播地址；如果该位为“1”，表示该地址为临时地址。其他 3 个
标志位保留将来用。

 范围字段：


配置指南 IPv6

由 4 个比特位组成，用来表示组播的范围。即组播组是包括本地节点、本地链路、本地站点，还包括IPv6全球地址空间中任
何位置的节点。

 组标识符字段：

长 112 位，用于标识组播组。根据组播地址是临时的还是知名的以及地址的范围，同一个组播标识符可以表示不同的组。

IPv6的组播地址是以FF00::/8为前缀的这类地址。一个IPv6的组播地址通常标识一系列不同节点的接口。当一个报文发送到
一个组播地址上时，那么该报文将分发到标识有该组播地址的每个节点的接口上。一个节点(主机或者设备)必须加入下列的组
播：

5. 本地链路所有节点组播地址 FF02::1
6. 被请求节点的组播地址，前缀为FF02:0:0:0:0:1:FF00:0000/104

如果是设备那么还必须加入本地链路所有设备的组播地址 FF02::2。

被请求节点的组播地址是对应于IPv6单播(unicast)和泛播(anycast)地址的，IPv6节点必须为配置的每个单播地址和泛播地址
加入其相应的被请求节点的组播地址。被请求节点的组播地址的前缀为FF02:0:0:0:0:1:FF00:0000/104，另外 24 位由单播地
址或者泛播地址的低 24 比特组成，例如对应于单播地址FE80::2AA:FF:FE21:1234的被请求节点的组播地址是
FF02::1:FF21:1234 ，

被请求节点组播地址通常用于邻居请求(NS)报文中，被请求节点组播地址的格式如下：

图 3 - 7

######  泛播地址（ Anycast Addresses ）

泛播地址与组播地址类似，同样是多个节点共享一个泛播地址，不同的是只有一个节点期待接收给泛播地址的数据包而组播地
址成员的所有节点均期待着接收发给该地址的所有包。泛播地址被分配在正常的IPv6单播地址空间，因此泛播地址在形式上
与单播地址无法区分开，一个泛播地址的每个成员，必须显式地加以配置，以便识别是泛播地址。

### 泛播地址只能分配给设备，不能分配给主机，并且泛播地址不能作为报文的源地址。^

在RFC2373中预定义了一个泛播地址，称之为子网路由器的泛播地址。下图显示了子网路由器的泛播地址格式，这类地址由
子网前缀后面跟着一系列的0(作为接口标识符)组成。

其中子网前缀标识了一个指定的链路(子网)，送给子网路由器泛播地址的报文将被分发到在该子网上的一个设备。子网路由器
的泛播地址通常是被用于一个节点上的应用程序需要和远程子网的一个设备通信而使用。

图 3 - 8


配置指南 IPv6

**相关配置**

######  配置 IPv6 地址

 缺省情况接口没有配置IPv6地址。

 可通过ipv6 address命令配置接口IPv6单播地址和泛播地址。

 接口up之后将会自动加入相应的组播组。

###### 3.3.3 IPv6 包头结构

IPv6包头格式如下图：

图 3 - 9

在IPv4中，所有包头以 4 字节为单位。在IPv6中，包头以 8 字节为单位，包头的总长度是 40 字节。IPv6包头定义了以下字
段：

 版本(Version)：

长度为 4 位，对于IPv6该字段必须为 6 。

 类别(Traffic Class)：

长度为 8 位，指明为该包提供了某种服务，相当于IPv4中的“TOS”。


配置指南 IPv6

 流标签(Flow Label)：

长度为 20 位，用于标识属于同一业务流的包，一个节点可以同时作为多个业务流的发送源，流标签和源节点地址唯一标识了
一个业务流。

 净荷长度(Payload Length)：

长度为 16 位，其中包括包净荷的字节长度，同时也包含了各个IPv6扩展选项的长度(如果存在)，换句话说就是包含了除IPv6
头本身外的IPv6包的长度。

 下一个头(Next Header)：

这个字段指出了IPv6头后所跟的头字段中的协议类型。与IPv4协议字段类似，下一个头字段可以用来指出高层是TCP还是
UDP，它也可以用来指明IPv6扩展头的存在。

 跳数(Hop Limit)：

长度为 8 位。每当设备对包进行一次转发之后，这个字段就会被减 1 ，如果该字段达到 0 ，这个包就将被丢弃。它与IPv4包头
中的生存期字段类似。

 源地址(Source Address)：

长度为 128 位，指出了IPv6包的发送方地址。

 目的地址(Destination Address)：

长度为 128 位，指出了IPv6包的接收方地址。

IPv6的扩展头，目前IPv6定义了下列的扩展头：

 逐跳选项头(Hop-by-Hop Options)：

此扩展头必须紧随在IPv6头之后，它包含包所经过的路径上的每个节点都必须检查的选项数据。

 路由选项头（Routing （Type 0））：

此扩展头指明包在到达目的地途中将经过哪些节点，它包含包沿途经过的各节点的地址列表。IPv6头的最初目的地址是选路头
的一系列地址中的第一个地址，而不是包的最终目的地址。IPv6头部目的地址对应的节点接收到该包之后，对IPv6头和选路
头进行处理，并把包发送到选路头列表中的第二个地址，如此继续，直到包到达其最终目的地。

 分片头（Fragment）：

此扩展头用于源节点对长度超出源节点和目的节点路径MTU的包进行分片。

 目的地选项头（Destination Options）：

此扩展头代替了IPv4选项字段，目前唯一定义的目的地选项是在需要时把选项填充为6 4位（ 8 字节）的整数倍，此扩展头可
以用来携带由目的地节点检查的信息。

 上层扩展头(Upper-layer header)：

指明了上层传输数据的协议，如TCP(6)、UDP(17)。


配置指南 IPv6

此外还有身份验证头(Authentication )和封装安全性净荷(Encapsulating Security Payload )的扩展头，这将放到IPSec章节描
述。

**相关配置**

无

###### 3.3.4 IPv6 路径 MTU 发现

和IPv4的路径MTU发现类似，IPv6的路径MTU发现允许一台主机动态的发现并调整发送数据路径上的MTU的大小。另外，
当主机要发送的数据包的大小如果比发送数据路径上的MTU大时，那么将由主机自行负责分片。这种由主机分片的行为使得
设备无需处理分片从而节省了IPv6设备的资源，同时也提高了IPv6网络的效率。

图 3 - 10

```
MTU 1500 MTU 1480 MTU 1400
```

```
1500 字节的报文
发送ICMPv 6 报文太大消息，路径MTU 1480
```

```
1400 字节的报文
```

```
发送ICMPv 6 报文太大消息，路径MTU 1400
```

```
1480 字节的报文
```

如上图，当主机要发送的报文的长度比路径MTU大时，路由器丢弃报文，并且向主机发送一个ICMPv6报文太大消息，把MTU
告诉主机，然后主机根据新的路径MTU对报文进行分片。这种由主机分片的行为使得路由器不需要对报文进行分片从而节省
了路由器的资源，同时也提高了IPv6网络的效率。

**相关配置**

######  配置接口 IPv6 MTU

 以太网接口的默认IPv6 MTU是 1500 。

 可通过ipv6 mtu命令修改接口的IPv6 MTU值。


配置指南 IPv6

###### 3.3.5 IPv6 邻居发现

邻居发现协议是IPv6协议的一个基本的组成部分，它的主要功能有路由器发现、前缀发现、参数发现、地址自动配置、地址
解析（相当于ARP）、确定下一跳、邻居不可达检测、地址冲突检测和重定向。邻居发现定义了 5 种ICMP报文：“路由器请
求， ICMP类型为 133 ；路由器公告， ICMP类型为 134 ；邻居请求，相当于ARP请求，ICMP类型为 135 ；邻居公告，相
当于ARP应答，ICMP类型为 136 ；ICMP重定向报文，ICMP类型为 137 ”。

上述五种ICMP报文都会携带一个或者多个的选项，这些选项在某些情况下是可选，事实上，有些情况下选项实际上就是报文
的全部意义所在，邻居发现主要定义五种选项：“源链路层地址选项”，类型=1；“目标链路层地址选项”，类型=2；“前缀信息
选项”，类型=3；“重定向的首部选项”，类型=4；“MTU选项”类型=5；

######  地址解析

当一个节点要与另外一个节点通信时，那么该节点必须获取对方的链路层地址，此时就要向该节点发送邻居请求(NS)报文,报文
的目的地址是对应于目的节点的IPv6地址的被请求多播地址，发送的NS报文同时也包含了自身的链路层地址。当对应的节
点收到该邻居请求后发回一个响应的报文称之为邻居公告报文(NA)，其目的地址是邻居请求的源地址，内容为被请求的节点的
链路层的地址。当源节点收到该应答报文后就可以和目的节点进行通讯了。

下图是地址解析的过程：

图 3 - 11

######  邻居不可达检测

当一个邻居被认为可到达的时间到期以后，如果有IPv6单播报文需要发送给这个邻居，将执行邻居不可达检测 (Neighbor
Unreachability Detection)。

邻居不可达检测和向邻居发送IPv6报文可以同时进行，在检测过程中，继续向该邻居转发IPv6报文。

######  地址冲突检测

当给主机配置IPv6地址以后，想知道这个IPv6地址在链路上是不是唯一的，需要执行地址冲突检测，发送源IPv6地址是未
指定地址的邻居请求。

如果设备检测到地址冲突，该地址将被设置为冲突状态，设备将不能接收目的地址为该地址的ipv6报文，同时设备会为该冲突
的地址起一个定时器，定时进行地址冲突检测，如果重新检测没有冲突，该地址将可以正常使用。


配置指南 IPv6

######  路由器，前缀和参数发现

路由器公告报文(RA)在设备上是定期被发往链路本地所有节点的。

路由器公告报文发送如下图：

图 3 - 12

路由器公告报文中通常包含如下内容：

 一个或者多个IPv6地址前缀（用于on-link确定，或无状态地址自动配置）

 IPv6地址前缀的有效期。

 主机自动配置使用的方式(有状态还是无状态)。

 作为缺省设备的信息(即决定本设备是否要作为缺省设备，如果是那么还宣布自己充当缺省设备的时间)。

 提供给主机配置的一些其它信息如跳数限制、MTU、邻居请求重传间隔时间等。

路由器公告报文同时也用来应答主机发出的路由器请求(RS)报文，路由器请求报文允许主机一旦启动后可以立即获得自动配置
的信息而无需等待设备发出的路由器公告报文(RA)。当主机刚启动时如果没有单播地址，那么主机发出的路由器请求报文将使
用未指定地址(0:0:0:0:0:0:0:0)作为请求报文的源地址，否则使用已有的单播地址作为源地址，路由器请求报文使用本地链路所
有设备组播地址(FF02::2)作为目的地址。作为应答路由器请求(RS)报文的路由器公告(RA)报文将使用请求报文的源地址作为目
的地址(如果源地址是未指定地址那么将使用本地链路所有节点组播地址FF02::1)。

在路由器公告报文中下列参数是可以被配置的：

 Ra-interval 路由器公告报文的发送间隔。

 Ra-lifetime路由器生存期，即设备是否充当本地链路的缺省路由器以及充当该角色的时间。

 Prefix 本地链路的IPv6地址前缀，用于on-link确定，或无状态地址自动配置，包括前缀的其它参数配置。

 Ns-initerval 邻居请求报文重传的时间间隔。

 Reachabletime 检测到邻居可到达事件后认为邻居是可到达的所维持的时间。

 Ra-hoplimit路由器公告(RA)报文跳数的值，用于设置主机发送单播报文的hop-limit

 Ra-mtu路由器公告(RA)报文的MTU字段的值

 Maneged-config-flag 决定了收到该路由器公告的主机是否要使用全状态自动配置来获取地址

 Other-config-flag决定了收到该路由器公告的主机是否将使用dhcpv6来获取除IPv6地址以外的其他信息进行自动配置。


配置指南 IPv6

以上这些参数在IPv6接口属性中进行配置。

######  重定向

当路由器收到IPv6报文以后，发现存在更优的下一跳，就发送ICMP重定向报文把更优的下一跳告诉主机，下一次主机直接
把IPv6报文发给更优的下一跳。

######  未解析的邻居表项的最大数量

 为防止恶意扫描网段，生成大量的未解析邻居表项，占用过多的内存，可配置限制未解析的邻居表项的最大数量

######  处理 ND 选项最大数量

 为防止伪造ND报文携带无穷的ND选项，设备处理占用过多的CPU，可配置限制ND选项最大数量

######  接口邻居学习表项数量

 为防止邻居学习攻击，占用设备邻居表项，占用内存且影响转发性能，可配置限制接口邻居学习表项数量

**相关配置**

######  配置 IPv6 重定向

 缺省情况IPV6的接口上允许发送ICMPv6重定向报文

 可以使用接口配置模式命令“no ipv6 redirects”禁止接口发送重定向报文

######  配置 IPv6 地址冲突检测

 缺省情况接口上为IPV6地址执行地址冲突检测时会发送的 1 个邻居请求(NS)报文

 可以使用接口配置模式命令“ipv6 nd dad attempts value”配置DAD连续发送的NS报文个数， 0 表示阻止为该接口上
的Ipv6地址启动地址冲突检测

 使用“no ipv6 nd dad attempts”恢复默认配置

 缺省情况设备对已经冲突IPv6地址会定时执行地址冲突检测，时间间隔为60s

 可以使用全局配置模式命令“ipv6 nd dad retry value”配置重复地址冲突检测的时间间隔， 0 表示关闭设备进行重复冲
突地址检测功能。

 使用“no ipv6 nd dad retry”恢复默认配置

######  配置邻居可达时间

 缺省情况IPv6邻居默认可达时间为30s

 可以使用接口配置模式命令“ipv6 nd reachable-timemilliseconds”修改可达时间

######  配置邻居 stale 状态时间

 缺省情况IPv6邻居默认stale状态持续时间1h，到期后将进行邻居不可达检测


配置指南 IPv6

 可以使用接口配置模式命令“ipv6 nd stale-timeseconds”修改stale状态持续时间

######  配置前缀信息

 缺省情况RA公告的前缀是在该接口上通过ipv6 address命令配置的前缀

 可以使用接口配置模式命令“ipv6 nd prefix”添加或删除可公告的前缀及前缀参数

######  配置 RA 抑制功能

 缺省情况IPv6的接口上不会发送路由器公告报文

 可以使用接口配置模式命令“no ipv6 nd suppress-ra”关闭RA抑制功能

######  配置未解析的邻居表项的最大数量

 默认值为 0 ，表示不限制，即受限于设备支持的ND表项容量

 使用全局配置模式下命令ipv6 nd unresolved number限制未解析邻居数量，表项超过该限制后，将不为后续报文进行
主动解析

######  配置处理 ND 选项最大数量

 使用全局配置模式下命令ipv6 nd max-opt value限制处理邻居选项个数，默认值为 10

######  配置接口可学习邻居表项的数量

 使用接口配置模式下命令ipv6 nd cache interface-limitvalue限制接口可学习的邻居数量，默认值为 0 ，表示不限制

###### 3.3.6 IPv6 源路由

**工作原理**

IPv6报文通过路由首部被发送者用来指定报文经过哪些中间节点到达目的地址，类似于IPv4的宽松源路由选项和宽松记录路
由选项，格式为：

图 3 - 13

其中剩余段数用来指明报文从当前节点到最终目的地址，还需要经过多少个路由首部指明的中间节点，不包括路由首部没有列
出的中间节点。


配置指南 IPv6

目前定义了两种路由类型： 0 和 2 。类型 2 路由首部用于移动通信。RFC2460定义了类型 0 路由首部（类似于IPv4的宽松源
路由选项），格式如下图所示。

图 3 - 14

下面举例说明类型 0 路由首部的应用，如图 3 - 15 所示。

图 3 - 15

主机 1 发报文给主机 2 ，指明要经过路由器 2 和 3 ，转发过程中报文IPv6首部和路由首部的相关字段变化如下表所示：

传输节点 IPv6首部的相关字段 类型 0 路由首部的相关字段
主机 1 源地址=1000::2
目的地址=1001::1（路由器 2 的地址）

剩余段数=2
地址1=1002::1（路由器 3 的地址）
地址2=1003::2（主机 2 的地址）
路由器 1 无变化
路由器 2 源地址=1000::2 剩余段数=1


配置指南 IPv6

目的地址=1002::1（路由器 3 的地址） 地址1=1001::1（路由器 2 的地址）
地址2=1003::2（主机 2 的地址）
路由器 3 源地址=1000::2
目的地址=1003::2（主机 2 的地址）

剩余段数=0
地址1=1001::1（路由器 2 的地址）
地址2=1002::1（路由器 3 的地址）
主机 2 无变化

具体过程如下：

7. 主机 1 发出报文，目的地址是路由器 2 的地址1001::1，在类型 0 路由首部中填上路由器 3 的地址1002::1和主机 2 的地
   址1003::2，剩余段数是 2 。
8. 路由器 1 只是简单地把报文转发给路由器 2 。
9. 路由器 2 把IPv6首部的目的地址和路由首部的地址 1 交换，即现在目的地址是路由器 3 的地址1002::1，路由首部的地
   址 1 是路由器 2 的地址1001::1，剩余段数是 1 。修改完以后，路由器 2 把报文转发给路由器 3 。
10. 路由器 3 把IPv6首部的目的地址和路由首部的地址 2 交换，即现在目的地址是主机 2 的地址1003::2，路由首部的地址
    2 是路由器 3 的地址1002::1，剩余段数是 0 。修改完以后，路由器 3 把报文转发给主机 2 。

类型 0 路由首部有可能被利用进行拒绝服务攻击，如下图所示，主机 1 以1Mbps的速度向主机 2 发报文，故意构造一个路由
首部，使报文在路由器 2 和路由器 3 之间多次往返，从路由器 2 到路由器 3 走 50 次，从路由器 3 到路由器 2 走 49 次，这时
路由首部产生流量放大效应：“路由器 2 到路由器 3 方向的流量为50Mbps，路由器 3 到路由器 2 方向的流量为49Mbps”。由
于存在这个安全问题，RFC5095废除了类型 0 路由首部。

图 3 - 16

**相关配置**

######  配置 IPv6 源路由


配置指南 IPv6

 缺省情况不支持类型 0 路由首部

 可以使用全局配置模式命令“ipv6 source-route”打开这项功能

###### 3.3.7 控制 ICMPv6 差错报文的发送速率

**工作原理**

ICMPv6差错报文是由目标节点或者中间路由器发送，用于报告在转发和传送IPv6数据包过程中出现的错误。主要包括下面四
种类型的差错报文：目标不可达（Destination unreachable）、报文太大（Packet too big）、超时（Time exceeded）、参数问
题（Parameter problem）。

往设备发送非法IPv6报文，设备会丢弃这些报文，并向源IPv6地址发送相应的ICMPv6差错报文。如果受到IPv6非法报文
攻击，可能出现设备一直在应答ICMPv6差错报文而耗尽设备资源，这样设备将不能正常提供服务，针对这种攻击，可以对
ICMPv6差错报文的发送速率进行限制。

如果转发的IPv6报文的长度超过出口的IPv6 MTU，路由器会丢弃IPv6报文，并且向源IPv6地址发送ICMPv6报文太大消息，
这种ICMPv6差错报文的主要用途是IPv6路径MTU发现。为了防止其它ICMPv6差错报文太多而将ICMPv6报文太大消息限
速过滤掉，从而导致IPv6路径MTU发现功能失效，对ICMPv6报文太大消息和其它ICMPv6差错报文分别限速。

ICMPv6重定向报文不属于ICMPv6差错报文，我司把ICMPv6重定向报文和其它ICMPv6差错报一起限速。

**相关配置**

######  配置 ICMPv6 报文太大消息的发送速率

 缺省速率是 100 毫秒 10 个。

 可通过ipv6icmp error-interval too-big配置发送速率。

######  配置其它 ICMPv6 差错报文的发送速率

 缺省速率是 100 毫秒 10 个。

 可通过ipv6icmp error-interval配置发送速率。

###### 3.3.8 IPv6 HOP-LIMIT

**工作原理**

IPv6数据包从源地址向目的地址经过路由器间传播，设置一个hop-limit数值，每过一个路由器hop-limit值就减一，当减到零
的时候，路由器就把这个包丢掉，这样可以防止无用的包在网络上无限传播下去，浪费网络带宽。其功能类似于IPv4的TTL。

**相关配置**

######  设置 IPv6 hop-limit


配置指南 IPv6

 缺省情况设备IPv6 HOP-LIMIT为 64 。

 可通过ipv6 hop-limit设置设备的IPv6 HOP-LIMIT值。

###### 3.3.9 抑制往认证 vlan 发送广播邻居请求（ NS ）报文

**工作原理**

在网关认证模式下，SuperVLAN下的所有子VLAN默认都是认证VLAN，认证VLAN下的认证用户需要在认证后才能上网。
用户认证后会在设备上生成静态ND表项，因此设备访问认证用户时，不需要往认证VLAN发送NS请求。若设备需要访问免
认证VLAN下的用户时，只需要往免认证VLAN发送ARP请求。

在网关认证模式下，设备默认开启了抑制往认证VLAN发送NS请求的功能。如果设备需要访问认证VLAN下的非认证用户，
需要关闭该功能。

**相关配置**

######  设置抑制往认证 vlan 发送广播 NS 报文

 接口模式下，使用命令ipv6 nd suppress-auth-vlan-ns开启抑制往认证VLAN发送NS请求功能。

 缺省情况下开启抑制往认证VLAN发送NS请求功能。

 只支持在SVI接口上配置，且只有网关认证模式下才生效

###### 3.3.10 MGMT 接口支持缺省网关

**工作原理**

给MGMT口配置缺省网关，为MGMT口生成一条默认路由。

**相关配置**

######  设置 MGMT 口的缺省网关

 接口模式下，使用命令ipv6 gateway ipv6-address配置MGMT口的缺省网关。

 缺省情况下，MGMT口没有配置缺省网关


配置指南 IPv6

#### 3.4 配置详解

配置项 配置建议&相关命令

配置IPv6地址

### 必须配置，用于配置ipv6地址，启用IPv6协议。^

```
ipv6 enable 打开接口的IPv6协议
ipv6 address 配置接口IPv6的单播地址
```

配置IPv6邻居发现

### 可选配置，用于限制接口IPv6重定向功能。^

```
ipv6 redirects 打开该接口的IPv6重定向功能
```

### 可选配置，用于设置DAD检测。^

```
ipv6 nd dad attempts 配置冲突检测时要连续发送的邻居请求(NS)报文的数量。
```

### 可选配置，用于设置邻居发现的各种参数。^

```
ipv6 nd reachable-time 设置邻居被认为可到达的时间
ipv6 nd prefix 设置路由器公告(RA)报文中所要公告的地址前缀
ipv6 nd suppress-ra 设置是否在该接口上阻止路由器公告（RA）报文发送
```

### 可选配置，用于设置未解析邻居的最大数量。^

```
ipv6 nd unresolved 设置未解析邻居的最大数量
```

### 可选配置，用于设置处理ND报文的选项最大数量^

```
ipv6 nd max-opt 设置处理ND选项最大数量
```

### 可选配置，用于限制接口可学习的邻居数量^

```
ipv6 nd cache interface-limit 设置接口可学习邻居数量
```

### 配置路径MTU发现

```
可选配置，用于限制接口发送IPv6报文的mtu。
ipv6 mtu 设置IPv6 MTU值
```

### 配置IPv6源路由

```
可选配置，用于开启支持IPv6源路由功能。
ipv6 source-route 配置设备转发带有路由首部的IPv6报文。
```

配置ICMPv6差错报文的发送
速率

### 可选配置。^

```
ipv6 icmp error-interval
too-big 配置ICMPv6报文太大消息的发送速率。^
ipv6 icmp error-interval
配置其它ICMPv6差错报文和ICMPv6重定向报文的发送速
率。
```

### 配置设备IPv6 HOP-LIMIT

```
可选配置，用于限制接口发送IPv6单播报文的可转发跳数。
ipv6 hop-limit 设置IPv6 HOP-LIMIT值。
```

配置指南 IPv6

配置抑制往认证vlan发送广
播NS报文

### 可选配置，用于网关认证模式下，抑制往免认证vlan发送广播ns报文。^

```
ipv6 nd
suppress-auth-vlan-ns
设置抑制往免认证vlan发送广播ns报文。
```

### 配置MGMT口缺省网关

```
可选配置，用于给mgmt口配置缺省网关。
ipv6 gateway ipv6-address 设置mgmt口的缺省网关。
```

###### 3.4.1 配置 IPv6 地址

**配置效果**

通过配置接口IPv6地址实现IPv6网络通信。

**注意事项**

无

**配置方法**

######  打开接口的 IPv6 协议

 可选配置，若不想通过配置IPv6地址来开启接口IPv6协议，则必须配置ipv6 enable来开启接口IPv6功能。

######  配置接口 IPv6 的单播地址

 必须配置。

**检验方法**

通过show ipv6 interface可以看到配置的地址生效

**相关命令**

######  打开接口的 IPv6 协议

```
【命令格式】 ipv6 enable
【参数说明】 -
【命令模式】 接口模式
【使用指导】 有 2 种方式可以打开接口上的 IPv6功能，一是在接口下配置ipv6 enable命令，二是直接在接口下配置了IPv6
地址。
```

### 如果接口已经被绑定到没有配置IPv6地址族的多协议VRF，那么不允许在接口上打开IPv6功能，必须


配置指南 IPv6

```
先给多协议VRF配置IPv6地址族，然后才能在接口上打开IPv6功能。
如果在接口上配置了IPv6地址那么接口的IPv6功能就会自动打开，即使使用no ipv6 enable也不能关闭IPV6
功能。
```

######  配置接口 IPv6 的单播地址

```
【命令格式】 ipv6 addressipv6-address/prefix-length
ipv6 addressipv6-prefix/prefix-lengtheui- 64
ipv6 addressprefix-name sub-bits/prefix-length [eui- 64 ]
【参数说明】 ipv6-address：IPV6地址，必须遵循RFC4291定义的地址形式，每个地址域之间用冒号隔开，每个域占 16
比特，用十六进制数表示.
ipv6-prefix：IPV6 地址前缀，必须遵循RFC4291定义的地址形式，每个地址域之间用冒号隔开，每个域占
16 比特，用十六进制数表示.
prefix-length：IPV6前缀的长度即IPV6地址中代表网络的部分。
prefix-name：通用前缀的名字。使用这个指定的通用前缀生成接口地址。
sub-bits：子前缀比特与主机比特的值。这个值与通用前缀中的前缀合并生成接口地址。这个值的表示法要遵
循RFC4291描述的冒号表示法。
eui- 64 ：表示生成的IPV6地址由配置的地址前缀和 64 比特的接口ID标识符组成。
【命令模式】 接口模式
【使用指导】
```

### 如果接口已经被绑定到没有配置IPv6地址族的多协议VRF，那么不允许给接口配置IPv6地址，必须先

```
给多协议VRF配置IPv6地址族，然后才能给接口配置IPv6地址。^
当一个IPV6接口被创建并且链路状态为UP时那么系统将为该接口自动生成链路本地地址。
接口的IPv6地址也可以使用通用前缀机制生成。其机制就是IPv6地址=“通用前缀”+“子前缀”+“主机比
特”。通用前缀可以使用ipv6 general-prefix命令配置，也可能通过DHCPv6客户端的PD(前缀发现)功能学
习到(参见DHCPv6配置指南)。“子前缀”+“主机比特”就是使用本命令的sub-bits/prefix-length参数配置。
使用no ipv6 address如果不指定删除具体的地址，那么将删除所有手工配置的地址。
使用no ipv6 addressipv6-prefix/prefix-lengtheui- 64 可 以 删 除 使 用 命 令 ipv6
addressipv6-prefix/prefix-lengtheui- 64 配置的地址。
```

**配置举例**

######  给接口配置 IPv6 地址

【配置方法】 在接口GigabitEthernet 0/0开启IPv6协议，并添加ipv6地址2000::1
Ruijie(config)#interface gigabitEthernet 0/0
Ruijie(config-if-GigabitEthernet 0/0)#ipv6 enable
Ruijie(config-if-GigabitEthernet 0/0)#ipv6 address 2000::1/64
【检验方法】 使用show ipv6 interface可以看到接口GigabitEthernet 0/0添加地址成功
Ruijie(config-if-GigabitEthernet 0/0)#show ipv6 interface gigabitEthernet 0/0

```
interface GigabitEthernet 0/0 is Down, ifindex: 1, vrf_id 0
```

配置指南 IPv6

```
address(es):
Mac Address: 00:00:00:00:00:00
INET6: FE80::200:FF:FE00:1 [ TENTATIVE ], subnet is FE80::/64
INET6: 2000::1 [ TENTATIVE ], subnet is 2000::/64
Joined group address(es):
MTU is 1500 bytes
ICMP error messages limited to one every 100 milliseconds
ICMP redirects are enabled
ND DAD is enabled, number of DAD attempts: 1
ND reachable time is 30000 milliseconds
ND advertised reachable time is 0 milliseconds
ND retransmit interval is 1000 milliseconds
ND advertised retransmit interval is 0 milliseconds
ND router advertisements are sent every 200 seconds<160--240>
ND router advertisements live for 1800 seconds
```

**常见错误**

无

###### 3.4.2 配置路径 MTU 发现

**配置效果**

本地发送IPv6报文时根据路径MTU分片。

**注意事项**

接口IPv6 MTU的配置范围受接口MTU限制，最大值是接口MTU。

**配置方法**

######  设置接口 IPv6 MTU 值

 可选配置。

**检验方法**

 通过show run命令查看配置是否正确。

 通过show ipv6 interface命令查看接口IPv6 MTU配置是否正确。


配置指南 IPv6

**相关命令**

######  设置接口 IPv6 MTU 值

```
【命令格式】 ipv6 mtu bytes
【参数说明】 bytes：IPv6包最大传输单元，以字节为单位，范围 1280 ~1 500 。
【命令模式】 接口模式
【使用指导】 -^
```

**配置举例**

######  配置接口 IPv6 MTU

【配置方法】 修改接口IPv6 MTU为 1300 。
Ruijie(config-if-GigabitEthernet 0/0)#ipv6 mtu 1300
【检验方法】 通过show ipv6 interface查看配置是否生效。
Ruijie(config-if-GigabitEthernet 0/ 0 )#show ipv6 interface

```
interface GigabitEthernet 0/ is Down, ifindex: 1 , vrf_id 0
address(es):
Mac Address: 00:d0:f8:22:33:47
INET6: FE80::2D0:F8FF:FE22:3347 [ TENTATIVE ], subnet is FE80::/64
INET6: 1020::1 [ TENTATIVE ], subnet is 1020::/64
INET6: 1023::1 [ TENTATIVE ], subnet is 1023::/64
Joined group address(es):
MTU is 1300 bytes
ICMP error messages limited to one every 100 milliseconds
ICMP redirects are enabled
ND DAD is enabled, number of DAD attempts: 1
ND reachable time is 30000 milliseconds
ND advertised reachable time is 0 milliseconds
ND retransmit interval is 1000 milliseconds
ND advertised retransmit interval is 0 milliseconds
ND router advertisements are sent every 200 seconds<160--240>
ND router advertisements live for 1800 seconds
```

**常见配置错误**

无


配置指南 IPv6

###### 3.4.3 配置 IPv6 邻居发现

**配置效果**

配置ND协议相关属性，比如配置ipv6重定向功能，配置DAD检测等。

**注意事项**

接口默认是抑制发送RA报文，要设备能够发送RA报文必须在接口模式下配置no ipv6 nd suppress-ra。

**配置方法**

######  打开该接口的 IPv6 重定向功能

 可选配置，缺省已开启。

 当需要关闭接口IPv6重定向功能时，使用“no ipv6 redirects”。

######  配置冲突检测时要连续发送的邻居请求 (NS) 报文的数量

 可选配置。

 如果需要阻止为该接口上的Ipv6地址启动地址冲突检测或者修订DAD连续发送邻居请求(NS)报文个数，可使用该配置。

######  设置邻居被认为可到达的时间

 可选配置。

 如果需要修改邻接可达时间，可使用该配置。

######  设置路由器公告 (RA) 报文中所要公告的地址前缀

 缺省情况RA公告的前缀是在该接口上通过ipv6 address命令配置的前缀

######  设置是否在该接口上阻止路由器公告（ RA ）报文发送

 可选配置。

 如果需要设备能发送路由器公告，可使用该命令来配置。

######  配置未解析的邻居表项的最大数量

 可选配置。

 如果设备受到扫描攻击而创建大量未解析邻居表项，消耗表项资源，可以使用该命令限制未解析邻居的数量。

######  配置处理 ND 选项最大数量

 可选配置

 如果环境要求设备能够处理更多的选项内容，可使用该命令来配置。


配置指南 IPv6

######  配置接口可学习邻居表项的数量

 可选配置

 如果环境中IPv6主机数可控制，可以使用该功能限制接口的学习邻居个数，防止网络中进行ND学习攻击，使得设备学
习表项占用内存影响性能。

**检验方法**

通过以下命令查看配置是否正确：

 show ipv6 interface interface-type interface-num 可查看接口重定向功能，邻居可达时间、邻居请求发送间隔等信息是
否配置生效

 show ipv6 interface interface-type interface-num ra-inifo可查看路由器公告配置的前缀及其他信息是否正确

 show run

**相关命令**

######  打开该接口的 IPv6 重定向功能

```
【命令格式】 ipv6 redirects
【参数说明】 -^
【命令模式】 接口模式
【使用指导】 所有ICMPv6的错误报文的数据包传输速率是有限制的，缺省每秒钟最多可以发送 10 个错误ICMPv6错误报
文(10pps)。
```

######  配置冲突检测时要连续发送的邻居请求 (NS) 报文的数量

```
【命令格式】 ipv6 nd dad attempts value
【参数说明】 value：邻居请求(NS)报文的数量
【命令模式】 接口模式
【使用指导】 当在接口上配置一个新的IPV6地址前要为它启动地址冲突检测，此时该地址处于”tentative”（试验）的状态。
地址冲突过程执行完了，如果没有检测到冲突，那么该地址就可以被正确使用，如果检测到冲突了，并且该地
址所使用的接口标识符是使用EUI- 64 的标识符，那么表明在该链路上存在链路层地址出现重复，那么此时系
统会自动关闭该接口（即阻止在该接口上进行IPV6的相关操作），此时必须手工去修改并配置新的地址，并
通过再次down/up接口重新启动地址冲突检测。任何情况下当一个接口从down状态变为up状态时都会为该
接口上的地址重新启动地址冲突检测。
```

######  设置邻居被认为可到达的时间

```
【命令格式】 ipv6 nd reachable-timemilliseconds
【参数说明】 milliseconds：邻居被认为可到达的时间，以毫秒为单位，范围： 0 - 3600000 。缺省为 30 秒。
【命令模式】 接口模式
【使用指导】 设备通过该配置的时间来检测不可用的邻居，所设置的时间越短意味着可以更快的检测到邻居失效，但是将浪
费更多的网络带宽、消耗设备更多的资源。因此不建议将该时间配置的过小。
```

配置指南 IPv6

```
配置的值将在路由器公告报文(RA)中被发布出去，同时该值也被设备自身使用。如果设置的值为 0 表示设备
未指定该时间，即使用缺省值。
```

######  设置路由器公告 (RA) 报文中所要公告的地址前缀

```
【命令格式】 ipv6 nd prefix {ipv6-prefix/prefix-length | default} [[valid-lifetime {infinite | preferred-lifetime } ] | [at
valid-datepreferred-date] | [infinite{infinite | preferred-lifetime}]] [no-advertise] | [[ off-link ]
[no-autoconfig ]]
【参数说明】 ipv6-prefix：IPV6的网络号，必须遵循RFC4291的地址表示形式。
prefix-length：IPV6前缀的长度，注意前面必须加上’/’。
valid-lifetime：主机收到路由器公告的前缀后认为有效的时间，取值范围 0 - 4294967295 。缺省 30 天。
preferred-lifetime：主机收到路由器公告的前缀后认为首选有效的时间，取值范围 0 - 4294967295 ，缺省 7 天。
atvalid-date preferred-date：设置公告前缀有效和首选有效的截止时间，截止时间是以日、月、年、小时、分
钟表示的。
infinite：表示永远都有效。
default：设置要使用的缺省参数配置。
no-advertise：表示该前缀不被路由器公告。
off-link：主机在发送IPV6报文时如果目的地址的前缀匹配前缀那么认为该目的地是在同一链路(on-link)上是
可直接到达的。设置了该选项表示该前缀不用来做on-link的判断。
no-autoconfig：该选项指示主机收到该路由器公告中的前缀不能用于地址自动配置。
【命令模式】 接口模式
【使用指导】 通过该命令可以分别配置每一个前缀的各个参数，包括是否要公告该前缀，缺省情况下路由器公告报文中(RA)
公告的前缀是在该接口上通过ipv6 address命令配置的前缀，如果要增加其它前缀可以使用该命令进行配置。
ipv6 nd prefix default 设置该接口上使用的缺省配置参数，即新增加一个前缀时，如果没有指定任何参数，
那么将使用ipv6 nd prefix default所设置的参数做为配置的前缀的参数。注意一旦为该前缀指定了某个参数
以后将不再认为使用缺省参数配置。即以后使用ipv6 nd prefix default 改变缺省参数配置时不会去修改该前
缀的配置，而只修改完全使用缺省参数配置的前缀。
at valid-datepreferred-date前缀的有效时间有 2 种指定方式：一种是在公告报文中每个前缀指定一个固定的
时间；另外一种是指定截止时间，使用该方式那么每次发出去的公告报文中的前缀的有效时间将采用递减的方
式，直到值为 0 。
```

######  设置是否在该接口上阻止路由器公告（ RA ）报文发送

```
【命令格式】 ipv6 nd suppress-ra
【参数说明】 -
【命令模式】 接口模式
【使用指导】 当要在一个接口上抑制路由器公告报文发送时可以使用ipv6 suppress-ra命令
```

######  设置未解析的邻居表项的最大数量

```
【命令格式】 ipv6 nd unresolved number
【参数说明】 number：表示未解析邻居表项限制数
【命令模式】 全局模式
【使用指导】 为了防止恶意扫描攻击导致生成大量未解析的ND表项，占用表项资源，可以通过配置限制未解析的ND表项
```

配置指南 IPv6

```
的个数。
```

######  设置可处理 ND 选项数量

```
【命令格式】 ipv6 nd max-optvalue
【参数说明】 value：支持的选项个数
【命令模式】 全局模式
【使用指导】 配置设备处理ND选项数量限制，比如链路层地址选项，MTU选项，重定向选项，前缀选项。
```

######  设置接口可学习邻居表项数量

```
【命令格式】 ipv6 nd cache interface-limitvalue
【参数说明】 value：接口所能学习的邻居最大限制
【命令模式】 接口模式
【使用指导】 限制接口的邻居学习数量，可防止恶意的邻居攻击，让设备生成大量的邻居表项，占用过多的内存。配置的值
必须不小于当前接口已经学习到的邻居数，否则配置不生效。该限制受限于设备支持ND容量。
```

**配置举例**

######  打开接口的 IPv6 重定向功能

【配置方法】 开启接口IPv6重定向功能。
Ruijie(config-if-GigabitEthernet 0/0)#ipv6 redirects
【检验方法】 通过show ipv6 interface查看配置是否生效。
Ruijie#show ipv6 interface gigabitEthernet 0/0

```
interface GigabitEthernet 0/0 is Down, ifindex: 1, vrf_id 0
address(es):
Mac Address: 00:00:00:00:00:00
INET6: FE80::200:FF:FE00:1 [ TENTATIVE ], subnet is FE80::/64
Joined group address(es):
MTU is 1500 bytes
ICMP error messages limited to one every 100 milliseconds
ICMP redirects are enabled
ND DAD is enabled, number of DAD attempts: 1
ND reachable time is 30000 milliseconds
ND advertised reachable time is 0 milliseconds
ND retransmit interval is 1000 milliseconds
ND advertised retransmit interval is 0 milliseconds
ND router advertisements are sent every 200 seconds<160--240>
ND router advertisements live for 1800 seconds
```

######  配置 IPv6 地址冲突检测

【配置方法】 配置DAD检测要连续发送 3 个NS报文。


配置指南 IPv6

Ruijie(config-if-GigabitEthernet 0/0)# ipv6 nd dad attempts 3
【检验方法】 通过show ipv6 interface查看配置是否生效。
Ruijie#show ipv6 interface gigabitEthernet 0/0

```
interface GigabitEthernet 0/0 is Down, ifindex: 1, vrf_id 0
address(es):
Mac Address: 00:00:00:00:00:00
INET6: FE80::200:FF:FE00:1 [ TENTATIVE ], subnet is FE80::/64
Joined group address(es):
MTU is 1500 bytes
ICMP error messages limited to one every 100 milliseconds
ICMP redirects are enabled
ND DAD is enabled, number of DAD attempts: 3
ND reachable time is 30000 milliseconds
ND advertised reachable time is 0 milliseconds
ND retransmit interval is 1000 milliseconds
ND advertised retransmit interval is 0 milliseconds
ND router advertisements are sent every 200 seconds<160--240>
ND router advertisements live for 1800 seconds
Ruijie(config-if-GigabitEthernet 0/0)#
```

######  手工配置路由器公告的前缀信息

【配置方法】 为接口添加一个前缀1234::/64。
Ruijie(config-if-GigabitEthernet 0/0)#ipv6 nd prefix 1234::/6
【检验方法】 通过show ipv6 interface查看配置是否生效。
Ruijie#show ipv6 interface gigabitEthernet 0/0 ra-info

```
GigabitEthernet 0/0: DOWN (RA is suppressed)
RA timer is stopped
waits: 0, initcount: 0
statistics: RA(out/in/inconsistent): 0/0/0, RS(input): 0
Link-layer address: 00:00:00:00:00:00
Physical MTU: 1500
ND router advertisements live for 1800 seconds
ND router advertisements are sent every 200 seconds<160--240>
Flags: !M!O, Adv MTU: 1500
ND advertised reachable time is 0 milliseconds
ND advertised retransmit time is 0 milliseconds
ND advertised CurHopLimit is 64
Prefixes: <total: 1>
1234::/64(Def, CFG, vltime: 2592000, pltime: 604800, flags: LA)
```

配置指南 IPv6

######  配置路由器公告的前缀从前缀池获取

【配置方法】 配置路由器公告的前缀从前缀池“ra-pool”获取
Ruijie(config-if-GigabitEthernet 0/0)#peel default ipv6 pool ra-pool
【检验方法】 通过show run查看配置是否生效。
Ruijie(config-if-GigabitEthernet 0/0)#show run interface gigabitEthernet 0/0

```
Building configuration...
Current configuration : 125 bytes
```

```
interface GigabitEthernet 0/0
ipv6 enable
no ipv6 nd suppress-ra
peel default ipv6 pool ra-pool
!
```

######  配置关闭路由器公告抑制功能

【配置方法】 关闭接口抑制路由器公告功能
Ruijie(config-if-GigabitEthernet 0/0)# no ipv6 nd suppress-ra
【检验方法】 通过show run 查看配置是否生效。
Ruijie(config-if-GigabitEthernet 0/0)#show run interface gigabitEthernet 0/0

```
Building configuration...
Current configuration : 125 bytes
```

```
interface GigabitEthernet 0/0
ipv6 enable
no ipv6 nd suppress-ra
!
```

######  配置未解析的邻居表项的最大数量

【配置方法】 配置未解析的邻居表项的最大数量为 200
Ruijie(config)# ipv6 nd unresolved 200
【检验方法】 通过show run 查看配置是否生效。
Ruijie#show run^

```
ipv6 nd unresolved 200
!
```

######  配置可处理 ND 选项数量

【配置方法】 配置可处理ND选项数量为 20
Ruijie(config)# ipv6 nd max-opt20


配置指南 IPv6

【检验方法】 通过show run 查看配置是否生效。
Ruijie#show run

```
ipv6 nd max-opt20
!
```

######  配置接口可学习邻居表项数量

【配置方法】 配置接口可学习邻居表项数量 100
Ruijie(config-if-GigabitEthernet 0/1)# ipv6nd cache interface-limit 1 00
【检验方法】 通过show run 查看配置是否生效。
Ruijie#show run
!
interface GigabitEthernet 0/ 1
ipv6nd cache interface-limit 1 00
!

**常见配置错误**

无

###### 3.4.4 配置 IPv6 源路由

**配置效果**

RFC5095废除了类型 0 路由首部。锐捷的解决方法是缺省情况不支持类型 0 路由首部，管理员可以使用全局配置模式命令“ipv6

###### source-route”打开这项功能。

**注意事项**

无

**配置方法**

######  配置设备转发带有路由首部的 IPv6 报文

 可选配置。

 如果需要开启IPv6源路由功能，可使用该配置。


配置指南 IPv6

**检验方法**

向设备发送带有 0 路由首部的报文，设备能够正常转发。

**相关命令**

######  配置设备转发带有路由首部的 IPv6 报文

```
【命令格式】 ipv6 source-route
【参数说明】 -
【命令模式】 全局模式
【使用指导】 因为类型 0 路由首部有安全隐患：使设备很容易遭受拒绝服务攻击，所以在缺省情况下禁止转发带有路由首
部的IPv6报文，但是仍然处理最终目的地址是本机的带有类型 0 路由首部的IPv6报文。
```

**配置举例**

######  配置支持 IPv6 类型 0 路由。

【配置方法】 开启支持IPv6类型 0 路由功能。
Ruijie(config)#ipv6 source-route
【检验方法】 使用show run 查看配置是否生效。
Ruijie#show run | inc ipv6 source-route
ipv6 source-route

**常见配置错误**

无

###### 3.4.5 配置 ICMPv6 差错报文的发送速率

**配置效果**

###### 配置ICMPv6差错报文的发送速率。

**注意事项**

-

**配置方法**


配置指南 IPv6

######  配置 ICMPv6 报文太大消息的发送速率

 可选配置。

 如果设备收到大量IPv6报文的长度超过出口的IPv6 MTU，并因发送ICMPv6报文太大消息而消耗较大CPU的情况，可
以使用该配置限制该差错报文的发送。

######  配置其它 ICMPv6 差错报文的发送速率

 可选配置。

 如果设备收到大量非法IPv6报文，并因此而产生大量ICMPv6差错报文时，可以使用该配置限制差错报文发送速率（该
命令不会影响ICMPv6报文太大差错报文的发送速率）

**检验方法**

执行show running-config可以看到配置生效。

**相关命令**

######  配置 ICMPv6 报文太大消息的发送速率

```
【命令格式】 ipv6 icmp error-interval too-big milliseconds [bucket-size]
【参数说明】 milliseconds：令牌桶的刷新周期，取值范围0~2147483647，缺省值为 100 ，单位为毫秒。取值为 0 时，表
示不限制ICMPv6 差错报文的发送速率。
bucket-size：令牌桶中容纳的令牌数，取值范围1~200，缺省值为 10 。
【命令模式】 全局模式
【使用指导】 为了防止拒绝服务攻击，对ICMPv6差错报文的发送速率进行限制，采用令牌桶算法。
如果转发的IPv6报文的长度超过出口的IPv6 MTU，路由器会丢弃IPv6报文，并且向源IPv6地址发送ICMPv6
报文太大消息，这种ICMPv6差错报文的主要用途是IPv6路径MTU发现。为了防止其它ICMPv6差错报文
太多导致发不出ICMPv6报文太大消息，从而导致IPv6路径MTU发现功能失效，对ICMPv6报文太大消息
和其它ICMPv6差错报文分别限速。
因为定时器的精度是 10 毫秒，建议用户把令牌桶的刷新周期配置成 10 毫秒的整数倍。如果令牌桶的刷新周
期大于,0小于 10 ，实际生效的刷新周期是 10 毫秒，例如配置 5 毫秒 1 个，实际效果是 10 毫秒 2 个；如果令
牌桶的刷新周期不是 10 毫秒的整数倍，实际生效的刷新周期自动换算成 10 毫秒的整数倍，例如配置 15 毫秒
3 个，实际效果是 10 毫秒 2 个。
```

######  配置其它 ICMPv6 差错报文的发送速率

```
【命令格式】 ipv6 icmp error-interval milliseconds [bucket-size]
【参数说明】 milliseconds：令牌桶的刷新周期，取值范围0~2147483647，缺省值为 100 ，单位为毫秒。取值为 0 时，表
示不限制ICMPv6 差错报文的发送速率。
bucket-size：令牌桶中容纳的令牌数，取值范围1~200，缺省值为 10 。
【命令模式】 全局模式
【使用指导】 为了防止拒绝服务攻击，对ICMPv6差错报文的发送速率进行限制，采用令牌桶算法。
```

配置指南 IPv6

```
因为定时器的精度是 10 毫秒，建议用户把令牌桶的刷新周期配置成 10 毫秒的整数倍。如果令牌桶的刷新周
期大于,0小于 10 ，实际生效的刷新周期是 10 毫秒，例如配置 5 毫秒 1 个，实际效果是 10 毫秒 2 个；如果令
牌桶的刷新周期不是 10 毫秒的整数倍，实际生效的刷新周期自动换算成 10 毫秒的整数倍，例如配置 15 毫秒
3 个，实际效果是 10 毫秒 2 个。
```

**配置举例**

######  配置 ICMPv6 差错报文的发送速率

【配置方法】 配置ICMPv6报文太大消息的发送速率为 1 秒 100 个，配置其它ICMPv6差错报文的发送速率为 1 秒 10 个。
Ruijie(config)#ipv6 icmp error-interval too-big 1000 100
Ruijie(config)#ipv6 icmp error-interval 1000 10
【检验方法】 执行show running-config可以看到配置生效。
Ruijie#show running-config| include ipv6 icmp error-interval
ipv6 icmp error-interval 1000 10
ipv6 icmp error-interval too-big 1000 100

**常见配置错误**

无

###### 3.4.6 配置 IPv6 HOP-LIMIT

**配置效果**

配置发送单播报文的跳数，避免报文在网络上无限传播下去。

**注意事项**

-

**配置方法**

######  设置 IPv6 HOP-LIMIT 值

 可选配置

 如果需要修订单播报文的转发跳数，可以使用该配置

**检验方法**


配置指南 IPv6

 通过show running-config命令查看配置是否正确。

 本地发送ipv6单播报文，抓包可以看到ipv6首部的hop-limit字段值与配置的一致。

**相关命令**

######  设置 IPv6 HOP-LIMIT 值

```
【命令格式】 ipv6 hop-limit value^
【参数说明】 value：设备发送单播报文的跳数值，范围 1 ~ 255 。
【命令模式】 全局模式
【使用指导】 -
```

**配置举例**

######  配置 IPv6 HOP-LIMIT

【配置方法】 修改设备IPv6 HOP-LIMIT为 250 。
Ruijie(config)#ipv6 hop-limit 250
【检验方法】 通过show running-config查看配置是否生效。
Ruijie#show running-config
ipv6 hop-limit 254

**常见配置错误**

无

###### 3.4.7 配置抑制往认证 vlan 发送广播邻居请求（ NS ）报文

**配置效果**

抑制在SVI口上往认证vlan发送广播邻居请求（NS）报文。

**注意事项**

只支持SVI口配置，且在网络认证模式下才生效。

**配置方法**

######  配置抑制往免认证 vlan 发送广播 NS 报文

 可选配置


配置指南 IPv6

 网关认证模式下，如果希望设备能往认证vlan发送广播NS报文，可使用该配置

**检验方法**

 通过show running-config命令查看配置是否正确。

**相关命令**

######  设置抑制往免认证 vlan 发送广播 NS 报文

```
【命令格式】 ipv6 nd suppress-auth-vlan-ns
【参数说明】 -
【命令模式】 接口模式
【使用指导】 使用改命令的no形式，可以关闭该功能。
```

**配置举例**

######  配置关闭抑制往免认证 vlan 发送广播 NS 报文

【配置方法】 配置关闭抑制往免认证vlan发送广播ns报文。
Ruijie(config-if-VLAN 2)#no ipv6 nd suppress-auth-vlan-ns
【检验方法】 通过show running-configinterface vlan 2查看配置是否生效。
Ruijie#show running-config interface vlan 2
no ipv6 nd suppress-auth-vlan-ns

**常见配置错误**

无

###### 3.4.8 配置 MGMT 口缺省网关

**配置效果**

配置mgmt口缺省网关，生成一条默认路由出口是mgmt口，下一跳是配置的网关。

**注意事项**

MGMT口才支持。

**配置方法**


配置指南 IPv6

######  配置 MGMT 口缺省网关

 可选配置

 如果需要为MGMT配置一条默认路由并指定下一跳，可以使用该配置

**检验方法**

 通过show running-config命令查看配置是否正确。

**相关命令**

######  设置 MGMT 口缺省网关

```
【命令格式】 ipv6 gataway ipv6-address
【参数说明】 -^
【命令模式】 接口模式
【使用指导】 只在MGMT口支持
```

**配置举例**

######  配置 MGMT 口缺省网关为 2000::1

【配置方法】 配置MGMT口缺省网关为2000::1。

(^) Ruijie(config)# interface mgmt 0
Ruijie(config-mgmt)# ipv6gateway 2000 ::1
【检验方法】 通过show running-configinterface vlan 2查看配置是否生效。
Ruijie#show running-config interface mgmt 0
Ipv6 gateway 2000::1
**常见配置错误**
无

#### 3.5 监视与维护

**清除各类信息**

### 在设备运行过程中执行clear命令，可能因为重要信息丢失而导致业务中断。^


配置指南 IPv6

作用 命令
清除动态学习到的邻居。 clrear ipv6 neighbors [ vrfvrf-name ] [ oob ] [interface-id]

**查看运行情况**

作用 命令
显示接口上关于IPv6的信息 show ipv6 interface[[interface-id] [ra-info] ] [brief [interface-id]]

显示邻居的信息
show ipv6 neighbors[vrfvrf-name] [verbose][interface-id] [ipv6-address] [static]
[oob]

**查看调试信息**

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。^

作用 命令
查看ND学习情况 debug ipv6 nd


配置指南 DHCP

### 4 DHCP

#### 4.1 概述

DHCP（Dynamic Host Configuration Protocol，动态主机设置协议）是一个局域网的网络协议，使用UDP协议工作，被广泛
用来动态分配可重用的网络资源，如IP地址。

DHCP是基于Client/Server工作模式，DHCP客户端通过发送请求消息向DHCP服务器获取IP地址，等其他配置信息。当
DHCP客户端与服务器不在同一个子网上，必须有DHCP中继代理（DHCP Relay）来转发DHCP请求和应答消息。

**协议规范**

 RFC2131：Dynamic Host Configuration Protocol

 RFC2132：DHCP Options and BOOTP Vendor Extensions

 RFC3046：DHCP Relay Agent Information Option

#### 4.2 典型应用

典型应用 场景描述
在局域网内提供DHCP服务 为局域网内下游用户分配地址。
设备启动DHCP Client功能 局域网内下游多设备启动DHCP Client功能。
MPLS环境下的DHCP Server典型应用 L2vpn/L3vpn环境下DHCP Server的应用。
AM规则在DHCP-server中的典型应用 Supervlan场景下DHCP Server的应用。
有线场景中DHCP Relay典型应用 有线场景中跨网段的用户申请IP上网。
AM规则在DHCP Relay中的典型应用 Supervlan场景中跨网段的用户申请IP上网。

###### 4.2.1 在局域网内提供 DHCP 服务

**应用场景**

在一个局域网内，为四个用户分配IP地址。

以下图为例，为User1、User2、User3 、User4分配IP地址。

 User1、User2、User3 、User4通过A、B、C、D与Server相连

图 4 - 1


配置指南 DHCP

【注释】 S为出口网关设备，作DHCP-Server。
A、B、C、D为接入交换机，作二层透传
User1、User2、User3 、User4为用户

**功能部署**

 Server(S)上运行DHCP-Server服务

 在A、B、C、D上实行二层VLAN透传功能

 User1、User2、User3 、User4上主动发起DHCP-Client请求

###### 4.2.2 设备启动 DHCP Client 功能

**应用场景**

在一个局域网内，A、B、C、D四个接入设备向S请求地址

以下图为例，A、B、C、D接口上开启DHCP-Client功能，请求IP地址。

图 4 - 2


配置指南 DHCP

【注释】 S为出口网关设备，作DHCP-Server。
A、B、C、D为接入交换机，接口启动DHCP-Client功能

**功能部署**

 Server(S)上运行DHCP-Server服务

 在A、B、C、D在接口上开启DHCP-Client功能

###### 4.2.3 MPLS 环境下的 DHCP Server 典型应用

**应用场景**

如下图所示，如果在L3VPN环境下，PE1为DHCP-Server，CE1为DHCP-Client，这种场景下无影响；如果在L2VPN环境
下，PE1为DHCP-Server，CE1为DHCP-Client，这种场景下有影响，PE1的AC侧接口上无法配置IP地址，导致DHCP
报文无法到达Server模块

图 4 - 3 MPLS组网拓扑图(L2VPN/L3VPN)

###### mpls core

###### CE 1 PE 1 PE 3 CE 3

【注释】 在一个MPLS core 域内，PE1， PE3组成一个VPLS网络。 CE1， CE3分别被PE1，PE3接入到同一个VPLS，
CE1多归(Multi-Homing)到PE1和PE3并且接入同一个VPLS域。PE1上启动DHCP-Server

**功能部署**

 配置PE1、PE3为L3VPN的场景，并在PE1启动DHCP-Server功能。

 CE1上启动DHCP-Client。

###### 4.2.4 AM 规则在 DHCP-Server 中的典型应用

**应用场景**


配置指南 DHCP

如下图 1 - 4 所示，设备A作为核心交换设备，配置Supervlan场景、AM过滤规则及启动Dhcp-Server， B作为汇聚交换设备
层，C用作接入交换设备，D作为无线接入交换设备。主要需求如下：

 基于vlan+port的AM规则进行动态地址分配

 基于vlan的AM规则进行静态地址分配

 基于缺省AM规则进行动态地址分配

图 4 - 4 AM规则在DHCP-Server中的组网拓扑图

```
SuperVlan
```

```
汇聚 汇聚
```

##### A

##### B

##### C

##### D

```
suvlan suvlan suvlan
```

```
有线
用户
```

```
无线
用户
```

【注释】 A作为核心设备。
B作为汇聚设备。
C作为有线接入设备。
D作为无线接入设备。

**功能部署**

 在A上配置AM规则、启动Dhcp-Server服务、创建Supervlan。

 在B、C上创建Vlan，对有线用户DHCP报文透传至设备A，进行地址获取。

 在D上启动无线功能，将无线用户DHCP报文透传至设备A，进行地址获取。

###### 4.2.5 有线场景中 DHCP Relay 典型应用

**应用场景**


配置指南 DHCP

如下图所示，Switch C和Switch D作为接入设备，分布着VLAN 10和VLAN 20 的PC用户，Switch B作为网关设备，Switch
A作为核心设备。主要需求如下：

Switch A可以充当DHCP Server，为不同VLAN用户动态分配不同网段的IP地址。

Switch C和Switch D下的接入用户可以跨网段动态获取IP地址。。

图 4 - 5 DHCP Relay组网拓扑图

【注释】 Switch C与 Switch D作为接入设备。
Switch B作为网关设备。
Switch A作为核心设备。

**功能部署**

 配置Switch B和Switch C、D之间的二层通信。

 在Switch B上，指定DHCP服务器地址，并开启DHCP Relay功能。

 在Switch A上，分别为VLAN 10和VLAN 20的用户创建DHCP地址池，开启DHCP Server功能。

###### 4.2.6 AM 规则在 DHCP Relay 中的典型应用

**应用场景**

如下图 1 - 7 所示，设备A作为DHCP Server设备， 设备B作为核心交换设备，配置Supervlan场景、AM过滤规则及启动
Dhcp Relay， C作为汇聚交换设备层，D用作接入交换设备，E作为无线接入交换设备。主要需求如下：

 基于vlan+port的AM规则进行选择客户端子网作为中继报文Giaddress，并转发报文给DHCP Server分配对应客户端子
网的地址


配置指南 DHCP

 基于缺省AM规则进行选择客户端子网作为中继报文Giaddress，并转发报文给DHCP Server分配对应客户端子网的地
址

图 4 - 6 AM规则在DHCP Relay中的组网拓扑图

###### SuperVlan

###### DHCP Server

```
汇聚 汇聚
```

## B

## C

## D

## E

```
suvlan suvlan suvlan
```

```
有线
用户
```

```
无线
用户
```

## A

【注释】 A作为核心设备。
B作为核心设备。
C作为汇聚设备。
D作为有线接入设备。
E作为无线接入设备。


配置指南 DHCP

**功能部属**

 在A上启动Dhcp Server服务。

 在B上配置AM规则、启动Dhcp Relay服务、创建Supervlan。

 在C、D上创建Vlan，对有线用户DHCP报文透传至设备B，进行地址获取。

 在E上启动无线功能，将无线用户DHCP报文透传至设备B，进行地址获取。

#### 4.3 功能详解

**基本概念**

######  DHCP 服务器

锐捷产品的DHCP服务器完全根据RFC 2131来实现的，主要功能就是为主机分配和管理IP地址。

######  DHCP 客户端

DHCP客户端可以让设备自动地从DHCP服务器获得IP地址以及其它配置参数。

######  DHCP 中继

当DHCP客户端与服务器不在同一个子网上，就必须有DHCP中继代理来转发DHCP请求和应答消息。

######  租约

租约是客户机可使用指派的IP地址期间 DHCP 服务器指定的时间长度。租用给客户时，租约是活动的。在租约过期之前，客
户机一般需要通过服务器更新其地址租约时间。当租约期满或在服务器上删除时，租约是非活动的。租约期限决定租约何时期
满以及客户需要用服务器更新它的次数。

######  排除地址

排除地址是指从 DHCP 服务器中排除指定的一些IP地址序列，排除地址作用是为了确保在这些地址都不会是由DHCP服务
器提供给 DHCP 客户机。

######  地址池

地址池是指DHCP服务器可分配给用户的地址集合，所有分配给用户的地址都从管理员配置的池中取出的。

######  选项类型

选项类型是 DHCP 服务器在向 DHCP 客户机提供租约服务时指派的配置参数。例如，某些公用选项包括默认网关（路由器）、
WINS 服务器和 DNS 服务器的 IP 地址。DHCP-Server还允许配置其它选项。虽然大多数选项都是在 RFC 2132 中预定义
的，但若需要的话，可添加自定义选项类型。


配置指南 DHCP

**功能特性**

功能特性 作用
DHCP服务器 设备启用DHCP Server功能，可以为主机动态分配IP地址和提供主机配置参数。
DHCP中继代理 设备启用DHCP Relayr功能，可以在不同网段之间转发DHCP请求和应答消息。
DHCP客户端 设备启用DHCP Client功能，可以自动从DHCP服务器获取IP地址以及其它配置参数。
AM规则 设备启用AM功能，可以依据该规则进行地址分配

###### 4.3.1 DHCP 服务器

**工作原理**

######  DHCP 工作的基本流程

图 4 - 7

DHCP请求IP地址的过程如下：

11. 主机发送DHCPDISCOVER广播包在网络上寻找DHCP服务器；
12. DHCP服务器向主机发送DHCPOFFER单播/广播(依据主机报文相关属性确定)数据包，包含IP地址、MAC地址、域名
    信息以及地址租期；
13. 主机发送DHCPREQUEST广播包，正式向服务器请求分配已提供的IP地址；
14. DHCP服务器向主机发送DHCPACK单播包，确认主机的请求。

### DHCP客户端可以接收到多个DHCP服务器的DHCPOFFER数据包，然后可能接受任何一个DHCPOFFER数据包，但

```
客户端通常只接受收到的第一个DHCPOFFER数据包。另外，DHCP服务器DHCPOFFER中指定的地址不一定为最终
分配的地址，通常情况下，DHCP服务器会保留该地址直到客户端发出正式请求。
```

正式请求DHCP服务器分配地址DHCPREQUEST采用广播包，是为了让其它所有发送DHCPOFFER数据包的DHCP服务
器也能够接收到该数据包，然后释放已经OFFER（预分配）给客户端的IP地址。

如果发送给DHCP客户端的DHCPOFFER信息包中包含无效的配置参数，客户端会向服务器发送DHCPDECLINE信息包拒
绝接受已经分配的配置信息。


配置指南 DHCP

在协商过程中，如果DHCP客户端没有及时响应DHCPOFFER信息包，DHCP服务器会发送DHCPNAK消息给DHCP客户
端，导致客户端重新发起地址请求过程。

在网络建设中，应用锐捷产品DHCP服务器，可以带来以下好处：

 降低网络接入成本。一般采用静态地址分配的接入费用比较昂贵，应用动态地址分配的接入成本较低。

 简化配置任务，降低网络建设成本。采用动态地址分配，大大简化了设备配置，对于在没有专业技术人员的地方部署设备，
更是降低了部署成本。

 集中化管理。在对多个子网进行配置管理时，有任何配置参数的变动，只需要修改和更新DHCP服务器的配置即可。

######  地址池

Server收到来自Client请求报文，首先选择出一个合法有效地址池，并在该池中通过PING机制确认一个可用的地址，接着下
发该池相关配置信息与地址至客户端，同时本地保存该租约信息在，以供该客户续租时检查有效性使用；由此完成整个租约分
配流程。

地址池中可以带有各种配置参数，以下列举几个常用的：

 地址池范围，可以分配给用户的地址范围

 网关地址，通告用户网关地址，最多可以有八个

 DNS地址，通告用户DNS地址，最多可以有八个

 租约周期，通告用户地址何时老化，用户何时该请求续租

######  VRRP 监控功能

在VRRP (Virtual Router Redundancy Protocol，虚拟路由冗余协议)应用场景下，DHCP提供配置命令来决定是否监控当前接
口的VRRP状态。对于配置了VRRP地址的接口，当配置监控VRRP状态后，DHCP服务器仅对处于Master状态的设备接
口上来的DHCP客户端请求报文进行处理，处于备份(Backup)状态的接口请求报文将被丢弃。而对于没配置VRRP地址的接
口，DHCP服务器不再监控VRRP状态，所有DHCP请求报文都会得到处理。VRRP监控命令只能在三层口上配置，默认情
况下VRRP监控功能关闭，即只有主机处理DHCP业务备机不处理。

######  基于 vlan+ 端口 +ip-range 地址分配功能

在布署地址池的环境下，为每个vlan+端口号来分配指定ip-range的地址功能(在满足正常动态地址分配逻辑后，才能从本配置
中选择有效地址)。主要有三种应用场景：1.只有全局默认配置；2.只有基于vlan+端口+ip-range的配置；3.上述两种配置均有；
场景 1 有全局配置,默认分配全局配置的区间地址；场景 2 来自指定vlan+端口的用户分配指定区间的地址，其余则用户无地址
分配；场景 3 满足场景 2 的分配指定区间地址，其余用户分配全局默认配置地址。

######  基于 ARP 检测用户下线

DHCP提供配置命令来决定是否基于ARP检测用户下线。当配置了基于ARP检测用户下线时，用户下线后，DHCP服务器会
收到ARP老化通告，开始回收地址。如果一段时间内（默认 5 分钟），用户没有重新上线，DHCP服务器就回收该地址，分配
给新用户；如果在该段时间内重新上线，用户可以继续使用该地址。

######  添加伪服务器检测功能

如果网络中私自部署DHCP服务器，当客户端申请地址时，会与这台服务器进行交互，导致客户端分配到错误的IP地址。这
台服务器称为伪服务器。DHCP提供配置命令来决定是否开启伪服务器检测功能。当配置伪服务器检测功能时，DHCP会检查


配置指南 DHCP

接收到的DHCP报文中是否携带Option 54（Server Identifier Option，服务器标识选项）。如果携带该选项，并且选项内容与
真实DHCP服务器标识不相符，则记录此伪服务器的IP地址和接收到报文的端口信息。伪服务器检测只是一种事后检测的安
全功能，并不能预防非法DHCP服务器给客户端分配地址。

**相关配置**

######  全局启动 DHCP-Server 服务

 缺省情况下，该服务关闭。

 全局使用service dhcp开启该服务。

 必须在全局使用service dhcp功能，才能进行DHCP服务。

######  配置地址池

 缺省情况下，无地址池。

 使用ip dhcp pool命令可以进入到地址池配置模式，进行地址范围、网关地址、DNS等信息配置。

 不配置地址池范围将无地址可分配，无法下发任何地址。

###### 4.3.2 DHCP 中继代理

**工作原理**

DHCP请求报文的目的IP地址为255.255.255.255，这种类型报文的转发局限于子网内。为了实现跨网段的动态IP地址分配，
DHCP中继就产生了。DHCP中继将收到的DHCP请求报文以单播方式转发给DHCP服务器，同时将收到的DHCP响应报文
转发给DHCP客户端。DHCP中继相当于一个转发站，负责沟通位于不同网段的DHCP客户端和DHCP服务器，即转发客户
端DHCP请求报文、转发服务端DHCP应答报文。这样就实现了只要安装一个DHCP服务器，就可以实现对多个网段的动态
IP管理，即Client—Relay—Server模式的DHCP动态IP管理。如图所示：

图 4 - 8 DHCP Relay应用场景


配置指南 DHCP

VLAN 10和VLAN 20分别对应10.0.0.1/16和20.0.0.1/16的网络，而DHCP 服务器在30.0.0.1/16的网络上，30.0.0.2的DHCP
服务器要对10.0.0.1/16和20.0.0.1/16的网络进行动态IP管理，只要在作为网关的设备上打开DHCP中继功能，并配置30.0.0.2
为DHCP服务器的IP地址。

######  DHCP Relay Agent Information(option 82)

根据RFC3046的定义，中继设备进行DHCP Relay时，可以通过添加option的方式来详细的标明DHCP客户端的一些网络
信息，从而使服务器可以根据更精确的信息给用户分配不同权限的IP，根据RFC3046的定义，所使用option选项的选项号为
82 ，故也被称作option 82。锐捷实现的Relay agent information目前存在四种应用方案，下面分别对四种应用方案进行说明：

15. Relay agent information option dot1x：此种应用方案需要结合802.1x认证以及锐捷产品RG-SAM。DHCP中继根据
    RG-SAM在802.1x认证过程中下发的IP权限，以及DHCP客户端所属vid，组合构成Circuit ID子选项。选项格式如图
    4 - 9 所示：

图 4 - 9 选项格式

16. Relay agent information option82：此种option的应用不需要结合其他协议模块的运行。DHCP中继根据接收DHCP请
    求报文的实体端口，以及设备自身的物理地址信息，组合构成option82选项。选项格式如下图所示：

图 4 - 10 Agent Circuit ID

图 4 - 11 Agent Remote ID

17. Relay agent information option vpn：此种option的应用需要结合MPLS VPN相关功能。

图 4 - 12 MPLS VPN环境中应用


配置指南 DHCP

如图 4 - 12 所示，在MPLS VPN环境中，DHCP Client 1和DHCP中继上的fa0/1口相连，DHCP Client 2和DHCP中继上的
fa1/1相连，接口fa0/1和接口fa1/1分别属于不同的VRF，DHCP Client 1和DHCP Client 2通过DHCP获取地址。按照网络
规划，VPN DepartmentI和VPN DepartmentII使用重叠网段192.168.4.0/24，在该应用环境下，传统的DHCP应用根本无法
支持该部署。为了实现在MPLS VPN环境下对DHCP中继的支持，在DHCP中继中引入了option vpn选项，该选项包括VPN-ID、
Subnet-Selection以及Server-Identifier-Override三个子选项，简单说明一下这三个子选项的意义：

 VPN-ID：在接收到DHCP请求报文时，将DHCP客户端所属的VPN信息，以选项形式加入DHCP请求报文中。DHCP
服务器发送响应报文时，将该选项信息原样保留，DHCP中继根据该选项，将DHCP响应报文转发到正确的VRF中。选
项格式如下图所示：

图 4 - 13 VPN-ID

 Subnet-Selection：在传统的DHCP 中继环境中，通过gateway address[giaddr]字段表示客户端所在的网络信息以及
DHCP服务器与DHCP中继的通讯地址。在MPLS VPN环境中，将giaddr修改为DHCP中继连接DHCP服务器的接口
IP，使DHCP服务器可以与DHCP中继直接通讯。但是客户端的子网信息必须通过新的选项Subnet-Selection来表示。
选项格式如下图所示：

图 4 - 14 Subnet-Selection

 Server-Identifier-Override：在 MPLS VPN环境下，DHCP 客户端后续的请求报文都无法直接发送到DHC服务器。DHCP
中继使用该选项携带DHCP中继与DHCP 客户端直连的接口地址信息，DHCP 服务器发送响应报文的时候，用该选项
覆盖Server-identifier选项信息。从而使DHCP客户端在与DHCP服务器交互的过程中，能够将报文送往DHCP中继，
然后由DHCP中继将报文转发到DHCP服务器。选项格式如下图所示：

图 4 - 15 Server-Identifier-Override


配置指南 DHCP

18. Relay agent information option82：此种option的应用不需要结合其他协议模块的运行。与之前的option82相比较，其
    选项的填充内容有所改变，且支持自定义的内容填充；默认情况下，DHCP中继根据接收DHCP请求报文的实体端口信
    息，以及设备自身的物理地址信息和设备名称，组合构成option82选项。选项格式如图下图所示：

图 1 - 18 Option82.1-circuit-id

图 1 - 19 Option82-remote-id

######  DHCP Relay Check Server-id 功能

在DHCP应用环境中，通常会为每一个网络配备多个DHCP服务器，从而进行备份，防止因为一台服务器的工作不正常影响
网络的正常使用。在DHCP获取的四个交互过程中，当DHCP 客户端在发送DHCP REQUEST时已经选定了服务器，此时会
在请求的报文中携带一个server-id的option选项，在某些特定的应用环境中为了减轻网络服务器压力，需要我们Relay能够
使能此选项，只把请求报文发给此选项里的DHCP服务器，而不是发送给每一个配置的DHCP 服务器，上述就是DHCP Relay
check server-id功能 。

######  DHCP Relay suppression 功能

在指定接口上配置命令ip DHCP Relay suppression后，将屏蔽该接口上收到的DHCP请求报文；而对于其他接口上收到的
DHCP请求报文，则正常转发。

**相关配置**

######  启动设备上的 DHCP Relay 功能

 缺省情况下，设备上的DHCP Relay功能关闭。

 使用service dhcp命令可以启动设备上的DHCP Relay功能。

 必须在设备上启用DHCP Relay功能，DHCP Relay才能正常工作。


配置指南 DHCP

######  配置 DHCP 服务器的 IP 地址

 缺省情况下，无DHCP服务器的IP地址表项。

 使用ip helper-address命令可以添加DHCP服务器地址表项，DHCP服务器地址可以全局配置，也可以在三层接口上
配置。全局或者每个三层接口上最多可以配置 20 个DHCP服务器地址。

 在接口上收到DHCP请求报文时，首先使用接口上的DHCP服务器列表；如果接口上面没有配置DHCP服务器列表，则
使用全局配置的DHCP服务器列表。

######  启动 DHCP option 82 功能

 缺省情况下，设备上的DHCP option 82功能关闭。

 使用ip dhcp relay information option 82 命令可以启动设备上的DHCP option 82功能。

######  启动 DHCP Relay check server-id 功能

 缺省情况下，设备上的DHCP Relay check server-id功能关闭。

 使用ip dhcp relay check server-id命令可以启动设备上的DHCP Relay check server-id功能。

######  启动 DHCP Relay suppression 功能

 缺省情况下，所有接口上DHCP Relay suppression功能关闭。

 使用ip dhcp relay suppression命令可以启动对应接口上的DHCP Relay suppression功能。

######  启动 DHCP Relay multiple-giaddr 功能

 缺省情况下， DHCP Relay支持多giaddr IP功能关闭。

 使用ip dhcp relay multiple-giaddr命令可以启动DHCP Relay支持多giaddr IP功能。

######  启动 DHCP Relay 网关自动切换功能

 缺省情况下， DHCP Relay网关自动切换功能关闭。

 使用ip dhcp smart-relay命令可以启动网关自动切换功能。

###### 4.3.3 DHCP客户端

**工作原理**

Client状态机进入Init状态，主动发出广播Discover报文，之后Client有可能收到多份Offer，进入Offer选择阶段选择一份最
优的Offer后给予该服务器响应，此后在地址的老化1/2、4/5周期内还会发出续租等报文请求对地址的继续使用。

**相关配置**

######  接口上启动 DHCP-Client 功能

 缺省情况下，该服务关闭。


配置指南 DHCP

 接口模式下使用ip address dhcp开启功能。

 必须开启客户端功能，才能进行DHCP服务。

 该功能只在三层接口上有效，如SVI、Rourter Port等；

###### 4.3.4 AM规则

**工作原理**

AM规则用于规划不同vlan + port/vlan上来的DHCP客户端请求的IP范围，可快速定位出问题的DHCP客户端所属的vlan +
port/vlan，也可以更有效地分配地址池的地址。使用AM规则后，所有来自配置vlan + port/vlan的DHCP客户端能够正常获
得地址；反之，若DHCP客户端来源未配置vlan + port/vlan时：如果配置了缺省AM规则， DHCP客户端将获得缺省区间中
的地址，如果未配置缺省AM规则， DHCP客户端无法获得地址。

**相关配置**

######  在全局配置模式下进入 AM 规则配置模式

 全局配置模式下使用address-manage进入AM配置模式；

 使用match ip default命令配置缺省AM规则；

 使用match ip命令配置基于vlan+port/vlan的AM规则；

#### 4.4 配置详解

######  配置 DHCP 服务器

配置项 配置建议 & 相关命令

配置DHCP服务器动态分配IP地址

### 必须配置，用于启用DHCP服务器实现动态IP 址分配。^

```
service dhcp 启动DHCP-SERVER功能
ip dhcp pool 配置地址池
network 配置DHCP地址池的网络号和掩码
```

### 可选配置，用于设置地址池相关属性。^

```
default-router 配置客户端缺省网关
lease 配置地址租期
next-server 配置客户端启动的下载服务器地址
```

bootfile (^) 配置客户端启动文件
domain-name 配置客户端的域名
dns-server 配置域名服务器


配置指南 DHCP

```
netbios-name-server 配置NetBIOS WINS服务器
netbios-node-type 配置客户端NetBIOS节点类型
lease-threshold 配置地址池告警门限值
option 配置自定义选项
```

pool-status (^) 配置地址池启用或关闭
配置DHCP服务器手工地址绑定

### 可选配置，用于为客户静态配置IP地址。^

ip dhcp pool (^) 配置地址池名并进入地址池配置模式
host (^) 配置客户端主机的IP地址和网络掩码
hardware-address 配置客户端的硬件地址
client-identifier 配置客户端的唯一标识
client-name 配置客户端的名字
配置DHCP服务器全局属性

### 可选配置，用于设置DHCP服务器相关属性。^

```
ip dhcp excluded-address 配置排除地址
ip dhcp force-send-nak 配置DHCP服务器强制回复NAK
ip dhcp monitor-vrrp-state 配置监控VRRP状态
```

ip dhcp ping packets (^) 配置Ping包次数
ip dhcp ping timeout (^) 配置Ping包超时时间
ip dhcp server arp-detect 配置DHCP服务器检测用户下线
配置DHCP服务器AM 规则

### 可选配置，用于设置DHCP服务器相关属性。^

```
match ip default 配置基于vlan/port规则下的缺省AM规则
match ip ip-address 配置基于vlan/port规则下的AM规则
```

######  配置 DHCP 中继代理

配置项 配置建议 & 相关命令

配置DHCP Relay基本功能

### 必须配置。用于建立DHCP Relay服务。^

```
service dhcp 启动DHCP Relay功能
ip helper-address 配置DHCP 服务器的IP地址
```

配置DHCP Relay option 82功能

### 可选配置。结合设备自身物理接口信息，给用户分配不同权限IP。该功能与dhcp

```
option dot1x不可以同时使用。
ip dhcp relay information
option82 启用DHCP option82功能^
```

配置DHCP Relay check server-id 功能

### 可选配置。DHCP Relay仅将DHCP请求报文转发到option server-id中指定的

```
服务器。
ip dhcp relay check server-id 启用DHCP Relay check server-di功能
```

### 配置DHCP Relay suppression功能 可选配置。屏蔽对应接口地址上DHCP请求报文。


配置指南 DHCP

```
ip dhcp relay suppression 启用DHCP Relay suppression功能
```

### 配置网关IP自动切换功能

```
可选配置。使能网关自动切换功能。
Ip dhcp smart-relay 配置网关启动切换功能
```

######  配置 DHCP 客户端

配置项 配置建议 & 相关命令

配置DHCP客户端

### 必须配置，用于启用DHCP客户端^

```
ip address dhcp 使得以太网或者PPP、HDLC、FR封装的接
口能够通过DHCP获得IP地址信息
```

###### 4.4.1 配置 DHCP 服务器动态分配 IP 地址

**配置效果**

向所有dhcp-client提供dhcp服务，包括地址、网关等信息下发

**注意事项**

DHCP服务器和DHCP中继共用service dhcp这条命令，但是这两个功能是互斥的，两者之间的切换依赖于是否配置了DHCP
地址池。

**配置方法**

######  启动 DHCP-SERVER 功能

 实现动态分配地址功能，为必选配置。
 在配置模式下执行service dhcp命令。

######  配置地址池

 创建地址池，为必选配置。
 在配置模式下执行ip dhcp pool命令。

######  配置 DHCP 地址池的网络号和掩码

 动态分配地址范围，为必选配置。

######  在地址池模式下执行network命令。

######  配置客户端缺省网关

 用于通告客户端网关地址，为可选配置。
 在地址池模式下执行default-router命令。


配置指南 DHCP

######  配置地址租期

 用于通告客户端租约老化周期，默认值为24h，为可选配置。

######  在地址池模式下执行lease命令。

######  配置客户端启动的下载服务器地址

 用于通告客户端TFTP服务器地址，为可选配置。

######  在地址池模式下执行next-server命令。

######  配置客户端的域名

 用于通告客户端的域名，为可选配置。

######  在地址池模式下执行domain-name命令。

######  配置域名服务器

 用于通告客户客户端dns地址，为可选配置。

######  在地址池模式下执行dns命令。

######  配置 NetBIOS WINS 服务器

 用于通告windows客户端dns地址，为可选配置。

######  在地址池模式下执行netbios-name-server命令。

######  配置客户端 NetBIOS 节点类型

 用于通告windows客户端节点类型，为可选配置。

######  在地址池模式下执行netbios-name-type命令。

######  配置地址池告警门限值

 用于管理租约数量，达到限制时打印警告，默认为90%，为可选配置。

######  在地址池模式下执行lease-threshold命令。

######  配置自定义选项

 用于通告客户端相当配置信息，为可选配置。

######  在地址池模式下执行option命令。

######  配置地址池启用或关闭

 用于配置地址池是否可用，默认为开启，为可选配置。

######  在地址池模式下执行pool-status命令。

**检验方法**

利用DHCP客户端与DHCP服务器进行连接

 检查客户端是否能取到服务器上配置的相关信息


配置指南 DHCP

**相关命令**

######  启动 DHCP-SERVER 功能

```
【命令格式】 service dhcp
【参数说明】 -^
【命令模式】 全局模式
【使用指导】 启用DHCP服务器和DHCP中继代理功能，DHCP服务器和DHCP中继共用service dhcp这条命令，两功
能可以同时存在，但是报文是通过Relay转发还是直接由Server处理，取决于设备上是否配置了合法有效的
地址池，如果存在地址池则由Server处理，不存在由Relay转发。
```

######  配置地址池

```
【命令格式】 ip dhcp pool dhcp-pool
【参数说明】 pool-name：地址池名称
【命令模式】 全局模式
【使用指导】 要给用户下发地址，首先要配置地址池名并进入地址池配置模式
```

######  配置 DHCP 地址池的网络号和掩码

```
【命令格式】 network network-number mask [low-ip-address high-ip-address]
【参数说明】 network-number: DHCP地址池的IP地址网络号
mask: DHCP地址池的IP地址网络掩码。如果没有定义掩码，缺省为自然网络掩码
【命令模式】 DHCP地址池配置模式
【使用指导】 进行动态地址绑定的配置，必须配置新建地址池的子网及其掩码，为DHCP服务器提供了一个可分配给客户
端的地址空间。DHCP在分配地址池中的地址，是按顺序进行的，如果该地址已经在DHCP绑定表中或者检
测到该地址已经在该网段中存在，就检查下一个地址，直到分配一个有效的地址。
锐捷无线产品中新增了可以配置地址池的网段范围，指明可以分配的网段中的起始地址和终止地址，该配置为
可选配置。在不指明起始地址和终止地址的情况下，地址池的可分配的IP地址范围为该网段内的所有IP地址
锐捷产品的DHCP动态地址池中，地址的分配是以客户端的物理地址和客户端ID为索引的，这就意味着DHCP
动态地址池中不可能存在相同客户端的两份租约；如果客户端和服务器之间的网络拓扑存在路径上的冗余[客
户端可以通过直连路径，同时也可以通过中继路径到达服务器]，就会导致服务器分配地址出现问题，可能导
致地址分配失败；
因此，为了避免上述问题，要求网络管理员在构建网络的时候，通过其它的方式，如调整物理链路或者网络路
径，来避免这种客户端到服务器的路径冗余
```

######  配置客户端缺省网关

【命令格式】 default-router^ address [ _address2...address8_ ]^
【参数说明】 address：定义客户端默认网关的IP地址。要求至少配置一个
ip- _address2...ip_ - address8：（可选）最多可以配置 8 个网关
【命令模式】 DHCP地址池配置模式
【使用指导】 配置客户端默认网关，这个将作为服务器分配给客户端的默认网关参数。缺省网关的IP地址必须与DHCP客
户端的IP地址在同一网络


配置指南 DHCP

######  配置地址租期

```
【命令格式】 lease {days [hours] [ minutes] | infinite}
【参数说明】 days：定义租期的时间，以天为单位
hours: （可选）定义租期的时间，以小时为单位。定义小时数前必须定义天数
minutes: （可选）定义租期的时间，以分钟为单位。定义分钟前必须定义天数和小时数
infinite: 定义没有限制的租期
【命令模式】 DHCP地址池配置模式
【使用指导】 DHCP服务器给客户端分配的地址，缺省情况下租期为 1 天。当租期快到时客户端需要请求续租，否则过期
后就不能使用该地址
```

######  配置客户端启动文件

```
【命令格式】 bootfile filename
【参数说明】 file-name：定义用于启动的文件名
【命令模式】 DHCP地址池配置模式
【使用指导】 客户端启动文件是客户端启动时要用到的启动映像文件。启动映像文件通常是DHCP客户端需要下载的操作
系统
```

######  配置客户端的域名

```
【命令格式】 domain-name^ domain^
【参数说明】 domain-name: 定义DHCP客户端的后缀域名字符串
【命令模式】 DHCP地址池配置模式
【使用指导】 可以指定客户端的域名，这样当客户端通过主机名访问网络资源时，不完整的主机名会自动加上域名后缀形成
完整的主机名
```

######  配置域名服务器

【命令格式】 dns-server { ip-address [ ip-address2 _..._ ip-address8 ] }
【参数说明】 ip-address: 定义DNS服务器的IP地址。要求至少配置一个
ip- _address2...ip_ - address8: （可选）最多可以配置 8 个DNS服务器
【命令模式】 DHCP地址池配置模式
【使用指导】 当客户端通过主机名访问网络资源时，需要指定DNS服务器进行域名解析。要配置DHCP客户端可使用的域
名服务器

######  配置 NetBIOS WINS 服务器

```
【命令格式】 netbios-name-server address [ address2...address8 ]
【参数说明】 address: 定义WINS服务器的IP地址。要求至少配置一个
ip- address2...ip - address8: （可选）最多可以配置 8 个WINS服务器
【命令模式】 DHCP地址池配置模式
【使用指导】 WINS是微软TCP/IP网络解析NetNBIOS名字到IP地址的一种域名解析服务。WINS服务器是一个运行在
Windows NT下的服务器。当WINS服务器启动后，会接收从WINS客户端发送的注册请求，WINS客户端关
闭时，会向WINS服务器发送名字释放消息，这样WINS数据库中与网络上可用的计算机就可以保持一致了
```

配置指南 DHCP

######  配置客户端 NetBIOS 节点类型

```
【命令格式】 netbios-node-type type
【参数说明】 type: 定义NetBIOS节点类型，有两种方式
数字定义，范围从0~FF，十六进制数，但只能取以下值：
 1 ，代表b-node
 2 ，代表p-node
 4 ，代表m-node
 8 ，代表h-node
字符串定义：
 b-node，广播型节点
 p-node，对等型节点
 m-node，混合型节点
 h-node，复合型节点
【命令模式】 DHCP地址池配置模式
【使用指导】 微软DHCP客户端NetBIOS节点类型有四种： 1 ）Broadcast，广播型节点，通过广播方式进行NetBIOS名
字解析； 2 ）Peer-to-peer，对等型节点，通过直接请求WINS服务器进行NetBIOS名字解析； 3 ）Mixed，混
合型节点，先通过广播方式请求名字解析，后通过与WINS服务器连接进行名字解析； 4 ）Hybrid，复合型节
点，首先直接请求WINS服务器进行NetBIOS名字解析，如果没有得到应答，就通过广播方式进行NetBIOS
名字解析。
缺省情况下，微软操作系统的节点类型为广播型或者复合型。如果没有配置WINS服务器，就为广播型节点；
如果配置了WINS服务器，就为复合型节点
```

######  配置自定义选项

```
【命令格式】 option code { ascii string | hex string | ip ip-address }
【参数说明】 code: 定义DHCP选项代码
ascii string: 定义一个ASCII字符串
hex string: 定义十六进制字符串
ip ip-address: 定义IP地址列表
【命令模式】 DHCP地址池配置模式
【使用指导】 DHCP提供了一个机制，允许在TCP/IP网络中将配置信息传送给主机。DHCP报文专门有option字段，该
部分内容为可变化内容，用户可以根据实际情况进行定义，DHCP客户端必须能够接收携带至少 312 字节
option 信息的DHCP报文。另外DHCP报文中的固定数据字段也称为一个选项
在WLAN无线应用环境中，AP上的DHCP客户端会动态申请获取AC的IP地址列表，可以通过在DHCP服
务器上配置自定义选项携带AC的IP地址列表来实现
```

######  配置地址池启用或关闭

```
【命令格式】 pool-status {enable | disable}^
【参数说明】 enable: 启用地址池
disable: 关闭地址池
默认为开启
【命令模式】 DHCP地址池配置模式
```

配置指南 DHCP

```
【使用指导】 在锐捷无线产品中新增了可配置DHCP地址池是否启用命令，通过配置命令可以启用或关闭对应地址池服务
```

**配置举例**

######  配置地址池

```
【配置方法】  定义了一个地址池net172
 地址池网段为172.16.1.0/24
 缺省网关为172.16.1.254
 地址租期为 1 天
 排除172.16.1.2~172.16.1.100地址
Ruijie(config)# ip dhcp excluded-address 172.16.1.2 172.16.1.100
Ruijie(dhcp-config)# ip dhcp pool net172
Ruijie(dhcp-config)# network 172.16.1.0 255.255.255.0
Ruijie(dhcp-config)# default-router 172.16.1.254
Ruijie(dhcp-config)# lease 1
```

```
【检验方法】 1.show run查看
Ruijie(config)#show run | begin ip dhcp
ip dhcp excluded-address 172.16.1.2 172.16.1.100
ip dhcp pool net172
network 172.16.1.0 255.255.255.0default-router 172.16.1.254
lease 1
```

###### 4.4.2 配置 DHCP 服务器手工地址绑定

**配置效果**

###### 向某些特定的dhcp-client下发特定的ip地址及其它配置信息

**注意事项**

###### 无

**配置方法**

######  配置地址池名并进入地址池配置模式

 创建地址池，为必选配置。
 在配置模式下执行ip dhcp pool命令。


配置指南 DHCP

######  配置客户端主机的 IP 地址和网络掩码

 配置静态ip地址及网络掩码，必选配置。

######  在地址池模式下执行host命令。

######  配置客户端的硬件地址

 配置静态mac地址，可选配置。

######  在地址池模式下执行hardware命令。

######  配置客户端的唯一标识

 配置静态用户uid，可选配置。

######  在地址池配置下执行client-identifier命令。

######  配置客户端的名字

 配置静态用户名字，可选配置。

 在地址池模式下执行host-name命令。

**检验方法**

###### 对应的用户上线，判断是否能取到相应地址。

**相关命令**

######  配置地址池

```
【命令格式】 ip dhcp pool dhcp-pool
【参数说明】 pool-name：地址池名称
【命令模式】 全局模式
【使用指导】 要给用户下发地址，首先要配置地址池名并进入地址池配置模式
```

######  手工地址绑定

【命令格式】 host ip-address [ netmask ]
client-identifier unique-identifier
client-name name
【参数说明】 ip-address: 定义DHCP客户端主机的IP地址
netmask: 定义DHCP客户端主机的网络掩码
unique-identifier : 定义客户端硬件地址，如aabb.bbbb.bb88;定义客户端的标识，如01aa.bbbb.bbbb.88
name: （可选）用标准的ASCII字符定义客户端的名字，名字不要包括域名。如定义mary主机名，不可定
义成mary.rg.com
【命令模式】 DHCP地址池配置模式
【使用指导】 地址绑定是指IP地址和客户端MAC地址的映射关系。地址绑定有两种： 1 ）手工绑定，就是在DHCP服务
器数据库中，通过手工定义将IP地址和MAC地址进行静态映射，手工绑定其实是一个特殊地址池； 2 ）动态


配置指南 DHCP

```
绑定，DHCP 服务器接收到DHCP请求时，动态地从地址池中分配IP地址给客户端，而形成的IP地址和
MAC地址映射。
要定义手工地址绑定，首先需要为每一个手动绑定定义一个主机地址池，然后定义DHCP客户端的IP地址和
硬件地址或客户端标识。硬件地址就是MAC地址。客户端标识，微软客户端一般定义客户端标识，而不定义
MAC地址，客户端标识包含了网络媒介类型和MAC地址。关于媒介类型的编码，请参见RFC 1700中关于
“Address Resolution Protocol Parameters”部分内容。以太网类型为“01”
```

**配置举例**

######  动态地址池

```
【配置方法】  地址池 vlan1 20.1.1.0 255.255.255.0
 缺省网关为 20 .1.1. 1
 租约时间为 1 天
Ruijie(config)# ip dhcp pool vlan1
Ruijie(dhcp-config)# network 20.1.1.0 255.255.255.0
Ruijie(dhcp-config)# default-router 20.1.1.1
Ruijie(dhcp-config)# lease 1 0 0
【检验方法】 1.show run查看
Ruijie(config)#show run | begin ip dhcp
ip dhcp pool vlan1
network 20.1.1.0 255.255.255.0
default-router 20.1.1.1
lease 1 0 0
```

######  手工绑定配置

```
【配置方法】  主机地址172.16.1.101，掩码为255.255.255.0
 主机名Billy.rg.com
 缺省网关为172.16.1.254
 MAC地址为00d0.df34.32a3
Ruijie(config)# ip dhcp pool Billy
Ruijie(dhcp-config)# host 172.16.1.101 255.255.255.0
Ruijie(dhcp-config)# client-name Billy
Ruijie(dhcp-config)# hardware-address 00d0.df34.32a3 ethernet
Ruijie(dhcp-config)# default-router 172.16.1.254
```

```
【检验方法】 1.show run查看
Ruijie(config)#show run | begin ip dhcp
ip dhcp pool Billy
```

配置指南 DHCP

```
host 172.16.1.101 255.255.255.0
client-name Billy
hardware-address 00d0.df34.32a3 ethernet
default-router 172.16.1.254
```

###### 4.4.3 配置 DHCP 服务器 AM 规则

**配置效果**

###### 配置该命令后，可依据端口+VLAN按区间进行地址分配

**注意事项**

###### 锐捷产品目前版本支持以太网接口、千兆口以及FR、PPP、HDLC接口上的配置。

**配置方法**

######  配置地址管理功能

 进入到地址管理模式，为必选配置。
 在配置模式下执行address-manage命令。

######  配置 AM 规则

 配置基于端口+VLAN的AM规则，为必选配置。
 在配置模式下执行match ip命令。

**检验方法**

查看不同vlan、端口下的用户是否取到有效地址

**相关命令**

######  配置缺省区间

```
【命令格式】 match ip default ip-address netmask
【参数说明】 ip-address: 网络地址
netmask: 地址掩码
【命令模式】 address-manage模式下
【使用指导】 配置该命令后所有来自未配置vlan + port的DHCP客户端将取得缺省区间内的地址，如果无该配置命令同时
也无任何其它vlan + port配置，则按正常流程分配地址。
```

配置指南 DHCP

######  配置基于 vlan/port 规则下的动态地址分配

```
【命令格式】 match ip ip-address netmask interface [add/remove] vlan vlan-list
【参数说明】 ip-address: 网络地址
netmask: 地址掩码
interface: 接口名称
add/remove: 添加或删除指定vlan
vlan-list: vlan索引
【命令模式】 address-manage模式下
【使用指导】 配置该命令后来自指定vlan + port的DHCP客户端将取得配置间内地址。
```

######  配置基于 vlan 规则下的静态地址分配

```
【命令格式】 match ip^ ip-address^ netmask [add/remove]^ vlan^ vlan-list^
【参数说明】 ip-address: 网络地址
netmask: 地址掩码
add/remove: 添加或删除指定vlan
vlan-list: vlan索引
【命令模式】 address-manage模式下
【使用指导】 在supervlan场景下，满足Dhcp静态地址池配置的用户，无论在哪个subvlan下都只分配该静态地址；此时
AM无需基于所有subvlan/port对该地址进行配置，只需要配置该地址在对应的vlan区间生效即可。该规则当
前只对静态地址分配生效，动态地址不生效。
```

**配置举例**

######  AM 规则配置

【配置方法】  配置缺省规则规则
 配置指定vlan+port+地址区间规则
 配置指定vlan+地址区间规则
Ruijie(config)# address-manage
Ruijie(config-address-manage)# match ip default 172.50.128.0 255.255.128.0
Ruijie(config-address-manage)# match ip 10.1.5.0 255.255.255.0 Gi5/3 vlan 1005
Ruijie(config-address-manage)# match ip 1 0.1. 6 .0 255.255.255.0 vlan 100 6

【检验方法】 1 ：show run查看
address-manage
match ip default 172.50.128.0 255.255.128.0
match ip 10.1.5.0 255.255.255.0 Gi5/3 vlan 1005
match ip 1 0.1. 6 .0 255.255.255.0 vlan 100 6


配置指南 DHCP

###### 4.4.4 配置 DHCP 服务器全局属性

**配置效果**

###### 开启服务器一些特定的功能，如ping机制、强制nak等。

**注意事项**

###### Nak命令的配置可能引起网络中其它服务器的功能异常。

**配置方法**

######  配置排除地址

 配置某些地址或地址段不可用，为可选配置。
 在配置模式下执行ip dhcp excluded-address命令

######  配置 DHCP 服务器强制回复 NAK

 针对某些用户的错误地址请求，服务器回复nak报文，可选配置。

######  在配置模式下执行ip dhcp force-send-nak命令。

######  配置监控 VRRP 状态

 启动该功能后，主机server处理DHCP相关报文，备机server则不处理DHCP相关报文，可选配置。

######  在配置模式下执行ip dhcp monitor-vrrp-state命令。

######  配置 Ping 包次数

 检查地址的可达性，执行ping操作，默认值为 2 ，可选配置。

######  在配置模式下执行ip dhcp ping packet命令。

######  配置 Ping 包超时时间

 检查地址的可达性，设置ping返回时长，默认值为500ms， 可选配置。

######  在配置模式下执行ip dhcp ping timeout命令。

######  配置 DHCP 服务器检测用户下线

 用于配置DHCP服务器是否检测用户下线。如果用户下线后一段时间内没有重新上线，则回收分配给该用户的地址。

######  在配置模式下执行ip dhcp server arp-detect命令。

**检验方法**

###### 启动dhcp-server下发地址过程中可检验。


配置指南 DHCP

**相关命令**

######  配置排除地址

【命令格式】 ip dhcp excluded-address low-ip-address [ high-ip-address ]
【参数说明】 low-ip-address: 排斥IP地址范围的起始IP地址
high-ip-address：排斥地址范围的结束IP地址
【命令模式】 全局模式
【使用指导】 如果没有特别配置，DHCP服务器会试图将在地址池中定义的所有子网地址分配给DHCP客户端。因此，如
果想保留一些地址不分配，比如已经分配给服务器或者设备了，必须明确定义这些地址是不允许分配给客户端
的；配置DHCP服务器，一个好的习惯是将所有已明确分配的地址全部不允许DHCP分配，这样可以带来两
个好处： 1 ）不会发生地址冲突； 2 ）DHCP分配地址时，减少了检测时间，从而提高DHCP分配效率

######  配置 DHCP 服务器强制回复 NAK

```
【命令格式】 ip dhcp force-send-nak
【参数说明】 -^
【命令模式】 全局配置模式
【使用指导】 在无线应用中，DHCP客户端的移动性较大，DHCP客户端会经常性的从一个网络移动到另一个网络中。当
DHCP服务器在收到客户端的Request续租报文时，发现客户端的网段发生更改或者是租约超时时会给予回
复NAK，要求客户端重新获取IP地址，避免客户端不断发送Request报文直至超时后重新获取IP地址，延
长IP地址获取时间。
但是，DHCP服务器发送NAK报文的前提是该DHCP客户端在自己的管理范围之内，也就是可以查找到对应
的租约记录信息。当DHCP客户端从另一个网络环境中移入时，DHCP服务器将无法在本地查找到对应的租
约记录信息，不予回复NAK，此时DHCP客户端需要不断发送Request报文直至超时后重新获取IP地址，
导致IP地址获取时间变长。在DHCP服务器重启时丢失客户端租约，而客户端要求续租时也会遇到类似情况。
在这种情况下，可以通过配置命令强制让DHCP服务器在查找不到租约记录时也给予回复NAK报文，触发客
户端快速获取到IP地址，注意：默认情况下该条命令关闭；在开启该命令的时候，在同一广播域内，不允许
开启多台DHCP服务器
```

######  配置 Ping 包次数

```
【命令格式】 ip dhcp ping packets [ number^ ]^
【参数说明】 Number：（可选）范围从 0 到 10 ， 0 表示关闭ping操作。缺省ping两个包
【命令模式】 全局配置模式
【使用指导】 缺省情况，当DHCP服务器试图从地址池中分配一个IP地址时，会对该地址执行两次Ping命令(一次一个数
据包)。如果Ping没有应答，DHCP服务器认为该地址为空闲地址，就将该地址分配给DHCP客户端；如果
Ping有应答，DHCP服务器认为该地址已经在使用，就试图分配另外一个地址给DHCP客户端，直到分配成
功
```

######  配置 Ping 包超时时间

```
【命令格式】 ip dhcp ping timeout milliseconds
【参数说明】 milli-seconds：DHCP服务器等待ping应答的时间（以毫秒计）。取值范围为 100 到 10000
```

配置指南 DHCP

```
【命令模式】 全局配置模式
【使用指导】 缺省情况下，DHCP服务器Ping操作如果 500 毫秒没有应答，就认为没有该IP地址主机存在。可以通过调
整Ping包超时时间，改变服务器Ping等待应答的时间
```

######  配置基于 ARP 检测用户下线

```
【命令格式】 ip dhcp server arp-detect
【参数说明】 -^
【命令模式】 全局配置模式
【使用指导】 缺省情况下，DHCP服务器不会基于ARP检测用户下线。配置该命令后，DHCP服务器可以检测用户的下线。
如果用户在一段时间内（默认 5 分钟）未重新上线，DHCP服务器就回收分配给该用户的地址。
```

**配置举例**

######  配置 ping 机制

```
【配置方法】  配置ping次数为 5
 配置ping超时时长为800ms
Ruijie(config)# ip dhcp ping packet 5
Ruijie(config)# ip dhcp ping timeout 800
```

```
【检验方法】 1.show run查看
Ruijie(config)#show run | begin ip dhcp^
ip dhcp ping packet 5
ip dhcp ping timeout 800
```

######  配置排除地址

```
【配置方法】  排除192.168.0.0 – 192.168.255.255的所有地址
Ruijie(config)# ip dhcp excluded-address 192.168.0.0 192.168.255.255
```

```
【检验方法】 1.show run查看
Ruijie(config)#show run | begin ip dhcp
ip dhcp excluded-address 192.168.0.0 192.168.255.255
```

###### 4.4.5 配置 DHCP Relay 基本功能

**配置效果**

 建立Client—Relay—Server模式的DHCP动态IP管理，解决DHCP客户端与DHCP服务器不在同一网段时DHCP客
户端与在其他网段的DHCP服务器通讯问题。


配置指南 DHCP

**注意事项**

 DHCP Relay需要借助网络中现有的单播路由。因此，网络中必须配置IPv4单播路由。

**配置方法**

######  启动 DHCP Relay 功能

 必须配置。

 若无特殊要求，应在设备上启动DHCP Relay功能。

######  配置 DHCP 服务器的 IP 地址

 必须配置。

 应在设备上启动DHCP服务器的IP地址。

**检验方法**

 检查用户主机能否通过DHCP Relay成功获取到IP地址。

**相关命令**

######  启动 DHCP Relay 功能

```
【命令格式】 service dhcp
【参数说明】 -
【命令模式】 全局模式
【使用指导】 -
```

######  配置 DHCP 服务器的 IP 地址

```
【命令格式】 ip helper-address { cycle-mode | [ vrf { vrf-name }] A.B.C.D }
【参数说明】 cycle-mode^ ： 开启dhcp请求报文转发所有dhcp服务器^
vrf-name ： vrf 名称
A.B.C.D: Server的ip地址
【命令模式】 全局模式、接口模式
【使用指导】 配置接口必须是三层接口，包括：路由口、L3AP、SVI、loopback接口。
所有配置接口应IPv4单播路由可达。
```

**配置举例**

### 以下配置举例，仅介绍与DHCP Relay相关的配置。^


配置指南 DHCP

######  有线场景中 DHCP Relay 配置

```
【网络环境】
图 4 - 16
```

(^)
【配置方法】  用户设备启动通过DHCP获取地址的功能。
 在作为DHCP Relay Agent的网络设备中启动DHCP Relay功能。
 配置DHCP Server。
A 用户设备启动DHCP获取地址的功能。
B # 启用DHCP中继代理
Ruijie(config)# service dhcp

# 添加一个全局的DHCP服务器的地址

Ruijie(config)# ip helper-address 172.2.2.1

# 配置与用户设备连接的端口的IP地址

Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if)# ip address 192.1.1.1 255.255.255.0

# 配置与Server设备连接的端口的IP地址

Ruijie(config)# interface gigabitEthernet 0/2
Ruijie(config-if-gigabitEthernet 0/2)# ip address 172.2.2.2 255.255.255.0
C # 启用DHCP SERVER功能
Ruijie(config)# service dhcp

# 添加一个客户端地址池

Ruijie(config)# ip dhcp pool relay
Ruijie (dhcp-config)#network 192. 1 .1.0 255.255.255.0
Ruijie (dhcp-config)#default-router 192. 1 .1.1

# 配置与relay设备连接的端口的IP地址

Ruijie(config)# interface gigabitEthernet 0/ 1
Ruijie(config-if-gigabitEthernet 0/2)# ip address 172.2.2. 1 255.255.255.0
【检验方法】 查看用户是否能获取到IP地址。
 检查用户设备是否能获取到IP地址。
 检查DHCP Relay配置是否正确。
A 用户设备能获取到IP地址
B 登录到DHCP Relay Agent设备后在特权模式下用show running-config命令显示DHCP Relay配置
Ruijie# show running-config
service dhcp
ip helper-address 172.2.2.1
!
interface GigabitEthernet 0/1
ip address 192.1.1.1 255.255.255.0


配置指南 DHCP

```
!
interface GigabitEthernet 0/2
ip address 172.2.2.2 255.255.255.0
!
```

**常见错误**

 IPv4单播路由配置错误。

 没有启动DHCP Relay功能。

 没有配置DHCP Relay与DHCP Service之间的路由。

 没有配置DHCP 服务器IP地址。

###### 4.4.6 配置 DHCP Relay option 82 功能

**配置效果**

 中继设备进行DHCP Relay时，可以通过添加option的方式来详细的标明DHCP客户端的一些网络信息，从而使服务器
可以根据更精确的信息给用户分配不同权限的IP。

**注意事项**

 必须配置DHCP Relay基本功能。

**配置方法**

######  启动 DHCP Relay 基本功能

 必须配置。

 若无特殊要求，应在设备上启动DHCP Relay基本功能。

######  启动 DHCP option82 功能

 缺省情况下，设备上的DHCP option 82功能关闭。

 使用ip dhcp relay information option 82 命令可以启动或关闭设备上的DHCP option 82 功能。

**检验方法**

 检查客户端获取到的IP地址，是否是根据option 82 规则分配。。


配置指南 DHCP

**相关命令**

######  配置 DHCP option82 功能

```
【命令格式】 ip dhcp relay information option82
【参数说明】 -^
【命令模式】 全局模式
【使用指导】 -^
```

**配置举例**

######  启动 DHCP option 82 功能。

```
【配置方法】  启动DHCP option 82功能
 配置相关的子选项命令
Ruijie(config)# ip dhcp relay information option 82
```

```
【检验方法】 登录到DHCP Relay Agent设备后在特权模式下用show running-config命令显示DHCP Relay配置。
Ruijie#show ru | incl ip dhcp relay
ip dhcp relay information option82
```

**常见配置错误**

 DHCP Relay基本功能没有配置，或配置失败。

###### 4.4.7 配置 DHCP Relay check server-id 功能

**配置效果**

 当配置命令ip dhcp relay check server-id后，DHCP Relay仅将DHCP请求报文转发到option server-id中指定的服务
器。如果没有配置该命令，则向所有配置的DHCP服务器转发DHCP请求报文。

**注意事项**

 必须配置DHCP Relay基本功能。

**配置方法**

######  启动 DHCP Relay check server-id 功能

 缺省情况下，设备上的DHCP Relay check server-id功能关闭。


配置指南 DHCP

 使用ip dhcp relay check server-id命令可以启动设备上的DHCP Relay check server-id功能。

**检验方法**

DHCP Relay是否仅将DHCP请求报文转发到option server-id中指定的服务器。

**相关命令**

######  配置 DHCP Relay check server-id 功能

```
【命令格式】 ip dhcp relay check server-id
【参数说明】 -
【命令模式】 全局模式
【使用指导】 -
```

**配置举例**

######  配置 DHCP Relay check server-id 功能。

```
【配置方法】  配置DHCP Relay基本功能。略
 在对应接口上配置DHCP Relay check server-id功能。
Ruijie# configure terminal
Ruijie(config)# ip dhcp relay check server-id
```

```
【检验方法】 登录到DHCP Relay Agent设备后在特权模式下用show running-config命令显示DHCP Relay配置。
Ruijie# show running-config | include check server-id
ip dhcp relay check server-id
Ruijie#
```

**常见配置错误**

 DHCP Relay基本功能没有配置，或配置失败。

###### 4.4.8 配置 DHCP Relay suppression 功能

**配置效果**

 在指定接口上配置命令ip dhcp relay suppression后，将屏蔽该接口上收到的DHCP请求报文；而对于其他接口上收
到的DHCP请求报文，则正常转发。

**注意事项**


配置指南 DHCP

 必须配置DHCP Relay基本功能。

**配置方法**

######  启动 DHCP Relay suppression 功能

缺省情况下，设备上所有接口的DHCP Relay suppression功能关闭。

使用ip dhcp relay suppression命令可以启动设备上的DHCP Relay suppression功能。

**检验方法**

 接口上收到的DHCP请求报文是否被过滤。

**相关命令**

######  配置 DHCP Relay suppression 功能

```
【命令格式】 ip dhcp relay suppression
【参数说明】 -
【命令模式】 接口模式
【使用指导】 -^
```

**配置举例**

######  配置 DHCP Relay suppression 功能。

【配置方法】 (^)  配置DHCP Relay基本功能。略
 在对应接口上配置DHCP Relay suppression功能。
Ruijie# configure terminal
Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-GigabitEthernet 0/1)# ip dhcp relay suppression
Ruijie(config-if-GigabitEthernet 0/1)#end
Ruijie#
【检验方法】 登录到DHCP Relay Agent设备后在特权模式下用show running-config命令显示DHCP Relay配置。
Ruijie# show running-config | include relay suppression
ip dhcp relay suppression
Ruijie#
**常见配置错误**


配置指南 DHCP

DHCP Relay基本功能没有配置，或配置失败。

###### 4.4.9 配置 DHCP Relay 支持多 giaddr IP 功能

**配置效果**

 配置命令ip dhcp relay multiple-giaddr后，开启支持多giaddr IP功能。

**注意事项**

 必须配置DHCP Relay基本功能。

**配置方法**

######  启动 DHCP Relay multiple-giaddr 功能

缺省情况下，功能关闭。

使用ip dhcp relay multiple-giaddr命令可以启动功能。

**检验方法**

 接口上配置了多个IP地址时的DHCP请求报文是否可以带上不同的IP地址转发给DHCP服务器。

**相关命令**

######  配置 DHCP Relay multiple-giaddr 功能

```
【命令格式】 ip dhcp relay multiple-giaddr
【参数说明】 -
【命令模式】 全局模式
【使用指导】 -
```

**配置举例**

######  配置 DHCP Relay multiple-giaddr 功能。

```
【配置方法】 ^ 配置DHCP Relay基本功能。略^
 配置DHCP Relay multiple-giaddr功能。
Ruijie# configure terminal
Ruijie(config)# ip dhcp relay multiple-giaddr
```

配置指南 DHCP

```
【检验方法】 登录到DHCP Relay Agent设备后在特权模式下用show running-config命令显示DHCP Relay配置。
Ruijie# show running-config
ip dhcp relay multiple-giaddr
```

**常见配置错误**

DHCP Relay基本功能没有配置，或配置失败。

###### 4.4.10 配置 DHCP Relay 支持网关自动切换功能

**配置效果**

 配置命令ip dhcp smart-relay后，开启网关自动切换功能。

**注意事项**

 必须配置DHCP Relay基本功能。

**配置方法**

######  启动 DHCP Relay网关自动切换 功能

缺省情况下，功能关闭。

使用ip dhcp smart-relay命令可以启动功能。

**检验方法**

 接口上配置了多个IP地址，DHCP-RELAY转发DISCOVER报文 3 个，没有收到应答报文，切换网关地址。

**相关命令**

######  配置 DHCP Relay网关自动切换 功能

```
【命令格式】 ip dhcp smart-relay
【参数说明】 -
【命令模式】 全局模式
【使用指导】 -
```

配置指南 DHCP

**配置举例**

######  配置 DHCP Relay网关启动切换 功能。

【配置方法】 (^)  配置DHCP Relay基本功能。略
 配置DHCP Relay网关启动切换功能。
Ruijie# configure terminal
Ruijie(config)# ip dhcp smart-relay
【检验方法】 登录到DHCP Relay Agent设备后在特权模式下用show running-config命令显示DHCP Relay配置。
Ruijie# show running-config
ip dhcp smart-relay
**常见配置错误**
DHCP Relay基本功能没有配置，或配置失败。

###### 4.4.11 配置 DHCP Relay 指定源地址功能

**配置效果**

 在指定接口上配置命令ip dhcp relay source后，就指定Relay报文的源地址。

**注意事项**

 必须配置DHCP Relay基本功能。

 一个接口下只能指定一个Relay报文的源地址。

 该功能需配合option82功能一起使用，给客户端分配正确的子网地址。

**配置方法**

######  启动 DHCP Relay 指定源地址功能

缺省情况下，不指定DHCP Relay报文的源地址。

使用ip dhcp relay source ip-address命令可以指定Relay报文的源地址。

**检验方法**


配置指南 DHCP

 接口上配置了指定源地址时，发给的DHCP服务器的Relay报文的源地址即配置的地址。

**相关命令**

######  配置 DHCP Relay 指定源地址功能

```
【命令格式】 ip dhcp relay source ip-address
【参数说明】 ip-address：relay报文的源地址。
【命令模式】 接口模式
【使用指导】 -
```

**配置举例**

######  配置 DHCP Relay 指定源地址功能。

【配置方法】 (^)  配置DHCP Relay基本功能。略
 在对应接口上配置DHCP Relay指定源地址功能。
Ruijie(config-if)# ip dhcp relay source 1.1.1.1
【检验方法】 登录到DHCP Relay Agent设备后在特权模式下用show running-config命令显示DHCP Relay配置。
**常见配置错误**
DHCP Relay基本功能没有配置，或配置失败。

###### 4.4.12 配置 DHCP 客户端

**配置效果**

###### 设备启动dhcp-client，可动态取得地址及其它需求配置。

**注意事项**

###### 锐捷产品目前版本支持以太网接口以及FR、PPP、HDLC接口上的DHCP客户端。

**配置方法**

在接口上执行ip address dhcp命令

**检验方法**


配置指南 DHCP

查看接口是否取到ip地址

**相关命令**

######  配置 DHCP 客户端

```
【命令格式】 ip address dhcp
【参数说明】 -
【命令模式】 接口配置模式
【使用指导】  锐捷产品支持以太网端口通过DHCP获得动态分配的IP地址
 锐捷产品支持ppp封装的端口通过DHCP获得动态分配的IP地址
 锐捷产品支持FR封装的端口通过DHCP获得动态分配的IP地址
 锐捷产品支持HDLC封装的端口通过DHCP获得动态分配的IP地址
```

**配置举例**

######  DHCP 客户端配置

【配置方法】 1 ：为设备接口FastEthernet 0/0配置DHCP自动分配地址
Ruijie(config)# interface FastEthernet0/0
Ruijie(config-if-FastEthernet 0/0)#ip address dhcp

【检验方法】 1 ：show run查看
Ruijie(config)#show run | begin ip address dhcp^
ip address dhcp

#### 4.5 监视与维护

**清除各类信息**

### 在设备运行过程中执行clear命令，可能因为重要信息丢失而导致业务中断。^

作用 命令
清除DHCP地址绑定 clear ip dhcp binding^ { address^ | *}^
清除DHCP地址冲突 clear ip dhcp conflict { address | *}
清除DHCP服务器统计状态 clear ip dhcp server statistics
清除DHCP中继统计状态 clear ip dhcp relay statistics
清除DHCP服务器性能统计信息 clear ip dhcp server rate

**查看运行情况**


配置指南 DHCP

作用 命令
显示DHCP租约信息 show dhcp lease
显示dhcp用的套接字 show ip dhcp socket
显示已经分配的地址 show ip dhcp binding
显示创建的地址池 show^ ip dhcp pool^
显示dhcp-server统计信息 show^ ip dhcp server statistic^
显示dhcp-relay统计信息 show ip dhcp relay statistic
显示冲突地址 show ip dhcp conflict

**查看调试信息**

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。

作用 命令
DHCPagent调试开关 debug ip dhcp server agent
DHCP热备调试开关 debug ip dhcp server^ ha^
DHCP地址池调试开关 debug ip dhcp server pool
DHCP VRRP调试开关 debug ip dhcp server vrrp
DHCP 打开所有调试开关 debug ip dhcp server all
DHCP报文调试开关 debug ip dhcp client
DHCP Relay事件调试开关。 debug ip dhcp relay


配置指南 DHCPv6

### 5 DHCPv6

#### 5.1 概述

DHCPv6（Dynamic Host Configuration Protocol for IPv6，IPv6动态主机配置协议）是一种允许DHCP Server将配置信息（如
IPv6网络地址）传递给IPv6节点的协议。

与其他IPv6地址分配方法（手工配置、无状态的地址自动配置）相比，DHCPv6提供了分配地址、Prefix Delegation（前缀代
理）、配置参数分配的功能。

 DHCPv6是一种全状态的地址自动配置协议，提供了灵活地添加和重复使用网络地址的功能，能够记录分配的地址，增
强了网络的管理性。

 通过使用DHCPv6的前缀代理，上游网络设备可以为下游网络设备分派地址前缀，实现了灵活的站点级别的自动配置，
可以灵活地控制站点地址空间。

 DHCPv6的配置参数分配可以解决在无状态地址自动配置协议下无法获取参数的问题，为主机提供如DNS服务器地址和
域名等配置信息。

DHCPv6是一种Client/Server模型的协议。DHCPv6 Client用于获取各类配置信息；DHCPv6 Server用于提供各类配置信息。
如果DHCPv6 Client和DHCPv6 Server不在同一网络链路时，还可以通过DHCPv6 Relay进行交互。

DHCPv6 Client通常是通过链路范围内保留组播地址来发现DHCPv6 Server，因此DHCPv6 Client和DHCPv6 Server必须能
够直接通信，也就是说需要部署在相同的链路内。这给实际用户会带来管理上的不方便，经济上的浪费（如果每个子网都部署
一台DHCPv6 Server），升级不方便等麻烦。而DHCPv6 Relay Agent功能，允许DHCPv6 Client发送报文到处于不同链路上
的DHCPv6 Server，从而解决这些问题。DHCP Relay Agent通常都可以部署在DHCPv6 Client的链路内，主要用来中继
DHCPv6 Client和DHCPv6 Server之间的交互报文。DHCP Relay Agent对于客户端而言是透明的。

图 5 - 1

### 下文仅介绍DHCPv6的相关内容。^


配置指南 DHCPv6

**协议规范**

 RFC3315：Dynamic Host Configuration Protocol for IPv6

 RFC3633：IPv6 Prefix Options for Dynamic Host Configuration Protocol (DHCP) Version 6

 RFC3646：DNS Configuration Options for Dynamic Host Configuration Protocol for IPv6 (DHCPv6)

 RFC3736：Stateless DHCP Service for IPv6

 RFC5417 : Control And Provisioning of Wireless Access Points (CAPWAP) Access Controller DHCP Option

#### 5.2 典型应用

典型应用 场景描述
请求\分配地址、配置参数 DHCPv6 Client向DHCPv6 Server请求地址信息；DHCPv6 Server为其分配地址和配置参数
请求\分配前缀 DHCPv6 Client向DHCPv6 Server请求前缀信息；DHCPv6 Server为其分配前缀，DHCPv6
Client再以该前缀配置IPv6地址
中继服务 通过DHCPv6中继，使处于不同链路上的DHCPv6 Client和DHCPv6 Server进行通信。

###### 5.2.1 请求 \ 分配地址、配置参数

**应用场景**

在一个子网内，DHCPv6 Client向DHCPv6 Server请求地址信息；DHCPv6 Server为其分配地址和配置参数

以下图为例：

 DHCPv6 Server上配置了可供分配的IPv6地址和DNS Server、域名等配置参数信息。

 主机作为DHCPv6 Client向DHCPv6 Server请求分配IPv6地址，DHCPv6 Server收到请求后，从配置的地址中选择一
个可用的分配给主机。

 主机还可以向DHCPv6 Server请求分配DNS Server、域名等配置参数信息。

图 5 - 2


配置指南 DHCPv6

**功能部署**

 在子网内主机运行DHCPv6 Client，获取IPv6地址和参数。

 在DHCP Server设备上运行DHCPv6 Server并配置地址及参数，实现地址和参数的分配。

###### 5.2.2 请求 \ 分配前缀

**应用场景**

以下图为例，上游设备（PE）为下游设备（CPE）分配IPv6地址前缀，CPE根据得到的地址前缀为内部子网生成新的地址前
缀，CPE内部子网内的主机就以新的地址前缀通过RA（Router Advertisement）完成自己的地址配置。

 PE作为DHCPv6 Server提供前缀代理服务，配置好地址前缀信息。

 CPE作为DHCPv6 Client向PE请求地址前缀，在获取到地址前缀后，为内部子网生成新的地址前缀，并向内部子网内
主机发送RA（Router Advertisement）。

 CPE内部子网内的主机就可以根据CPE发送的RA完成自己的地址配置。

图 5 - 3


配置指南 DHCPv6

【注释】 PE（Provider Edge），作为DHCPv6 Server，又叫Delegating Router ，提供前缀信息。
CPE（Customer Premises Equipment），作为DHCPv6 Client，又叫Requesting Router，请求前缀信息。
A、B、C为各种类型主机

**功能部署**

 在PE运行DHCPv6 Server，实现前缀代理服务。

 在CPE运行DHCPv6 Client，实现地址前缀的获取。

 在CPE和主机之间部署IPv6 ND，实现通过RA配置子网内主机地址。

###### 5.2.3 中继服务

**应用场景**

DHCPv6 Relay Agent为处于不同链路上的DHCPv6 Client和DHCPv6 Server提供中继服务，使得二者可以进行通信。

以下图为例：

 Device1 开启DHCPv6 Relay Agent并且目的地址指向3001::2；

 Device2由于希望通过下一级Relay继续处理转到其他服务器，所以开启DHCPv6 Relay Agent并且目的地址指向
FF02::1:2（所有服务器和Relay组播地址），出接口指定为上联目标地址的三层接口为gi 0/1。

图 5 - 4


配置指南 DHCPv6

**功能部署**

 在Device1上启用DHCPv6 Relay Agent，并将地址指定为3000::1。

 在Device2上启用DHCPv6 Relay Agent，并将地址指定为FF02::1:2。

#### 5.3 功能详解

**基本概念**

######  DUID

DUID（DHCP Unique Identifier）即DHCP唯一标识。RFC3315中明确定义，每一台DHCPv6设备（包括客户端、中继和服
务器）都必须拥有一个DHCPv6唯一标识，并用于在设备之间交换DHCPv6消息时相互验证。

RFC3315上规定了三种类型的DUID：

 DUID-LLT：DUID Based on Link-Layer address plus Time，链路地址加时间。

 DUID-EN：DUID Assigned by Vendor Based on Enterprise Number，厂商私有ID加企业内部编号。

 DUID-LL：Link-Layer address，链路地址。

锐捷DHCPv6设备采用的DUID类型是DUID-LL。DUID-LL的结构如下：


配置指南 DHCPv6

其中，DUID type为DUID 类型，DUID-LL 类型取值为0x0003；Hardware type为硬件类型，设备支持的硬件类型为以太网，
取值为0x0001；Link layer address为链路层地址，取值为设备的MAC 地址。

######  标识联盟（ IA ）

在DHCPv6中Server分配给Client的地址信息是一个集合（Identity association，IA），DHCPv6 Server以IA为单位进行地
址分配，每一个IA都由IAID唯一标识。IAID（Identity association identifier）由DHCPv6 Client生成。IA与Client成一一对
应关系，一个IA中可以包含多个地址，Client可以将IA中的地址分配给设备上的其他接口。IA中可以包含的地址有以下三类：

 NA：Non-temporary Addresses，全球唯一地址；

 TA：Temporary Addresses，临时地址（基本没有相关应用）；

 PD：Prefix Delegation，前缀空间；

因此根据IA中包含的地址不同，IA又分为IA_NA、IA_TA、IA_PD三种类型（IA-Type）。锐捷DHCPv6 Server支持分配IA_NA
和IA_PD，不支持IA_TA

######  绑定（ Binding ）

DHCPv6的绑定（DHCPv6 Binding）是一组可管理的信息结构。在Server上的绑定中，记录着分配给每个Client的IA和其
他配置信息。每个Client可以申请多个绑定，Server上的绑定以绑定表的形式组织，包含IA的绑定以DUID、IA-Type、IAID
为索引，包含配置信息的绑定以DUID为索引。

######  地址冲突

DHCPv6的地址冲突(DHCPv6 conflict)是指当DHCPv6 Client自身分配的地址存在冲突，Client发送Decline报文通知Server
本地址存在重复绑定，Server将本地址添加到地址冲突队列中。只要存在于该队列中的地址，之后Server将不再把该地址分
配出去，Server支持查看和清除地址冲突队列中的地址信息的功能。

######  报文类型

RFC3315规定DHCPv6使用 546 和 547 端口和UDP进行报文交互，DHCPv6 Client在 546 端口上接收报文，DHCPv6 Server
和DHCPv6 Relay在 547 端口上接收报文。RFC3315定义DHCPv6 Server、DHCPv6 Client、DHCPv6 Relay之间可以收发
的报文类型，如下：

 DHCPv6 Client允许发送给DHCPv6 Server的报文类型包括：Solicit、Request、Confirm、Renew、Rebind、Release、
Decline、Information-request。

 DHCPv6 Server允许发送给DHCPv6 Client的报文类型包括：Advertise、Reply、Reconfigure。

 DHCPv6 Relay允许发送给DHCPv6 Relay或DHCPv6 Server的报文类型包括：Relay-forward。

 DHCPv6 Server或DHCPv6 Relay允许发送给DHCPv6 Relay的报文类型包括：Relay-reply。


配置指南 DHCPv6

### 锐捷DHCPv6 Server不支持Reconfigure报文类型。^

### 锐捷DHCPv6 Client不支持Confirm、Reconfigure报文类型。^

**功能特性**

功能特性 作用
请求\分配地址 通过Client/Server模式在网络中动态获取\分配IPv6地址。
请求\分配前缀 通过Client/Server模式在网络中动态获取\分配IPv6前缀。
无状态服务 为网络中主机提供无状态的参数自动配置服务。
中继服务 通过Relay为不在同一网络中的主机提供DHCPv6 Server服务。

###### 5.3.1 请求 \ 分配地址

DHCPv6 Client可以向网络中的DHCPv6 Server请求IPv6网络地址信息。

DHCPv6 Server配置可用的地址后，可以为网络中的主机提供IPv6网络地址，并记录所分配的地址，能够提高网络管理性。

**工作原理**

网络中主机作为DHCPv6 Client与DHCPv6 Server通过消息交互完成地址的分配、更新、确认、释放等操作。

######  四次消息交互

四次消息交互的过程如图所示：

图 5 - 5


配置指南 DHCPv6

 DHCPv6 Client在本链路内发送一个目的地址为FF02::1:2，目的端口 547 的SOLICIT消息来请求地址分配、前缀分配、
配置参数分配。本链路内的所有DHCPv6 Server或者DHCPv6 Relay Agent都会收到SOLICIT消息。

 DHCPv6 Server收到SOLICIT消息后，如果本地可以提供SOLICIT消息里的请求信息，则以单播方式回应一个
ADVERTISE消息，包含了DHCPv6 Server所能提供的地址、前缀、配置参数等信息。

 DHCPv6 Client可能收到多个DHCPv6 Server发送的ADVERTISE消息。选择最合适的DHCPv6 Server后，DHCPv6
Client发送一个目的地址为FF02::1:2，目的端口 547 的REQUEST消息请求地址分配、前缀分配、配置参数分配。

 DHCPv6 Server收到REQUEST消息后，本地创建绑定信息，并单播回应一个REPLY消息，包含了DHCPv6 Server
将要分配给DHCPv6 Client的地址、前缀、配置参数等信息。DHCPv6 Client根据REPLY消息里的信息完成地址分配、
前缀分配或配置参数分配。

######  二次消息交互

如果DHCPv6 Client需要更短的配置时间时，可以通过两次消息交互完成地址、前缀、参数配置。

图 5 - 6

 DHCPv6 Client在本地链路内发送一个目的地址为FF02::1:2，目的端口为 547 的SOLICIT消息，同时SOLICIT消息里
面包含Rapid Commit选项，来请求地址分配、前缀分配、配置参数消息分配。

 如果DHCPv6 Server支持处理Rapid Commit选项，在本地创建绑定信息，并单播回应一个REPLY消息，包含了将要
分配给DHCPv6 Client的地址、前缀、配置参数等信息。DHCPv6 Client根据REPLY消息里的信息完成配置。

######  更新和重新绑定

DHCPv6 Server在发给DHCPv6 Client消息中的IA中提供了控制地址和更新的参数T1和T2。

图 5 - 7


配置指南 DHCPv6

 T1的值表示在T1秒后，DHCPv6 Client需要向DHCPv6 Server发送一个Renew多播消息进行地址和前缀的更新。Renew
消息里包含了DHCPv6 Server的DUID，需要更新的IA信息等内容。

 DHCPv6 Server收到Renew消息后，如果Renew消息中的DUID值等于本设备的DUID值，则更新本地的绑定，并以
单播的方式回应一个Reply消息，包含新的T1和其他参数值。

图 5 - 8

 T2的值表示DHCPv6 Client向DHCPv6 Server发送Renew消息后，一直没有收到响应，当到达T2时间后，需要向
DHCPv6 Server发送一个Rebind多播消息进行地址和前缀的重新绑定。

 DHCPv6 Server（可能是新的DHCPv6 Server）收到Rebind后，根据Rebind的内容单播回应一个Reply报文。

######  释放


配置指南 DHCPv6

如果DHCPv6 Client需要释放一个地址或前缀时，通过向DHCPv6 Server发送一个Release消息通知DHCPv6 Server不再
使用的地址或前缀，以便DHCPv6 Server能够将这些地址和前缀再次分配给其他DHCPv6 Client。

图 5 - 9

 DHCPv6 Server收到Release消息后，根据Release消息里的地址或前缀信息移除相关绑定，并回复一个携带状态选项
的Reply消息给DHCPv6 Client。

######  确认

DHCPv6 Client如果移动到新的链路（ 如发生重启），则会发送一个Confirm消息来向新链路里的DHCPv6 Server确认原来
的地址是否仍然可用。

图 5 - 10

 DHCPv6 Server收到Confirm消息后，根据Confirm消息里的地址信息进行确认，并回复一个携带状态选项的Reply消
息给DHCPv6 Client。如果确认失败，DHCPv6 Client可能重新发起地址分配请求。

######  地址冲突


配置指南 DHCPv6

DHCPv6 Client完成地址分配后，如果在链路上检测到所分配地址已被使用，则发送Decline消息通知DHCPv6 Server存在
地址冲突。

图 5 - 11

 DHCPv6 Client在Decline消息里包含冲突地址的IA信息。

 DHCPv6 Server收到Decline消息后，将Decline消息里的地址标记为“declined”，不会在后续的地址分配中使用这些
地址，然后回复一个携带状态选项的Reply消息给DHCPv6 Client。标记为“declined”的地址，可以通过手工清除，以
便可以重新分配。

**相关配置**

######  启用接口上的 DHCPv6 Server 功能

 缺省情况下，接口上的DHCPv6 Server功能未启用。

 使用ipv6 dhcp server 命令可以启用或停用接口上的DHCPv6 Server功能。

### 只能在三层接口上启用DHCPv6 Server功能。^

######  DHCPv6 Server 分配地址

 缺省情况下，DHCPv6 Server没有创建信息池和配置可分配的地址。

 使用ipv6 dhcp pool命令可以创建信息池。

 使用iana-address命令可以配置可分配的地址，以及地址的preferred lifetime和valid lifetime值。

######  DHCPv6 Server 清除冲突地址

 缺省情况下，DHCPv6 Server检测到的冲突地址不会清除。

 使用clear ipv6 dhcp conflict命令可以清除冲突的地址，以便在后续的地址分配中可以继续使用这些地址。

######  启用接口上的 DHCPv6 Client 请求地址功能

 缺省情况下，接口上的DHCPv6 Client地址请求功能未启用。


配置指南 DHCPv6

 使用ipv6 dhcp client ia 命令可以启用或停用接口上的DHCPv6 Client请求地址功能。

### 只能在三层接口上启用DHCPv6^ Client请求地址功能。^

###### 5.3.2 请求 \ 分配前缀

在DHCPv6 Server上配置可用的前缀，通过使用DHCPv6的前缀代理，上游网络设备可以为下游网络设备分派地址前缀，实
现了灵活的站点级别的自动配置，可以灵活地控制站点地址空间。

**工作原理**

下游网络设备作为DHCPv6 Client与DHCPv6 Server通过消息交互完成前缀的分配、更新、释放等操作。下游网络设备通过
与分配地址一样的机制进行四次消息交互、两次消息交互获取前缀信息，进行前缀信息的更新和重新绑定，进行前缀的释放。
但也与分配地址存在一些差异。

 前缀代理的消息交互中，没有使用到Confirm和Decline消息。

 如果DHCPv6 Client移动到新的链路，需要确认前缀信息是否可用时，使用Rebind和Reply的消息交互机制进行重新确
认。

 各类消息里的IA类型是IA_PD，而不是IA_NA。

### 前缀代理的消息交互参照请求\分配地址^

**相关配置**

######  启用接口上的 DHCPv6 Server 功能

 缺省情况下，接口上的DHCPv6 Server功能未启用。

 使用ipv6 dhcp server 命令可以启用或停用接口上的DHCPv6 Server功能。

### 只能在三层接口上启用DHCPv6 Server功能。^

######  DHCPv6 Server 前缀代理

 缺省情况下，DHCPv6 Server没有创建信息池和配置前缀信息。

 使用ipv6 dhcp pool命令可以创建信息池。

 使用prefix-delegation命令可为特定的DHCPv6 Client分配指定的前缀信息

 使用prefix-delegation pool配置前缀信息池，后续所有的DHCPv6 Client请求的前缀信息都从该池中分配。

######  启用接口上的 DHCPv6 Client 请求前缀功能

缺省情况下，接口上的DHCPv6 Client请求前缀功能未启用。

使用ipv6 dhcp client pd 命令可以启用或停用接口上的DHCPv6 Client请求前缀功能。

### 只能在三层接口上启用DHCPv6 Client请求前缀功能。^


配置指南 DHCPv6

###### 5.3.3 无状态服务

DHCPv6 Client在只需要配置参数信息，而不需要地址或前缀信息时，通过DHCPv6无状态服务，可以获取相关的配置参数
信息，解决了在无状态地址自动配置协议下无法获取参数的问题，如DNS Server地址。

**工作原理**

网络中主机作为DHCPv6 Client与DHCPv6 Server通过消息交互完成配置参数的获取、更新等操作，

######  无状态服务消息交互

图 5 - 12

 DHCPv6 Client向DHCPv6 Server发送一个Information-request消息，即可请求无状态信息，该消息里通常没有包含特
定DHCPv6 Server的DUID。

 DHCPv6 Server向DHCPv6 Client回复一个包含配置参数信息的Reply报文。

**相关配置**

######  启用接口上的 DHCPv6 Server 功能

 缺省情况下，接口上的DHCPv6 Server功能未启用。

 使用ipv6 dhcp server 命令可以启用或停用接口上的DHCPv6 Server功能。

### 只能在三层接口上启用DHCPv6 Server功能。^

######  DHCPv6 Server 的无状态服务

 缺省情况下，DHCPv6 Server没有创建信息池和配置参数信息。

 使用ipv6 dhcp pool命令可以创建信息池。

 使用dns-server命令可以添加DNS Server列表信息。


配置指南 DHCPv6

 使用domain-name命令可以添加域名列表信息。

 使用option52命令可以添加CAPWAP AC的 IPv6地址信息。

######  DHCPv6 Client 的无状态服务

 缺省情况下，接口上的DHCPv6 Client无状态服务未启用。

 主机收到的RA通告里面设置了O标记，则会使DHCPv6 Client启动无状态服务。

###### 5.3.4 中继服务

当DHCPv6 Client与DHCPv6 Server不在同一链路上时，DHCPv6 Client可以通过DHCPv6 Relay Agent将相关的消息中继
到DHCPv6 Server，DHCPv6 Server在处理后，也将响应消息通过Relay Agent中继到DHCPv6 Client。

**工作原理**

当DHCPv6 Relay Agent收到来自DHCPv6 Client消息时，会创建一个Relay-forward消息，该消息中包含了原始的DHCPv6
Client消息以及Relay Agent可能添加的一些选项信息。然后将Relay-forward发往指定的DHCPv6 Server或者特定的多播地
址FF05::1:3。

当DHCPv6 Server接收到Relay-forward消息后，将封装在Relay-forward消息里的原始DHCPv6 Client消息提取出来并进行
处理。DHCPv6 Server接着对该原始消息进行响应，并将响应消息封装Relay-reply消息，然后发送给DHCPv6 Relay Agent。

当DHCPv6 Relay Agent收到Relay-reply消息时，将封装在Relay-reply消息中的原始DHCPv6 Server消息提取出来并转发
给DHCPv6 Client。

在DHCPv6 Client和DHCPv6 Server之间还允许有多级的Relay Agent。

######  DHCPv6 Relay Agent

图 5 - 13

 DHCPv6 Relay Agent在DHCPv6 Client和DHCPv6 Server之间进行报文的封装和解封装，解决DHCPv6 Client和
DHCPv6 Server不在同一链路的问题。


配置指南 DHCPv6

###### 5.3.5 中继源接口指定功能

当DHCPv6 Server无法通过上联口IP识别唯一的DHCPv6 Relay时，采用指定源接口的方式可区分不同的DHCPv6 Relay
设备，确保报文转发正常。

**工作原理**

源接口指定功能允许指定IP地址或者接口，DHCPv6 Relay转发报文到DHCPv6 Server时，采用指定的信息填充到中继转发
报文Relay-forward的源IP地址中，而其目的IP地址仍然为DHCPv6 Server的IP地址；DHCPv6 Server收到Relay-forward
报文后，将记录该报文的源IP地址，作为其应答报文Relay-reply的目的地址，即应答报文指向的是中继设备上的源接口指定
功能配置的指定IP地址或者接口，从而实现绕过DHCPv6 Relay上联口的问题。

**相关配置**

######  全局 / 接口配置模式下启用源接口指定功能

 缺省情况下，未指定任何的源接口信息。

 使用ipv6 dhcp relay source命令可以配置或删除全局上的源接口指定功能配置信息。

 使用show ipv6 dhcp relay source可以查看相应的源接口指定功能配置信息。

### ²^ 接口配置模式下，只能在三层接口上启用源接口指定功能。^

#### 5.4 配置详解

配置项 配置建议 & 相关命令

配置DHCPv6 Server

### 必须配置。用于创建&配置信息池。^

```
ipv6 dhcp pool 配置DHCPv6 Server的信息池。
```

### 可选配置。用于分配地址。^

```
iana-address prefix 配置DHCPv6 Server上可分配的地址前缀。
```

### 可选配置。用于分配前缀。^

```
prefix-delegation 配置DHCPv6 Server的静态绑定地址前缀信息。
prefix-delegation pool 配置DHCPv6 Server通过本地前缀池分配前缀。
```

ipv6 local pool (^) 配置IPv6的本地前缀池。

### 可选配置。用于分配配置参数^

dns-server (^) 配置DHCPv6 Server的DNS Server列表信息。
domain-name 配置DHCPv6 Server的domain name信息。
option52 配置DHCPv6 Server的CAPWAP AC的 ipv6地址信息。


配置指南 DHCPv6

### 必须配置。用于启用DHCPv6 Server服务。^

```
ipv6 dhcp server 配置接口上启用DHCPv6 Server服务。
```

配置DHCPv6 Relay

### 必须配置。用于启用DHCPv6 Relay服务。^

```
ipv6 dhcp relay destination
ipv6 dhcp relay source
```

```
配置DHCPv6 Relay Agent功能。
配置DHCPv6 Relay的源接口指定功能
```

配置DHCPv6 Client

### 必须配置。用于请求地址信息或前缀信息。^

```
ipv6 dhcp client ia 启用DHCPv6 Client并请求IANA地址信息。
ipv6 dhcp client pd 启用DHCPv6 Client并请求地址前缀信息。
```

### 可选配置。使收到RA通告的主机通过DHCPv6 Client请求无状态服务。^

```
ipv6 nd other-config-flag
```

```
在发送RA通告的设备上设置RA里的O标识，
使收到RA通告的主机通过DHCPv6 Client请
求无状态服务。
```

###### 5.4.1 配置 DHCPv6 Server

**配置效果**

 上游设备能自动为下游设备分配DHCPv6地址、前缀及相关配置参数。

**注意事项**

 要提供DHCPv6 Server服务，必须指定DHCPv6 Server信息池。

 配置的信息池的名字不能过长。

 启用DHCPv6 Server服务时，必须指定一个信息池。

 只支持SVI（Switch Virtual Interface）、ROUTED PORT、L3 AP三层接口上配置。

**配置方法**

######  配置 DHCPv6 Server 信息池

 必须配置。

 若无特殊要求，应在每台需要提供DHCPv6 Server服务的设备上配置信息池。

######  配置 DHCPv6 Server 上可分配的地址前缀

 可选配置。


配置指南 DHCPv6

 若要提供分配地址服务，应在每台需要提供DHCPv6 Server服务的设备上配置可分配的地址前缀。

######  配置 DHCPv6 Server 的静态绑定地址前缀信息

 可选配置。

 若要提供静态绑定地址前缀代理服务，应在每台需要提供DHCPv6 Server服务的设备上配置静态绑定地址前缀信息。

######  配置 DHCPv6 Server 通过本地前缀池分配前缀

 可选配置。

 若要提供前缀代理服务，应在每台需要提供DHCPv6 Server服务的设备上指定本地前缀池。

######  配置 IPv6 的本地前缀池

 可选配置。

 若要提供通过前缀池的前缀代理服务，应在每台需要提供DHCPv6 Server服务的设备上配置本地前缀池。

######  配置 DHCPv6 Server 的 DNS Server 列表信息

 可选配置。

 若要提供DNS Server信息，应在每台需要提供DHCPv6 Server服务的设备上配置DNS Server信息。

######  配置 DHCPv6 Server 的 domain name 信息

 可选配置。

 若要提供Domain name信息，应在每台需要提供DHCPv6 Server服务的设备上配置domain name信息。

######  配置 DHCPv6 Server 的 CAPWAP AC 的 ipv6 地址信息

 可选配置。

 若要提供CAPWAP AC信息，应在每台需要提供DHCPv6 Server服务的设备上配置CAPWAP AC信息。

######  配置启用 DHCPv6 Server 服务

 必须配置。

 若无特殊要求，应在每台需要提供DHCPv6 Server服务的设备上的具体接口配置启用DHCPv6 Server服务。

**检验方法**

DHCPv6 Server成功为DHCPv6 Client提供地址、前缀或配置参数信息。

 DHCPv6 Client获取到所需的信息。

 DHCPv6 Server本地成功创建绑定。

**相关命令**


配置指南 DHCPv6

######  配置 DHCPv6 Server 信息池

```
【命令格式】 ipv6 dhcp pool poolname
【参数说明】 poolname: 用户定义的DHCPv6池名字。
【命令模式】 全局模式
【使用指导】 使用ipv6 dhcp pool命令来创建一个DHCPv6 Server的配置信息池。配置该命令之后，将进入DHCPv6池
配置模式，在这种模式下，管理员可以配置池的参数，例如前缀信息以及DNS Server信息等。
DHCPv6 Server的配置信息池创建之后，可以使用ipv6 dhcp server命令将该池与某个接口上的DHCPv6
Server关联起来。
```

######  配置 DHCPv6 Server 的 IA_NA 地址前缀

```
【命令格式】 iana-address prefix ipv6-prefix/prefix-length [ lifetime { valid-lifetime | preferred-lifetime } ]
【参数说明】 ipv6-prefix/prefix-length：IPv6地址前缀和前缀长度。
lifetime: 用来设置客户端可以使用分配到的地址的有效时间。如果该关键字配置，则valid-lifetime和
preferred-lifetime都要配置。
valid-lifetime: 客户端可以有效使用该地址的时间。
preferred-lifetime: 地址仍然被优先分配给客户端的时间。
【命令模式】 接口模式
【使用指导】 iana-address prefix命令为DHCPv6 Server配置了IA_NA地址范围，可以从中分配IA_NA地址给客户端。
当Server收到客户端的IA_NA地址请求时，将尝试从IA_NA地址范围中选取一个可用的地址分配给客户端。
当客户端不再使用该地址时，Server将该地址标记可用以提供给其他客户端使用。
```

######  配置 DHCPv6 Server 的静态绑定地址前缀信息

```
【命令格式】 prefix-delegation ipv6-prefix/prefix-length client-DUID [ lifetime ]
【参数说明】 ipv6-prefix/prefix-length：IPv6地址前缀和前缀长度。
client-DUID：客户端的DUID。
lifetime：设定客户端可以使用这个前缀的时间间隔。
【命令模式】 DHCPv6 池配置模式
【使用指导】 管理员可以使用prefix-delegation命令为客户端的IA_PD手动配置一个地址前缀信息列表，并为这些前缀配
置有效时间。
参数client-DUID指定了哪个客户端将分配到该地址前缀，该地址前缀将分配给客户端中第一个IA_PD。
DHCPv6 Server收到客户端对地址前缀的request消息之后，先查找是否有对应的静态绑定，如果找到则直
接返回该静态绑定；否则，Server将尝试从另外的前缀信息源来分配地址前缀。
```

######  配置 DHCPv6 Server 通过本地前缀池分配前缀

```
【命令格式】 prefix-delegation pool poolname [lifetime { valid-lifetime | preferred-lifetime } ]
【参数说明】 poolname：用户定义的本地前缀池的名字。
lifetime：用来设置客户端可以使用分配到的前缀的有效时间。如果该关键字配置，则valid-lifetime 和
preferred-lifetime都要配置。
valid-lifetime：客户端可以有效使用该前缀的时间。
preferred-lifetime：前缀仍然被优先分配给客户端的时间。
【命令模式】 DHCPv6 池配置模式
```

配置指南 DHCPv6

```
【使用指导】 prefix-delegation pool命令为DHCPv6 Server配置了前缀池，可以从中分配前缀信息给客户端。使用ipv6
local pool命令来配置前缀池。
当Server收到客户端的前缀请求时，将尝试从前缀池中选取一个可用的前缀分配给客户端。当客户端不再使
用该前缀时，Server将该前缀返回前缀池以提供给其他客户端使用。
```

######  配置 IPv6 本地前缀池

```
【命令格式】 ipv6 local pool poolname^ prefix/prefix-length assigned-length^
【参数说明】 poolname：本地前缀池名字。
prefix/prefix-length：前缀和前缀长度。
assigned-length：分配给用户的前缀长度。
【命令模式】 全局模式
【使用指导】 使用ipv6 local pool创建本地前缀池，DHCPv6 Server如果需要进行前缀代理，使用prefix-delegation pool
指定本地前缀池，后续的前缀将从指定的本地前缀池中分配。
```

######  配置 DHCPv6 Server 的 DNS Server 列表信息

```
【命令格式】 dns-server ipv6-address
【参数说明】 ipv6-address：DNS Server的地址。
【命令模式】 DHCPv6 池配置模式
【使用指导】 可以多次使用dns-server命令来配置多个DNS Server地址。新配置的DNS Server地址不会覆盖旧的DNS
Server地址。
```

######  配置 DHCPv6 Server 的 domain name 信息

```
【命令格式】 domain-name domain
【参数说明】 domain：定义要分配给用户的domain-name名字。
【命令模式】 DHCPv6 池配置模式
【使用指导】 可以多次使用domain-name 命令来创建多个domain-name。新配置的domain-name 不会覆盖旧的
domain-name。
```

######  配置 DHCPv6 Server 的 option52 信息

【命令格式】 option52^ ipv6-address^
【参数说明】 ipv6-address ：指定CAPWAP AC的ipv6地址。
【命令模式】 DHCPv6 池配置模式
【使用指导】 可以多次使用option52命令来创建多个CAPWAP AC的ipv6-address。新配置的CAPWAP AC ipv6-address
不会覆盖旧的ipv6-address。

######  配置启用 DHCPv6 Server 服务

```
【命令格式】 ipv6 dhcp server poolname [rapid-commit] [preference value]
【参数说明】 poolname：用户定义的DHCPv6池名字。
rapid-commit：允许使用two-message交互过程。
preference value：配置advertise消息的优先级。取值范围<0-255>，默认值为 0 。
【命令模式】 接口配置模式
```

配置指南 DHCPv6

```
【使用指导】 ipv6 dhcp server命令在接口上启用DHCPv6服务。
rapid-commit关键字允许在分配地址前缀以及其他配置信息时，和客户端进行two-message的交互过程。配
置了该关键字后，如果客户端的solicit消息中包含rapid-commit选项，那么DHCPv6 Server将直接以Reply
消息回复。
preference如果配置为非 0 的值，那么DHCPv6 Server在发送advertise消息时会携带preference选项。
preference选项字段会影响客户端对Server的选取，如果advertise消息不包含该字段，则认为preference
为 0 ，如果客户端收到preference值为 255 ，则立即向该Server发出request消息来获取配置信息。
DHCPv6 Client、Server以及Relay功能是互斥的，一次只能有一种模式能够在接口上配置。
```

**配置举例**

######  配置 DHCPv6 Server

```
【配置方法】  配置一个名为“pool1”的信息池
 配置DHCPv6 Server的IA_NA地址前缀
 配置DHCPv6 Server的静态绑定地址前缀信息。
 配置两个DNS Server。
 配置域名。
 在接口启用DHCPv6 Server服务。
Ruijie# configure terminal
Ruijie(config)# ipv6 dhcp pool pool1
Ruijie(config-dhcp)# iana-address prefix 2008:50::/64 lifetime 2000 1000
Ruijie(config-dhcp)# prefix-delegation 2008:2::/64 0003000100d0f82233ac
Ruijie(config-dhcp)# dns-server 2008:1::1
Ruijie(config-dhcp)# dns-server 2008:1:: 2
Ruijie(config-dhcp)# domain-name example.com
Ruijie(config-dhcp)#exit
Ruijie(config)# interface GigabitEthernet 0/1
Ruijie(config-if)# ipv6 dhcp server pool1
```

```
【检验方法】  使用show ipv6 dhcp pool查看创建的信息池。
Ruijie# show ipv6 dhcp pool
DHCPv6 pool: pool1
Static bindings:
Binding for client 0003000100d0f82233ac
IA PD prefix: 2008:2::/64
preferred lifetime 3600, valid lifetime 3600
IANA address range: 2008:50::1/64 -> 2008:50::ffff:ffff:ffff:ffff/64
preferred lifetime 1000, valid lifetime 2000
DNS server: 2008:1::1
DNS server: 2008:1::2
Domain name: example.com
```

配置指南 DHCPv6

**常见错误**

 指定了过长的poolname。

 配置的信息池数目超出系统限制 256 个。

 在非SVI（Switch Virtual Interface）、ROUTED PORT、L3 AP三层接口上配置。

 配置DHCPv6 Server服务的接口数目超过系统限定值 256 个。

 指定的valid lifetime值比preferred lifetime值小。

 指定非法的IA_NA地址。

 配置的地址范围个数超过系统的限定值 20 个。

 配置静态绑定地址前缀信息时，指定了过长的DUID。

 配置静态绑定地址前缀的数目超过系统的限定值 1024 个。

 配置本地前缀池时，错误指定valid lifetime的时间大于preferred lifetime。

 配置的DNS Server个数超过系统限定值 10 个。

 配置的Domain Name个数超过系统限定值 10 个。

 配置的option52地址个数超过系统限定值 10 个。

###### 5.4.2 配置 DHCPv6 Relay

**配置效果**

 处于不同链路的DHCPv6 Client和DHCPv6 Server可以通过Relay Agent建立通信，进行地址分配、前缀代理、参数分
配。

**注意事项**

 需要指定目的地址，如果目的地址为多播地址（如FF05::1:3）,还需要指定出接口。

**配置方法**

######  配置 DHCPv6 Relay Agent 功能

 必须配置。

 若无特殊要求，应在每台需要提供DHCPv6 Relay Agent的设备上配置DHCPv6 Relay功能。

**检验方法**


配置指南 DHCPv6

DHCPv6 Client和DHCPv6 Server通过Relay Agent进行报文交互。

 检查接口状态是否为DHCPv6 Relay模式。

 检查DHCPv6 Relay Agent是否可以正常收发报文。

**相关命令**

######  配置 DHCPv6 Relay Agent 功能

```
【命令格式】 ipv6 dhcp relay destination ipv6-address [interface-type interface-number]
【参数说明】 ipv6-address: 指定Relay Agent的目的端地址。
interface-type：指定到达目的端接口的类型（可选）。
interface-number：指定到达目的端接口的编号（可选）。
【命令模式】 接口配置
【使用指导】 开启Dhcpv6 Relay功能接口接收到的所有DHCPv6客户端报文都将被封装并朝指定接口（可选）发往配置
好的目的地址（如果配置多个目的地址，则同时发多份。）
```

**配置举例**

######  配置 DHCPv6 Relay

```
【配置方法】 指定开启Relay服务的接口对于接收到的DHCPv6 Client报文通过指定接口（可选）转发至指定目的地址
Ruijie#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)#interface vlan 1
Ruijie(config-if)#ipv6 dhcp relay destination 3001::2
Ruijie(config-if)#ipv6 dhcp relay destination ff02::1:2 vlan 2
```

```
【检验方法】 使用show ipv6 dhcp relay destination all查看配置的目的地址信息。
Interface:VLAN 1
Destination address(es) Output Interface
3001::2
ff02::1:2 VLAN 2
```

**常见错误**

 在非SVI（Switch Virtual Interface）、ROUTED PORT、L3 AP三层接口上配置。

###### 5.4.3 配置 DHCPv6 Client

**配置效果**


配置指南 DHCPv6

 实现设备自动向服务器请求IPv6地址，或相关参数。

**注意事项**

 只能在三层接口上配置。

**配置方法**

######  启用 DHCPv6 Client 并请求 IANA 地址信息。

 必须配置。

 若无特殊要求，应在每台需要通过DHCPv6请求地址的设备上启用DHCPv6 Client地址请求功能。

######  启用 DHCPv6 Client 并请求地址前缀信息。

 必须配置。

 若无特殊要求，应在每台需要通过DHCPv6请求前缀的设备上启用DHCPv6 Client前缀请求功能。

######  启用 DHCPv6 Client 无状态服务。

 需要获取配置参数信息时，必须配置。

**检验方法**

检查接口是否使能DHCPv6 Client和接口上获取到的地址、前缀等信息。

**相关命令**

######  启用 DHCPv6 Client 请求地址功能

```
【命令格式】 ipv6 dhcp client ia^ [^ rapid-commit^ ]^
【参数说明】 rapid-commit：允许使用简化的交互过程。
【命令模式】 接口配置模式
【使用指导】 如果DHCPv6客户端模式还没有打开，该命令会在接口上启用DHCPv6客户端模式。
ipv6 dhcp client ia命令启用之后会向DHCPv6 Server发出IANA地址请求。
rapid-commit关键字允许客户端和服务器端使用two-message交互过程，如果配置了该关键字，客户端发出
的solicit消息中将包含rapid-commit选项。
```

######  启用 DHCPv6 Client 前缀请求

```
【命令格式】 ipv6 dhcp client pd prefix-name [ rapid-commit ]
【参数说明】 prefix-name：IPv6通用前缀名。
rapid-commit：允许使用简化的交互过程。
【命令模式】 接口配置模式
```

配置指南 DHCPv6

```
【使用指导】 如果DHCPv6客户端模式还没有打开，该命令会在接口上启用DHCPv6客户端模式。
ipv6 dhcp client pd命令启用之后会向DHCPv6 Server发出前缀请求。得到前缀信息时，client会将这个前
缀信息保存在IPv6通用前缀池中，其他的命令以及应用程序就可以使用这个前缀。
rapid-commit关键字允许客户端和服务器端使用two-message交互过程，如果配置了该关键字，客户端发出
的solicit消息中将包含rapid-commit选项。
```

######  配置无状态服务

```
【命令格式】 ipv6 nd other-config-flag
【参数说明】 -
【命令模式】 接口配置模式
【使用指导】 在发送RA通告的主机上设置other-config-flag，则触发收到该RA通告的主机通过DHCPv6 Client获取无状
态配置信息。
```

**配置举例**

######  启用 DHCPv6 Client 请求地址功能

```
【配置方法】  在接口上配置DHCPv6 Client地址请求功能。
Ruijie(config)# interface GigabitEthernet 0/1
Ruijie(config-if)# ipv6 dhcp client ia
```

```
【检验方法】  使用show ipv6 dhcp interface命令可以检查接口上是否启用DHCPv6 Client。
Ruijie#show ipv6 dhcp interface GigabitEthernet 0/1
GigabitEthernet 0/1 is in client mode
Rapid-Commit: disable
```

######  启用 DHCPv6 Client 前缀请求

```
【配置方法】  在接口上配置DHCPv6 Client前缀请求功能。
Ruijie(config)# interface GigabitEthernet 0/1
Ruijie(config-if)# ipv6 dhcp client pd pd_name
```

```
【检验方法】  使用show ipv6 dhcp interface命令可以检查接口上是否启用DHCPv6 Client。
Ruijie#show ipv6 dhcp interface GigabitEthernet 0/1
GigabitEthernet 0/1 is in client mode
Rapid-Commit: disable
```

######  启用 DHCPv6 Client 无状态请求

```
【配置方法】  在提供RA通告设备的接口上配置other-config-flag。
Ruijie# configure terminal
Ruijie(config)# interface GigabitEthernet 0/1
Ruijie(config-if)# ipv6 nd other-config-flag
```

配置指南 DHCPv6

```
【检验方法】  使用show ipv6 dhcp interface命令可以检查主机的某个接口是否获取到的配置参数信息。
Ruijie#show ipv6 dhcp interface GigabitEthernet 0/ 2
GigabitEthernet 0/ 2 is in client mode
DNS server: 2001::1
Rapid-Commit: disable
```

**常见错误**

 在非三层接口上启用DHCPv6 Client地址请求。

 在已启用DHCPv6 Relay或者DHCPv6 Server的接口上启用DHCPv6地址请求。

 在非三层接口上启用DHCPv6 Client前缀请求。

 在已启用DHCPv6 Relay或者DHCPv6 Server的接口上启用DHCPv6前缀请求。

###### 5.4.4 配置源接口指定功能

**配置效果**

 指定DHCPv6 Relay转发报文的源IP地址和link address字段。

**注意事项**

 指定参数类型为接口时，该接口必须为三层口，且接口变更为非三层口后，将会删除对应的源接口指定配置信息。

**配置方法**

######  配置源接口 - 源 IP 地址指定功能

 可选配置。

 若仅要求改变转发报文的源IP地址信息，可在相应的接口或者全局配置源接口-源IP地址指定功能。

######  配置源接口 - 网关地址指定功能

 可选配置。

 若要求改变DHCPv6 Client获取到的网段信息，可在相应的接口或者全局配置源接口-网关地址指定功能。

**检验方法**

DHCPv6 Relay的转发报文中相应字段根据指定配置信息正确填充。


配置指南 DHCPv6

 抓包查看相应字段是否与源接口指定功能的配置信息一致。

 检查DHCPv6 Relay Agent是否可以正常收发报文。

**相关命令**

######  配置源接口指定功能

```
【命令格式】 ipv6 dhcp relay source {source-ip-address | gateway-address}^ {ipv6 address^ | interface-type
interface- number }
【参数说明】 source-ip-address ： 源接口-源IP地址指定类型，填充转发报文的源IP地址
gateway-address ： 源接口-网关地址指定类型，填充转发报文的源IP地址和link address字段
ipv6-address:：源接口的指定参数类型，IPv6地址
interface-type：源接口的指定参数类型，指定接口的接口类型
interface-number：源接口的指定参数类型，指定接口的接口编号
【命令模式】 全局/接口配置模式
【使用指导】 源接口指定功能会变更DHCPv6中继转发报文的源IP地址和link address字段；源接口指定功能的指定类型
分为源IP地址指定和网关地址指定，前者变更转发报文的源IP地址，后者变更转发报文的源IP地址和link
address字段。源接口指定功能允许配置于全局模式和接口模式，其中接口模式的源接口指定类型优先级大于
全局模式的；而同一个模式下，新配置的源接口指定类型覆盖旧的指定类型。
```

**配置举例**

######  配置源接口指定功能

```
【配置方法】 配置接口Interface VLAN 1上开启源接口指定功能，指定类型为源接口-网关地址，指定参数类型为IPv6地址；
全局模式上开启源接口指定功能，指定类型为源接口-源IP地址，指定参数类型为接口。
Ruijie# configure terminal^
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)# interface vlan 1
Ruijie(config-if)# ipv6 dhcp relay source gateway-address 1000::1
Ruijie(config-if)# exit
Ruijie(config)# ipv6 dhcp relay source source-ip-address loopback 0
Ruijie(config)#
```

```
【检验方法】 使用show ipv6 dhcp relay source 查看 设备当前源接口指定功能配置信息。
Ruijie#show ipv6 dhcp relay source
Interface-Name Source-Intf-Type Source-Intf-Parameter
Global Source Address Loopback 0
VLAN 1 Gateway Address 1000::1
```

**常见错误**


配置指南 DHCPv6

在非SVI（Switch Virtual Interface）、ROUTED PORT、L3 AP三层接口上配置

###### 5.4.5 配置网关地址自动切换功能

**配置效果**

 Dhcpv6 relay在client申请地址失败时，会变更转发报文中的link address字段。达到自动切换网段申请地址的目的

**注意事项**

 只能在三层接口上配置

**配置方法**

######  配置网关地址自动切换功能

 可选配置。

 若需要网关地址自动切换功能，需要在相应接口启用该功能。

**检验方法**

DHCPv6 Relay的转发报文中相应字段在申请地址失败时会自动变更。

 抓包查看在申请地址失败时，link address 字段会自动切换。

 检查DHCPv6 Relay Agent是否可以正常收发报文。

**相关命令**

######  配置源接口指定功能

```
【命令格式】 ipv6 dhcp smart-relay
【参数说明】 -^
【命令模式】 接口配置模式
【使用指导】 网关地址自动切换功能能够在设备申请ipv6地址失败后，自动变更转发报文中的link address字段，达到切
换网段申请地址的功能。
```

**配置举例**

######  配置源接口指定功能

```
【配置方法】 配置接口Interface VLAN 1上开启源接口指定功能，指定类型为源接口-网关地址，指定参数类型为IPv6地址；
```

配置指南 DHCPv6

```
全局模式上开启源接口指定功能，指定类型为源接口-源IP地址，指定参数类型为接口。
Ruijie# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)# interface vlan 1
Ruijie(config-if)# ipv6 dhcp smart-relay
Ruijie(config-if)# exit
```

```
【检验方法】 使用show run查看网关地址自动切换功能的配置信息。
Ruijie#show run
interface VLAN 1
ipv6 dhcp smart-relay
!
```

**常见错误**

在非SVI（Switch Virtual Interface）、ROUTED PORT、L3 AP三层接口上配置

#### 5.5 监视与维护

**清除各类信息**

### 在设备运行过程中执行clear命令，可能因为重要信息丢失而导致业务中断。^

作用 命令
清除DHCPv6绑定信息。 clear ipv6 dhcp binding [ ipv6-address ]
清除DHCPv6服务器统计信息。 clear ipv6 dhcp server statistics
清除DHCPv6 Server的冲突地址信
息。

```
clear ipv6 dhcp conflict { ipv6-address | * }
```

清除当前设备开启DHCPv6 Relay功
能后各类报文收发情况统计。

```
clear ipv6 dhcp relay statistics
```

重新启动DHCPv6 Client功能。 clear ipv6 dhcp client interface-type interface-number

**查看运行情况**

作用 命令
查看设备的DUID信息。 show ipv6 dhcp
查看DHCPv6 服务器的地址绑定信
息。

```
show ipv6 dhcp binding [ ipv6-address ]
```

查看DHCPv6接口信息。 show ipv6 dhcp interface [ interface-name ]
查看DHCPv6池信息。 show ipv6 dhcp pool [ poolname ]


配置指南 DHCPv6

查看DHCPv6的冲突地址信息。 show ipv6 dhcp conflict
查看DHCPv6 Server的统计信息。 show ipv6 dhcp server statistics
查看DHCPv6 Relay Agent目的端地
址信息。

```
show ipv6 dhcp relay destination { all | interface-type interface-number }
```

查看当前设备开启DHCPv6 Relay功
能后各类报文收发情况。

```
show ipv6 dhcp relay statistics
```

查看IPv6本地前缀池信息。 show ipv6 local pool [ poolname ]
查看源接口指定功能的配置信息 show ipv6 dhcp relay source^

**查看调试信息**

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。^

作用 命令
打开DHCPv6 调试开关。 debug ipv6 dhcp [ detail ]


配置指南 DNS

### 6 DNS

#### 6.1 概述

DNS（Domain Name System，域名系统），因特网上作为域名和IP地址相互映射的一个分布式数据库，能够使用户更方便的
访问互联网，而不用去记住能够被机器直接读取的IP数串。通过主机名，最终得到该主机名对应的IP地址的过程叫做域名解
析（或主机名解析）。

### 下文仅介绍DNS的相关内容。^

**协议规范**

 RFC1034：DOMAIN NAMES - CONCEPTS AND FACILITIES

 RFC1035：DOMAIN NAMES - IMPLEMENTATION AND SPECIFICATION

#### 6.2 典型应用

典型应用 场景描述
静态域名解析 直接在本设备上根据预设的域名/IP对应表进行域名解析
动态域名解析 从网络上的DNS服务器动态获取域名对应的地址

###### 6.2.1 静态域名解析

**应用场景**

 在设备上预设置域名和IP的对应表

 设备上的一些应用（比如Ping，Telnet等）进行域名操作时，直接在设备上就能解析到预设的IP，无需连到网络上的服
务器。

**功能部属**

 在设备上预设置域名和IP的对应关系

###### 6.2.2 动态域名解析

**应用场景**


配置指南 DNS

 “DNS Server”部署在网络上，对外提供域名服务

 “host.com”部署在网络上，使用域名(host.com)对外提供服务

 “Device-A"设备指定“DNS Server”作为DNS服务器，从“DNS Server”上获取到“host.com"的地址

图 6 - 1 动态域名解析配置组网图

**功能部属**

 将 DNS Server部署为"Device-A"的DNS服务器

#### 6.3 功能详解

**基本概念**

######  DNS

DNS由解析器和域名服务器组成。域名服务器是指保存有网络中所有主机的域名和IP地址的对应关系，并提供将域名和IP互
转的服务器。DNS的TCP和UDP端口号都是 53 ，通常使用UDP。

**功能特性**

功能特性 作用
域名解析 根据域名从域名服务器或本地数据库获取对应的IP地址

###### 6.3.1 域名解析

**工作原理**

######  静态域名解析


配置指南 DNS

静态域名解析，就是用户在设备上预先设置好域名和IP的对应关系，当用户使用某些应用(比如Ping、Telnet等等)进行域名操
作时，系统从本设备上解析出域名对应的IP，而不需要到网络上的DNS服务器获取域名对应的IP。

######  动态域名解析

动态域名解析，就是当用户使用某些应用进行域名操作时，系统DNS解析器查询外部的DNS服务器，获取到域名对应的IP。

动态域名解析过程：

19. 用户应用(Ping、Telnet等)向系统DNS解析器请求域名对应的IP
20. 系统DNS解析器先查找动态缓存，如果动态缓存的域名未过期则返回给应用程序
21. 如果不存在未过期的域名，DNS解析器向外部的DNS服务器发起域名转IP的请求
22. DNS解析器接收到DNS服务器的应答，缓存并转发给应用程序

**相关配置**

######  开启域名解析功能

 缺省情况下，设备是开启域名解析功能。

 通过ip domain-lookup命令开启域名解析功能。

######  配置静态域名对应的 IP

 缺省情况下，没有域名/IP的静态配置。

 通过ip host命令指定域名对应的IPv4地址

 通过ipv6 host命令配置域名对应的IPv6地址

######  配置域名服务器

 缺省情况下，未配置域名服务器。

 通过ip name-server命令配置域名服务器。

#### 6.4 配置详解

配置项 配置建议 & 相关命令

配置静态域名解析

### 可选配置^

```
ip domain-lookup 开启域名解析功能
ip host 配置域名对应的IPv4地址
ipv6 host 配置域名对应的IPv6地址
```

配置动态域名解析

### 可选配置^

```
ip domain-lookup 开启域名解析功能
```

ip name-server (^) 配置域名服务器


配置指南 DNS

###### 6.4.1 配置静态域名解析

**配置效果**

系统解析器从设备本地解析域名对应的IP。

**配置方法**

######  开启域名解析功能

 缺省已开启域名解析功能

 如果关闭该功能，静态域名解析不生效。

######  配置静态域名对应的 IP 地址

 必须配置，用户使用到的域名必须配置对应的IP。

**检验方法**

 通过show run查看配置信息。

 通过show hosts当前的域名和IP对应关系

**相关命令**

######  配置域名对应的 IPv4 地址

```
【命令格式】 ip host host-name ip-address
【参数说明】 host-name：域名
ip-address：对应的IPv4地址
【命令模式】 全局模式
【使用指导】 -^
```

######  配置域名对应的 IPv6 地址

```
【命令格式】 ipv6 host host-name ipv6-address^
【参数说明】 host-name：域名
ipv6-address：对应的IPv6地址
【命令模式】 全局模式
【使用指导】 -
```

**配置举例**


配置指南 DNS

######  配置静态域名解析

```
【配置方法】  在设备上静态配置域名www.test.com的IP地址为192.168.1.1
 在设备上静态配置域名www.testv6.com的IP地址为2001::1
Ruijie#configure terminal
Ruijie(config)# ip host http://www.test.com 192.168.1.1
Ruijie(config)# ipv6 host http://www.testv6.com 2001::1
Ruijie(config)# exit
【检验方法】 通过show hosts查看是否有所配置的静态域名表项
Ruijie#show hosts
Name servers are:
```

```
Host type Address TTL(sec)
http://www.test.com static 192.168.1.1 ---
http://www.testv6.com static 2001::1 ---
```

###### 6.4.2 配置动态域名解析

**配置效果**

系统解析器从DNS服务器解析域名对应的IP

**配置方法**

######  开启域名解析功能

 缺省已开启域名解析功能

 如果关闭该功能，动态域名解析不生效。

######  配置 DNS 服务器

 必须配置，使用动态域名解析必须配置外部的DNS服务器。

**检验方法**

 通过show run查看配置信息

**相关命令**

######  配置域名服务器

```
【命令格式】 ip name-server [ oob ] { ip-address | ipv6-address }
【参数说明】 ip-address：DNS服务器的IPv4地址
```

配置指南 DNS

```
ipv6-address：DNS服务器的IPv6地址
oob：DNS服务器支持带外管理接口（interface of mgmt）
【命令模式】 全局模式
【使用指导】 -
```

**配置举例**

######  配置动态域名解析

```
【网络环境】
图 6 - 2
```

```
DEVICE：从网络上的DNS服务器(192.168.10.1)解析域名
【配置方法】 在设备上配置DNS服务器地址为192.168.10.1
DEVICE#configure terminal
DEVICE(config)# ip name-server 192.168.10.1
DEVICE(config)# exit
【检验方法】 通过show hosts查看是否配置指定DNS服务器
Ruijie(config)#show hosts
Name servers are:
192.168.10.1 static
```

```
Host type Address TTL(sec)
```

#### 6.5 监视与维护

**清除各类信息**

### 在设备运行过程中执行clear命令，可能因为重要信息丢失而导致业务中断。^

作用 命令
清除动态主机名缓存表。 clear host [ host-name ]

**查看运行情况**

作用 命令
查看DNS的相关参数 show hosts [ host-name ]

**查看调试信息**


配置指南 DNS

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。^

作用 命令
打开调试功能 debug ip dns


配置指南 FTP-Server

### 7 FTP-Server

#### 7.1 概述

FTP Server功能可以将一台设备配置为FTP服务器。这样可以通过FTP客户端与之连接，通过FTP协议往设备上传或下载
文件。

用户可以利用FTP Server功能方便地获取设备中的文件，如syslog日志文件等；也可以通过FTP直接往设备的文件系统拷贝
文件。

### 下文仅介绍FTP的相关内容。^

**协议规范**

 RFC 959 ：FILE TRANSFER PROTOCOL (FTP)

 RFC 3659 ：Extensions to FTP

 RFC2228: FTP Security Extensions

 RFC2428: FTP Extensions for IPv6 and NATs

 RFC1635: How to Use Anonymous FTP

#### 7.2 典型应用

典型应用 场景描述
局域网内提供FTP服务 在一个局域网内为同一个用户提供上传与下载服务

###### 7.2.1 局域网内提供 FTP 服务

**应用场景**

在一个局域网内为同一个用户提供上传与下载服务

以下图为例，仅在局域网内开启FTP-Server服务

 G开启FTP Server服务，S二层透传功能

 User发起FTP上传与下载请求

图 7 - 1


配置指南 FTP-Server

【注释】 G为出口网关设备。
S为接入设备

**功能部属**

 G启动FTP Server

 S当作二层交换机，起到二层透传的作用

#### 7.3 功能详解

**基本概念**

######  FTP 协议

FTP（File Transfer Protocol）是IETF Network Working Group所制定的一套标准协议，属于网络协议组的应用层，FTP基于
TCP传输控制协议(Transmission Control Protocol)实现文件传输。FTP使用户能在两个联网的计算机之间传输文件，它是
Internet传递文件最主要的方法。使用匿名FTP，用户可以免费获取Internet丰富的资源。除此之外，FTP还提供登录、目录
查询、文件操作及其它会话控制等功能。FTP协议在TCP/IP 协议族中属于应用层协议，使用TCP端口 20 和 21 进行传输。
端口 20 用于传输数据，端口 21 用于传输控制消息。FTP 协议基本操作在RFC959 中进行了描述。

######  用户授权

FTP Client要连上 FTP Server，必须要有该 FTP服务器授权的帐号，只有拥有一个用户标识和一个口令后才能登陆FTP服
务器，享受FTP服务器提供的服务。设计考虑最大支持设定用户个数为 10 个，每个用户最大连接数为 2 个，服务器最大连接
数为 10 个。

######  FTP 文件传输模式

FTP 有两种文件传输模式：

 文本传输方式：也称为ASCII模式，用于传输文本格式的文件（比如后缀名为.txt、.bat 和.cfg的文件），与Binary模式
的区别是回车换行的处理，ASCII模式将回车换行转换为本机的回车字符，比如Unix下是\n，Windows下是\r\n，Mac
下是\r。假定用户正在拷贝的文件包含ASCII码文本，如果在远程机器上运行的不是UNIX，当文件传输时FTP通常会自
动地调整文件的内容以便于把文件解释成对端计算机存储文本文件的格式。

 二进制传输模式：也称为Binary模式，用于传输程序文件（比如后缀名为.app、.bin 和.btm的文件），可用来传送可执
行文件，压缩文件，和图片文件，不对数据进行任何处理，比文本模式更快，可以传输所有ASCII值，保证不出错。

######  FTP 工作方式

FTP的两种工作方式：


配置指南 FTP-Server

图 7 - 2

图 7 - 3

 PORT模式见图 7 - 2 ：FTP 客户端首先通过端口(1026)和FTP服务器的端口(21)建立连接，通过这个通道发送命令，客
户端需要接收数据的时候在这个通道上发送PORT命令。PORT命令包含了客户端数据通道端口(1027)来接收数据。在
传送数据的时候，服务器端通过自己的端口(20)连接至客户端的端口(1027)建立数据通道，实现数据收发；FTP Server
必须和客户端建立一个新的连接用来传送数据。

 PASV模式见图 7 - 3 ：在建立控制通道的时候与PORT模式类似，但建立连接后发送的不是Port命令，而是PASV命令。
FTP服务器收到PASV命令后，随机打开一个高端端口（ 2024 ）并且通知客户端在该端口上传送数据，客户端用端口（ 1027 ）
连接FTP服务器该端口，之后便可以在通道上进行数据收发，这个时候FTP Server不再需要建立一个新的和客户端之间
的连接。

######  支持的 FTP 命令

当设备收到FTP连接请求时， FTP服务器将要求客户端提供登录用户名和密码以进行身份认证。
如果客户端通过身份认证，即可执行FTP客户端命令进行操作。目前的FTP服务器并没有支持所有的FTP命令，具体支持的
FTP客户端命令如下：

```
ascii delete mdelete mput quit send
bin dir mdir nlist recv size
```

配置指南 FTP-Server

```
bye mget rename system
cd get mkdir passive type
cdup mls put rmdir user
close ls pwd
```

以上FTP客户端命令的用法请参考您所使用的FTP客户端软件的文档。另外不少FTP客户端工具（如CuteFTP、FlashFXP
等）均提供了图形化的操作界面，使用此类工具可以无需再通过FTP命令进行操作。

**功能特性**

功能特性 作用
开启FTP Server服务 为FTP-Client提供上传、下载、显示文件、创建文件、删除文件等功能

###### 7.3.1 开启 FTP Server 服务

**工作原理**

基本工作原理如上一章所述，我司设备需要配置用户名、密码、顶层目录即可为用户提供FTP服务。

**相关配置**

######  全局使能 FTP Server

缺省情况下，全局不开启FTP服务器

使用 ftp-server enable开启

必须在全局开启FTP服务器功能，否则无法使用

######  配置用户名密码及顶层目录

缺省情况下，无用户授权及顶层目录

使用ftp-server username password、ftp-server topdir来设置授权与顶层目录

以上三项必须配置无配置无法启动FTP服务器功能

#### 7.4 配置详解

配置项 配置建议&相关命令

配置FTP Server基本功能

### 必须配置，用于启动FTP服务器。^

```
ftp-server enable 启动FTP服务器功能
ftp-server login timeout 配置FTP登陆有效时长
```

配置指南 FTP-Server

```
ftp-server login times 配置FTP登陆有效次数
ftp-server topdir 配置FTP服务器顶层目录
ftp-server username password 设置用户名，密码
```

### 可选配置^

```
ftp-server timeout 配置FTP会话的空闲时限
```

###### 7.4.1 配置 FTP Server 基本功能

**配置效果**

 建立FTP Server，向FTP Client提供FTP服务

**注意事项**

 需要配置用户名、密码及顶层访问目录

 如果需要服务器在有限时间内关闭异常的会话，需要配置会话空闲时限

**配置方法**

######  启动 FTP Server 功能

 必须配置

 若无特殊要求，应在每台路由器上启动FTP Server功能

######  配置顶层目录

 必须配置

 若无特殊要求，应每台路由器上配置顶层目录为根目录

######  配置登录用户名和密码

 必须配置

 注意用户名和密码的长度有限制

######  配置会话空闲时限

 可先配置

 当FTP服务器某个用户在线时，如果该用户连接异常中断或用户非正常中断连接，FTP服务器可能无法知道用户断开而
将继续保持连接，导致与服务器的连接被长期占用使服务器无法响应其他用户的登录请求，因此可以配置该选项保证异常
发生时在一定时间段内让其它用户可连接上


配置指南 FTP-Server

**检验方法**

利用FTP客户端与服务器进行连接

 检查客户端是否能连接成功

 检查客户端相关操作是否正常

**相关命令**

######  启动 FTP Server 功能

```
【命令格式】 ftp-server enable
【参数说明】 -
【命令模式】 全局模式
【使用指导】 在正确配置服务器的顶层目录、登录用户名和密码之前客户端仍然无法访问FTP服务器，因此建议在首次启
动服务之前先参考后面的章节完成服务器顶层目录、登录用户名与密码的配置
```

######  配置会话登陆有效次数

```
【命令格式】 ftp-server login times times
```

```
【参数说明】 times：有效次数（范围： 1 - 10 ）
```

```
【命令模式】 全局模式
```

```
【使用指导】 会话的有效次数是指在一个FTP会话在登陆过程中，用户最多可以进行账号密码认证的次数。默认设置为 3
次，即在累计三次输入错误的用户名或密码时，会话被中止，从而允许其他用户上线。
```

######  配置会话登陆有效时长

```
【命令格式】 ftp-server^ login^ timeout^ timeout^
```

```
【参数说明】 timeout：登陆有效时间（单位：分钟；范围： 1 - 30 ）
【命令模式】 全局模式
```

```
【使用指导】 登陆有效时间是指用户建立链接后，每次认证用户账号和密码的最长在线时间。在该有效时间内用户若未再次
进行用户密码认证将被中止会话，从而保证其他用户能够登陆。
```

######  配置服务器顶层目录

```
【命令格式】 ftp-server topdir directory
【参数说明】 directory: 指定用户访问路径
【命令模式】 全局模式
【使用指导】 如可以指定服务器的顶层目录为“/syslog”目录，则FTP客户端登录后将仅能访问设备上“/syslog”目录下
的文件和文件夹，客户端由于顶层目录的限制将无法退到“/syslog”目录的上级目录中
```

配置指南 FTP-Server

######  配置服务器登录用户名和密码

```
【命令格式】 ftp-server username username password [type] password
【参数说明】 username：用户名
type： 0 或 7 ， 0 代表密码未加密（明文）， 7 代表密码为加密过的密文
password：密码
【命令模式】 全局模式
【使用指导】 FTP服务器不支持匿名用户，因此需要配置用户名
用户名最大长度为 64 个字符，中间不允许有空格。用户名可以由英文字母、半角数字和半角符号组成
密码必须为字母或数字，密码前后可以有空格，但将被忽略；密码中间的空格作为密码的一部分。
明文密码的最小长度为 1 个字符、最大长度为 25 个字符；密文密码的最小长度为 4 个字符、最大长度为 52
个字符。
用户名和密码必须一一配对，最多仅能配置 10 个用户。
```

######  配置会话空闲时限

```
【命令格式】 ftp-Server timeout time
【参数说明】 time：空闲时限（单位：分钟；范围： 1 - 3600 ）
【命令模式】 全局模式
【使用指导】 会话的空闲时间是指在一个FTP会话中从上次FTP操作完成后到下次FTP操作开始之间的时间。服务器在
响应完一个FTP Client命令操作后（如一个文件全部传输完毕后）重新开始计算会话空闲时间；在下一个FTP
Cient命令操作到来的时停止计算会话空闲时间。 因此会话空闲时限的配置并不会对某些耗时的文件传输操
作带来任何影响
```

######  查看服务器的状态信息

```
【命令格式】 show ftp-server
【参数说明】 -
【命令模式】 特权模式
【使用指导】 显示FTP服务器的相关状态信息
```

######  打开服务器的调试信息

```
【命令格式】 debug ftp-server pro/err
【参数说明】 -
【命令模式】 特权模式
【使用指导】 打开FTP服务器的过程/错误调试信息输出
```

**配置举例**

### 以下配置举例，仅介绍与FTP Server相关的配置。^

######  在 IPv4 网络上建立 FTP Server 服务

```
【网络环境】  能够建立从服务器传输到客户端的TCP连接。
```

配置指南 FTP-Server

```
【配置方法】  开启FTP Server服务
 配置顶层目录/syslog
 配置用户名为user、密码为password
 配置会话空闲时限为 5 分钟
Ruijie(config)#ftp-server username user
Ruijie(config)#ftp-server password password
Ruijie(config)#ftp-server timeout 5
Ruijie(config)#ftp-server topdir /
Ruijie(config)#ftp-server enable
```

```
【检验方法】 1.show ftp-server查看
```

(^) Ruijie#show ftp-server

ftp-server information
===================================

enable : Y
topdir : tmp:/
timeout: 10min
username:aaaa password:(PLAINT)bbbb connect num[2]
[0]trans-type:BINARY (ctrl)server IP:192.168.21.100[21]
client IP:192.168.21.26[3927]
[1]trans-type:ASCII (ctrl)server IP:192.168.21.100[21]
client IP:192.168.21.26[3929]
username:a1 password:(PLAINT)bbbb connect num[0]
username:a2 password:(PLAINT)bbbb connect num[0]
username:a3 password:(PLAINT)bbbb connect num[0]
username:a4 password:(PLAINT)bbbb connect num[0]
username:a5 password:(PLAINT)bbbb connect num[0]
username:a6 password:(PLAINT)bbbb connect num[0]
username:a7 password:(PLAINT)bbbb connect num[0]
username:a8 password:(PLAINT)bbbb connect num[0]
username:a9 password:(PLAINT)bbbb connect num[0]
**常见错误**
 未配置用户名


配置指南 FTP-Server

 未配置密码

 未配置顶层目录

#### 7.5 监视与维护

**清除各类信息**

-

**查看运行情况**

作用 命令
查看FTP Server配置 show ftp-server

**查看调试信息**

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。

作用 命令
打开FTP Server错误事件的调试开关。 debug ftp-server err^
打开FTP Server消息事件的调试开关。 debug ftp-server pro


配置指南 FTP Client

### 8 FTP Client

#### 8.1 概述

FTP（File Transfer Protocol，文件传输协议），是TCP/IP的一种具体应用，通过在FTP客户端和服务器之间建立面向连接的，
可靠的TCP连接，用户可以访问一个运行有FTP服务器程序的远程计算机。

FTP Client为用户提供在设备上通过FTP协议与远程FTP服务器进行文件传输的功能。用户通过客户端向服务器发出命令，
服务器响应命令并把执行结果返回客户端，通过这种命令交互，用户可以察看服务器目录下的文件，并把文件从远程计算机上
拷到本地，或把本地的文件传送到远程计算机去。

FTP 主要是作用是：促进程序/数据文件的共享；鼓励（通过程序）使用远程计算机；使用户不必面对不同主机上不同文件系
统的差异；对数据进行高效可靠的传输。适用于远程安全的文件传输。

锐捷FTP Client并不像标准FTP客户端一样实现交互式命令，其控制连接相关的open、user、pass指令由CLI输入copy命
令自动完成，在控制连接建立完成后，则进入文件传输过程，建立数据连接，实现文件的上传或下载。

### 用于原来的设备支持TFTP，但是TFTP是用于小文件传输，FTP协议支持大文件传输，在设备上实现文件传输协议FTP，

```
使设备可以同其它客户机或服务器进行文件传输。
```

**协议规范**

 RFC 959 ：FILE TRANSFER PROTOCOL (FTP)

#### 8.2 典型应用

典型应用 场景描述
从本地上传一个文件到远程服务上 本地与远程的的文件需要共享，如需要从本地上传一个文件到远程服务上
从远程服务器中下载一个文件到本地
设备

```
本地与远程的的文件需要共享，如需要从远程服务器中下载一个文件到本地设备。
```

###### 8.2.1 从本地上传一个文件到远程服务上

**应用场景**

本地与远程的文件需要共享，如需要从本地上传一个文件到远程服务上。

以下图为例，仅在Intranet提供共享资源作用。

图 8 - 1


配置指南 FTP Client

**功能部属**

 在Intranet中只实现通信。

 FTP Client打开 FTP Client文件上传功能。

 FTP Server打开FTP Server文件上传功能。

###### 8.2.2 从远程服务器中下载一个文件到本地设备

**应用场景**

本地与远程的的文件需要共享，如需要从远程服务器中下载一个文件到本地设备。

以下图为例，仅在Intranet提供共享资源作用。

图 8 - 2

**功能部属**

 在Intranet中只实现通信。

 FTP Client打开 FTP Client文件下载功能。

 FTP Server打开FTP Server文件下载功能。

#### 8.3 功能详解

**基本概念**

######  FTP 文件上传

从FTP Client上把文件上传到FTP Server上。

######  FTP 文件下载


配置指南 FTP Client

把FTP Server上的文件下载到FTP Client上。

######  FTP 连接模式

FTP Client与FTP Server的连接方式，有主动连接和被动连接之分。

######  FTP 传输模式

FTP Client与FTP Server的之间的传输数据的方式，FTP的传输有两种方式：文本（ASCII）传输模式和二进制（BINARY）
数据传输模式。

######  FTP 传输指定源接口 IP

FTP Client可以对与服务端进行通信的客户端源IP地址进行绑定。

**功能特性**

功能特性 作用
FTP文件上传 从FTP Client上把文件上传到FTP Server上
FTP文件下载 将FTP Server上的文件下载到FTP Client上
FTP连接模式 FTP Client与FTP Server的连接方式
FTP传输模式 FTP Client与FTP Server的之间的传输数据的方式
FTP传输指定源接口IP FTP Client可以对与服务端进行通信的客户端源IP地址进行绑定
FTP校验文件大小 FTP Client 下载文件时，可指定不进行文件大小校验

###### 8.3.1 FTP 文件上传

FTP具有文件上传的功能。进行FTP文件上传文件需要FTP Client与FTP Server两个设备同时打开，从FTP Client上把文
件上传到FTP Server上。

###### 8.3.2 FTP 文件下载

FTP具有文件下载的功能。进行FTP文件下载文件需要FTP Client与FTP Server两个设备同时打开，把FTP Server上的文
件下载到FTP Client上。

###### 8.3.3 FTP 连接模式

FTP协议要用到两个TCP连接，一个是控制链路（也称命令链路），用来在FTP客户端与服务器之间传递命令；另一个是数
据链路，用来上传或下载数据。

1. 控制连接：对于一些比较简单的连接只需要建立控制连接，客户端向服务器发送命令，服务器接收到命令则进行命令响应，
   其过程如下：

图 8 - 3 控制连接


配置指南 FTP Client

2. 控制连接与数据连接：当客户端发出的命令需要上传或下载数据时，这时不仅要建立控制连接还需要建立数据连接。

FTP协议有两种数据连接方式：主动（PORT）方式和被动（PASV）方式。这两种工作模式主要区别在于数据连接建立方式
不同，控制连接基本是一样的。

 主动方式

该模式下FTP server在数据连接时是主动去连接FTP client，所以被称为主动连接，其主要执行如下四个步骤：

1. 客户端使用图例中的源端口 5150 与server端的 21 端口通信，请求建立连接，告诉服务器将用的端口是 5151 。
2. server收到后，发送应答信息，OK(ACK)，client and server通过控制端口交换控制信令。
3. 服务器打开 20 端口作为数据发送的源端口，向客户端的 5151 端口发送。
4. 客户端应答，传输过程结束。

图 8 - 4 PORT（主动）模式

 被动方式

图 8 - 5 PASV（被动）模式


配置指南 FTP Client

该模式一般通过passive命令进行设置，由于FTP server在数据连接时是被动连接FTP Client，所以称为被动连接，其主要执
行如下四个步骤：

1. 被动模式下，客户端初始化控制信令连接，使用图例中 5150 源端口与服务器的 21 端口建立连接，并使用passive命令请
   求进入被动模式。
2. 服务器同意进入PASV模式，并随机选择一个大于 1024 的端口号，告知客户端。
3. 客户端接收到此信息后，使用图例中的 5151 端口与刚才服务器提供的 3268 端口进行数据通信，这里 5151 是源端口， 3268
   是目的端口。
4. 服务器收到信息，回传数据并发送应答ACK（OK）。

当客户端和服务器建立数据连接后，就可以进行FTP最基本的上传和下载功能，并且在客户端可以对服务器进行一些相关文
件操作。

### 用于传输命令和反馈信息的传输的控制连接始终存在，而数据连接只在需要的时候建立；PASV和PORT模式的设置选

```
择权仅在FTP Client，由FTP Client发出命令建立不同的数据连接模式，我司FTP Client默认方式为被动模式
```

###### 8.3.4 FTP 传输模式

FTP的传输有两种方式：文本（ASCII）传输模式和二进制（BINARY）数据传输模式。我司产品FTP Client目前支持ASCII
和BINARY两种传输模式，默认情况下为BINARY传输模式。

 文本模式

ASCII 模式和BINARY模式的区别是回车换行的处理，ASCII模式将回车换行转换为本机的回车字符，比如Unix下是\n，
Windows下是\r\n，Mac下是\r。

 二进制模式

BINARY模式可用来传送可执行文件，压缩文件和图片文件，不对数据进行任何处理。以Unix传送文本文件到Windows为例，
使用BINARY模式时，不会对Unix下的换行符进行从\r到\r\n的转换，因此在windows上看这个文件是没有换行的，里面是
一个个的黑方块。由于不进行回车换行的处理，因此BINARY模式比文本模式更快，可以传输所有ASCII值，保证不出错。


配置指南 FTP Client

###### 8.3.5 FTP 传输指定源接口 IP

FTP Client可以对与服务端进行通信的客户端源IP地址进行绑定，这样可以用指定的源IP与FTP Server进行连接和传输文
件。

###### 8.3.6 FTP 传输不校验文件大小

FTP Client 可以配置为下载文件时，不校验文件大小。通过不对文件大小校验，可以从不支持应答文件大小的ftp 服务器下载
文件。

#### 8.4 配置详解

配置项 配置建议 & 相关命令

配置FTP Client基本功能

### 必须配置。配置FTP CLEINT功能^

```
copy flash 文件上传
copy ftp 文件下载
```

配置FTP Client可选功能

### 可选配置。配置FTP CLEINT功能的工作模式^

```
ftp-client port 设置FTP为主动连接模式
```

ftp-client ascii (^) 设置FTP为文本传输模式
ftp-client source 配置进行FTP连接的客户端源IP地址
default ftp-client
恢复FTP Client为缺省配置，数据连接为被
动方式，文件传输为二进制模式，清除源IP
绑定
ftp-client disable-size-check 配置下载文件时，不校验文件大小

###### 8.4.1 配置 FTP Client 基本功能

**配置效果**

 实现文件上传与下载。

**注意事项**

 文件上传与下载的格式。

**配置方法**


配置指南 FTP Client

######  文件上传

 需要实现文件上传时，为必选配置。

 在特权模式下的copy下的目的地址上配置ftp相关的url。

######  文件下载。

 需要实现文件下载时，为必选配置。

 在特权模式下的copy下的源地址上配置ftp相关的url。

**检验方法**

 在FTP Server的目录中看所上传的文件是否存在。

 在目的地址上查看下载的文件是否存在。

**相关命令**

######  文件上传

【命令格式】 (^) copy flash:[ local-directory/ ]local-file ftp:
//username:password@dest-address[ /remote-directory ]/remote-file
【参数说明】 local-directory：指定设备目录，如果未指定，则表示当前工作目录。
local-file：表示要操作的本地文件名
username：指定访问FTP Server的用户名，最长不超过三十二个字节，不可包含“:”、“/”和空格等字符，
不可省略。
Password：指定访问FTP Server的密码，最长不超过三十二个字节，不可包含“:”、“/”和空格等字符，不
可省略。
dest-address：指定FTP Server的IP地址
remote-directory：指定Server端的目录路径
remote-file：指定要操作的Server端文件名

### 如果包含local-directory字段，则必须保证设备中已创建了该目录，此下载命令不支持目录的自动创建。^

```
【命令模式】 全局模式
【使用指导】 使用该命令从本地设备的flash上上传一个文件到FTP SERVER上去。
```

######  文件下载

【命令格式】 (^) copy ftp://username:password@dest-address[ /remote-directory ]/remote-file
flash:[ local-directory/ ]local-file
【参数说明】 username：指定访问FTP Server的用户名，最长不超过三十二个字节，不可包含“:”、“/”和空格等字符，
不可省略。
password：指定访问FTP Server的密码，最长不超过三十二个字节，不可包含“:”、“/”和空格等字符，不
可省略。


配置指南 FTP Client

```
dest-address：指定FTP Server的IP地址。
remote-directory：指定Server端的目录路径。
remote-file：指定要操作的Server端文件名。
local-directory：指定设备目录，如果未指定，则表示当前工作目录。
local-file：表示要操作的本地文件名。
```

### 如果包含local-directory字段，则必须保证设备中已创建了该目录，此下载命令不支持目录的自动创建。^

```
【命令模式】 全局模式
【使用指导】 使用该命令从FTP SERVER下载一个文件到本地设备的flash上去。
```

**配置举例**

### 以下配置举例，仅介绍与FTP Client上传下载相关的配置。^

######  上传文件示例

【配置方法】 将设备home目录中的local-file文件上传到用户名为user，密码为pass，IP地址为192.168.23.69的FTP
Server的root目录下，文件命名为remote-file。
Ruijie# copy flash: home/local-file ftp://user:pass@192.168.23.69/root/remote-file

```
【检验方法】 在FTP SERVER上查看remote-file是否存在。
```

######  下载文件示例

```
【配置方法】 从用户名为user，密码为pass，IP地址为192.168.23.69的FTP Server的root目录下载文件名为remote-file
的文件到设备上的home目录中，存储的文件名为local-file
Ruijie# copy ftp://user:pass@192.168.23.69/root/remote-file flash: home/local-file
```

```
【检验方法】 在flash的home目录下查看remote-file是否存在。
```

**常见配置错误**

 上传下载输入的格式错误。

 用户名或密码错误。

###### 8.4.2 配置 FTP Client 可选功能

**配置效果**

 根据配置能让FTP工作在指定连接、传输模式及指定的IP地址下进行文件上传与下载。


配置指南 FTP Client

**注意事项**

 FTP Client在配置时如果需要指定的vrf-name进行配置时，首先必须先进行vrf-name的相关配置。

**配置方法**

######  设置 FTP 为主动连接方式。

 可选配置。

 配置FTP的连接模式。

######  设置 FTP 为文本传输模式。

 可选配置。

 配置FTP的传输模式。

######  设置进行 FTP 连接的客户端源 IP 地址。

 可选配置。

 配置进行FTP连接的客户端源IP地址。

######  恢复 FTP Client 为缺省配置。

 可选配置。

 恢复FTP Client为缺省配置。

**检验方法**

通过show run查看

**相关命令**

**配置** FTP **为主动连接模式**

```
【命令格式】 ftp-client^ [^ vrf vrf-name ]^ port^
【参数说明】 vrf vrf-name：指定VRF。
【命令模式】 全局配置模式
【使用指导】 使用该命令可以将连接模式设置为主动方式，主动方式下，服务器主动去连接客户端。默认情况下FTP连接
为被动（PASV）方式。
```

**配置进行** FTP **连接的客户端源** IP **地址**

```
【命令格式】 ftp-client [ vrf vrfname ] source {ip-address | ipv6-address | interface}
【参数说明】 vrf vrf-name：指定VRF。
```

配置指南 FTP Client

```
ip-address：本地接口的ipv4地址。
ipv6-address：本地接口的ipv6地址。
【命令模式】 全局配置模式
【使用指导】 使用该命令可以绑定客户端不同的接口IP地址，使客户端使用此IP地址连接服务器。默认情况下客户端不进
行本地IP绑定，由路由进行选择。
```

######  设置 FTP 为文本传输模式

```
【命令格式】 ftp-client [ vrf vrf-name ] ascii
【参数说明】 vrf vrf-name：指定VRF。
【命令模式】 全局配置模式
【使用指导】 使用该命令可以将文件传输方式设置为文本（ASCII）方式。默认情况下FTP传输模式为二进制（BINARY）
方式。
```

######  恢复 FTP Client 为缺省配置

```
【命令格式】 default ftp-client^ [^ vrf vrf-name ]^
【参数说明】 vrf vrf-name：指定VRF。
【命令模式】 全局配置模式
【使用指导】 恢复FTP Client为缺省配置，数据连接为被动方式，文件传输为二进制模式，清除源IP绑定。
```

######  设置 FTP 不校验文件大小

```
【命令格式】 ftp-client disable-size-check
【参数说明】 -^
【命令模式】 全局配置模式
【使用指导】 配置下载文件时，不校验文件大小。默认校验文件大小。
```

**配置举例**

### 以下配置举例，仅介绍与FTP Client可选择项相关的配置。^

######  可选项配置

```
【配置方法】  配置FTP连接模式为：port
 配置传输模式为：ASCI
 配置源IP为192.168.23.167
 配置vrf 123的连接模式为：port
 配置vrf 123的传输模式为：ASCII
Ruijie# configure terminal
Ruijie(config)# ftp-client ascii
Ruijie(config)# ftp-client port
Ruijie(config)# ftp-client source 192.168.23.167
Ruijie(config)# ftp-client vrf 123 port
Ruijie(config)# ftp-client vrf 123 ascii
```

配置指南 FTP Client

```
Ruijie(config)# end
```

```
【检验方法】 在设备上进行show run，能看到以下信息
Ruijie# show run
```

```
!
ftp-client ascii
ftp-client port
ftp-client source 192.168.23.167
!
```

**常见配置错误**

 源IP不是本地IP。

 配置ftp-client vrf之前，先要配置好vrf。

#### 8.5 监视与维护

**清除各类信息**

无

**查看配置情况**

作用 命令
查看FTP Client的配置 show run

**查看调试信息**

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。^

作用 命令
打开FTP Client调试开关。 debug ftp-client


配置指南 TFTP-Server

### 9 TFTP-Server

#### 9.1 概述

TFTP Server功能可以将一台设备配置为TFTP服务器。这样可以通过TFTP客户端与之连接，通过TFTP协议往设备上传或
下载文件。

用户可以利用TFTP Server功能方便地获取设备中的文件，如升级包文件等；也可以通过TFTP Server直接往设备的文件系
统拷贝文件。

### 下文仅介绍TFTP Server的相关内容。^

**协议规范**

 RFC1350: The TFTP Protocol (revision 2)

 RFC2347: TFTP Option Extension

 RFC2348: TFTP Blocksize Option

 RFC2349: TFTP Timeout Interval and Transfer Size Options

#### 9.2 典型应用

典型应用 场景描述
局域网内提供TFTP Server服务 在一个局域网内为用户提供上传与下载服务

###### 9.2.1 局域网内提供 TFTP Server 服务

**应用场景**

在一个局域网内为用户提供上传与下载服务

以下图为例

 G开启TFTP-server服务

 User发起TFTP上传与下载请求

图 9 - 1


配置指南 TFTP-Server

【注释】 G为运行TFTP SERVER的网络设备。

**功能部属**

 G设备启动TFTP Server

 User通过TFTP Client上传或下载文件

#### 9.3 功能详解

**基本概念**

######  TFTP 协议

TFTP（Trivial File Transfer Protocol，简单文件传输协议）是IETF Network Working Group所制定的一套标准协议，属于网
络协议族的应用层，TFTP基于UDP（User Datagram Protocol）传输控制协议，提供不复杂、开销不大的文件传输服务。TFTP
不具备许多通常的FTP功能，只能上传或下载文件，不能列出目录，不能认证，没有安全机制。TFTP使用超时重传确认的方
式确保数据的传输，具有三种传输模式： 8 位ASCII码形式的netascii， 8 位源数据类型的octet和mail模式（已不再支持）。
TFTP使用的UDP端口号为 69 。在RFC1350中对TFTP协议进行了描述。

######  TFTP 报文

在TFTP客户端发起读取或者写入文件请求，TFTP服务端批准请求后，TFTP就以固定大小（ 512 字节）的数据报文来传输
数据。如果数据报文小于 512 字节，则表明传输结束。

每个数据报文包含一块数据，并且必须在收到对端的确认报文后才可以继续发送下一个数据报文。如果在规定时间内没有收到
确认报文，需要重传最后发送的一个数据报文。

TFTP报文头部包含一个操作码（opcode）字段，表明报文类型，共有五类报文：

 读请求报文（Read Request，RRQ）

 写请求报文（Write Request，WRQ）

 数据报文（Data，DATA）

 确认报文（Acknowledgment，ACK）

 错误报文（Error，ERROR）

图 9 - 2


配置指南 TFTP-Server

######  TFTP 工作方式

图 9 - 3


配置指南 TFTP-Server

 TFTP客户端向TFTP服务端发起读请求（RRQ）或者写请求（WRQ）。

 TFTP服务端收到读请求时，先判断读取条件是否满足（文件是否存在，是否有访问权限等），如果满足则发送数据报文
（DATA）给TFTP客户端；TFTP服务端收到写请求时，先判断写入条件是否满足（是否足够空间，是否有写入权限等），
如果满足，则发送ACK报文给TFTP客户端。

 TFTP客户端在准备下载文件时，收到DATA报文，则回复ACK报文；在准备上传文件时，收到ACK报文，则继续发送
DATA报文。

 重复发送确认的流程，直到最后一个长度小于 512 的DATA报文，表明传输的结束。

 在传输过程中，如果遇到错误，则发送错误（ERROR）报文给对端。

**功能特性**

功能特性 作用
开启TFTP-Server服务 为TFTP-Client提供上传、下载文件功能

###### 9.3.1 开启TFTP-Server服务

**工作原理**


配置指南 TFTP-Server

基本工作原理如上一章所述，设备开启TFTP server服务后，配置顶层目录即可为用户提供FTP服务。

**相关配置**

######  使能 TFTP-Server

 缺省情况下，不开启TFTP Server

 使用 tftp-server enable开启

 必须开启TFTP服务器功能，否则无法使用

######  配置顶层目录

 缺省情况下，无配置顶层目录

 使用tftp-server topdir来设置顶层目录

 必须配置顶层目录，否则无法提供上传和下载

#### 9.4 配置详解

配置项 配置建议&相关命令

配置TFTP-SERVER基本功能

### 必须配置，用于启动TFTP服务器。^

tftp-server enable (^) 启动TFTP服务器功能
tftp-server topdir 配置TFTP服务器顶层目录

###### 9.4.1 配置 TFTP-Server 基本功能

**配置效果**

 建立TFTP-Server，向TFTP-Client提供上传和下载服务

**注意事项**

 需要配置顶层访问目录

**配置方法**

######  启动 TFTP-SERVER 功能

 必须配置

 若无特殊要求，应在每台设备上启动TFTP-Server功能


配置指南 TFTP-Server

######  配置顶层目录

 必须配置

 若无特殊要求，应在每台设备上配置顶层目录为根目录

**检验方法**

利用TFTP客户端与服务器进行连接

 检查客户端是否能连接成功

 检查客户端下载和上传是否正常

**相关命令**

######  启动 TFTP-SERVER 功能

```
【命令格式】 tftp-server enable
【参数说明】 -
【命令模式】 全局模式
【使用指导】 在正确配置服务器的顶层目录之前客户端仍然无法访问TFTP服务器，因此建议在首次启动服务之前先参考后
面的章节完成服务器顶层目录的配置
```

######  配置服务器顶层目录

```
【命令格式】 tftp-servertopdirdirectory^
【参数说明】 directory：指定用户访问路径
【命令模式】 全局模式
【使用指导】 如可以指定服务器的顶层目录为“/dir”目录，则TFTP客户端登录后将仅能访问设备上“/dir”目录下的文件
和文件夹，客户端由于顶层目录的限制将无法退到“/dir”目录的上级目录中
```

######  打开服务器的调试信息

```
【命令格式】 debug tftp-server
【参数说明】 -
【命令模式】 特权模式
【使用指导】 打开TFTP服务器的过程/错误调试信息输出
```

**配置举例**

######  在 IPv4 网络上建立 TFTP-SERVER 服务

```
【配置方法】  开启TFTP-SERVER服务
 配置顶层目录/dir
Ruijie(config)#tftp-server topdir /dir
```

配置指南 TFTP-Server

```
Ruijie(config)#tftp-server enable
```

```
【检验方法】  通过show run 查看配置结果
Ruijie#show run
...
tftp-server enable
tftp-server topdir /dir
...
```

**常见错误**

 未配置顶层目录

#### 9.5 监视与维护

**清除各类信息**

-

**查看运行情况**

-

**查看调试信息**

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。

作用 命令
打开TFTP服务器的调试开关。 debug tftp-server^


配置指南 TUNNEL

### 10 TUNNEL

#### 10.1 概述

Tunnel接口用于实现隧道功能，是系统虚拟的接口。Tunnel接口并不特别指定传输协议或者负载协议，它提供的是一个用来
实现标准的传输链路。每一个Tunnel接口代表一个传输链路。

Tunnel功能实现包括下面三个主要组成部分：

 负载协议：通过Tunnel传输的负载(网络数据)的封装协议。如IPv4和IPv6协议作为负载协议，对于GRE隧道，可以是
不是IPv4或者IPv6协议；

 载体协议：用来二次封装并辨识待传输负载的协议。在本文描述的TUNNEL中，只有GRE隧道有载体协议，即GRE协
议（也即封装协议）。其他类型的隧道都是IPv4/IPv6 外面直接封装IPv4/IPv6；

 传输协议：实际传输经过载体协议二次封装后的负载的网络协议。锐捷产品使用最广泛应用的IPv4和IPv6协议作为传输
协议。

实际上，如果两个私有同种协议网络需要通过异种公有网络实现互通讯，就可以采用Tunnel模式实现。

Tunnel传输适用于以下情况：

 允许运行非IP协议的本地网络之间通过一个单一网络（IP网络）通讯，因为Tunnel支持多种不同的负载协议；允许那
些对路由跳数有限制的协议可以在更广泛的范围内工作，因为Tunnel使用的是传输协议 (IP) 的路由工作；

 允许通过单一的网络 (IP网络) 连接间断子网；

 允许在广域网上提供VPN （Virtual Private Network，虚拟专用网络）功能。

由于Tunnel将负载封装后传输，这会带来处理上的复杂性，在某些情况下需要注意以下的变化。

 由于Tunnel是逻辑链路，在路由的时候看起来只有一跳（hop），可实际上可能其路由花费不止一跳。在使用Tunnel的
时候必须注意到Tunnel链路的路由与实际路由并不一致。

 由于Tunnel传输将负载封装在传输协议中，在设置防火墙特别是访问控制链表(ACL)的时候，这一点需要考虑；同时必
须注意到此时负载协议的传输带宽等(如MTU)也比理论值更小。

### 下文仅介绍Tunnel的相关内容。^

**协议规范**

 RFC2784：Generic Routing Encapsulation (GRE)

 RFC2890：Key and Sequence Number Extensions to GRE

 RFC3056：Connection of IPv6 Domains via IPv4 Clouds

 RFC3068：An Anycast Prefix for 6to4 Relay Routers


配置指南 TUNNEL

 RFC3964：Security Considerations for 6to4

 RFC4023：Encapsulating MPLS in IP or Generic Routing Encapsulation (GRE)

 RFC4 087 ：IP Tunnel MIB

 RFC 4213 ：Basic Transition Mechanisms for IPv6 Hosts and Routers

 RFC4797：Use of Provider Edge to Provider Edge (PE-PE) Generic Routing Encapsulation (GRE) or IP in
BGP/MPLS IP Virtual Private Networks

 RFC5158：6to4 Reverse DNS Delegation Specification

 RFC 5214 ：Intra-Site Automatic Tunnel Addressing Protocol (ISATAP)

 RFC5332：MPLS Multicast Encapsulations

 RFC 5579 ：Transmission of IPv4 Packets over Intra-Site Automatic Tunnel Addressing Protocol (ISATAP)
Interfaces

 RFC5845：Generic Routing Encapsulation (GRE) Key Option for Proxy Mobile IPv6

 RFC5969：IPv6 Rapid Deployment on IPv4 Infrastructures (6rd) -- Protocol Specification

 RFC6245：Generic Routing Encapsulation (GRE) Key Extension for Mobile IPv4

 RFC6343：Advisory Guidelines for 6to4 Deployment

 RFC6372：6to4 Provider Managed Tunnels

 RFC6654：Gateway-Initiated IPv6 Rapid Deployment on IPv4 Infrastructures (GI 6rd)

 draft-zhou-dhc-gre-option- 00 DHCPv4 and DHCPv6 options for GRE

 draft-cai-softwire-6rd-mib- 03 Definitions of Managed Objects for 6rd

 draft-howard-isp-ip6rdns- 05 Reverse DNS in IPv6 for Internet Service Providers

 draft-tsou-softwire-6rd-multicast- 02 IPv6 Multicast Using Native IPv4 Capabilities in a 6rd Deployment

 draft-templin-v6ops-isops- 18 Operational Guidance for IPv6 Deployment in IPv4 Sites using ISATAP

#### 10.2 典型应用

典型应用 场景描述
访问园区网内部的IPv6站点 访问园区网内部的IPv6站点。^
园区网接入IPv6骨干网 园区网接入IPv6骨干网。^

###### 10.2.1 访问园区网内部的 IPv6 站点

**应用场景**

一些园区网有部署IPv6服务器，PC需要能访问这些服务器。可以利用ISATAP自动隧道实现这种应用。


配置指南 TUNNEL

图 10 - 1

【注释】 ISATAP-RELAY为支持tunnel的设备，园区网用户访问IPv4的服务器时，直接通过IPv4网络访问；访问IPv6的
服务器时，需通过ISATAP隧道访问

**功能部属**

 V4/V6用户通过V4地址访问IPv4网络。

 V4/V6用户通过ISATAP隧道访问IPv6网络。

 ISATAP隧道在PC和ISATAP-RELAY路由器建建立ISATAP隧道。

###### 10.2.2 园区网接入 IPv6 骨干网

**应用场景**

将旧的园区网升级成支持IPv6，或者新建一个支持IPv6的园区网。可以使用6to4自动隧道实现。

#### 10.3 功能详解

**基本概念**

######  隧道 MTU

 隧道接口的MTU（Maximum Transmission Unit，最大传输单元）一般低于普通接口，如普通的IPv4 over IPv4的隧道，
假定在以太网上传输，那么除去 2 层IP头部，每个报文实际能传输的最大数据量是 1460 字节。所以隧道接口的MTU为
1480 字节，而不是标准以太网接口的 1500 字节。

######  隧道路径 MTU


配置指南 TUNNEL

 隧道接口实际上代表了一个虚拟的链路。以IPv4 over IPv4隧道为例。这个隧道接口的MTU实际上是隧道链路的MTU，
即隧道本端和对端之间的路径MTU。当本端和对端之间的路由路径发生变化后，则路径MTU可能发生变化，从而影响
隧道接口的MTU

######  隧道嵌套层数

 隧道可以嵌套。以IPv4 over IPv4隧道为例。可以将原始的IPv4报文再封装 2 层IPv4首部或者更多层次的IPv4首部以
后再发送出去。需要隧道嵌套的场景一般不多见，主要是为了更安全的缘故。隧道嵌套后，可以传输的数据更少了。一个
隧道接口的对端地址经过FIB选路后，如果出口是另一个隧道接口，则会发生隧道嵌套封装；如果选路后出口又是本隧
道，那么会出现无穷嵌套（锐捷产品能检测出这种情况，并给出提示）。

**功能特性**

功能特性 作用
隧道嵌套封装层数限
制

```
根据实际需要调大隧道嵌套封装层数限制（很少使用）。
```

隧道数据有效性校
验

```
对GRE隧道传输的数据增加校验和，用于检查数据传输过程中的是否发生错误。
```

#### 10.4 配置详解

配置项 配置建议 & 相关命令

配置隧道接口基本功能

### 必须配置。用于建立隧道。^

Interface tunnel (^) 新建一个隧道接口
tunnel source 设置隧道的本端地址

### 配置隧道模式

```
可选配置，用于设置隧道模式
```

tunnel mode (^) 配置隧道封装模式

### 配置隧道对端地址

```
可选配置，用于设置隧道对端地址
```

tunnel destination (^) 配置隧道对端地址

### 配置隧道传输网络TOS

```
可选配置，用于设置传输网络的TOS
tunnel tos 配置隧道传输网络TOS
```

### 配置隧道传输网络TTL

```
可选配置，用于设置传输网络的TTL
```

tunnel ttl (^) 配置传输网络的TTL

###### 10.4.1 配置隧道接口

**配置效果**


配置指南 TUNNEL

 新建一个隧道接口。

**注意事项**

无

**配置方法**

######  新建隧道接口功能

 在全局配置模式下，使用interface tunnel number 新建隧道接口。

 只有创建了隧道接口，才能使用隧道服务。

**检验方法**

 使用show interfaces tunnel number观察是否成功配置。

**相关命令**

######  配置隧道接口

```
【命令格式】 interface tunnel number
【参数说明】 number：隧道接口编号。
【命令模式】 全局模式
【使用指导】 -^
```

######  检查隧道配置

```
【命令格式】 show interfaces tunnel number
【参数说明】 number：隧道接口编号。
【命令模式】 全局模式
【使用指导】 -
```

**配置举例**

######  新建一个隧道接口

【配置方法】 (^)  新建一个隧道接口
Ruijie# configure terminal
Ruijie(config)# interface tunnel 1
Ruijie(config-if-Tunnel 1)# end


配置指南 TUNNEL

【检验方法】 (^)  检查隧道接口的配置
Ruijie# show interfaces tunnel 1
......
Tunnel attributes:
......
Tunnel protocol/transport is gre ip
**常见错误**
 内存不足导致隧道接口创建失败。
 硬件芯片资源不足导致隧道接口创建失败。

###### 10.4.2 配置隧道封装模式

**配置效果**

 需要使用非缺省封装模式的隧道时

 在隧道接口模式下配置

**注意事项**

无

**配置方法**

######  设置隧道的封装模式

 可选配置

 交换机，无线产品的缺省封装模式是tunnel mode ipv6ip。

 路由器，网关产品缺省封装模式是tunnel mode gre ip。

 在隧道接口模式下，通过tunnel mode命令可以修改成其他模式。

**检验方法**

 使用show interfaces tunnel number观察是否成功配置。

**相关命令**


配置指南 TUNNEL

######  配置隧道封装模式

```
【命令格式】 tunnel mode { gre {ip | ipv6} | ipv6| ipip | ipv6ip [ 6to4 | isatap ] }
【参数说明】 每一种mode代表从此隧道接口发出的报文的封装格式
gre ip表示，先经过一个GRE头部封装，再经过IPv4封装，然后在新的IPv4网络发送
gre ipv6表示，先经过一个GRE头部封装，再经过IPv6封装，然后在新的IPv6网络发送
ipv6表示，从此接口发出的报文直接经过IPv6封装后，在新的IPv6网络发送
ipip表示，此接口只能承载IPv4报文，并且此报文再经过IPv4封装后，在新的IPv4网络发送
ipv6ip表示，此接口只能承载IPv6报文，并且报文经过IPv4封装后，在新的IPv4网络中发送
上述隧道都是手工隧道，而ipv6ip 6to4/isatap是自动隧道，报文封装过程中，目标IPv4地址是通过目标IPv6
地址映射而成。
【命令模式】 接口模式
【使用指导】 隧道的 2 端一般情况下需要配置相同的模式，否则不能正常工作。
```

**配置举例**

######  配置隧道的封装模式为 IPv4 over IPv4 。

【配置方法】 (^)  配置隧道接口的封装模式为IPv4 over IPv4。
Ruijie# configure terminal
Ruijie(config)# interface tunnel 1
Ruijie(config-if-Tunnel 1)# tunnel mode ipip
Ruijie(config)# end
【检验方法】 (^)  检查隧道接口的配置
Ruijie# show interfaces tunnel 1
......
Tunnel attributes:
......
Tunnel protocol/transport is ipv6ip
**常见错误**
 相同vrf已经有一个6to4或者isatap隧道，继续配置这 2 种隧道。

###### 10.4.3 配置隧道本端地址

**配置效果**

 设置隧道的本端地址。


配置指南 TUNNEL

**注意事项**

 隧道的本端地址必须同隧道的传输协议匹配。否则隧道口不会UP(被禁用)。

 当通过指定另外一个接口间接指定本端地址时，指的是IPv4主地址或者IPv6第一个全球公网地址。

**配置方法**

######  设置隧道的本端地址

 必须配置

 在隧道接口模式下使用tunnel source命令指定隧道的本端地址。

**检验方法**

 通过show interfaces tunnel number命令可以观察隧道的本端地址

**相关命令**

######  配置隧道本端地址

```
【命令格式】 tunnel source {^ ip-address^ | interface-name^ interface-number^ }^
【参数说明】 ip-address：可以是IPv4地址，也可以是IPv6地址。
Interface-name interface-number：可以是各种 3 层接口。
【命令模式】 接口模式
【使用指导】 如果直接指定IPv4或者IPv6地址，则需要设置成设备自身的地址
```

**配置举例**

######  配置隧道的本端地址。

【配置方法】 (^)  配置隧道的本端地址为1.1.1.1
Ruijie# configure terminal
Ruijie(config)# interface tunnel 1
Ruijie(config-if-Tunnel 1)# tunnel mode ipv6ip
Ruijie(config-if-Tunnel 1)# tunnel source 1.1.1.1
【检验方法】 (^)  检查隧道接口的配置。
Ruijie# show interfaces tunnel 1
......
Tunnel attributes:


配置指南 TUNNEL

【配置方法】 (^)  配置隧道的本端地址为1.1.1.1
Ruijie# configure terminal
Ruijie(config)# interface tunnel 1
Ruijie(config-if-Tunnel 1)# tunnel mode ipv6ip
Ruijie(config-if-Tunnel 1)# tunnel source 1.1.1.1
【检验方法】 (^)  检查隧道接口的配置。
Tunnel source 1.1.1.1, destination UNKNOWN, unrouteable
Tunnel TOS/Traffic Class not set, Tunnel TTL 254
Tunnel config nested limit is 0, current nested number is 0
Tunnel protocol/transport ipv6ip
Tunnel transport VPN is no set
......
**常见配置错误**
无

###### 10.4.4 配置隧道对端地址

**配置效果**

 手工隧道，必须配置对端地址后，才能使用（接口才会UP）。

**注意事项**

 自动隧道不能配置对端地址。

**配置方法**

######  配置隧道对端地址

 6to4, isatap隧道不能配置，其他隧道必须配置

 在接口模式下通过tunnel destination命令配置对端地址。

**检验方法**

 show interfaces tunnel 命令可以查看是否配置成功。


配置指南 TUNNEL

**相关命令**

######  配置对端地址

```
【命令格式】 tunnel destination { ip-address }
【参数说明】 ip-address：可以是ipv4地址，也可以是IPv6地址。
【命令模式】 接口模式
【使用指导】 手工隧道必须配置对端地址。
配置的对端地址的协议族类型必须同传输协议一致，否则隧道接口禁用（不UP）。
```

**配置举例**

######  配置隧道对端地址。

【配置方法】 (^)  配置隧道对端地址为2.2.2.2
Ruijie# configure terminal
Ruijie(config)# interface tunnel 1
Ruijie(config-if-Tunnel 1)# tunnel mode ipv6ip
Ruijie(config-if-Tunnel 1)# tunnel destination 2.2.2.2
【检验方法】 (^)  检查隧道接口的配置
Ruijie# show interfaces tunnel 1
......
Tunnel attributes:
Tunnel source: UNKNOWN, destination 2.2.2.2, unrouteable
Tunnel TOS/Traffic Class not set, Tunnel TTL 254
Tunnel config nested limit is 0, current nested number is 0
Tunnel protocol/transport ipv6ip
......
**常见错误**
 为自动隧道配置对端地址。
 和另一个隧道的对端地址相同。

###### 10.4.5 配置隧道传输网络 TOS

**配置效果**


配置指南 TUNNEL

 指定传输协议首部的tos或者traffic class字段。

**注意事项**

 如果不指定，则拷贝承载协议对应的tos和traffic class字段。

**配置方法**

######  配置传输网络 TOS

 可选配置

 如果需要修订隧道数据在网络中的优先级

 在接口模式下使用tunnel tos命令

**检验方法**

 使用show interfaces tunnel命令查看是否成功设置。

**相关命令**

######  配置传输网络 TOS

```
【命令格式】 tunnel tos number
【参数说明】 number：需要设置的tos的值。
【命令模式】 接口模式
【使用指导】 缺省情况下，如果隧道内层承载与外层封装都是IPv4协议，则缺省将内层IPv4头的tos字节拷贝到外层IPv4
头。如果隧道内层承载与外层封装都是IPv6协议，则缺省将内层IPv6头的traffic class8比特拷贝到外层IPv6
头。其他情况，外层IPv4 tos / IPv6 traffic class,为 0 。
```

**配置举例**

######  配置传输网络 TOS 。

【配置方法】 (^)  配置传输网络TOS
Ruijie# configure terminal
Ruijie(config)# interface tunnel 1
Ruijie(config-if-Tunnel 1)# tunnel mode ipv6ip
Ruijie(config-if-Tunnel 1)# tunnel tos 2
【检验方法】 (^)  检查隧道接口的配置


配置指南 TUNNEL

【配置方法】 (^)  配置传输网络TOS
Ruijie# configure terminal
Ruijie(config)# interface tunnel 1
Ruijie(config-if-Tunnel 1)# tunnel mode ipv6ip
Ruijie(config-if-Tunnel 1)# tunnel tos 2
【检验方法】 (^)  检查隧道接口的配置
Ruijie# show interfaces tunnel 1
......
Tunnel attributes:
Tunnel source 1.1.1.1, destination UNKNOWN, unrouteable
Tunnel TOS/Traffic Class 0x2, Tunnel TTL 254
Tunnel config nested limit is 0, current nested number is 0
Tunnel protocol/transport ipv6ip
Tunnel transport VPN is VPN1
......
**常见错误**
无

###### 10.4.6 配置隧道传输网络 TTL

**配置效果**

 指定隧道封装协议首部的TTL或者hoplimit的值。

**注意事项**

无

**配置方法**

######  配置传输网络 TTL

 可选配置

 缺省 254

 如果需要将隧道链路的长度修改成特定值


配置指南 TUNNEL

 使用tunnel ttl命令进行设置。

**检验方法**

 使用show interfaces tunnel命令查看是否成功设置。

**相关命令**

######  配置传输网络 TTL

```
【命令格式】 tunnel ttl hop-limit
【参数说明】 hop-limit：传输网络的跳数限制。
【命令模式】 全局模式
【使用指导】 指的是传输网络最多可以经过的路由器数目，缺省是 254 。需要修改成特定值，可以使用此命令。
```

**配置举例**

######  配置传输网络 TTL

【配置方法】 (^)  配置传输网络TTL。
Ruijie# configure terminal
Ruijie(config)# interface tunnel 1
Ruijie(config-if-Tunnel 1)# tunnel mode ipv6ip
Ruijie(config-if-Tunnel 1)# tunnel ttl 3
【检验方法】 (^)  检查隧道接口的配置
Ruijie# show interfaces tunnel 1
......
Tunnel attributes:
Tunnel source 1.1.1.1, destination UNKNOWN, unrouteable
Tunnel TOS/Traffic Class 0x2, Tunnel TTL 3
Tunnel config nested limit is 0, current nested number is 0
Tunnel protocol/transport ipv6ip
Tunnel transport VPN is VPN1
**常见错误**
无


配置指南 TUNNEL

#### 10.5 监视与维护

**清除各类信息**

###### 无

**查看运行情况**

作用 命令
查看隧道接口相关信息。 show interfaces^ tunnel number^

**查看调试信息**

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。^

作用 命令
打开隧道接口的调试开关 debug tunnel


配置指南 网络通信检测工具

### 11 网络通信检测工具

#### 11.1 概述

网络通信检测工具可以用于检查网络是否能够连通，用好网络通信监测工具可以很好地帮助我们分析判定网络故障。网络通信
检测工具包括PING（Packet Internet Groper，因特网包探索器）和Traceroute（路由侦测）。PING工具主要用于检测网络通
与不通，以及网路的时延，时延值越大，则表示网络速度越慢。Traceroute工具则可以帮助用户了解网络的物理与逻辑连接的
拓扑情况以及数据传输的效率。在网络设备上，这两个工具所对应的命令为ping和traceroute。

**协议规范**

 RFC 792 ：Internet Control Message Protocol

 RFC 4443 ：Internet Control Message Protocol (ICMPv6) for the Internet Protocol Version 6 (IPv6) Specification

#### 11.2 典型应用

典型应用 场景描述
端对端连通性检查 网络设备与目标主机都连接在IP网络上，都配置有IP地址。
主机路由检查 网络设备与目标主机都连接在IP网络上，都配置有IP地址。

###### 11.2.1 端对端连通性检查

**应用场景**

图 11 - 1 网络设备A与目标主机B都连接在IP网络上。

网络设备与目标主机都连接在IP网络上，端对端连通性检查就是判定IP报文能否在二者之间传输。目标主机可以是网络设备
本身，这种情况一般用于检查设备自身网络接口和TCP/IP协议配置的正确性。

**功能部属**

通过在网络设备上运行Ping功能。


配置指南 网络通信检测工具

###### 11.2.2 主机路由检查

**应用场景**

图 11 - 2 网络设备A与目标主机B都连接在IP网络上。

网络设备与目标主机都连接在IP网络上，主机路由检查就是判定IP报文在二者之间传输，究竟需要经过多少网关（路由器）。
目标主机通常不是网络设备本身，并且通常与网络设备不在同一个IP网段。

**功能部属**

通过在网络设备上运行Traceroute功能。

#### 11.3 功能详解

**功能特性**

功能特性 作用
Ping连通性测试 检测指定IPv4/v6地址是否可达，并输出相关信息。
Traceroute连通性测试 显示IPv4/v6数据包从源地址到目的地址所经过的网关。

###### 11.3.1 Ping 连通性测试

**工作原理**

PING工具向目标IP地址发送一个ICMP请求（ICMP Request）数据包，要求对方返回一个ICMP回声（ICMP Echo）数据
包，来确定两台网络机器是否连接相通，时延是多少。

**相关配置**

 通过ping命令进行配置


配置指南 网络通信检测工具

###### 11.3.2 Traceroute 连通性测试

**工作原理**

Traceroute工具利用ICMP及IP报文头部的TTL（Time To Live）字段。首先，网络设备的Traceroute工具送出一个TTL是
1 的ICMP Request到目的主机，当路径上的第一个路由器收到这个报文时，它将TTL减 1 。此时TTL变为 0 了，所以该路由
器会将此报文丢弃，并送回一个ICMP超时（ICMP time exceeded）消息，Traceroute工具收到这个消息后，便知道这个路由
器存在于这个路径上，接着再送出另一个TTL是 2 的报文，发现第 2 个路由器。Traceroute工具每次将送出的报文的TTL 加
1 来发现另一个路由器，这个重复的动作一直持续到某个数据报文到达目的主机。当报文到达目的主机后，该主机不会送回ICMP
time exceeded消息，而是送回ICMP Echo，Traceroute工具结束探测并显示从网络设备到目的主机的路径信息。

**相关配置**

 通过traceroute命令进行配置

#### 11.4 配置详解

配置项 配置建议 & 相关命令

### Ping连通性测试

```
可选配置，用于检测IPv4/v6地址是否可达。
ping 运行Ping功能。
```

### Traceroute连通性测试

```
可选配置，显示IPv4/v6数据包从源地址到目的地址所经过的网关。
traceroute 运行Traceroute功能。
```

###### 11.4.1 Ping 连通性测试

**配置效果**

在网络设备上采用Ping连通性测试，可以得知该网络设备和目的主机之间是否保持连通，报文是否可以在网络设备和目的主
机之间传输。

**注意事项**

执行PING操作的网络设备本身需要配置IP地址。

**配置方法**

 如果需要检测IPv4地址是否可达，可通过Ping IPv4命令。


配置指南 网络通信检测工具

 如果需要检测IPv6地址是否可达，可通过Ping IPv 6 命令。

**检验方法**

输入ping命令，即可在CLI界面显示相关信息。

**相关命令**

######  Ping IPv4

```
【命令格式】 ping [ oob | vrf vrf-name | ip ] { address ] [ length length ] [ ntimes times ] [ timeout seconds ] [ data data ]
[ source source ] [ df-bit ] [ validate ] [ detail ] [interval millisecond] }
【参数说明】 oob：设置使用带外通道。当指定MGMT口作为源接口时，必须设置该参数。
vrf-name：VRF名字。
address：指定目的IPv4地址或域名。length：指定发送数据包数据填充段的长度，范围：36~18024，默认
填充长度为 100 。
times：指定发送数据包的个数，范围：1~ 4294967295。
seconds：指定超时的时间，范围：1~10（秒）。
data：指定报文填充数据，格式为 1 - 255 长度的字符串，默认填充为abcd。
source：指定报文源IPv4地址或源接口。其中，环回接口地址（例如127.0.0.1）不允许作为源地址。
df-bit：设置IP的DF标识位，当DF位被设置为 1 时，表示不对数据包进行分段处理，默认DF位为 0 。
validate：设置是否校验响应报文。
detail：设置回显是否显示详细信息，默认只显示‘！’和‘.’。
millisecond：指定每个ping报文的间隔时间，范围：10~300000（毫秒），缺省间隔时间是 100 毫秒
【命令模式】 在普通用户模式下，只能运行基本的ping功能；在特权用户模式下，还可以运行ping的扩展功能。
在其他模式下，可以通过do命令执行ping的扩展功能，具体配置请参考do命令说明。
【使用指导】 运行ping功能，如果有应答，则显示出应答的相关信息，最后输出一个统计信息。在扩展ping中，可以指
定发送数据包的个数、长度、超时的时间等等，和基本的ping功能一样，最后也输出一个统计信息。
要使用域名功能，则要先配置域名服务器，具体配置请参考DNS配置部分。
```

######  Ping IPv 6

```
【命令格式】 ping [ vrf vrf-name | [ oob ] ipv6 ] [ address [ length length ] [ ntimes times ] [ timeout seconds ] [ data
data ] [ source source ] [ detail ] [interval millisecond] ]
【参数说明】 oob：设置使用带外通道。当指定MGMT口作为源接口时，必须设置该参数。
vrf-name：VRF名字。
address：指定目的IPv6地址或域名。
length：指定发送数据包的长度，范围：16~18024，默认填充长度为 100 。
times：指定发送数据包的个数，范围：1~ 4294967295。
seconds：指定超时的时间，范围：1~10（秒）。
data：指定报文填充数据，格式为 1 - 255 长度的字符串。
source：指定报文源IPv6地址或源接口。其中，环回接口地址（例如::1）不允许作为源地址。
```

配置指南 网络通信检测工具

```
Detail：设置回显是否显示详细信息，默认只显示‘！’和‘.’。
millisecond：指定每个ping报文的间隔时间，范围：10~300000（毫秒），缺省间隔时间是 100 毫秒
【命令模式】 在普通用户模式下，只能运行基本的ping ipv6功能；在特权用户模式下，还可以运行ping ipv6的扩展功能。
在其他模式下，可以通过do命令执行ping的扩展功能，具体配置请参考do命令说明。
【使用指导】 运行ping ipv6功能，如果有应答，则显示出应答的相关信息，最后输出一个统计信息。
在扩展ping ipv6中，可以指定发送数据包的个数、长度、超时的时间等等，和基本的ping ipv6功能一样，
最后也输出一个统计信息。
要使用域名功能，则要先配置域名服务器，具体配置请参考DNS配置部分。
```

**配置举例**

######  运行普通 Ping 功能

【配置方法】 在特权模式下输入Ping IPv4地址192.168.21.26
常规ping
Ruijie# ping 192.168.21.26
Sending 5, 100-byte ICMP Echoes to 192.168.21.26, timeout is 2 seconds:
< press Ctrl+C to break >
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/10 ms
显示detail的ping
Ruijie#ping 192.168.21.26 detail
Sending 5, 100-byte ICMP Echoes to 192.168.21.26, timeout is 2 seconds:
< press Ctrl+C to break >
Reply from 192.168.21.26: bytes=100 time=4ms TTL=64
Reply from 192.168.21.26: bytes=100 time=3ms TTL=64
Reply from 192.168.21.26: bytes=100 time=1ms TTL=64
Reply from 192.168.21.26: bytes=100 time=1ms TTL=64
Reply from 192.168.21.26: bytes=100 time=1ms TTL=64

Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/4 ms.
【检验方法】 缺省将 5 个数据段长度为100Byte的数据包发送到指定的IP地址，在指定的时间（缺省为 2 秒）内，显示相
应的探测信息，最后输出一个统计信息。

######  运行扩展 Ping 功能

【配置方法】 在特权模式下输入Ping IPv4地址192.168.21.26，并指定发送数据包的长度、个数、超时的时间等。
常规ping
Ruijie# ping 192.168.21.26 length 1 5 00 ntimes 100 data ffff source 192.168.21. 99 timeout 3
Sending 100, 1 500 - byte ICMP Echoes to 192.168.21.26, timeout is 3 seconds:
< press Ctrl+C to break >
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!


配置指南 网络通信检测工具

```
Success rate is 100 percent (100/100), round-trip min/avg/max = 2/2/ 3 ms
显示detail的ping
ping 192.168.21.26 length 1500 ntimes 20 data ffff source 192.168.21.99 timeout 3 detail
Sending 20, 1500-byte ICMP Echoes to 192.168.21.26, timeout is 3 seconds:
< press Ctrl+C to break >
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=2ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=3ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
Reply from 192.168.21.26: bytes=1500 time=1ms TTL=64
```

```
Success rate is 100 percent (20/20), round-trip min/avg/max = 1/1/3 ms.
```

【检验方法】 将 20 个长度为1500Byte的数据包发送到指定的IP地址，在指定的时间（ 3 秒）内，如果有应答，显示相应
的探测信息，最后输出一个统计信息。

######  运行普通 Ping IPv6 功能

【配置方法】 在特权模式下输入Ping IPv6地址2001:: 1
常规ping
Ruijie# ping ipv6 2001:: 1
Sending 5, 100-byte ICMP Echoes to 2001:: 1 , timeout is 2 seconds:
< press Ctrl+C to break >
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/10 ms

```
显示detail的ping
```

配置指南 网络通信检测工具

```
Ruijie#ping 2001:: 1 detail
Sending 5, 100-byte ICMP Echoes to 2001:: 1 , timeout is 2 seconds:
< press Ctrl+C to break >
Reply from 2001:: 1 : bytes=100 time=1ms
Reply from 2001:: 1 : bytes=100 time=1ms
Reply from 2001:: 1 : bytes=100 time=1ms
Reply from 2001:: 1 : bytes=100 time=1ms
Reply from 2001:: 1 : bytes=100 time=1ms
```

```
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms.
```

【检验方法】 缺省将 5 个数据段长度为100Byte的数据包发送到指定的IP地址，在指定的时间（缺省为 2 秒）内，显示相
应的探测信息，最后输出一个统计信息。

######  运行扩展 Ping IPv6 功能

【配置方法】 在特权模式下输入Ping IPv6地址 2001 :: 5 ，并指定发送数据包的长度、个数、超时的时间等。
常规ping
Ruijie# ping ipv6 2001::5 length 1 5 00 ntimes 100 data ffff source 2001::9 timeout 3
Sending 100, 1 500 - byte ICMP Echoes to 2000::1, timeout is 3 seconds:
< press Ctrl+C to break >
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!
Success rate is 100 percent (100/100), round-trip min/avg/max = 2/2/ 3 ms
显示detail的ping
Ruijie#ping 2001::5 length 1500 ntimes 10 data ffff source 2001::9 timeout 3
Sending 10, 1500-byte ICMP Echoes to 2001::5, timeout is 3 seconds:
< press Ctrl+C to break >
Reply from 2001::5: bytes=1500 time=1ms
Reply from 2001::5: bytes=1500 time=1ms
Reply from 2001::5: bytes=1500 time=1ms
Reply from 2001::5: bytes=1500 time=1ms
Reply from 2001::5: bytes=1500 time=1ms
Reply from 2001::5: bytes=1500 time=1ms
Reply from 2001::5: bytes=1500 time=1ms
Reply from 2001::5: bytes=1500 time=1ms
Reply from 2001::5: bytes=1500 time=1ms
Reply from 2001::5: bytes=1500 time=1ms

Success rate is 100 percent (10/10), round-trip min/avg/max = 1/1/1 ms.
【检验方法】 将 100 个长度为1500Byte的数据包发送到指定的IPv6地址，指定的时间（ 3 秒）内，显示相应的探测信息，
最后输出一个统计信息。


配置指南 网络通信检测工具

###### 11.4.2 Traceroute 连通性测试

**配置效果**

在网络设备上采用Traceroute连通性测试，可以得知该网络设备和目的主机之间的路由拓扑信息，报文从网络设备到目的主机
经过了多少个网关。

**注意事项**

执行Traceroute操作的网络设备本身需要配置IP地址。

**配置方法**

 如果需要跟踪IPv4数据包到达目的主机经过哪些网关，可通过配置Traceroute IPv4命令 **。**

 如果需要跟踪IPv6数据包到达目的主机经过哪些网关，可通过配置Traceroute IPv6命令 **。**

**检验方法**

###### 输入traceroute命令，即可在CLI界面显示相关信息。

**相关命令**

Traceroute IPv4

```
【命令格式】 traceroute [ oob | vrf vrf-name | ip ] { adress ] [ probe number ] [ source source ] [ timeout seconds ] [ ttl
minimum maximum ] }
【参数说明】 oob：设置使用带外通道。当指定MGMT口作为源接口时，必须设置该参数。
vrf-name：VRF名字。
address：指定目的IPv4地址或域名。
number：指定发送的探测的数量，范围：1~255。
source：指定报文源IPv4地址或源接口。其中，环回接口地址（例如127.0.0.1）不允许作为源地址
seconds：指定超时的时间，范围：1~10（秒）。
minimum maximum：指定最小和最大TTL值，范围：1~255。
【命令模式】 在普通用户模式下，只能运行基本的traceroute功能；在特权用户模式下，还可以运行traceroute的扩展功
能。
【使用指导】 Traceroute命令主要用于检查网络的连通性，并在网络故障发生时，准确的定位故障发生的位置。要使用域
名功能，则要先配置域名服务器，具体配置请参考DNS配置部分。
```

Traceroute IPv6

```
【命令格式】 traceroute [ vrf vrf-name | [ oob ] ipv6 ] { address [ probe number ] [ timeout seconds ] [ ttl minimum
```

配置指南 网络通信检测工具

```
maximum ] }
【参数说明】 oob：设置使用带外通道。当指定MGMT口作为源接口时，必须设置该参数。
vrf-name：VRF名字。
address：指定目的IPv6地址或域名。
number：指定发送的探测的数量，范围：1~255。
seconds：指定超时时间，范围：1~10（秒）。
minimum maximum：指定最小和最大TTL值，范围：1~255。
【配置模式】 在普通用户模式下，只能运行基本的traceroute ipv6功能；在特权用户模式下，还可以运行traceroute ipv6
的扩展功能。
【使用指导】 Traceroute ipv6命令主要用于检查网络的连通性，并在网络故障发生时，准确的定位故障发生的位置。要使
用域名功能，则要先配置域名服务器，具体配置请参考DNS配置部分。
```

**配置举例**

######  网络畅通的 Traceroute 举例

【配置方法】 在特权模式下，输入Traceroute IPv6地址3002::1。
Ruijie#
Ruijie# traceroute ipv6 3004::1
< press Ctrl+C to break >
Tracing the route to 3004::1
1 3000::1 0 msec 0 msec 0 msec
2 3001::1 4 msec 4 msec 4 msec
3 3002::1 8 msec 8 msec 4 msec

从上面的结果可以清楚地看到，从源地址要访问IP地址为3002::1的主机，网络数据包都经过了哪些网关（ 1
－ 3 ），同时给出了到达该网关所花费的时间。

######  网络中某些网关不通的 Traceroute 举例

【配置方法】 在特权模式下，输入Traceroute IPv4地址 2 02.108.37.42。


配置指南 网络通信检测工具

Ruijie# traceroute 202.108.37.42
< press Ctrl+C to break >
Tracing the route to 202.108.37.42
1 192.168.12.1 0 msec 0 msec 0 msec
2 192.168.9.2 0 msec 4 msec 4 msec
3 192.168.110.1 16 msec 12 msec 16 msec
4 * * *
5 61.154.8.129 12 msec 28 msec 12 msec
6 61.154.8.17 8 msec 12 msec 16 msec
7 61.154.8.250 12 msec 12 msec 12 msec
8 218.85.157.222 12 msec 12 msec 12 msec
9 218.85.157.130 16 msec 16 msec 16 msec
10 218.85.157.77 16 msec 48 msec 16 msec
11 202.97.40.65 76 msec 24 msec 24 msec
12 202.97.37.65 32 msec 24 msec 24 msec
13 202.97.38.162 52 msec 52 msec 224 msec
1 4 202.96.12.38 84 msec 52 msec 52 msec
15 202.106.192.226 88 msec 52 msec 52 msec
16 202.106.192.174 52 msec 52 msec 88 msec
17 210.74.176.158 100 msec 52 msec 84 msec
18 202.108.37.42 48 msec 48 msec 52 msec

(^) 从上面的结果可以清楚地看到，从源地址要访问IP地址为202.108.37.42的主机，网络数据包都经过了哪些
网关（ 1 － 17 ），并且网关 4 出现了故障。

######  网络畅通的 Traceroute ipv6 举例

【配置方法】 在特权模式下，输入Traceroute IPv6地址3004::1。
Ruijie# traceroute ipv6 3004::1
< press Ctrl+C to break >
Tracing the route to 3004::1
1 3000::1 0 msec 0 msec 0 msec
2 3001::1 4 msec 4 msec 4 msec
3 3002::1 8 msec 8 msec 4 msec
4 3004::1 4 msec 28 msec 12 msec
从上面的结果可以清楚地看到，从源地址要访问IP地址为3004::1的主机，网络数据包都经过了哪些网关（ 1
－ 4 ），同时给出了到达该网关所花费的时间。

######  网络中某些网关不通的 Traceroute IPv6 举例

【配置方法】 在特权模式下，输入Traceroute IPv6地址3004::1。


配置指南 网络通信检测工具

Ruijie# traceroute ipv6 3004::1
< press Ctrl+C to break >
Tracing the route to 3004::1
1 3000::1 0 msec 0 msec 0 msec
2 3001::1 4 msec 4 msec 4 msec
3 3002::1 8 msec 8 msec 4 msec
4 * * *
5 3004::1 4 msec 28 msec 12 msec
从上面的结果可以清楚地看到，从源地址要访问IP地址为3004::1的主机，网络数据包都经过了哪些网关（ 1
－ 5 ），并且网关 4 出现了故障。


配置指南 TCP

### 12 TCP

#### 12.1 概述

TCP协议为应用层提供了一个可靠的、有连接的基于IP的传输层协议。

应用层向TCP层发送用于网间传输的、用 8 位字节表示的数据流，然后TCP把数据流分割成适当长度的报文段，最大分段大
小（MSS）通常受该计算机连接的网络的数据链路层的最大传送单元（MTU）限制。之后TCP把报文传给IP层，由它来通过
网络将报文传送给接收端实体的TCP层。

TCP为了保证不发生丢包，就给每个字节一个序号，同时序号也保证了传送到接收端实体的包的按序接收。然后接收端实体对
已成功收到的字节发回一个相应的确认(ACK)；如果发送端实体在合理的往返时延(RTT)内未收到确认，那么对应的数据（假设
丢失了）将会被重传。

 在数据正确性与合法性上，TCP用一个校验和函数来检验数据是否有错误，在发送和接收时都要计算校验和。

```
同时可以使用MD 5 认证对数据进行校验。
```

 在保证可靠性上，采用超时重传和捎带确认机制。

######  在流量控制上，采用滑动窗口协议，协议中规定，对于窗口内未经确认的分组需要重传。

**协议规范**

 RFC 793：Transmission Control Protocol

 RFC 1122：Requirements for Internet Hosts -- Communication Layers

 RFC 1191：Path MTU Discovery

 RFC 1213：Management Information Base for Network Management of TCP/IP-based internets:MIB-II

 RFC 2385：Protection of BGP Sessions via the TCP MD5 Signature Option

 RFC 4022：Management Information Base for the Transmission Control Protocol (TCP)

#### 12.2 典型应用

典型应用 场景描述
TCP性能优化 TCP传输路径上某一段链路的MTU比较小，为了避免TCP报文分片，可以开启TCP
的路径MTU发现功能。
TCP连接异常检测 TCP探测对端是否还在正常工作。


配置指南 TCP

###### 12.2.1 TCP 性能优化

**应用场景**

以下图为例，A和D建立TCP连接，A和B之间链路的MTU是 1500 字节，B和C之间链路的MTU是 1300 字节，C和D
之间链路的MTU是 1500 字节，为了使TCP传输性能达到最优，需要避免TCP报文在设备B和设备C上分片。

图 12 - 1

【注释】 A、B、C和D为路由器。

**功能部署**

 在A和D上开启TCP的路径MTU发现功能。

###### 12.2.2 TCP 连接异常检测

**应用场景**

以下图为例，用户远程登陆到设备A，用户异常关机，如果设备A等待TCP重传超时，会导致用户的TCP连接残留比较长的
一段时间，可以利用TCP保活功能快速检测出用户的TCP连接异常。

图 12 - 2

【注释】 A是路由器。

**功能部署**


配置指南 TCP

 在设备A上开启TCP保活功能。

#### 12.3 功能详解

**基本概念**

######  TCP 首部格式

0 1 2 3

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Source Port | Destination Port |

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Sequence Number |

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Acknowledgment Number |

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Data | |U|A|P|R|S|F| |

| Offset| Reserved |R|C|S|S|Y|I| Window |

| | |G|K|H|T|N|N| |

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Checksum | Urgent Pointer |

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Options | Padding |

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| data |

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

 Source Port是源端口， 16 位。

 Destination Port是目的端口， 16 位。

 Sequence Number是序列号， 32 位。

 Acknowledgment Number是确认序列号， 32 位。

 Data Offset是数据偏移， 4 位，该字段的值是TCP首部（包括选项）长度除以 4 。


配置指南 TCP

 标志位： 6 位，URG表示Urgent Pointer字段有意义，ACK表示Acknowledgment Number字段有意义，PSH表示Push
功能，RST表示复位TCP连接，SYN表示SYN报文（在建立TCP连接的时候使用），FIN表示发送方没有数据需要发
送了（在关闭TCP连接的时候使用）。

 Window表示接收缓冲区的空闲空间， 16 位，用来告诉TCP连接对端自己能够接收的最大数据长度。

 Checksum是校验和， 16 位。

 Urgent Pointers是紧急指针， 16 位，只有URG标志位被设置时该字段才有意义，表示紧急数据相对序列号（Sequence
Number字段的值）的偏移。

######  TCP 三次握手

 TCP三次握手的过程如下：

(1) 客户端发送SYN报文给服务器端。

(2) 服务器端收到SYN报文，回应一个SYN ACK报文。

(3) 客户端收到服务器端的SYN报文，回应一个ACK报文。

 三次握手完成，TCP客户端和服务器端成功地建立连接，可以开始传输数据了。

**功能特性**

功能特性 作用
配置SYN超时 配置TCP发送SYN报文或者SYN ACK报文后等待应答报文的超时
配置窗口大小 配置窗口大小
配置端口不可达时是否发送
reset报文

```
配置在收到端口不可达的TCP报文时是否发送reset报文
```

配置MSS 配置TCP连接的MSS
路径MTU发现功能 探测TCP传输路径上的最小MTU，根据最小MTU调整发送的TCP报文的大小，避免分片
TCP保活功能 探测TCP连接对端是否还在正常工作

###### 12.3.1 配置 SYN 超时

**工作原理**

建立TCP连接需要经过三次握手：发起方先发送SYN报文，响应方回应SYN+ACK报文，然后发起方再回应ACK。

 在发起方发送SYN报文后，如果响应方一直不回应SYN+ACK报文，发起方会不断的重传SYN报文直到超过一定的重
传次数或超时时间。

 在发起方发送SYN报文后，响应方回应SYN+ACK报文，但发起方不再回复ACK，响应方也会一直重传直到超过一定
的重传次数或超时时间。（SYN报文攻击会出现这种情况。）


配置指南 TCP

**相关配置**

######  设置 TCP SYN 超时时间

 TCP SYN超时时间的缺省值是 20 秒。

 用户可以在全局配置模式下使用“ip tcp synwait-time seconds”命令设置SYN超时时间，取值范围是 5 到 300 ，单位
是秒。

 如果网络中存在SYN攻击，减少SYN超时时间可以防止一些资源消耗，但对连续的SYN攻击达不到效果。在设备主动
与外界请求建立连接时，减少SYN超时时间可以减少用户等待时间，如telnet。如果网络比较差也可以适当增加超时时
间。

### 11.0版本废弃了10.x版本的配置命令“ip tcp syntime-out”被废弃，但兼容10.x版本，如果执行了10.x版本的配置命

```
令，将自动转换成11.0版本的配置命令。
```

### 10.x版本该命令只对IPv4 TCP生效，从11.0版本开始该命令对IPv4 TCP和IPv6 TCP都生效。^

###### 12.3.2 配置窗口大小

**工作原理**

TCP的接收缓冲区用来缓存从对端接收到的数据，这些数据后续会被应用程序读取。一般情况下，TCP的窗口值反映接收缓
冲区的空闲空间的大小。对于带宽比较大、有大批量数据的连接，增大窗口可以显著提高TCP传输性能。

**相关配置**

######  设置窗口大小

 用户可以在全局配置模式下使用“ip tcp window-size size”命令设置窗口大小，单位是字节，取值范围是 128 到(65535<<
14)，缺省值是 65535 。如果窗口大于 65535 字节，自动开启窗口扩大功能。

 实际通告给对端的窗口大小是从配置的窗口大小和接收缓冲区的剩余空间取较小值。

### 10.x版本只对IPv4 TCP生效，从11.0版本开始对IPv4 TCP和IPv6 TCP都生效。^

###### 12.3.3 配置端口不可达时是否发送 reset 报文

**工作原理**

TCP协议在分发TCP报文给应用程序时，如果找不到该报文所属的TCP连接会主动回复一个reset报文以终止对端的TCP
连接。攻击者可能利用大量的端口不可达的TCP报文对设备进行攻击。


配置指南 TCP

**相关配置**

######  配置端口不可达时是否发送 reset 报文

收到端口不可达的TCP报文时，默认发送reset报文。

用户可以在全局配置模式下使用“no ip tcp send-reset”命令禁止发送reset报文。

如果允许发送reset报文，攻击者可能利用大量的端口不可达的TCP报文对设备进行攻击。

### 11.0版本废弃了10.x版本的配置命令“ip tcp not-send-rst”，并且兼容10.x版本，如果执行了10.x版本的配置命令，将

```
自动转换成11.0版本的配置命令。
```

### 10.x版本只对IPv4 TCP生效，从11.0版本开始对IPv4 TCP和IPv6 TCP都生效。^

###### 12.3.4 配置 MSS

**工作原理**

最大分段大小（Maxitum Segment Size，MSS），指一个TCP报文的数据载荷的最大长度，不包括TCP选项。

在TCP建立连接的三次握手中需要进行MSS协商，连接的双方都在SYN报文中增加MSS选项，其选项值表示本端最大能
接收的段大小，即对端最大能发送的段大小。连接的双方取本端发送的MSS值和接收对端的MSS值的较小者作为本连接最大
传输段大小。

发送SYN报文时MSS选项值的计算方法如下：

 IPv4 TCP：MSS = 对端IP地址对应的出口的IP MTU - 20 字节IP首部 - 20 字节TCP首部。

 IPv6 TCP：MSS = 对端IPv6地址对应的路径MTU - 40 字节IPv6首部 - 20 字节TCP首部。

### 10.x版本只对IPv4 TCP生效，从11.0版本开始对IPv4 TCP和IPv6 TCP都生效。^

### 实际生效的MSS是从根据MTU计算得到的MSS和用户配置的MSS取较小值。^

### 如果该连接支持某些选项，那么MSS还要减去选项^4 字节对齐后的长度值。如MD^5 选项要减去^20 字节，MD^5 选项长

```
度^18 字节，对齐后^20 字节。^
```

**相关配置**

######  设置 MSS

 用户可以在全局配置模式下使用“ip tcp mss max-segment-size”命令设置TCP连接的MSS，单位是字节，取值范围
是 68 到 10000 ，默认使用根据MTU计算得到的MSS。如果用户配置了MSS，实际生效的MSS是从根据MTU计算得
到的MSS和用户配置的MSS取较小值。

######  MSS太小会降低传输性能，增加MSS可以提高传输性能，但不是越大越好，选择MSS值可以参考接口的MTU，如果

###### MSS大于接口的MTU，TCP报文需要分片重组，会降低传输性能。


配置指南 TCP

###### 12.3.5 路径 MTU 发现功能

**工作原理**

RFC1191规定的TCP连接的路径MTU发现功能，用来发现TCP报文传输路径的最小MTU，避免分片重组，可以提高网络
带宽的利用率。IPv4 TCP路径MTU发现的过程如下：

(1) TCP源端将发送的TCP报文的外层IP首部设置不可分片标志位。

(2) 如果TCP 路径上某路由器的出口MTU 值小于该IP报文长度，则会丢弃报文，并向TCP源端发送ICMP差错报文，报
文中会携带该出口MTU 值。

(3) TCP源端通过解析该ICMP差错报文，可知TCP路径上当前最小的MTU值，即路径MTU。

(4) 后续TCP源端发送数据段的长度不超过MSS，MSS＝路径MTU－IP 头部长度－TCP头部长度。

**相关配置**

######  启用路径 MTU 发现功能

TCP缺省关闭路径MTU发现功能。

用户可以在全局配置模式下使用“ip tcp path-mtu-discovery”命令开启路径MTU发现功能。

### 10.x版本对IPv4 TCP和IPv6 TCP都生效。从11.0版本开始只对IPv4^ TCP生效，IPv6 TCP总是开启路径MTU发现功

```
能，并且不能关闭。
```

###### 12.3.6 TCP 保活功能

**工作原理**

如果TCP希望知道对端是否还在正常工作，可以开启保活功能。当TCP对端在一段时间内（称为空闲时间）没有发送过报文
给本端，本端开始发送保活报文，连续发送若干次，如果没有收到一个应答报文，就认为对端异常，关闭TCP连接。

**相关配置**

######  启用保活功能

 TCP缺省关闭保活功能。

 用户可以在全局配置模式下使用“ip tcp keepalive [interval num1] [times num2] [idle-period num3]”命令开启保活功
能。interval是时间间隔，默认值是 75 秒；times是发送保活报文的最大次数，默认值是 6 次；idle-period是空闲时间，
默认值是 15 分钟。

### 10.x版本只对IPv4 TCP生效，从11.0版本开始对IPv4 TCP和IPv6 TCP都生效。^


配置指南 TCP

### 10.x版本提供全局配置模式的配置命令“service^ tcp-keepalives-in”用来开启TCP服务器端的保活功能，11.0版本废

```
弃该命令，该命令隐藏，如果用户执行该命令，将转换成新的配置命令保存。
```

### 10.x版本提供全局配置模式的配置命令“service^ tcp-keepalives-out”用来开启TCP客户端的保活功能，11.0版本废

```
弃该命令，该命令隐藏，如果用户执行该命令，将转换成新的配置命令保存。
```

### 该命令不再区分服务器端和客户端，对所有的TCP连接都生效。^

#### 12.4 配置详解

配置项 配置建议 & 相关命令

TCP性能优化

### 可选配置，用于优化TCP连接的性能。^

ip tcp synwait-time (^) 配置建立TCP连接的超时时间。
ip tcp window-size 配置TCP窗口大小。
ip tcp send-reset
配置收到端口不可达的TCP报文时是否发送
reset报文。
ip tcp mss (^) 配置TCP连接的MSS。
ip tcp path-mtu-discovery 开启路径MTU发现功能。

### TCP连接异常检测 可选配置，用于检测TCP对端是否正常工作。^

ip tcp keepalive (^) 开启TCP保活功能。

###### 12.4.1 TCP 性能优化

**配置效果**

 TCP连接的传输性能达到最优，避免分片。

**注意事项**

-

**配置方法**

######  配置 SYN 超时

 可选配置。

 在TCP连接的两端配置。


配置指南 TCP

######  配置 TCP 窗口大小

 可选配置。

 在TCP连接的两端配置。

######  配置端口不可达时是否发送 reset 报文

 可选配置。

 在TCP连接的两端配置。

######  配置 MSS

 可选配置。

 在TCP连接的两端配置。

######  配置 TCP 的路径 MTU 发现功能

 可选配置。

######  在TCP连接的两端配置。

**检验方法**

-

**相关命令**

######  配置 SYN 超时

```
【命令格式】 ip tcp synwait-time seconds
【参数说明】 seconds：SYN报文超时时间。单位为秒，取值范围是 5 到 300 ，缺省值是 20 。
【命令模式】 全局模式
【使用指导】 如果网络中存在SYN攻击，减少SYN超时时间可以防止一些资源消耗，但对连续的SYN攻击达不到效果。
在设备主动与外界请求建立连接时，减少SYN超时时间可以减少用户等待时间，如telnet。如果网络比较差
也可以适当增加超时时间。
```

######  配置 TCP 窗口大小

```
【命令格式】 ip tcp window-size size
【参数说明】 size：单位是字节，取值范围是 128 到( 65535 << 14)，缺省值是 65535 。
【命令模式】 全局模式
【使用指导】 -^
```

######  配置端口不可达时是否发送 reset 报文

```
【命令格式】 ip tcp send-reset^
【参数说明】 -
```

配置指南 TCP

```
【命令模式】 全局模式
【使用指导】 收到端口不可达的TCP报文时，默认发送reset报文。
```

######  配置 MSS

```
【命令格式】 ip tcp mss max-segment-size
【参数说明】 max-segment-size：MSS的上限值。单位为字节，取值范围是 68 到 10000 ，默认使用根据MTU计算得到的
MSS。
【命令模式】 全局模式
【使用指导】 ip tcp mss的作用就是限制即将建立的TCP连接的MSS的最大值。任何新建立的连接协商的MSS值不能超
过配置的值。如果要减小连接的最大MSS值，可以配置该命令，一般情况下不需要配置。
```

######  配置路径 MTU 发现功能

```
【命令格式】 ip tcp path-mtu-discovery [ age-timer minutes | age-timer infinite ]
【参数说明】 age-timer minutes：TCP在发现路径MTU后，重新进行探测的时间间隔。单位是分钟，取值范围是 10 到
30 。缺省值是 10 。
age-timer infinite：TCP在发现路径MTU后，不重新探测。
【命令模式】 全局模式
【使用指导】 TCP的路径MTU发现功能是按RFC1191实现的，这个功能可以提高网络带宽的利用率。当用户使用TCP
来批量传输大块数据时，该功能可以使传输性能得到明显提升。
按RFC1191的描述，TCP在发现路径MTU后，隔一段时间可以使用更大的MSS来探测新的路径MTU。这
个时间间隔就是使用参数age-timer来指定。当设备发现的路径MTU比TCP连接两端协商出来的MSS小时，
设备就会按上述配置时间间隔，去尝试发现更大的路径MTU。直到路径MTU达到MSS的值，或者用户停止
这个定时器，这个探测过程才会停止。停止这个定时器，使用age-timer infinite参数。
```

**配置举例**

######  开启 TCP 的路径 MTU 发现功能。

```
【配置方法】 在设备上开启TCP的路径MTU发现功能，重新探测的时间间隔取缺省值。
Ruijie# configure terminal
Ruijie(config)# ip tcp path-mtu-discovery
Ruijie(config)# end
```

```
【检验方法】 用户可以执行命令show tcp pmtu查看IPv4 TCP连接的路径MTU。
Ruijie# show tcp pmtu
Number Local Address Foreign Address PMTU
1 192.168.195.212.23 192.168.195.112.13560 1440
用户可以执行命令show ipv6 tcp pmtu查看IPv6 TCP连接的路径MTU。
Ruijie# show ipv6 tcp pmtu
```

配置指南 TCP

```
【配置方法】 在设备上开启TCP的路径MTU发现功能，重新探测的时间间隔取缺省值。
Ruijie# configure terminal
Ruijie(config)# ip tcp path-mtu-discovery
Ruijie(config)# end
```

```
【检验方法】 用户可以执行命令show tcp pmtu查看IPv4 TCP连接的路径MTU。
Number Local Address Foreign Address PMTU
1 1 000::1: 23 1 000::2.13560 1440
```

**常见错误**

-

###### 12.4.2 TCP 连接异常检测

**配置效果**

 TCP探测对端是否还在正常工作。

**注意事项**

-

**配置方法**

######  开启保活功能

 可选配置。

**检验方法**

-

**相关命令**

######  开启保活功能

```
【命令格式】 ip tcp keepalive [interval num1] [times num2] [idle-period num3]
【参数说明】 interval num1：发送保活报文的时间间隔，单位是秒，取值范围是 1 到 120 ，缺省值是 75 秒。
times num2：发送保活报文的最大次数，取值范围是 1 到 10 ，缺省值是 6 。
```

配置指南 TCP

```
idle-period num3：空闲时间，即对端没有向本端发送过报文的时间长度，单位是秒，取值范围是 60 到 1800 ，
缺省值是 15 分钟。
【命令模式】 全局模式
【使用指导】 如果TCP希望知道对端是否还在正常工作，可以开启保活功能，默认关闭。
假设用户开启保活功能，时间间隔，次数和空闲时间都使用缺省值，TCP在 15 分钟内没有收到过对端发送的
报文，开始发送保活报文，每隔 75 秒发送一次，连续发送 6 次，如果没有收到对方发送的任何TCP报文，
就认为TCP连接无效，自动释放TCP连接。
```

**配置举例**

######  开启 TCP 保活功能。

```
【配置方法】 在设备上开启TCP保活功能，空闲时间是 3 分钟，发送保活报文的时间间隔是 60 秒，如果连续发送 4 次保
活报文，没有收到对方发送的任何TCP报文，就认为TCP连接无效。
Ruijie# configure terminal
Ruijie(config)# ip tcp keepalive interval 60 times 4 idle-period 180
Ruijie(config)# end
```

```
【检验方法】 用户远程登录到设备，然后用户异常关机，在设备上执行show tcp connect观察用户的IPv4 TCP连接被删除
的时间。
```

**常见错误**

-

#### 12.5 监视与维护

**清除各类信息**

###### -

**查看运行情况**

作用 命令

显示IPv4 TCP连接的基本信息
show tcp connect [local-ip a.b.c.d] [local-port num] [peer-ip a.b.c.d] [peer-po
rt num]
显示IPv4 TCP连接的统计信息 show tcp^ connect statistics^

显示IPv4 TCP路径MTU的信息
show tcp pmtu [local-ip a.b.c.d] [local-port num] [peer-ip a.b.c.d] [peer-port
num]


配置指南 TCP

显示IPv4 TCP 端口使用情况 show tcp port [num]
显示 IPv4 TCP参数信息 show tcp parameter
显示 IPv4 TCP统计信息 show tcp statistics

显示IPv6 TCP连接的基本信息
show ipv6 tcp connect [local-ipv6 X:X:X:X::X] [local-port num] [peer-ipv6 X:
X:X:X::X] [peer-port num]
显示IPv6 TCP连接的统计信息 show ipv6 tcp connect statistics

显示IPv6 TCP路径MTU的信息
show ipv6 tcp pmtu [local-ipv6 X:X:X:X::X] [local-port num] [peer-ipv6 X:X:X:
X::X] [peer-port num]
显示IPv6 TCP 端口使用情况 show ipv6 tcp^ port [num]^

**查看调试信息**

### 输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。^

作用 命令
查看IPv4 TCP报文的调试信息 debug ip tcp packet [ in | out] [local-ip a.b.c.d] [peer-ip a.b.c.d] [global | vrf
vrf-name] [local-port num] [peer-port num] [deeply]
查看IPv4 TCP连接的调试信息 debug ip tcp transactions^ [local-ip^ a.b.c.d] [peer-ip^ a.b.c.d] [local-port^ num]
[peer-port num]
查看IPv6 TCP报文的调试信息 debug ipv6 tcp packet [ in | out] [local-ipv6 X:X:X:X::X] [peer-ipv6 X:X:X:X::X]
[global | vrf vrf-name] [local-port num] [peer-port num] [deeply]
查看IPv6 TCP连接的调试信息 debug ipv6 tcp transactions [local-ipv6 X:X:X:X::X] [peer-ipv6 X:X:X:X::X]
[local-port num] [peer-port num]


配置指南 软件IPv4/v6快转

### 13 软件 IPv4/v6 快转

#### 13.1 概述

在不支持硬件转发的产品上，由软件转发IPv4/v6报文，为了使软件转发性能达到最优，我司实现了软件IPv4/v6快转。

快转主要维护两张表：转发表和邻接表。转发表用来存放路由；邻接表用来存放下一跳的链路层信息，相当于ARP表和IPv6
邻居表。

快转可以主动解析下一跳，还可以实现流量负载均衡。

### 下文仅介绍软件IPv4/v6的相关内容。^

**协议规范**

-

#### 13.2 典型应用

典型应用 场景描述
流量负载均衡 在网络路由中，当路由前缀关联到多个下一跳时，快转可以在多个下一跳中实现流量负载均衡。

###### 13.2.1 流量负载均衡

**应用场景**

以下图为例，路由器A上，对于某条路由前缀关联 3 个下一跳，即链路 1 、链路 2 和链路 3 。缺省情况下，快转使用目的IP
地址进行负载均衡，还可以根据源IP地址和目的IP地址进行负载均衡。

图 13 - 1


配置指南 软件IPv4/v6快转

【注释】 A为运行软件快转的路由器。
B、C、D可以为其它转发设备。

**功能部属**

 路由器A上运行软件快转。

#### 13.3 功能详解

**基本概念**

IPv4/v6快转主要涉及以下基本概念：

######  路由表

IPv4/v6路由表中存储着指向特定网络地址的路径，同时含有网络周边的拓扑信息。在报文转发的过程中IPv4/v6快转根据路
由表选择报文的传输路径。

######  邻接节点

邻接节点包含了被路由报文的输出接口信息。例如下一跳列表、下一个处理部件、链路层输出封装等信息。当报文与该邻接节
点匹配时，直接对报文进行封装，而后调用该节点的发送函数即可实现转发。为了便于检索和更新，邻接节点构成的表一般组
织成哈希表的形式；为了支持路由负载均衡，邻接节点的下一条列表信息被组织为负载均衡表的形式；邻接节点中也可以不包
含下一跳信息，也可以包含下一个处理部件的索引号（例如其它线卡，多业务卡）。

######  主动解析


配置指南 软件IPv4/v6快转

快转支持主动解析下一跳。对于以太网接口上的下一跳，如果不知道MAC地址，快转将主动解析下一跳。IPv 4 快转请求ARP
模块解析下一跳；

IPv 6 快转请求ND模块解析下一跳。

######  报文转发路径

报文的路由转发是根据报文的IPv4/v6地址，所以如果指定了报文源IPv4/v6地址和目的IPv4/v6地址，则该报文的转发路径
将是确定的。

###### 13.3.1 快转负载均衡策略

###### 快转负载均衡就是利用多个网络设备通道均衡分担流量。

**工作原理**

快转支持报文的负载均衡处理，目前实现两种基于IP地址的负载均衡策略。在快转模型中，当路由前缀关联到多个下一跳时，
即多径路由，该路由将关联到一个负载均衡表，并依路由权重实现负载均衡。当IPv4/v6报文依最长前缀匹配到该均衡表时，
快转根据报文的IPv4/v6地址进行散列，选中其中的一条路径转发报文。

IPv4/v6快转支持两种负载均衡模式，分别是根据报文的目的IP地址进行均衡、根据报文的源IP和目的IP地址进行均衡。

**相关配置**

######  配置 IPv4 源 IP 地址 + 目的 IP 地址负载均衡算法

 缺省根据IPv4报文的目的IP地址进行均衡。

 可以根据ip ref load-sharing original配置该负载均衡算法 **。**

 配置后根据IPv4报文的目的IP地址和源IP地址进行均衡。

######  配置 IPv 6 源 IP 地址 + 目的 IP 地址负载均衡算法

 缺省根据IPv 6 报文的目的地址进行均衡。

 根据ipv6 ref load-sharing original配置该负载均衡算法。

 配置后根据IPv 6 报文的目的IP地址和源IP地址进行均衡。

#### 13.4 配置详解

```
配置项 配置建议&相关命令
```

```
配置快转负载均衡策略
```

### 可选配置。^

```
ip ref load-sharing original 启动IPv4源IP地址 + 目的IP地址负载均衡算法
ipv6 ref load-sharing original 启动Ipv 6 源IP地址 + 目的IP地址负载均衡算法
```

配置指南 软件IPv4/v6快转

###### 13.4.1 配置快转负载均衡策略

**配置效果**

路由快转支持的两种选路策略如下：

 按IPv4/v6报文的目的IPv4/v6地址进行均衡，对报文的目标地址进行散列，权重大的路径被选中的机率大。缺省采用此
策略。

 按IPv4/v6报文的目的IPv4/v6地址和源IPv4/v6地址进行均衡，对报文的目的IPv4/v6地址和源IPv4/v6地址进行散列，
权重大的路径被选中的机率大。

**注意事项**

-

**配置方法**

 可选配置。

 在IPv4/v6环境下，如果需要根据源IP地址+目的IP地址进行流量均衡，可采用此配置。

 在连接多条链路的路由设备上配置。

**检验方法**

使用show ip ref adjacency statistic命令可以查看IPv 4 快转的负载均衡策略；

使用show ipv6 ref adjacency statistic命令可以查看IPv 6 快转的负载均衡策略。

**相关命令**

**配置** IPv4 **源** IP **地址** + **目的** IP **地址负载均衡算法**

```
【命令格式】 ip ref load-sharing original
【参数说明】 -
【命令模式】 全局模式
```

【使用指导】

######  - 配置 IPv 6 源 IP 地址 + 目的 IP 地址负载均衡算法

```
【命令格式】 ipv6^ ref load-sharing original^
```

配置指南 软件IPv4/v6快转

```
【参数说明】 -
【命令模式】 全局模式
```

**配置举例**

######  配置基于 IPv4 源 IP 地址 + 目的 IP 地址负载均衡

```
【网络环境】
图 13 - 2
```

###### 在路由器A上，对于某条路由前缀关联 3 个下一跳，即链路 1 、链路 2 和链路 3 。

```
【配置方法】 在路由器A上配置IPv4源IP地址 + 目的IP地址负载均衡
A A#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
A(config)#ip ref load-sharing original
【检验方法】
A #show ip ref adjacency statistics
adjacency balance table statistic:
source-dest-address load-sharing
balance: 0
```

```
adjacency node table statistic:
total : 3
local : 1
glean : 0
forward: 0
discard: 0
mcast : 1
punt : 1
bcast : 0
```

配置指南 软件IPv4/v6快转

**常见配置错误**

-

#### 13.5 监视与维护

**统计快转报文信息**

快转报文统计信息即快转所处理的报文统计信息，包括了转发的报文数目，以及各种原因丢弃的报文数目等。快转提供配置信
息查看和清除当前的统计信息，以供判断报文的转发行为是否和预期相同。

```
命令 作用
show ip ref packet statistics 显示IPv4快转当前的报文统计信息
clear ip ref packet statistics 清除IPv4快转当前的报文统计信息
show ipv6 ref packet statistics 显示IPv6快转当前的报文统计信息
clear ipv6 ref packet statistics 清除IPv6快转当前的报文统计信息
```

**查看邻接信息**

用户可以通过以下命令来查看当前的邻接信息：

```
命令 作用
showip ref adjacency[glean | local | ip-address |
{interfaceinterface_type interface_number)| discard |
statistics]
```

```
可以指定显示IPv4快转的集合邻接、本地邻接、指定IP
对应邻接、指定接口关联邻接及所有邻接节点相关信息。
showipv6 ref adjacency[glean | local | ipv6-address |
(interfaceinterface_type interface_number)| discard |
statistics]
```

```
可以指定显示IPv6快转的集合邻接、本地邻接、指定IPv6
地址对应邻接、指定接口关联邻接及所有邻接节点相关信
息。
```

**查看主动解析信息**

用户可以通过以下命令来查看需要主动解析的下一跳：

```
命令 作用
showip ref resolve-list 查看IPv4快转主动解析的下一跳。
showipv6 ref resolve-list 查看IPv6快转主动解析的下一跳。
```

**查看报文转发路径信息**


配置指南 软件IPv4/v6快转

报文的路由转发是根据报文的IPv4/v6地址，所以如果指定了报文源IPv4/v6地址和目的IPv4/v6地址，则该报文的转发路径
将是确定的。执行下面的命令，并指定报文的源IPv4/v6地址与目的IPv4/v6地址，将会显示该报文的实际转发路径，比如报
文丢弃、提交CPU或转发，进一步还可以知道从哪个接口转发等等。

```
命令 作用
show ip ref exact-route [oob| vrf vrf_name]
source-ipaddressdest_ipaddress
```

```
显示某特定报文的实际转发路径。oob表示带外，即管理
口所属的管理网络。
show ipv6 ref exact-route[oob| vrf
vrf-name ]src-ipv6-addressdst-ipv6-address
```

```
显示某特定IPv6报文的实际转发路径。oob表示带外，即
管理口所属的管理网络。
```

**查看快转表路由信息**

通过下面的命令可以查看快转表的路由信息：

```
命令 作用
show ip ref route[oob | vrfvrf_name] [default | {ip mask}|
statistics]
```

```
显示当前IPv4快转表中的路由信息，参数default表示显
示缺省路由。oob表示带外，即管理口所属的管理网络。
show ipv6 ref route [oob | vrf vrf-name ] [ default | statistics |
prefix/len ]
```

```
显示当前IPv6快转表中的路由信息，参数default表示显
示缺省路由。oob表示带外，即管理口所属的管理网络。
```

1-7 ![ref6]

[ref1]: Output.001.png
[ref2]: Output.004.png
[ref3]: Output.005.png
[ref4]: Output.006.png
[ref5]: Output.007.png
[ref6]: Output.011.png
[ref7]: Output.012.png
[ref8]: Output.013.png
[ref9]: Output.017.png

【检验方法】 

+ 通过show spanning-tree interface命令查看端口的配置信息。

```
Ruijie#show spanning-tree int gi 0/3 
PortAdminPortFast : Enabled 
PortOperPortFast : Enabled 
PortAdminAutoEdge : Enabled 
PortOperAutoEdge : Enabled
PortAdminLinkType : auto 
PortOperLinkType : point-to-point
PortBPDUGuard : Enabled 
PortBPDUFilter : Disabled PortGuardmode : None

#####MST 0 vlans mapped :ALL
PortState : forwarding
PortPriority : 128
PortDesignatedRoot : 0.00d0.f822.3344
PortDesignatedCost : 0
PortDesignatedBridge :0.00d0.f822.3344
PortDesignatedPortPriority : 128
PortDesignatedPort : 4
PortForwardTransitions : 1
PortAdminPathCost : 20000
PortOperPathCost : 20000
Inconsistent states : normal
PortRole : designatedPort
```

