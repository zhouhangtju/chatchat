# 配置指南-以太网交换



本分册介绍以太网交换配置指南相关内容，包括以下章节：

1. 接口 
1. MAC 地址 
1. Aggregate Port 
1. VLAN 
1. MAC VLAN 
1. Super VLAN 
1. Protocol VLAN 配置 
1. Private VLAN 
1. Voice VLAN 
1. MSTP 
1. GVRP 
1. LLDP 
1. QINQ 
1. ERPS 



## 1  接口

### 1.1 概述 

接口是网络设备上能够实现数据交换功能的重要部件。我司网络设备上支持两种类型的接口：物理接口和逻辑接口。物理接口 意味着该接口在设备上有对应的、实际存在的硬件接口，如：百兆以太网接口、千兆以太网接口等。逻辑接口意味着该接口在 路由器上没有对应的、实际存在的硬件接口，逻辑接口可以与物理接口关联，也可以独立于物理接口存在，如： Loopback 接 口和 Tunnel 接口等等。实际上对于网络协议而言，无论是物理接口还是逻辑接口，都是一样对待的。

### 1.2 典型应用

| 典型应用                       | 场景描述                                           |
| ------------------------------ | -------------------------------------------------- |
| 以太网物理接口实现二层数据交换 | 通过二层以太网物理接口实现网络设备的二层数据通信。 |
| 以太网物理接口实现三层数据路由 | 通过三层以太网物理接口实现网络设备的三层数据通信。 |

#### 1.2.1 以太网物理接口二层数据交换

##### 应用场景 

三台设备 Switch A、Switch B 和 Switch C 组成了一个简单的二层数据交换网络。 

##### 功能部属

- Switch A 和 Switch B 分别通过千兆以太网物理接口 GigabitEthernet 1/0/1 和 GigabitEthernet 2/0/1 进行相连。
- Switch B 和 Switch C 分别通过千兆以太网物理接口 GigabitEthernet 2/0/2 和 GigabitEthernet 3/0/1 进行相连。
- 将接口 GigabitEthernet 1/0/1、GigabitEthernet 2/0/1、GigabitEthernet 2/0/2 和 GigabitEthernet3/0/1 配置为 Trunk 口。 
- 分别在 Switch A 和 Switch C 上创建一个交换虚拟接口(Switch Virtual Interface, SVI) SVI 1，并给 SVI 1 接口配置相同网 段的 IP 地址，其中，Switch A 的 SVI 1 接口的 IP 地址配置为 192.168.1.1/24，Switch C 的 SVI 1 接口的 IP 地址配置为 192.168.1.2/24。 
- 在 Switch A 和 Switch C 上分别执行 ping 192.168.1.2 和 ping 192.168.1.1 操作，可以实现设备 B 上的二层数据交换功能。

#### 1.2.2 以太网物理接口三层路由通信

##### 应用场景

三台设备 Switch A、Switch B 和 Switch C 组成了一个简单的三层数据通信网络 

##### 功能部属 

- Switch A 和 Switch B 分别通过千兆以太网物理接口 GigabitEthernet 1/0/1 和 GigabitEthernet 2/0/1 进行相连。
- Switch B 和 Switch C 分别通过千兆以太网物理接口 GigabitEthernet 2/0/2 和 GigabitEthernet 3/0/1 进行相连。
- 将接口 GigabitEthernet 1/0/1、GigabitEthernet 2/0/1、GigabitEthernet 2/0/2 和 GigabitEthernet3/0/1 配置为三层路由口。
- 分别给 GigabitEthernet 1/0/1 和 GigabitEthernet 2/0/1 配置相同网段的 IP 地址，其中，GigabitEthernet 1/0/1 的 IP 地址 配置为 192.168.1.1/24，GigabitEthernet 2/0/1 的 IP 地址配置为 192.168.1.2/24。 
- 分别给 GigabitEthernet 2/0/2 和 GigabitEthernet 3/0/1 配置相同网段的 IP 地址，其中，GigabitEthernet 2/0/2 的 IP 地址 配置为 192.168.2.1/24，GigabitEthernet 3/0/1 的 IP 地址配置为 192.168.2.2/24。 
- 在 Switch C 上配置一条静态路由表项使其能够三层直通 192.168.1.0/24 网段,  在 Switch A 上配置一条静态路由表 项使其能够三层直通 192.168.2.0/24 网段。 
- 在 Switch A 和 Switch C 上分别执行 ping 192.168.2.2 和 ping 192.168.1.1 操作，可以实现设备 B 上的三层路由通信功能。

### 1.3 功能详解

##### 基本概念 

######  接口类型分类 

锐捷设备的接口类型可分为以下两大类：

- 二层接口(L2 interface) (交换设备或者网关桥模式) 
- 三层接口(L3 interface) (三层设备支持) 

1. 常见的二层接口可分为以下几种类型：

+ 交换端口（Switch Port） 

+ 二层聚合端口（L2 Aggregate Port） 

2. 常见的三层接口可分为以下几种类型

- 路由端口（Routed Port） 

- 三层聚合端口（L3 Aggregate Port） 

- SVI 口 

- Loopback 接口 

- Tunnel 接口 

  

######  交换端口 

+ 交换端口由设备上的单个物理端口构成，只有二层交换功能。交换端口被用于管理物理接口和与之相关的第二层协议。

######  二层聚合端口 

+ 聚合端口是由多个物理成员端口聚合而成的。我们可以把多个物理链接捆绑在一起形成一个简单的逻辑链接，这个逻辑链接我们称之为一个聚合端口（以下简称聚合端口）。 对于二层交换来说聚合端口就好像一个高带宽的交换端口，它可以把多个端口的带宽叠加起来使用，扩展了链路带宽。此外， 通过二层聚合端口发送的帧还将在二层聚合端口的成员端口上进行流量平衡，如果聚合端口中的一条成员链路失效，二层聚合 端口会自动将这个链路上的流量转移到其他有效的成员链路上，提高了连接的可靠性。

######  SVI 口 

+ SVI 接口可以做为本机的管理接口，通过该管理接口管理员可管理设备。用户也可以创建 SVI 接口为一个网关接口，就相当于 是对应各个 VLAN 的虚拟接口，可用于三层设备中跨 VLAN 之间的路由。创建一个交换虚拟接口很简单，用户可通过 **interface** **vlan** 接口配置命令来创建 SVI 接口，然后给交换虚拟接口分配 IP 地址来建立 VLAN 之间的路由。
+ VLAN 20 的主机可直接互相通讯，无需通过三层设备的路由，若 VLAN 20 内的主机 A 想和 VLAN 30 内的主机 B 通讯必须通过 VLAN 20 对应的 SVI 1 和 VLAN30 对应的 SVI 2 才能实现。



######  路由端口 

+ 在三层设备上，可以把单个物理端口设置为路由端口，作为三层交换的网关接口。一个路由端口与一个特定的 VLAN 没有关系， 而是作为一个访问端口。路由端口不具备二层交换的功能。

+ 用户可通过 **no switchport** 命令将一个交换端口转变为路由端口，然后给路由端口分配 IP 地址来建立路由。注意的是，当使 用 **no switchport** 接口配置命令时，将删除该端口的所有二层特性。



######  三层聚合端口

三层聚合端口同二层聚合端口一样，也是由多个物理成员端口汇聚构成的一个逻辑上的聚合端口组。汇聚的端口必须为同类型 的三层接口。对于三层交换来说，聚合端口作为三层交换的网关接口，它相当于把同一聚合组内的多条物理链路视为一条逻辑 链路，是链路带宽扩展的一个重要途径。此外，通过三层聚合端口发送的帧同样能在三层聚合端口的成员端口上进行流量平衡， 当聚合端口中的一条成员链路失效后，三层聚合端口会自动将这个链路上的流量转移到其它有效的成员链路上，提高了连接的 可靠性。 

三层聚合端口不具备二层交换的功能。用户可通过 **no switchport** 命令将一个无成员的二层聚合端口转变为三层聚合端口，接 着将多个路由端口加入此三层聚合端口，然后给三层聚合端口分配 IP 地址来建立路由。

######  Loopback 口 

Loopback 接口是完全软件模拟的本地三层逻辑接口，它永远都处于 UP 状态。发往 Loopback 接口的数据包将会在设备本地处 理，包括路由信息。Loopback 接口的 IP 地址可以用来作为 OSPF 路由协议的设备标识、实施发向 Telnet 或者作为远程 Telnet 访问的网络接口等等。配置一个 Loopback 接口类似于配置一个以太网接口，可以把它看作一个虚拟的以太网接口。

######  Tunnel 口 

Tunnel 接口来实现隧道功能，允许利用传输协议(如 IP)来传送任意协议的网络数据包。同其它逻辑接口一样，Tunnel 接口也 是系统虚拟的接口。Tunnel 接口并不特别指定传输协议或者负载协议，它提供的是一个用来实现标准的点对点的传输模式。由 于 Tunnel 实现的是点对点的传输链路，所以对于每一个单独的链路都必须设置一个 Tunnel 接口。 

功能特性

| 功能特性                                | 作用                                                         |
| --------------------------------------- | ------------------------------------------------------------ |
| 接口配置命令的使用                      | 进入接口配置模式，在接口配置模式下用户可配置接口的相关属性。对于逻辑口，用户进入 接口模式时，如果该接口不存在，将会首先创建出该接口。 |
| 接口的描述和管理状态                    | 用户可以为一个接口起一个专门的名字来标识这个接口，有助于用户记住一个接口的功能； 用户可以设置接口的管理状态。 |
| 接口的 MTU                              | 用户可以通过设置端口的 MTU 来控制该端口允许收发的最大帧长。  |
| 配置接口带宽                            | 用户可以基于接口配置接口的带宽。                             |
| 配置接口的 Load-interval                | 用户可以指定每隔多少时间计算报文输入输出的负载情况。         |
| 配置接口载波时延                        | 用户可以调整接口的载波时延来调整接口状态从 Down 状态到 Up 状态或者从 Up 状态到 Down 状态的时间延时。 |
| 接口的 LinkTrap 策略                    | 在设备中可以基于接口配置是否发送该接口的 LinkTrap 信息。     |
| 接口索引永久化功能                      | 接口索引永久化功能，即设备重启后接口索引不变。               |
| 配置路由口                              | 在三层设备上，用户可以把物理端口设置为路由端口，作为三层交换的网关接口。 |
| 配置三层 AP 口                          | 在三层设备上，可以把 AP 端口设置为三层 AP 端口，作为三层交换的网关接口。 |
| 选择接口介质类型                        | 光电复用端口，用户可以根据需要选择使用光口还是电口。         |
| 接口的速率，双工、流控和自协 商因子模式 | 用户可以调整接口的速率，双工模式、流控模式和自协商因子模式。 |
| 模块自动检测                            | 在配置接口速率为自动协商模式的情况下，能够根据插入的模块类型自动调节接口的速率。 |
| 保护口                                  | 用户可以通过将某些端口设置为保护口来实现端口之间不能互相通信。同时还可以通过配置 操作来设置保护口之间不能进行路由。 |
| 端口违例恢复                            | 当端口因发生违例而被关闭之后，用户可以在全局模式下使用端口违例恢复命令来将所有违 例接口从错误状态中恢复过来，重新复位使能该接口。 |
| 接口节能管理                            | 用户配置接口节能使能，能够使接口工作在低功耗模式下。         |
| 端口震荡保护                            | 用户配置端口震荡保护功能，当端口发生震荡时，系统自动 shutdown 端口，用于保护端口 |

#### 1.3.1 接口配置命令的使用

用户可在全局配置模式下使用 **interface** 命令进入接口配置模式。在接口配置模式下用户可配置接口的相关属性。

##### 工作原理

在全局配置模式下输入 interface 命令，进入接口配置模式。对于逻辑口，用户进入接口模式时，如果该接口不存在，将会首先 创建出该接口。用户也可以在全局配置模式下使用 interface range 或 interface range macro 命令配置一定范围的接口（接口 的编号）。但是定义在一个范围内的接口必须是相同类型和具有相同特性的。 

对于逻辑口，可以在全局配置模式下通过执行 no interface 命令删除指定的逻辑接口。

######  接口编号规则

对于物理端口，在单机模式下编号由两部分组成：插槽号和端口在插槽上的编号，例如端口所在的插槽编号为 2，端口在插槽 上的编号为 3，则端口对应的接口编号为 2/3；在 VSU 模式或者堆叠模式下编号由三部分组成：设备号，插槽号和端口在插槽 上的编号，例如设备号为 1，端口所在的插槽编号为 2，端口在插槽上的编号为 3，则端口对应的接口编号为 1/2/3。 

设备号是从 1 到支持的成员设备的最大数量。

插槽的编号规则：静态插槽的编号固定为 0，动态插槽（可插拔模块或线卡）的编号是从 1－插槽的个数。动态插槽的编号规 则是：面对设备的面板，插槽按照从前至后，从左至右，从上至下的顺序一次排列，对应的插槽号从 1 开始依次增加。

插槽上的端口编号是从 1－插槽上的端口数，编号顺序是从左到右。 对于可以选择介质类型的设备，端口包括两种介质：光口和电口，称为光电复用端口，无论使用那种介质，都使用相同的端口

编号。 

对于聚合端口，其编号的范围为 1－设备支持的聚合端口个数。 

对于交换虚拟接口，其编号就是这个交换虚拟接口对应的 VLAN 的 VID。 

###### 配置一定范围的接口

用户可以使用全局配置模式下的 **interface range** 命令同时配置多个接口。当进入 **interface range** 配置模式时，此时设置的属 性适用于所选范围内的所有接口。

输入一定范围的接口。

interface range 命令可以指定若干范围段。

macro 参数可以使用范围段的宏定义，参见配置和使用端口范围的宏定义。

每个范围段可以使用逗号（,）隔开。 

同一条命令中的所有范围段中的接口必须属于相同类型。

当使用 interface range 命令时，请注意 range 参数的格式：

常见的有效的接口范围格式：

- FastEthernet device/slot/{第一个 port} - {最后一个 port}； 
- GigabitEthernet device/slot/{第一个 port} - {最后一个 port}； 
- TenGigabitEthernet device/slot/{第一个 port} - {最后一个 port}； 
- FortyGigabitEthernet device/slot/{第一个 port} - {最后一个 port}； 
- AggregatePort Aggregate-port 号– Aggregate-port 号，范围是 1～设备支持的最大聚合端口数量；
- vlan vlan-ID-vlan-ID, VLAN ID  范围 1～4094； 
- Loopback loopback-ID-loopback-ID,  范围是 1～2147483647； 
- Tunnel tunnel-ID-tunnel-ID,  范围是 0～设备支持的最大 Tunnel 端口数量减一。

在一个 interface range 中的接口必须是相同类型的，即或者全是 FastEthernet、GigabitEthernet 等。 

######  配置和使用端口范围的宏定义

用户可以自行定义一些宏来取代端口范围的输入。但在用户使用 interface range 命令中的 **macro** 关键字之前，必须先在全局 配置模式下使用 define interface-range 命令定义这些宏。

在全局配置模式下使用 no define interface-range macro_name 命令来删除设置的宏定义。

#### 1.3.2 接口的描述和管理状态

用户可以为一个接口起一个专门的名字来标识这个接口，有助于用户记住一个接口的功能。 用户可以进入接口模式对接口进行关闭和打开管理。

##### 工作原理

######  接口的描述

用户可以根据要表达的含义来设置接口的具体名称，比如，用户想将 GigabitEthernet 1/1 分配给用户 A 专门使用，用户就可以 将这个接口的描述设置为“Port for User A”。 

######  接口的管理状态

在某些情况下，用户可能需要禁用某个接口。用户可以通过设置接口的管理状态来直接关闭一个接口。如果关闭一个接口，则 这个接口上将不会接收和发送任何帧，这个接口将丧失这个接口对应的所有功能。用户也可以通过设置管理状态来重新打开一 个已经关闭的接口。接口的管理状态有两种：Up 和 Down，当端口被关闭时，端口的管理状态为 Down，否则为 Up。 

#### 1.3.3 接口的 MTU

用户可以通过设置端口的MTU来控制该端口允许收发的最大帧长。

##### 工作原理

当端口进行大吞吐量数据交换时，可能会遇到大于以太网标准帧长度的帧，这种帧被称为jumbo帧。MTU是指帧中有效数据
段的长度，不包括以太网封装的开销。

端口收到或者转发的帧，如果长度超过设置的MTU将被丢弃。

#### 1.3.4 配置接口带宽

##### 工作原理

主要用于一些路由协议(如OSPF路由协议)计算路由量度和RSVP计算保留带宽。修改接口带宽不会影响物理接口的数据传输速率。接口的带宽命令不能实际影响某个接口的带宽，它只是个路由参数，不会影响物理链路的接口的真正带宽。

#### 1.3.5 配置接口的 Load-interval

**工作原理**

接口的load-interval可以指定每隔多少时间计算报文输入输出的负载情况，一般是每隔 10 秒钟计算一次每秒中输入输出的报文数和比特数。

#### 1.3.6 配置接口载波时延

##### 工作原理

接口的载波时延Carry-delay是指接口链路的载波检测信号DCD从Down状态到Up状态或者从Up状态到Down状态的时间延时，如果DCD在延时之内发生变化，那么系统将忽略这种状态的变化而不至于上层的数据链路层重新协商。如果参数设置的比较大，那么几乎每次瞬间的DCD变化将无法被检测到；相反，如果参数设置成 0 ，那么每次微小的DCD信号的跳变都将被系统检测到，这样系统也就将增加不稳定性。

如果DCD载波中断时间比较长，那么将该参数设长些，可以尽快加速拓扑收敛和路由汇聚，以便网络拓扑或者路由表可以较快的收敛。如果相反，DCD载波中断时间小于网络拓扑或者路由汇聚所花的时间，那么应该将该参数设置相对的大些，以免造成没有必要的网络拓扑振荡或者路由振荡。

#### 1.3.7 接口的 LinkTrap 策略

在设备中，用户可以基于接口配置选择是否发送该接口的LinkTrap状态变化信息。

##### 工作原理

当接口的LinkTrap发送功能打开时，如果该接口的Link状态变化，SNMP将发出LinkTrap信息，反之则不发。

#### 1.3.8 接口索引永久化功能

和接口的名字一样，接口索引也可以用于标识一个接口，接口索引是一个接口的“身份ID”，每个接口创建时，系统会自动为每个接口分配不重复的接口索引值，而当设备重启后，一个接口的索引值可能会和重启前的不一致。接口索引永久化功能，即设备重启后接口索引不变。

##### 工作原理

当配置了该功能，设备重启后相同接口的接口索引值保持不变。




#### 1.3.9 配置路由口

##### 工作原理

在三层设备上，可以把物理端口设置为路由端口，作为三层交换的网关接口。路由端口不具备二层交换的功能。用户可通过no switchport命令将一个交换端口转变为路由端口，然后给路由端口分配IP地址来建立路由。注意的是，当使用no switchport接口配置命令时，将删除该端口的所有二层特性。

#### 1.3.10 配置三层 AP 口

##### 工作原理

在三层设备上，类似三层路由口一样，用户可通过no switchport命令将一个二层AP端口转变为三层AP端口，然后给该AP端口分配IP地址来建立路由。注意的是，当使用no switchport接口配置命令时，将删除该AP端口的所有二层特性。

当AP口中含有成员口时，不允许将二层AP口配置为三层AP口，反之，也不允许将带有成员口的三层AP口转变为二层AP口。

#### 1.3.11 选择接口介质类型

对于光电复用端口，用户可以根据需要选择使用光口还是电口。

##### 工作原理

用户可以选择使用光口还是电口。但是这两种介质不能同时生效。一旦用户选定介质类型，接口的连接状态、速率、双工和流控等属性都是指该介质类型的属性，如果用户改变介质类型，新选介质类型的这些属性将使用默认值，用户可以根据需要重新设定这些属性。

######  光电复用端口支持接口介质自动选择

+  如果用户配置接口介质自动选择，在接口只有一种介质连接上时，设备使用当前连接的介质；

+  在接口的两种介质都连接上时，设备将使用用户配置的优先介质。介质自动选择优先介质默认为电口，用户可以通过配置medium-type auto-select prefer fiber来设置优先介质为光口。在自动选择模式下，接口的速率、双工、流控等属性将使用默认值。



#### 1.3.12 接口的速率、双工、流控和自协商因子模式

对于以太网物理接口和AP口，用户可以配置管理接口的速率、双工、流控和自协商因子模式。

##### 工作原理

######   接口的速率

通常情况下，以太网物理接口速率是通过和对端设备自协商决定的。协商得到的速率可以是接口速率能力范围内的任意一个速率。用户也可以通过配置接口能力范围内的任意一个具体速率值让以太网物理接口工作在该指定速率值上。

对于AP口，当用户设置AP口的速率时，实际上是生效到该AP口的所有成员口上(这些成员口都是以太网物理接口)的。

######  接口的双工

以太网物理接口和AP口的双工模式时存在三种情况：

+ 可以将接口设置为全双工属性实现接口在发送数据包的同时可以接收数据包；

+ 可以将接口设置为半双工属性控制接口同一时刻只能发送数据包或接收数据包时；

+ 当设置接口的双工属性为自协商模式时，接口的双工状态由本接口和对端接口自动协商而定。

对于AP口，当用户设置AP口的双工模式时，实际上是生效到该AP口的所有成员口上(这些成员口都是以太网物理接口)的。

######  接口的流控

接口的流控模式分为非对称流控模式和对称流控模式：

+ 对称流控模式，即在一般情况下，接口开启流控模式后，接口上将会处理接收到的流控帧，并在接口出现拥塞时发送流控帧，接收和发送流控帧的处理是一致的，这就是对称流控模式。

+ 非对称流控模式，即在一些情况下，设备希望某个接口能够处理接收到的流控帧保证报文不会因为拥塞而丢弃，又不想发出流控帧而导致整个网络速率下降，这个时候，就要通过配置非对称流控，将接收流控帧和发送流控帧的处理步调分开。

对于AP口，当用户设置AP口的流控模式时，实际上是生效到该AP口的所有成员口上(这些成员口都是以太网物理接口)的。

如 **错误**! **未找到引用源。** 所示，设备的端口A为上联口，端口B-D为下联端口，其中端口B和C对应的是一个慢速网络，假如端口A上开启了接收流控和发送流控功能，由于端口B和C对应的是一个慢速网络，在发送端口B的数据流过大，导致端口B和C拥塞，进而导致端口A上的入口拥塞，端口A上就会发送流控帧，当上联设备响应流控帧时，就会降低往端口A的数据流，间接导致端口D上的网速下降。这个时候，可以配置端口A的发送流控功能关闭，来保障整个网络带宽利用率。

######  接口的自协商因子模式

接口的自协商因子模式有on和off两种。接口的自协商状态和接口的自协商因子模式并不完全等同，接口的自协商状态通常由
接口的速率、双工、流控和自协商因子模式共同决定。

对于AP口，当用户设置AP口的自协商因子模式时，实际上是生效到该AP口的所有成员口上(这些成员口都是以太网物理接
口)的。

一般情况下，只要接口的速率、双工和流控中的一种属性为auto模式，或者接口的自协商模式为on模式，那么接口的自协商工作状态就是on的，即接口的自协商功能是打开的；反之，当接口的速率、双工和流控中的属性全部为非auto模式，并且接口的自协商模式为off模式时，那么接口的自协商工作状态就是off的，即接口的自协商功能是关闭的。
对于百兆光口，接口的自协商功能永远都是关闭的，即百兆光口的自协商工作状态永远都是off的；对于千兆电口，接口的自协商功能永远都是开启的，即千兆电口的自协商工作状态永远都是on的。

#### 1.3.13 模块自动检测

在配置接口速率为自动协商模式的情况下，能够根据插入的模块类型自动调节接口的速率。

##### 工作原理

目前支持的模块有SFP和SFP+两种模块，其中SFP为千兆模块，SFP+为万兆模块，若插入的是SFP模块，则接口工作在千兆模式，若插入的是SFP+模块，则接口工作在万兆模式。

模块的自动检测功能只在速率配置为自动协商时才能生效。

#### 1.3.14 保护口

有些应用环境下，要求交换机上的部分端口间不能互相通讯，可以通过将某些端口设置为保护口(Protected Port)来达到目的。同时还可以通过配置操作来设置保护口之间不能进行路由。

##### 工作原理

######  保护口

当端口设为保护口之后，保护口之间互相无法通讯，保护口与非保护口之间可以正常通讯。

保护口有两种模式，一种是阻断保护口之间的二层交换，但允许保护口之间进行路由，第二种是同时阻断保护口之间的二层交换和阻断路由；在两种模式都支持的情况下，第一种模式将作为缺省配置模式。

当两个保护口设为一个镜像会话端口对时，该镜像会话的源端口发送或接收的帧依然能够镜像到该镜像会话的目的端口上。

目前只支持在以太网物理接口和AP口上设置保护口。当一个AP口被设置为保护口时，该AP所有成员口都被设置为保护口。

######  保护口之间三层路由阻断

缺省情况下，保护口之间的三层路由并没有被阻断，这个时候可以通过设置保护口之间不能进行路由的功能来实现保护口之间的路由阻断功能。

#### 1.3.15 端口违例恢复

某些协议具备设置端口违例（关闭端口）的功能，用以保证网络的安全性和稳定性。比如端口安全协议，当用户配置开启端口安全，并配置端口上最大安全地址数量，当端口下学习到的地址数超过最大安全地址数时，将产生端口违例事件。另外生成树协议、DOT1X协议、REUP协议等也都具备类似的功能，违例的端口会自动关闭该接口，以保证安全性。

##### 工作原理

当端口因发生违例而被关闭之后，可以在全局模式下使用端口违例恢复命令来将所有违例接口从错误状态中恢复过来，重新复位使能该接口。可以选择手动恢复，也可以选择定时自动恢复。

#### 1.3.16 端口节能管理配置

EEE(Energy Efficient Ethernet)，高效能以太网，是一种节省能源的以太网方案。EEE是在以太网网连接闲置时间，使端口进入低功耗节能模式来达到节省能源的目的。

LPI(Low Power Idle)模式，即低功耗节能模式，端口进入该模式后，会大幅减小端口发送的信号，仅发送维持端口链路连接的信号来达到节能的目的。

##### 工作原理

100M及100M以上接口的固有以太网标准规格具备闲置状态 (Active Idle State)，若要维持在连接状态，不受数据传输的限制，则需使用大量的电能。因此，无论链路上有没有数据，耗电量都很大。即使没有数据传输，为了保持连接状态，端口也会一直发送IDLE信号来维持端口链路的连接状态。

EEE通过控制交换机端口，将端口进入LPI(Low Power Idle)模式来达到节省能源的目的。LPI 低功耗模式在链路利用率低的阶段耗电量低。EEE技术也可以使端口从LPI状态快速转换成正常状态，提供高性能数据传输。

端口使能EEE节能功能后，如果在连续一段时间内端口状态始终为up且没有收发任何报文，则端口自动进入节能模式；当端口需要收发报文时，端口又自动恢复工作模式，从而达到节能的效果。EEE功能要生效，达到节能效果，需要对端端口也支持EEE功能。

仅工作在100M和1000M速率模式的电口支持EEE功能。EEE功能仅在端口开启自协商能力时生效。

#### 1.3.17 端口震荡保护

当发生接口震荡时，会产生大量硬件中断，从而消耗大量CPU资源，另一方面频繁的接口震荡容易损害接口，用户可以配置接口震荡保护功能来保护接口。

##### 工作原理

接口链路震荡保护功能由用户自行决定是否开启，默认情况下为开启保护功能。当接口发生震荡时，接口每2s或 10 秒都会检测一次震荡，如果检测到接口2s内震荡 6 次，则打印提示信息，连续打印 10 次提示信息(也就是20s内连续检测到接口震荡)，则关闭接口；对于10s检测一次震荡，如果检测到接口10s发生 10 次震荡，则打印提示信息，不关闭接口.。

#### 1.3.18 接口 Syslog

用户可以通过配置打开或关闭Syslog开关来决定是否查看接口状态发生改变或异常的信息。

##### 工作原理

接口Syslog开关由用户自行决定是否开启，默认情况下为开启。当接口发生异常情况，比如接口状态发生改变，接口收到错误帧或接口发生震荡时，系统将打印提示信息告之用户。

#### 1.3.19 全局的 MTU

用户可以通过设置全局的MTU来控制所有端口允许收发的最大帧长。

**工作原理**

当端口进行大吞吐量数据交换时，可能会遇到大于以太网标准帧长度的帧，这种帧被称为jumbo帧。MTU是指帧中有效数据段的长度，不包括以太网封装的开销。端口收到或者转发的帧，如果长度超过设置的MTU将被丢弃。MTU允许设置的范围为64~9216字节，粒度为 4 字节，缺省一般为 1500 字节。

全局设置的接口链路MTU的变化会引起接口的IP MTU的变化，接口的IP MTU会自动与接口的链路MTU保持一致。

端口下配置的MTU优先级高于全局MTU，当配置全局MTU后，接口MTU无法配置成缺省值。

#### 1.3.20 配置标准 MIB 节点中接口名称的增强显示

##### 工作原理

我司设备对于标准MIB节点中接口名称的显示方式中默认在接口类型和接口号之间含有空格，并且ifName显示的是接口的简称。增强显示功能开启后，标准MIB的ifName节点将会显示接口全称，同时标准MIB所有接口名称相关节点的显示中将不含空格。涉及的标准MIB节点包含但不限于ifDescr，ifName节点。

##### 相关配置

######  启用标准 MIB 节点中接口名称的增强显示

缺省情况下，标准MIB节点中接口名称相关节点的显示中包含空格，ifName显示的是接口的简称在全局模式下使用snmp-server if-name enhance开启标准MIB节点中接口名称的增强显示。启用后，标准MIB节点中接口名称相关节点的显示中不包含空格，ifName显示的是接口的全称。

#### 1.4 配置详解

配置项 配置建议 & 相关命令

<table border="1">
  <tr>
    <th>配置项</th>
    <th colspan=2>配置建议 & 相关命令</th>
  </tr>
  <tr>
    <td rowspan="10">接口配置管理</td>
    <td colspan=2>⚠️ 可选配置。主要用于进行接口的创建、删除、接口描述管理等配置。</td>
  </tr>
  <tr>
    <td>interface</td>
    <td>创建一个接口，并进入指定接口配置模式，或者直接进入该接口的接口配置模式。</td>
  </tr>
  <tr>
    <td>interface range</td>
    <td>输入一定范围的接口，当这些接口未被创建时，向内进行接口创建，并进入接口配置模式。</td>
  </tr>
  <tr>
    <td>define interface-range</td>
    <td>将此接口操作的接口定义成宏定义或定义成正义形定义。</td>
  </tr>
  <tr>
    <td>snmp-server if-index persist</td>
    <td>开启接口索引永久化功能，即设备重启后接口索引不变。</td>
  </tr>
  <tr>
    <td>description</td>
  </tr>
  <tr>
    <td>snmp trap link-status</td>
    <td>在接口配置模式下，使用设备命令关闭接口。</td>
  </tr>
  <tr>
    <td>shutdown</td>
    <td>在接口配置模式下，使用设备命令关闭接口。</td>
  </tr>
  <tr>
    <td>physical-port dither protect</td>
    <td>在全局配置模式下，配置接口震荡保护功能。</td>
  </tr>
  <tr>
    <td>logging [link-updown | error-frame | link-dither]</td>
    <td>在全局配置模式下，配置接口打开打印接口状态信息。</td>
  </tr>
  <tr>
    <td rowspan="17">配置接口属性</td>
    <td colspan=2>⚠️ 可选配置。主要用于进行接口的属性管理配置。</td>
  </tr>
    <tr>
    <td>bandwidth</td>
    <td>在接口配置模式下，使用该命令设置接口的带宽参数。</td>
  </tr>
  <tr>
    <td>carrier-delay</td>
    <td>在接口配置模式下，使用该命令设置链路载波时延。</td>
  </tr>
  <tr>
    <td>load-interval</td>
    <td>在接口配置模式下，使用该命令设置接口的统计周期时间间隔。</td>
  </tr>
  <tr>
    <td>duplex</td>
    <td>设置接口的双工模式。</td>
  </tr>
  <tr>
    <td>flowcontrol</td>
    <td>打开或关闭接口的流控控制。</td>
  </tr>
  <tr>
    <td>medium-type</td>
    <td>选择接口的媒介类型。</td>
  </tr>
  <tr>
    <td>mtu</td>
    <td>设置接口的 MTU。</td>
  </tr>
  <tr>
    <td>negotiation mode</td>
    <td>设置接口的协商模式。</td>
  </tr>
  <tr>
    <td>speed</td>
    <td>设置接口的速率。</td>
  </tr>
  <tr>
    <td>switchport</td>
    <td>在接口配置模式下使用该命令将交换机端口配置为 switchport 命令，将一个接口配置为三层接口时，使用 no switchport 命令将一个接口从三层口配置为三层接口。</td>
  </tr>
  <tr>
    <td>switchport protected</td>
    <td>在接口配置模式下，使用该命令设置接口之间的保护端口。</td>
  </tr>
  <tr>
    <td>protected-ports route-deny</td>
    <td>在接口配置模式下，使用该命令设置接口之间的保护端口。</td>
  </tr>
  <tr>
    <td>errdisable recovery</td>
    <td>在全局配置模式下(敏感开关命令设置(F)下，使用该命令恢复接口。</td>
  </tr>
  <tr>
    <td>eee enable</td>
    <td>在接口配置模式下，配置 Telnet 或者</td>
  </tr>
  <tr>
    <td>mtu forwarding</td>
    <td>设置接口 MTU 和 IP MTU。</td>
  </tr>
  <tr>
    <td>snmp-server if-name enhance</td>
    <td>配置 MIB 书中的接口的增强显示</td>
  </tr>
</table>


#### 1.4.1 接口配置管理

##### **配置效果**

+ 能够创建出指定的单个逻辑口，并进入接口的配置模式，或者对于已经存在的物接口或者逻辑接口，可以进入接口的配置模式。

+ 能够批量创建出指定的逻辑口，并进入接口批量操作的配置模式，或者对于已经存在的物接口或者逻辑接口，可以进入接口批量操作的配置模式。

+ 能够实现相同接口在设备重启前后接口索引保持不变。

+ 设置接口的描述符，对该接口直观、形象化的理解。

+ 能够启用或者关闭接口的LinkTrap功能。

+ 配置接口管理状态，关闭或者打开接口。

+ 能够启用标准MIB节点中接口名称的增强显示功能。

##### **注意事项**

+ 对于逻辑接口，可以使用该命令的no命令形式删除接口或者将指定范围接口的批量删除，但不可以使用该命令的no命令形式删除指定的物理接口或批量删除指定范围的物理接口。

+ 可以使用该命令的default命令形式将指定物理接口或者逻辑接口或者指定范围的接口在接口模式下的相关配置恢复到缺省配置。

##### **配置方法**

######  配置单个指定的接口

+ 可选配置。

+ 可以用于需要创建某个不存在的逻辑接口或者进入已经存在的物理接口和逻辑接口的接口配置模式以进行接口相关的配
  置时，需要配置该命令。
  【命令格式】 interface interface-type interface-number
  【参数说明】 interface-type interface-number：即接口的类型和接口编号，可以是以太网物理接口、AP口、SVI口、Loopback
  口等。
  【缺省配置】 无
  【命令模式】 全局配置模式
  【使用指导】 
  + 对于物理接口或者已经创建的逻辑接口，直接进入该接口的配置模式。
  + 对于逻辑接口，如果该接口未被创建，则首先创建出该接口并进入接口的配置模式。
  + 使用no命令形式删除指定的逻辑接口。
  + 使用default命令形式将该接口的接口模式下配置恢复到缺省配置。

######  配置一定范围的接口

+ 可选配置。

+ 可以用于需要批量创建不存在的逻辑接口或者进入已经存在的物理接口和逻辑接口的接口批量配置模式以进行接口相关的配置时，需要配置该命令。
  【命令格式】 interface range { port-range | macro macro_name }
  【参数说明】 port-range：即批量操作的接口类型和接口编号范围，可以是以太网物理接口、AP口、SVI口、Loopback口等。
  macro_name：即一定范围接口类型的宏定义名。
  【缺省配置】 无
  【命令模式】 全局配置模式
  【使用指导】 
  + 对于物理接口或者已经创建的逻辑接口，直接进入接口的批量配置模式。
  + 对于逻辑接口，如果接口未被创建，则首先创建出接口然后再进入接口的批量配置模式。
  + 使用default命令形式批量将接口模式下配置恢复到缺省配置。
  + 使用宏定义的时候，需要在全局配置模式下，先将一定范围的接口类型通过define interface-range命令进行宏定义成macro_name，然后再通过interface range macro macro_name进行接口的批量配置管理。

######  配置接口的索引永久化

+ 可选配置。

+ 可以用于需要保持接口索引在系统重启前后一致时使用。

【命令格式】 snmp-server if-index persist
【参数说明】 -
【缺省配置】 该功能关闭。
【命令模式】 全局配置模式
【使用指导】 执行该命令后，保存配置时将会把当前所有接口的索引保存起来，重启后接口使用重启前分配的接口索引。可以使用该命令的no命令或者default命令形式关闭该功能。

######  配置接口的描述符

+ 可选配置。

+ 可以用于为接口设置描述信息时使用。

【命令格式】 description string
【参数说明】 string： 最长 80 个字符
【缺省配置】 缺省无接口描述符
【命令模式】 接口配置模式
【使用指导】 该命令配置接口的描述符。可以使用该命令的no命令或者default命令形式取消配置接口的描述符。-

######  配置接口的 LinkTrap

+ 可选配置。

+ 可以用于通过SNMP获取接口状态变化的Trap信息。

【命令格式】 snmp trap link-status
【参数说明】 -^
【缺省配置】 缺省情况下，该功能打开
【命令模式】 接口配置模式
【使用指导】 该命令配置是否发送该接口的LinkTrap，当功能打开时，如果接口的Link状态变化，SNMP将发出LinkTrap，反之则不发。可以使用该命令的no命令或者default命令形式关闭该功能。

######  配置接口的管理状态

+ 可选配置。

+ 用于关闭或者打开接口。

+ 接口关闭后将无法收发报文。

【命令格式】 shutdown
【参数说明】 -
【缺省配置】 接口的管理状态是UP

【命令模式】 接口配置模式
【使用指导】 对接口执行shutdown操作时，即关闭该接口，执行no shutdown操作将重新打开该接口。注意有些情况下，不允许将端口执行no shutdown操作，比如该端口处于端口违例状态，那么该端口将无法执行no shutdown操作。可以使用该命令的no命令或者default命令形式重新打开该接口。

######  配置接口震荡保护功能

+ 可选配置。
+ 用于保护发生震荡的接口。

【命令格式】 physical-port dither protect
【参数说明】
【缺省配置】 默认开启接口震荡保护功能
【命令模式】 全局配置模式
【使用指导】

######  配置打印接口 Syslog 信息功能

+ 可选配置。

+ 用于开启或关闭打印接口状态信息功能。

【命令格式】 [no] logging [link-updown | error-frame | link-dither ]
【参数说明】 link-updown ： 打印接口状态发生改变时的信息，error-frame ： 打印接口收到错误帧时的信息，link-dither ： 打印接口发生震荡时的信息
【缺省配置】 开启打印接口Syslog信息
【命令模式】 全局配置模式
【使用指导】

######  配置标准 MIB 节点中接口名称的增强显示功能

+ 可选配置。

+ 用于开启或关闭标准MIB节点中接口名称的增强显示功能。

【命令格式】 [no | default] snmp-server if-name enhance
【参数说明】 -
【缺省配置】 关闭标准MIB节点中接口名称的增强显示功能
【命令模式】 全局配置模式
【使用指导】

##### **检验方法**

######  配置单个指定的接口

+ 执行interface操作，如果能够正常进入接口模式，即说明配置是成功的。

+ 对于逻辑接口，如果是执行no interface操作，也可以通过show running命令或者show interfaces命令查看对应的接口是否存在，如果不存在，则该逻辑接口是被正常删除的。

+ 执行default interface操作，通过show running命令查看对应的接口下的配置是否都恢复到了缺省配置，如果是，则说明该操作是成功的。

######  配置一定范围的接口

+ 执行interface range操作，如果能够正常进入接口批量配置模式，即说明配置是成功的。

+ 执行default interface range操作，通过show running命令查看对应的接口下的配置是否都恢复到了缺省配置，如果是，则说明该操作是成功的。

######  配置接口索引永久化

+ 配置完该命令后，执行write保存配置操作，重启设备后，通过show interface命令查看接口的接口索引值，如果对于同一个接口的索引值在设备重启后保持一致，那么说明接口的索引永久化功能是正常的。

######  配置接口的 LinkTrap

+ 选择一个物理端口，进行网线插拔，同时打开SNMP服务器，如果在网线插拔的时候，SNMP服务器能够正常收到该接口的Link状态变化的Trap信息，则说明该功能是正常的。

+ 执行no命令形式操作，如果验证到在一个物理端口，进行网线插拔，同时打开SNMP服务器，如果在网线插拔的时候，
  SNMP服务器无法收到该接口的Link状态变化的Trap信息，则说明已经正常关闭了接口的LinkTrap功能。

######  配置接口的管理状态

+ 选择一个物理端口，插上网线，让端口Up起来，对该端口执行shutdown关闭接口的操作，用户在控制台上能够看到端口状态变成管理Down的Syslog信息，同时该端口上的指示灯灭掉，则关闭端口的功能是正常的，并且通过show interfaces命令可以看到接口状态显示为administratively down。在此基础上，执行no shutdown重新打开该接口，用户在控制台上能够看到端口Up的Syslog信息，同时该端口上的指示灯重新亮起来，则打开端口的功能是正常的。

######  配置接口震荡保护功能

+ 在全局配置模式下配置命令，如physical-port dither protect。选择一个物理端口，频繁插拔网线模拟端口发生震荡的情
  况，在控制台上可以看到系统打印端口发生震荡的信息，经过连续打印若干次之后，系统会提示端口不稳定将shutdown
  接口。

######  配置打印接口 Syslog 信息功能

+ 在全局配置模式下配置命令，如logging link-updown查看接口状态信息。选择一个物理端口，插拔网线，接口将发生两次状态改变，用户可以在控制台上看到接口link状态从up变为down的信息，又从down变为up的信息；配置 no logging link-updown后，再次插拔网线，控制台上看不到信息，说明该功能是正常的。

######  配置标准 MIB 节点中接口名称的增强显示功能

+ 在全局配置模式下配置命令snmp-server if-name enhance后，通过snmp工具去读取标准MIB中接口名称的节点，比如ifDescr，ifName节点，读取出来的结果不包含空格(例：GigabitEthernet0/1)；配置命令no snmp-server if-name enhance后，再次读取ifDescr节点，读取出来的结果包含空格(例：GigabitEthernet 0/1)，同时读取ifName节点的结果是接口简称，说明该功能正常。

##### 配置举例

######  配置接口基本属性

【配置方法】 + 将 2 台设备通过交换端口进行连接。

+ 分别给 2 台设备配置一个SVI口，并配置相同网段的IP地址。
+ 在 2 台设备上分别配置接口索引永久化。
+ 在 2 台设备上分别启用LinkTrap功能。
+ 在两台设备上配置接口管理状态。

```
A
A# configure terminal
A(config)# snmp-server if-index persist
A(config)# interface vlan 1
A(config-if-VLAN 1)# ip address 192.168.1. 1 255.255.255.0
A(config-if-VLAN 1)# exit
A(config)# interface gigabitethernet 0/1
A(config-if-GigabitEthernet 0/1)# snmp trap link-status
A(config-if-GigabitEthernet 0/1)# shutdown
A(config-if-GigabitEthernet 0/1)# end
A# write
```

```
B 
B# configure terminal
B(config)# snmp-server if-index persist
B(config)# interface vlan 1
B(config-if-VLAN 1)# ip address 192.168.1. 2 255.255.255.0
B(config-if-VLAN 1)# exit
B(config)# interface gigabitethernet 0/1
B(config-if-GigabitEthernet 0/1)# snmp trap link-status
B(config-if-GigabitEthernet 0/1)# shutdown
B(config-if-GigabitEthernet 0/1)# end
B# write
```

【检验方法】 在A、B设备上分别进行如下检验：

+ 检查设备上的GigabitEthern 0/1和SVI 1在接口GigabitEthern 0/1 在shutdown操作后的接口状态是否正确
+ 检查接口GigabitEthern 0/1 shutdown操作后，是否有发出该接口Link Down的Trap信息
+ 重启设备后，接口GigabitEthern 0/1的接口索引值是否和重启前的一致

【检验方法】 在A、B设备上分别进行如下检验：

#### 1.4.2 配置接口属性

##### 配置效果

+ 将设备通过交换端口或者路由端口进行连接和数据通信。
+ 在设备上分别调整各种接口属性。

##### 配置方法

######  配置路由端口

+ 可选配置。

+ 可以用于需要将接口转换为三层路由口时使用。

+ 配置成三层路由口后将使该接口上运行的二层协议失效。

+ 支持二层交换口上配置。

【命令格式】 no switchport
【参数说明】 -
【缺省配置】 交换机上的以太网物理端口缺省为二层交换
【命令模式】 接口配置模式
【使用指导】 在三层交换机设备上，使用该命令可以将一个二层交换口配置成三层路由口。使用switchport命令可以将一个三层路由口转换成二层交换口。

######  配置三层 AP 口

+ 可选配置。

+ 可以在接口配置模式下，执行no switchport命令将一个二层AP口配置成三层AP口。使用switchport命令时，可以
  将一个三层AP口配置成二层AP口。

+ 配置成三层路由口后将使该接口上运行的二层协议失效。

+ 支持二层聚合口上配置。

【命令格式】 no switchport
【参数说明】 -^
【缺省配置】 缺省情况下，交换机上的AP端口缺省为二层AP口
【命令模式】 接口配置模式
【使用指导】 在三层交换机设备上，进入二层AP口的接口模式后，使用该命令可以将一个二层AP口配置成三层AP口。进入三层AP口的接口模式后，使用switchport命令可以将一个三层AP口转换成二层AP口。

######  配置接口介质类型

+ 可选配置。
+ 对于光电复用口，接口的缺省介质为电口。
+ 配置的端口介质类型变化时，可能会引起端口状态震荡。
+ 支持以太网物理端口上及聚合口上配置。

【命令格式】 medium-type { auto-select [ prefer [ fiber | copper ] ] | fiber | copper }
【参数说明】 auto-select：自动选择介质类型
prefer [ fiber | copper ]：自动选择的时候优先选择某种介质类型
fiber：强制选择光口
copper：强制选择电口
【缺省配置】 缺省情况下，端口上选择的介质类型为电口
【命令模式】 接口配置模式

【使用指导】 如果同一端口可以选择光口和电口两种介质类型，用户只能使用其中之一。一旦确定介质类型之后，在配置端口的属性，例如状态、双工、流量控制和速率等，都是指端口当前选择类型的属性。改变端口类型后，新类型对应的端口的属性为其默认属性，用户可以根据需要重新配置。

如果用户配置端口介质自动选择，在端口只有一种介质连接上时，设备使用当前连接的介质；在端口的两种介质都连接上时，设备将使用用户配置的优先介质。介质自动选择优先介质默认为电口，用户可以通过配置medium-type auto-select prefer fiber来设置优先介质为光口。在自动选择模式下，端口的速率、双工、流控等属性将使用默认值。

######  配置接口速率

+ 可选配置。

+ 配置的端口速率模式变化时，可能会引起端口震荡。

+ 支持以太网物理端口上及聚合口上配置。

【命令格式】 speed [ 10 | 100 | 1000 | auto ]
【参数说明】 10 ：表示接口的速率为10Mbps。
100 ：表示接口的速率为100Mbps。
1000 ：表示接口的速率为1000Mbps。
auto：表示接口的速率为自适应的。
【缺省配置】 缺省情况下，接口的速率是自协商模式，即接口的速率配置缺省为auto模式
【命令模式】 接口模式
【使用指导】 如果接口是聚合端口的成员，则该接口的速率由聚合端口的速率决定。接口退出聚合端口时使用自己的速率设置。使用show interfaces命令查看设置。接口类型不同，允许设置的速率类型也会有所不同，如SFP类型的接口就不允许把速率设为10M。

######  配置接口双工模式

+ 可选配置。

+ 配置的端口双工模式变化时，可能会引起端口震荡。

+ 支持以太网物理端口上及聚合口上配置。

【命令格式】 duplex { auto | full | half }
【参数说明】 auto：表示全双工和半双工自适应。
full：表示全双工。
half：表示半双工。
【缺省配置】 缺省情况下，接口的双工是自协商模式，即接口的双工配置缺省为auto模式
【命令模式】 接口模式
【使用指导】 接口的双工属性与接口的类型有关。可以使用show interfaces命令查看接口双工的设置。

######  配置接口流控模式

+ 可选配置。

+ 一般情况下，接口的流控模式缺省为off模式。部分产品的缺省模式为on模式。

+ 接口开启流控模式后，在接口上出现拥塞时，将接收或者发送流控帧调整网络数据流量。

+ 配置的端口流控模式变化时，可能会引起端口震荡。

+ 支持以太网物理端口上及聚合口上配置。

【命令格式】 flowcontrol {^ auto^ | off | on^ }^
【参数说明】 auto：自协商流量控制。
off：关闭流量控制。
on：打开流量控制。
【缺省配置】 缺省情况下，接口的流控一般是off模式，即接口的流控功能缺省是关闭的
【命令模式】 接口配置模式
【使用指导】 -

######  配置接口自协商因子模式

+ 可选配置。

+ 配置的端口自协商因子变化时，可能会引起端口震荡。

+ 支持以太网物理端口上及聚合口上配置。

【命令格式】 negotiation mode { on | off }
【参数说明】 on：自协商因子模式为on模式。
off：自协商因子模式为off模式。
【缺省配置】 缺省情况下，接口的自协商因子是off模式
【命令模式】 接口配置模式
【使用指导】 -^

######  配置接口 MTU

+ 可选配置。

+ 可以通过设置端口的MTU来控制端口允许收发的最大帧长。

+ 支持以太网物理端口及SVI口设置。

【命令格式】 mtu num
【参数说明】 num： 64 － 9216
【缺省配置】 缺省情况下，接口的MTU值一般为 1500 字节
【命令模式】 接口模式
【使用指导】 设置接口所支持的MTU，即链路层数据部分的最大长度。目前只支持设置物理端口和包含成员口的AP口的
MTU。

######  配置全局 MTU

+ 可选配置。

+ 可以通过设置全局MTU和IP MTU来控制所有端口允许收发的最大帧长。

+ 端口范围以太网物理端口。

【命令格式】 mtu forwarding num
【参数说明】 num： 64 － 9216

【缺省配置】 缺省情况下，接口的MTU值一般为 1500 字节
【命令模式】 全局模式
【使用指导】 全局设置的接口链路MTU的变化会引起接口的IP MTU的变化，接口的IP MTU会自动与接口的链路MTU
保持一致。

######  配置接口带宽

+ 可选配置。

+ 一般情况下，接口的带宽值和接口支持的速率值相同。

【命令格式】 bandwidth kilobits
【参数说明】 kilobits：以以每秒K比特为单位，范围为 1 到 2147483647 。
【缺省配置】 缺省情况下，接口带宽值一般和接口类型相匹配，比如对于千兆以太网物理端口，该接口的缺省带宽值为
1000000 ，万兆以太网物理端口则为 10000000
【命令模式】 接口配置模式
【使用指导】 -

######  配置接口载波时延

+ 可选配置。

+ 配置的载波时延时间较长时，接口物理状态变化时会较晚引起协议状态的变化，若配置为 0 秒时，接口物理状态变化则
  立刻引起协议状态变化。
  【命令格式】 carrier-delay {[milliseconds] num | up [milliseconds] num down [milliseconds] num}
  【参数说明】 num：默认以秒为单位，范围 0 ～ 60 秒。
  milliseconds ：配置以毫秒为单位的载波延迟，范围0~60000毫秒。
  Up ：设置载波检测信号DCD从Down状态到Up状态的时间延时。
  Down ：设置载波检测信号DCD从Up状态到Down状态的时间延时。
  【缺省配置】 缺省情况下，接口的Carry-delay值为 2 秒
  【命令模式】 接口配置模式
  【使用指导】 - 以毫秒为单位设置载波延迟必须是 100 毫秒的整数倍

######  配置接口 Load-interval

+ 可选配置。

+ 配置的报文采样时间影响接口报文平均速率的计算，配置的时间较短时，报文平均速率能较快反映报文实时流量的变化。

【命令格式】 load-interval seconds
【参数说明】 seconds：以秒为单位，范围 5 - 600 秒。
【缺省配置】 缺省情况下，接口的load-interval值为 10 秒
【命令模式】 接口配置模式
【使用指导】 -

######  设置保护口


配置指南 接口

+ 可选配置。

+ 配置为保护口的端口之间无法进行二层报文转发。

+ 支持以太网物理端口上及聚合口上配置。

【命令格式】 switchport protected
【参数说明】 -
【缺省配置】 缺省情况下，接口不是一个保护口
【命令模式】 接口配置模式
【使用指导】 -

######  保护口之间三层路由阻断

+ 可选配置。

+ 配置了该命令后，配置了保护口命令的端口之间无法进行三层路由转发。

【命令格式】 protected-ports^ route-deny^
【参数说明】 -
【缺省配置】 缺省情况下，该功能关闭
【命令模式】 全局配置模式
【使用指导】 缺省情况下，保护口之间的三层路由并没有被阻断，这个时候可以通过设置保护口之间不能进行路由的功能来实现保护口之间的路由阻断功能。

######  端口违例恢复

+ 可选配置。

+ 端口违例发生后，端口被关闭，缺省情况下不会恢复。配置了端口违例恢复后，违例的端口会被恢复，端口会被打开。

【命令格式】 errdisable recovery [interval time]
【参数说明】 time：自动恢复定时时间，取值范围为 30 - 86400 ，单位是秒。
【缺省配置】 缺省情况下，没有该功能
【命令模式】 全局配置模式和特权模式(恢复违例的命令操作)下
【使用指导】 缺省情况下，端口违例不会恢复，这个时候可以使用此命令手动恢复或者配置自动恢复。

######  配置端口节能

+ 可选配置。

+ 配置该命令后，开启端口节能模式。

【命令格式】 eee enable
【参数说明】
【命令模式】 接口配置模式
【使用指导】 缺省情况下，端口节能模式为关闭状态，使用此命令使能端口节能模式，使用该命令的no命令或者default命令形式取消配置接口EEE功能。

##### 检验方法

+ 可以通过show interfaces命令查看接口的属性配置是否正常。

【命令格式】 show interfaces [ interface-type interface-number ] [ description | switchport | trunk]
【参数说明】 interface-type interface-number：接口类型和接口编号
description：接口的描述符信息，包括link状态
switchport：二层接口信息，只对二层接口有效
trunk：Trunk端口信息，对物理端口和聚合端口有效
【命令模式】 特权模式
【使用指导】 如果不加参数，则显示接口的基本信息
【命令展示】 

```
SwitchA#show interfaces GigabitEthernet 0/1^
Index(dec):1 (hex):1
GigabitEthernet 0/1 is DOWN , line protocol is DOWN
Hardware is Broadcom 5464 GigabitEthernet, address is 00d0.f865.de9b (bia 00d0.f865.de9b)
Interface address is: no ip address
Interface IPv6 address is:
No IPv6 address
MTU 1500 bytes, BW 1000000 Kbit
Encapsulation protocol is Ethernet-II, loopback not set
Keepalive interval is 10 sec , set
Carrier delay is 2 sec
Ethernet attributes:
Last link state change time: 2012- 12 - 22 14:00:48
Time duration since last link state change: 3 days, 2 hours, 50 minutes, 50 seconds
Priority is 0
Medium-type is Copper
Admin duplex mode is AUTO, oper duplex is Unknown
Admin speed is AUTO, oper speed is Unknown
Flow receive control admin status is OFF,flow send control admin status is OFF
Flow receive control oper status is Unknown,flow send control oper status is Unknown
Storm Control: Broadcast is OFF, Multicast is OFF, Unicast is OFF
Bridge attributes:
Port-type: trunk
Native vlan:1
Allowed vlan lists:1- 4094 //Trunk口的许可VLAN列表
Active vlan lists:1, 3- 4 //实际生效的vlan（即该设备上仅创建了VLAN1、 3 和 4 ）
Rxload is 1/255,Txload is 1/255
5 minutes input rate 0 bits/sec, 0 packets/sec
5 minutes output rate 0 bits/sec, 0 packets/sec
0 packets input, 0 bytes, 0 no buffer, 0 dropped
Received 0 broadcasts, 0 runts, 0 giants
0 input errors, 0 CRC, 0 frame, 0 overrun, 0 abort
0 packets output, 0 bytes, 0 underruns , 0 dropped
0 output errors 0 collisions, 0 interface resets
```

+ 可以通过show eee interfaces status命令查看接口EEE状态。

【命令格式】 show eee interfaces { interface-type interface-number | status}
【参数说明】 interface-type interface-number：接口类型和接口编号
status：所有接口EEE状态
【命令模式】 特权模式
【使用指导】 指定接口时不加参数status，显示单个接口的EEE信息，否则显示所有接口的EEE信息。
【命令展示】 1 ：显示接口GigabitEthernet 0/1的EEE状态信息。

```
Ruijie#show eee interface gigabitEthernet 0/1
Interface : Gi0/1
EEE Support : Yes
Admin Status : Enable
Oper Status : Disable
Remote Status : Disable
Trouble Cause : Remote Disable
```

2 ：显示所有接口EEE状态信息。

```
Ruijie#show eee interface status
Interface EEE Admin Oper Remote Trouble
Support Status Status Status Cause

--------- ------- -------- -------- -------- --------------------

Gi0/1 Yes Enable Disable Disable Remote Disable
Gi0/2 Yes Enable Disable Unknown None
Gi0/3 Yes Enable Enable Enable None
Gi0/4 Yes Enable Enable Enable None
Gi0/5 Yes Enable Enable Enable None
Gi0/6 Yes Enable Enable Enable None
Gi0/7 Yes Enable Enable Enable None
Gi0/8 Yes Enable Enable Enable None
Gi0/9 Yes Enable Enable Enable None
Gi0/10 Yes Enable Enable Enable None
```

### 1.5 监视与维护

##### 清除各类信息

<table border="1">   
    <tr>     
        <th>作用</th>     
        <th>命令</th>   
    </tr>   
    <tr>     
        <td>清除接口的统计值。</td>     
        <td>Clear counters [ interface-type interface-number ]</td>   
    </tr>
    	<td>接口硬件复位。</td>     
    	<td>Clear interface [ interface-type interface-number ]</td>   
    </tr> 
</table>


##### 查看运行情况

######  显示接口配置和状态

<table>
  <thead>
    <tr>
      <th>作用</th>
      <th>命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>显示指定接口的全部状态和配置信息。</td>
      <td>Show interfaces [interface-type interface-number]</td>
    </tr>
    <tr>
      <td>显示接口的状态。</td>
      <td>Show interfaces [interface-type interface-number] status</td>
    </tr>
    <tr>
      <td>显示接口禁止的状态。</td>
      <td>Show interfaces [interface-type interface-number] status err-disable</td>
    </tr>
    <tr>
      <td>查看端口链路状态变化的时间和次数。</td>
      <td>Show interfaces [interface-type interface-number] link-state-change statistics</td>
    </tr>
    <tr>
      <td>显示可交换接口（非路由接口）的 administrative 和 operational 状态信息。</td>
      <td>Show interfaces [interface-type interface-number] switchport</td>
    </tr>
    <tr>
      <td>显示指定接口的描述配置和接口状态。</td>
      <td>Show interfaces [interface-type interface-number] description [up | down]</td>
    </tr>
    <tr>
      <td>显示各端口的统计值信息。其中速率显示可能在 0.5% 的误差。</td>
      <td>Show interfaces [interface-type interface-number] counters [up | down]</td>
    </tr>
    <tr>
      <td>显示上一采样时间间隔内增加的报文统计值。</td>
      <td>Show interfaces [interface-type interface-number] counters increment</td>
    </tr>
    <tr>
      <td>显示错误报文统计值。</td>
      <td>Show interfaces [interface-type interface-number] counters errors [up | down]</td>
    </tr>
    <tr>
      <td>显示报文收发率</td>
      <td>Show interfaces [interface-type interface-number] counters rate [up | down]</td>
    </tr>
    <tr>
      <td>显示接口摘要统计值</td>
      <td>Show interfaces [interface-type interface-number] counters summary [up | down]</td>
    </tr>
    <tr>
      <td>线缆检测状态显示。在线缆处于短路或断路等异常状态时，线缆检测有助于正确判断线缆的工作状况。</td>
      <td>Show interfaces [interface-type interface-number] line-detect</td>
    </tr>
    <tr>
      <td>显示接口丢包报文统计值。</td>
      <td>Show interfaces [interface-type interface-number] counters drops [up | down]</td>
    </tr>
    <tr>
      <td>显示接口实时收发率</td>
      <td>Show interfaces [interface-type interface-number] usage [up | down]</td>
    </tr>
    <tr>
      <td>显示接口 EEE 状态。</td>
      <td>Show interfaces [interface-type interface-number] status</td>
    </tr>
    <tr>
      <td>显示全局 MTU 信息</td>
      <td>Show interfaces [interface-type interface-number] mtu forwarding</td>
    </tr>
  </tbody>
</table>


######  显示光模块信息

<table>
  <thead>
    <tr>
      <th>作用</th>
      <th>命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>显示指定接口的光模块基本信息。</td>
      <td>show interfaces [interface-type interface-number] transceiver</td>
    </tr>
    <tr>
      <td>显示指定接口的光模块当前故障告警信息，当没有故障时显示 “None”。</td>
      <td>show interfaces [interface-type interface-number] transceiver alarm</td>
    </tr>
    <tr>
      <td>显示指定接口的光模块诊断参数的当前测量值。</td>
      <td>show interfaces [interface-type interface-number] transceiver diagnosis</td>
    </tr>
  </tbody>
</table>


##### 线缆检测

管理员可以通过线缆检测命令来检测线缆的工作状况。在线缆处于短路或断路等异常状态时，线缆检测有助于正确判断线缆的工作状况。

只有电介质的物理口才支持线缆检测，光介质物理口、聚合端口不支持线缆检测。

在正常连接的接口执行线缆检测，会导致连接暂时断掉，然后再重新建立连接。

<table>
  <thead>
    <tr>
      <th>作用</th>
      <th>命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>在接口模式下执行线缆检测。在线缆处于短路或断路等异常状态时，线缆检测有助于正确判断线缆的工作状况。</td>
      <td>line-detect</td>
    </tr>
  </tbody>
</table>




## 2 MAC 地址

### 2.1 概述

MAC地址表记录了与该设备相连的设备的MAC地址、接口号以及所属的VLAN ID。

设备在转发报文时通过报文的目的MAC地址以及报文所属的VLAN ID的信息在MAC地址表中查找相应的转发输出端口。根据mac地址查找到转发出口后就可以采取单播、组播或广播的方式转发报文。

本文只涉及动态地址、静态地址与过滤地址的管理，组播地址的管理不在本文内描述，请参看《IGMP Snooping配置指南》。

##### 协议规范

+ IEEE 802.3：Carrier sense multiple access with collision detection (CSMA/CD) access method and physical layer specifications

+ IEEE 802.1Q：Virtual Bridged Local Area Networks

### 2.2 典型应用

<table>
  <thead>
    <tr>
      <th>典型应用</th>
      <th>场景描述</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>动态地址学习</td>
      <td>通过动态地址学习，实现报文单播转发</td>
    </tr>
    <tr>
      <td>MAC 地址变化通知</td>
      <td>通过 MAC 地址添加删除通知，监控网络设备下用户变化。</td>
    </tr>
  </tbody>
</table>


#### 2.2.1 动态地址学习

##### 应用场景

通常情况下MAC地址表的维护都是通过动态地址学习的方式进行，其工作原理如下：

设备的MAC地址表为空的情况下，UserA要与UserB进行通讯，UserA首先发送报文到交换机的端口GigabitEthernet 0/2，此时设备将UserA的MAC地址学习到MAC地址表中。由于地址表中没有UserB的源MAC地址，因此设备以广播的方式将报文发送到除了UserA以外的所有端口，包括User B与User C的端口，此时UserC能够收到UserA所发出的不属于它的报文。

UserB收到报文后将回应报文通过设备的端口GigabitEthernet 0/3发送UserA，此时设备的MAC地址表中已存在UserA的MAC地址，所以报文被以单播的方式转发到GigabitEthernet 0/2端口，同时设备将学习UserB的MAC地址，与步骤 1 中所不同的是UserC此时接收不到UserB发送给UserA的报文。

通过UserA与UserB的一次交互过程后，设备学习到了UserA与UserB的源MAC地址，之后UserA与UserB之间的报文交互则采用单播的方式进行转发，此后UserC将不再接收到UserA与UserB之间的交互报文。

##### 功能部属

+ 二层交换设备通过动态地址学习，实现报文单播转发，减少广播报文，减轻网络不必要的负荷。

#### 2.2.2 MAC 地址变化通知

设备的MAC地址通知功能通过与网络管理工作站（NMS）的协作为网络管理提供了监控网络设备下用户变化的机制。

##### 应用场景

打开MAC地址通知的功能后，当设备学习到一个新的MAC地址或老化掉一个已学习到的MAC地址时，一个反映MAC地址变化的通知信息就会产生，并以SNMP Trap的方式将通知信息发送给指定的NMS(网络管理工作站)。

当一个MAC地址增加的通知产生，就可以知道一个由此MAC地址标识的新用户开始使用网络，当一个MAC地址删除的通知产生，则表示一个用户在地址老化时间内没有新的报文发送，通常可以认为此用户已经停止使用网络了。

当使用设备下接的用户较多时，可能会出现在短时间内会有大量的MAC地址变化产生，导致网络流量增加。为了减轻网络负担，可以设置发送MAC地址通知的时间间隔。在达到配置的时间间隔之后，系统将这个时间内的所有通知信息进行打包封装，此时在每条地址通知信息中，包含了若干个MAC地址变化的信息，从而可以会有效地减少网络流量。

当MAC地址通知产生时，通知信息同时会记录到MAC地址通知历史记录表中。此时即便没有配置接收Trap的NMS，管理员也可以通过查看MAC地址通知历史记录表来了解最近MAC地址变化的消息。

MAC地址通知仅对动态地址有效，对于配置的静态地址与过滤地址的变化将不会产生通知信息。

##### 功能部属

+ 二层交换设备开启MAC地址变化通知，实现监控网络设备下的用户变化。

### 2.3 功能详解

##### 基本概念

######  动态地址

通过设备的自动地址学习过程产生的MAC地址表项被称为动态地址。

######  地址老化

设备的MAC地址表是有容量限制的，设备采用地址表老化机制进行不活跃的地址表项淘汰。

设备在学习到一个新的地址的同时启动该地址的老化记时，在达到老化记时前，如果设备没有再一次收到以该地址为源MAC地址的报文，那该地址在达到老化时间后会从MAC地址表中删除。

######  单播转发

设备能够在MAC地址表中查到与报文的目的MAC地址和VLAN ID相对应的表项并且表项中的输出端口是唯一的，报文直接从表项对应的端口输出。

######  广播转发

设备收到目的地址为ffff.ffff.ffff的报文或者在MAC地址表中查找不到对应的表项时，报文被送到所属的VLAN中除报文输入端
口外的其他所有端口输出。

##### 功能特性

<table>
  <thead>
    <tr>
      <th>功能特性</th>
      <th>作用</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>VLAN 的动态地址个数限制</td>
      <td>用户可规划各个 VLAN 内可学习的动态地址数</td>
    </tr>
    <tr>
      <td>接口的动态地址个数限制</td>
      <td>用户可规划各个接口下可学习的动态地址数</td>
    </tr>
  </tbody>
</table>


#### 2.3.1 VLAN 的动态地址个数限制

##### 工作原理

设备的MAC地址表的容量是有限制的并且所有的VLAN共享整个MAC地址表容量，为避免一个VLAN内大量动态地址将整个MAC地址表所占用而使其他VLAN无法学习动态地址，导致其他VLAN的报文都采用广播方式转发，锐捷设备提供了VLAN的动态地址个数限制功能，用户可以规划各个VLAN内可学习的动态地址数，为每个VLAN配置可动态学习的地址的个数上限。

配置了VLAN的动态地址个数限制功能的VLAN只能够学到用户所指定个数的MAC地址，对超出用户配置上限部份的地址将不再学习，报文继续被转发。

用户可以配置VLAN超过地址限数丢弃功能，配置上该功能时，当超过限制数量的地址不再学习，同时报文被丢弃不再转发。

如果配置VLAN的动态地址学习个数限制的上限小于当前VLAN中已学习到的动态地址数，此时设备不再学习该VLAN中的地址，直到VLAN内的地址数通过地址老化删除到小于上限后，设备才会重新学习。

MAC地址复制功能，复制到指定VLAN的MAC地址表项，不受该VLAN下动态MAC地址学习个数的限制。

#### 2.3.2 接口的动态地址个数限制

**工作原理**

配置了接口的动态地址个数限制功能的接口只能够学到用户所指定个数的MAC地址，对超出用户配置上限部份的地址将不再学习，报文继续被转发。

用户可以配置VLAN超过地址限数丢弃功能，配置上该功能时，当超过限制数量的地址不再学习，同时报文被丢弃不再转发。

如果配置接口的动态地址学习个数限制的上限小于当前接口下已学习到的动态地址数，此时设备不再学习该接口下的地址，直到接口下的地址数通过地址老化删除到小于上限后，设备才会重新学习。

### 2.4 产品说明

S6000E设备，对于源MAC为全^0 ，目的MAC为全^0 的报文，不学习源MAC，但泛洪转发。

S6000E设备，配置一条过滤地址，需占用 2 条地址容量。如全局过滤MAC地址数目为4K，实际整机可用地址容量减少8K。

### 2.5 配置详解

<table>
  <thead>
    <tr>
      <th>配置项</th>
      <th colspan="2">配置建议 & 相关命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">配置地址学习能力和老化时间。</td>
      <td colspan="2">可选配置。用于实现动态地址学习。</td>
    </tr>
    <tr>
      <td>mac-address-learning</td>
      <td>配置全局或接口 MAC 地址学习能力</td>
    </tr>
    <tr>
      <td>mac-address-table aging-time</td>
      <td>配置动态地址老化时间</td>
    </tr>
    <tr>
      <td rowspan="2">配置静态地址</td>
      <td colspan="2">可选配置。用于绑定设备下接的网络设备的 MAC 地址与端口关系。</td>
    </tr>
    <tr>
      <td>mac-address-table static</td>
      <td>配置静态地址</td>
    </tr>
    <tr>
      <td>配置过滤地址</td>
      <td colspan="2">可选配置。用于过滤报文。</td>
    </tr>
    <tr>
      <td>mac-address-table filtering</td>
      <td colspan="2">配置全局 MAC 地址变化通知功能</td>
    </tr>
    <tr>
      <td rowspan="3">配置 MAC 地址变化通知</td>
      <td colspan="2">可选配置。用于监控网络设备下的用户变化。</td>
    </tr>
    <tr>
      <td>mac-address-table notification</td>
      <td>配置全局 MAC 地址变化通知功能</td>
    </tr>
    <tr>
      <td>snmp trap mac-notification</td>
      <td>配置接口 MAC 地址变化通知功能</td>
    </tr>
    <tr>
      <td rowspan="2">配置 M2数量达到阈值进行 syslog 告警</td>
      <td colspan="2">可选配置。用于配置 MAC 地址数量达到一定阈值进行 syslog 告警。</td>
    </tr>
    <tr>
      <td>mac-address-table warning-threshold</td>
      <td>配置 MAC 地址数量达到阈值后的 syslog 告警的间隔</td>
    </tr>
    <tr>
      <td rowspan="2">配置 MAC 地址漂移打印 Syslog 告警功能</td>
      <td colspan="2">可选配置。用于配置 MAC 地址漂移检测到后，打印 Syslog 的功能。</td>
    </tr>
    <tr>
      <td>mac-address-table flapping-logging</td>
      <td>开启 MAC 地址漂移打印 Syslog 告警功能</td>
    </tr>
    <tr>
      <td rowspan="2">配置地址学习限数</td>
      <td colspan="2">可选配置。用于配置 MAC 地址最大学习个数。</td>
    </tr>
    <tr>
      <td>max-dynamic-mac-count count</td>
      <td>配置 VLAN/端口下的最大地址学习个数</td>
    </tr>
  </tbody>
</table>


#### 2.5.1 配置动态地址

##### 配置效果

实现动态地址学习，报文正常单播转发。

##### 配置方法

######  配置全局 MAC 地址学习能力

+ 可选配置。

+ 如果需要关闭全局MAC地址学习能力，则应该执行此配置项。

+ 交换机设备上配置。

【命令格式】 mac-address-learning { enable | disable }
【参数说明】 enable：开启全局MAC地址学习能力
disable：关闭全局MAC地址学习能力
【缺省配置】 全局地址学习能力开启
【命令模式】 全局模式
【使用指导】 -

全局MAC地址学习能力缺省开启。当全局MAC地址学习能力关闭时，全局无法进行MAC地址学习；当全局MAC地址学习能力开启时，按端口的MAC地址学习能力生效。^

######  配置接口 MAC **地址学习能力**

+ 可选配置。

+ 如果需要关闭接口MAC地址学习能力，则应该执行此配置项。

+ 交换机设备上配置。

【命令格式】 mac-address-learning
【参数说明】 -
【缺省配置】 地址学习能力开启
【命令模式】 接口模式
【使用指导】 接口必须是二层接口，包括交换口、AP口。

MAC地址学习能力缺省开启，如果端口上配置了DOT1X，IP SOURCE GUARD 绑定，端口安全功能，端口的学习能力不能开启；同样，关闭端口学习能力的端口不能开启接入控制功能。

######  配置动态地址老化时间

+ 可选配置。

+ 如果需要修改动态地址老化时间，则应该执行此配置项。

+ 交换机设备上配置。

【命令格式】 mac-address-table aging-time value
【参数说明】 value：老化时间。取值范围{ 0 | 10－1000000 }，缺省值 300 秒。
【缺省配置】 缺省值是 300 秒
【命令模式】 全局模式
【使用指导】 当设置该值为 0 时，地址老化功能将被关闭，学习到的地址将不会被老化。

地址表的实际老化时间会与设定值存在一定偏差，但不会超过设定值的2 倍。

**检验方法**

+ 检查设备是否能正常学习动态地址。

+ 通过show mac-address-table dynamic命令查看动态地址信息。

+ 通过show mac-address-table aging-time命令查看动态地址老化时间。

【命令格式】 show mac-address-table dynamic [ address mac-address ] [ interface interface-id ] [ vlan vlan-id ]
【参数说明】 address mac-address：查看设备上特定动态MAC地址信息。
interface interface-id：指定的物理接口或是Aggregate Port。
vlan vlan-id：查看特定的VLAN中的动态地址。
【命令模式】 特权模式，全局模式，接口模式
【使用指导】 -
【命令展示】 

```
Ruijie# show mac-address-table dynamic
Vlan MAC Address Type Interface

---- ------------ ------ ------------------

1 0000.0000.0001 DYNAMIC GigabitEthernet 1 /1
1 0001.960c.a740 DYNAMIC GigabitEthernet 1 /1
1 0007.95c7.dff9 DYNAMIC GigabitEthernet 1 /1
1 0007.95cf.eee0 DYNAMIC GigabitEthernet 1 /1
1 0007.95cf.f41f DYNAMIC GigabitEthernet 1 /1
1 0009.b715.d400 DYNAMIC GigabitEthernet 1 /1
1 0050.bade.63c4 DYNAMIC GigabitEthernet 1 /1
```

字段解释

<table>
  <thead>
    <tr>
      <th>字段</th>
      <th>说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Vlan</td>
      <td>MAC 地址所在的 VLAN</td>
    </tr>
    <tr>
      <td>MAC Address</td>
      <td>MAC 地址</td>
    </tr>
    <tr>
      <td>Type</td>
      <td>MAC 地址类型</td>
    </tr>
    <tr>
      <td>Interface</td>
      <td>MAC 地址所在的接口</td>
    </tr>
  </tbody>
</table>


【命令格式】 show mac-address-table aging-time^
【参数说明】 -
【命令模式】 特权模式，全局模式，接口模式
【使用指导】 -
【命令展示】

```
 Ruijie# show mac-address-table aging-time
Aging time : 300
```



##### 配置举例

######  配置动态地址

【配置方法】 

+ 打开接口MAC地址学习能力

+ 配置动态地址老化时间为 180 秒

+ 删除接口GigabitEthernet 0/1下VLAN 1中的所有动态地址

  ```
  Ruijie# configure terminal
  Ruijie(config-if-GigabitEthernet 0/1)# mac-address-learning
  Ruijie(config-if-GigabitEthernet 0/1)# exit
  Ruijie(config)# mac aging-time 180
  Ruijie# clear mac-address-table dynamic interface GigabitEthernet 0/1 vlan 1
  ```

  

【检验方法】

+ 查看接口MAC地址学习能力
+ 查询动态地址老化时间
+ 查看接口GigabitEthernet 0/1下VLAN 1中的所有动态地址

```
Ruijie# show mac-address-learning
GigabitEthernet 0/1 learning ability: enable
Ruijie# show mac aging-time
Aging time : 180 seconds
Ruijie# show mac-address-table dynamic interface GigabitEthernet 0/1 vlan 1
Vlan MAC Address Type Interface
----------  -------------------- -------- -------------------
1 00d0.f800.1001 STATIC GigabitEthernet 1 /1
```

##### 常见错误

配置接口地址学习能力时，接口没有先配置成二层接口，包括交换口、AP口。

#### 2.5.2 配置静态地址

##### 配置效果

+ 配置静态地址，绑定设备下接的网络设备的MAC地址与端口关系。

##### 配置方法

######  配置静态地址

+ 可选配置。

+ 如果需要绑定设备下接的网络设备的MAC地址与端口关系，则应该执行此配置项。

+ 交换机设备上配置。

【命令格式】 mac-address-table static mac-address vlan vlan-id interface interface-id
【参数说明】 address mac-address：指定要删除的MAC地址。vlan vlan-id：指定要删除的MAC地址所在的VLAN。interface interface-id：指定的物理接口或是Aggregate Port。
【缺省配置】 缺省没有设置任何静态地址
【命令模式】 全局模式
【使用指导】 当设备在vlan-id指定的VLAN上接收到以mac- address为目的地址的报文时，这个报文将被转发到interface-id所指定的接口上。

##### 检验方法

+ 通过命令show mac-address-table static显示静态地址信息是否正确。

【命令格式】 show mac-address-table static [ address mac-address ] [ interface interface-id ] [ vlan vlan-id ]
【参数说明】 address mac-address：查看设备上特定静态MAC地址信息。interface interface-id：指定的物理接口或是Aggregate Port。vlan vlan-id：查看特定的VLAN中的静态地址。

【命令模式】 特权模式，全局模式，接口模式
【使用指导】 -
【命令展示】 

```
Ruijie# show mac-address-table static
Vlan MAC Address Type Interface

----- ----------- -------- ------------------

1 00d0.f800.1001 STATIC GigabitEthernet 1/1
1 00d0.f800.1002 STATIC GigabitEthernet 1/1
1 00d0.f800.1003 STATIC GigabitEthernet 1/1
```

##### 配置举例

######  配置静态地址

本例的MAC地址同VLAN、接口对应关系如下表所示：

<table>
  <thead>
    <tr>
      <th>角色</th>
      <th>MAC 地址</th>
      <th>VLAN ID</th>
      <th>接口 ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Web 服务器</td>
      <td>00d0.3232.0001</td>
      <td>VLAN2</td>
      <td>Gi0/10</td>
    </tr>
    <tr>
      <td>信息服务器</td>
      <td>00d0.3232.0002</td>
      <td>VLAN2</td>
      <td>Gi0/11</td>
    </tr>
    <tr>
      <td>网络管理员</td>
      <td>00d0.3232.1000</td>
      <td>VLAN2</td>
      <td>Gi0/12</td>
    </tr>
  </tbody>
</table>




【配置方法】 

+ 指定表项对应的目的MAC地址（Mac-address）

+ 指定该地址所属的VLAN（vlan-id）

+ 接口ID（Interface-id）

  ```
  A A# configure terminal^
  A(config)# mac-address-table static 00d0.f800.3232.0001 vlan 2 interface gigabitEthernet 0/10
  A(config)# mac-address-table static 00d0.f800.3232.0002 vlan 2 interface gigabitEthernet 0/11
  A(config)# mac-address-table static 00d0.f800.3232.1000 vlan 2 interface gigabitEthernet 0/12
  ```

```
【检验方法】 在交换机上查看配置的静态MAC地址
A A# show mac-address-table static
Vlan MAC Address Type Interface
---------- -------------------- -------- -------------------
2 00d0.f800.3232.0001 STATIC GigabitEthernet 0/10
2 00d0.f800.3232.0002 STATIC GigabitEthernet 0/11
2 00d0.f800.3232.1000 STATIC GigabitEthernet 0/12
```

#### 2.5.3 配置过滤地址

##### 配置效果

+ 配置过滤地址，当在对应VLAN中接收到源MAC或目的MAC为过滤地址的报文时，将丢弃此报文。

**配置方法**

######  配置过滤地址

+ 可选配置。

+ 如果需要过滤报文，则应该执行此配置项。

+ 交换机设备上配置。

【命令格式】 mac-address-table filtering mac-address vlan vlan-id
【参数说明】 address mac-address：指定要删除的MAC地址
vlan vlan-id：指定要删除的MAC地址所在的VLAN。
【缺省配置】 缺省没有设置任何过滤地址
【命令模式】 全局模式
【使用指导】 当设备在vlan-id指定的VLAN上接收到以mac-address指定的地址为源地址或目的地址的报文将被丢弃。

##### 检验方法

+ 通过命令show mac-address-table filter显示过滤地址信息。

【命令格式】 show mac-address-table filter [ address mac-address ] [ vlan vlan-id ]
【参数说明】 address mac-address：查看设备上特定过滤MAC地址信息。vlan vlan-id：查看特定的VLAN中的过滤地址。
【命令模式】 特权模式，全局模式，接口模式
【使用指导】 -^
【命令展示】 

```
Ruijie# show mac-address-table filtering
Vlan MAC Address Type Interface

------ -------------------- -------- -----------

1 0000.2222.2222 FILTER
```

##### 配置举例

######  配置过滤地址

【配置方法】 

+ 指定过滤地址对应的目的MAC地址（Mac-address）

+ 指定过滤地址所属的VLAN（vlan-id）

```
Ruijie# configure terminal
Ruijie(config)# mac-address-table static 00d0.f800.3232.0001 vlan 1
```

【检验方法】 在交换机上查看配置的过滤MAC地址

```
Ruijie# show mac-address-table filter
Vlan MAC Address Type Interface
---------- -------------------- -------- -------------------
1 00d0.f800.3232.0001 FILTER
```

#### 2.5.4 配置 MAC 地址变化通知

##### 配置效果

+ 配置MAC地址变化通知，监控网络设备下的用户变化。

##### 配置方法

######  配置接收 MAC 地址通知的 NMS

+ 可选配置

+ 如果需要接收MAC地址通知，则应该执行此配置项。

+ 交换机设备上配置。

【命令格式】 snmp-server host host-addr traps [ version {^1 | 2c^ |^3 [ auth^ | noauth^ | priv ] } ]^ community-string^
【参数说明】 host host-addr：指明接收者的IP。
version { 1 | 2c | 3 [ auth | noauth | priv ] }：指明发送哪种版本的snmp trap报文，对v3版本还可以指定是否认证以及安全等级参数。
community-string：认证名
【缺省配置】 缺省不需要配置
【命令模式】 全局模式
【使用指导】 -

######  配置使能发送 Trap 功能

+ 可选配置。

+ 如果需要发送Trap，则应该执行此配置项。

+ 交换机设备上配置。

【命令格式】 snmp-server enable traps
【参数说明】 -
【缺省配置】 缺省不需要配置
【命令模式】 全局模式
【使用指导】 -^

######  配置全局 MAC 地址通知开关

+ 可选配置。

+ 全局开关被关闭，所有接口的MAC地址通知功能也均被关闭。

+ 交换机设备上配置。

【命令格式】 mac-address-table notification
【参数说明】 -
【缺省配置】 缺省全局MAC地址变化通知开关关闭
【命令模式】 全局模式
【使用指导】 -^

######  配置接口 MAC 地址通知开关

+ 可选配置
+ 如果需要接收接口MAC地址变化通知，则应该执行此配置项。
+ 交换机设备上配置。

【命令格式】 snmp trap mac-notification { added | removed }
【参数说明】 added：当地址增加时通知。
removed：当地址被删除时通知。
【缺省配置】 缺省接口MAC地址变化通知开关关闭
【命令模式】 接口模式
【使用指导】 -^

######  配置 MAC 地址通知的时间间隔与历史记录容量

+ 可选配置。
+ 如果需要修改MAC地址通知的时间间隔或历史记录容量，则应该执行此配置项。
+ 交换机设备上配置。

【命令格式】 mac-address-table notification { interval value | history-size value }
【参数说明】 interval value ：设置产生MAC地址通知的时间间隔(可选)。时间间隔的单位为秒，范围为 1 － 3600 ，缺省
为 1 秒。
history-size value ：MAC通知历史记录表中记录的最大个数，范围 1 － 200 ，缺省为 50 。
【缺省配置】 时间间隔缺省为 1 秒，表项默认通告的最大通告个数为 50 。
【命令模式】 全局模式
【使用指导】 -

##### 检验方法

+ 通过命令show mac-address-table notification检查NMS是否能正常接收MAC地址变化通知。

【命令格式】 show mac-address-table notification [ interface [ interface-id ] | history ]
【参数说明】 interface : 显示全部接口上的MAC通知功能设置。
interface-id ：查看接口的MAC地址变化通知的使能状况。
history：查看MAC地址变化通知信息的历史记录表。
【命令模式】 特权模式，全局模式，接口模式
【使用指导】 -
【使用指导】1、查看MAC地址通告功能的全局配置信息

```
Ruijie#show mac-address-table notification
MAC Notification Feature : Enabled
Interval(Sec): 300
Maximum History Size : 50
Current History Size : 0
```

字段解释：

<table>     <thead>         <tr>             <th>字段</th>             <th>说明</th>         </tr>     </thead>     <tbody>         <tr>             <td>Interval(Sec)</td>             <td>通告 MAC 地址的时间间隔</td>         </tr>         <tr>             <td>Maximum History Size</td>             <td>MAC 地址通告历史记录表的最大表项个数</td>         </tr>         <tr>             <td>Current History Size</td>             <td>当前记录条目数</td>         </tr>     </tbody> </table>  </body> </html>

##### 配置举例

【网络环境】

图为某企业内部网络示意图。下联用户通过Gi0/2口连接到交换机。
为了便于管理员对下联用户使用网络情况信息的掌控，希望通过配置达到以下目的：

+ 当交换机下联用户的接口学习到一个新的MAC地址或老化掉一个已学习到的地址时，将地址变化信息记录到MAC地址通知历史记录表中，供管理员了解最近的MAC地址变化信息。
+ 同时，交换机能将MAC地址变化通知以SNMP Trap的方式将通知信息发送给指定的NMS(网络管理工
  作站)
+ 当交换机下联用户较多时，能尽量避免短时间内产生大量的MAC地址变化信息，减轻网络的负担。

【配置方法】 

+ 打开交换机全局MAC地址通知开关，在Gi0/2接口上配置MAC地址通知功能。

+ 配置NMS主机地址，使能交换机主动发送SNMP Trap通知。交换机到NMS（网络管理工作站）的路由可达。

+ 设置交换机发送MAC地址通知的时间间隔为 300 秒（默认时间间隔为 1 秒）。

  ```
  A 
  Ruijie# configure terminal^
  Ruijie(config)# mac-address-table notification
  Ruijie(config)# interface gigabitEthernet 0/2
  Ruijie(config-if-GigabitEthernet 0/2)# snmp trap mac-notification added
  Ruijie(config-if-GigabitEthernet 0/2)# snmp trap mac-notification removed
  Ruijie(config-if-GigabitEthernet 0/2)# exit
  Ruijie(config)# snmp-server host 192.168.1.10 traps version 2c comefrom2
  Ruijie(config)# snmp-server enable traps
  Ruijie(config)# mac-address-table notification interval 300
  ```

【检验方法】 

+ 查看MAC地址通知功能的全局配置信息。
+ 查看接口的MAC地址变化通知的使能状况。
+ 查看接口MAC地址表，并使用使用clear mac-address-table dynamic命令模拟动态地址的老化。
+ 查看MAC地址通知功能的全局配置信息。
+ 查看MAC地址变化通知信息的历史记录表。

```
A
Ruijie# show mac-address-table notification
MAC Notification Feature : Enabled
Interval(Sec): 300
Maximum History Size : 50
Current History Size : 0
Ruijie# show mac-address-table notification interface GigabitEthernet 0/2
Interface MAC Added Trap MAC Removed Trap
----------- -------------- --------------
GigabitEthernet 0/2 Enabled Enabled
Ruijie# show mac-address-table interface GigabitEthernet 0/2
Vlan MAC Address Type Interface
---------- -------------------- -------- -------------------
1 00d0.3232.0001 DYNAMIC GigabitEthernet 0/2
Ruijie# show mac-address-table notification
MAC Notification Feature : Enabled
Interval(Sec): 300
Maximum History Size : 50
Current History Size : 1
Ruijie# show mac-address-table notification history
History Index : 0
Entry Timestamp: 221683
MAC Changed Message :
Operation:DEL Vlan:1 MAC Addr: 00d0.3232.0003 GigabitEthernet 0/2
```

#### 2.5.5 配置 MAC 数量到达一定阀值发出 syslog 告警

##### 配置效果

+ MAC数目到达一定阀值后，会发出syslog告警，可以配置告警的时间间隔，告警阀值（可指定用百分比表示或直接用数字表示）。

##### 配置方法

######  配置告警间隔

+ 可选配置。

+ 如果需要控制告警的间隔，而不使用默认值一小时，则应配置此项。

+ 交换机设备上配置。

【命令格式】 mac-address-table warning-threshold interval seconds
【参数说明】 seconds：时间间隔，单位为秒，范围 10 - 7200 。
【缺省配置】 3600 秒，即一小时。
【命令模式】 全局模式
【使用指导】

##### 检验方法

+ 可以通过show run查看配置结果。

##### 配置举例

######  配置告警间隔

【配置方法】  配置告警间隔

```
Ruijie# configure terminal
Ruijie(config)# mac-address-table warning-threshold interval 1800
```

【检验方法】 在交换机上通过show running命令可以查看到相应配置。

###### 2.5.6 配置 MAC 地址漂移检测功能

##### 配置效果

+ 当同一个VLAN中，两个端口上同一个MAC地址在短时间内发生漂移（即之前在一个端口上学习到，然后又在另一个端口学习到），则打印一条Syslog告警。

##### 配置方法

######  配置 MAC 地址漂移检测功能

+ 可选配置。

+ 如果需要在同一VLAN内检测到同一个MAC地址在不同端口上短时间内漂移时，打印Syslog告警，则应配置此项。

+ 交换机设备上配置。

【命令格式】 mac-address-table flapping-logging
【参数说明】
【缺省配置】 缺省该功能关闭。
【命令模式】 全局模式
【使用指导】

##### 检验方法

+ 可以通过show run查看配置结果。

+ 可以通过打印Syslog查看是否有检测到MAC地址漂移。

##### 配置举例

######  配置告警间隔

【配置方法】 

+ 配置MAC地址漂移检测功能

```
Ruijie# configure terminal
Ruijie(config)# mac-address-table flapping-logging
```

【检验方法】 在交换机上通过show running命令可以查看到相应配置。



#### 2.5.7 配置 MAC 地址漂移防护策略

##### 配置效果

+ 当MAC漂移功能检测到存在MAC地址漂移时，若在MAC地址漂移的端口上有配置MAC漂移防护策略，则对应策略会生效，将端口shutdown。

##### 注意事项

+ 需要先开启MAC漂移检测功能。

**配置方法**

######  配置 MAC 地址漂移防护策略

+ 可选配置。

+ 如果需要在检测到出现MAC地址在不同端口上漂移时，防止继续出现漂移，则应配置此项。

+ 交换机设备上配置。

【命令格式】 mac-address-table flapping action [error-down | priority priotiry-num]
【参数说明】 error-down ： 检测到MAC地址漂移后，采用shutdown端口的策略。
priority priotiry-num ： 配置接口error-down策略生效的优先级，priotiry-num缺省为最低优先级 0 ，范围在
0 - 5 ，值越大则优先级越高。
【缺省配置】 缺省该功能关闭。
【命令模式】 接口模式。
【使用指导】 需要先配置MAC地址漂移检测功能，否则配置后不会生效。

**检验方法**

+ 可以通过show run查看配置结果。

##### 配置举例

######  配置告警间隔

【配置方法】 

+ 配置MAC地址漂移检测功能

  ```
  Ruijie# configure terminal 
  Ruijie(config)# mac-address-table flapping-logging
  ```

  

+ 开启接口上 MAC 地址漂移防护策略

  ```
  Ruijie(config)# interface GigabitEthernet 1/1
  Ruijie(config-if-GigabitEthernet 1/1)# mac-address-table flapping action error-down
  Ruijie(config-if-GigabitEthernet 1/1)# mac-address-table flapping action priority 2
  ```

【检验方法】 在交换机上通过show running命令可以查看到相应配置

#### 2.5.8 配置端口下 MAC 地址限数

##### 配置效果

+ 端口下只能学习限制数量的动态地址。

##### 配置方法

######  配置端口 MAC 地址限数

+ 可选配置。

+ 交换机设备上配置。

【命令格式】 max-dynamic-mac-count count
【参数说明】 count：端口下最大地址学习个数
【缺省配置】 默认端口学习个数不限制；配置端口限数之后，默认超过源地址学习个数的报文继续转发
【命令模式】 接口模式
【使用指导】

##### 检验方法

+ 可以通过show run查看配置结果。

##### 配置举例

######  配置端口 MAC 地址限数

【配置方法】 

+ 配置端口下的地址学习最大个数

+ 配置端口下的地址学习最大个数

  ```
  Ruijie(config)# interface GigabitEthernet 1/1
  Ruijie(config-if-GigabitEthernet 1/1)# max-dynamic-mac-count 100
  ```

【检验方法】 在交换机上通过show running命令可以查看到相应配置。



### 2.6 监视与维护

##### 清除各类信息

在设备运行过程中执行clear命令，可能因为重要信息丢失而导致业务中断。

<table border="1">
  <tr>
    <th>作用</th>
    <th>命令</th>
  </tr>
  <tr>
    <td>清除动态地址表项。</td>
    <td>clear mac-address-table dynamic [ address mac-address ] [ interface interface-id ] [ vlan vlan-id ]</td>
  </tr>
</table>


**查看运行情况**

<table border="1">
  <tr>
    <th>作用</th>
    <th>命令</th>
  </tr>
  <tr>
    <td>查看 MAC 地址表。</td>
    <td>show mac-address-table { dynamic | static | filter } [ address mac-address ] 
[ interface interface-id ] [ vlan vlan-id ]
</td>
  </tr>
    <tr>
    <td>查看动态地址老化时间。</td>
    <td>show mac-address-table aging-time</td>
  </tr>
  <tr>
    <td>查看动态地址个数限制情况。</td>
    <td>show mac-address-table max-dynamic-mac-count</td>
  </tr>
  <tr>
    <td>查看地址变化通知配置及历史记录表。</td>
    <td>show mac-address-table notification [ interface [ interface-id ] | history ]
  </tr>
</table>


##### 查看调试信息

<table border="1">
  <tr>
    <th>作用</th>
    <th>命令</th>
  </tr>
  <tr>
    <td>打开 MAC 运行情况的调试开关。</td>
    <td>debug bridge mac</td>
  </tr>
</table>





## 3 Aggregate Port

### 3.1 概述

Aggregate Port（简称AP）是将多个物理链接捆绑在一起形成一个逻辑链接，可以用于扩展链路带宽，提供更高的连接可靠性。

AP支持流量平衡，可以把流量均匀地分配给各成员链路。AP还实现了链路备份，当AP中的一条成员链路断开时，系统会将该成员链路的流量自动地分配到AP中的其它有效成员链路上。AP中一条成员链路收到的广播或者多播报文，将不会被转发到其它成员链路上。

比如两台设备之间，单个端口相连最多为 1000 M（假定两台设备的端口都为 1000 M），当该链路上承载的业务流量超过1000M时，超过的部分就会被丢弃，而端口聚合将可以解决这一问题。例如，使用若干根网线连接这两台设备，再将这若干个端口进行聚合绑定，这样这些端口就逻辑捆绑形成了1000M * n的最大流量。

又比如，如果两台设备是通过单个网线相连接，当这两个端口之间出现链路断开时，这条线路上承载的业务就会断掉，而如果将多干个互连的端口进行聚合绑定，只要有一条链路没有出现链路断开，那么在这些端口上承载的业务就不会断掉。



### 3.2 典型应用

<table >
  <tr>
    <th>典型应用 </th>
    <th>场景描述</th>
  </tr>
  <tr>
    <td>AP链路聚合及流量平衡</td>
    <td>汇聚和核心设备之间通常存在大量报文流，需要更大的端口带宽来支撑，这时候就可以把设备上多条物理链路聚合成一条逻辑链路，增大链路带宽，并通过配置适当的流量平衡算法，使聚合口上的报文尽可能平衡到每一条物理链路，以提高带宽利用率。</td>
  </tr>
</table>


#### 3.2.1 AP 链路聚合及流量平衡

##### 应用场景

在下图中，左边的交换机设备通过AP与右边的路由器进行通讯，所有内网中的设备（如图中的左边 2 台PC机）以路由器为网关，所有外网（如图中的右边 2 台PC机）经路由器发出的报文的源MAC都是网关的MAC地址，为了让路由器与其他主机之间的通讯流量能由其他链路来分担，应设置为根据目的MAC地址进行流量平衡；而在交换机处，则需要设置为根据源MAC地址进行流量平衡。

【注释】 -

##### 功能部属

+ 把交换机与路由器之间的直连端口配置成一个静态AP或LACP在交换机上设置基于源MAC的流量平衡算法

+ 在路由器上设置基于目的MAC的流量平衡算法

### 3.3 功能详解

##### **基本概念**

######  静态 AP

静态AP模式是一种利用手工配置模式直接将物理端口加入到AP聚合组中，在物理端口的链路状态和协议状态准备好的情况下，就能进行数据报文转发的一种聚合模式。

静态AP模式下的AP接口，称为静态AP口，对应的成员口称为静态AP成员口。

LACP是一个关于动态链路聚合的协议，它通过协议报文 LACPDU(Link Aggregation Control Protocol Data Unit，链路聚合控制协议数据单元)和相连的设备交互信息。

LACP模式下的AP接口，称为LACP AP口，对应的成员口称为LACP AP成员口。

######  AP 成员端口模式

AP成员端口有 3 种聚合模式：主动(Active)模式、被动模式(Passive)和静态模式。

其中主动模式的端口会主动发起LACP报文协商；被动模式的端口则只会对收到的LACP报文做应答；静态模式不会发出LACP报文进行协商，这种模式只会在静态AP模式下生效。各个聚合模式的相邻端口聚合模式要求如下：

<table >
  <tr>
    <th>端口模式</th>
    <th>相邻端口聚合模式要求。</th>
  </tr>
  <tr>
    <td>主动模式</td>
    <td>相邻端口聚合模式要求。</td>
  </tr>
  <tr>
    <td>被动模式</td>
    <td>主动模式。</td>
  </tr>
  <tr>
    <td>静态模式</td>
    <td>静态模式。</td>
  </tr>
</table>




######  AP 成员端口状态

静态AP成员端口的状态主要有以下两种：

+ 当成员端口的链路处于Down状态，端口不能转发任何数据报文，显示为”Down”状态；

+ 当成员端口链路处于Up状态，且链路协议准备好后，端口可以参与转发数据报文，显示为“Up”状态。

LACP成员端口可能处于以下三种状态：

+ 当端口的链路处于Down状态，端口不能转发任何数据报文，显示为”down”状态；

+ 端口链路处于Up状态，并经过LACP协商后，端口被置于聚合状态(端口被作为一个聚合组的一个成员，参与聚合组的数据报文转发)，显示为“bndl”状态；

+ 当端口链路处于UP状态，但是由于对端没有启用LACP，或者因为端口属性和主端口不一致等一些因素导致经过报文协
  商端口被置于挂起状态（处于挂起状态的端口不参与数据报文转发），显示为“susp”状态。

只有全双工的端口才能进行LACP聚合。
成员端口的速率、流控、介质类型以及成员端口的二、三层属性必须一致才能进行LACP聚合绑定。
LACP成员端口聚合后修改端口的上述属性将导致同聚合组内的其他端口也无法进行LACP聚合绑定。
已经启用禁止成员口加入或者退出AP功能的端口不能将端口加入静态AP或者LACP AP，或者从静态AP或者LACP AP中退出。



######  AP 容量模式

由于系统中总的成员口数量有限制，系统总支持成员口数 = 系统支持的最大AP口数量 * 单个AP口支持最大成员口数。因此当希望系统中最大AP口数量大一点，那么单个AP口下的最大成员口数就会小一点，反过来单个AP最大成员口数大一点，全局最大AP数量就小一点。某些特定的场景有这种需求，这就引出了AP容量模式的概念，在某些产品设备上支持AP容量模式可配置，比如系统支持 16384 个成员口，那么容量模式可以选择1024*16、512*32等等（最大AP数*单个AP下最大成员口数）。

######  LACP 的系统 ID

每台设备仅能配置一个LACP聚合系统。聚合系统有一个系统ID来标示这个系统的优劣，同时存在一个系统优先级，这是一个可配置的数值。系统ID 由LACP的系统优先级和设备MAC地址组成。系统优先级越小，系统ID的优先级越高；在系统优先级相同的情况下，比较设备的MAC地址，设备MAC地址越小，系统ID的优先级越高。系统ID优先级较高的系统决定端口状态，低优先级系统的端口状态随高优先级系统的端口状态变化而变化。

######  LACP 的端口 ID

每个端口有独立的LACP端口优先级，这是一个可配置的数值。端口ID由LACP的端口优先级和端口号组成。端口优先级数值越小，端口ID的优先级越高；在端口优先级相同的情况下，端口号越小，端口ID的优先级越高。

######  LACP 的主端口

当有动态成员处于Up状态时，LACP会根据端口的速率，双工速率等关系，并综合聚合组内端口ID优先级、聚合组内已经Up的成员口的绑定状态等信息，选择其中的一个成员口端口作为主端口。只有和主端口属性相同的端口才能处于聚合状态，参与聚合组的数据转发。当端口的属性变化时，LACP会重新选择主端口；当新的主端口不处于聚合状态时，LACP会把同一个聚合组内的成员解聚合，重新聚合。


配置指南 Aggregate Port

######  LACP 独立口

通常用在接入交换机和双网卡服务器对接的场景下。一些双网卡服务器启机未预安装系统情况下，需要通过远程网络PXE装机设备进行系统安装，此时双网卡服务器因为没有安装系统不能和接入设备进行LACP协商，并且仅一个网卡是可工作的，这便要求接入设备的端口在不能进行LACP协商时可以自动转换为普通以太网物理口，保障服务器和远程PXE装机设备能够正常通信，当服务系统安装完成，其双网卡可以正常运行LACP协议之后，接入设备上的端口要能重新启用LACP协议进行协商。

LACP独立口仅支持工作在L2 LACP，设置使能LACP独立口之后，独立口未收到LACP报文自动转换为普通以太网口，会自动拷贝AP口的速率双工流控以及VLAN配置，保证端口的转发能力。

LACP独立口在独立口超时时间内没有收到LACP报文之后才会自动转换为普通物理口，当重新收到LACP报文时，又会重新转换为LACP成员口。

##### 功能特性

<table>     <tr>         <th>功能特性</th>         <th>作用</th>     </tr>     <tr>         <td>链路聚合</td>         <td>将物理链路通过静态或动态的方式聚合，以达到扩展带宽、链路备份的作用。</td>     </tr>     <tr>         <td>流量平衡</td>         <td>通过不同的流量均衡模式，可以灵活地对聚合组内流量进行负载均衡。</td>     </tr> </table>

#### 3.3.1 链路聚合

##### 工作原理

AP链路聚合方式分为两种，一种是通过手工配置，即静态AP；另一种是通过LACP协议动态聚合。

+ 静态AP

静态AP实现简单，用户只要将指定的物理端口通过配置命令加入到同一个聚合组AP中，就可以实现多条物理链路的聚合。成员端口一旦加入聚合组后，即可参与AP聚合组的数据收发功能，并参与聚合组的流量均衡。

+ 动态AP(LACP)

如果端口启用LACP协议，端口会发送LACPDU来通告自己的系统优先级、系统MAC、端口的优先级、端口号和操作key等。相连设备收到对端的LACP报文后，根据报文中的系统ID比较两端的系统优先级。在系统ID优先级较高的一端，将按照端口ID优先级从高到低的顺序，设置聚合组内端口处于聚合状态，并发出更新后的LACP报文，对端设备收到报文后，也会把相应的端口设置成聚合状态，从而使双方在端口退出或者加入聚合组上达到一致。只有双方的端口都完成动态聚合绑定操作后，
该物理链路才能进行数据报文的转发。

LACP成员口链路绑定之后，还会进行周期性的LACP报文交互，在一段时间没有收到LACP报文时，就认为收包超时，成员口链路解除绑定，端口重新处于不可转发状态。这里的超时时间有两种模式:长超时模式和短超时模式.在长超时模式下，端口间隔 30 秒发送一个报文，若 90 秒没有收到对端报文，就处于收包超时；在短超时模式下，端口间隔 1 秒发送一个报文，若 3秒钟没有收到对端报文，就处于收包超时。

如上图所示，交换机A和交换机B通过 3 个端口连接在一起。设置交换机A的系统优先级为 61440 ，设置交换机B的系统优先级为 4096 。在交换机A和B的 3 个直连端口上打开LACP链路聚合，设置 3 个端口的聚合模式为主动模式，设置 3 个端口的端口优先级为默认优先级 32768 。

在收到对端的LACP报文后，交换机B发现自己的系统ID优先级比较高(交换机B的系统优先级比交换机A高)，于是按照端口ID优先级的顺序(端口优先级相同的情况下，按照端口号从小到大的顺序)设置端口 4 、 5 、 6 处于聚合状态。交换机A收到交换机B更新后的LACP报文后，发现对端的系统ID优先级比较高，并且把端口设置成聚合状态了，也把端口 1 、 2 、 3 设置成聚合状态了。

#### 3.3.2 流量平衡

##### 工作原理

AP可以根据报文的源MAC地址、目的MAC地址、源IP地址、目的IP地址、L4层源端口、L4层目的端口号等报文特征信息，进行一种或几种组合模式算法对报文流进行区分，将属于同一报文流从同一条成员链路通过，不同的报文流则平均分配到各个成员链路中。例如，采用源MAC地址流量平衡模式，会根据报文的源MAC地址将报文分配到AP的各个成员链路上。不同源MAC的报文，根据源MAC地址在各成员链路间平衡分配；相同源MAC的报文，固定从同一个成员链路转发。

目前可支持的AP流量平衡模式如下：

+ 源MAC或目的MAC地址

+ 源MAC+目的MAC地址

+ 源IP地址或目的IP地址

+ 源IP地址+目的IP地址

根据报文的IP地址或端口号进行流量平衡的模式仅适用于三层报文，如果在此流量平衡模式下收到二层报文，则自动根据设备的默认方式进行流量平衡。
各种流量平衡模式都是利用流量算法（哈希算法）、根据该模式采用的输入参数（源MAC、目的MAC、源MAC+目的MAC、源IP、目的IP、源IP+目的IP、源ip+目的ip和L4端口号等）计算特定报文应选择的成员链路，来实现流量均衡。这种算法能够保证输入参数不同的报文被大致均衡地分配给各成员链路，但并不意味着，输入参数不同的报文就一定选择不同的成员链路。比如，对IP模式而言，两个具有不同源IP+目的IP地址的报文，通过计算可能分配到同一个AP的成员链路。
不同产品，流量均衡支持度可能存在差异。

######  增强模式流量均衡

增强模式允许用户将不同报文类型的多个字段进行组合以达到流量均衡，包含L2 报文对应的字段src-mac、dst-mac、l2-protocol、vlan、src-port，Ipv4报文的对应的字段src-ip、dst-ip、protocol、l4-src-port、l4-dst-port、vlan，Ipv6报文的字段src-ip、dst-ip、protocol、l4-src-port、l4-dst-port、vlan，mpls报文对应的字段top-label、 2 nd-label、src-ip、dst-ip、vlan、src-port，TRILL报文对应的字段vlan、src-mac、dst-mac，FCOE报文对应的字段src-id、ox-id、dst-id。在增强模式下，设备先判断发送报文的类型，然后根据指定报文的字段进行流量均衡。比如，源IP变化的Ipv4报文要从AP口输出，那么AP会根据用户指定的Ipv4报文字段src-ip进行流量均衡。

以上所有流量平衡模式都适用于二层AP和三层AP，用户应根据不同的网络环境设置合适的流量分配方式，以便能把流量较均匀地分配到各个链路上，充分利用网络的带宽。
增强模式中L2均衡包含src-mac、dst-mac、vlan，Ipv4均衡包含src-ip，如果输入的报文是源MAC变化的 Ipv4报文，那么均衡算法不生效，因为该模式先检查报文类型为 Ipv4，那么只会根据 Ipv4对应设置的字段src-ip均衡。
增强模式中MPLS均衡算法只对MPLS L3 VPN报文生效，对MPLS L2 VPN报文无效。^

######  哈希流量均衡控制

哈希流量均衡允许用户在不同的场景更加灵活的控制流量均衡。目前我司采用流量哈希均衡控制主要有以下：哈希扰动功能、同步哈希功能。

+ 哈希扰动功能：AP聚合口流量均衡采用哈希散列方式进行均衡，同类型的两台设备，同一条流流量均衡会计算出相同的路径，在部署ECMP的环境下,可能导致两台设备上的同一条流均衡到同一台目的设备，称之为哈希极化问题。哈希扰动因子的作用就是用来影响设备流量均衡算法,不同设备上通过配置不一样的扰动因子,来达到同一条流计算出不同路径的目的。

+ 同步哈希功能：为了保障网络安全，实际组网通常会在内网和外网之间架设防火墙集群进行流量清洗，其要求一个会话的下行和上行双向流都要传递给防火墙集群中的同一台设备处理。一个会话的上行流和下行流的源IP和目的IP是颠倒的，传统哈希算法计算来的上行流和下行流会被定向到不同的防火墙上。同步哈希功能可以确保双向流计算出路径一致。

#### 3.3.3 成员口支持 BFD 检测

##### 工作原理

BFD是一种路由通路故障快速检测的协议。根据RFC7130，LACP协议即使是运行短超时模式，也需要 3 秒钟的时间才能检测到链路故障。而这 3 秒期间，往该链路均衡的报文就将全部丢包。BFD能够提供更短时间的故障检测，因此可设置成员口与BFD协议联动，BFD协议辅助检测链路故障，以便故障发生时，流量能快速切换到其他成员链路。当BFD检测到某条成员口通路故障时，AP口上的报文不往该口均衡。

在AP口上配置开启BFD检测功能后，AP内每个处于转发状态的成员口会自动创建BFD检测会话，每个成员口独立进行检
测。

### 3.4 配置详解

<table>
  <thead>
    <tr>
      <th>配置项</th>
      <th colspan="2">配置建议 & 相关命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">配置静态AP。</td>
      <td colspan="2">必须配置。用于手工设置链路聚合。</td>
    </tr>
    <tr>
      <td>interface aggregateport</td>
      <td>创建一个以太网 AP 口。</td>
    </tr>
    <tr>
      <td>port-group</td>
      <td>配置以太网静态 AP 成员口。</td>
    </tr>
    <tr>
      <td rowspan="5">配置 LACP</td>
      <td colspan="2">必须配置。用于动态设置链路聚合。</td>
    </tr>
    <tr>
      <td>port-group mode</td>
      <td>配置 LACP 成员口。</td>
    </tr>
    <tr>
      <td>Lacp system-priority</td>
      <td>配置端口的优先级。</td>
    </tr>
    <tr>
      <td>lacp port-priority</td>
      <td>配置 LACP 成员口。</td>
    </tr>
    <tr>
      <td>lacp short-timeout</td>
      <td>配置端口为短超时模式。</td>
    </tr>
    <tr>
      <td rowspan="3">配置 AP 的 LinkTrap 功能</td>
      <td colspan="2">可选配置。用于过滤报文。</td>
    </tr>
    <tr>
      <td>snmp trap link-status</td>
      <td>打开发送 AP 口 LinkTrap 通告功能。</td>
    </tr>
    <tr>
      <td>aggregateport member linktrap</td>
      <td>打开发送 AP 成员口 LinkTrap 通告功能。</td>
    </tr>
    <tr>
      <td rowspan="13">配置流量平衡模式</td>
      <td colspan="2">可选配置。用于指定当前聚合链路的流量均衡模式。</td>
    </tr>
    <tr>
      <td>aggregateport load-balance</td>
      <td>设置 AP 的全局或单个 AP 口流量平衡算法。</td>
    </tr>
    <tr>
      <td colspan="2">可选配置。用于设置增强模式的模板。</td>
    </tr>
    <tr>
      <td>load-balance-profile</td>
      <td>重命名增强模式模板。</td>
    </tr>
    <tr>
      <td>l2 field</td>
      <td>配置二层报文的负载均衡方式。</td>
    </tr>
    <tr>
      <td>ipv4 field</td>
      <td>配置 Ipv4 报文的负载均衡方式。</td>
    </tr>
    <tr>
      <td>ipv6 field</td>
      <td>配置 Ipv6 报文的负载均衡方式。</td>
    </tr>
    <tr>
      <td>mpls field</td>
      <td>配置 MPLS 报文的负载均衡方式。</td>
    </tr>
    <tr>
      <td>trill field</td>
      <td>配置 TRILL 报文的负载均衡方式。</td>
    </tr>
    <tr>
      <td>fcoe field</td>
      <td>配置 FCOE 报文的负载均衡方式。</td>
    </tr>
    <tr>
      <td colspan="2">可选配置。用于控制流量均衡策略。</td>
    </tr>
    <tr>
      <td>hash-disturb string</td>
      <td>配置哈希扰动因子。</td>
    </tr>
    <tr>
      <td>hash-symmetrical [ipv4 | ipv6]</td>
      <td>配置使能同步哈希因子。</td>
    </tr>
    <tr>
      <td rowspan="2">配置 AP 的容量模式</td>
      <td colspan="2">可选配置。用于指定当前系统的 AP 容量模式。</td>
    </tr>
    <tr>
      <td>aggregateport capacity mode</td>
      <td>设置全局 AP 容量模式。</td>
    </tr>
    <tr>
      <td rowspan="2">配置AP下成员口开启BFD检测</td>
      <td colspan="2">可选配置。用于指定 AP 下成员口开启 BFD 检测功能。</td>
    </tr>
    <tr>
      <td>aggregate bfd-detect ipv4</td>
      <td>配置 AP 成员口开启 Ipv4 BFD 检测</td>
    </tr>
    <tr>
      <td>配置 LACP 独立口功能</td>
      <td>lacp individual-port enable</td>
      <td>配置使能 LACP 独立口功能。</td>
    </tr>
    <tr>
      <td>配置独立口超时时间</td>
      <td>lacp individual-timeout period time</td>
      <td>配置 LACP 独立口超时的时间。</td>
    </tr>
  </tbody>
</table>


#### 3.4.1 配置静态 AP

##### 配置效果

+ 通过手工添加AP口成员，将多个物理端口绑定，以实现链路聚合。

+ 聚合后的逻辑链路带宽是成员链路带宽的总和。

+ 当AP中的一条成员链路断开时，系统会将该成员链路的流量自动地分配到AP中的其它有效成员链路上。

##### 注意事项

+ 只有物理端口才允许加入AP口。

+ 不同介质类型或者不同端口类型的接口不允许加入同一个AP口。

+ 二层端口只能加入二层AP，三层端口只能加入三层AP；包含成员口的AP口不允许改变二层/三层属性。

+ 一个端口加入AP，端口的属性将被AP的属性所取代。

+ 一个端口从AP中删除，则端口的属性将恢复为加入AP前的属性。

当一个端口加入AP后，该端口的属性取代为AP口的属性，所以一般情况下不允许在AP成员口上进行配置，或者将配置单独生效到AP成员口上。但一些少数的命令或者功能，如shutdown和no shutdown配置命令等，这些仍然可以支持在AP成员口上配置，且配置能生效。所以用户在使用AP成员口的时候，需要根据具体的功能要求来确定是否支持单独
在AP成员口上生效，并进行正确配置。

静态聚合不具备检错机制，成员端口Link up即绑定，用户需自己保证拓扑正确性和成员口端口之间协商属性的一致性。

##### 配置方法

######  创建以太网 AP 口

+ 必须配置。

+ 在支持AP功能的设备上配置。以太网口使用聚合功能时需要创建对应的以太网AP口。

【命令格式】 interface aggregateport ap-number
【参数说明】 ap-number：AP接口编号
【缺省配置】 缺省情况下，AP口未被创建。
【命令模式】 全局配置模式
【使用指导】 在全局配置模式下，用户可以通过interfaces aggregateport配置命令创建一个以太网AP口。用户可以在全局配置模式下，通过no interfaces aggregateport ap-number删除指定的以太网AP口。

用户可以通过在指定以太网端口的接口模式下，执行port-group命令将物理端口加入一个静态AP；如果该AP不存在，则同时自动创建这个AP口。
用户也可以通过在指定物理端口的接口模式下，执行port-group mode命令将物理端口加入一个LACP AP；如果该AP不存在，则同时自动创建这个AP口。
配置AP功能时，需要在链路两端的设备上都配置，且需要配置相同的AP类型(静态AP或者LACP)。

######  配置以太网静态AP 成员口

+ 必须配置。

+ 在支持AP功能的设备上配置。使用静态聚合功能时需要配置对应的静态AP成员口。

【命令格式】 port-group ap-number
【参数说明】 port-group ap-number : AP接口编号
【缺省配置】 以太网端口不属于任何静态AP的成员口
【命令模式】 以太网接口配置模式
【使用指导】 在接口模式下，用户可以通过port-group配置命令向AP口中添加成员口。在接口配置模式下使用no
port-group命令将此成员口退出AP。

为保证链路聚合功能正常，在链路两端的设备上需要对称配置静态AP成员口。
将普通端口加入某个AP口后，当该端口再次从AP口退出时，普通端口上的原先相关的配置可能会恢复为缺省的配置。不同功能对AP口的成员的原有配置的处理方式有所不同，因此建议在端口从AP口退出后，应查看并确认端口的配置。
AP成员端口从AP口退出变成普通端口后，该端口会被shutdown以防止出现环路等问题，用户需要在确认拓扑无异常之后再在接口模式下执行no shutdown命令重新使能该接口。

######  二层 AP 与三层 AP 的转化

+ 为可选配置。

+ 如果需要启用AP口的三层路由等功能，比如需要在AP口上配置IP地址，或者配置静态路由表项等，需要先将二层AP口转化为三层AP口，再在三层AP口上启用路由等功能。

+ 该功能可在三层交换机等支持二、三层功能和AP功能的设备上配置。

【命令格式】 no switchport
【参数说明】 -
【缺省配置】 在支持二、三层功能和接口二、三层转换功能的设备上，AP口缺省为二层口。
【命令模式】 AP接口配置模式
【使用指导】 L3 AP是三层设备才支持的功能，所有二层设备均不支持。

对于三层设备，如果该设备不支持二层功能，AP口被创建时，则是一个三层AP口，否则AP口被创建时是一个二层AP口。

##### 检验方法

+ 通过show running命令查看相应的配置。

+ 通过show aggregateport summary命令查看AP口配置情况。

【命令格式】 show aggregateport aggregate-port-number [ load-balance | summary ]
【参数说明】 aggregate-port-number ： AP接口号
load-balance ： 显示AP的流量平衡算法summary ： 显示AP中的每条链路的摘要信息
【命令模式】 各模式均可执行
【使用指导】 如果没有指定AP接口号，则所有AP的信息将被显示出来

【命令展示】

```
Ruijie# show aggregateport 1 summary
AggregatePort MaxPorts SwitchPort Mode Load balance Ports

------------- --------------- ---------- ------ ----------------------------

------------------------

Ag1 8 Enabled ACCESS dst-mac Gi0/2
```

##### 配置举例

######  配置以太网静态 AP

【配置方法】 

+ 将SwitchA上的端口GigabitEthernet 1 /1和GigabitEthernet 1 / 2 加入到静态AP 3中。

+ 将SwitchB上的端口GigabitEthernet 2 /1和GigabitEthernet 2 / 2 加入到静态AP 3中。

```
SwitchA SwitchA# configure terminal
SwitchA(config)# interface range GigabitEthernet 1 /1- 2
SwitchA(config-if-range)# port-group 3
SwitchB SwitchB# configure terminal
SwitchB(config)# interface range GigabitEthernet 2 /1- 2
SwitchB(config-if-range)# port-group 3
```

【检验方法】

+ 通过show aggregateport summary查看AP口和成员口的对应关系是否正确。

```
SwitchA SwitchA# show aggregateport summary
AggregatePort MaxPorts SwitchPort Mode Ports
------------- -------- ---------- ------ -----------------------------------
Ag 3 8 Enabled ACCESS Gi 1 /1,Gi 1 /2
SwitchB SwitchB# show aggregateport summary
AggregatePort MaxPorts SwitchPort Mode Ports
------------- -------- ---------- ------ -----------------------------------
Ag 3 8 Enabled ACCESS Gi 2 /1,Gi 2 /2
```

#### 3.4.2 配置 LACP

##### 配置效果

+ 相连设备根据LACP自协商，动态聚合链路。

+ 聚合后的逻辑链路带宽是成员链路带宽的总和。

+ 当AP中的一条成员链路断开时，系统会将该成员链路的流量自动地分配到AP中的其它有效成员链路上。

+ 长超时模式时，链路故障后 90 秒才能感知到；配置短超时模式时， 3 秒钟就能感知到。

##### **注意事项**

+ 将普通端口加入某个LACP AP口后，当该端口再次从LACP AP口退出时，普通端口上的原先相关的配置可能会恢复为缺省的配置。不同功能对LACP AP口的成员的原有配置的处理方式有所不同，因此建议在端口从LACP AP口退出后，应查看并确认端口的配置。

+ 改变LACP的系统优先级可能引起LACP的成员端口出现解聚合再聚合现象。

+ 改变LACP成员口的端口优先级可能引起该LACP成员口对应的聚合组所有端口出现解聚合再聚合现象。

##### 配置方法

######  配置 LACP 成员口

+ 必须配置。

+ 将指定的物理端口配置为LACP成员口。在支持LACP功能的设备上配置。使用LACP功能时需要配置对应的LACP成员口。

【命令格式】 port-group^ key-number mode {^ active | passive }^
【参数说明】 Key-number :为聚合组的管理key，Key-number取值范围根据不同产品支持的聚合组数量不同而变，这个Key-number值就是对应的LACP AP口的端口号。
active:表示端口以主动模式加入动态聚合组
passive:模式表示端口以被动模式加入聚合组
【缺省配置】 物理端口不属于任何LACP的成员口
【命令模式】 物理接口配置模式
【使用指导】 在接口模式下，用户可以通过下面的配置命令向LACP AP口中添加成员口。

为保证LACP功能正常，在链路两端的设备上需要对称配置LACP成员口。

######  配置LACP的系统优先级

+ 为可选配置。

+ 在需要调整该设备系统ID优先级时进行配置，配置值越小，系统ID优先级越高，系统ID优先级高的设备优先选择聚合端口。

+ 可在支持LACP功能的设备上配置该功能。

【命令格式】 lacp system-priority system-priority
【参数说明】 system-priority ：LACP系统的优先级，可选范围为 0 - 65535 ，默认优先级为 32768 。
【缺省配置】 LACP的系统优先级为 32768
【命令模式】 全局配置模式
【使用指导】 在全局模式下，用户可以通过下面的配置命令配置LACP的系统优先级。一台设备的所有的动态链路组只能有一个LACP系统优先级，修改这个值会影响到交换机上的所有聚合组。在接口配置模式下使用no lacp system-priority命令将LACP的系统优先级恢复到缺省值。

######  配置LACP成员口的端口优先级

+ 可选配置。

+ 在需要调整端口ID优先级时进行配置，配置值越小，端口ID优先级越高，端口ID优先级高的端口会被优选为主端口。

+ 可在支持LACP功能的设备上配置该功能。

【命令格式】 lacp port-priority port-priority
【参数说明】 port-priority ：端口的优先级，可选范围为 0 - 65535, 默认优先级为 32768 。
【缺省配置】 LACP成员口的端口优先级为 32768
【命令模式】 物理接口配置模式
【使用指导】 在全局模式下，用户可以通过下面的配置命令配置LACP的系统优先级。在接口配置模式下使用no lacp port-priority命令将LACP的系统优先级恢复到缺省值。

######  配置LACP成员口的超时模式

+ 可选配置。

+ 在需要更实时感知链路故障的场景下，需要配置成短超时模式。配置短超时模式时，端口 3 秒收包超时，长超时模式，
  端口 90 秒收包超时。

+ 可在支持LACP功能的设备上配置该功能，比如交换机产品等。

【命令格式】 lacp short-timeout
【参数说明】 
【缺省配置】 LACP成员口的端口超时模式为长超时
【命令模式】 接口配置模式
【使用指导】 仅在物理口上支持。
在接口配置模式下使用no lacp short-timeout命令将LACP超时模式恢复为缺省值。

##### 检验方法


配置指南 Aggregate Port

+ 通过show running命令查看相应的配置。

+ 通过show lacp summary命令查看LACP链路状态。

【命令格式】 show lacp summary^ [ key-number^ ]^
【参数说明】 key-name：指定的LACP AP接口号
【命令模式】 各模式均可执行
【使用指导】 如果没有指定key-number，则所有LACP AP的链路聚合状态信息将被显示出来。
【命令展示】 

```
Ruijie(config)# show lacp summary 3
System Id:32768, 00d0.f8fb. 0002
Flags: S - Device is requesting Slow LACPDUs
F - Device is requesting Fast LACPDUs.
A - Device is in active mode. P - Device is in passive mode.
Aggregate port 3:
Local information:
LACP port Oper Port Port
Port Flags State Priority Key Number State
Gi0/ 1 SA bndl 4096 0x3 0x 1 0x3d
Gi0/ 2 SA bndl 4096 0x3 0x 2 0x3d
Gi0/ 3 SA bndl 4096 0x3 0x 3 0x3d
Partner information:
LACP port Oper Port Port
Port Flags Priority Dev ID Key Number State
Gi0/ 1 SA 61440 00 d0.f800.0 001 0x3 0x 1 0x3d
Gi0/ 2 SA 61440 00 d0.f800.0 001 0x3 0x 2 0x3d
Gi0/ 3 SA 61440 00 d0.f800.0 001 0x3 0x 3 0x3d
```

##### 配置举例

######  配置 LACP

【网络环境】

【配置方法】

+ 在SwitchA上设置LACP系统优先级为 4096 。 

+ 在SwitchA上的端口GigabitEthernet1/1和GigabitEthernet1/2上启用动态链路聚合协议，将其加入到LACP 3中。

+ 在SwitchB上设置LACP系统优先级为 61440 。

+ 在SwitchB上的端口GigabitEthernet2/1和GigabitEthernet2/2启用动态链路聚合协议，将其加入到LACP 3中。

  ```
  SwitchA 
  SwitchA# configure terminal
  SwitchA(config)# lacp system-priority 4096
  SwitchA(config)# interface range GigabitEthernet 1 /1- 2
  SwitchA(config-if-range)# port-group 3 mode active
  SwitchA(config-if-range)# end
  
  
  SwitchB 
  SwitchB# configure terminal
  SwitchB(config)# lacp system-priority 61440
  SwitchB(config)# interface range GigabitEthernet 2 /1- 2
  SwitchB(config-if-range)# port-group 3 mode active
  SwitchB(config-if-range)# end
  ```

  

【检验方法】 

+ 通过show lacp summary 3 查看LACP和成员口的对应关系是否正确。



#### 3.4.3 配置 AP 的 LinkTrap 功能

##### 配置效果

当聚合链路发生变化时，系统会发出相应的LinkTrap通告

配置方法

######  配置 AP口 的 LinkTrap

+ 在接口模式下配置。为可选配置。AP口的LinkTrap通告功能默认开启， 在此情况下，AP口的链路状态或者协议状态
  发生变化时，设备会发出LinkTrap通告；当不需要要该AP口的LinkTrap通告时，配置关闭该功能。

+ 可在所有支持AP功能的设备上配置该功能。

【命令格式】 snmp trap link-status
【参数说明】 -^
【缺省配置】 LinkTrap通告默认开启
【命令模式】 AP接口配置模式
【使用指导】 在接口模式下，用户可以对指定的AP口设置是否发送LinkTrap通告功能。当该功能打开，AP口发生Link状态变化时将发出LinkTrap通告，反之则不发。缺省情况下，该功能是打开的。用户可以在指定AP口的接口模式下，通过配置no snmp trap link-status命令关闭指定AP口的LinkTrap通告功能。AP 成员口不支持在端口模式下打开LinkTrap通告功能。需要通过下面的配置，即在全局模式下配置aggregateport member linktrap命令来打开AP成员口的LinkTrap通告功能。

######  配置 AP成员口 的 LinkTrap

+ 为可选配置。成员口LinkTrap默认关闭，当需要使能成员口的LinkTrap通告功能时，配置开启。

+ 可在所有支持AP功能的设备上配置该功能。

【命令格式】 aggregateport member linktrap
【参数说明】 -
【缺省配置】 缺省情况下，AP成员口的LinkTrap通告功能是关闭的。
【命令模式】 全局配置模式
【使用指导】 用户可以在全局配置模式下，通过配置aggregateport member linktrap命令打开所有AP成员口的LinkTrap通告功能。默认情况下，AP成员口不发送LinkTrap通告。用户可以在全局配置模式下，通过配置no aggregateport member linktrap命令关闭所有AP成员口的LinkTrap通告功能。

##### 检验方法

+ 通过show running命令查看相应的配置。

+ 打开LinkTrap通告的情况下，通过MIB软件可以监控到AP口或成员口的LinkTrap通告。

##### 配置举例

######  配置AP的LinkTrap功能

【配置方法】 

+ 将SwitchA上的端口GigabitEthernet 1 /1和GigabitEthernet 1 / 2 加入到静态AP 3中。
+ 将SwitchB上的端口GigabitEthernet 2 /1和GigabitEthernet 2 / 2 加入到静态AP 3中。
+ 在SwitchA上配置关闭AP 3的LinkTrap功能，同时打开成员口的LinkTrap功能。
+ 在SwitchB上配置关闭AP 3的LinkTrap功能，同时打开成员口的LinkTrap功能。

```
SwitchA 
SwitchA# configure terminal
SwitchA(config)# interface range GigabitEthernet 1 /1- 2
SwitchA(config-if-range)# port-group 3
SwitchA(config-if-range)# exit
SwitchA(config)# aggregateport member linktrap
SwitchA(config)# interface Aggregateport 3
SwitchA(config-if-AggregatePort 3)# no snmp trap link-status
```

```
SwitchB SwitchB# configure terminal
SwitchB(config)# interface range GigabitEthernet 2 /1- 2
SwitchB(config-if-range)# port-group 3
SwitchB(config-if-range)# exit
SwitchB(config)# aggregateport member linktrap
SwitchB(config)# interface Aggregateport 3
SwitchB(config-if-AggregatePort 3)# no snmp trap link-status
```

【检验方法】 

+ 通过show running查看AP的流量均衡算法配置是否正确。

```
SwitchA 
SwitchA# show run | include AggregatePort 3
Building configuration...
Current configuration: 54 bytes
interface AggregatePort 3
no snmp trap link-status
SwitchA# show run | include AggregatePort
aggregateport member linktrap

SwitchB 
SwitchB# show run | include AggregatePort 3
Building configuration...
Current configuration: 54 bytes
interface AggregatePort 3
no snmp trap link-status
SwitchB# show run | include AggregatePort
aggregateport member linktrap
```



#### 3.4.4 配置流量平衡模式

##### 配置效果

+ 系统会根据指定的流量平衡算法，对输入报文进行流量分配。同一报文流将固定通过同一条链路输出，不同报文流将平均分配到各个链路。在增强模式下，设备先判断发送报文的类型，然后根据指定报文的字段进行流量均衡。比如，源IP变化的IPv4报文要从AP口输出，那么AP会根据用户指定的IPv4报文字段src-ip进行流量均衡。

+ 增强模式下配置哈希扰动因子，同类型的两台设备相同报文会均衡到不同的链路上。

+ 增强模式下配置哈希扰动因子，同类型的两台设备相同报文会均衡到不同的链路上。

+ 增强模式下配置同步哈希因子使能，同类型报文流上行流量和下行流量固定从同一条链路输出。比如，基于源和目的ip地址均衡策略，使能同步哈希ipv4因子，同一条IPv4流上下行数据流路径一致。

+ 配置弹性哈希使能，将AP成员口失效链路流量将二次均衡到活动链路上，不影响其他活动链路上原来的数据流。

##### 注意事项

+ 不同的扰动因子计算扰动效果可能一样。

+ 同步哈希因子ipv4、ipv6、fcoe默认开启还是关闭根据不同产品而定，用户根据需求关闭或开启。

+ 弹性哈希支持全局模式和AP口接口模式下配置。

##### 配置方法

######  设置 AP 的全局流量平衡算法

+ 为可选配置，当需要改变AP的流量平衡算法以实现更好的流量均衡时，需要配置该功能。

+ 可在所有支持AP功能的设备上配置该功能。

【命令格式】 aggregateport load-balance { dst-mac | src-mac | src-dst-mac | dst-ip | src-ip | src-dst-ip |
src-dst-ip-l4port | enhanced profile profile-name}
【参数说明】 dst-mac：根据输入报文的目的MAC地址进行流量分配。
src-mac：根据输入报文的源MAC地址进行流量分配。
src-dst-ip：根据源IP与目的IP进行流量分配。
dst-ip：根据输入报文的目的IP地址进行流量分配。
src-ip：根据输入报文的源IP地址进行流量分配。
src-dst-mac：根据源MAC与目的MAC进行流量分配。
src-dst-ip-l4port(在接口模式下不支持，全局模式下支持)：根据源IP与目的IP和L4源端口号与L4目的端口号进行流量分配。
enhanced profile profile-name：根据增强模式模板profile-name设置对应的报文类型字段进行流量分配。
【缺省配置】 AP的流量均衡模式为基于源和目的MAC(如交换机产品系列)或者基于源和目的IP(如网关产品系列)的流量均衡方式或为基于增强模式模板的流量均衡(如使用CB线卡的交换机设备)。
【命令模式】 全局配置模式
【使用指导】 要将AP的流量平衡设置恢复到缺省值，可以在全局配置模式下使用no aggregateport load-balance命令。在某些支持基于指定AP口配置流量平衡算法的产品上，上述的流量平衡算法配置命令也可以进入AP口的接口模式下进行配置，配置生效后，该AP口上就会以新配置的流量平衡算法进行工作。同样的，在这些产品下面，用户可以在AP口的接口模式下使用no aggregateport load-balance命令使该AP口下配置的流量平衡算法失效，进而生效为当前设备上生效的AP全局流量平衡算法。

在支持基于AP口配置流量均衡的产品上，aggregateport load-balance^ 还支持在AP口接口模式下进行配置。



######  重命名增强模式模板

+ 在默认情况下，对于支持增强型流量均衡功能的设备，系统会创建一个名字为default的增强模式模板，当需要改变增强模板名字或把当前增强模式模板恢复为默认配置时可以使用该功能。其他情况下，该配置为可选配置。

+ 可在汇聚或者核心交换机等支持增强型流量均衡功能的设备上配置该功能。

【命令格式】 load-balance-profile profile-name^
【参数说明】 profile-name：模板名称。支持最多 31 个字符。
【缺省配置】 默认增强模式模板的名字为default
【命令模式】 全局配置模式
【使用指导】 可以通过load-balance-profile default 进入默认模板模式，重新命名增强模式模板的名字可以通过load-balance-profile profile-nam来实现，把名字恢复为default 可以在全局配置模式下使用default load-balance-profile ， 把当前增强模式模板下所有报文流量的均衡配置恢复为默认配置，可以在全局配置模式下使用default load-balance-profile profile-name命令。
全局只支持一个模板,不允许配置删除，使用show load-balance-profile 查看目前的配置。

######  配置二层报文流量均衡模式

+ 为可选配置。当采用增强型模板模板配置作为AP的流量均衡方式时，可以根据网络的流量特征配置适当配置该功能，以实现更优的流量均衡。

+ 可在汇聚或者核心交换机等支持增强型流量均衡功能的设备上配置该功能。

【命令格式】 l2 field { [ src-mac ] [dst-mac ] [l2-protocol ] [vlan ] [ src-port ] }
【参数说明】 src-mac：根据输入二层的报文的源MAC地址进行流量分配。
dst-mac：根据输入二层的报文的目的MAC地址进行流量分配。
l 2 - protocol ： 根据输入二层的报文的二层协议类型进行流量分配。
vlan：根据输入二层的报文的vlan值进行流量分配。
src-port：根据输入二层报文的面板端口进行流量分配。
【缺省配置】 缺省模式下，二层报文负载均衡方式为src-mac、dst-mac、vlan。
【命令模式】 profile配置模式
【使用指导】 配置指定增强模板中二层报文的负载均衡方式。缺省为src-mac、dst-mac、vlan。要将二层报文的流量平衡设置恢复到缺省值，可以在该模式下使用no l2 field命令。

######  配置 IPv 4 报文流量均衡模式

+ 为可选配置。

+ 需要修改IPv4报文均衡方式时，在增强型模板配置模式下进行配置。

+ 可在汇聚或者核心交换机等支持增强型流量均衡功能的设备上配置该功能。

【命令格式】 ipv4 field { [ src-ip ] [ dst-ip ] [ protocol ] [ l4-src-port ] [ l4-dst-port ] [ src-port ] }
【参数说明】 src-ip：根据输入IPv4报文的源IP地址进行流量分配。
dst-ip：根据输入IPv4报文的目的IP地址进行流量分配。
protocol：根据输入的IPv4报文的协议类型进行流量分配。

l4-src-port：根据输入的IPv4报文的L4层的源端口号进行流量分配。
l4 - dst-port： 根据输入的IPv4报文的L4层的目的端口号进行流量分配。
src-port：根据输入IPv4报文的源端口号进行流量分配。
缺省配置】 缺省模式下，IPv4报文负载均衡方式为src-ip、dst-ip。
【命令模式】 profile配置模式
【使用指导】 配置指定增强模板中IPv4报文的负载均衡方式。缺省为src-ip、dst-ip。要将IPv 4 报文的流量平衡设置恢复到缺省值，可以在该模式下使用no ipv4 field命令。

######  配置 IPv 6 报文流量均衡模式

+ 可选配置。

+ 需要修改IPv6报文均衡方式时，在增强型模板配置模式下进行配置。

+ 可在汇聚或者核心交换机等支持IPv6流量均衡功能的设备上配置该功能。

【命令格式】 ipv6 field {[ src-ip ] [ dst-ip ] [ protocol ] [ l4-src-port ] [ l4-dst-port] [ src-port ]}
【参数说明】 src-ip：根据输入IPv6报文的源IP地址进行流量分配。
dst-ip：根据输入IPv6报文的目的IP地址进行流量分配。
protocol：根据输入的IPv6报文的协议类型进行流量分配。
l4-src-port：根据输入的IPv6报文的L 4 层的源端口号进行流量分配。
l4 - dst-port：根据输入的IPv6报文的L 4 层的目的端口号进行流量分配。
src-port：根据输入IPv6报文的源端口号进行流量分配。
【缺省配置】 缺省模式下，IPv6报文负载均衡方式为src-ip、dst-ip 。
【命令模式】 profile配置模式
【使用指导】 配置指定增强模板中IPv6报文的负载均衡方式。缺省为src-ip、dst-ip。
要将IPv 6 报文的流量平衡设置恢复到缺省值，可以在该模式下使用no ipv6 field命令。

######  配置 MPLS 报文流量均衡模式

+ 可选配置。

+ 需要修改MPLS报文均衡方式时，在增强型模板配置模式下进行配置。

+ 可在汇聚或者核心交换机等支持MPLS报文流量均衡功能的设备上配置该功能。

【命令格式】 mpls field { [ top-label ] [ 2nd-label ] [ src-ip ] [ dst-ip ] [ vlan ] [ src-port ]
【参数说明】 src-ip：根据输入MPLS报文的源IP地址进行流量分配。
dst-ip：根据输入MPLS报文的目的IP地址进行流量分配。
top-label：根据输入MPLS报文的目的top-label进行流量分配。
2nd-label：根据输入MPLS报文的目的2nd-label进行流量分配。
vlan：根据输入MPLS报文的VLAN值进行流量分配。
src-port：根据输入MPLS报文的源端口号进行流量分配。
【缺省配置】 缺省模式下，MPLS报文负载均衡方式为top-label 、 2nd-label 。
【命令模式】 profile配置模式
【使用指导】 配置指定增强模板中MPLS报文的负载均衡方式。缺省为top-label、2nd-label。
要将MPLS报文的流量平衡设置恢复到缺省值，可以在该模式下使用no mpls field命令。

增强模式中MPLS均衡算法只对MPLS L3 VPN报文生效，对MPLS L2 VPN报文无效。

######  配置 TRILL 报文流量均衡模式

+ 可选配置。

+ 需要修改TRILL报文均衡方式时，在增强型模板配置模式下进行配置。

+ 可在汇聚或者核心交换机等支持TRILL报文流量均衡功能的设备上配置该功能。

【命令格式】 trill field { [vlan] [src-mac] [dst-mac]
【参数说明】 vlan：根据输入TRILL报文的VLAN值进行流量分配
src-mac：根据输入TRILL报文的源MAC地址进行流量分配。
dst-mac：根据输入TRILL报文的目的MAC地址进行流量分配。
【缺省配置】 缺省模式下，TRILL报文负载均衡方式为src-mac、dst-mac、vlan 。
【命令模式】 profile配置模式
【使用指导】 配置指定增强模板中TRILL报文的负载均衡方式。缺省为src-mac、dst-mac、 vlan。
要将TRILL报文的流量平衡设置恢复到缺省值，可以在该模式下使用no trill field命令。

TRILLTransit RBridge报文可均衡的字段包括：ing-nick、egr-nick、src-mac、dst-mac、vlan、l2-etype。

TRILL Egress RBridge报文可均衡的字段包括：
L2报文：src-mac、dst-mac、vlan、l2- protocol
L3报文：src-ip、dst-ip、l4-src-port、l 4 - dst-port、protocol、vlan

src-port、dst-port使用于所有TRILL Transit RBridge和TRILL Egress RBridge报文。^

######  配置 FCOE 报文流量均衡模式

+ 可选配置。

+ 需要修改FCOE报文均衡方式时，在增强型模板配置模式下进行配置。

+ 可在汇聚或者核心交换机等支持FCOE报文流量均衡功能的设备上配置该功能。

【命令格式】 fcoe field { [src-id] [dst-id] [ox-id]}^
【参数说明】 src-id：根据FCOE报文的source ID进行流量分配。
dst-id：根据FCOE报文的destination ID进行流量分配。
ox-id：根据FCOE报文的Originator Exchange ID进行流量分配。
【缺省配置】 在缺省模式下，FCOE报文负载均衡方式为src-id 、 dst-id 、 ox-id 。
【命令模式】 profile配置模式
【使用指导】 配置指定增强模板中FCOE报文的负载均衡方式。缺省为：src-id 、 dst-id 、 ox-id 。
要将FCOE报文的流量平衡设置恢复到缺省值，可以在该模式下使用no fcoe field命令。

######  配置哈希扰动因子

+ 可选配置，同类型设备需要指定AP口均衡相同类型报文时配置。

【命令格式】 hash-disturb string
【参数说明】 String:用于计算哈希扰动因子的字符串
【缺省配置】 缺省情况下，没有设置扰动
【命令模式】 profile配置模式
【使用指导】 当不需要扰动AP口流量时，使用no hash-disturb，回复默认当前流量均衡方式。

######  配置关闭或使能同步哈希因子

+ 可选配置，当需要指定报文类型上行流量和下行流量走同一条路径时配置。

【命令格式】 hash-symmetrical {ipv4 | ipv6 }
【参数说明】 ipv4：使能ipv4报文开启同步哈希流量均衡功能。
ipv6：使能ipv6报文开启同步哈希流量均衡功能。
【缺省配置】 同步哈希因子功能缺省值根据不同产品而定
【命令模式】 profile配置模式
【使用指导】 在缺省开启同步哈希的产品上，当不需要指定报文上下行流量走同一路径时，使用no命令关闭。

**检验方法**

+ 通过show running命令查看相应的配置。

+ 通过show aggregateport load-balance命令查看AP流量平衡算法的配置情况, 在支持基于AP口配置流量均衡的产品上，可以通过show aggregateport summary来查看某个AP口上生效的流量均衡。

+ 通过show load-balance-profile命令查看增强模式模板的设置情况。

【命令格式】 show aggregateport aggregate-port-number [ load-balance | summary ]
【参数说明】 aggregate-port-number ： AP接口号
load-balance ： 显示AP的流量平衡算法
summary ： 显示AP中的每条链路的摘要信息
【命令模式】 各模式均可执行
【使用指导】 如果没有指定AP接口号，则所有AP的信息将被显示出来

【命令展示】 

```
Ruijie# show aggregateport 1 summary
AggregatePort MaxPorts SwitchPort Mode Load balance Ports

------------- --------------- ---------- ------ ----------------------------

------------------------

Ag1 8 Enabled ACCESS dst-mac Gi0/2
```

【命令格式】 show load-balance-profile [ profile-name ]
【参数说明】 profile-name：模板名称
【命令模式】 各模式均可执行
【使用指导】 如果没有指定profile-name，则所有增强模式模板的信息将被显示出来。
【命令展示】

```
 Ruijie# show load-balance-profile module0
Load-balance-profile: module0
Packet Hash Field:
IPv 4 : src-ip dst-ip
IPv 6 : src-ip dst-ip
L 2 : src-mac dst-mac vlan
MPLS: top-labe l2nd-label
```

##### 配置举例

######  配置流量平衡模式

【配置方法】 

+ 将SwitchA上的端口GigabitEthernet 1 /1和GigabitEthernet 1 / 2 加入到静态AP 3中。

+ 将SwitchB上的端口GigabitEthernet 2 /1和GigabitEthernet 2 / 2 加入到静态AP 3中。

+ 在SwitchA上配置全局的AP流量均衡模式为基于源MAC地址的流量均衡方式。

+ 在SwitchB上配置全局的AP流量均衡模式为基于目的MAC地址的流量均衡方式。

  ```
  SwitchA 
  SwitchA# configure terminal^
  SwitchA(config)# interface range GigabitEthernet 1 /1- 2
  SwitchA(config-if-range)# port-group 3
  SwitchA(config-if-range)# exit
  SwitchA(config)# aggregateport load-balance src-mac
  ```

  ```
  SwitchB 
  SwitchB# configure terminal
  SwitchB(config)# interface range GigabitEthernet 2 /1- 2
  SwitchB(config-if-range)# port-group 3
  SwitchB(config-if-range)# exit
  SwitchB(config)# aggregateport load-balance dst-mac
  ```

【检验方法】 

+ 通过show aggregateport load-balance查看AP的流量均衡算法配置是否正确。

  ```
  SwitchA 
  SwitchA# show aggregatePort load-balance
  Load-balance : Source MAC
  SwitchB 
  SwitchB# show aggregatePort load-balance
  Load-balance : Destination MAC
  ```

######  配置哈希流量均衡控制

【配置方法】 
 将SwitchA上的端口GigabitEthernet 1 /1和GigabitEthernet 1 / 2 加入到静态AP 3中。
 将SwitchB上的端口GigabitEthernet 2 /1和GigabitEthernet 2 / 2 加入到静态AP 3中。
 在SwitchA上配置关闭使能同步哈希因子fcoe。
 在SwitchB上配置关闭使能同步哈希因子fcoe。
 在SwitchA上配置哈希扰动因子A。
 在SwitchB上配置哈希扰动因子B。

```
SwitchA 
SwitchA# configure terminal
SwitchA(config)# interface range GigabitEthernet 1 /1- 2
SwitchA(config-if-range)# port-group 3
SwitchA(config-if-range)# exit
SwitchA(config)#load-balance-profile
SwitchA(config-load-balance-profile)#no hash-symmetrical fcoe
SwitchA(config-load-balance-profile)#hash-disturb A
```

```
SwitchB 
SwitchB# configure terminal
SwitchB(config)# interface range GigabitEthernet 2 /1- 2
SwitchB(config-if-range)# port-group 3
SwitchB(config-if-range)# exit
SwitchB(config)#load-balance-profile
SwitchB(config-load-balance-profile)# no hash-symmetrical fcoe
SwitchA(config-load-balance-profile)#hash-disturb B
```

【检验方法】

+ 通过show running查看配置是否正确。

##### 常见错误

用户配置了使能同步哈希因子ipv4、ipv6，show running发现没有显示配置，原因是某些产品同步哈希功能默认开启，关闭功能时显示。

#### 3.4.5 配置 AP 的容量模式

##### 配置效果

+ 改变当前系统支持的最大可配置AP口数和单个AP口下最大可配置成员口数。

##### 注意事项

+ 默认配置下，系统有一个默认的AP容量模式，可以通过show aggregateport capacity命令查看当前容量模式。

+ 配置容量模式时，当系统中已经存在的最大AP号或者某个AP下成员口数量超过了要配置的容量值，则容量模式配置会失败。

##### 配置方法

######  配置 AP 容量模式

+ 为可选配置，当需要改变当前系统AP的容量值时配置，以适应网络部署中AP的个数或者每个AP口允许聚合的成员口个数的变化需求。

+ 可在核心交换机等支持改变AP容量功能的设备上配置该功能。

【命令格式】 aggregateport capacity mode capacity-mode
【参数说明】 capacity-mode： 模式选项
【缺省配置】 缺省情况下，AP的容量模式随着不同的产品系列而不同，比如有256*16(其中， 256 代表设备支持的最大AP口个数， 16 代表每个AP口支持的最大成员口个数)等容量模式。
【命令模式】 全局配置模式
【使用指导】 在支持容量模式配置的产品中，系统会提供几种可配置的容量模式供用户选择，在全局配置模式下，用户可以通过aggregateport capacity mode capacity-mode配置命令来选择需要的容量模式。用户可以在全局配置模式下，通过no aggregateport capacity mode 将容量模式恢复为默认值。

##### 检验方法

+ 通过show running命令查看相应的配置。

+ 通过show aggregateport capacity命令查看当前AP容量模式以及AP口容量使用情况。

【命令格式】 show aggregateport capacity
【参数说明】 -
【命令模式】 各模式均可执行
【使用指导】 -
【命令展示】 

```
Ruijie# show aggregateport capacity
AggregatePort Capacity Information:
Configuration Capacity Mode: 128*16.
Effective Capacity Mode : 256*8.
Available Capacity : 128 * 8.
Total Number: 128 , Used: 1 , Available: 127.
```

##### 配置举例

######  配置 AP 的容量模式

【配置方法】 

+ 将SwitchA上的端口GigabitEthernet 1 /1和GigabitEthernet 1 / 2 加入到静态AP 3中。

+ 将SwitchB上的端口GigabitEthernet 2 /1和GigabitEthernet 2 / 2 加入到静态AP 3中。

+ 将SwitchA上的AP容量模式配置为128*128模式。

+ 将SwitchB上的AP容量模式配置为256 * 64模式。

  ```
  SwitchA SwitchA# configure terminal
  SwitchA(config)# interface range GigabitEthernet 1 /1- 2
  SwitchA(config-if-range)# port-group 3
  SwitchA(config-if-range)# exit
  SwitchA(config)# aggregateport capacity mode 128*128
  ```

  ```
  SwitchB SwitchB# configure terminal
  SwitchB(config)# interface range GigabitEthernet 2 /1- 2
  SwitchB(config-if-range)# port-group 3
  SwitchB(config-if-range)# exit
  SwitchB(config)# aggregateport capacity mode 256 * 64
  ```

【检验方法】  通过show aggregateport capacity查看AP的容量模式是否正确。

```
SwitchA 
SwitchA# show aggregatePort capacity
AggregatePort Capacity Information:
Configuration Capacity Mode: 128 * 128.
Effective Capacity Mode ： 128 * 128.
Available Capacity Mode ： 128 * 128.
Total Number : 128 , Used: 1 , Available: 127.
```

```
SwitchB 
SwitchB# show aggregatePort capacity
AggregatePort Capacity Information:
Configuration Capacity Mode: 256 * 64.
Effective Capacity Mode ： 256 * 64.
Available Capacity Mode ： 256 * 64.
Total Number : 256 , Used: 1 , Available: 255.
```

#### 3.4.6 配置 AP 下成员口开启 BFD 检测

##### 配置效果

+ 指定AP下所有成员口都开启BFD检测。

+ AP上配置BFD检测后，每个成员口独立进行BFD检测，根据检测结果决定AP口的报文是否往该成员口均衡。当BFD检测Down时，AP口的报文不会往该口均衡；当BFD重新检测UP的时候，AP口的报文才往该口均衡。

##### 注意事项

+ AP口开启BFD检测，仅仅是创建BFD检测会话，要让会话生效还需要配置BFD检测参数，BFD检测参数配置参见BFD配置指南。

+ 不支持AP下单个成员口配置开启关闭BFD检测，配置开启关闭BFD检测基于整个AP组。

+ 只有处于转发状态的成员口才会启动BFD会话检测，成员口由于链路Down或者Lacp协议Down等原因处于非转发状态时，该成员口上BFD会话自动删除。

+ AP口内剩下最后一个可用成员口（即处于转发状态的成员口）时，此时AP口报文只能往该成员口均衡，因此BFD检测自动失效，可用成员口数量大于等于 2 个时，BFD检测重新生效。

##### 配置方法

######  配置 AP 成员口开启 BFD 检测

+ 为可选配置，当需要能快速检测（毫秒级别）成员口通路故障时，启用该功能。以便某个成员口通路发生故障时，AP口流量能迅速切换到另外成员口。

+ 可在支持AP与BFD联动的设备上配置该功能。

【命令格式】 aggregate bfd-detect {ipv4} src_ip dst_ip
【参数说明】 ipv4 ：开启ipv4 BFD检测，AP口上使用ipv4地址时可选择开启ipv4 BFD检测
src_ip： 源IP地址，即AP口上所配置的IP地址
dst_ip：目的IP地址，即对端AP口上所配置的IP地址
【缺省配置】 缺省情况下，AP口BFD检测功能关闭。
【命令模式】 AP口接口模式
【使用指导】 1. 还需要配置相应的BFD检测参数才能生效，参见BFD配置指南。
2.在AP口上配置该AP组开启BFD检测功能，AP口内处于转发状态的成员就会自动创建BFD会话进行检测。

##### 检验方法

+ 通过show running命令查看相应的配置

+ 通过show interface aggregateport 命令查看当前AP下成员口BFD检测状态。

【命令格式】 show interface aggregateport ap-num
【参数说明】 ap-num： AP号
【命令模式】 各模式均可执行
【使用指导】 -
【命令展示】

```
 Ruijie# show interface aggregateport 11
...
Aggregate Port Informations:
Aggregate Number: 11
Name: “AggregatePort 11”
Members: (count=2)
GigabitEthernet 0/ 1 Link Status: Up Lacp Status: bndl BFD Status: UP
GigabitEthernet 0/ 2 Link Status: Up Lacp Status: susp BFD Status: Invalid
...
```

##### 配置举例

######  配置 AP 成员口开启 BFD IPv4 检测

【配置方法】 

+ 将SwitchA上的端口GigabitEthernet 1 /1和GigabitEthernet 1 / 2 开启LACP，加入到LACP AP 3中。
+ 将SwitchB上的端口GigabitEthernet 2 /1和GigabitEthernet 2 / 2 开启LACP，加入到LACP AP 3中。
+ 将SwitchA上的AP 3配置IP地址1.0.0.1，并开启IPv4 BFD检测。
+ 将SwitchB上的AP 3配置IP地址1.0.0.2，并开启IPv4 BFD检测。

```
SwitchA 
SwitchA# configure terminal
SwitchA(config)# interface range GigabitEthernet 1 /1- 2
SwitchA(config-if-range)# no switchport
SwitchA(config-if-range)# port-group 3 mode active
SwitchA(config-if-range)# exit
SwitchA(config)# interface aggregateport 3
SwitchA(config-if-Aggregateport 3 )# ip address 1.0.0.1
SwitchA(config-if-Aggregateport 3 )# aggregate bfd-detect ipv4 1.0.0.1 1.0.0.2
SwitchA(config-if-Aggregateport 3 )# bfd interval 50 min_rx 50 multiplier 3
```

```
SwitchB 
SwitchB# configure terminal
SwitchB(config)# interface range GigabitEthernet 1 /1- 2
SwitchB(config-if-range)# no switchport
SwitchB(config-if-range)# port-group 3 mode active
SwitchB(config-if-range)# exit
SwitchB(config)# interface aggregateport 3
SwitchB(config-if-Aggregateport 3 )# ip address 1.0.0.2
SwitchB(config-if-Aggregateport 3 )# aggregate bfd-detect ipv4 1.0.0.2 1.0.0.1
SwitchB(config-if-Aggregateport 3 )# bfd interval 50 min_rx 50 multiplier 3
```

【检验方法】 

+ 通过show run查看配置是否正确。
+ 通过show interface aggregateport 查看AP口下每个成员口BFD状态。

```
SwitchA
SwitchA#^ show run | include AggregatePort 3^
Building configuration...
Current configuration: 54 bytes
interface AggregatePort 3
no switchport
ip address 1.0.0.1
aggregate bfd-detect ipv4 1.0.0.1 1.0.0.2
bfd interval 50 min_rx 50 multiplier 3
SwitchA# show interface aggregateport 3
...
Aggregate Port Informations:
Aggregate Number: 3
Nam“: "AggregatePor” 3 "
Members: (count=2)
GigabitEthernet 1 /1 Link Status: Up Lacp Status: bndl BFD Status: UP
GigabitEthernet 1 / 2 Link Status: Up Lacp Status: bndl BFD Status: UP
...

SwitchB 
SwitchB# show run | include AggregatePort 3
Building configuration...
Current configuration: 54 bytes
interface AggregatePort 3
no switchport
ip address 1.0.0.2
aggregate bfd-detect ipv4 1.0.0.2 1.0.0.1

bfd interval 50 min_rx 50 multiplier 3
SwitchB# show interface aggregateport 3
...
Aggregate Port Informations:
Aggregate Number: 3
Nam“: "AggregatePor” 3 "
Members: (count=2)
GigabitEthernet 1 /1 Link Status: Up Lacp Status: bndl BFD Status: UP
GigabitEthernet 1 / 2 Link Status: Up Lacp Status: bndl BFD Status: UP
...
```

##### 常见错误

1. 配置了AP口开启BFD检测，但没有配置BFD检测参数，这时候BFD没有真正生效。
2. AP口上开启BFD检测，BFD检测邻居必须是直连的对端AP，中间不能跨设备，且对端也需要开启BFD检测。

#### 3.4.7 配置 LACP 独立口功能

##### 配置效果

+ 配置使能LACP独立口功能后，当LACP成员口在独立口超时时间内没有收到LACP协议报文时，将自动转换为普通物理口，成员口的状态变成individual状态，可以正常参与报文转发。

+ 当该普通口重新收到LACP协议报文时，重新转换为LACP独立口，正常进行LACP报文协商。

+ 可以通过配置来调整独立口超时的时间。

**注意事项**

+ 使能LACP独立口功能，不会立即转换为普通物理口，当成员口在独立口超时时间内没有收到LACP协议报文，此时该成员口进入独立口状态(转换成普通物理口)；

+ LACP独立口超时时间的配置仅会影响还未变成独立口的LACP成员口。配置超时时间后，会重新开始计算超时时间。

+ 长超时模式时，LACP报文的周期发包为30s，配置独立口超时时间需要大于30s，以免影响到正常的LACP协商。建议配置的LACP独立口超时时间至少为发包周期的 2 倍。短超时模式，没有限制。

##### 配置方法

######  配置使能 LACP 独立口

+ 可选配置，当需要指定某个LACP成员口不能进行动态协商聚合时，其成员口可以正常参与报文转发时配置。

【命令格式】 lacp individual-port enable
【参数说明】 -
【缺省配置】 缺省情况下，关闭使能LACP独立口功能。
【命令模式】 接口模式
【使用指导】 -

######  配置 LACP 独立口的超时时间

+ 可选配置，当需要调整LACP独立口功能的独立口超时时间时配置。

【命令格式】 lacp individual-timeout^ period time^
【参数说明】 time：超时时间，配置范围 10 - 90 ，单位s
【缺省配置】 缺省情况下，LACP独立口超时时间为90s。
【命令模式】 全局模式
【使用指导】 -

##### 检验方法

+ 通过show running命令查看相应的配置。

+ 通过show interface aggregateport 命令查看当前AP下成员口状态。

【命令格式】 show interface aggregateport ap-num
【参数说明】 ap-num： AP号
【命令模式】 任意模式
【使用指导】 -^
【命令展示】 

```
Ruijie# show interface aggregateport 3
...
Aggregate Port Informations:
Aggregate Number: 3
Nam“: "AggregatePor” 3 "
Members: (count=2)
GigabitEthernet 0/ 1 Link Status: Up Lacp Status: individual
GigabitEthernet 0/ 2 Link Status: Up Lacp Status: individual
...
```

##### 配置举例

######  配置使能 LACP 独立口功能


配置指南 Aggregate Port

【场景描述】 双网卡服务器使用网卡 1 和网卡 2 做通讯口，接入到接入设备Gigabitethernet1/1和
Gigabitethernet1/ 2 。Gigabitethernet1/1和Gigabitethernet1/ 2 加入LACP聚合组，比如AP3，划分特定的VLAN，比如VLAN 10。Gigabitethernet1/1和Gigabitethernet1/ 2 使能LACP独立口功能。服务器启机未安装系统，与接入设备LACP协商失败，接入设备Gigabitethernet1/1和Gigabitethernet1/ 2 转换成普通物理口，自动划分进VLAN 10 ，服务器使用网卡 1 或网卡 2 与远程装机设备通信。装机结束后，服务器重新启用LACP方式接入到接入设备。

【配置方法】

 + 将接入设备上的端口GigabitEthernet 1 /1和GigabitEthernet 1 / 2 开启LACP，加入到LACP AP 3中。

+ 将接入设备上的端口GigabitEthernet 1 /1和GigabitEthernet 1 / 2 配置使能LACP独立口功能
+ 将接入设备上的AP3划分VLAN10。

```
SwitchA 
SwitchA# configure terminal
SwitchA(config)# interface range GigabitEthernet 1 /1- 2
SwitchA(config-if-range)# port-group 3 mode active
SwitchA(config-if-range)# lacp individual-port enable
SwitchA(config-if-range)# exit
SwitchA(config)# interface aggregateport 3
SwitchA(config-if-Aggregateport 3 )#switch access vlan 10
SwitchA(config-if-Aggregateport 3 )#
```

【检验方法】 

+ 通过show run查看配置是否正确。

+ 通过show lacp summery 查看AP口下每个成员口聚合状态。

```
SwitchA 
SwitchA# show LACP summary 3
System Id:32768, 00d0.f8fb. 0001
Flags: –S - Device is requesting Slow LACPDUs
F - Device is requesting Fast LACPDUs.–A - Device is in active mode. –P - Device is in
passive mode.
Aggregate port 3:
Local information:
LACP port Oper Port Port
Port Flags State Priority Key Number Sta--
Gi 1 / 1 SA individual 32768 0x3 0x 1 0x3d
Gi 1 / 2 SA individual 32768 0x3 0x 2 0x3d
Partner informat ion:
LACP port Oper Port Port
Port Flags Priority Dev ID Key Number Sta--
Gi 1 / 1 SA 32768 00 d0.f800.0 002 0x3 0x 1 0x3d
Gi 1 / 2 SA 32768 00 d0.f800.0 002 0x3 0x 2 0x3d
```



### 3.5 监视与维护

##### 查看运行情况

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>显示增强模式模板的设置。</td>         <td>show load-balance-profile [ profile-name ]</td>     </tr>     <tr>         <td>查看 LACP 的链路聚合状态，可指定显示特定聚合组的信息，参数 key-numebr 表示 LACP 聚合组的 Id。</td>         <td>show lacp summary [ key-number ]</td>     </tr>     <tr>         <td>显示 AP 口摘要信息或流量平衡算法。</td>         <td>show aggregateport ap-number { load-balance | summary }</td>     </tr>     <tr>         <td>显示 AP 当前容量模式以及 AP 口容量使用情况</td>         <td>show aggregateport capacity</td>     </tr> </table>

##### 查看调试信息

输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。^

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>打开 AP 的调试开关。</td>         <td>debug lsm ap</td>     </tr>     <tr>         <td>打开 LACP 的调试开关。</td>         <td>Debug lacp { packet | event | database | ha | realtime | stm | timer | all}</td>     </tr> </table>

## 4 VLAN

### 4.1 概述

VLAN是虚拟局域网（Virtual Local Area Network）的简称，它是在一个物理网络上划分出来的逻辑网络。这个网络对应于ISO模型的第二层网络。

VLAN有着和普通物理网络同样的属性，除了没有物理位置的限制，它和普通局域网一样。第二层的单播、广播和多播帧在一个VLAN内转发、扩散，而不会直接进入其他的VLAN之中。

可以把一个端口定义为一个VLAN的成员，所有连接到这个特定端口的终端都是虚拟网络的一部分，并且整个网络可以支持多个VLAN。当在VLAN中增加、删除和修改用户的时候，不必从物理上调整网络配置。VLAN之间的通讯必须通过三层设备，



### 4.2 典型应用

<table>     <tr>         <th>典型应用</th>         <th>场景描述</th>     </tr>     <tr>         <td>VLAN 间二层隔离、三层互连</td>         <td>用户内网被划分为多个 VLAN，实现相互间的 2 层隔离， VLAN 间通过 3 层核心交换机的 IP 转发能力实现子网互连。</td>     </tr> </table>

#### 4.2.1 VLAN 间二层隔离、三层互连

##### 应用场景

某用户内网被划分为VLAN 10、VLAN 20、VLAN 30，以实现相互间的 2 层隔离； 3 个VLAN对应的IP子网分别为192.168.10.0/24、192.168.20.0/24、192.168.30.0/24， 3 个VLAN通过 3 层核心交换机的IP转发能力实现子网互连。

【注释】 

Switch A、Switch B、Switch C为接入交换机。
在核心交换机配置 3 个VLAN，配置下连接入交换机的端口为trunk口，并指定许可vlan列表，实现 2 层隔离；
在核心交换机配置 3 个SVI口，分别作为 3 个VLAN对应IP子网的网关接口，配置对应的IP地址；
分别在 3 台接入交换机创建VLAN，为各VLAN分配Access口，指定上连核心交换机的trunk口。

##### 功能部属

+ 在Intranet中通过划分多个 VLAN，实现VLAN间的二层隔离。

+ 三层交换设备中配置SVI接口，实现VLAN之间的三层通信。

### 4.3 功能详解

##### 基本概念

######  VLAN

VLAN是虚拟局域网（Virtual Local Area Network）的简称，它是在一个物理网络上划分出来的逻辑网络。VLAN有着和普通物理网络同样的属性，除了没有物理位置的限制，它和普通局域网一样。第二层的单播、广播和多播帧在一个VLAN内转发、扩散，而不会直接进入其他的VLAN之中。

产品支持的VLAN遵循IEEE802.1Q标准，最多支持^4094 个VLAN(VLAN ID 1-^4094 )，其中VLAN 1是不可删除的默认VLAN。
许可配置的VLAN ID范围为1 -4094 。
当硬件资源不足的情况下，系统将返回创建VLAN失败信息。^

######  VLAN 成员类型

可以通过配置一个端口的VLAN成员类型，来确定这个端口能通过怎样的帧，以及这个端口可以属于多少个VLAN。关于VLAN
成员类型的详细说明，请看下表：

<table>     <tr>         <th>端口类型</th>         <th>作用</th>     </tr>     <tr>         <td>Access 端口</td>         <td>一个 Access 端口，只能属于一个 VLAN，并且是通过手工设置指定 VLAN 的。</td>     </tr>     <tr>         <td>Trunk 端口 (802.1Q)</td>         <td>一个 Trunk 口，在缺省情况下是属于本设备所有 VLAN 的，它能够转发所有 VLAN 的帧，也可以通过设置许可 VLAN 列表(Allowed-VLANs)来加以限制。</td>     </tr>     <tr>         <td>Uplink 端口</td>         <td>一个 Uplink 口，在缺省情况下是属于本设备所有 VLAN 的，它能够转发所有 VLAN 的帧，并且以 tag 方式转发 native-vlan 的帧。</td>     </tr>     <tr>         <td>Hybrid 端口</td>         <td>一个 Hybrid 口，在缺省情况下是属于本设备所有 VLAN 的，它能够转发所有 VLAN 的帧，并允许以 untag 方式转发多个 VLAN 的帧，也可以通过设置许可 VLAN 列表(Allowed-VLANs)来加以限制。</td>     </tr>     <tr>         <td>Servicechain 端口</td>         <td>一个 Servicechain 端口，不学习 MAC 地址，且可以转发任何 VLAN 的报文；同时，该端口下不允许有其他配置。</td>     </tr> </table>



##### 功能特性

<table>     <tr>         <th>功能特性</th>         <th>作用</th>     </tr>     <tr>         <td>VLAN</td>         <td>划分的 VLAN 间二层隔离</td>     </tr> </table>

#### 4.3.1 VLAN

VLAN是虚拟局域网的简称，每个VLAN具备VLAN的独立广播域，不同的 VLAN之间是二层隔离的。

##### 工作原理

每个VLAN具备VLAN的独立广播域，不同的VLAN之间是二层隔离的。

VLAN的二层隔离：如果VLAN没有配置SVI，各个 VLAN之间是二层隔离的，即VLAN间的用户之间不能通信；

VLAN的三层互连：三层交换设备中如果VLAN配置SVI，各个 VLAN间能三层互连通信；




### 4.4 配置详解

<table>
  <thead>
    <tr>
      <th>配置项</th>
      <th colspan="2">配置建议 & 相关命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">配置基本VLAN。</td>
      <td colspan="2">必须配置。用于创建 VLAN，加入 ACCESS 模式接口。</td>
    </tr>
    <tr>
      <td>vlan</td>
      <td>输入一个VLAN ID。</td>
    </tr>
    <tr>
      <td colspan="2">可选配置。 配置 ACCESS 口，用于传输单个 VLAN 的信息。</td>
    </tr>
    <tr>
      <td>switchport mode access</td>
      <td>定义该接口的类型为二层 Access 口。</td>
    </tr>
    <tr>
      <td>switchport access vlan</td>
      <td>将这个接口分配给一个 vlan。</td>
    </tr>
    <tr>
      <td>add interface </td>
      <td>向当前 VLAN 中添加一个或一组 Access 口
。</td>
    </tr>
    <tr>
      <td colspan="2">可选配置，用于 VLAN 重命名。</td>
    </tr>
    <tr>
      <td>name</td>
      <td>为 VLAN 取一个名字。</td>
    </tr>
    <tr>
      <td rowspan="5">配置TRUNK</td>
      <td colspan="2">必须配置。配置接口模式为 TRUNK 口。</td>
    </tr>
    <tr>
      <td>switchport mode trunk</td>
      <td>定义该接口的类型为二层 Trunk 口。</td>
    </tr>
    <tr>
      <td colspan="2">可选配置。配置 TRUNK 口，用于传输多个 VLAN。</td>
    </tr>
    <tr>
      <td>switchport trunk allowed vlan</td>
      <td>配置这个 Trunk 口的许可 VLAN 列表。</td>
    </tr>
    <tr>
      <td>switchport trunk native vlan</td>
      <td>为这个口指定一个 Native VLAN。</td>
    </tr>
    <tr>
      <td rowspan="4">配置 UPLINK</td>
      <td colspan="2">必选配置。 配置接口模式为 UPLINK 口。</td>
    </tr>
    <tr>
      <td>switchport mode uplink</td>
      <td>配置为端口为 Uplink 口。</td>
    </tr>
    <tr>
      <td colspan="2">可选配置，用于恢复接口模式。</td>
    </tr>
    <tr>
      <td>no switchport mode</td>
      <td>删除端口模式。</td>
    </tr>
    <tr>
      <td rowspan="6">配置 HYBRID</td>
      <td colspan="2">必选配置。 配置接口模式为 HYBRID 口。</td>
    </tr>
    <tr>
      <td>switchport mode hybrid</td>
      <td>配置为端口为 Hybrid 口。</td>
    </tr>
    <tr>
      <td colspan="2">可选配置。用于转发多个 VLAN 的帧，并且允许以 UNTAG 方式转发多个 VLAN 的帧。</td>
    </tr>
    <tr>
      <td>no switchport mode</td>
      <td>删除端口模式。</td>
    </tr>
    <tr>
      <td>switchport hybrid allowed vlan</td>
      <td>设置端口的输出规则。</td>
    </tr>
    <tr>
      <td>switchport hybrid native vlan</td>
      <td>设置 Hybrid 口的默认 VLAN。</td>
    </tr>
  </tbody>
</table>


#### 4.4.1 配置基本 VLAN

##### 配置效果

+ 一个VLAN是以VLAN ID来标识的。在设备中，您可以添加、删除、修改VLAN 2 - 4094 ，而VLAN 1是由设备自动创建，并且不可被删除。可以在接口配置模式下配置一个端口的VLAN成员类型或加入、移出一个VLAN。

##### 配置方法

######  创建、修改一个 VLAN

+ 必须配置。
+ 当硬件资源不足的情况下，系统将返回创建VLAN失败信息。
+ 使用vlan vlan-id命令添加一个新的VLAN或者进入VLAN模式。
+ 交换机设备上配置。

【命令格式】 vlan vlan-id
【参数说明】 vlan-id: VLAN vid，范围为 1 - 4094
【缺省配置】 VLAN 1由设备自动创建，并且不可被删除
【命令模式】 全局配置模式
【使用指导】 如果输入的是一个新的VLAN ID，则设备会创建一个VLAN，如果输入的是已经存在的VLAN ID，则修改相应的VLAN。使用no vlan vlan-id命令可以删除vlan，其中不允许删除的VLAN有：默认VLAN1、配置SVI的VLAN、SUBVLAN等。

######  VLAN 重命名

+ 可选配置。
+ 用户不能将VLAN重命名为其他VLAN的缺省名字。 
+ 交换机设备上配置。

【命令格式】 name vlan-name
【参数说明】 vlan-name：要重新命令的VLAN名字
【缺省配置】 缺省情况下，VLAN的名称为该VLAN的VLAN ID。比如，VLAN 0004就是VLAN 4的缺省名字。
【命令模式】 VLAN配置模式
【使用指导】 如果想把VLAN的名字改回缺省名字，只需输入no name命令即可

######  将当前 ACCESS 口加入到指定 VLAN

+ 可选配置。
+ 通过switchport mode access命令指定二层接口（switch port）的模式为access口。
+ 通过switchport access vlan vlan-id命令将一个access port加入指定VLAN，可传输该VLAN流量。
+ 交换机设备上配置。

【命令格式】 switchport mode access
【参数说明】 -^
【缺省配置】 switch port缺省模式为access
【命令模式】 接口配置模式
【使用指导】 -

【命令格式】 switchport^ access^ vlan^ vlan-id^
【参数说明】 vlan-id: VLAN vid：
【缺省配置】 Access口缺省仅加入VLAN 1
【命令模式】 接口配置模式
【使用指导】 如果把一个接口分配给一个不存在的VLAN，那么这个VLAN将自动被创建。

######  向当前 VLAN 添加 ACCESS 口

+ 可选配置。
+ 该命令只对Access口有效，VLAN添加Access口后，接口可传输该VLAN数据。
+ 交换机设备上配置。

【命令格式】 add interface { interface-id | range interface-range }
【参数说明】 interface-id：单个接口
interface-range：多个接口
【缺省配置】 缺省情况下，所有二层以太网口都属于VLAN1
【命令模式】 VLAN配置模式
【使用指导】 在VLAN配置模式下，将指定的Access口加入该VLAN。该命令的配置效果同在接口模式下指定该接口所属
VLAN的命令（即switchport access vlan vlan-id）效果一致。

对于两种形式的接口加入VLAN命令，配置生效的原则是后配置的命令覆盖前面配置的命令

##### 检验方法

+ 往ACCESS口发送untag报文，报文在该VLAN内广播。
+ 使用命令show vlan **和** show interface switchport查看配置显示是否生效。

【命令格式】 show vlan [ id vlan-id ]
【参数说明】 vlan-id^ **：** VLAN ID号^
【命令模式】 所有模式
【使用指导】 -^
【命令展示】 

```
Ruijie(config-vlan)#show vlan id 20
VLAN Name Status Ports

---- -------------------------------- --------- -----------------------------------

20 VLAN0020 STATIC Gi0/1
```

##### 配置举例

######  基本 VLAN 与 access 口配置

以下配置举例，仅介绍VLAN相关的配置。

【配置方法】 

+ 创建一个新VLAN，并且重命名

+ 将一个ACCESS口加入加入VLAN，两种方式。

```
Ruijie# configure terminal^
Ruijie(config)# vlan 888
Ruijie(config-vlan)# name test888
Ruijie(config-vlan)# exit
Ruijie(config)# interface GigabitEthernet 0/ 3
Ruijie(config-if-GigabitEthernet 0/ 3 )# switchport mode access
Ruijie(config-if-GigabitEthernet 0/ 3 )# switchport access vlan 20
```

VLAN或者用如下方式：把Access口 (GigabitEthernet 0 /3)添加到VLAN20：

```
Ruijie# configure terminal
SwitchA(config)#vlan 20
SwitchA(config-vlan)#add interface GigabitEthernet 0 / 3
```

【检验方法】 show显示是否正确

```
Ruijie(config-vlan)#show vlan
VLAN Name Status Ports

---- -------------------------------- --------- -----------------------------------

1 VLAN0001 STATIC
20 VLAN0020 STATIC Gi0/3
888 test888 STATIC
Ruijie(config-vlan)#

Ruijie# show interface GigabitEthernet 0 / 3 switchport
Interface Switchport Mode Access Native Protected VLAN lists

-------------------------------- ---------- --------- ------ ------ --------- --------------

GigabitEthernet 0/3 enabled ACCESS 20 1 Disabled ALL
Ruijie# show run
!
```



#### 4.4.2 配置 TRUNK

##### 配置效果

一个Trunk是将一个或多个以太网交换接口和其他的网络设备（如路由器或交换机）进行连接的点对点链路，一条Trunk链路可以传输属于多个VLAN的流量。

您可以把一个普通的以太网端口，或者一个Aggregate Port设为一个Trunk口（关于Aggregate Port的详细说明，请见配置Aggregate Port）。

必须为Trunk口指定一个Native VLAN。所谓Native VLAN，就是指在这个接口上收发的UNTAG报文，都被认为是属于这个VLAN的。显然，这个接口的缺省VLAN ID（即IEEE 802.1Q中的PVID）就是Native VLAN的VLAN ID。同时，在Trunk上发送属于Native VLAN的帧，则必然采用UNTAG的方式。每个Trunk口的缺省Native VLAN是VLAN 1。

在配置Trunk链路时，请确认连接链路两端的Trunk口使用相同的Native VLAN。

##### 配置方法

######  配置一个 TRUNK 口

+ 必须配置。
+ 将接口配置成trunk可传输多个VLAN的流量。
+ 交换机设备上配置。

【命令格式】 switchport mode trunk
【参数说明】 -
【缺省配置】 缺省模式是ACCESS模式，可配置成TRUNK模式
【命令模式】 接口配置模式
【使用指导】 如果想把一个Trunk口的所有Trunk相关属性都复位成缺省值，请使用no switchport mode配置命令。

######  定义 Trunk 口的许可 VLAN 列表

+ 可选配置。
+ 一个Trunk口缺省可以传输本设备支持的所有VLAN（ 1 － 4094 ）的流量。也可以通过设置Trunk口的许可VLAN列表来限制某些VLAN的流量不能通过这个Trunk口。
+ 交换机设备上配置。

【命令格式】 switchport trunk allowed vlan {all | [add | remove | except | only ] } vlan-list
【参数说明】 参数vlan-list可以是一个VLAN，也可以是一系列VLAN，VLAN ID按顺序排列，中间用“-”号连接。如：
10 – 20 。
all的含义是许可VLAN列表包含所有支持的VLAN；
add表示将指定VLAN列表加入许可VLAN列表；
remove表示将指定VLAN列表从许可VLAN列表中删除；
except表示将除列出的VLAN列表外的所有VLAN加入许可VLAN列表；
only表示将列出的VLAN列表加入许可VLAN列表，其他VLAN从许可列表中删除;
【缺省配置】 trunk口和uplink口属于所有VLAN
【命令模式】 接口配置模式
【使用指导】 如果想把Trunk的许可VLAN列表改为缺省的许可所有VLAN的状态，请使用no switchport trunk allowed
vlan接口配置命令

######  配置 Native VLAN

+ 可选配置。
+ 一个Trunk口能够收发TAG或者UNTAG的802.1Q帧。其中UNTAG帧用来传输Native VLAN的流量。缺省的Native
  VLAN是VLAN 1。

+ 如果一个帧带有Native VLAN的VLAN ID，在通过这个Trunk口转发时，会自动被剥去TAG。
+ 交换机设备上配置。

【命令格式】 switchport trunk native vlan vlan-id
【参数说明】 vlan-id: VLAN vid
【缺省配置】 trunk/uplinK的默认VLAN为VLAN 1
【命令模式】 接口配置模式
【使用指导】 如果想把Trunk的Native VLAN列表改回缺省的VLAN 1，请使用no switchport trunk native vlan接口配置命令。

把一个接口的Native VLAN设置为一个不存在的VLAN时，设备不会自动创建此VLAN。此外，一个接口的Native VLAN可以不在接口的许可VLAN列表中。此时，Native VLAN的流量不能通过该接口。

##### 检验方法

+ 往TRUNK口发送tag报文，报文在指定VLAN内广播。
+ 使用命令show vlan 和 show interface switchport查看配置显示是否生效。

【命令格式】 show vlan [ id vlan-id ]
【参数说明】 vlan-id **：** VLAN ID号
【命令模式】 所有模式
【使用指导】 -
【命令展示】 

```
Ruijie(config-vlan)#show vlan id 20
VLAN Name Status Ports

---- -------------------------------- --------- -----------------------------------

20 VLAN0020 STATIC Gi0/1
```



##### 配置举例

以下配置举例，仅介绍TRUNK相关的配置。

######  配置基本 VLAN ，实现二层隔离、三层互连

【配置方法】 组网需求

如上图所示，某用户内网被划分为VLAN 10、VLAN 20、VLAN 30，以实现相互间的 2 层隔离； 3 个VLAN
对应的IP子网分别为192.168.10.0/24、192.168.20.0/24、192.168.30.0/24， 3 个VLAN通过 3 层核心交换
机的IP转发能力实现子网互连。
配置要点
本例以核心交换机和 1 台接入交换机为例说明配置过程。要点如下：

+ 在核心交换机配置 3 个VLAN，配置下连接入交换机的端口为trunk口，并指定许可vlan列表，实现 2层隔离；
+ 在核心交换机配置 3 个SVI口，分别作为 3 个VLAN对应IP子网的网关接口，配置对应的IP地址；
+ 分别在 3 台接入交换机创建VLAN，为各VLAN分配Access口，指定上连核心交换机的trunk口。本例以接入交换机Switch A为例说明配置步骤。

```
D D#configure terminal
D(config)#vlan 10
D(config-vlan)#vlan 20
D(config-vlan)#vlan 30
D(config-vlan)#exit
D(config)#interface range GigabitEthernet 0 /2- 4
D(config-if-range)#switchport mode trunk
D(config-if-range)#exit
D(config)#interface GigabitEthernet 0 /2
D(config-if-GigabitEthernet 0/ 2 )#switchport trunk allowed vlan remove 1 - 4094
D(config-if-GigabitEthernet 0/ 2 )#switchport trunk allowed vlan add 10,20
D(config-if-GigabitEthernet 0/ 2 )#interface GigabitEthernet 0 /3
D(config-if-GigabitEthernet 0/ 3 )#switchport trunk allowed vlan remove 1 - 4094
D(config-if-GigabitEthernet 0/ 3 )#switchport trunk allowed vlan add 10,20,30
D(config-if-GigabitEthernet 0/ 3 )#interface GigabitEthernet 0 /4
D(config-if-GigabitEthernet 0/ 4 )#switchport trunk allowed vlan remove 1 - 4094
D(config-if-GigabitEthernet 0/ 4 )#switchport trunk allowed vlan add 20,30
D#configure terminal
D(config)#interface vlan 10
D(config-if-VLAN 10)#ip address 192.168.1 0 .1 255.255.255.0
D(config-if-VLAN 10 )#interface vlan 20
D(config-if-VLAN 20 )#ip address 192.168. 20 .1 255.255.255.0
D(config-if-VLAN 20 )#interface vlan 30
D(config-if-VLAN 30 )#ip address 192.168. 30 .1 255.255.255.0
D(config-if-VLAN 30 )#exit
A A#configure terminal
A(config)#vlan 10
A(config-vlan)#vlan 20
A(config-vlan)#exit
A(config)#interface range GigabitEthernet 0 /2- 12
A(config-if-range)#switchport mode access
A(config-if-range)#switchport access vlan 10
A(config-if-range)#interface range GigabitEthernet 0 / 13 - 24
A(config-if-range)#switchport mode access
A(config-if-range)#switchport access vlan 20
A(config-if-range)#exit
A(config)#interface GigabitEthernet 0 / 1
A(config-if-GigabitEthernet 0/ 1 )#switchport mode trunk
```

【检验方法】 在核心交换机上查看vlan配置

+ 查看vlan信息，包括vlan id、名称、状态、包括的端口

+ 查看端口Gi 0/2、Gi 0/3、Gi 0/4的vlan状态

```
D 
D#show vlan
VLAN Name Status Ports

---- -------- -------- -------------------------------

1 VLAN0001 STATIC Gi0/1, Gi0/5, Gi0/6, Gi0/7
Gi0/8, Gi0/9, Gi0/10, Gi0/11
Gi0/12, Gi0/13, Gi0/14, Gi0/15
Gi0/16, Gi0/17, Gi0/18, Gi0/19
Gi0/20, Gi0/21, Gi0/22, Gi0/23
Gi0/24
10 VLAN0010 STATIC Gi0/2, Gi0/3
20 VLAN0020 STATIC Gi0/2, Gi0/3, Gi0/4
30 VLAN0030 STATIC Gi0/3, Gi0/4
D#show interface GigabitEthernet 0/2 switchport
Interface Switchport Mode Access Native Protected VLAN lists

-------------------------------- ---------- --------- ------ ------ --------- --------------

GigabitEthernet 0/ 2 enabled TRUNK 1 1 Disabled 10,
D#show interface GigabitEthernet 0/3 switchport
Interface Switchport Mode Access Native Protected VLAN lists
-------------------------------- ---------- --------- ------ ------ --------- --------------
GigabitEthernet 0/ 3 enabled TRUNK 1 1 Disabled 10,20,30
D#show interface GigabitEthernet 0/4 switchport
Interface Switchport Mode Access Native Protected VLAN lists
-------------------------------- ---------- --------- ------ ------ --------- --------------
GigabitEthernet 0/ 4 enabled TRUNK 1 1 Disabled 20,30
```

#### 4.4.3 配置 UPLINK

##### 配置效果

+ UPLINK 端口一般用于QinQ（出自标准IEEE 802.1ad）环境中，它和TRUNK 端口的功能很相似，不同之处在于UPLINK端口只发送TAG帧，而TRUNK 端口缺省VLAN 的帧以UNTAG形式发送。

##### 配置方法

######  配置一个 UPLINK 口

+ 必须配置。
+ 将接口配置成uplink口，可传输多个vlan的流量，但只能发送TAG帧。
+ 交换机设备上配置。

【命令格式】 switchport mode uplink
【参数说明】 -
【缺省配置】 缺省模式是ACCESS模式，可配置成ACCESS模式UPLINK模式
【命令模式】 接口配置模式
【使用指导】 如果想把一个UPLINK口的所有UPLINK相关属性都复位成缺省值，请使用no switchport mode配置命令。

######  定义 UPLINK 口的许可 VLAN 列表

+ 可选配置。
+ 可以通过设置UPLINK口的许可VLAN列表来限制某些VLAN的流量不能通过这个UPLINK口。
+ 交换机设备上配置。

【命令格式】 switchport trunk allowed vlan {all | [add | remove | except | only ] } vlan-list
【参数说明】 参数vlan-list可以是一个VLAN，也可以是一系列VLAN，VLAN ID按顺序排列，中间用“-”号连接。如：
10 – 20 。
all的含义是许可VLAN列表包含所有支持的VLAN；
add表示将指定VLAN列表加入许可VLAN列表；
remove表示将指定VLAN列表从许可VLAN列表中删除；
except表示将除列出的VLAN列表外的所有VLAN加入许可VLAN列表；
only表示将列出的VLAN列表加入许可VLAN列表，其他VLAN从许可列表中删除;
【命令模式】 接口配置模式
【使用指导】 如果想把UPLINK的许可VLAN列表改为缺省的许可所有VLAN的状态，请使用no switchport trunk allowed vlan接口配置命令

######  配置 Native VLAN

+ 可选配置。
+ 如果一个帧带有Native VLAN的VLAN ID，在通过这个UPLINK口转发时，不会被剥去TAG。这与TRUNK相反。
+ 交换机设备上配置。

【命令格式】 switchport trunk native vlan vlan-id^
【参数说明】 vlan-id: VLAN vid
【命令模式】 接口配置模式
【使用指导】 如果想把UPLINK的Native VLAN列表改回缺省的VLAN 1，请使用no switchport trunk native vlan接口配置命令。

##### 检验方法

+ 往UPLINK口发送tag报文，报文在指定VLAN内广播。
+ 使用命令show vlan **和** show interface switchport查看配置显示是否生效。

【命令格式】 show vlan [ id vlan-id ]
【参数说明】 vlan-id **：** VLAN ID号
【命令模式】 所有模式
【使用指导】 -
【命令展示】 

```
Ruijie(config-vlan)#show vlan id 20
VLAN Name Status Ports

---- -------------------------------- --------- -----------------------------------

20 VLAN0020 STATIC Gi0/1
```

##### 配置举例

######  配置一个 uplink 口

以下配置举例，仅介绍UPLINK相关的配置。^

【配置方法】 下面是一个把端口Gi0/ 1 变成UPLINK的例子：

```
Ruijie# configure terminal
Ruijie(config)# interface gi 0/1
Ruijie(config-if-GigabitEthernet 0/ 1 )# switchport mode uplink
Ruijie(config-if-GigabitEthernet 0/ 1 )# end
```

【检验方法】 show显示是否正确

```
Ruijie# show interfaces GigabitEthernet 0 / 1 switchport
Interface Switchport Mode Access Native Protected VLAN lists

-------------------------------- ---------- --------- ------ ------ --------- -----------------

GigabitEthernet 0/ 1 enabled UPLINK 1 1 disabled ALL
```



#### 4.4.4 配置 HYBRID

##### 配置效果

+ HYBRID端口一般用于SHARE VLAN的环境中。HYBRID 端口在缺省情况下与TRUNK 端口相同，不同是它可以设置除了缺省VLAN外的其它VLAN 的帧以UNTAG形式发送

##### 配置方法

######  配置一个 HYBRID 口

+ 必须配置。
+ 将接口配置成hybrid口，可传输多个VLAN的流量。
+ 交换机设备上配置。

【命令格式】 switchport mode hybrid
【参数说明】 -^
【缺省配置】 缺省模式是ACCESS模式，可配置成HYBRID模式
【命令模式】 接口配置模式
【使用指导】 (^) 如果想把一个HYBRID口的所有HYBRID相关属性都复位成缺省值，请使用no switchport mode配置命令。

######  定义 HYBRID 口的许可 VLAN 列表

+ 可选配置。
+ 一个HYBRID口缺省可以传输本设备支持的所有VLAN（ 1 － 4094 ）的流量。也可以通过设置HYBRID口的许可VLAN
  列表来限制某些VLAN的流量不能通过这个HYBRID口。
+ 交换机设备上配置。

【命令格式】 switchport hybrid allowed vlan [ [add | only ] tagged | [ add ] untaged | remove ] vlan_list
【参数说明】 vlan-id: VLAN vid
【缺省配置】 默认hybrid口属于所有VLAN，端口以Tag形式加入所有除了默认VLAN以外的其它VLAN，默认VLAN以UNTag形式加入
【命令模式】 接口配置模式
【使用指导】 -

######  配置 Native VLAN

+ 可选配置。
+ 如果一个帧带有Native VLAN的VLAN ID，在通过这个HYBRID口转发时，会自动被剥去TAG。

+ 交换机设备上配置。

【命令格式】 switchport hybrid native vlan vlan_id
【参数说明】 vlan-id: VLAN vid^
【缺省配置】 缺省的Native VLAN是VLAN 1
【命令模式】 接口配置模式
【使用指导】 如果想把HYBRID的Native VLAN列表改回缺省的VLAN 1，请使用no switchport hybrid native vlan接口配置命令。

##### 检验方法

+ 往HYBRID口发送tag报文，报文在指定VLAN内广播。
+ 使用命令show vlan 和 show interface switchport查看配置显示是否生效。

【命令格式】 show vlan^ [ id vlan-id ]^
【参数说明】 vlan-id ： AP VLAN ID号
【命令模式】 所有模式
【使用指导】 -
【命令展示】 

```
Ruijie(config-vlan)#show vlan id 20
VLAN Name Status Ports

---- -------------------------------- --------- -----------------------------------

20 VLAN0020 STATIC Gi0/1
```



##### 配置举例

######  配置一个 hybrid 口

以下配置举例，仅介绍HYBRID相关的配置。^

【配置方法】 下面是一个端口Gi0/ 1 关于HYBRID配置的例子：

```
Ruijie# configure terminal
Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if-GigabitEthernet 0/ 1 )# switchport mode hybrid
Ruijie(config-if-GigabitEthernet 0/ 1 )# switchport hybrid native vlan 3
Ruijie(config-if-GigabitEthernet 0/ 1 )# switchport hybrid allowed vlan untagged 20- 30
Ruijie(config-if-GigabitEthernet 0/ 1 )# end
```



【检验方法】 show run显示是否正确

```
Ruijie(config-if-GigabitEthernet 0/1)#show run interface gigabitEthernet 0/1

Building configuration...
Current configuration : 166 bytes

interface GigabitEthernet 0/1
switchport
switchport mode hybrid
switchport hybrid native vlan 3
switchport hybrid allowed vlan add untagged 20- 30
```



### 4.5 监视与维护

##### 查看运行情况

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>查看 VLAN 配置</td>         <td>show vlan</td>     </tr>     <tr>         <td>查看交换口配置</td>         <td>show interface switchport</td>     </tr> </table>

##### 查看调试信息

输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>打开 VLAN 的调试开关。</td>         <td>debug bridge vlan</td>     </tr> </table>






## 5 MAC VLAN

### 5.1 概述

MAC VLAN就是基于MAC地址划分的VLAN，是一种新的VLAN划分方法。该功能通常会和802.1X下发VLAN功能结合使用，以实现802.1X终端的安全、灵活接入。当802.1X用户通过认证后，根据认证服务器下发的VLAN和用户MAC地址，由交换机自动生成MAC VLAN表项。网络管理员也可以预先在交换机上配置MAC地址和VLAN的关联关系。

##### 协议规范

+ IEEE 802.1Q：Virtual Bridged Local Area Networks

### 5.2 典型应用

<table>     <tr>         <th>典型应用</th>         <th>场景描述</th>     </tr>     <tr>         <td>MAC VLAN 配置应用</td>         <td>通过配置 MAC VLAN ,实现按用户 MAC 地址划分 VLAN ,当用户物理位置发生移动时，即从一台交换机换到其它的交换机时，不需要重新配置用户所在端口的 VLAN。</td>     </tr> </table>

#### 5.2.1 MAC VLAN 配置应用

##### 应用场景

随着移动办公的普及，终端设备不再通过固定端口接入设备，它可能本次使用端口 A接入网络，下次使用端口 B接入网络。如果端口A和端口B的VLAN配置不同，则终端设备第二次接入后就会被划分到不同VLAN，导致无法使用原VLAN内的资源；如果端口A和端口B的VLAN配置相同，当端口B被分配给别的终端设备时，又会引入安全问题。如何在同一端口下，允许不同VLAN的主机自由接入呢？MAC VLAN功能由此产生。

MAC VLAN的最大优点就是当用户物理位置发生移动时，即从一台交换机换到其它的交换机时，不需要重新配置用户所在端口的VLAN。所以，可以认为这种根据MAC地址的VLAN划分方法是基于用户的VLAN。

**功能部属**

+ 二层交换设备通过配置或下发MAC VLAN表项，实现根据用户MAC地址来分配VLAN。

### 5.3 功能详解

**功能特性**

<table>     <tr>         <th>功能特性</th>         <th>作用</th>     </tr>     <tr>         <td>MAC VLAN</td>         <td>配置 MAC VLAN，实现基于用户 MAC 地址分配 VLAN。</td>     </tr> </table>

#### 5.3.1 MAC VLAN

**工作原理**

当交换机收到报文时，将数据流的源MAC与MAC VLAN表项中指定的MAC地址进行匹配。如果匹配成功，则将该报文转发到MAC VLAN表项指定的VLAN中；如果匹配失败，则该数据流所属的VLAN仍然由端口的VLAN规则决定。

为了实现PC从任意交换机接入时，都会被划分到指定的VLAN，可以通过如下两种方式进行配置：

+ 通过命令行静态配置。用户通过命令行在本地交换机设备上配置 MAC地址和VLAN的关联关系。
+ 通过认证服务器来自动配置（802.1X VLAN下发功能）。当用户认证通过后，交换机根据认证服务器提供的信息，动态创建MAC地址和VLAN的关联关系。用户下线时，交换机将自动删除该对应关系。该方式需要在认证服务器上配置MAC地址和VLAN的关联，有关“802.1X VLAN下发功能”的详细介绍请参见“802.1X配置”。

MAC VLAN表项可以同时支持两种配置方式，即在本地设备和认证服务器上都进行了配置，但是这两种配置必须一致配置才能生效；如果不一致的话，则先执行的配置生效。

基于MAC的VLAN功能只能在^ HYBRID端口上配置。

MAC VLAN表项仅针对UNTAG的报文生效，对携带TAG的报文不生效。

静态配置或动态生成MAC VLAN表项时，指定VLAN必需已经存在。

MAC VLAN表项中指定的VLAN不能是Super VLAN(可以是Sub VLAN)、Remote VLAN、Primary VLAN（可以是Secondary VLAN）。

MAC VLAN表项中指定的MAC地址必须是单播地址。

MAC VLAN表项对所有开启MAC VLAN功能的HYBRID端口生效。

### 5.4 配置详解

<table>
  <thead>
    <tr>
      <th>配置项</th>
      <th colspan="2">配置建议 & 相关命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">基于端口开启 MAC VLAN</td>
      <td colspan="2">必选配置。用于开启端口 MAC VLAN 功能。</td>
    </tr>
    <tr>
      <td>mac-vlan enable</td>
      <td>配置配置端口 MAC VLAN 功能。</td>
    </tr>
    <tr>
      <td rowspan="2">全局添加静态 MAC VLAN 表项</td>
      <td colspan="2">可选配置。用于绑定 MAC 地址与 VLAN 关系
</td>
    </tr>
    <tr>
      <td>mac-vlan mac-address </td>
      <td>配置静态 MAC VLAN 表项。</td>
    </tr>
  </tbody>
</table>


### 

#### 5.4.1 基于端口开启 MAC VLAN

##### 配置效果

基于端口配置MAC VLAN，使得MAC VLAN表项在端口上生效。

**配置方法**

######  配置端口 MAC VLAN 功能

+ 必选配置。

+ 缺省情况下，基于端口的MAC VLAN开关处于关闭状态，所有MAC VLAN表项均不会在端口上生效。

+ 交换机设备上配置。

【命令格式】 mac-vlan enable
【参数说明】 -
【缺省配置】 端口MAC VLAN功能关闭
【命令模式】 接口模式
【使用指导】 -

**检验方法**

+ 通过show mac-vlan interface命令查看开启MAC VLAN功能的端口信息。

【命令格式】 show mac-vlan interface
【参数说明】 -
【命令模式】 特权模式，全局模式，接口模式
【使用指导】 -
【命令展示】 

```
Ruijie#^ show mac-vlan interface^

MAC VLAN is enabled on following interface:

FastEthernet 0/1

```

##### 配置举例

######  配置端口 MAC VLAN 功能

【配置方法】 

+ 打开接口FastEthernet 0/10的MAC VLAN功能

```
Ruijie# configure terminal
Ruijie(config)# interface FastEthernet 0/10
Ruijie(config-if-FastEthernet 0/1 0 )# mac-vlan enable
```



【检验方法】 

+ 查看开启MAC VLAN功能的端口信息

```
Ruijie# show mac-vlan interface
MAC VLAN is enabled on following interface:
FastEthernet 0/10
```

##### 常见错误

配置接口MAC VLAN功能时，接口没有先配置成二层接口，包括交换口、AP口。

#### 5.4.2 全局添加静态 MAC VLAN 表项

##### 配置效果

 配置静态MAC VLAN表项，绑定MAC地址和VLAN的关联关系。可选配置802.1p优先级，默认值为 0 。

##### 配置方法

######  添加静态 MAC VLAN 表项

+ 可选配置。

+ 如果需要绑定MAC地址和VLAN的关联关系，则应该执行此配置项。可选配置802.1p优先级，默认值为 0 。

+ 交换机设备上配置。

【命令格式】 mac-vlan mac-address mac-address [ mask mac-mask ] vlan vlan-id [ priority pri_val ]
【参数说明】 mac-address mac-address：MAC地址
mask mac-mask：掩码
vlan vlan-id：所在的VLAN
priority pri_val：优先级
【缺省配置】 缺省没有设置任何静态MAC VLAN表项
【命令模式】 全局模式
【使用指导】 -

UNTAG的报文如果能够匹配MAC VLAN表项，由于MAC VLAN表项的优先级最高，报文一进入交换机就被修改为MACVLAN表项指定的VLAN，后续功能和协议都是按照修改后的VLAN进行处理。可能造成的影响，举例如下：
802.1x用户认证失败后，Hybrid端口跳转到FAIL VLAN功能指定的VLAN 100中，但是静态配置的MAC VLAN表项将该用户所有的报文重定向到VLAN 200中；导致该用户无法在FAIL VLAN 100中正常通讯；
UNTAG的报文匹配MAC VLAN表项后，触发MAC地址学习的VLAN是根据MAC VLAN表项重定向之后的VLAN；
开启MAC VLAN的端口，如果接收报文可以同时匹配掩码不为全F和掩码为全F的MAC VLAN表项，报文处理按照掩码不为全F的MAC VLAN表项为准；
UNTAG的报文同时匹配MAC VLAN表项和VOICE VLAN表项时，同时修改报文优先级，报文优先级以VOICE VLAN为准；
UNTAG的报文同时匹配MAC VLAN表项和PROTOCOL VLAN表项时，报文携带VLAN以MAC VLAN为准；
MAC VLAN只适用于UNTAG的报文，对于PRIORITY报文（VLAN TAG 为0 ，带COS PRIORITY信息的报文）不适用，处理行为不确定；
交换机上QOS的报文信任模式默认处于关闭状态，这会导致修改所有报文的PRIORITY信息为^0 ，从而覆盖MAC VLAN功能对报文PRIORITY的修改。可以在端口配置模式下执行：“mls qos trust cos”命令开启QOS信任模式，信任报文的PRIORITY信息；

######  删除全部静态 MAC VLAN 表项

+ 可选配置。
+ 如果需要删除全部静态MAC VLAN表项，则应该执行此配置项。

+ 交换机设备上配置。

【命令格式】 no mac-vlan all
【参数说明】 -
【命令模式】 全局模式
【使用指导】 -

######  删除指定 MAC 的静态 MAC VLAN 表项

 可选配置。

 如果需要删除指定MAC的MAC VLAN表项，则应该执行此配置项。

 交换机设备上配置。

【命令格式】 no mac-vlan mac-address mac-address [ mask mac-mask ]
【参数说明】 mac-address mac-address：要删除的指定MAC地址
mask mac-mask：掩码
【命令模式】 全局模式
【使用指导】 -

######  删除指定 VLAN 的静态 MAC VLAN 表项

+ 可选配置。

+ 如果需要删除指定VLAN的MAC VLAN表项，则应该执行此配置项。

+ 交换机设备上配置。

【命令格式】 no mac-vlan vlan vlan-id
【参数说明】 vlan vlan-id：指定的VLAN
【命令模式】 全局模式
【使用指导】 -

**检验方法**

+ 通过命令show mac-vlan static显示所有的静态MAC VLAN表项信息是否正确。

+ 通过命令show mac-vlan vlan vlan-id 显示指定VLAN的MAC VLAN表项信息是否正确。

+ 通过命令show mac-vlan mac-address mac-address [ mask mac-mask ] 显示指定MAC地址的MAC VLAN表项信息。

【命令格式】 show mac-vlan static
show mac-vlan vlan vlan-id
show mac-vlan mac-address mac-address [ mask mac-mask ]
【参数说明】 vlan vlan-id：指定的VLAN
mac-address mac-address：指定的MAC地址
mask mac-mask：指定的掩码
【命令模式】 特权模式，全局模式，接口模式
【使用指导】 -
【命令展示】 

```
Ruijie#^ show mac-vlan all^
The following MAC VLAN address exist:
S: Static D: Dynamic
MAC ADDR MASK VLAN ID PRIO STATE
-------------------------------------------------------
0000.0000.0001 ffff.ffff.ffff 2 0 D
0000.0000.0002 ffff.ffff.ffff 3 3 S
0000.0000.000 3 ffff.ffff.ffff 3 3 S&D
Total MAC VLAN address count: 3
```



##### 配置举例

######  全局添加静态 MAC VLAN 表项

如图所示： PC-A1、PC-A2属于A部门，规划为VLAN 100；PC-B1、PC-B2属于B部门，规划为VLAN 200。因为人员流动关系，公司在会议室提供了临时办公场所，但是要求接入后只能划分到自己部门所在的VLAN。如：PC-A1接入后只能划分到VLAN 100，PC-B1接入后只能划分到VLAN 200。

因为会议室PC接入网络的端口不固定，因此可能通过MAC VLAN功能，将员工PC的MAC地址和员工所在部门的VLAN关联起来。不管从哪个端口接入，均可以被自动划分到部门所在的VLAN。

【配置方法】 

+ Switch C与Router 1相连的端口配置为TRUNK口

+ Switch C所有与PC相连的端口配置为HYBRID口，开启MAC VLAN功能开关，并修改默认UNTAG
  VLAN列表
+ Switch C上配置MAC VLAN表项

```
A A# configure terminal
A(config)# interface interface_name
A(config-if)# switchport mode trunk
A(config-if)# exit
A(config)# interface interface_name
A(config-if)# switchport mode hybrid
A(config-if)# switchport hybrid allowed vlan add untagged 100,200
A(config-if)# mac-vlan enable
A(config-if)# exit
A(config)# mac-vlan mac-address PC-A1-mac vlan 100
A(config)# mac-vlan mac-address PC-B1-mac vlan 200
```



【检验方法】 在Switch C上查看配置的静态MAC VLAN表项

```
A A# Ruijie# show mac-vlan static
The following MAC VLAN address exist:
S: Static D: Dynamic
MAC ADDR MASK VLAN ID PRIO STATEPC-A1-mac 
-------------------------------------------------------
ffff.ffff.ffff 100 0 S
PC-B1-mac ffff.ffff.ffff 200 3 S
Total MAC VLAN address count: 2
```



### 5.5 监视与维护

##### 查看运行情况

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>显示所有的 MAC VLAN 表项，包括静态配置和动态生成的。</td>         <td>show mac-vlan all</td>     </tr>     <tr>         <td>显示动态生成的 MAC VLAN 表项。</td>         <td>show mac-vlan dynamic</td>     </tr>     <tr>         <td>显示静态配置的 MAC VLAN 表项。</td>         <td>show mac-vlan static</td>     </tr>     <tr>         <td>显示指定 VLAN 的 MAC VLAN 表项。</td>         <td>show mac-vlan vlan vlan-id</td>     </tr>     <tr>         <td>显示指定 MAC 地址的 MAC VLAN 表项。</td>         <td>show mac-vlan mac-address mac-address [mask mac-mask]</td>     </tr> </table>

##### 查看调试信息

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>打开 MAC VLAN 运行的调试开关。</td>         <td>debug bridge mvlan
</td>     </tr>     </table>


## 6 Super VLAN

### 6.1 概述

Super VLAN是VLAN划分的一种方式。Super VLAN又称为VLAN聚合，是一种专门优化IP地址的管理技术。

采用Super VLAN技术可以极大的节省IP地址，它只需对包含多个Sub VLAN的Super VLAN分配一个IP地址，既节省地址又方便网络管理。

下文仅介绍Super VLAN的相关内容。

#### 6.2 典型应用

<table>     <tr>         <th>典型应用</th>         <th>场景描述</th>     </tr>     <tr>         <td>多个 VLAN 共享一个 IP 网关</td>         <td>接入用户通过划分 VLAN 实现二层隔离，所有 VLAN 用户共享一个 IP 网关，实现三层通信以及与外网通信。</td>     </tr> </table>

#### 6.2.1 多个 VLAN 共享一个 IP 网关

##### 应用场景

在一台三层设备上实现多个VLAN的二层隔离，但是这些VLAN的用户可以在一个网段并进行三层通信。

【注释】 Switch A为网关设备或核心交换机。
Switch B、Switch C、Switch D为接入交换机。
Switch A上配置Super VLAN和Sub VLAN，并为Super VLAN配置三层口和三层口的IP地址。
Switch B、Switch C、Switch D上分别配置VLAN 10、VLAN 20、VLAN 30 ，将公司的不同部门分别划分在这些VLAN内。

##### 功能部属

在Intranet中通过Super VLAN实现多个子VLAN的共享一个IP网关，又能保证VLAN间的二层隔离。子VLAN内的用户间可以通过Super VLAN的网关进行三层通信。

### 6.3 功能详解

##### 基本概念

######  Super VLAN

Super VLAN又称为VLAN聚合，是一种专门优化IP地址的管理技术，将多个VLAN聚合到一个IP网段。Super VLAN不能加入任何物理口，主要通过其SVI口来管理Sub VLAN的跨VLAN通信，不能当做正常的802.1Q VLAN来使用。可以将Super VLAN看成Sub VLAN的主VLAN。

######  Sub VLAN

Sub VLAN又称子VLAN，每一个Sub VLAN都是一个独立的广播域，它们之间是二层隔离。同一Super VLAN的Sub VLAN或不同Super VLAN的Sub VLAN的用户之间通信需要依靠各自Super VLAN三层口SVI实现。

######  ARP 代理

只有Super VLAN才能创建三层口SVI，子VLAN不能创建SVI。子VLAN依靠其主VLAN（Super VLAN）的三层口通过ARP代理，实现同一Super VLAN不同Sub VLAN之间以及不同网段用户之间的通信。Sub VLAN的用户向其他VLAN的用户发送ARP请求时，主VLAN的网关用其MAC地址代替其发送和回应ARP请求，这个过程称为ARP代理。

######  Sub VLAN IP 地址范围

每个Sub VLAN可以根据主VLAN配置的网关IP地址来配置一个子IP地址范围，可以限制Sub VLAN内用户所在的IP范围。

**功能特性**

<table>     <tr>         <th>功能特性</th>         <th>作用</th>     </tr>     <tr>         <td>Super VLAN</td>         <td>创建三层次接口，作为一个虚拟接口通过 ARP 代理来实现其所有 Sub VLAN 共用一个 IP 网段</td>     </tr> </table>

#### 6.3.1 Super VLAN

Super VLAN可以使其所有的的Sub VLAN内用户都划分在同一个IP范围内，并通用一个IP网关，用户通过这个网关可以跨VLAN通信，而不用每个VLAN划分一个网关，从而节省了IP地址。

##### 工作原理

Super VLAN的工作原理是将一个网段的IP地址分给不同的子VLAN（Sub VLAN），这些Sub VLAN同属于一个Super VLAN。每个Sub VLAN具备VLAN的独立广播域，不同的Sub VLAN之间是二层隔离的。当Sub VLAN内的用户需要进行三层通信时，使用Super VLAN的虚接口的IP地址作为网关地址，这样多个VLAN共享一个IP网关，不用每个VLAN配置一个网关。同时，为了实现不同的Sub VLAN间的三层互通及Sub VLAN与其它网段互通，需要利用ARP代理功能，通过ARP代理可以进行ARP请求和响应报文的转发和处理，从而实现三层通信。

Sub VLAN的二层通信：如果Super VLAN没有配置SVI，Super VLAN内的各个Sub VLAN之间是二层隔离的，即Sub VLAN内的用户之间不能通信；如果Super VLAN配置了SVI，通过Super VLAN的网关作为ARP代理，同一Super VLAN内的Sub VLAN之间可以通信，因为这些Sub VLAN用户的IP是同一个网段，认为还是二层通信。

Sub VLAN的三层通信：Sub VLAN内的用户要跨网段进行三层通信时，其所属的Super VLAN的网关作为ARP代理， 代替Sub VLAN回应ARP请求。

### 6.4 配置详解

<table>
  <thead>
    <tr>
      <th>配置项</th>
      <th colspan="2">配置建议 & 相关命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">配置 Super VLAN 基本功能</td>
      <td colspan="2">必选配置</td>
    </tr>
    <tr>
      <td>supervlan</td>
      <td>配置 Super VLAN。</td>
    </tr>
    <tr>
      <td>subvlan vlan-id-list </td>
      <td>配置 Sub VLAN</td>
    </tr>
    <tr>
      <td>proxy-arp</td>
      <td>ARP 代理使能</td>
    </tr>
    <tr>
      <td>interface vlan vlan-id </td>
      <td>创建 Super VLAN 的虚拟接口</td>
    <tr>
      <td>ip address ip mask</td>
      <td>设置 Super VLAN 虚拟接口的 IP 地址</td>
    </tr>
    <tr>
      <td colspan="2">可选配置</td>
    </tr>      
    <tr>
      <td>subvlan-address-range start-ip end-ip</td>
      <td>指定 Sub VLAN 内用户的 IP 地址范围。</td>
    </tr>
  </tbody>
</table>


#### 6.4.1 配置 Super VLAN 基本功能

##### 配置效果

启动Super VLAN功能，给Super VLAN配置SVI，实现Sub VLAN跨VLAN的二三层通信。同一Super VLAN的所有Sub VLAN内用户共用一个IP网关，不用每个VLAN指定一个网段，从而节省IP地址。

##### 注意事项

因为Super VLAN不属于任何物理口，所以配置Super VLAN的设备不能处理Tag为Super VLAN的报文。

必须同时使能Super VLAN和Sub VLAN的ARP代理功能。

必须为Super VLAN配置SVI和IP地址，作为其所有Sub VLAN通信的虚接口，Sub VLAN内的用户才能跨VLAN通信。

##### 配置方法

######  配置 Super VLAN

+ 必须配置。

+ 该VLAN内不包括任何物理口。

+ 必须使能ARP代理功能，默认是打开的。

+ 使用supervlan命令将一个普通VLAN变成Super VLAN。

+ 普通VLAN变成Super VLAN后，加入该VLAN的端口都将从这个VLAN退出，这是因为Super VLAN内不能有任何物理端口。

必须为Super VLAN配置Sub VLAN，Super VLAN才有意义、
VLAN 1不能配置为Super VLAN。
Super VLAN不能配置为其它Super VLAN的Sub VLAN，反之亦然。^

【命令格式】 supervlan
【参数说明】 -
【缺省配置】 (^) VLAN都是普通VLAN
【命令模式】 VLAN模式
【使用指导】 缺省情况下，Super VLAN功能是关闭的。Super VLAN不能加入任何物理口。一旦VLAN不再是Super VLAN，其所属的所有Sub VLAN都恢复成普通静态VLAN。

######  配置 Super VLAN 的虚拟口

+ 必须配置。

+ Super VLAN不能加入任何物理口，通过配置的VLAN三层口SVI作为虚拟口。

Super VLAN配置SVI时，会同时为其所有Sub VLAN分配一个对用户不可见的三层口，如果因为资源不足不能为Sub VLAN分配三层口，此时会将该Sub VLAN恢复为普通VLAN。
【命令格式】 interface vlan vlan-id
【参数说明】 vlan-id : Super VLAN的id。
【缺省配置】 默认无配置
【命令模式】 全局模式
【使用指导】 为Super VLAN配置三层口，作为Super VLAN的虚拟接口，必须配置。

######  Super VLAN 网关

+ 必须配置。

+ Super VLAN通过配置在三层口SVI上的IP网关来代理Sub VLAN内用户的IP回应其它用户的ARP请求。

【命令格式】 ip address ip mask
【参数说明】 ip : IP地址，Super VLAN虚拟接口的网关地址。Mask : 掩码。
【缺省配置】 默认无配置
【命令模式】 接口模式
【使用指导】 为Super VLAN配置网关，Super VLAN所有Sub VLAN的用户都属于这个网关。

######  配置 Sub VLAN

+ 必须配置。

+ Sub VLAN内可以加入任何物理口，同一Super VLAN的Sub VLAN共享Super VLAN的网关地址，使用同一网段。

+ 必须使能ARP代理功能，默认是打开的。

+ 使用subvlan vlan-id-list命令将普通VLAN变成Super VLAN的Sub VLAN，这些VLAN内可以有物理口。

+ Sub VLAN内的用户通信由Super VLAN来管理。

Sub VLAN不能直接通过no vlan命令删除，必须先恢复为普通VLAN后才能被删除。
不同Super VLAN的Sub VLAN不能有交叠。

【命令格式】 subvlan^ vlan-id-list^
【参数说明】 vlan-id-list : 指定若干VLAN作为某个Super VLAN的Sub VLAN。
【缺省配置】 VLAN都是普通VLAN
【命令模式】 VLAN模式
【使用指导】 用户连接的接口可以加入Sub VLAN。
不能使用no vlan [ id ]来删除Sub VLAN，必须先转化成普通VLAN后才能删除。不能为Sub VLAN配置VLAN三层口SVI。

如果Super VLAN配置了VLAN三层口SVI，再增加Sub VLAN时可能会因为资源不足而导致Sub VLAN配置失败。
如果Super VLAN配置了Sub VLAN，再配置VLAN三层口SVI，这时可能会因为资源不足将部分Sub  VLAN恢复为普通VLAN。

######  ARP 代理

+ 必须配置，默认是打开的。

+ 只有Super VLAN和Sub VLAN同时使能ARP代理功能，Sub VLAN内的用户才能通过Super VLAN的网关代理实现跨VLAN二三层通信。

+ Super VLAN和Sub VLAN均开启该功能，Sub VLAN内的用户才能和其它VLAN的用户通信。

必须在Super VLAN和Sub VLAN上使能ARP代理，否则ARP代理功能不起作用。

【命令格式】 proxy-arp
【参数说明】 -
【缺省配置】 缺省打开
【命令模式】 VLAN模式
【使用指导】 默认是打开的。
此命令用来使能Super VLAN和Sub VLAN的ARP代理。
只有Super VLAN和对应的Sub VLAN都使能，Sub VLAN的用户才能跨VLAN进行二三层通信。

######  Sub VLAN IP 地址范围

+ 如果需要划分用户的IP地址使用范围，可以为每个Sub VLAN划分一个IP地址范围，Sub VLAN内用户的IP地址在规定的范围内才能与其它VLAN的用户正常通信，否则不能跨VLAN通信。

+ 若无特殊要求，可以不用划分IP地址范围。

这里划分了IP地址范围，并不能保证DHCP给用户动态IP地址也在该范围内，如果DHCP分配的IP地址不在规定的范围内，用户不能对外通信，请慎用。

必须保证Sub VLAN的IP地址范围在Super VLAN的网关范围内，否则Sub VLAN内的用户无法通信。

Sub VLAN内的用户的IP地址必须在Sub VLAN的IP地址范围内，否则Sub VLAN内的用户无法通信。

【命令格式】 subvlan-address-range start-ip end-ip
【参数说明】 start-ip：Sub VLAN的起始IP地址。
end-ip：Sub VLAN的最大IP地址。
【缺省配置】 没有IP地址范围
【命令模式】 VLAN模式
【使用指导】 可选配置。此命令用来划分Sub VLAN内用户IP地址使用范围。同一个Super VLAN的Sub VLAN的IP地址范围不可以有交叠。

Sub VLAN的IP地址范围必须在其所属Super VLAN的IP地址范围内，否则Sub VLAN内的用户无法通信。

Sub VLAN内的用户IP地址(无论静态分配还是DHCP静态分配)必须在这个范围内才能与其它VLAN的用户进行通信。

不能保证DHCP分配的IP地址都在这个范围内，这样就可能造成用户不能通信，所以该命令需要慎用。

##### 检验方法

各个Sub VLAN关联网关后，Sub VLAN内用户之间互ping能通。

##### 配置举例

以下配置举例，仅介绍Super VLAN相关的配置。

在网络中配置 Super VLAN ，使其 Sub VLAN 的用户使用同一网段，共享一个 IP 网关，节省 IP 地址。

【配置方法】 在核心交换机上配置Super VLAN必须配置部分。略
在接入交换机上配置对应核心交换机上Sub VLAN的普通VLAN。

```
A SwitchA#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
SwitchA(config)#vlan 2
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 10
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 20
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 30
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 2
SwitchA(config-vlan)#supervlan
SwitchA(config-vlan)#subvlan 10,20,30
SwitchA(config-vlan)#exit
SwitchA(config)#interface vlan 2
SwitchA(config-if-VLAN 2)#ip address 192.168.1.1 255.255.255.0
SwitchA(config)#vlan 10
SwitchA(config-vlan)#subvlan-address-range 192.168.1.10 192.168.1.50
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 20
SwitchA(config-vlan)#subvlan-address-range 192.168.1.60 192.168.1.100
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 30
SwitchA(config-vlan)#subvlan-address-range 192.168.1.110 192.168.1.150
SwitchA(config)#interface range gigabitEthernet 0/1,0/5,0/9
SwitchA(config-if-range)#switchport mode trunk
```

【检验方法】 使Source（ 192 .1 68 .1.1 0 ）与Dest（192.168.1.60）之间互ping能通。

```
A SwitchA(config-if-range)# show supervlan
supervlan id supervlan arp-proxy subvlan id subvlan arp-proxy subvlan ip range
------------ ------------------- ---------- ----------------- ---------
2 ON 10 ON 192.168.1.10 - 192.168.1.50
20 ON 192.168.1.60 - 192.168.1.100
30 ON 192.168.1.110 - 192.168.1.150
```

##### 常见错误

Super VLAN没有配置SVI和IP网关，导致Sub VLAN之间、Sub VLAN与其它VLAN之间不能通行。
关闭Super VLAN或者Sub VLAN的ARP代理功能，导致Sub VLAN的用户间不能跨VLAN通信。
配置了Sub VLAN的IP地址范围，但是给用户分配的IP地址不在该范围内。

### 6.5 监视与维护

##### 查看运行情况

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>打开 Super VLAN 配置。</td>         <td>show supervlan</td>     </tr> </table>

##### 查看调试信息

输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>打开 Super VLAN 调试开关。</td>         <td>debug bridge svlan</td>     </tr> </table>

## 7 Protocol VLAN 配置

### 7.1 概述

Protocol VLAN技术就是基于报文协议类型的VLAN分类技术，其可以将某一协议类型的空VLAN ID报文都划分到同一个VLAN。即交换机可以根据端口接收到的报文所属的协议类型以及封装格式，将收到的不携带VLAN 标记的报文，与用户设定的协议模板相匹配，匹配成功的自动分发到相应的VLAN中传输。Protocol VLAN共有两种类型：基于IP地址的VLAN分类和端口上的基于报文类型和以太网类型的VLAN分类两种VLAN分类技术， 后续说明文中将基于协议类型的Protocol VLAN简称为协议VLAN，基于IP地址类型的Protocol VLAN简称为子网VLAN。

下文仅介绍Protocol VLAN的相关内容。
协议只作用于Trunk、Hybrid模式下端口。

##### 协议规范

IEEE standard 802.1Q

### 7.2 典型应用

<table>     <tr>         <th>典型应用</th>         <th>场景描述</th>     </tr>     <tr>         <td>协议 VLAN 配置应用</td>         <td>实现不同协议报文的用户二层通信隔离，减少网络流量</td>     </tr>     <tr>         <td>子网 VLAN 配置应用</td>         <td>实现根据用户报文所属的 IP 网段确定其 VLAN 范围</td>     </tr> </table>

#### 7.2.1 协议 VLAN 配置应用

##### 应用场景

如下图所示，由Windows NT和Novell Netware操作系统互联的网络结构，办公区通过HUB与三层设备Switch A相连。在办公区内分散着不同的PC用户，一部分采用Windows NT操作系统，支持IP协议；一部分采用Novell Netware操作系统，支持IPX协议。整个办公区通过上链口Gi 0/3与外网以及服务器通信。
主要需求如下：

+ 实现Windows NT和Novell Netware操作系统的PC用户二层通信隔离，减少网络流量。

【注释】 SwitchＡ为交换机设备，端口Gi 0/3为Hybrid口。Gi0/1为Access口，所属VLAN 2；Gi0/2也为Access口，所属VLAN3。

##### 功能部署

+ 配置报文类型和以太网类型的profile（本例将支持IP协议的报文对应Profile 1，支持IPX协议的报文对应Profile 2）

+ 将Profile应用到上链口（本例对应为Gi 0/3）上，并与VLAN关联（本例将Profile 1关联VLAN 2，Profile 2关联VLAN
  3 ）。

配置协议VLAN的端口仅针对Trunk口和Hybrid口生效。

#### 7.2.2 子网 VLAN 配置应用

##### 应用场景

如下图所示，办公区A和办公区B通过HUB与三层设备Switch A相连：办公区A内，分布着固定网段的办公用户，统一基于端口划分属于一个VLAN；办公区B内，分布着两个网段的办公用户，无法基于固定端口划分VLAN。
主要需求如下：

对于办公区B内的PC用户，Switch A可以根据报文所属的IP网段确定其VLAN范围。

【注释】 SwitchＡ为交换机设备，端口G0/1为Access口，所属VLAN 2；G0/2为Access口，所属VLAN 3 ；G0/3为Hybrid口。

##### 功能部署

+ 全局配置子网VLAN（本例将IP网段为192.168.1.1/24划分属于VLAN 3，IP网段为192.168.2.1/24划分属于VLAN 2），并在上链口（本例为Gi 0/3）使能子网功能

配置子网VLAN的端口仅针对Trunk口和Hybrid口生效。^

### 7.3 功能详解

##### 基本概念

######  Protocol VLAN

Protocol VLAN技术就是基于报文协议类型的VLAN分类技术，其可以将某一协议类型的空VLAN ID报文都划分到同一VLAN。设备端口接收到的报文，都需要进行VLAN分类，使报文属于唯一的个VLAN，有以下三种可能：

+ 如果报文是空VLAN ID报文（UNTAG或Priority报文），而设备仅支持基于端口的VLAN分类的话，报文所添加TAG的VLAN ID将是输入端口的PVID。

+ 如果报文是空VLAN ID报文（UNTAG或Priority报文），而设备支持基于报文协议类型的VLAN分类的话，报文所添加TAG的VLAN ID将会从输入端口上的协议组配置相对应的VLAN ID集中选取，而如果报文的协议类型与输入端口上的所有协议组配置都不相符的话，将按照基于端口的VLAN分类来分配VLAN ID。

+ 如果报文是TAG报文，其所属VLAN分类由TAG中的VLAN ID决定。

其中子网VLAN只有全局配置 ，即端口上配置只有开启/关闭Protocol VLAN功能。协议VLAN全局配置报文类型，接口上配置对应报文类型分配VLAN。如下所示：

+ 如果输入报文为空VLAN ID报文，且输入报文的IP地址匹配用户配置的IP地址的话，该报文将被划分到用户配置的子网VLAN内。

+ 如果输入报文为空VLAN ID报文，且输入报文的报文类型和以太网类型，匹配用户配置在输入端口上的报文类型和以太网类型的话，该报文将被划分到用户配置的协议VLAN内。

######  Protocol VLAN 优先级

子网VLAN优先级高于协议VLAN，即同时配置了子网VLAN和协议VLAN，且输入报文同时符合两者的话，将是子网VLAN

分配起作用。

**功能特性**

<table>     <tr>         <th>功能特性</th>         <th>作用</th>     </tr>     <tr>         <td>根据报文类型自动划分 VLAN</td>         <td>将网络中提供的服务类型与 VLAN 相绑定，或将指定 IP 网段发出的报文在指定的 VLAN 中传送，方便管理与维护。</td>     </tr> </table>



#### 7.3.1 根据报文类型自动划分 VLAN

##### 工作原理

设置规则到硬件，并在端口使能规则，且只有在端口上使能后，才真正生效；这些规则包括报文类型，报文的IP地址；当端口上收到符合规则的，不带VLAN标记的数据流报文，将其自动划分到规则中指定的VLAN中传送。端口关闭功能则不带VLAN标记的数据流报文遵守端口上配置，都划分到native VLAN中。



### 7.4 配置详解

<table>
  <thead>
    <tr>
      <th>配置项</th>
      <th colspan="2">配置建议 & 相关命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">配置协议 VLAN 功能</td>
      <td colspan="2">必须配置。用于使能 Protocol-VLAN 基于报文类型和以太网类型分类功能。</td>
    </tr>
    <tr>
      <td>protocol-vlan profile num frame-type [ type ] ether-type [ type ] </td>
      <td>配置报文类型和以太网类型的 profile。</td>
    </tr>
    </tr>
    <tr>
      <td>protocol-vlan profile num ether-type [ type ]</td>
      <td>(某些型号不支持 frame 识别)配置以太网类型的 profile。</td>
    </tr>  
    <tr>
      <td>protocol-vlan profile num vlan vid</td>
      <td>(接口模式下)端口上应用协议 VLAN。</td>
    </tr>  
    <tr>
      <td rowspan="3">配置子网 VLAN 功能</td>
      <td colspan="2">必须配置。用于使能 Protocol-VLAN 基于 ip 地址 VLAN 分类功能</td>
    </tr>
    <tr>
      <td>protocol-vlan ipv4 address mask address vlan vid </td>
      <td>配置 IP 地址、子网掩码以及 VLAN 分类。</td>
    </tr>
    <tr>
      <td>protocol-vlan ipv4 </td>
      <td>(接口模式下)端口上使能子网 VLAN。</td>
    </tr>
  </tbody>
</table>


#### 7.4.1 配置协议 VLAN 功能

##### 配置效果

将网络中提供的服务类型与 VLAN 相绑定，方便管理和维护。

##### 注意事项

+ 用户最好在配置好VLAN、端口的Trunk、Hybrid 、Access和AP属性后，再配置Protocol VLAN；

+ 如果用户在Trunk或Hybrid口上配置了Protocol VLAN， 那么用户需要报文Trunk和Hybrid口的许可VLAN列表包含Protocol VLAN相关的所有VLAN。

##### 配置方法

######  全局配置协议 VLAN

+ 必须配置。

+ 只有全局配置上，接口上才能应用对应协议VLAN。

【命令格式】 protocol-vlan profile num frame-type type ether-type type
【参数说明】 num：profile索引
type：报文类型和以太网类型
【缺省配置】 默认关闭
【命令模式】 全局模式
【使用指导】 只有在Protocol-VLAN全局配置存在的情况，Protocol-VLAN接口上才能配置协议VLAN。删除全局配置时，会删除对应索引的所有接口协议VLAN配置。

######  切换端口模式为 trunk / hybrid 模式

+ 必须配置，协议VLAN功能只有在trunk / hybrid模式的端口上才生效。

######  端口上使能协议 VLAN

+ 必须配置，默认为关闭应用。

+ 只有接口上应用，才真正使能协议VLAN。

【命令格式】 protocol-vlan profile num vlan vid
【参数说明】 num：profile索引
vid ：VLAN ID， 1 - 产品支持的最大VLAN
【缺省配置】 默认关闭
【命令模式】 接口模式
【使用指导】 接口必须为trunk / hybrid 模式。

##### 检验方法

show protocol-vlan profile 查看配置信息。

##### 配置举例

######  在拓扑环境中开启协议 VLAN 功能

【配置方法】 在交换机A配置用户通信的VLAN 2 - 3 。
在交换机A全局配置协议VLAN （本例将支持IP协议的报文对应Profile 1，支持IPX协议的报文对应Profile 2 ）；并在上链口（本例为Gi 0/3）使能协议VLAN功能，完成协议与VLAN关联（本例将Profile 1关联VLAN 2 ，Profile 2关联VLAN 3）。
端口Gi 0/1为Access口，所属VLAN 2；Gi0/2为Access口，所属VLAN 3；Gi0/3为Hybrid口。必须保证Hybrid口的untagged VLAN许可列表包含用户通信的VLAN。
1 ：创建用户网络通信的VLAN 2 - 3 。

```
A# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
A(config)# vlan range 2-3
```

2 ：配置端口模式

```
A(config)#interface gigabitEthernet 0/1
A(config-if-GigabitEthernet 0/1)#switchport
A(config-if-GigabitEthernet 0/1)#switchport access vlan 2
A(config-if-GigabitEthernet 0/1)#exit
A(config)#interface gigabitEthernet 0/2
A(config-if-GigabitEthernet 0/ 2 )#switchport
A(config-if-GigabitEthernet 0/2)#switchport access vlan 3
A(config-if-GigabitEthernet 0/2)#exit
A(config)# interface gigabitEthernet 0/3
A(config-if-GigabitEthernet 0/ 3 )#switchport
A(config-if-GigabitEthernet 0/ 3 )# switchport mode hybrid
A(config-if-GigabitEthernet 0/ 3 )# switchport hybrid allowed vlan untagged 2- 3
```

3 ：全局配置协议VLAN。
IP、IPX协议配置相应的Profile 1、 2 。（此处假设报文使用EthernetII封装，IP和IPX分别对应的以太网类型为0X0800、0X8137）

```
A(config)#protocol-vlan profile 1 frame-type ETHERII ether-type 0x0800
A(config)#protocol-vlan profile 2 frame-type ETHERIIether-type 0x8137
```

4 ：将Profile 1、 2 应用到端口Gi 0/3上，划分为VLAN 2和VLAN 3。

```
A(config)# interface gigabitEthernet 0/3
A(config-if-GigabitEthernet 0/3) #protocol-vlan profile 1 vlan 2
A(config-if-GigabitEthernet 0/3) #protocol-vlan profile 2 vlan 3
```

4 ：将Profile 1、 2 应用到端口Gi 0/3上，划分为VLAN 2和VLAN 3。
A(config)# interface gigabitEthernet 0/3
A(config-if-GigabitEthernet 0/3) #protocol-vlan profile 1 vlan 2
A(config-if-GigabitEthernet 0/3) #protocol-vlan profile 2 vlan 3

【检验方法】 查看设备上Protocol VLAN配置是否正确。

```
A 
A(config)#show protocol-vlan profile
profile frame-type ether-type/DSAP+SSAP interface vlan
------- ---------------- ---------------------- --------------- ----
1 ETHERII 0x0800 Gi0/ 3 2
2 ETHERII 0x8137 Gi0/3 3
```

##### 常见配置错误

+ 设备连接的端口不是Trunk/Hybrid模式。

+ 设备连接的端口许可VLAN列表不包含用户通信的VLAN。

+ 端口未使能协议VLAN功能

#### 7.4.2 配置子网 VLAN 功能

##### 配置效果

将指定网段或 IP 地址发出的报文在指定的VLAN 中传送。

##### 注意事项

+ 用户最好在配置好VLAN、端口的Trunk、Hybrid 、Access和AP属性后，再配置Protocol VLAN；

+ 如果用户在Trunk或Hybrid口上配置了Protocol VLAN， 那么用户需要报文Trunk和Hybrid口的许可VLAN列表包含Protocol VLAN相关的所有VLAN。

##### 配置方法

######  全局配置子网 VLAN

+ 必须配置。

+ 只有全局配置上，接口上才能应用对应子网VLAN。

【命令格式】 protocol-vlan ipv4 address mask address vlan vid
【参数说明】 address ：ip地址
vid ：VLAN ID， 1 - 产品支持的最大VLAN
【缺省配置】 默认关闭
【命令模式】 全局模式
【使用指导】 在Protocol-VLAN未全局使能的状态下，接口也可配置使能，但只有在Protocol-VLAN全局配置存在的情况，Protocol-VLAN配置子网VLAN才有作用。

######  切换端口模式为 trunk / hybrid 模式

+ 必须配置，子网VLAN功能只有在trunk / hybrid模式的端口上才生效。

######  端口上使能子网 VLAN

+ 必须配置，默认为关闭应用。

+ 只有接口上应用，才真正使能子网VLAN功能。

【命令格式】 protocol-vlan ipv4
【参数说明】 -
【缺省配置】 默认关闭
【命令模式】 接口模式
【使用指导】 接口必须为trunk / hybrid 模式。

##### 检验方法

show protocol-vlan ipv4 查看配置信息。

##### 配置举例

######  在拓扑环境中开启子网 VLAN 功能

【网络环境】
图 7 - 4

【配置方法】 

+ 在交换机A配置用户通信的VLAN 2 - 3
+ 在交换机A全局配置子网VLAN（本例将IP网段为192.168.1.1/24划分属于VLAN 3，IP网段为192.168.2.1/24划分属于VLAN 2），并在上链口（本例为Gi 0/3）使能子网VLAN功能 
+ 端口Gi 0/1为Access口，所属VLAN 2；Gi0/2为Access口，所属VLAN 3；Gi0/3为Hybrid口。必须保证Hybrid口的untagged VLAN许可列表包含用户通信的VLAN。

```
A 
1 ：创建用户网络通信的VLAN 2 - 3 。
A# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
A(config)# vlan range 2- 3
2 ：配置端口模式
A(config)#interface gigabitEthernet 0/1
A(config-if-GigabitEthernet 0/1)#switchport
A(config-if-GigabitEthernet 0/1)#switchport access vlan 2
A(config-if-GigabitEthernet 0/1)#exit
A(config)#interface gigabitEthernet 0/2
A(config-if-GigabitEthernet 0/2)#switchport
A(config-if-GigabitEthernet 0/2)#switchport access vlan 3
A(config-if-GigabitEthernet 0/2)#exit
A(config)# interface gigabitEthernet 0/3
A(config-if-GigabitEthernet 0/3)#switchport
A(config-if-GigabitEthernet 0/3)# switchport mode hybrid
A(config-if-GigabitEthernet 0/3)# switchport hybrid allowed vlan untagged 2- 3
3 ：全局配置子网VLAN。
A(config)# protocol-vlan ipv4 192.168.1.0 mask 255.255.255.0 vlan 3
A(config)# protocol-vlan ipv4 192.168. 2 .0 mask 255.255.255.0 vlan 2
4 ：接口上使能子网VLAN，默认关闭。
A(config-if-GigabitEthernet 0/ 3 )# protocol-vlan ipv4
```




【检验方法】 查看设备上Protocol VLAN配置是否正确。

```
A A# show protocol-vlan ipv4
ip mask vlan
--------------- --------------- ----
192.68.1.0 255.255.255.0 3
192.168.2.0 255.255.255.0 2
-------------------- -----------
interface ipv4 status
Gi0/ 3 enable
```

##### 常见配置错误

+ 设备连接的端口不是Trunk/Hybrid模式。

+ 设备连接的端口许可VLAN列表不包含用户通信的VLAN。

+ 端口未使能子网VLAN

### 7.5 监视与维护

##### 查看运行情况

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>显示 Protocol VLAN 的内容</td>         <td>show protocol-vlan</td>     </tr> </table>

##### 查看调试信息

输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>打开Protocol VLAN debug 开关</td>         <td> debug bridge protvlan</td>     </tr> </table>

## 8 Private VLAN

### 8.1 Private VLAN 技术

私有VLAN(Private VLAN)将一个VLAN的二层广播域划分成多个子域，每个子域都由一个私有VLAN对组成：主VLAN(Primary VLAN)和辅助VLAN(Secondary VLAN)。

一个私有VLAN域可以有多个私有VLAN对，每一个私有VLAN对代表一个子域。在一个私有VLAN域中所有的私有VLAN对共享同一个主VLAN。每个子域的辅助VLAN ID不同。

服务提供商如果给每个用户一个VLAN，则由于一台设备支持的VLAN数最大只有 4096 而限制了服务提供商能支持的用户数；在三层设备上，每个VLAN被分配一个子网地址或一系列地址，这种情况导致IP地址的浪费。Private VLAN技术可以很好的同时解决以上两种问题，后续说明文中将Private VLAN简称为PVLAN。

### 8.2 典型应用

<table>     <tr>         <th>典型应用</th>         <th>场景描述</th>     </tr>     <tr>         <td>PVLAN 跨设备二层应用</td>         <td>企业内用户之间可以进行通信，企业间用户通信隔离。</td>     </tr>     <tr>         <td>PVLAN 单台设备三层应用</td>         <td>所有企业用户共享一个网关地址，可以与外网通信。</td>     </tr> </table>

#### 8.2.1 PVLAN 跨设备二层应用

**应用场景**

如下图所示，在主机托管业务运营网络中，各企业用户通过设备Switch A、Switch B接入网络。主要需求如下：

+ 企业内用户之间可以进行通信，企业间用户通信隔离

所有企业用户共享一个网关地址，可以与外网通信。

【注释】 Switch A、B为接入交换机。
跨设备运行PVLAN，需要将相连的端口配置为Trunk Port，将A的Gi 0/5和B的Gi 0/1均配置为Trunk Port。
与网关相连的A的Gi 0/1需要配置为Promiscuous Port；
网关设备Gi 0/1口可以配置为Trunk Port或者Hybrid Port，且Native VLAN是PVLAN的Primary VLAN。

##### 功能部属

+ 将所有企业配置属于同一个PVLAN（本例为Primary VLAN 99），所有企业用户均通过该VLAN共享一个三层接口，实
  现外网通信。
+ 如果企业内有多个用户，可以将各企业划分属于不同的Community VLAN，即将相关企业用户连接的端口配置为Community VLAN的host Port，实现企业内用户互相通信，企业间用户通信隔离。
+ 如果企业内仅有一个用户，可以将这些企业的该用户划分属于一个Isolated VLAN的host Port，实现企业间用户通信隔离。

#### 8.2.2 PVLAN 单台设备三层应用

如下图所示，在主机托管业务运营网络中，各企业用户通过三层设备Switch A接入网络。主要需求如下：

+ 企业内用户之间可以通信，企业间用户通信隔离。
+ 所有企业用户都可以访问服务器 
+ 所有企业用户共享一个网关地址，可以与外网通信。

【注释】 A为网关交换机。
单台设备连接时，为了各企业用户能与服务器通信，连接服务器的端口Gi 0/7配置为Promiscuous Port。
为了用户能与外网通信，需要将Primary VLAN和Secondary VLAN进行三层映射。

##### 功能部属

+ 将直连服务器的端口设置为Promiscuous Port，所有企业用户都可以通过Promiscuous Port和服务器通信。

+ 在三层设备（本例为Switch A）配置PVLAN的网关地址（本例配置VLAN 2的SVI为192.168.1.1/24），并配置Primary VLAN和Secondary VLAN的三层接口映射关系，所有企业用户可以通过这个网关地址与外网通信。

#### 8.3 功能详解

##### 基本概念

######  PVLAN

PVLAN中包含了三种类型的VLAN：主VLAN(Primary vlan) 、隔离VLAN(Isolated VLAN)、群体VLAN(Community VLAN)。一个私有VLAN域中只有一个主VLAN，辅助VLAN实现同一个私有VLAN域中的二层隔离，有两种类型的辅助VLAN。

######  隔离 VLAN

隔离VLAN(Isolated VLAN)：同一个隔离VLAN中的端口不能互相进行二层通信。一个私有VLAN域中只有一个隔离VLAN。

######  群体 VLAN

群体VLAN(Community VLAN)：同一个群体VLAN中的端口可以互相进行二层通信，但不能与其它群体VLAN中的端口进行二层通信。一个私有VLAN域中可以有多个群体VLAN。

######  PVLAN 的二层关联

PVLAN的三种VLAN必须进行二层关联才能构成PVLAN对，主VLAN才有了指定的辅助VLAN，辅助VLAN才有了指定的主VLAN。主VLAN和辅助VLAN之间是一对多的关系。

######  PVLAN 的三层关联

PVLAN中只有主VLAN可以创建三层口SVI，辅助VLAN必须通过与主VLAN三层关联后，辅助VLAN内的用户才能进行三层通信，否则仅能二层通信。

######  隔离端口 (Isolated Port)

隔离VLAN中的端口，只能和混杂口通信。隔离端口接受到的报文可允许转发到Trunk Port，但 Trunk Port接收到vid是IsolatedVLAN的报文不能向隔离端口转发。

######  群体端口 (Community Port)

属与Community VLAN的端口，同一个Community VLAN的群体端口可以互相通讯，也可以与混杂口通讯。不能与其它群体VLAN中的群体端口及隔离VLAN中的隔离端口通讯。

######  混杂端口（ Promiscuous Port ）

属于主VLAN的端口，可以和任意端口通信，包括同一个PVLAN域中辅助VLAN的隔离端口和群体端口。

######  混杂 Trunk 端口 (Promiscuous Trunk Port)

可以同时是多个普通VLAN和多个PVLAN的成员端口，可以和同一VLAN内的任意端口通讯。

+ 在普通VLAN中，报文转发遵循802.1Q规则；
+ 在PVLAN中，从混杂TRUNK端口转发出的带TAG报文，其VID如果是辅助VLAN ID，会转成相应主VLAN的VID后再输出。

######  隔离 Trunk 端口（ Isolated Trunk Port ）

可以同时是多个普通VLAN和多个PVLAN的成员端口。

+ 在隔离VLAN中，只能与混杂口通讯。
+ 在群体VLAN中，可以与同一个群体VLAN的群体端口通讯，也可以同混杂口通讯。
+ 在普通VLAN中，遵循802.1Q规则。
+ 隔离TRUNK端口接收到的Isolated VLAN ID的报文可允许转发到Trunk Port，但 Trunk Port接收到vid是Isolated VLAN的报文不能向隔离端口转发。
+ 从隔离TRUNK端口转发出的带TAG报文，其VID如果是主VLAN ID，会转成相应辅助VLAN的VID后再输出。

PVLAN中，只有主VLAN可以创建SVI接口，辅助VLAN不可以创建SVI。

PVLAN中的端口可以作为镜像源端口，不可以作为镜像目的端口。

##### 功能特性

<table>     <tr>         <th>功能特性</th>         <th>作用</th>     </tr>     <tr>         <td>PVLAN 二层隔离和节省 IP 地址</td>         <td>通过配置各种 PVLAN 类型的端口，实现 VLAN 中间用户的互通和隔离。主 VLAN 和辅助 VLAN 二层映射后，只能支持一些二层通信。如果要进行三层通信，辅助 VLAN 的用户需要借助主 VLAN 的 SVI 口来进行三层通信。</td>     </tr> </table>

#### 8.3.1 PVLAN 二层隔离和节省 IP 地址

通过将用户加入PVLAN的各个子域，可以隔离企业间、企业用户间的通信。

**工作原理**

通过配置PVLAN、PVLAN的主VLAN和子VLAN二三层关联、以及用户、外网设备、服务器等连接的端口设置为PVLAN的各种端口，实现各子域的划分，各子域用户与外网和服务器的通信。

######  各种端口类型间的报文转发关系

<table>     <tr>         <th></th>         <th>混杂端口</th>         <th>隔离端口</th>         <th>群体端口</th>         <th>隔离 TRUNK 端口（同 VLAN 内）</th>         <th>混杂 TRUNK 端口（同 VLAN 内）</th>         <th>TRUNK 端口（同 VLAN 内）</th>     </tr>     <tr>         <td>混杂端口</td>         <td>通</td>         <td>不通</td>         <td>通</td>         <td>通</td>         <td>通</td>         <td>通</td>     </tr>     <tr>         <td>隔离端口</td>         <td>通</td>         <td>不通</td>         <td>不通</td>         <td>通</td>         <td>通</td>         <td>通</td>     </tr>     <tr>         <td>群体端口</td>         <td>通</td>         <td>不通</td>         <td>通</td>         <td>通</td>         <td>通</td>         <td>通</td>     </tr>     <tr>         <td>隔离 TRUNK 端口（同 VLAN 内）</td>         <td>通</td>         <td>不通</td>         <td>通</td>         <td>不通（隔离 VLAN 内不通，非隔离 VLAN 内通）</td>         <td>通</td>         <td>通</td>     </tr>     <tr>         <td>混杂 TRUNK 端口（同 VLAN 内）</td>         <td>通</td>         <td>通</td>         <td>通</td>         <td>通</td>         <td>通</td>         <td>通</td>     </tr>     <tr>         <td>TRUNK 端口（同 VLAN 内）</td>         <td>通</td>         <td>不通</td>         <td>通</td>         <td>不通（隔离 VLAN 内不通，非隔离 VLAN 内通）</td>         <td>通</td>         <td>通</td>     </tr> </table>

######  各种端口类型间的报文转发后 VLAN TAG 变化关系

<table>     <tr>         <th></th>         <th>混杂端口</th>         <th>隔离端口</th>         <th>群体端口</th>         <th>隔离 TRUNK 端口（同 VLAN 内）</th>         <th>混杂 TRUNK 端口（同 VLAN 内）</th>         <th>TRUNK 端口（同 VLAN 内）</th>     </tr>     <tr>         <td>混杂端口</td>         <td>不变</td>         <td>不变</td>         <td>不变</td>         <td>加上辅助 VLAN ID</td>         <td>加上主 VLAN ID TAG，其它非私有 VLAN 内不变。</td>         <td>加上主 VLAN ID TAG，其它非私有 VLAN 内不变。</td>     </tr>     <tr>         <td>隔离端口</td>         <td>NA</td>         <td>NA</td>         <td>NA</td>         <td>NA</td>         <td>加上主 VLAN ID TAG，加 上 隔 离 VLAN ID TAG</td>         <td>NA</td>     </tr>     <tr>         <td>群体端口</td>         <td>NA</td>         <td>不变</td>         <td>不变</td>         <td>加上群体 VLAN ID TAG</td>         <td>加上主 VLAN ID TAG，加 上 群 体 VLAN ID TAG</td>         <td>不变</td>     </tr>     <tr>         <td>隔离 TRUNK 端口（同 VLAN 内）</td>         <td>去 掉 VLAN TAG</td>         <td>NA</td>         <td>去 掉 VLAN TAG</td>         <td>非隔离 VLAN 内不变。</td>         <td>加上主 VLAN ID TAG，其它非私有 VLAN 内不变。</td>         <td>不变</td>     </tr>     <tr>         <td>混杂 TRUNK 端口（同 VLAN 内）</td>         <td>去 掉 VLAN TAG</td>         <td>不变</td>         <td>不变</td>         <td>加上辅助 VLAN ID</td>         <td>加上主 VLAN ID TAG，其它非私有 VLAN 内不变。</td>         <td>不变</td>     </tr>     <tr>         <td>TRUNK 端口（同 VLAN 内）</td>         <td>去 掉 VLAN TAG</td>         <td>NA</td>         <td>去 掉 VLAN TAG</td>         <td>主 VLAN 内转 成 辅 助VLAN ID，其它非隔离VLAN 内不变。</td>         <td>加上主 VLAN ID TAG，其它非私有VLAN内不变。</td>         <td>不变</td>     </tr>
<tr>         <td>交换机 CPU</td>         <td>Untag</td>         <td>Untag</td>         <td>Untag</td>         <td>加上辅助 VLAN ID TAG。</td>         <td>加上主 VLAN ID TAG，其它非私有VLAN内不变。</td>         <td>加上主VLAN ID TAG</td>     </tr>
</table>




### 8.4 产品说明

S6000E不支持隔离TRUNK口和混杂TRUNK口。

### 8.5 配置详解

<table>
  <thead>
    <tr>
      <th>配置项</th>
      <th colspan="2">配置建议 & 相关命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="12">配置PVLAN 基本功能</td>
      <td colspan="2">必选配置</td>
    </tr>
    <tr>
      <td>private-vlan {community | isolated | primary}
</td>
      <td>配置 PVLAN 类型。</td>
    </tr>
    <tr>
      <td colspan="2">必选配置，用于实现 PVLAN 的主 VLAN 和辅助 VLAN 的二层关联，构成 PVLAN 对</td>
    </tr>
    <tr>
      <td>private-vlan association {svlist | add svlist | remove svlist}
 </td>
      <td>主 VLAN 和辅助 VLAN 二层关联，这样才构成PVLAN 对。
</td>
    </tr>
    <tr>
        <td colspan="2">可选配置，用于将用户划分到隔离 VLAN 或者群体 VLAN</td>
    </tr>
    <tr>
      <td>switchport mode private-vlan host</td>
      <td>配置成私有 VLAN host 端口</td>
    </tr>
    <tr>
      <td>switchport private-vlan host-association p_vid s_vid </td>
      <td>关联二层端口与 PVLAN，将端口划分到相关子域</td>
    </tr>
    <tr>
        <td colspan="2">可选配置，将端口配置为混杂端口</td>
    </tr>
     <tr>
      <td>Switchport mode private-vlan promiscuous</td>
      <td>配置成私有 VLAN 混杂端口</td>
    </tr>
    <tr>
        <td>switchport private-vlan mapping p_vid
{ svlist| add svlist | remove svlist }</td>
        <td>配置私有 VLAN 混杂端口所在的 Primary VLAN 以 Secondary VLAN 列表。配置之后对应 PVLAN 的报文才能通过这个端口通信。
</td>
    </tr>
    <tr>
      <td colspan="2">可选配置。用于实现辅助 VLAN 的用户的三层通信。
</td>
    </tr>      
    <tr>
      <td>private-vlan mapping { svlist | add svlist |
remove svlist }
</td>
      <td>创建 PVLAN 并进行二层关联后，配置主VLAN 的 SVI，并将主 VLAN 和辅助 VLAN 进行三层关联，子 VLAN 可以借助主 VLAN 的SVI 进行三层通信。
。</td>
    </tr>
  </tbody>
</table>


###### 8.5.1 配置 PVLAN 基本功能

##### 配置效果

+ 构成PVLAN子域，实现企业和企业用户间的隔离；
+ 多个辅助VLAN三层映射到主VLAN，多个VLAN利用同一个IP网关，节省IP地址。

##### 注意事项

+ 在配置主VLAN和辅助VLAN后，必须进行二层关联才能构成PVLAN子域。

+ 必须将用户连接的端口配置为特定PVLAN端口类型，用户才能加入对应的子域，才能实现真正的用户隔离。
+ 同时连接外网和服务器的接口必须配置成混杂口，上下行报文转发才能正常。
+ 辅助VLAN只有与主VLAN进行三层映射后才能借助主VLAN的SVI进行三层通信。

##### 配置方法

######  配置 PVLAN

+ 必须配置。
+ 需要配置主VLAN和辅助VLAN，这两种VLAN不能独立存在。
+ private-vlan { community | isolated | primary }命令可以将VLAN配置为PVLAN的主VLAN和辅助VLAN。

【命令格式】 private-vlan { community | isolated | primary }
【参数说明】 community：指定VLAN类型为群体VLAN。
isolated：指定VLAN类型为隔离VLAN。
primary：指定VLAN类型为PVLAN对的主VLAN。
【缺省配置】 VLAN属于普通VLAN，不具备Private VLAN的属性
【命令模式】 VLAN模式
【使用指导】 此命令用来指定PVLAN的主VLAN和辅助VLAN。

######  PVLAN 的二层关联

+ 必须配置。

+ PVLAN的主VLAN和辅助VLAN进行二层关联后才能构成PVLAN子域，才能配置相应的隔离口、群体口以及三层关联等。

+ 缺省情况下，配置各种PVLAN后，主VLAN和辅助VLAN之间没有任何关系，都是一个个单独的个体，只有进行二层关联后主VLAN才有辅助VLAN，辅助VLAN才有主VLAN。

使用private-vlan association { svlist | add svlist | remove svlist }可以增加或取消PVLAN的主VLAN和辅助VLAN的二层关联，二层关联后才能构成一个PVLAN子域，一旦取消二层关联对应的子域也就不存在了。另外不进行二层关联，后续的各种隔离端口和混杂口配置关联PVLAN对时会失败或取消已经配置的端口关联VLAN。
【命令格式】 private-vlan association { svlist | add svlist | remove svlist }
【参数说明】 svlist：指定需要关联或解关联的辅助VLAN列表。
add svlist：增加关联的辅助VLAN。
remove svlist：解除svlist与主VLAN的关联。
【缺省配置】 缺省主VLAN和辅助VLAN之间没有关联
【命令模式】 PVLAN的主VLAN模式
【使用指导】 此命令用来进行主VLAN和辅助VLAN的二层关联，构成PVLAN对。每个主VLAN只能关联一个Isolated VLAN，但可以关联多个Commuity VLAN。

######  PVLAN 的三层关联

+ 如果辅助VLAN域内的用户需要进行三层通信，需要给主VLAN配置一个三层口SVI，然后在SVI口上配置主VLAN和
  辅助VLAN的三层。

+ 缺省情况下，仅PVLAN的主VLAN可以配置三层口SVI，辅助VLAN不能进行三层通信。

+ 如果PVLAN辅助VLAN内的用户要进行三层通信，需要借助于主VLAN的SVI来收发包。

+ 使用private-vlan mapping { svlist | add svlist | remove svlist }命令可以增加或取消PVLAN的主VLAN和辅助VLAN之间的三层关联。三层关联后，辅助VLAN内的用户才可以与外网进行三层通信。关闭后辅助VLAN内的用户不能进行三层通信。

【命令格式】 private-vlan mapping { svlist | add svlist | remove svlist }
【参数说明】 svlist：三层映射的辅助VLAN列表。
add svlist：增加三层口关联的辅助VLAN。
remove svlist：取消三层口关联的辅助VLAN
【缺省配置】 缺省主VLAN和辅助VLAN之间没有关联
【命令模式】 主VLAN的接口模式
【使用指导】 必须先为主VLAN配置三层口SVI。
仅主VLAN可以配置三层口。
关联的辅助VLAN必须和主VLAN是二层关联的。

######  隔离端口和群体端口

+ 配置PVLAN的主VLAN和辅助VLAN并进行二层关联后，还需要对用户连接的设备端口进行划分，才能真正对用户所在
  的子域进行划分。 
+ 如果企业内仅有一个用户，可以考虑将用户连接的端口设置成隔离端口。 
+ 如果企业内有多个用户，可以讲用户连接的端口设置成群体端口。

【命令格式】 switchport mode private-vlan host
switchport private-vlan host-association p_vid s_vid
【参数说明】 p_vid：PVLAN对中的主VLAN id。
s_vid：PVLAN对中的辅助VLAN id，如果为Isolated VLAN，则该端口为隔离端口；如果为Community VLAN，则该端口为群体端口。
【缺省配置】 接口默认为access模式；没有关联Private VLAN对
【命令模式】 两个命令都在接口模式
【使用指导】 需要上面两条命令来完成，并且配置为隔离端口或混杂端口前，端口的模式必须先配置成host口模式。是配置成隔离端口还是群体端口，视s_vid参数而定。p_vid 和s_vid 必须是有二层关联的PVLAN对。一个host口仅能关联一对PVLAN对。

######  混杂端口

+ 从功能详解章节各种端口收发报文的规则表格可见PVLAN的单一端口类型不能保证上下行报文转发对称，为了保证用户能正常访问外网和服务器，一般需要将连接外网和服务器的端口配置成混杂口。

【命令格式】 switchport mode private-vlan promiscuous
switchport private-vlan mapping p_vid{ svlist | add svlist | remove svlist }
【参数说明】 p_vid：PVLAN对的主VLAN。
svlist：混杂端口关联的辅助VLAN，必须和p_vid是二层关联的。
add svlist：增加端口关联的辅助VLAN。
remove svlist：取消端口关联的辅助VLAN
【缺省配置】 接口默认为access模式；混杂口无辅助VLAN
【命令模式】 接口模式
【使用指导】 必须向将端口模式配置成混杂模式。端口必须与PVLAN对进行关联，否则不起作用。一个混杂口可以关联一个主VLAN内的过个PVLAN对，但不能关联多个主VLAN。

##### 检验方法

使PVLAN端口内的用户能按照PVLAN的端口转发规则进行收发报文，达到隔离作用；通过三层关联，同一个PVLAN内的主VLAN和辅助VLAN共用一个网关IP进行三层通信。

##### 配置举例

以下配置举例，介绍与跨设备二层应用的配置。

######  在跨二层设备上应用 PVLAN

【配置方法】 

+ 将所有企业配置属于同一个PVLAN（本例为Primary VLAN 99），所有企业用户均通过该VLAN共享一个三层接口，实现外网通信。
+ 如果企业内有多个用户，可以将各企业划分属于不同的Community VLAN（本例将企业A划分属于Community VLAN 100），实现企业内用户互相通信，企业间用户通信隔离。

如果企业内仅有一个用户，可以将这些企业划分属于同一个Isolated VLAN（本例将企业B和C划分属于Isolated VLAN 101），实现企业间用户通信隔离。

```
A SwitchA#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
SwitchA(config)#vlan 99
SwitchA(config-vlan)#private-vlan primary
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 100
SwitchA(config-vlan)#private-vlan community
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 101
SwitchA(config-vlan)#private-vlan isolated
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 99
SwitchA(config-vlan)#private-vlan association 100- 101
SwitchA(config-vlan)#exit
SwitchA(config)#interface range gigabitEthernet 0/2- 3
SwitchA(config-if-range)#switchport mode private-vlan host
SwitchA(config-if-range)#switchport private-vlan host-association 99 100
SwitchA(config-if-range)#exit
SwitchA(config)#interface gigabitEthernet 0/4
SwitchA(config-if-GigabitEthernet 0/4)#switchport mode private-vlan host
SwitchA(config-if-GigabitEthernet 0/4)#switchport private-vlan host-association 99 101
SwitchA(config)#interface gigabitEthernet 0/5
SwitchA(config-if-GigabitEthernet 0/5)#switchport mode trunk
SwitchA(config-if-GigabitEthernet 0/5)#exit
B SwitchB#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
SwitchB(config)#vlan 99
SwitchB(config-vlan)#private-vlan primary
SwitchB(config-vlan)#exit
SwitchB(config)#vlan 100
SwitchB(config-vlan)#private-vlan community
SwitchB(config-vlan)#exit
SwitchB(config)#vlan 101
SwitchB(config-vlan)#private-vlan isolated
SwitchB(config-vlan)#exit
SwitchB(config)#vlan 99
SwitchB(config-vlan)#private-vlan association 100- 101
SwitchB(config-vlan)#exit
SwitchB(config)#interface gigabitEthernet 0/2
SwitchB(config-if-GigabitEthernet 0/2)#switchport mode private-vlan host
SwitchB(config-if-GigabitEthernet 0/2)# switchport private-vlan host-association 99 101
SwitchB(config-if-GigabitEthernet 0/2)#exit
SwitchB(config)#interface gigabitEthernet 0/3
SwitchB(config-if-GigabitEthernet 0/3)#switchport mode private-vlan host
SwitchB(config-if-GigabitEthernet 0/3)# switchport private-vlan host-association 99 100
SwitchB(config-if-GigabitEthernet 0/3)#exit
SwitchB(config)#interface gigabitEthernet 0/1
SwitchB(config-if-GigabitEthernet 0/1)#switchport mode trunk
SwitchB(config-if-GigabitEthernet 0/1)#exit
```



【检验方法】 检查VLAN和端口上配置是否正确。根据功能详解中的转发规则查看报文转发是否正确。

```
A SwitchA#show running-config
!
vlan 99
private-vlan primary
private-vlan association add 100- 101
!
vlan 100
private-vlan community
!
vlan 101
private-vlan isolated
!
interface GigabitEthernet 0/1
switchport mode private-vlan promiscuous
switchport private-vlan mapping 99 add 100- 101
!
interface GigabitEthernet 0/2
switchport mode private-vlan host
switchport private-vlan host-association 99 100
!
interface GigabitEthernet 0/3
switchport mode private-vlan host
switchport private-vlan host-association 99 100
!
interface GigabitEthernet 0/4
switchport mode private-vlan host
switchport private-vlan host-association 99 101
!
interface GigabitEthernet 0/5
switchport mode trunk
!
SwitchA# show vlan private-vlan
VLAN Type Status Routed Ports Associated VLANs
------------------------------ ------------------
99 primary active Disabled Gi0/1, Gi0/5 100 - 101
100 community active Disabled Gi0/2, Gi0/3, Gi0/5 99
101 isolated active Disabled Gi0/4, Gi0/5 99
```

```
B SwitchB#show running-config
!
vlan 99
private-vlan primary
private-vlan association add 100- 101
!
vlan 100
private-vlan community
!
vlan 101
private-vlan isolated
!
interface GigabitEthernet 0/1
switchport mode trunk
!
interface GigabitEthernet 0/2
switchport mode private-vlan host
switchport private-vlan host-association 99 101
!
interface GigabitEthernet 0/3
switchport mode private-vlan host
switchport private-vlan host-association 99 100
。。。。。
```

##### 常见错误

+ PVLAN的主VLAN和辅助VLAN没有二层关联，配置隔离端口、混杂口、群体口时增加端口的VLAN列表失败。
+ 一个host口关联多个PVLAN对时失败。

##### 配置举例

######  PVLAN 单台设备三层应用

【配置方法】

+ 在设备上（本例为Switch A）配置PVLAN功能，具体配置要点可参考“PVLAN跨设备二层应用”章节的配置要点。
+ 将直连服务器的端口（本例为端口Gi 0/7）设置为Promiscuous Port，所有企业用户都可以通过Promiscuous Port和服务器通信。
+ 在三层设备（本例为Switch A）配置PVLAN的网关地址（本例配置VLAN 2的SVI为192.168.1.1/24），并配置Primary VLAN（本例为VLAN 2）和Secondary VLAN（本例为VLAN 10、 20 、 30 ）的三层接口映射关系，所有企业用户可以通过这个网关地址与外网通信

跨设备运行PVLAN，需要将跨界的设备连接端口配置为Trunk口。^

```
A 
SwitchA#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
SwitchA(config)#vlan 2
SwitchA(config-vlan)#private-vlan primary
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 10
SwitchA(config-vlan)#private-vlan community
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 20
SwitchA(config-vlan)#private-vlan community
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 30
SwitchA(config-vlan)#private-vlan isolated
SwitchA(config-vlan)#exit
SwitchA(config)#vlan 2
SwitchA(config-vlan)#private-vlan association 10,20,30
SwitchA(config-vlan)#exit
SwitchA(config)#interface range gigabitEthernet 0/1- 2
SwitchA(config-if-range)#switchport mode private-vlan host
SwitchA(config-if-range)#switchport private-vlan host-association 2 10
SwitchA(config-if-range)#exit
SwitchA(config)#interface range gigabitEthernet 0/3- 4
SwitchA(config-if-range)#switchport mode private-vlan host
SwitchA(config-if-range)#switchport private-vlan host-association 2 20
SwitchA(config-if-range)#exit
SwitchA(config)#interface range gigabitEthernet 0/5- 6
SwitchA(config-if-range)#switchport mode private-vlan host
SwitchA(config-if-range)#switchport private-vlan host-association 2 30
SwitchA(config-if-range)#exit
SwitchA(config)#interface gigabitEthernet 0/7
SwitchA(config-if-GigabitEthernet 0/7)#switchport mode private-vlan promiscuous
SwitchA(config-if-GigabitEthernet 0/7)#switchport private-vlan maping 2 10,20,30
SwitchA(config-if-GigabitEthernet 0/7)#exit
SwitchA(config)#interface vlan 2
SwitchA(config-if-VLAN 2)#ip address 192.168.1.1 255.255.255.0
SwitchA(config-if-VLAN 2)#private-vlan mapping 10,20,30
SwitchA(config-if-VLAN 2)#exit
```

【检验方法】 使各个子域内的用户IP来ping网关地址192.168.1.1能ping通。

```
A
SwitchA#show running-config
!
vlan 2
private-vlan primary
private-vlan association add 10,20,30
!
vlan 10
private-vlan community
!
vlan 20
private-vlan community
!
vlan 30
private-vlan isolated
!
interface GigabitEthernet 0/1
switchport mode private-vlan host
switchport private-vlan host-association 2 10
!
interface GigabitEthernet 0/2
switchport mode private-vlan host
switchport private-vlan host-association 2 10
!
interface GigabitEthernet 0/3
switchport mode private-vlan host
switchport private-vlan host-association 2 20
!
interface GigabitEthernet 0/4
switchport mode private-vlan host
switchport private-vlan host-association 2 20
!
interface GigabitEthernet 0/5
switchport mode private-vlan host
switchport private-vlan host-association 2 30
!
interface GigabitEthernet 0/6
switchport mode private-vlan host
switchport private-vlan host-association 2 30
!
interface GigabitEthernet 0/7
switchport mode private-vlan promiscuous
switchport private-vlan mapping 2 add 10,20,30
!
interface VLAN 2
no ip proxy-arp
ip address 192.168.1.1 255.255.255.0
private-vlan mapping add 10,20,30
!
SwitchA#show vlan private-vlan
VLAN Type Status Routed Ports Associated VLANs
------------------------------ ------------------
2 primary active Enabled Gi0/7 10,20,30
10 community active Enabled Gi0/1, Gi0/2 2
20 community active Enabled Gi0/3, Gi0/4 2
30 isolated active Enabled Gi0/5, Gi0/6 2
```

######  常见配置错误

+ PVLAN的主VLAN和辅助VLAN没有二层关联，在三层关联时配置失败。

+ 没进行三层关联就连接外网，结果无法与外网通信。

+ 连接服务器和外网的接口没有配置为混杂口，导致上下行报文转发不对称。

#### 8.6 监视与维护

##### 查看运行情况

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>查看 PVLAN 的配置。</td>         <td>show vlan private-vlan</td>     </tr> </table>

**查看调试信息**

输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>打开 PVLAN 调试开关。</td>         <td>debug bridge pvlan
</td>     </tr> </table>


## 9 Voice VLAN

### 9.1 概述

随着技术的日益发展，IP电话应用越来越广泛。Voice VLAN是为用户的语音数据流专门划分的 VLAN。

用户通过创建 Voice VLAN并将连接语音设备的端口加入 Voice VLAN，可以使语音数据集中在Voice VLAN中进行传输，并对语音流进行有针对性的 QoS（Quality of Service，服务质量）配置，提高语音流量的传输优先级，保证通话质量。

##### 协议规范

 无

### 9.2 典型应用

<table>     <tr>         <th>典型应用</th>         <th>场景描述</th>     </tr>     <tr>         <td>Voice VLAN 自动模式配置</td>         <td>IP电话与PC构成菊花链接入网络。部署的IP电话支持自动获取IP地址和Voice VLAN信息，发送Tagged的声音流。</td>     </tr>     <tr>         <td>Voice VLAN 手动模式配置</td>         <td>IP电话单独接入网络。</td>     </tr>     <tr>         <td>语音流和数据流隔离配置</td>         <td>PC连接到IP电话，IP电话连接到交换机，IP电话自动获取IP地址，发送Untagged声音流。</td>     </tr> </table>

#### 9.2.1 Voice VLAN 自动模式配置

##### 应用场景

PC和IP电话组成菊花链接入网络。该链路中同时有语音流和数据流。此时，语音流和数据流分别在Voice VLAN和数据VLAN中，保证其互不干扰。一般办公人员需使用PC进行数据业务通信，同时也需通过IP电话进行语音通信时采用该种链接。

Fa 0/1接入的是自动获取IP地址的IP电话，IP电话在Voice Vlan内获取IP地址以后，就可以正常使用了。组网要求Fa 0/1端口同时转发并且隔离语音流和数据流，端口可配置为Trunk口，Native Vlan转发数据流，Voice Vlan转发语音流。

支持Voice VLAN功能的设备可以根据进入端口的数据报文中的源MAC地址字段，判断该数据流是否为指定语音设备的语音数据流，源MAC地址符合系统设置的语音设备OUI（Organizationally Unique Identifier，全球统一标识符）地址的报文被认为是语音数据流，被划分到Voice VLAN中传输。

OUI地址为MAC地址的前24 位，是IEEE（Institute of Electrical and Electronics Engineers，电气和电子工程师学会）为不同设备供应商分配的一个全球唯一的标识符，从OUI地址可以判断出该设备是哪一个厂商的产品。

##### 功能部属

+ 将连接IP电话的端口配置为自动模式，发送tagged语音流到设备。

#### 9.2.2 Voice VLAN 手动模式配置

##### 应用场景

IP电话单独接入Voice VLAN中，该链路中只有一条语音流。这类链接一般用于会议室部署IP电话，或无需用到PC进行数据业的场合。

图 9 - 2 Voice VLAN手动模式配置组网图

部署的IP电话，自动获取IP地址，发送Untagged语音流，由于Fa0/1下连的是发出Untagged的语音流IP电话，而且只有语音流， 由于不带Tag的语音流不支持自动模式，所以端口只能配置为手动模式， 同时配置Fa0/1为Hybrid Port，依据匹配关系要求（见功能详解部分），Fa0/1的Native VLAN必须是Voice VLAN， 且Voice VLAN须在端口的允许通过的Untagged VLAN 列表中。

##### 功能部属

+ 将连接IP电话的端口配置为手动模式，发送untagged语音流到设备。

#### 9.2.3 语音流和数据流隔离配置

##### 应用场景

为保证通话质量，需要将语音数据在专用的Voice VLAN中传输，并且这个Voice VLAN中不能传输非语音数据。

图 9 - 3 Voice VLAN与数据流隔离组网图

组网要求Fa 0/1端口同时转发并且隔离语音流和数据流， 由于IP电话和PC都是Untagged， 所以端口需配置为Hybrid口，使用Native Vlan转发数据流，Voice Vlan转发语音流。由于Fa0/1下连的IP电话是发送Untagged语音流，故需要配置Voice VLAN模式为手动模式， 而PC也是发送Untagged数据流， 为了实现数据流和语音流隔离， 需要在Fa0/1口上开启MAC VLAN功能， Fa0/1的Native VLAN是数据VLAN，不能和Voice Vlan一样， 并且为了保证回来的数据流和语音流均为Untagged， 数据VLAN和Voice VLAN均须在端口的允许通过的Untagged VLAN 列表中。同时为了数据流可以转发，需关闭端口下的安全模式。

##### 功能部属

+ PC连接到IP电话， IP电话连接到交换机， IP电话自动获取IP地址， 发送Untagged语音流。设备关闭安全模式。

### 9.3 功能详解

##### 基本概念

######  Voice VLAN 的自动模式与手动模式

Voice VLAN中的端口可工作在Voice VLAN的自动模式或手动模式，在不同的工作模式下端口加入Voice VLAN的方式不同。

+ 自动模式：

当用户IP电话启动时，所发出的报文经支持Voice VLAN的设备时，设备通过识别该报文的源MAC地址，匹配设备上所配置的OUI 地址，OUI地址匹配成功后，设备自动将该语音报文的输入端口添加到Voice VLAN，并下发策略，将语音报文的优先级修改为设备上所配置的Voice VLAN中语音流的优先级，并使用老化机制对Voice VLAN内的端口进行维护。在老化时间内，系统没有从输入端口收到任何语音报文时，系统将把该端口从Voice VLAN 中删除。

+ 手动模式：

手动模式下，端口加入Voice VLAN或从Voice VLAN中删除的过程由管理员手动进行配置。用户IP电话通讯过程中，设备通过识别报文的源MAC地址，匹配设备上所配置的OUI 地址，OUI地址匹配成功后，下发策略，将语音报文的优先级修改为设备上所配置的Voice VLAN中语音流的优先级。

自动模式适用于PC--IP电话串联接入端口，可以同时传输语音数据和普通业务数据的组网方式。

手工模式适用于IP电话单独接入交换机，端口仅传输语音报文的组网方式， 这种组网的方式可以使该端口专用于传输语音数据，避免业务数据对语音数据传输的影响。

######  Voice VLAN 的端口与 IP 电话的配合工作

按照是否自动获取IP地址与Voice VLAN信息来划分，一般来说，IP电话有 2 种：

+ 自动获取IP地址及Voice VLAN编号的电话，这类电话可以发送Untagged或Tagged的语音流。

+ 手工设置IP地址及Voice VLAN编号的电话，这类电话只能发送Tagged语音流。

IP电话的工作原理

与其他网络设备一样，IP电话也需要IP地址才能在网络中正常通信。IP电话获取IP地址的方式有两种：

+ 通过DHCP自动获取。

+ 通过用户手工配置。

在自动获取IP地址时，IP 电话还可以向DHCP 服务器同时请求Voice VLAN信息，如果DHCP服务器返回了Voice VLAN 信息，IP电话就可以直接发送携带有Voice VLAN Tag 的语音流；如果DHCP服务器没有返回Voice VLAN信息，IP电话就只能发送不带VLAN Tag 的语音流。 如果IP电话支持手动设置IP地址和Voice VLAN编号，用户也可以在IP电话上手工设置IP地址，设置Voice VLAN信息，IP电话将根据用户的配置发出Tagged、Untagged 语音流。

+ Voice VLAN端口与发送Tagged语音流的IP电话

IP电话发送Tagged语音流时，IP电话必须已经通过自动获取或手工配置的方式得到了Voice VLAN信息，这种情况下，不同
类型的端口需要进行相应的配置，才能使语音报文能够在Voice VLAN中正常传输，同时不影响交换机对普通业务数据的转发
处理。 与自动获取Voice VLAN信息的IP电话不同，手工配置Voice VLAN的IP电话将始终发送、接收带有Voice VLAN Tag
的语音流。

+ Voice VLAN端口与发送Untagged语音流的IP电话

IP 电话在以下两种情况下会发送、接收Untagged语音流：

自动获取IP地址，但没有获取到Voice VLAN信息。

手工配置IP地址，但没有配置Voice VLAN信息。

IP电话发送Untagged 语音流的情况下，用户需要配置接收端口的缺省VLAN且允许缺省VLAN 通过，又必须将端口的缺省VLAN 配置为Voice VLAN，才能使语音流在Voice VLAN 中传输，此时端口的 Voice VLAN 工作模式只能为手工模式。

具体IP电话的支持情况、获取IP地址和Voice VLAN的过程，不同厂商的IP电话产品，其工作原理可能与上述的描述不同，具体情况请参见IP电话的用户手册。

Voice VLAN工作模式、IP电话类型、端口类型能够具体匹配关系如下表所示：

<table border="1">
  <tr>
    <th>Voice VLAN 工作模式</th>
    <th>语音流类型</th>
    <th>端口类型</th>
    <th>支持条件</th>
  </tr>
  <tr>
    <td rowspan="12">自动模式</td>
    <td rowspan="6">Tagged 语音流</td>
    <td>Access Port</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>Private VLAN 主机口</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>Private VLAN 混杂口</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>Trunk Port</td>
    <td>支持，接入端口的 native VLAN 必须存在且不能是 Voice VLAN，同时该端口允许 native VLAN 通过</td>
  </tr>
  <tr>
    <td>Hybrid Port</td>
    <td>支持，接入端口的 native VLAN 必须存在且不能是 Voice VLAN，同时该端口允许 native VLAN 通过</td>
  </tr>
  <tr>
    <td>Uplink 口</td>
    <td>支持，接入端口的 native VLAN 必须存在且不能是 Voice VLAN，同时接入端口应允许 native VLAN 的报文通过</td>
  </tr>
  <tr>
    <td rowspan="6">Untagged 语音流</td>
    <td>Access Port</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>Private VLAN 主机口</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>Private VLAN 混杂口</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>Trunk Port</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>Hybrid Port</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>Uplink 口</td>
    <td>不支持</td>
  </tr>
<tr>
    <td rowspan="12">手动模式</td>
    <td rowspan="6">Tagged 语音流</td>
    <td>Access Port</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>Private VLAN 主机口</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>Private VLAN 混杂口</td>
    <td>不支持</td>
  </tr>
  <tr>
    <td>Trunk Port</td>
    <td>支持，接入端口的 native VLAN 必须存在且不能是 Voice VLAN，同时接入端口允许 native VLAN 和 Voice VLAN 的报文通过</td>
  </tr>
  <tr>
    <td>Hybrid Port</td>
    <td>支持，接入端口的 native VLAN 必须存在且不能是 Voice VLAN，同时该端口允许 native VLAN 通过，且 Voice VLAN 应在该端口允许通过的 tagged VLAN 列表中</td>
  </tr>
  <tr>
    <td>Uplink 口</td>
    <td>支持，接入端口的 native VLAN 必须存在且不能是 Voice VLAN，同时接入端口允许 native VLAN 和 Voice VLAN 的报文通过</td>
  </tr>
  <tr>
      <td rowspan="6">Untagged 语音流 </td>
  <td>Access Port</td>
  <td>支持，Voice VLAN 须和接入端口所属 VLAN 一致
</td>
  </tr>
  <tr>
    <td>Private VLAN 主机口</td>
    <td>支持，Voice VLAN 必须配置成该端口所对应的 Isolated VLAN 或Community VLAN</td>
    </tr>
<tr>
    <td>Private VLAN 混杂口</td>
    <td>支持，Voice VLAN 必须配置成 Primary VLAN</td>
  </tr>
  <tr>
    <td>Trunk Port</td>
    <td>支持，接入端口的 native VLAN 必须是 Voice VLAN，且接入端口允许该 VLAN 通过</td>
  </tr>
  <tr>
    <td>Hybrid Port</td>
    <td>支持，接入端口的 native VLAN 必须是 Voice VLAN (如果端口使能 MAC VLAN 来进行数据流与语音流隔离，则 native VLAN 可以不是 Voice VLAN)，且在接入端口允许通过的 untagged VLAN 列表中</td>
  </tr>
  <tr>
    <td>Uplink 口</td>
    <td>不支持</td>
  </tr> 
</table>





如果用户的IP Phone 发出的是tagged 语音流，且接入的端口上使能了802.1x认证和Guest VLAN功能，为保证各种功能的正常使用，请为Voice VLAN、端口的缺省VLAN 和802.1x 的Guest VLAN 分配不同的VLAN ID。

由于Protocol VLAN只对Trunk Port/Hybrid Port输入的untagged报文生效，而Voice VLAN自动模式下的Trunk/Hybrid。Port只能对tagged语音流进行处理，因此请不要将某个VLAN同时设置为Protocol VLAN与Voice VLAN。

在使用自动模式时，请不要将OUI地址配置为静态地址，否则会影响自动模式的使用。

######  Voice VLAN 安全模式

为了能够更好地进行用户语音流与数据流分离传输，Voice VLAN提供安全模式功能。安全模式打开时，Voice VLAN只允许传输语音流，设备会对报文的源MAC地址进行检查，当报文源MAC地址是可识别的Voice VLAN OUI地址时，允许该报文在Voice VLAN内传输，否则将该报文丢弃。安全模式关闭时，不对报文的源MAC地址进行检查，所有报文均可在Voice VLAN内进行传输。

安全模式下，仅对untagged报文及带有Voice VLAN tag的报文进行源MAC地址检查，对于带有其它非Voice VLAN tag的报文，设备按照VLAN规则对报文进行转发和丢弃的处理，不受Voice VLAN 安全/普通模式的影响。

建议用户尽量不要在Voice VLAN 中同时传输语音和业务数据。若的确有此需要，请确认Voice VLAN 的安全模式已关闭。

##### 功能特性

<table>     <tr>         <th>功能特性</th>         <th>作用</th>     </tr>     <tr>         <td>Voice VLAN</td>         <td>将数据流和语音流分别限制在数据 VLAN 和 Voice VLAN 中，从而保证语音通话与业务报文互不影响</td>     </tr> </table>

#### 9.3.1 Voice VLAN

##### 工作原理

支持Voice VLAN功能的设备，通过将数据流和语音流分别限制在数据VLAN和Voice VLAN中，从而保证语音通话与业务报文互不影响。同时下发优先级策略提高语音流的优先级，保证通话质量。其基本工作方式如下所述：

第一步，由用户在设备上创建 1 个专用传输语音报文的VLAN，即Voice VLAN，并使能连接IP电话的端口的Voice VLAN功能。

第二步，连接IP电话的端口加入Voice VLAN，这是关键的一步。加入的方式视Voice VLAN的工作模式为自动模式或手动模式而有所不同，具体如下：

自动模式下，当设备从该端口收到一个untagged报文以后，会将其源MAC地址和合法OUI地址相匹配。如果该源MAC为OUI地址，即认为该报文为语音报文。设备将该端口自动加入到Voice VLAN 中，同时在该端口上学习这个MAC地址。

手动模式下，由用户手动配置连接IP电话的端口加入到Voice VLAN。

第三步，无论是自动模式还是手动模式，当端口加入Voice VLAN时，设备会下发策略，提高所有通过Voice VLAN的源MAC匹配该OUI的报文的优先级，将能够匹配该OUI地址的语音报文的优先级设置为cos=6，dscp= 46 。

经过上述步骤后，连接IP电话的端口加入到专用的Voice VLAN中，语音报文在Voice VLAN中集中传输，同时语音报文以高优先级从设备中转发出去。

如果IP电话支持LLDP协议，则用户无需配置OUI，设备可以通过捕捉IP电话发出的LLDP协议，对协议报文中的设备能力字段进行识别，对于标识其能力为“telephone”的设备识别为语音设备，将协议报文中的源MAC提取出来作为语音设备MAC进行处理，从而实现语音设备的自动识别。

##### 相关配置

######  使能 Voice VLAN 功能

缺省情况下，Voice VLAN功能关闭。

VLAN 1不可配置为Voice VLAN。

使用vlan vlan-id命令，创建一个VLAN。

使用voice vlan vlan-id命令, 使能Voice VLAN，设置一个VLAN为Voice VLAN。

######  使能端口 Voice VLAN 功能

缺省情况下端口的Voice VLAN功能关闭。

使用voice vlan enable 命令，使能端口的Voice VLAN功能。

######  配置端口的 Voice VLAN 工作模式

缺省情况下，端口的Voice VLAN工作模式为自动模式。

使用voice vlan mode auto命令，设置端口的Voice VLAN模式为自动模式。

使用no voice vlan mode auto命令，设置端口的Voice VLAN模式为手动模式。

各个端口Voice VLAN的工作模式相互独立，不同的端口可以设置为不同的模式。

######  配置 Voice VLAN 老化时间

缺省情况下，老化时间为 1440 分钟，老化时间仅对自动模式端口启作用。老化时间内端口没收到语音流报文，端口将自动从Voice VLAN中删除。老化时间设置的越长，端口在没收到语音流时驻留在Voice VLAN内的时间就越长。

使用voice vlan aging命令，设置端口老化时间。

######  配置 Voice VLAN OUI 地址

确实情况下，没有配置OUI地址。

使用voice vlan mac-address，配置设备可识别的Voice VLAN oui地址。

######  配置 Voice VLAN 的安全模式

缺省情况下，Voice VLAN的安全模式打开。

使用voice vlan security enable命令，打开Voice VLAN的安全模式。

安全模式打开时Voice VLAN内只允许传输语音流。

######  配置 Voice VLAN 的语音流优先级

缺省情况下，缺省情况下，CoS为 6 ，DSCP为 46 。语音流优先级设置的越高，报文传输的优先级越高，从而提高通话质量。

使用voice vlan security cos命令，设置Voice VLAN语音流的CoS值。

使用voice vlan security dscp命令，设置Voice VLAN语音流的DSCP值。

### 9.4 配置详解

<table>
  <thead>
    <tr>
      <th>配置项</th>
      <th colspan="2">配置建议 & 相关命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">使能 Voice VLAN 功能</td>
      <td colspan="2">必选配置。 用于开启全局 Voice VLAN 功能。</td>
    </tr>
    <tr>
      <td>voice vlan </td>
      <td>使能 Voice VLAN，设置一个 VLAN 为Voice VLAN。</td>
    </tr>
    <tr>
      <td rowspan="2">使能端口 Voice VLAN 功能</td>
      <td colspan="2">必选配置。 用于开启端口 Voice VLAN 功能。</td>
    </tr>
    <tr>
      <td>voice vlan enable </td>
      <td>使能端口的 Voice VLAN 功能。</td>
    </tr>
    <tr>
      <td rowspan="2">配置 Voice VLAN 老化时间</td>
      <td colspan="2">可选配置。 用于配置 Voice VLAN 老化时间。</td>
    </tr>
    <tr>
      <td>voice vlan aging </td>
      <td>配置 Voice VLAN 的老化时间，取值范围为 5-10000 分钟，缺省为 1440 分钟。</td>
    </tr>
    <tr>
      <td rowspan="2">配置 Voice VLAN OUI 地址</td>
      <td colspan="2">可选配置。 用于配置 Voice VLAN OUI 地址。</td>
    </tr>
    <tr>
      <td>voice vlan mac-address </td>
      <td>配置设备可识别的 Voice VLAN OUI地址。</td>
    </tr>   
    <tr>
      <td rowspan="2">配置 Voice VLAN 的安全模
式</td>
      <td colspan="2">可选配置。 用于配置 Voice VLAN 安全模式。</td>
    </tr>
    <tr>
      <td>voice vlan security enable </td>
      <td>打开 Voice VLAN 的安全模式。</td>
    </tr>    
    <tr>
      <td rowspan="2">配置 Voice VLAN 的语音流优先级</td>
      <td colspan="2">可选配置。 用于配置 Voice VLAN 的语音流优先级。</td>
    </tr>
    <tr>
      <td>voice vlan cos cos-value
voice vlan dscp dscp-value
 </td>
      <td>配置 Voice VLAN 的语音流优先级。</td>
    </tr> 
    <tr>
      <td rowspan="2">配置端口的 Voice VLAN 工作模式
</td>
      <td colspan="2">可选配置。 用于配置端口 Voice VLAN 工作模式。</td>
    </tr>
    <tr>
      <td>voice vlan mode autoe </td>
      <td>设置端口的Voice VLAN模式为自动模式。</td>
    </tr>       
  </tbody>
</table>


### 

#### 9.4.1 使能 Voice VLAN 功能

##### 配置效果

 配置一个VLAN为Voice VLAN用于传输语音数据流。

##### 注意事项

 配置Voice VLAN之前，须先创建对应的VLAN。

 VLAN 1是默认VLAN，无需创建，但VLAN 1不能被设置为 Voice VLAN。

 不允许将某个VLAN同时设置为Voice VLAN与Super VLAN。

 如果接入的端口上开启了802.1x VLAN自动跳转功能，为保证功能的正常使用，请不要将下发的VID设置为Voice VLAN
ID。

 不要将RSPAN的Remote VLAN与Voice VLAN配置成同 1 个VLAN，否则可能会影响远程端口镜像功能与Voice VLAN
功能。

**配置方法**

######  配置一个 Voice VLAN

+ 必须配置。
+ 创建一个vlan，并将其配置为Voice VLAN用于传输语音数据流。
+ 交换机设备上配置。

【命令格式】 voice vlan vlan-id
【参数说明】 vlan-id: VLAN vid，范围为 2 - 4094
【缺省配置】 Voice VLAN 功能关闭
【命令模式】 全局配置模式
【使用指导】 如果要关闭Voice VLAN功能，可用no voice vlan全局配置命令进行设置

当端口同时打开802.1x与Voice VLAN功能时，符合Voice VLAN OUI设置的IP电话无需认证即可使用Voice VLAN通信。譬如在同一个端口上接入PC和IP 电话, 打开802.1x认证功能后，PC使用网络需进行1x认证，而IP电话不受影响。

##### 检验方法

+ 使用命令show voice vlan查看配置显示是否生效。

【命令格式】 show voice vlan^
【参数说明】 -
【命令模式】 所有模式
【使用指导】 -
【命令展示】 

```
Ruijie#show voice vlan
Voice VLAN status : ENABLE
Voice VLAN ID : 10
Voice VLAN security mode: Security
Voice VLAN aging time : 1440 minutes
Voice VLAN cos : 6
Voice VLAN dscp : 46
Current voice VLAN enabled port mode:
PORT MODE
-------------------- ---------- 
```

##### 配置举例

######  配置 Voice VLAN

【配置方法】 

+ 创建VLAN 2

+ 全局使能Voice VLAN功能，并设置VLAN 2为Voice VLAN。

  ```
  Ruijie# configure terminal
  Enter configuration commands, one per line. End with CNTL/Z.
  Ruijie(config)# vlan 2
  Ruijie(config-vlan)# exit
  Ruijie(config)# voice vlan 2
  ```

  

【检验方法】 通过show voice vlan命令显示是否正确

```
Ruijie#show voice vlan
Voice VLAN status : ENABLE
Voice VLAN ID : 2
Voice VLAN security mode: Security
Voice VLAN aging time : 1440 minutes
Voice VLAN cos : 6
Voice VLAN dscp : 46
Current voice VLAN enabled port mode:
PORT MODE

-------------------- ----------
```



#### 9.4.2 使能端口 Voice VLAN 功能

##### 配置效果

使能连接IP电话的端口的Voice VLAN功能，这是端口能够传输语音流的必须步骤。

##### 注意事项

+ Voice VLAN仅支持二层物理口（Access Port/Trunk Port/Hybrid Port/Uplink Port/ Private VLAN端口等），不支持在AP口与Routed Port上打开Voice VLAN功能。

+ 端口使能了Voice VLAN功能后，为保证功能运行正常，请不要切换端口的二层模式（Access Port/Trunk Port/Hybrid Port等）。若需切换，请先关闭端口的Voice VLAN功能。

##### 配置方法

######  使能端口的 Voice VLAN 功能

+ 必须配置。
+  用户要想将端口用于IP电话通信，必须使能端口的Voice VLAN功能。
+ 交换机设备上配置。

【命令格式】 voice vlan enable
【参数说明】 -
【缺省配置】 端口Voice VLAN 功能关闭
【命令模式】 接口配置模式
【使用指导】 如果要关闭端口的Voice VLAN功能，可用no voice vlan enable命令进行设置

在全局Voice VLAN关闭的情况下，也允许使能端口的Voice^ VLAN功能，但不生效。

##### 检验方法

 使用命令show voice vlan查看配置显示是否生效。
【命令格式】 show voice vlan
【参数说明】 -^
【命令模式】 所有模式
【使用指导】 -
【命令展示】 

```
Ruijie#show voice vlan^
Voice VLAN status : ENABLE
Voice VLAN ID : 10
Voice VLAN security mode: Security
Voice VLAN aging time : 1440 minutes
Voice VLAN cos : 6
Voice VLAN dscp : 46
Current voice VLAN enabled port mode:
PORT MODE

-------------------- ----------

Gi0/1 MANUAL
```

##### 配置举例

######  配置端口开启 Voice VLAN 功能

【配置方法】  进入端口的配置模式，可使能Voice VLAN的端口为物理端口。

```
Ruijie# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)# interface gigabitEthernet 0/1
Ruijie(config-if)# voice vlan enable
```

【检验方法】 通过show voice vlan命令显示是否正确

```
Ruijie#show voice vlan
Voice VLAN status : ENABLE
Voice VLAN ID : 10
Voice VLAN security mode: Security
Voice VLAN aging time : 1440 minutes
Voice VLAN cos : 6
Voice VLAN dscp : 46
Current voice VLAN enabled port mode:
PORT MODE
-------------------- ----------
Gi0/1 MANUAL
```

#### 9.4.3 配置 Voice VLAN 老化时间

##### 配置效果

+ 用户可在设备上设置Voice VLAN 的老化时间，当在老化时间内，设备没有从输入端口收到任何语音报文时，将把该端口从Voice VLAN 中删除。老化时间仅对自动模式生效。

##### 配置方法

######  配置 Voice VLAN 老化时间

+ 可选配置。

+ 用户如果需要改变在没收到语音流的时候端口驻留在Voice VLAN中的时间，需要执行此配置。

+ 交换机设备上配置。

【命令格式】 voice vlan aging minutes
【参数说明】 minutes ：Voice VLAN的老化时间
【缺省配置】 缺省为 1440 分钟
【命令模式】 全局模式
【使用指导】 如果要将老化时间恢复到缺省值，可用no voice vlan aging全局配置命令进行设置。

##### 检验方法

+ 使用命令show voice vlan查看配置显示是否生效。

【命令格式】 show voice vlan
【参数说明】
【命令模式】 所有模式
【使用指导】 -^
【命令展示】 

```
Ruijie#show voice vlan
Voice VLAN status : ENABLE
Voice VLAN ID : 10
Voice VLAN security mode: Security
Voice VLAN aging time : 1440 minutes
Voice VLAN cos : 6
Voice VLAN dscp : 46
Current voice VLAN enabled port mode:
PORT MODE
-------------------- ----------
```

##### 配置举例

######  配置 Voice VLAN 老化时间

```
【配置方法】  设置Voice VLAN老化时间为 10 分钟。
Ruijie# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)# voice vlan aging 10
```

【检验方法】 通过show voice vlan命令显示是否正确

```
Ruijie#show voice vlan
Voice VLAN status : ENABLE
Voice VLAN ID : 10
Voice VLAN security mode: Security
Voice VLAN aging time : 10 minutes
Voice VLAN cos : 6
Voice VLAN dscp : 46
Current voice VLAN enabled port mode:
PORT MODE
-------------------- ----------
```



#### 9.4.4 配置 Voice VLAN OUI 地址

##### 配置效果

+ 锐捷产品提供Voice VLAN可识别的OUI地址设置，OUI地址的说明请参见Voice VLAN概述部分。支持Voice VLAN功能的设备通过识别输入报文的源MAC，是否匹配设备上所配置的Voice VLAN的OUI 地址，来判断该数据流是否为指定语音设备的语音数据流。

##### 注意事项

+ Voice VLAN OUI地址不能是组播地址，所配置的掩码需连续。

##### 配置方法

######  配置 Voice VLAN OUI

+ 可选配置。

+ IP电话连接设备后，用户需要配置其OUI地址从而使IP电话能够在网络中通信。

+ 交换机设备上配置。

【命令格式】 voice vlan mac-address mac-addr mask oui-mask [description text]
【参数说明】 mac-addr：语音报文的源mac地址
oui-mask：OUI地址的有效长度，用掩码表示
text：OUI地址描述符
【缺省配置】 缺省情况下没有配置任何OUI
【命令模式】 全局模式
【使用指导】 如果要删除设备上设置的某个OUI地址，可用no voice vlan mac-address oui全局配置命令进行设置。

##### 检验方法

+ 使用命令show voice vlan oui查看配置显示是否生效。

【命令格式】 show voice vlan oui
【参数说明】
【命令模式】 所有模式
【使用指导】 -^
【命令展示】 

```
Ruijie(config)# show voice vlan oui
Oui Address Mask Description
00 12.34 00 .0000 ffff.ff00. 0000 Company A
```

##### 配置举例

######  配置 Voice VLAN OUI

【配置方法】  

+ 设置 OUI 地址 0012.3400.0000 为 Voice VLAN 的合法地址，厂商为 Company A。

```
Ruijie# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)# voice vlan mac-address 00 12.34 00. 0000 mask ffff.ff00. 0000 description Company A
```

【检验方法】 show voice vlan oui显示是否正确

```
Ruijie(config)# show voice vlan oui
Oui Address Mask Description
00 12.34 00 .0000 ffff.ff00. 0000 Company A
```

#### 9.4.5 配置 Voice VLAN 的安全模式

##### 配置效果

+ 为了更好地进行用户语音流与数据流分离传输，锐捷产品的Voice VLAN提供安全模式功能，安全模式打开时Voice VLAN内只允许传输语音流，更好地保证语音流传输质量

##### 注意事项

 无。

##### 配置方法

######  配置 Voice VLAN 的安全模式

+ 可选配置。

+ 配置Voice VLAN的安全模式用来隔离语音流与数据流，用户如果需要让Voice VLAN只传输语音流，需要执行此配置。

+ 交换机设备上配置。

【命令格式】 voice vlan security enable
【参数说明】 -
【缺省配置】 缺省情况下，Voice VLAN的安全模式打开。
【命令模式】 全局模式
【使用指导】 如果要关闭Voice VLAN的安全模式，可用no voice vlan security enable全局配置命令进行设置。

##### 检验方法

+ 使用命令show voice vlan 查看配置显示是否生效。

【命令格式】 show voice vlan

【参数说明】 -
【命令模式】 所有模式
【使用指导】 -
【命令展示】 

```
Ruijie#show voice vlan
Voice VLAN status : ENABLE
Voice VLAN ID : 10
Voice VLAN security mode: Security
Voice VLAN aging time : 1440 minutes
Voice VLAN cos : 6
Voice VLAN dscp : 46
Current voice VLAN enabled port mode:
PORT MODE

-------------------- ----------
```

##### 配置举例

######  配置 Voice VLAN 安全模式

【配置方法】 

+ 进入全局配置模式，打开Voice VLAN的安全模式。

```
Ruijie# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)# voice vlan security enable
```



【检验方法】 show voice vlan显示是否正确

```
Ruijie#show voice vlan
Voice VLAN status : ENABLE
Voice VLAN ID : 10
Voice VLAN security mode: Security
Voice VLAN aging time : 1440 minutes
Voice VLAN cos : 6
Voice VLAN dscp : 46
Current voice VLAN enabled port mode:
PORT MODE
-------------------- ----------
```

#### 9.4.6 配置 Voice VLAN 的语音流优先级

##### 配置效果

+ 设备通过修改Voice VLAN的语音流的CoS与DSCP值来提高语音流的优先级，保证通话质量。关于CoS与DSCP的概念，请参见QoS配置章节的说明。

##### 注意事项

+ 无。

**配置方法**

######  配置 Voice VLAN 的语音流优先级

+ 可选配置。

+ 用户如果需要提高语音流报文的传输优先级，需要执行此配置。

+ 交换机设备上配置。

【命令格式】 voice^ vlan^ cos^ cos-value^
voice vlan dscp dscp-value
【参数说明】 cos-value : Voice VLAN语音流的CoS值，范围<0，7>。
cos-value : Voice VLAN语音流的DSCP值，范围<0， 63 >。
【缺省配置】 缺省情况下，Cos为 6 ，DSCP为 46 。
【命令模式】 全局模式
【使用指导】 如果要将CoS与DSCP值恢复为缺省值，可使用no voice vlan cos或no voice vlan dscp全局配置命令进行设置。

##### 检验方法

+ 使用命令show voice vlan 查看配置显示是否生效。

【命令格式】 show voice vlan
【参数说明】 -^
【命令模式】 所有模式
【使用指导】 -
【命令展示】 

```
Ruijie#show voice vlan^
Voice VLAN status : ENABLE
Voice VLAN ID : 10
Voice VLAN security mode: Security
Voice VLAN aging time : 1440 minutes
Voice VLAN cos : 6
Voice VLAN dscp : 46
Current voice VLAN enabled port mode:
PORT MODE
-------------------- ---------- 
```

##### 配置举例

######  配置 Voice VLAN 语音流优先级

【配置方法】  配置Voice VLAN的语音流优先级，CoS为 5 ，DSCP为 40 。。

```
Ruijie# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)# voice vlan cos 5
Ruijie(config)# voice vlan dscp 40
```

【检验方法】 show voice vlan显示是否正确

```
Ruijie#show voice vlan
Voice VLAN status : ENABLE
Voice VLAN ID : 10
Voice VLAN security mode: Security
Voice VLAN aging time : 1440 minutes
Voice VLAN cos : 5
Voice VLAN dscp : 40
Current voice VLAN enabled port mode:
PORT MODE
-------------------- ----------
```

#### 9.4.7 配置端口的 Voice VLAN 工作模式

##### 配置效果

+ Voice VLAN的工作模式分为自动模式与手动模式，基于端口配置，关于自动模式与手动模式的概念请参见Voice VLAN的自动模式与手动模式部分说明。

##### 注意事项

+ 当端口使能了Voice VLAN 并工作在手工模式时，必须手工将端口加入Voice VLAN，才能保证Voice VLAN 功能生效。

+ 当端口工作于自动模式时，为保证功能运行正常，请注意不要将端口的native VLAN设置为Voice VLAN。

+ 锐捷产品Trunk Port/Hybrid Port缺省可以传输所有VLAN的报文，请先将Voice VLAN从端口的VLAN许可列表中移出，再打开Voice VLAN功能，以保证未连接语音设备的端口不会加入Voice VLAN，或长时间不使用的端口一直驻留在Voice VLAN中。

##### 配置方法

######  配置端口的 Voice VLAN 工作模式为自动模式

+ 可选配置。

+ 用户如果需要让端口在收到语音流时自动加入Voice VLAN，达到老化时间时自动退出Voice VLAN，需要执行此配置，将端口模式切换为自动模式。

+ 交换机设备上配置。

【命令格式】 voice^ vlan^ mode auto^
【参数说明】 -
【缺省配置】 端口Voice VLAN 工作模式为自动模式
【命令模式】 接口配置模式
【使用指导】 如果要设置端口的工作模式为手动模式，则使用no voice vlan mode auto命令进行设置。

端口使能了Voice VLAN功能后，不允许进行手动模式和自动模式的切换，若需进行模式切换，请先关闭端口的Voice VLAN功能。

自动模式下，不允许通过手工配置命令将端口加入Voice VLAN 或从Voice VLAN中删除。

**检验方法**

 使用命令show voice vlan查看配置显示是否生效。

【命令格式】 show voice vlan^
【参数说明】 -
【命令模式】 所有模式
【使用指导】 -
【命令展示】 

```
Ruijie#show voice vlan
Voice VLAN status : ENABLE
Voice VLAN ID : 10
Voice VLAN security mode: Security
Voice VLAN aging time : 1440 minutes
Voice VLAN cos : 6
Voice VLAN dscp : 46
Current voice VLAN enabled port mode:
PORT MODE
Gi0/1 AUTO
```



##### 配置举例

######  配置端口加入 Voice VLAN ，工作于自动模式

【配置方法】 配置要点

+ Fa 0/1接入的是自动获取IP地址的IP电话，IP电话在Voice Vlan内获取IP地址以后，就可以正常使用了。组网要求Fa 0/1端口同时转发并且隔离语音流和数据流，端口可配置为Trunk口，Native Vlan
  转发数据流，Voice Vlan转发语音流。
+ PC发出的是Untagged的报文，因此会在端口的Native VLAN内传输，我们将Native Vlan设置为 5 ， 用来传输PC发出的数据流。
+ 组网要求隔离语音流和数据流，当配置端口为Trunk Port， Voice VLAN模式为自动模式时， 依据匹配关系要求，Fa0/1的native VLAN必须存在且不能是Voice VLAN，同时该端口允许Native VLAN通过，Native VLAN为 5 ，非 Voice VLAN（VLAN2），可满足上述要求。同时由于Trunk Port缺省包含所有VLAN，为更好地使用自动模式，使不连接语音设备的端口不加入Voice VLAN，需要先将Voice VLAN(VLAN 2)从Fa0/1的VLAN许可列表中移出。

第一步，创建VLAN2为Voice VLAN。

```
Ruijie# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)# vlan 2
Ruijie(config-vlan)# exit
Ruijie(config)# voice vlan 2
```

第二步，设置设备允许OUI地址为 0012. 3400. 0000 ，掩码是ffff.ff00. 0000 的语音报文通过Voice VLAN转发。

```
Ruijie(config)# voice vlan mac-address 00 12.34 00. 0000 mask ffff.ff00. 0000
```

第三步，设置Fa0/1为Trunk Port，端口的native VLAN为VLAN 5 。

```
Ruijie(config)# interface fastEthernet 0/1
Ruijie(config-if)# switchport mode trunk
Ruijie(config-if)# switchport trunk native vlan 5
```

第四步，将Voice VLAN从加入Fa0/1的VLAN列表中移出，并使能Voice VLAN功能。

```
Ruijie(config-if)# switchport trunk allowed vlan remove 2
Ruijie(config-if)# voice vlan enable
```

【检验方法】 使用命令show voice vlan查看设备当前的Voice VLAN状态

```
Ruijie(config)# show voice vlan
Voice Vlan status: ENABLE
Voice Vlan ID : 2
Voice Vlan security mode: Security
Voice Vlan aging time: 1440 minutes
Voice Vlan cos : 6
Voice Vlan dscp : 46
Current voice vlan enabled port mode:
PORT MODE
-------------------- ----------
Fa0/1 AUTO
# 查看设备的Voice VLAN OUI地址
Ruijie(config)# show voice vlan oui
Oui Address Mask Description
0012. 34 00.0000 ffff.ff00.0000
```

### 9.5 监视与维护

##### 查看运行情况

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>查看 Voice VLAN 配置</td>         <td>show voice vlan</td>     </tr>     <tr>         <td>查看 Voice VLAN 的 OUI 配置</td>         <td>show voice vlan oui</td>     </tr> </table>

##### 查看调试信息

输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>打开 Voice VLAN 的调试开关。</td>         <td>debug bridge vvlan</td>     </tr> </table>

### 10 MSTP

#### 10.1 概述

生成树协议是一种二层管理协议，它通过选择性地阻塞网络中的冗余链路来消除二层环路，同时还具备链路备份的功能。

与众多协议的发展过程一样，生成树协议也是随着网络的发展而不断更新的，从最初的STP（Spanning Tree Protocol，生成树协议）到RSTP（Rapid Spanning Tree Protocol，快速生成树协议），再到最新的MSTP（Multiple SpanningTree Protocol，多生成树协议）。

对二层以太网来说，两个LAN间只能有一条活动着的通路，否则就会产生广播风暴。但是为了加强一个局域网的可靠性，建立冗余链路又是必要的，其中的一些通路必须处于备份状态，如果当网络发生故障，另一条链路失效时，冗余链路就必须被提升为活动状态。手工控制这样的过程显然是一项非常艰苦的工作，STP协议就自动地完成这项工作。它能使一个局域网中的设备起以下作用：

+ 发现并启动局域网的一个最佳树型拓朴结构。

+ 发现故障并随之进行恢复，自动更新网络拓朴结构，使在任何时候都选择了可能的最佳树型结构。

局域网的拓朴结构是根据管理员设置的一组网桥配置参数自动进行计算的。使用这些参数能够生成最好的一棵拓朴树。只有配置得当，才能得到最佳的方案。

RSTP协议完全向下兼容802.1D STP协议，除了和传统的STP协议一样具有避免回路、提供冗余链路的功能外，最主要的特点就是“快”。如果一个局域网内的网桥都支持RSTP协议且管理员配置得当，一旦网络拓朴改变而要重新生成拓朴树只需要不超过 1 秒的时间（传统的STP需要大约 50 秒）。

STP和RSTP存在的不足：

+ STP 不能快速迁移，即使是在点对点链路或边缘端口，也必须等待两倍的Forward Delay的时间延迟，端口才能迁移到转发状态。

+ RSTP可以快速收敛，但和STP一样还存在如下缺陷：由于局域网内所有VLAN都共享一棵生成树，因此所有VLAN 的报文都沿这棵生成树进行转发，不能按VLAN 阻塞冗余链路，也无法在VLAN 间实现数据流量的负载均衡。

MSTP(Multiple Spanning Tree Protocol，多生成树协议)，由IEEE制定的802.1s 标准定义，它可以弥补STP、RSTP的缺陷，既可以快速收敛，也能使不同VLAN 的流量沿各自的路径转发，从而为冗余链路提供了更好的负载分担机制。简单地说，STP/RSTP是基于端口的，MSTP是基于实例的。所谓实例就是多个VLAN的一个集合，通过多个VLAN捆绑到一个实例的方法可以节省通信开销和资源占用率。

本设备既支持STP协议，也支持RSTP协议与MSTP协议，遵循IEEE 802.1D、IEEE 802.1w及IEEE 802.1s标准。

下文仅介绍MSTP的相关内容。

##### 协议规范

######  IEEE 802.1D：Media Access Control (MAC) Bridges

+ IEEE 802.1w：Part 3: Media Access Control (MAC) Bridges—Amendment 2: Rapid Reconfiguration

+ IEEE 802.1s：Virtual Bridged Local Area Networks—Amendment 3: Multiple Spanning Trees

#### 10.2 典型应用

<table>     <tr>         <th>典型应用</th>         <th>场景描述</th>     </tr>     <tr>         <td>MSTP+VRRP 双核心拓扑</td>         <td>通过设计层次化的网络架构模型，使用MSTP+VRRP协议实现冗余备份和负载均衡，提高网络系统可用性。</td>     </tr>     <tr>         <td>BPDU TUNNEL 应用</td>         <td>介绍在 QINQ 网络环境中,使用 BPDU TUNNEL 功能,实现 STP 协议报文的隧道透传。</td>     </tr> </table>

#### 10.2.1 MSTP+VRRP 双核心拓扑

##### 应用场景

MSTP协议典型的应用场景是MSTP+VRRP的双核心应用方案。该方案是提高网络系统可用性的一个比较优秀的解决方案，通常采用层次化的网络架构模型，分为三层（核心层、汇聚层和接入层）或二层（核心层和接入层）架构，共同组成交换网络系统，提供数据交换服务。

这种架构的主要优点在于层次化的结构。在层次化网络架构中，每一层次网络设备的各种容量指标、特点和功能，都针对其所
在的网络位置和作用进行了优化，稳定性和可用性都得到了加强。

功能部属

##### 配置指南 MSTP

+ 核心层：MSTP配置多实例达到负载均衡的效果。比如创建两个实例 1 ， 2 。实例 1 映射VLAN 10，实例 2 映射VLAN 20。
  设备A为实例 0 ， 1 的根桥（实例 0 即CIST是默认存在的），设备B为实例 2 根桥。

+ 核心层：设备A为VLAN 10的VRRP的主设备，设备B为VLAN 20的VRRP的主设备。

+ 接入层：将直连终端（PC或服务器）的端口配置成Portfast端口。同时配置BPDU Guard功能，防止用户私自接入非法的设备。

#### 10.2.2 BPDU TUNNEL 应用

##### 应用场景

在QINQ网络中，通常分为用户网络和运营商网络。为了实现用户网络之间STP协议报文的传输而又不对运营商网络产生影响，可以使用BPDU TUNNEL功能，以达到用户网络和运营商网络的STP协议分开计算，互不干扰。

【注释】 如上图所示，上部为运营商网络，下部为用户网络。其中，运营商网络包括边缘设备Provider S1和Provider S2。Customer Network A1和Customer Network A2为同一用户在不同地域的两个站点，Customer S1和Customer S2为用户网络到运营商网络的接入设备，分别通过Provider S1和Provider S2接入运营商网络。应用BPDU TUNNEL功能，可以满足处于不同地域的Customer Network A1和Customer Network A2可以跨越运营商网络进行统一生成树计算，而不影响运营商网络的生成树计算。

**功能部属**

 在运营商边缘设备（本例为Provider S1/Provider S2上开启基本QinQ功能，实现用户网络的数据报文在运营商网络的
指定VLAN内传输。


配置指南 MSTP

 在运营商边缘设备（本例为Provider S1/Provider S2上开启STP协议透传功能，使运营商网络可以通过BPDU TUNNEL
对用户网络的STP报文进行隧道传输。

### 10.3 功能详解

##### 基本概念

######  BPDU （ Bridge Protocol Data Units ）

要生成一个稳定的树型拓朴网络需要依靠以下元素：

+ 每个网桥拥有的唯一的桥ID（Bridge ID），由桥优先级和Mac地址组合而成。

+ 网桥到根桥的路径花费（Root Path Cost），以下简称根路径花费。

+ 每个端口ID（Port ID），由端口优先级和端口号组合而成。

网桥之间通过交换BPDU（Bridge Protocol Data Units，网桥协议数据单元）帧来获得建立最佳树形拓朴结构所需要的信息。这些帧以组播地址 01 - 80 - C2- 00 - 00 - 00 （十六进制）为目的地址。

每个BPDU由以下这些要素组成：

+ Root Bridge ID（本网桥所认为的根桥ID）。

+ Root Path Cost（本网桥的根路径花费）。

+ Bridge ID（本网桥的桥ID）。

+ Message Age（报文已存活的时间）

+ Port ID（发送该报文端口的ID）。

Forward-Delay Time、Hello Time、Max-Age Time 三个协议规定的时间参数。

其他一些诸如表示发现网络拓朴变化、本端口状态的标志位。

当网桥的一个端口收到高优先级的BPDU（更小的Bridge ID，更小的Root Path Cost等），就在该端口保存这些信息，同时向所有端口更新并传播这些信息。如果收到比自己低优先级的BPDU，网桥就丢弃该信息。

这样的机制就使高优先级的信息在整个网络中传播开，BPDU的交流就有了下面的结果：

+ 网络中选择了一个网桥为根桥（Root Bridge）。

+ 除根桥外的每个网桥都有一个根口（Root Port），即提供最短路径到Root Bridge的端口。

+ 每个网桥都计算出了到根桥（Root Bridge）的最短路径。

+ 每个LAN都有了指派网桥（Designated Bridge），位于该LAN与根桥之间的最短路径中。指派网桥和LAN相连的端口称为指派端口（Designated Port）。

+ 根口（Root port）和指派端口（Designated Port）进入Forwarding状态。

######  Bridge ID

按IEEE 802.1W标准规定，每个网桥都要有单一的网桥标识（Bridge ID），生成树算法中就是以它为标准来选出根桥（Root Bridge）的。Bridge ID由 8 个字节组成，后 6 个字节为该网桥的mac地址，前 2 个字节如下表所示，前4 bit表示优先级（Priority），后8 bit表示System ID，为以后扩展协议而用，在RSTP中该值为 0 ，因此给网桥配置优先级就要是 4096 的倍数。

<table border="1">
  <tr>
    <th></th>
    <th>bit位</th>
    <th>值</th>
  </tr>
  <tr>
    <td rowspan="4">Priority value</td>
    <td>16</td>
    <td>32768</td>
  </tr>
  <tr>
    <td>15</td>
    <td>16384</td>
  </tr>
  <tr>
    <td>14</td>
    <td>8192</td>
  </tr>
  <tr>
    <td>13</td>
    <td>4096</td>
  </tr>
  <tr>
    <td rowspan="12">System ID</td>
    <td>12</td>
    <td>2048</td>
  </tr>
  <tr>
    <td>11</td>
    <td>1024</td>
  </tr>
  <tr>
    <td>10</td>
    <td>512</td>
  </tr>
  <tr>
    <td>9</td>
    <td>256</td>
  </tr>
  <tr>
    <td>8</td>
    <td>128</td>
  </tr>
  <tr>
    <td>7</td>
    <td>64</td>
  </tr>
  <tr>
    <td>6</td>
    <td>32</td>
  </tr>
  <tr>
    <td>5</td>
    <td>16</td>
  </tr>
  <tr>
    <td>4</td>
    <td>8</td>
  </tr>
  <tr>
    <td>3</td>
    <td>4</td>
  </tr>
  <tr>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
  </tr>
</table>





######  Spanning-Tree Timers （生成树的定时器）

以下描述影响到整个生成树性能的三个定时器。

+ Hello timer：定时发送BPDU报文的时间间隔。

+ Forward-Delay timer：端口状态改变的时间间隔。当RSTP协议以兼容STP协议模式运行时，端口从Listening转变向Learning，或者从Learning转向Forwarding状态的时间间隔。

+ Max-Age timer：BPDU报文消息生存的最长时间。当超出这个时间，报文消息将被丢弃。

######  Port Roles and Port States

每个端口都在网络中有扮演一个角色（Port Role），用来体现在网络拓朴中的不同作用。

+ Root port：提供最短路径到根桥（Root Bridge）的端口。

+ Designated port：每个LAN的通过该口连接到根桥。

+ Alternate port：根口的替换口，一旦根口失效，该口就立该变为根口。

+ Backup port：Designated Port的备份口，当一个网桥有两个端口都连在一个LAN上，那么高优先级的端口为Designated Port，低优先级的端口为Backup Port。

+ Disable port：当前不处于活动状态的口，即Operation State为Down的端口都被分配了这个角色。

以下为各个端口角色的示意图 1 、 2 、 3 ：

R = Root Port D = Designated Port A = Alternate Port B = Backup Port

在没有特别说明情况下，端口优先级从左到右递减。

每个端口有三个状态（Port State）来表示是否转发数据包，从而控制着整个生成树拓朴结构。

+ Discarding：既不对收到的帧进行转发，也不进行源Mac地址学习。

+ Learning：不对收到的帧进行转发，但进行源Mac地址学习，这是个过渡状态。

+ Forwarding：既对收到的帧进行转发，也进行源Mac地址的学习。

对一个已经稳定的网络拓朴，只有Root Port和Designated Port才会进入Forwarding状态，其它端口都只能处于Discarding
状态。

######  Hop Count

IST和MSTI已经不用Message Age和Max Age来计算BPDU信息是否超时，而是用类似于IP报文TTL的机制来计算，它就是Hop Count。

可以用spanning-tree max-hops全局配置命令来设置。在Region内，从Region Root Bridge开始，每经过一个设备，Hop Count就会减 1 ，直到为 0 则表示该BPDU信息超时，设备收到Hops值为 0 的BPDU就要丢弃它。

为了和Region外的STP、RSTP兼容，MSTP依然保留了Message Age和Max Age的机制。

##### 功能特性

<table>
    <tr>
        <th>功能特性</th>
        <th>作用</th>
    </tr>
    <tr>
        <td>STP 协议</td>
        <td>STP（Spanning Tree Protocol，生成树协议），由 IEEE 制定的 802.1D 标准定义，用于在局域网中消除数据链路层物理环路的协议。</td>
    </tr>
    <tr>
        <td>RSTP 协议</td>
        <td>RSTP（Rapid Spanning Tree Protocol，快速生成树协议），由IEEE制定的802.1w标准定义，它在STP基础上进行了改进，实现了网络拓扑的快速收敛。</td>
    </tr>
    <tr>
        <td>MSTP 协议</td>
        <td>MSTP（Multiple SpanningTree Protocol，多生成树协议），由IEEE 制定的802.1s 标准定义，它可以弥补STP、RSTP 和 PVST 的缺陷，既可以快速收敛，也能使不同VLAN 的流量沿各自的路径转发，从而为冗余链路提供了更好的负载分担机制。</td>
    </tr>
    <tr>
        <td>MSTP 的可选特性</td>
        <td>包括以下功能：Port Fast 特性、BPDU Guard、BPDU Filter、Tc-protection、TC Guard、TC 过滤、BPDU源 MAC检查、BPDU非法长度过滤、边缘口的自动识别、ROOT Guard 功能及 LOOP Guard 功能。</td>
    </tr>
</table>

#### 10.3.1 STP

STP协议是用来避免链路环路产生的广播风暴、并提供链路冗余备份的协议。

##### 工作原理

对二层以太网来说，两个LAN间只能有一条活动着的通路，否则就会产生广播风暴。但是为了加强一个局域网的可靠性，建立冗余链路又是必要的，其中的一些通路必须处于备份状态，如果当网络发生故障，另一条链路失效时，冗余链路就必须被提升为活动状态。手工控制这样的过程显然是一项非常艰苦的工作，STP协议就自动地完成这项工作。它能使一个局域网中的设备起以下作用：

+ 发现并启动局域网的一个最佳树型拓朴结构。

+ 发现故障并随之进行恢复，自动更新网络拓朴结构，使在任何时候都选择了可能的最佳树型结构。

局域网的拓朴结构是根据管理员设置的一组网桥配置参数自动进行计算的。使用这些参数能够生成最好的一棵拓朴树。只有配置得当，才能得到最佳的方案。

#### 10.3.2 RSTP

RSTP协议完全向下兼容802.1D STP协议，除了和传统的STP协议一样具有避免回路、提供冗余链路的功能外，最主要的特点就是“快”。如果一个局域网内的网桥都支持RSTP协议且管理员配置得当，一旦网络拓朴改变而要重新生成拓朴树只需要不超过 1 秒的时间（传统的STP需要大约 50 秒）。

##### 工作原理

######  RSTP 的快速收敛

现在开始介绍RSTP所特有的功能，即能让端口“快速”的Forwarding。

STP协议是选好端口角色（Port Role）后等待 30 秒(为 2 倍的Forward-Delay Time，Forward-Delay Time可配置，默认为 15秒)再Forwarding的，而且每当拓朴发生变化后，每个网桥重新选出的Root Port和Designated Port都要经过 30 秒再Forwarding，因此要等整个网络拓朴稳定为一个树型结构就大约需要 50 秒。

而RSTP端口的Forwarding过程就大不一样了，如下图所示，Switch A发送RSTP特有“Proposal”报文，Switch B发现SwitchA的优先级比自身高，就选Switch A为根桥，收到报文的端口为Root Port，立即Forwarding，然后从Root Port向Switch A发送“Agree”报文。Switch A的Designated Port得到“同意”，也就Forwarding了。然后Switch B的Designated Port又发送“Proposal”报文依次将生成树展开。因此在理论上，RSTP是能够在网络拓朴发生变化的一瞬间恢复网络树型结构，达到快速收敛。

以上的“握手”过程是有条件的，就是端口间必须是“Point-to-point Connect（点对点连接）”。为了让设备发挥最大的功效，最好不要使设备间为非点对点连接。

以下列出了“非点对点连接”的范例图。

######  RSTP 与 STP 的兼容

RSTP协议可以与STP协议完全兼容，RSTP协议会根据收到的BPDU版本号来自动判断与之相连的网桥是支持STP协议还是支持RSTP协议，如果是与STP网桥互连就只能按STP的Forwarding方法，过 30 秒再Forwarding，无法发挥RSTP的最大功效。

另外，RSTP和STP混用还会遇到这样一个问题。如下图所示，Switch A是支持RSTP协议的，Switch B只支持STP协议，它们俩互连，Switch A发现与它相连的是STP桥，就发STP 的BPDU来兼容它。但后来如果换了台Switch C，它支持RSTP协议，但Switch A却依然在发STP的BPDU，这样使Switch C也认为与之互连的是STP桥了，结果两台支持RSTP的设备却以STP协议来运行，大大降低了效率。

为此RSTP协议提供了Protocol-migration功能来强制发RSTP BPDU (这种情况下，对端网桥必须支持RSTP)，这样Switch A强制发了RSTP BPDU，Switch C就发现与之互连的网桥是支持RSTP的，于是两台设备就都以RSTP协议运行了，

#### 10.3.3 MSTP 协议

MSTP(Multiple Spanning Tree Protocol)，多生成树协议，它可以弥补STP、RSTP的缺陷，既可以快速收敛，也能使不同VLAN的流量沿各自的路径转发，从而为冗余链路提供了更好的负载分担机制。

##### 工作原理

本设备支持MSTP，MSTP是在传统的STP、RSTP的基础上发展而来的新的生成树协议，本身就包含了RSTP的快速FORWARDING机制。

由于传统的生成树协议与Vlan没有任何联系，因此在特定网络拓朴下就会产生以下问题：

如下图所示，设备A、B在Vlan1内，设备C、D在Vlan2内，然后连成环路。

若从设备A依次通过设备C、D到达B的链路花费比从设备A直接到B的链路花费更少的情况下，会造成把设备A和B间的链路给DISCARDING（如图 15 所示）。由于设备C、D不包含Vlan1，无法转发Vlan1的数据包，这样设备A的Vlan1就无法与设备B的Vlan1进行通讯。

为了解决这个问题，MSTP就产生了，它可以把一台设备的一个或多个Vlan划分为一个Instance，有着相同Instance配置的设备就组成一个域（MST Region），运行独立的生成树（这个内部的生成树称为IST，Internal Spanning-tree）；这个MST region组合就相当于一个大的设备整体，与其他MST Region再进行生成树算法运算，得出一个整体的生成树，称为CST（Common Spanning Tree）。

按这种算法，以上网络就可以在MSTP算法下形成图 16 的拓朴：设备A和B都在MSTP Region 1内，MSTP Region 1没能环路产生，所以没有链路DISCARDING，同理MSTP Region 2的情况也是一样的。然后Region 1和Region 2就分别相当于两个大的设备，这两台“设备”间有环路，因此根据相关配置选择一条链路DISCARDING。

这样，既避免了环路的产生，也能让相同Vlan间的通讯不受影响。

######  划分 MSTP Region

根据以上描述，很明显，要让MSTP产生应有的作用，首先就要合理地划分MSTP Region，相同MSTP Region内的设备“MST配置信息”一定要相同。

MST配置信息包括：

+ MST配置名称（Name）：最长可用 32 个字节长的字符串来标识MSTP Region。

+ MST Revision Number：用一个16bit长的修正值来标识MSTP Region。

+ MST Instance—vlan的对应表：每台设备都最多可以创建 64 个Instance（id从 1 到 64 ），Instance 0是强制存在的，所以系统最多可以支持 65 个Instance。用户还可以按需要分配 1 - 4094 个Vlan属于不同的Instance（ 0 － 64 ），未分配的Vlan缺省就属于Instance 0。这样，每个MSTI（MST Instance）就是一个“Vlan组”，根据BPDU里的MSTI信息进行MSTI内部的生成树算法，不受CIST和其他MSTI的影响。

可在用spanning-tree mst configuration全局配置命令进入“MST配置模式”配置以上信息。

MSTP BPDU里附带以上信息，如果一台设备收到的BPDU里的MST配置信息和自身的一样，就会认为该端口上连着的设备和自已是属于同一个MST Region，否则就认为是从另外一个Region来的。

建议在关闭MSTP模式后配置Instance—vlan的对应表，配置好后再打开MSTP，以保证网络拓朴的稳定和收敛。^

######  IST （ MSTP region 内的生成树）

划分好MSTP Region后，每个Region里就按各个Instance所设置的Bridge Priority、Port Priority等参数选出各个Instance独立的Root Bridge，以及每台设备上各个端口的Port Role，然后就Port Role指定该端口在该Instance内是FORWARDING还是DISCARDING的。

这样，经过MSTP BPDU的交流，IST(Internal Spanning Tree) 就生成了，而各个Instance也独立的有了自己的生成树（MSTI），其中Instance 0所对应的生成树与CST共同称为CIST（Common Instance Spanning Tree）。也就是说，每个Instance都为各自的“vlan组”提供了一条单一的、不含环路的网络拓朴。

如下图所示，在Region 1 内，设备A、B、C组成环路。

在CIST（Instance 0）中，如图 17 ，因A的优先级最高，被选为Region Root，再根据其他参数，把A和C间的链路给DISCARDING。因此，对Instance 0的“Vlan组”来说，只有A到B、B到C的链路可用，打断了这个“Vlan组”的环路。

而对MSTI 1（Instance 1）来说，如图 18 ，B的优先级最高，被选为Region Root，再根据其他参数，把B和C间的链路给DISCARDING。因此，对Instance 1的“Vlan组”来说，只有A到B、A到C的链路可用，打断了这个“Vlan组”的环路。

而对MSTI 2（Instance 2）来说，图 19 ，C的优先级最高，被选为Region Root，再根据其他参数，把A和B间的链路给DISCARDING。因此，对Instance 2的“Vlan组”来说，只有B到C、A到C的链路可用，打断了这个“Vlan组”的环路。

用户在这里要注意的是MSTP协议本身不关心一个端口属于哪个Vlan，所以用户应该根据实际的Vlan配置情况来为相关端口配置对应的Path Cost和Priority，以防MSTP协议打断了不该打断的环路。

######  CST （ MSTP region 间的生成树）

个MSTP region对CST来说可以相当于一个大的设备整体，不同的 MSTP Region也生成一个大的网络拓朴树，称为CST(Common Spanning Tree) 。如图 20 所示，对CST来说，Bridge ID最小的设备A被选为整个CST的根(CST Root)，同时也是这个Region内的CIST Regional Root。在Region 2中，由于设备B到CST Root的Root Path Cost最短，所以被选为这个Region内的CIST Regional Root。同理，Region 3选设备C为CIST Regional Root。

CIST Regional Root不一定是该Region内Bridge ID最小的那台设备，它是指该Region内到CST Root的Root Path Cost最小的设备。

同时，CIST Regional Root的Root Port对MSTI来说有了个新的Port Role，为“Master port”，作为所有Instance对外的“出口”，它对所有Instance都是FORWARDING的。为了使拓朴更稳定，我们建议每个Region对CST Root的“出口”尽量只在该Region的一台设备上!

######  MSTP 和 RSTP 、 STP 协议的兼容

对STP协议来说，MSTP会像RSTP那样发STP BPDU来兼容它，详细情况请参考“RSTP与STP的兼容”章节内容。而对RSTP协议来说，本身会处理MSTP BPDU中CIST的部分，因此MSTP不必专门的发RSTP BPDU以兼容它。每台运行STP或RSTP协议的设备都是单独的一个Region，不与任何一个设备组成同一个Region。

#### 10.3.4 MSTP 的可选特性

MSTP的可选特性，主要包括Port Fast端口设置、BPDU Guard设置、BPDU Filter设置、TC Guard和Guard模式设置等。主要用来在MSTP的组网应用中，能够根据网络的拓扑结构和应用特点，针对性地进行MSTP的配置部署，增加MSTP协议运行的稳定性、健壮性和抗功击性，满足MSTP协议在不同用户场景的应用需求。

##### 工作原理

######  Port Fast

如果设备的端口直连着网络终端，那么就可以设置该端口为Port Fast，端口直接Forwarding，这样可免去端口等待Forwarding的过程（如果不配置Port Fast的端口，就要等待 30 秒Forwarding）。下图表示了一个设备的哪些端口可以配置为Port Fast enable。

如果在设了Port Fast的端口中还收到BPDU，则它的Port Fast Operational State为Disabled。这时该端口会按正常的STP算法进行Forwarding。

######  BPDU Guard

BPDU Guard既能全局的enable，也能针对单个Interface进行enable。这两者有些细小的差别。

可以在全局模式中用spanning-tree portfast bpduguard default命令打开全局的BPDU Guard enabled状态，在这种状态下，如果某个Interface打开了Port Fast，或该接口自动识别为边缘口，而该Interface收到了BPDU，该端口就会进入Error-disabled状态，以示配置错误；同时整个端口被关闭，表示网络中可能被非法用户增加了一台网络设备，使网络拓朴发生改变。

也可以在Interface配置模式下用spanning-tree bpduguard enable命令来打开单个Interface的BPDU Guard（与该端口是否打开Port Fast无关）。在这个情况下如果该Interface收到了BPDU，就进入Error-disabled 状态。

######  BPDU Filter

BPDU Filter既能全局的enable，也能针对单个Interface进行enable。这两者有些细小的差别。

可以在全局模式中用spanning-tree portfast bpdufilter default命令打开全局的BPDU Filter enabled状态，在这种状态下，Port Fast enabled的Interface将既不收BPDU，也不发BPDU，这样，直连Port Fast enabled端口的主机就收不到BPDU。而如果Port Fast enabled的Interface因收到BPDU而使Port Fast Operational 状态disabled，BPDU Filter也就自动失效。

也可以在Interface配置模式下用spanning-tree bpdufilter enable命令设置了单个Interface的BPDU Filter enable（与该端口是否打开Port Fast无关）。在这个情况下该Interface既不收BPDU，也不发BPDU，并且是直接Forwarding的。

######  Tc-protection

TC-BPDU报文是指携带TC标志的BPDU报文，交换机收到这类报文表示网络拓扑发生了变化，会进行MAC地址表的删除操作，对三层交换机，还会引发快转模块的重新打通操作，并改变ARP表项的端口状态。为避免交换机受到伪造TC-BPDU报文的恶意攻击时频繁进行以上操作，负荷过重，影响网络稳定，可以使用TC-protection功能进行保护。

Tc-protection只能全局的打开和关闭，缺省情况下为关闭此功能。

在打开相应功能时，收到TC-BPDU报文后的一定时间内（一般为 4 秒），只进行一次删除操作，同时监控该时间段内是否收到TC-BPDU报文。如果在该时间段内收到了TC-BPDU报文，则设备在该时间超时后再进行一次删除操作。这样可以避免频繁的删除MAC地址表项和ARP表项。

######  TC Guard

Tc-Protection功能可以保证网络产生大量tc报文时减少动态MAC地址和ARP的删除，但在遇到TC报文攻击的时候还是会产生很多的删除操作，并且TC报文是可扩散的，将影响整个网络。使用TC Guard功能，我们允许用户在全局或者端口上禁止TC 报文的扩散。当一个端口收到TC报文的时候，如果全局配置了TC Guard或者是端口上配置了TC Guard，则该端口将屏蔽掉该端口接收或者是自己产生的TC报文，使得TC报文不会扩散到其它端口，这样能有效控制网络中可能存在的TC攻击，保持网络的稳定，尤其是在三层设备上，该功能能有效避免接入层设备的振荡引起核心路由中断的问题。

错误的使用tc-guard功能会使网络之间的通讯中断。

建议在确认网络当中有非法的tc报文攻击的情况下再打开此功能。

打开全局的tc-guard,则所有端口都不会对外扩散tc报文。适用于桌面接入设备上开启。

打开接口的tc-guard,则对于该接口产生的拓扑变化以及收到的tc报文，将不向其它端口扩散。适合在上链口，尤其是汇聚接核心的端口开启该功能。

######  TC 过滤

配置TC Guard功能，端口将不扩散TC报文到本设备上其它参与生成树计算的端口，这里的不扩散包括了两种情况：一种是端口收到的TC报文不扩散，一种是端口自己产生的TC报文不扩散。端口自己产生的TC报文是指当端口转发状态发生变化时(例如从block到forwarding的转变)，端口会产生TC报文，表示拓扑可能发生了变化。

这样，可能引发的问题时，由于TC Guard阻止了TC报文的扩散，导致当发生拓扑变化的时候，设备没有清除相应端口的MAC地址，转发数据出错。

因此，引入了TC过滤的概念。TC过滤是指对于端口收到的TC报文不处理，而正常的拓扑变化的情况，能够处理。这样，解决了未配置Portfast的端口频繁地UP/DOWN引起的清地址和核心路由中断的问题，又能保证发生拓扑变化时，核心路由表项能够得到及时地更新。

TC过滤功能缺省关闭。

######  BPDU 源 MAC 检查

BPDU源MAC检查是为了防止通过人为发送BPDU报文来恶意攻击交换机而使MSTP工作不正常。当确定了某端口点对点链路对端相连的交换机时，可通过配置BPDU源MAC检查来达到只接收对端交换机发送的BPDU帧，丢弃所有其他BPDU帧，从而达到防止恶意攻击。你可以在interface模式下来为特定的端口配置相应的BPDU源MAC检查MAC地址，一个端口只允许配置一个过滤MAC地址，通过no bpdu src-mac-check来禁止BPDU源MAC检查，此时端口接收任何BPDU帧。

######  BPDU 非法长度过滤

BPDU的以太网长度字段超过 1500 时，该BPDU帧将被丢弃，以防止收到非法BPDU报文。

######  边缘口的自动识别

指派口在一定的时间范围内(为 3 秒)，如果收不到下游端口发送的BPDU，则认为该端口相连的是一台网络设备，从而设置该端口为边缘端口，直接进入Forwarding状态。自动标识为边缘口的端口因收到BPDU而自动识别为非边缘口。

可以通过spanning-tree autoedge disabled命令取消边缘口的自动识别功能。

该功能是缺省打开的。

边缘口的自动标识功能与手工的Port Fast冲突时，以手工配置的为准。
该功能作用于指派口与下游端口进行快速协商转发的过程中，所以STP协议不支持该功能。同时如果指派口已经处于转发状态，对该端口进行Autoedge的配置不会生效，只有在重新快速协商的过程中才生效，如拔插网线。
端口如果先打开了BPDU Filter,则该端口直接Forwarding，不会自动识别为边缘口。
该功能只适用与指派口。

######  ROOT Guard 功能

在网络设计中常常将根桥和备份根桥划分在同一个域内，由于维护人员的错误配置或网络中的恶意攻击，根桥有可能收到优先级更高的配置信息，从而失去当前根桥的位置，引起网络拓扑的错误的变动。Root Guard功能就是为了防止这种情况的出现。

接口打开Root Guard功能时，强制其在所有实例上的端口角色为指定端口，一旦该端口收到优先级更高的配置信息时，Root Guard功能会将该接口置为root-inconsistent (blocked)状态,在足够长的时间内没有收到更优的配置信息时，端口会恢复成原来的正常状态。

当端口因Root Guard而处于blocked状态时，可以通过手动恢复为正常状态，即关闭端口的ROOT Guard功能或关闭接口的保护功能（在接口模式下配置spanning-tree guard none）。

错误的使用ROOT Guard特性会导致网络链路的断开。
在非指派口上打开ROOT Guard功能会强制其为指派口，同时端口会进入BKN状态，该状态表示端口因Root不一致而进入blocked状态。
如果端口在MST0因收到更优的配置消息而进入BKN状态，会强制端口在其它所有的实例中处于BKN状态。
端口的ROOT Guard和LOOP Guard同一时刻只能有一个生效。^

######  LOOP Guard 功能

由于单向链路的故障，根口或备份口由于收不到BPDU会变成指派口进入转发状态，从而导致了网络中环路的产生，LOOP
Guard功能防止了这种情况的发生。

对于配置了环路保护的端口，如果收不到BPDU，会进行端口角色的迁移，但端口状态将一直被设成discarding状态。直到重
新收到BPDU而进行生成树的重计算。

可以基于全局或接口打开LOOP Guard特性。

端口的ROOT Guard和LOOP Guard同一时刻只能有一个生效。

MSTP进程重启前，端口进入环路保护的block状态，而MSTP进程重启后，如果端口仍然接收不到BPDU，则端口将转变成指派口并进入forward状态。因此，建议在重启MSTP进程前，检查端口进入环路保护的block状态的原因并及时解决，避免进程重启后生成树拓扑仍然出现异常。

######  BPDU 透传

在IEEE 802.1Q标准中，BPDU的目的MAC地址 01 - 80 - C2- 00 - 00 - 00 是作为保留地址使用的，即遵循IEEE 802.1Q标准的设备，对于接收到的BPDU帧是不转发的。然而，在实际的网络布署中，可能需要设备能够支持透传BPDU帧。例如，设备未开启STP协议时，需要透传BPDU帧，使得与之互连的设备之间的生成树计算正常。

BPDU透传默认关闭。
BPDU透传功能只在STP协议关闭时才启作用。当STP协议打开时，设备不透传BPDU帧。

######  BPDU TUNNEL

在QINQ网络中，通常分为用户网络和运营商网络。QinQ的基本原理是在用户报文进入运营商网络之前封装上一个运营商网络的VLAN Tag，而把用户报文中的原有的VLAN Tag当做数据，使报文带着两层VLAN Tag穿越运营商网络。在运营商网络中，报文只根据外层VLAN Tag传播，当用户报文离开运营商网络时，剥去外层VLAN Tag。

为了实现用户网络之间STP协议报文的传输而又不对运营商网络产生影响，可以使用STP报文透传功能，即BPDU TUNNEL功能。当用户网络中STP协议报文进入边缘设备后，将目的mac地址改成私有地址在运营商网络中转发，到了另外一端边缘设备后，再将目的mac地址改成公有地址回到另一端用户网络，以达到STP协议报文在运营商网络透传的效果，从而使得用户网络和运营商网络的STP协议分开计算，互不干扰。

### 10.4 配置详解

<table>
  <thead>
    <tr>
      <th>配置项</th>
      <th colspan="2">配置建议 & 相关命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">打开生成树协议</td>
      <td colspan="2">必须配置。用于打开生成树协议。</td>
    </tr>
    <tr>
      <td>spanning-tree </td>
      <td>打开生成树协议，并配置基本属性。</td>
    </tr>     
    <tr>
      <td>spanning-tree mode </td>
      <td>配置生成树模式。</td>
    </tr>
    <tr>
      <td rowspan="3">配置生成树的兼容性</td>
      <td colspan="2">可选配置。用于兼容友商设备。</td>
    </tr>
    <tr>
      <td>spanning-tree compatible enable</td>
      <td>打开接口的兼容模式。</td>
    </tr>
    <tr>
      <td>clear spanning-tree detected-protocols</td>
      <td>对 BPDU 进行强制版本检查。</td>
    </tr>      
    <tr>
      <td rowspan="2">配置 MSTP Region</td>
      <td colspan="2">可选配置。用于配置 MSTP Region。</td>
    </tr>
    <tr>
      <td>spanning-tree mst configuration </td>
      <td>进入 MSTP Region 配置模式。</td>
    </tr>
    <tr>
      <td rowspan="2">配置 RSTP 快速收敛</td>
      <td colspan="2">可选配置。用于配置端口的连接类型是不是“点对点连接”。</td>
    </tr>
    <tr>
      <td>spanning-tree link-type </td>
      <td>配置 link type。</td>
    </tr>   
    <tr>
      <td rowspan="3">配置优先级</td>
      <td colspan="2">可选配置。用于配置设备优先级或者端口优先级。</td>
    </tr>
    <tr>
      <td>spanning-tree priority </td>
      <td>配置设备优先级。</td>
    </tr>    
    <tr>
      <td>spanning-tree port-priority </td>
      <td>配置端口优先级。</td>
    </tr>       
    <tr>
      <td rowspan="3">配置接口的路径花费</td>
      <td colspan="2">可选配置。用于配置端口的路径花费或路径花费缺省计算方法。</td>
    </tr>
    <tr>
      <td>spanning-tree cost</td>
      <td>配置端口的路径花费。</td>
    </tr>
    <tr>
      <td>spanning-tree pathcost method</td>
      <td>配置路径花费的缺省计算方法。</td>
    </tr>      
    <tr>
      <td rowspan="2">配置 BPDU 帧的最大跳数</td>
      <td colspan="2">可选配置。用于配置 BPDU 帧的最大跳数。</td>
    </tr>
    <tr>
      <td>spanning-tree max-hops </td>
      <td>配置 BPDU 帧的最大跳数。</td>
    </tr>  
    <tr>
      <td rowspan="6">配置接口 port fast 的相关特性</td>
      <td colspan="2">可选配置。用于配置 port fast 特性。</td>
    </tr>
    <tr>
      <td>spanning-tree portfast </td>
      <td>打开 port fast 特性。</td>
    </tr>      
    <tr>
      <td>spanning-tree portfast bpduguard default </td>
      <td>打开所有接口的 BPDU Guard。</td>
    </tr>  
    <tr>
      <td>spanning-tree bpduguard enabled </td>
      <td>打开某个接口的 BPDU Guard。</td>
    </tr>  
    <tr>
      <td>spanning-tree portfast bpdufilter default </td>
      <td>打开所有接口的 BPDU Filter。</td>
    </tr>   
    <tr>
      <td>spanning-tree bpdufilter enabled </td>
      <td>打开某个接口的 BPDU Filter。</td>
    </tr>  
    <tr>
      <td rowspan="5">配置 TC 相关的特性</td>
      <td colspan="2">可选配置。用于配置 TC 特性。</td>
    </tr>
    <tr>
      <td>spanning-tree tc-protection </td>
      <td>打开 tc protection。</td>
    </tr>      
    <tr>
      <td>spanning-tree tc-protection tc-guard </td>
      <td>打开所有接口的 tc guard。</td>
    </tr>  
    <tr>
      <td>spanning-tree tc-guard  </td>
      <td>打开某个接口的 tc guard。</td>
    </tr>  
    <tr>
      <td>spanning-tree ignore tc </td>
      <td>打开某个接口的 tc 过滤。</td>
    </tr>  
    <tr>
      <td rowspan="2">配置 BPDU 源 MAC 检查</td>
      <td colspan="2">可选配置。用于配置 BPDU 源 MAC 检查功能。</td>
    </tr>
    <tr>
      <td>bpdu src-mac-check </td>
      <td>打开某个接口的 BPDU 源 MAC 检查。</td>
    </tr>    
    <tr>
      <td rowspan="2">配置边缘口的自动识别</td>
      <td colspan="2">可选配置。用于配置边缘口的自动识别功能。</td>
    </tr>
    <tr>
      <td>spanning-tree autoedge </td>
      <td>打开某个接口的边缘口自动识别，缺省是打开的</td>
    </tr>        
    <tr>
      <td rowspan="5">配置接口保护相关的特性</td>
      <td colspan="2">可选配置。用于配置接口保护相关的功能。</td>
    </tr>
    <tr>
      <td>spanning-tree guard root </td>
      <td>打开某个接口的 root guard。</td>
    </tr>      
    <tr>
      <td>spanning-tree loopguard default </td>
      <td>打开所有接口的 loop guard。</td>
    </tr>  
    <tr>
      <td>spanning-tree guard loop  </td>
      <td>打开某个接口的 loop guard。</td>
    </tr>  
    <tr>
      <td>spanning-tree guard none </td>
      <td>关闭某个接口的 guard 特性。</td>
    </tr>  
    <tr>
      <td rowspan="2">配置 BPDU 透传功能 </td>
      <td colspan="2">可选配置。用于配置 BPDU 透传功能。</td>
    </tr>
    <tr>
      <td>bridge-frame forwarding protocol bpdu </td>
      <td>打开 BPDU 透传功能。</td>
    </tr> 
	<tr>
      <td rowspan="4">配置 BPDU TUNNEL</td>
      <td colspan="2">可选配置。用于配置 BPDU TUNNEL 功能。</td>
    </tr>
    <tr>
      <td>l2protocol-tunnel stp </td>
      <td>全局使能 BPDU TUNNEL 功能。</td>
    </tr>     
    <tr>
      <td>l2protocol-tunnel stp enable  </td>
      <td>接口使能 BPDU TUNNEL 功能。</td>
    </tr>     
    <tr>
      <td>l2protocol-tunnel stp tunnel-dmac   </td>
      <td>配置 BPDU TUNNEL 的透传地址。</td>
    </tr>        
  </tbody>
</table>





#### 10.4.1 打开生成树协议

##### 配置效果

+ 打开全局Spanning Tree协议，同时设置全局的基本设置

+ 配置Spanning Tree模式

##### 注意事项

+ 缺省情况下，Spanning Tree协议是关闭的；当打开Spanning Tree协议时，设备即开始运行生成树协议，本设备缺省运行的是MSTP协议。

+ Spanning Tree协议的缺省模式是MSTP模式。

+ Spanning Tree协议与数据中心的TRILL协议功能互斥。

**配置方法**

######  打开 Spanning Tree 协议

+ 必须配置。

+ 若无特殊要求，应在每台设备上启动Spanning Tree协议。

+ 使用spanning-tree [ forward-time seconds | hello-time seconds | max-age seconds ]命令可以打开STP，所带参数可在打开STP的同时，设置全局的基本设置。

+ forward-time取值范围是< 4 - 30 >，hello-time取值范围是<1-10>，max-age取值范围是<6-40>。

在设备运行过程中执行clear命令，可能因为重要信息丢失而导致业务中断。forward-time、hello-time、max-age三个值的范围是相关的，修改了其中一个会影响到其他两个的值范围。这三个值之间有一个制约关系： 2 *(Hello Time+1.0 second)<= Max-Age Time <= 2*(Forward-Delay–1.0 second)，不符合这个条件的值也会设置不成功。

【命令格式】 spanning-tree [ forward-time^ seconds^ |^ hello-time^ seconds^ | max-age^ seconds^ | tx-hold-count^ numbers]^
【参数说明】 forward-time seconds：端口状态改变的时间间隔，取值范围为 4 - 30 秒，缺省值为 15 秒。
hello-time seconds：设备定时发送BPDU报文的时间间隔，取值范围为 1 - 10 秒，缺省值为 2 秒。
max-age second：BPDU报文消息生存的最长时间，取值范围为 6 - 40 秒，缺省值为 20 秒。
tx-hold-count numbers：配置每秒最多发送BPDU个数，取值范围为 1 - 10 个，缺省值为 3 个。
【缺省配置】 spanning-tree功能关闭
【命令模式】 全局配置模式
【使用指导】 forward-time 、 hello-time 、 max-age三个值的范围是相关的，修改了其中一个会影响到其他两个的值范围。这三个值之间有一个制约关系：
2*(Hello Time+1.0 second) <= Max-Age Time <= 2*(Forward-Delay–1.0 second) 您配置的这三个参数必须满足这个条件，否则有可能导致拓朴不稳定，也会设置不成功。

######  配置 Spanning Tree 模式

+ 可选配置

+ 按802.1相关协议标准，STP、RSTP、MSTP这三个版本的Spanning Tree协议本来就无须管理员再多做设置，版本间自然会互相兼容。但考虑到有些厂家不完全按标准实现，可能会导致一些兼容性的问题。因此我们提供这么一条命令配置，以供管理员在发现其他厂家的设备与本设备不兼容时，能够切换到低版本的Spanning Tree模式，以兼容之。

+ 使用spanning-tree mode [ stp | rstp | mstp ]命令可以修改STP模式。

【命令格式】 spanning-tree mode^ [ stp | rstp | mstp^ ]^
【参数说明】 stp：Spanning tree protocol(IEEE 802.1d)
rstp：Rapid spanning tree protocol(IEEE 802.1w)
mstp：Multiple spanning tree protocol(IEEE 802.1s)
【缺省配置】 MSTP版本
【命令模式】 全局配置模式
【使用指导】 有些友商产品不完全按标准实现，可能会导致一些兼容性的问题。在管理员发现其他厂家的设备与本设备不兼容时，使用此命令可以切换到低版本的Spanning Tree模式，以兼容之。

**检验方法**

+ 显示验证

**配置举例**

######  配置 Spanning Tree 协议和定时器参数


【配置方法】

 + 设备开启生成树协议，同时配置生成树协议模式为STP协议。

+ 配置根桥DEV A的定时器参数为：Hello Time=4s，Max Age=25s，Forward Delay=18s。

DEV A (^) 第一步，开启生成树协议，同时配置生成树协议模式为STP协议。

```
Ruijie#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)#spanning-tree
Ruijie(config)#spanning-tree mode stp
```

第二步，配置根桥DEV A的定时器参数

```
Ruijie(config)#spanning-tree hello-time 4
Ruijie(config)#spanning-tree max-age 25
Ruijie(config)#spanning-tree forward-time 18
```

DEV B (^) 第一步，开启生成树协议，同时配置生成树协议模式为STP协议。

```
Ruijie#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)#spanning-tree
Ruijie(config)#spanning-tree mode stp
```

【检验方法】  通过show spanning-tree summary查看生成树拓扑和协议配置参数。

```
DEV A Ruijie#show spanning-tree summary
Spanning tree enabled protocol stp
Root ID Priority 0
Address 00d0.f822.3344
this bridge is root
Hello Time 4 sec Forward Delay 18 sec Max Age 25 sec
Bridge ID Priority 0
Address 00d0.f822.3344
Hello Time 4 sec Forward Delay 18 sec Max Age 25 sec
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/2 Desg FWD 20000 128 False P2p
Gi0/1 Desg FWD 20000 128 False P2p
DEV B Ruijie#show spanning-tree summary
```



```
DEVB
Spanning tree enabled protocol stp
Root ID Priority 0
Address 00d0.f822.3344
this bridge is root
Hello Time 4 sec Forward Delay 18 sec Max Age 25 sec
Bridge ID Priority 32768
Address 001a.a917.78cc
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/ 2 Altn BLK 20000 128 False P2p Bound(STP)
Gi0/1 Root FWD 20000 128 False P2p Bound(STP)
```



##### 常见错误

+ 配置生成树协议定时器相关参数，只有在设备选举为生成树的根桥时才起作用。即非根桥的定时器参数是以根桥的定时器参数为准。

#### 10.4.2 配置生成树的兼容性

##### 配置效果

+ 配置接口的兼容性模式，可以实现与其它产商之间的互连。

+ 配置Protocol Migration进行强制版本检查会影响RSTP与STP的兼容。

##### 注意事项

+ 配置接口的兼容性模式，可以使该端口发送BPDU时根据当前端口的属性有选择的携带不同的MSTI的信息，以实现与其它产商之间的互连。

##### 配置方法

######  配置接口的兼容性模式

+ 可选配置。

【命令格式】 spanning-tree compatible enable
【参数说明】 -
【缺省配置】 缺省是关闭接口的兼容模式
【命令模式】 接口模式
【使用指导】 打开接口的兼容模式，可以使当前端口的接口属性信息有选择性的携带MSTI的信息进行发送，以实现与其它产商之间的互连。

######  配置 Protocol Migration

+ 可选配置

+ 管理员发现对端设备可支持RSTP协议时，可将本设备设置为强制版本检查，强制两对接设备运行RSTP协议。

+ 使用clear spanning-tree detected-protocols [ interface interface-id ]命令可以让该端口强制进行版本检查。相关说明请参看 RSTP与STP的兼容。

【命令格式】 clear spanning-tree detected-protocols [ interface interface-id ]
【参数说明】 interface interface-id：对应的接口
【缺省配置】 -
【命令模式】 特权模式
【使用指导】 此命令用来强制接口发送RSTP BPDU帧，对BPDU帧执行强制检查。

**检验方法**

+ 显示验证。

##### 配置举例

######  配置 Spanning Tree 协议兼容模式

【配置方法】 

+ 设备A，B配置实例 1 ， 2 。实例 1 关联VLAN 10，实例 2 关联VLAN 20。
+ 端口gi 0/1属于VLAN 10，gi 0/2属于VLAN 20，配置端口的生成树兼容模式。

DEV A  第一步，创建实例 1 ， 2 。实例 1 关联VLAN 10，实例 2 关联VLAN 20。

```
Ruijie#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)#spanning-tree mst configuration
Ruijie(config-mst)#instance 1 vlan 10
Ruijie(config-mst)#instance 2 vlan 20
```

第二步，配置端口所属的VLAN，同时开启端口的生成树兼容模式。

```
Ruijie(config)#int gi 0/1
Ruijie(config-if-GigabitEthernet 0/1)#switchport access vlan 10
Ruijie(config-if-GigabitEthernet 0/1)#spanning-tree compatible enable
Ruijie(config-if-GigabitEthernet 0/1)#int gi 0/2
Ruijie(config-if-GigabitEthernet 0/ 2 )#switchport access vlan 20
Ruijie(config-if-GigabitEthernet 0/ 2 )#spanning-tree compatible enable
```

DEV B (^) 同DEV A。

【检验方法】 

+ 通过show spanning-tree summary查看生成树拓扑计算是否正确。

```
DEV A 
Ruijie#show spanning-tree summary
Spanning tree enabled protocol mstp
MST 0 vlans map : 1-9, 11-19, 21- 4094
Root ID Priority 32768
Address 001a.a917.78cc
this bridge is root
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Bridge ID Priority 32768
Address 001a.a917.78cc
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Interface Role Sts Cost Prio OperEdge Type

---------------- ---- --- ---------- -------- -------- ----------------

Gi0/ 2 Desg FWD 20000 128 False P2p
Gi0/1 Desg FWD 20000 128 False P2p
MST 1 vlans map : 10
Region Root Priority 32768
Address 001a.a917.78cc
this bridge is region root
Bridge ID Priority 32768
Address 001a.a917.78cc
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/ 1 Desg FWD 20000 128 False P2p
MST 2 vlans map : 20
Region Root Priority 32768
Address 001a.a917.78cc
this bridge is region root
Bridge ID Priority 32768
Address 001a.a917.78cc
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/ 2 Desg FWD 20000 128 False P2p
```

```
DEV B 
Ruijie#show spanning-tree summary
Spanning tree enabled protocol mstp
MST 0 vlans map : 1-9, 11-19, 21- 4094
Root ID Priority 32768
Address 001a.a917.78cc
this bridge is root
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Bridge ID Priority 32768
Address 00d0.f822.3344
Hello Time 4 sec Forward Delay 18 sec Max Age 25 sec
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/2 Altn BLK 20000 128 False P2p
Gi0/1 Root FWD 20000 128 False P2p
MST 1 vlans map : 10
Region Root Priority 32768
Address 001a.a917.78cc
this bridge is region root
Bridge ID Priority 32768
Address 00d0.f822.3344
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/1 Root FWD 20000 128 False P2p
MST 2 vlans map : 20
Region Root Priority 32768
Address 001a.a917.78cc
this bridge is region root
Bridge ID Priority 2768
Address 00d0.f822.3344
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/2 Root FWD 20000 128 False P2p
```

##### 常见错误

 配置端口的兼容模式，需要关注端口的VLAN裁剪信息。建议链路两端的端口VLAN列表配置一致。

#### 10.4.3 配置 MSTP Region

##### 配置效果

+ 配置MSTP Region可以改变哪些设备处于同一个MSTP Regin内，从而影响网络拓扑。

##### 注意事项

+ 要让多台设备处于同一个MSTP Region，就要让这几台设备有相同的名称（Name）、相同的Revision Number、相同的Instance—Vlan对应表。

+ 可以配置 0 － 64 号Instance包含哪些Vlan，剩下的Vlan就自动分配给Instance 0。一个Vlan只能属于一个Instance。

+ 建议您在关闭STP的模式下配置Instance—Vlan的对应表，配置好后再打开MSTP，以保证网络拓朴的稳定和收敛。

##### 配置方法

######  配置 MSTP Region

+ 可选配置

+ 要让多台设备处于同一个MSTP Region时配置。

+ 通过spanning-tree mst configuration命令配置MSTP Region配置模式。

+ 通过instance instance-id vlan vlan-range命令配置MST Instance与Vlan的对应关系。

+ 通过name name命令配置MST名称。

+ 通过revision version命令配置MST版本号。

【命令格式】 spanning-tree mst configuration
【参数说明】 -
【缺省配置】 -
【命令模式】 全局配置模式
【使用指导】 配置该命令进入MST 配置模式

【命令格式】 instance instance-id vlan vlan-range
【参数说明】 instance-id：MST Instance ID，范围为 0 － 64 。
vlan-range：VLAN ID，范围为 1 － 4094 。
【缺省配置】 缺省instance和vlan的对应关系是所有的Vlan都在Instance 0中
【命令模式】 MST 配置模式
【使用指导】 把vlan组添加到一个MST instance中使用此命令。
举例来说：
instance 1 vlan 2- 200 就是把vlan 2到vlan 200都添加到instance 1中。
instance 1 vlan 2,20,200 就是把vlan 2、vlan 20，vlan 200添加到instance 1中。
同样，您可以用no命令把vlan从instance中删除，删除的vlan自动转入instance 0。

【命令格式】 name name
【参数说明】 name：MST配置名称，该字符串最多可以有 32 个字节。
【缺省配置】 name为空字符串
【命令模式】 MST 配置模式
【使用指导】 -

【命令格式】 revision version
【参数说明】 version：指定MST revision number，范围为 0 － 65535 。缺省值为 0
【缺省配置】 revision为 0
【命令模式】 MST 配置模式
【使用指导】 -

##### 检验方法

+ 显示验证。

+ 使用show spanning-tree mst configuration查看MSTP Region配置信息。

##### 配置举例

以下配置举例，仅介绍与MSTP和VRRP相关的配置。

######  在 MSTP+VRRP 拓扑中，配置 MSTP 协议，实现 VLAN 的负载均衡

【配置方法】 

+ 在交换机A，B，C，D上，打开MSTP协议，创建实例 1 ， 2 。
+ 配置交换机A为MSTP的实例 0 和 1 的根桥，交换机B为实例 2 的根桥。
+ 配置交换机A为VLAN 1， 10 的VRRP的Master设备，交换机B为VLAN 20的VRRP的Master设备。

A 第一步，配置VLAN 10,20，同时设备互联端口配置成Trunk口

```
A(config)#vlan 10
A(config-vlan)#vlan 20
A(config-vlan)#exit
A(config)#int range gi 0/1- 2
A(config-if-range)#switchport mode trunk
A(config-if-range)#int ag 1
A(config-if-AggregatePort 1)# switchport mode trunk
```

第二步，打开MSTP，同时创建实例 1 ， 2

```
A(config)#spanning-tree
A(config)# spanning-tree mst configuration
A(config-mst)#instance 1 vlan 10
A(config-mst)#instance 2 vlan 20
A(config-mst)#exit
```

第三步，配置设备A为实例 0 和 1 的根桥

```
A(config)#spanning-tree mst 0 priority 4096
A(config)#spanning-tree mst 1 priority 4096
A(config)#spanning-tree mst 2 priority 8192
```

第四步，配置VRRP的优先级，使设备A为VLAN 10的VRRP Master设备，同时配置VRRP虚网关IP地址

```
A(config)#interface vlan 10
A(config-if-VLAN 10)ip address 192.168.10.2 255.255.255.0
A(config-if-VLAN 10) vrrp 1 priority 120
A(config-if-VLAN 10) vrrp 1 ip 192.168.10.1
```

第五步，VRRP的默认优先级为 100 ，使设备A为VLAN 20的VRRP Backup设备

```
A(config)#interface vlan 20
A(config-if-VLAN 20 )ip address 192.168.20.2 255.255.255.0
A(config-if-VLAN 20 ) vrrp 1 ip 192.168. 20 .1
```

B 第一步，配置VLAN 10,20，同时设备互联端口配置成Trunk口

```
B(config)#vlan 10
B(config-vlan)#vlan 20
B(config-vlan)#exit
B(config)#int range gi 0/1- 2
B(config-if-range)#switchport mode trunk
B(config-if-range)#int ag 1
B(config-if-AggregatePort 1)# switchport mode trunk
```

第二步，打开MSTP，同时创建实例 1 ， 2

```
B(config)#spanning-tree
B(config)# spanning-tree mst configuration
B(config-mst)#instance 1 vlan 10
B(config-mst)#instance 2 vlan 20
B(config-mst)#exit
```

第三步，配置设备A为实例 2 的根桥

```
B(config)#spanning-tree mst 0 priority 8192
B(config)#spanning-tree mst 1 priority 8192
B(config)#spanning-tree mst 2 priority 4096
```

第四步，配置VRRP虚网关IP地址

```
B(config)#interface vlan 10
B(config-if-VLAN 10)ip address 192.168.10.3 255.255.255.0
B(config-if-VLAN 10) vrrp 1 ip 192.168.10.1
```

第五步，配置VRRP的优先级为 120 ，使设备B为VLAN 20的VRRP Master设备

```
B(config)#interface vlan 20
B(config-if-VLAN 20 )vrrp 1 priority 120
B(config-if-VLAN 20 )ip address 192.168.20.3 255.255.255.0
B(config-if-VLAN 20 ) vrrp 1 ip 192.168. 20 .1
```

C 第一步，配置VLAN 10,20，同时设备互联端口配置成Trunk口

```
C(config)#vlan 10
C(config-vlan)#vlan 20
C(config-vlan)#exit
C(config)#int range gi 0/1- 2
C(config-if-range)#switchport mode trunk
```

第二步，打开MSTP，同时创建实例 1 ， 2

```
C(config)#spanning-tree
C(config)# spanning-tree mst configuration
C(config-mst)#instance 1 vlan 10
C(config-mst)#instance 2 vlan 20
C(config-mst)#exit
```

第三步，配置设备C直接用户的端口为Portfast口，同时启用BPDU Guard。

```
C(config)#int gi 0/3
C(config-if-GigabitEthernet 0/3)#spanning-tree portfast
C(config-if-GigabitEthernet 0/3)#spanning-tree bpduguard enable
```

D 同设备C。

【检验方法】 

+ 通过show spanning-tree summary查看生成树拓扑计算的正确性。
+ 通过show vrrp brief查看VRRP主备是否建立成功。

```
A Ruijie#show spanning-tree summary
Spanning tree enabled protocol mstp
MST 0 vlans map : 1-9, 11-19, 21- 4094
Root ID Priority 4096
Address 00d0.f822.3344
this bridge is root
Hello Time 4 sec Forward Delay 18 sec Max Age 25 sec
Bridge ID Priority 4096
Address 00d0.f822.3344
Hello Time 4 sec Forward Delay 18 sec Max ge 25 sec
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- - --------- -------- -------- ----------------
Ag1 Desg FWD 19000 128 False P2p
Gi0/1 Desg FWD 200000 128 False P2p
Gi0/ 2 Desg FWD 200000 128 False P2p
MST 1 vlans map : 10
Region Root Priority 4096
Address 00d0.f822.3344
this bridge is region root
Bridge ID Priority 4096
Address 00d0.f822.3344
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Ag1 Desg FWD 19000 128 False P2p
Gi0/1 Desg FWD 200000 128 False P2p
Gi0/ 2 Desg FWD 200000 128 False P2p
MST 2 vlans map : 20
Region Root Priority 4096
Address 001a.a917.78cc
this bridge is region root
Bridge ID Priority 8192
Address 00d0.f822.3344
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Ag1 Root FWD 19000 128 False P2p
Gi0/1 Desg FWD 200000 128 False P2p
Gi0/ 2 Desg FWD 200000 128 False P2p
B Ruijie#show spanning-tree summary
Spanning tree enabled protocol mstp
MST 0 vlans map : 1-9, 11-19, 21- 4094
Root ID Priority 4096
Address 00d0.f822.3344
this bridge is root
Hello Time 4 sec Forward Delay 18 sec Max Age 25 sec
Bridge ID Priority 8192
Address 001a.a917.78cc
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- - --------- -------- -------- ----------------
Ag1 Root FWD 19000 128 False P2p
Gi0/1 Desg FWD 200000 128 False P2p
Gi0/ 2 Desg FWD 200000 128 False P2pMST 1 vlans map : 10
Region Root Priority 4096
Address 00d0.f822.3344
this bridge is region root
Bridge ID Priority 8192
Address 001a.a917.78cc
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Ag1 Root FWD 19000 128 False P2p
Gi0/1 Desg FWD 200000 128 False P2p
Gi0/ 2 Desg FWD 200000 128 False P2p
MST 2 vlans map : 20
Region Root Priority 4096
Address 001a.a917.78cc
this bridge is region root
Bridge ID Priority 4096
Address 001a.a917.78cc
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Ag1 Desg FWD 19000 128 False P2p
Gi0/1 Desg FWD 200000 128 False P2p
Gi0/ 2 Desg FWD 200000 128 False P2p
C Ruijie#show spanning-tree summary
Spanning tree enabled protocol mstp
MST 0 vlans map : 1-9, 11-19, 21- 4094
Root ID Priority 4096
Address 00d0.f822.3344
this bridge is root
Hello Time 4 sec Forward Delay 18 sec Max Age 25 sec
Bridge ID Priority 32768
Address 001a.a979.00ea
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Interface Role Sts Cost Prio Type OperEdge
---------------- ---- --- ---------- -------- ----- ---------------
Fa0/2 Altn BLK 200000 128 P2p False
Fa0/1 Root FWD 200000 128 P2p False
MST 1 vlans map : 10
Region Root Priority 4096
Address 00d0.f822.3344
this bridge is region root
Bridge ID Priority 32768
Address 001a.a979.00ea
Interface Role Sts Cost Prio Type OperEdge
---------------- ---- --- ---------- -------- ----- ---------------
Fa0/2 Altn BLK 200000 128 P2p False
Fa0/1 Root FWD 200000 128 P2p False
MST 2 vlans map : 20
Region Root Priority 4096
Address 001a.a917.78cc
this bridge is region root
Bridge ID Priority 32768
Address 001a.a979.00ea
Interface Role Sts Cost Prio Type OperEdge
---------------- ---- --- ------ -------- ----- ---------------
Fa0/2 Root FWD 200000 128 P2p False
Fa0/1 Altn BLK 200000 128 P2p False
```

**常见错误**

+ MSTP拓扑中，MST域的配置建议配置一致。
+  配置实例和VLAN的映射关系时，VLAN没有创建。
+  在MSTP+VRRP拓扑中，设备如果运行STP或RSTP协议，则该设备是按照不同MST域的算法进行生成树计算。

#### 10.4.4 配置 RSTP 快速收敛

##### 配置效果

+ 配置link-type关系到RSTP是否能快速的收敛。

##### 注意事项

+ 配置该端口的连接类型是不是“点对点连接”，这一点关系到RSTP是否能快速的收敛。请参照“RSTP的快速收敛”。当您不设置该值时，设备会根据端口的“双工”状态来自动设置的，全双工的端口就设link type为point-to-point，半双工就设为shared。您也可以强制设置link type来决定端口的连接是不是“点对点连接”。

##### 配置方法

######  配置 link-type

+ 可选配置。

【命令格式】 spanning-tree link-type [ point-to-point | shared ]
【参数说明】 point-to-point：强制设置该接口的连接类型为point-to-point
shared：强制设置该接口的连接类型为shared
【缺省配置】 接口类型为全双工时，该接口的连接类型为point-to-point；接口类型为半双工时该接口的连接类型为shared
【命令模式】 接口配置模式
【使用指导】 配置该端口的连接类型是不是“点对点连接”，这一点关系到RSTP是否能快速的收敛。当用户不设置该值时，设备会根据端口的“双工”状态来自动设置的。

##### 检验方法

+ 显示验证。

+ 使用show spanning-tree [mst instance-id] interface interface-id命令查看生成树接口的配置信息。

##### 配置举例

######  配置 RSTP 快速收敛

【配置方法】 配置端口的连接类型为点对点网络。

```
Ruijie(config)#int gi 0/1
Ruijie(config-if-GigabitEthernet 0/1)#spanning-tree link-type point-to-point
```

【检验方法】  

+ 通过show spanning-tree summary查看端口连接类型。

```
Ruijie#show spanning-tree summary
Spanning tree enabled protocol mstp
MST 0 vlans map : ALL
Root ID Priority 32768
Address 001a.a917.78cc
this bridge is root
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Bridge ID Priority 32768
Address 00d0.f822.3344
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/1 Root FWD 20000 128 False P2p
```



**常见错误**

+ 端口的连接类型和速率、双工有关。如果是半双工，则连接类型为shared。

#### 10.4.5 配置优先级

##### 配置效果

+ 设置设备优先级（Switch Priority）关系着到底哪个设备为整个网络的根，同时也关系到整个网络的拓朴结构。

+ 设置端口的优先级（Port Priority）关系着到底哪个端口进入Forwarding状态。

##### 注意事项

+ 建议管理员把核心设备的优先级设得高些（数值小），这样有利于整个网络的稳定。可以给不同的Instance分配不同的设备优先级，各个Instance可根据这些值运行独立的生成树协议。对于不同Region间的设备，它们只关心CIST（Instance 0 ）的优先级。如Bridge ID所讲，优先级的设置值有 16 个，都为 4096 的倍数，分别是 0 ， 4096 ， 8192 ， 12288 ， 16384 ，20480 ， 24576 ， 28672 ， 32768 ， 36864 ， 40960 ， 45056 ， 49152 ， 53248 ， 57344 ， 61440 。缺省值为 32768 。

+ 当有两个端口都连在一个共享介质上，设备会选择一个高优先级（数值小）的端口进入Forwarding状态，低优先级（数值大）的端口进入Discarding状态。如果两个端口的优先级一样，就选端口号小的那个进入Forwarding状态。您可以在一个端口上给不同的Instance分配不同的端口优先级，各个Instance可根据这些值运行独立的生成树协议。

+ 端口优先级和设备优先级一样，可配置的优先级值也有 16 个，都为 16 的倍数，分别是 0 ， 16 ， 32 ， 48 ， 64 ， 80 ， 96 ，112 ， 128 ， 144 ， 160 ， 176 ， 192 ， 208 ， 224 ， 240 。缺省值为 128 。

##### 配置方法

######  配置设备优先级

+ 可选配置

+ 在管理员需要改变网络的根或者拓扑结构时需要配置设备优先级。

【命令格式】 spanning-tree [ mst instance-id ] priority priority
【参数说明】 mst instance-id：Instance号，范围为 0 － 64
priority priority：设备优先级，可选用0, 4096,8192, 12288, 16384, 20480, 24576, 28672, 32768, 36864,40960, 45056, 49152,53248, 57344和 61440 。共 16 个整数，均为 4096 的倍数。
【缺省配置】 instance-id的缺省值为 0 ，priority的缺省值为 32768
【命令模式】 全局配置模式
【使用指导】 设置设备的优先级关系到哪个设备为整个网络的根，同时也关系到整个网络的拓朴结构。

######  配置端口优先级

+ 可选配置

+ 在管理员需要改变哪个端口优先进入Forwarding状态时配置。

【命令格式】 spanning-tree [ mst instance-id ] port-priority priority
【参数说明】 mst instance-id：Instance号，范围为 0 － 64 。
port-priority priority：端口优先级，可选用 0 ， 16 ， 32 ， 48 ， 64 ， 80 ， 96 ， 112 ， 128 ， 144 ， 160 ， 176 ， 192 ，208 ， 224 ， 240 ，共 16 个整数，均为 16 的倍数。
【缺省配置】 Instance-id的缺省值为 0
priority的缺省值为 128
【命令模式】 接口配置模式
【使用指导】 在Region内形成环路时，优先选择高优先级的端口处于发送状态。优先级相同时，以选用接口号较小的端口。使用此命令，这将影响到Region 内形成环路中的哪个端口会处于发送状态。

##### 检验方法

+ 显示验证

+ 使用show spanning-tree [ mst instance-id ] interface interface-id命令查看生成树接口的配置信息。

##### 配置举例

######  配置端口优先级

【配置方法】  

+ 配置网桥优先级，使DEV A为生成树根桥。 
+ 配置DEV A的端口gi 0/2的端口优先级为 16 ，使DEV B的端口gi 0/2选举为根端口。

 第一步，打开生成树协议，配置网桥优先级。

```
DEV A
Ruijie(config)#spanning-tree
Ruijie(config)#spanning-tree mst 0 priority 0
```

第二步，配置端口Gi 0/2的端口优先级。

```
DEV B
Ruijie(config)# int gi 0/2
Ruijie(config-if-GigabitEthernet 0/2)#spanning-tree mst 0 port-priority 16
Ruijie(config)#spanning-tree
```

【检验方法】 

+ 通过show spanning-tree summary查看生成树拓扑计算结果。

```
DEV A Ruijie# Ruijie#show spanning-tree summary
Spanning tree enabled protocol mstp
MST 0 vlans map : ALL
Root ID Priority 0
Address 00d0.f822.3344
this bridge is root
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Bridge ID Priority 0
Address 00d0.f822.3344
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/2 Desg FWD 20000 16 False P2p
Gi0/1 Desg FWD 20000 128 False P2p
```

```
DEV B Ruijie#show spanning-tree summary
Spanning tree enabled protocol mstp
MST 0 vlans map : ALL
Root ID Priority 0
Address 00d0.f822.3344
this bridge is root
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Bridge ID Priority 32768
Address 001a.a917.78cc
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/ 2 Root FWD 20000 128 False P2p
Gi0/ 1 Altn BLK 20000 128 False P2p
```

##### 常见错误

 端口优先级只有在指派端口修改才起作用。

#### 10.4.6 配置接口的路径花费

##### 配置效果

+ 端口的路径花费（Path Cost）会影响端口的转发状态，及影响整个网络的拓扑结构。

+ 当某端口Path Cost为缺省值时，配置路径花费的计算方法会影响端口的路径花费计算结果。

##### 注意事项

+ 设备是根据哪个端口到根桥（Root Bridge）的Path Cost总和最小而选定Root Port的，因此Port Path Cost的设置关系到本设备Root Port。它的缺省值是按Interface的链路速率（The Media Speed）自动计算的，速率高的花费小，如果管理员没有特别需要可不必更改它，因为这样算出的Path Cost最科学。您可以在一个端口上针对不同的Instance分配不
  同的路径花费，各个Instance可根据这些值运行独立的生成树协议。

+ 当该端口Path Cost为缺省值时，设备会自动根据端口速率计算出该端口的Path Cost。但IEEE 802.1d- 1998 和IEEE 802.1t对相同的链路速率规定了不同Path Cost值，802.1d- 1998 的取值范围是短整型（short）（ 1 — 65535 ），802.1t的取值范围是长整型（long）(1—200,000,000)。其中对于AP的Cost值有两个方案：我司的私有方案固定为物理口的Cost值*95%；标准推荐的方案为20,000,000,000/(AP的实际链路带宽)，其中AP的实际链路带宽为成员口的带宽*UP成员口个数。请管理员一定要统一好整个网络内Path Cost的标准。缺省模式为私有长整型模式。

+ 下表列出两种方法对不同链路速率自动设置的Path Cost。

+ <table>     <tr>         <th>端口速率</th>         <th>Interface</th>         <th>IEEE 802.1d (short)</th>         <th>IEEE 802.1t (long)</th>         <th>IEEE 802.1t (long standard)</th>     </tr>     <tr>         <td>10M</td>         <td>普通端口</td>         <td>100</td>         <td>2000000</td>         <td>2000000</td>     </tr>     <tr>         <td></td>         <td>Aggregate Link</td>         <td>95</td>         <td>1900000</td>         <td>2000000 / linkupcnt</td>     </tr>     <tr>         <td>100M</td>         <td>普通端口</td>         <td>19</td>         <td>2000000</td>         <td>2000000</td>     </tr>     <tr>         <td></td>         <td>Aggregate Link</td>         <td>18</td>         <td>1900000</td>         <td>2000000 / linkupcnt</td>     </tr>     <tr>         <td>1000M</td>         <td>普通端口</td>         <td>4</td>         <td>2000000</td>         <td>2000000</td>     </tr>     <tr>         <td></td>         <td>Aggregate Link</td>         <td>3</td>         <td>1900000</td>         <td>2000000 / linkupcnt</td>     </tr>     <tr>         <td>10000M</td>         <td>普通端口</td>         <td>2</td>         <td>2000000</td>         <td>2000000</td>     </tr>     <tr>         <td></td>         <td>Aggregate Link</td>         <td>1</td>         <td>1900000</td>         <td>2000000 / linkupcnt</td>     </tr> </table>



+ 默认采用我司的私有长整型模式。修改成标准推荐方案的path cost方案后，AP的cost会随着UP成员口数量的变化而变化，而端口cost值变化会导致网络拓扑发生变化。
+ AP为静态AP时，表格中的linkupcnt为UP成员口个数；AP为LACP AP时，表格中的linkupcnt为参与AP数据转发的成员口个数；当AP内没有任何成员口linkup时，linkupcnt为 1 。具体AP和LACP的配置，请参见AP章节的说明。

##### 配置方法

######  配置端口的路径花费

+ 可选配置

+ 在管理员需要数据报文优先走哪个端口或哪条路径时配置。

【命令格式】 spanning-tree [ mst instance-id ] cost cost
【参数说明】 mst instance-id：Instance号，范围为 0 － 64
cost cost：路径花费值，范围为 1 － 200 ， 000 ， 000
【缺省配置】 Instance-ID的缺省值为 0
缺省值为根据Interface的链路速率自动计算。
1000 Mbps— 20000
100 Mbps— 200000
10 Mbps— 2000000
【命令模式】 接口配置模式
【使用指导】 cost值越大表明路径花费越高。

######  配置 Path Cost 的缺省计算方法

+ 可选配置

+ 在管理员需要修改路径花费计算方式时配置。

【命令格式】 spanning-tree pathcost method { long [ standard ] | short }
【参数说明】 long：采用802.1t标准设定path-cost的值。
standard：standard 表示按照标准推荐的公式计算cost值。
short：采用802.1d标准设定path-cost的值。
【缺省配置】 缺省采用802.1T标准设定Path-cost的值
【命令模式】 全局配置模式
【使用指导】 当该端口Path Cost为缺省值时，设备会自动根据端口速率计算出该端口的Path Cost。

##### 检验方法

+ 显示验证。

+ 使用show spanning-tree [ mst instance-id ] interface interface-id命令查看生成树接口的配置信息。

##### 配置举例

######  配置端口的路径花费



【配置方法】  

+ 配置网桥优先级，使DEV A为生成树根桥。 
+ 配置DEV B的端口gi 0/2的端口路径花费为 1 ，使端口gi 0/2选举为根端口。

```
DEV A
Ruijie(config)#spanning-tree
Ruijie(config)#spanning-tree mst 0 priority 0
DEV B 
Ruijie(config)#spanning-tree
Ruijie(config)# int gi 0/2
Ruijie(config-if-GigabitEthernet 0/2)# spanning-tree cost 1
```

【检验方法】 

+ 通过show spanning-tree summary查看生成树拓扑计算结果。

```
DEV A
Ruijie# Ruijie#show spanning-tree summary
Spanning tree enabled protocol mstp
MST 0 vlans map : ALL
Root ID Priority 0
Address 00d0.f822.3344
this bridge is root
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Bridge ID Priority 0
Address 00d0.f822.3344
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/2 Desg FWD 20000 128 False P2p
Gi0/1 Desg FWD 2000 128 False P2p
```

```
DEV B 
Ruijie#show spanning-tree summary
Spanning tree enabled protocol mstp
MST 0 vlans map : ALL
Root ID Priority 0
Address 00d0.f822.3344
this bridge is root
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Bridge ID Priority 32768
Address 001a.a917.78cc
Hello Time 2 sec Forward Delay 15 sec Max Age 20 sec
Interface Role Sts Cost Prio OperEdge Type
---------------- ---- --- ---------- -------- -------- ----------------
Gi0/ 2 Root FWD 1 128 False P2p
Gi0/ 1 Altn BLK 20000 128 False P2p
```



##### 常见错误

+ 修改端口路径花费，只有在接收端口配置才起作用。

#### 10.4.7 配置 BPDU 帧的最大跳数

##### 配置效果

+ 配置BPDU帧的最大跳数（Maximum-Hop Count），会影响BPDU的生命期，从而影响网络拓扑

##### 注意事项

+ BPDU帧最大跳数的缺省值是 20 ，一般不需要进行修改。

##### 配置方法

######  配置 Maximum-Hop Count

+ 可选配置。如果网络拓扑规模较大，使得BPDU帧的传递超过了默认的 20 跳，则建议更改max-hops配置。

【命令格式】 spanning-tree max-hops hop-count
【参数说明】 hop-count：BPDU在被丢弃之前可以经过设备的次数，范围为 1 － 40
【缺省配置】 hop-count的缺省值为 20
【命令模式】 全局配置模式
【使用指导】 在Region内，Root Bridge发送的BPDU包含一个Hot Count项，从Root Bridge开始，每经过一个设备，Hop Count就会减 1 ，直到为 0 则表示该BPDU信息超时，设备收到Hops值为 0 的BPDU就要丢弃它。此命令指定了BPDU在一个Region内经过多少台设备后被丢弃。改变max-hops将影响到所有Instance。

##### 检验方法

+ 显示验证。

+ 使用show spanning-tree max-hops查看max-hops配置信息。

##### 配置举例

######  设置 BPDU 帧的最大跳数

【配置方法】  

+ 配置BPDU帧的最大跳数为 25 。

```
Ruijie(config)# spanning-tree max-hops 25
```

【检验方法】 

+ 通过show spanning-tree命令查看配置。

```
Ruijie# show spanning-tree
StpVersion : MSTP
SysStpStatus : ENABLED
MaxAge : 20
HelloTime : 2
ForwardDelay : 15
BridgeMaxAge : 20
BridgeHelloTime : 2
BridgeForwardDelay : 15
MaxHops: 25
TxHoldCount : 3
PathCostMethod : Long
BPDUGuard : Disabled
BPDUFilter : Disabled
LoopGuardDef : Disabled
###### mst 0 vlans map : ALL
BridgeAddr : 00d0.f822.3344
Priority: 0
TimeSinceTopologyChange : 2d:0h:46m:4s
TopologyChanges : 25
DesignatedRoot : 0.001a.a917.78cc
RootCost : 0
RootPort : GigabitEthernet 0/1
CistRegionRoot : 0.001a.a917.78cc
CistPathCost : 20000
```

##### 常见错误

无

#### 10.4.8 配置接口 port fast 的相关特性

##### 配置效果

+ 打开Port Fast后该端口会直接Forwarding。但会因为收到BPDU而使Port Fast Operational State为disabled，从而正常的参与STP算法而Forwarding。

+ 端口打开BPDU Guard后，如果在该端口上收到BPDU，则会进入Error-disabled 状态。

+ 打开BPDU Filter后，相应端口会既不发，也不收BPDU。

##### 注意事项

+ 打开某接口的port fast，全局的BPDU guard配置才生效。

+ 打开全局的BPDU Filter enabled状态下，Port Fast enabled的Interface将既不收BPDU，也不发BPDU，这样，直连Port Fast enabled端口的主机就收不到BPDU。而如果Port Fast enabled的Interface因收到BPDU而使Port Fast Operational 状态disabled，BPDU Filter也就自动失效。

+ 打开某接口的port fast，全局的BPDU filter配置才生效。

##### 配置方法


配置指南 MSTP

######  配置 port fast

+ 可选配置

+ 如果设备的端口直连着网络终端，那么就可以设置该端口为Port Fast。

+ 在全局配置模式下，使用spanning-tree portfast default命令可以打开所有接口的Portfast开关；使用no spanning-tree portfast default命令关闭所有接口的portfast开关。

+ 在接口配置模式下使用spanning-tree portfast命令可以打开某个接口的Portfast开关；使用spanning-tree portfast disabled命令关闭某个接口的portfast开关。

【命令格式】 spanning-tree portfast default^
【参数说明】 -
【缺省配置】 缺省关闭所有接口的Portfast开关
【命令模式】 全局配置模式
【使用指导】 -

【命令格式】 spanning-tree portfast^
【参数说明】 -
【缺省配置】 接口上的Port Fast开关是关闭的
【命令模式】 接口配置模式
【使用指导】 打开Port Fast后该端口会直接Forwarding。但会因为收到BPDU而使Port Fast Operational State为disabled，
从而正常的参与STP算法而Forwarding。

######  打开 BPDU Guard

+ 可选配置

+ 如果设备的端口直连着网络终端，为了防止受到BPDU攻击导致生成树拓扑发生异常，可以在这些端口上配置BPDU Guard功能。开启BPDU Guard的端口收到BPDU，端口会进入Error-disabled 状态。

+ 如果设备的端口直连着网络终端，为了防止端口下连出现环路，也可以配置BPDU Guard功能防止环路。该应用依赖下连设备（比如HUB）能够转发BPDU帧。

+ 在全局配置模式下，使用spanning-tree portfast bpduguard default命令可以打开所有接口的BPDU guard开关；使用no spanning-tree portfast bpduguard default命令关闭所有接口的BPDU guard开关。

+ 在接口配置模式下使用spanning-tree bpduguard enabled命令可以打开某个接口的BPDU guard 开关；使用spanning-tree bpduguard disabled命令关闭某个接口的BPDU guard开关。

【命令格式】 spanning-tree portfast bpduguard default
【参数说明】 -
【缺省配置】 缺省关闭全局BPDU Guard
【命令模式】 全局配置模式
【使用指导】 打开BPDU guard，如果在该端口上收到BPDU，则会进入error-disabled 状态。使用show spanning-tree 命令查看设置。

【命令格式】 spanning-tree bpduguard enabled
【参数说明】 -
【缺省配置】 接口上的BPDU guard开关是关闭的
【命令模式】 接口配置模式
【使用指导】 打开单个接口的BPDU Guard的情况下，如果该接口收到了BPDU，就进入Error-disabled 状态。

######  打开 BPDU Filter

+ 可选配置

+ 为了防止异常的BPDU报文对生成树拓扑的影响，可以在端口配置BPDU Filter功能过滤掉这些异常的BPDU。

+ 在全局配置模式下，使用spanning-tree portfast bpdufilter default命令可以打开所有接口的BPDU Filter开关；使用no spanning-tree portfast bpdufilter default命令关闭所有接口的BPDU Filter开关。

+ 在接口配置模式下使用spanning-tree bpdufilter enabled命令可以打开某个接口的 BPDU Filter 开关；使用spanning-tree bpdufilter disabled命令关闭某个接口的BPDU Filter开关。

【命令格式】 spanning-tree portfast bpdufilter default
【参数说明】 -
【缺省配置】 缺省是关闭的
【命令模式】 全局配置模式
【使用指导】 打开BPDU Filter后，相应端口会既不发也不收BPDU。

【命令格式】 spanning-tree bpdufilter enabled
【参数说明】 -^
【缺省配置】 缺省是关闭的
【命令模式】 接口配置模式
【使用指导】 打开BPDU Filter后，相应端口会既不发BPDU，也不收BPDU。

##### 检验方法

+ 显示验证。

+ 使用show spanning-tree [ mst instance-id ] interface interface-id命令查看生成树接口的配置信息。

##### 配置举例

######  配置端口的 Port Fast 特性

【配置方法】 

+ 配置DEV C的端口gi 0/3为Port Fast端口，同时开启BPDU Guard功能。

```
DEV C Ruijie(config)#^ int gi 0/3^
Ruijie(config-if-GigabitEthernet 0/3)# spanning-tree portfast
%Warning: portfast should only be enabled on ports connected to a singlehost. Connecting hubs, switches, bridges to this interface when portfast isenabled,can cause temporary loops.
Ruijie(config-if-GigabitEthernet 0/3)#spanning-tree bpduguard enable
DEV C Ruijie#show spanning-tree int gi 0/3^
PortAdminPortFast : Enabled
PortOperPortFast : Enabled
PortAdminAutoEdge : Enabled
PortOperAutoEdge : Enabled
PortAdminLinkType : auto
PortOperLinkType : point-to-point
PortBPDUGuard : Enabled
PortBPDUFilter : Disabled
PortGuardmode : None
```

##### 常见错误

无

#### 10.4.9 配置 TC 相关的特性

##### 配置效果

+ 打开TC Protection功能时，收到TC-BPDU报文后的一定时间内（一般为 4 秒），只进行一次删除操作。这样可以避免频繁的删除MAC地址表项和ARP表项。

+ 打开TC Guard后，当一个端口收到TC报文的时候，该端口将屏蔽掉该端口接收或者是自己产生的TC报文，使得TC
  报文不会扩散到其它端口，这样能有效控制网络中可能存在的TC攻击，保持网络的稳定。

+ TC过滤是指对于端口收到的TC报文不处理，而正常的拓扑变化的情况，能够处理。

##### 注意事项

+ 建议在确认网络当中有非法的tc报文攻击的情况下再打开TC Guard功能。

##### 配置方法

######  打开 TC Protection 功能

+ 可选配置

+ 缺省是关闭的。

+ 在全局配置模式下，使用spanning-tree tc-protection 命令可以打开所有接口的Tc-protection开关；使用no spanning-tree tc-protection命令关闭所有接口的Tc-protection开关。

+ Tc-protection只能全局的打开和关闭。

【命令格式】 spanning-tree tc-protection
【参数说明】 -
【缺省配置】 缺省关闭tc-protection开关
【命令模式】 全局配置模式
【使用指导】 -

######  打开 TC Guard 功能

+ 可选配置

+ 缺省是关闭的。

+ 需要过滤掉端口收到的TC报文或端口因拓扑变化自己产生的TC报文时，可以配置端口的TC Guard功能。

+ 在全局配置模式下，使用spanning-tree tc-protection tc-guard命令可以打开所有接口的tc guard开关；使用no spanning-tree tc-protection tc-guard命令关闭所有接口的tc guard开关。

+ 在接口配置模式下使用spanning-tree tc-guard命令可以打开某个接口的tc guard开关；使用no spanning-tree
  tc-guard命令关闭某个接口的tc guard开关。

【命令格式】 spanning-tree tc-protection tc-guard
【参数说明】 -
【缺省配置】 缺省关闭全局tc-guard开关
【命令模式】 全局配置模式
【使用指导】 启用tc-guard功能，能防止tc报文的扩散。

【命令格式】 spanning-tree tc-guard
【参数说明】 -
【缺省配置】 缺省关闭tc-guard开关
【命令模式】 接口配置模式
【使用指导】 启用tc-guard功能，能防止tc报文的扩散。

######  打开 TC 过滤功能

+ 可选配置

+ 缺省是关闭的。

+ 只需要过滤掉端口收到的TC报文时，可以配置端口的TC过滤功能。

+ 在接口配置模式下使用spanning-tree ignore tc命令打开某个接口的TC过滤功能；使用no spanning-tree ignore tc命
  令关闭某个接口的TC过滤功能。

【命令格式】 spanning-tree ignore tc^
【参数说明】 -
【缺省配置】 (^) 缺省关闭TC过滤功能
【命令模式】 (^) 接口配置模式
【使用指导】 启用tc过滤功能，则端口收到的TC报文将不处理。

##### 检验方法

+ 显示验证。

##### 配置举例

######  配置端口的 TC Guard 功能

【配置方法】 配置端口的TC Guard功能

```
Ruijie(config)#int gi 0/1
Ruijie(config-if-GigabitEthernet 0/1)#spanning-tree tc-guard
```

【检验方法】 

 通过show run interface命令查看端口的TC Guard配置。

```
Ruijie#show run int gi 0/1
Building configuration...
Current configuration : 134 bytes
interface GigabitEthernet 0/1
switchport mode trunk
spanning-tree tc-guard
```

##### 常见错误

+ 错误地配置TC Guard或TC过滤功能，可能会导致网络设备报文转发出错。比如在拓扑发生变化的情况下，没有及时清除MAC地址导致报文转发出错。

#### 10.4.10 配置 BPDU 源 MAC 检查

##### 配置效果

+ 打开BPDU源MAC检查开关，将只接受源MAC地址为指定MAC的BPDU帧，过滤掉其它所有接收的BPDU帧。

##### 注意事项

+ 当确定了某端口点对点链路对端相连的交换机时，可以配置BPDU源MAC检查来达到只接收对端交换机发送的BPDU
  帧。

##### 配置方法

######  打开 BPDU 源 MAC 检查

+ 可选配置

+ 为了防止恶意的BPDU攻击，可以配置BPDU源MAC检查功能。

+ 在接口配置模式下使用bpdu src-mac-check H.H.H命令打开某个接口的BPDU源MAC检查功能；使用no bpdu src-mac-check命令关闭某个接口的BPDU源MAC检查功能。

【命令格式】 bpdu src-mac-check H.H.H
【参数说明】 H.H.H：表示只接收源mac地址为该地址的bpdu帧。
【缺省配置】 缺省是关闭的
【命令模式】 接口模式
【使用指导】 使用BPDU源MAC检查是为了防止通过人为发送BPDU报文来恶意攻击交换机而使MSTP工作不正常。当确定了某端口点对点链路对端相连的交换机时，可通过配置BPDU源MAC检查来达到只接收对端交换机发送
的BPDU帧，丢弃所有其他BPDU帧，从而达到防止恶意攻击。可以在interface模式下来为特定的端口配置相应的BPDU源MAC检查MAC地址，且一个端口只允许配置一个过滤MAC地址。

##### 检验方法

 显示验证。

##### 配置举例

######  配置端口的 BPDU 源 MAC 检查功能

【配置方法】 配置端口的BPDU源MAC检查

```
Ruijie(config)#int gi 0/1
Ruijie(config-if-GigabitEthernet 0/1)#bpdu src-mac-check 00d0.f800.1234
```

【检验方法】 

+ 通过show run interface命令查看端口的Spanning Tree配置。

```
Ruijie#show run int gi 0/1
Building configuration...
Current configuration : 170 bytes
interface GigabitEthernet 0/1
switchport mode trunk
bpdu src-mac-check 00d0.f800.1234
spanning-tree link-type point-to-point
```

##### 常见错误

+ 配置BPDU源MAC检查，是只接收以配置的MAC为源MAC的BPDU帧，而丢弃其它所有BPDU帧。

#### 10.4.11 配置边缘口的自动识别

##### 配置效果

+ 打开边缘口自动识别功能时，如果在一定的时间范围内(为 3 秒)，指派口没有收到BPDU,则自动识别为边缘口。但会因为收到BPDU而使Port Fast Operational State为disabled。

##### 注意事项

+ 一般情况下不需要关闭边缘口自动识别功能。

##### 配置方法

######  打开边缘口的自动识别

+ 可选配置

+ 缺省是打开的。

+ 在接口配置模式下使用spanning-tree autoedge命令打开某个接口的边缘口自动识别功能；使用spanning-tree autoedge disabled命令关闭某个接口的边缘口自动识别功能。

【命令格式】 spanning-tree autoedge
【参数说明】 -
【缺省配置】 接口上的边缘口自动识别功能是打开的
【命令模式】 接口模式
【使用指导】 指派口在一定的时间范围内(为 3 秒)，如果收不到下游端口发送的BPDU，则认为该端口相连的是一台网络设备，从而设置该端口为边缘端口，直接进入Forwarding状态。自动标识为边缘口的端口因收到BPDU而自动识别为非边缘口。可以通过spanning-tree autoedge disabled命令取消边缘口的自动识别功能。

##### 检验方法

+ 显示验证。

##### 配置举例

######  关闭端口的 Auto Edge 功能

【配置方法】 关闭端口的Auto Edge功能

```
Ruijie(config)#int gi 0/1
Ruijie(config-if-GigabitEthernet 0/1)#spanning-tree autoedge disabled
```

【检验方法】 通过show spanning-tree interface命令查看端口的Spanning Tree配置。

```
Ruijie#show spanning-tree interface gi 0/1
PortAdminPortFast : Disabled
PortOperPortFast : Disabled
PortAdminAutoEdge : Disabled
PortOperAutoEdge : Disabled
PortAdminLinkType : point-to-point
PortOperLinkType : point-to-point
PortBPDUGuard : Disabled
PortBPDUFilter : Disabled
PortGuardmode : None
```

```
###### MST 0 vlans mapped :ALL
PortState : forwarding
PortPriority : 128
PortDesignatedRoot : 0.00d0.f822.3344
PortDesignatedCost : 0
PortDesignatedBridge :0.00d0.f822.3344
PortDesignatedPortPriority : 128
PortDesignatedPort : 2
PortForwardTransitions : 6
PortAdminPathCost : 20000
PortOperPathCost : 20000
Inconsistent states : normal
PortRole : designatedPort
```

**常见错误**

+ 边缘端口的自动识别功能，默认指派口 3 秒内未接收到BPDU就将端口识别成边缘端口并立即Forward。如果网络环境存在丢包或收发报文延迟现象，建议将端口的自动识别功能关闭。

#### 10.4.12 配置接口保护相关的特性

##### 配置效果

+ 接口打开Root Guard功能时，强制其在所有实例上的端口角色为指定端口，一旦该端口收到优先级更高的配置信息时，Root Guard功能会将该接口置为root-inconsistent (blocked)状态,在足够长的时间内没有收到更优的配置信息时，端口会恢复成原来的正常状态。

+ 由于单向链路的故障，根口或备份口由于收不到BPDU会变成指派口进入转发状态，从而导致了网络中环路的产生，LOOPGuard功能防止了这种情况的发生。

##### 注意事项

+ 端口的ROOT Guard和LOOP Guard同一时刻只能有一个生效。

##### 配置方法

######  打开 ROOT Guard 特性

+ 可选配置。

+ 为了防止因维护人员的错误配置或网络中的恶意攻击，根桥可能收到优先级更高的配置信息，从而失去当前根桥的位置，引起网络拓扑的错误的变动，可以在设备的指派端口上配置ROOT Guard功能。

+ 在接口配置模式下使用spanning-tree guard root命令打开某个接口的Root Guard功能；使用no spanning-tree guard root命令关闭某个接口的Root Guard功能。

【命令格式】 spanning-tree guard root
【参数说明】 -
【缺省配置】 缺省关闭root guard功能
【命令模式】 接口配置模式
【使用指导】 启用root guard功能，能防止因错误配置或非法报文的攻击导致当前根桥地位的变化。

######  打开 LOOP Guard 特性

+ 可选配置。

+ 为了防止接收端口（根端口、Master端口或Alternate端口）因接收不到指派网桥发送的BPDU而使网络拓扑发生变化，从而引起可能的环路，可以在上述接收端口上配置LOOP Guard功能，提高设备的稳定性。

+ 在全局配置模式下，使用spanning-tree loopguard default命令打开所有接口的Loop Guard功能；使用no spanning-tree loopguard default命令关闭所有接口的Loop Guard功能。

+ 在接口配置模式下使用spanning-tree guard loop命令打开某个接口的Loop Guard功能；使用no spanning-tree guard loop命令关闭某个接口的Loop Guard功能。

【命令格式】 spanning-tree loopguard default
【参数说明】 -
【缺省配置】 缺省关闭loop guard功能
【命令模式】 全局配置模式
【使用指导】 启用loop guard功能，能防止根端口或备份口因收不到bpdu而产生的可能的环路。

【命令格式】 spanning-tree guard loop
【参数说明】 -
【缺省配置】 缺省关闭loop guard功能
【命令模式】 接口配置模式
【使用指导】 启用loop guard功能，能防止根端口或备份口因收不到bpdu而产生的可能的环路。

######  关闭 Guard 特性

+ 可选配置。

【命令格式】 spanning-tree guard none
【参数说明】 -
【缺省配置】 缺省关闭guard功能
【命令模式】 接口配置模式
【使用指导】 缺省是关闭guard功能。

##### 检验方法

+ 显示验证。

##### 配置举例

######  配置端口的 Loop Guard 特性

【配置方法】  

+ 配置DEV A为生成树根桥，DEV B为非根桥。
+ 配置DEV B的端口gi 0/1和gi 0/2的LOOP Guard特性。

```
DEV A Ruijie(config)#spanning-tree
Ruijie(config)#spanning-tree mst 0 priority 0
```

```
DEV B Ruijie(config)#spanning-tree
Ruijie(config)# int range gi 0/1- 2
Ruijie(config-if-range)#spanning-tree guard loop
```

【检验方法】  通过show spanning-tree interface命令查看端口的Spanning Tree配置。

```
DEV A 略
DEV B Ruijie#show spanning-tree int gi 0/1
PortAdminPortFast : Disabled
PortOperPortFast : Disabled
PortAdminAutoEdge : Enabled
PortOperAutoEdge : Disabled
PortAdminLinkType : auto
PortOperLinkType : point-to-point
PortBPDUGuard : Disabled
PortBPDUFilter : Disabled
PortGuardmode : Guard loop
###### MST 0 vlans mapped :ALL
PortState : forwarding
PortPriority : 128
PortDesignatedRoot : 0.001a.a917.78cc
PortDesignatedCost : 0
PortDesignatedBridge :0.001a.a917.78cc
PortDesignatedPortPriority : 128
PortDesignatedPort : 17
PortForwardTransitions : 1
PortAdminPathCost : 20000
PortOperPathCost : 20000
Inconsistent states : normal
PortRole : rootPort
Ruijie#show spanning-tree int gi 0/2
PortAdminPortFast : Disabled
PortOperPortFast : Disabled
PortAdminAutoEdge : Enabled
PortOperAutoEdge : Disabled
PortAdminLinkType : auto
PortOperLinkType : point-to-point
PortBPDUGuard : Disabled
PortBPDUFilter : Disabled
PortGuardmode : Guard loop
###### MST 0 vlans mapped :ALL
PortState : discarding
PortPriority : 128
PortDesignatedRoot : 0.001a.a917.78cc
PortDesignatedCost : 0
PortDesignatedBridge :0.001a.a917.78cc
PortDesignatedPortPriority : 128
PortDesignatedPort : 18
PortForwardTransitions : 1
PortAdminPathCost : 20000
PortOperPathCost : 20000
Inconsistent states : normal
PortRole : alternatePort
```



##### 常见错误

+ 将ROOT Guard功能配置在根端口、Master端口或Alternate端口，可能会错误地将端口BLOCK。

#### 10.4.13 配置 BPDU 透传功能

##### 配置效果

+ 设备未开启STP协议时，需要透传BPDU帧，使得与之互连的设备之间的生成树计算正常。

##### 注意事项

+ BPDU透传功能只在STP协议关闭时才启作用。当STP协议打开时，设备不透传BPDU帧。

##### 配置方法

######  配置 BPDU 透传功能

+ 可选配置

+ 设备未开启STP协议时，如里需要透传BPDU帧，则需要配置BPDU透传功能。

+ 在全局配置模式下，使用bridge-frame forwarding protocol bpdu命令打开BPDU透传功能；使用no bridge-frame forwarding protocol bpdu命令关闭BPDU透传。

+ BPDU透传功能只在STP协议关闭时才启作用。当STP协议打开时，设备不透传BPDU帧。

【命令格式】 bridge-frame forwarding protocol bpdu
【参数说明】 -
【缺省配置】 缺省是关闭的
【命令模式】 全局配置模式
【使用指导】 在IEEE 802.1Q标准中，BPDU的目的MAC地址 01 - 80 - C2- 00 - 00 - 00 是作为保留地址使用的，即遵循IEEE
802.1Q标准的设备，对于接收到的BPDU帧是不转发的。然而，在实际的网络布署中，可能需要设备能够支持透传BPDU帧。例如，设备未开启STP协议时，需要透传BPDU帧，使得与之互连的设备之间的生成树计算正常。
BPDU透传功能只在STP协议关闭时才启作用。当STP协议打开时，设备不透传BPDU帧。

##### 检验方法

+ 显示验证。

##### 配置举例

######  配置 BPDU 透传功能

 DEVA，C上开启生成树协议，DEV B未开启生成树协议。
【配置方法】  DEV B上配置BPDU透传功能，使得DEV A，C之间的STP协议能够正确计算。

```
DEV B Ruijie(config)#bridge-frame forwarding protocol bpdu
```

【检验方法】  通过show run查看BPDU透传功能是否开启。

```
DEV B Ruijie#show run
Building configuration...
Current configuration : 694 bytes
bridge-frame forwarding protocol bpdu
```



##### 常见错误

无

#### 10.4.14 配置 BPDU TUNNEL

##### 配置效果

+ 配置BPDU TUNNEL功能，使用户网络的STP协议报文能够通过运营商网络进行隧道透传，用户网络之间的STP协议报文的传输对运营商网络不会产生影响，从而使得用户网络和运营商网络的STP协议分开计算，互不干扰。

##### 注意事项

+ 需要全局和接口同时开启BPDU TUNNEL功能后，BPDU TUNNEL功能才生效。

##### 配置方法

######  配置 BPDU 透传功能

+ 可选配置。在QINQ网络中，如果需要用户网络和运营商网络的STP协议分开计算，互不干扰，可以通过配置BPDUTUNNEL达到效果。

+ 缺省情况下，BPDU TUNNEL功能是关闭的。

+ 在全局配置模式下，使用l2protocol-tunnel stp命令使能全局的BPDU TUNNEL功能；使用no l2protocol-tunnel stp命令关闭全局的BPDU TUNNEL功能。

+ 在接口模式下，使用l2protocol-tunnel stp enable命令使能接口的BPDU TUNNEL功能；使用no l2protocol-tunnel stp enable命令关闭接口的BPDU TUNNEL功能。

+ 在全局模式下通过命令l2protocol-tunnel stp tunnel-dmac mac-address配置BPDU TUNNEL的透传地址。

+ BPDU TUNNEL功能只在全局和接口同时使能的情况下才启作用。

【命令格式】 l2protocol-tunnel stp
【参数说明】 -
【缺省配置】 缺省是关闭的
【命令模式】 全局配置模式
【使用指导】 BPDU TUNNEL功能只在全局和接口同时使能的情况下才启作用。

【命令格式】 l2protocol-tunnel stp enable
【参数说明】 -
【缺省配置】 缺省是关闭的
【命令模式】 接口配置模式
【使用指导】 BPDU TUNNEL功能只在全局和接口同时使能的情况下才启作用。

【命令格式】 l2protocol-tunnel stp tunnel-dmac mac-address
【参数说明】 mac-address：需要透传的STP协议地址
【缺省配置】 缺省为01d0.f800.0005
【命令模式】 全局配置模式
【使用指导】 BPDU TUNNEL应用中，当用户网络的STP协议报文进入运营商网络的边缘设备后，将目的mac地址改成
私有地址在运营商网络中转发，到了另外一端边缘设备后，再将目的mac地址改成公有地址回到另一端用户
网络，以达到STP协议报文在运营商网络透传的效果。这个私有地址，即为BPDU TUNNEL的透传地址。

STP报文可选透传地址范围：01d0.f800.0005 、011a.a900.0005 、010 f.e200.0003 、0100.0ccd.cdd0、0100. 0ccd.cdd1、 0100. 0ccd.cdd2。
当未配置透传地址时，BPDU TUNNEL缺省使用的地址为01d0.f800.0005。

##### 检验方法

+ 通过show l2protocol-tunnel stp命令查看BPDU TUNNEL配置。

##### 配置举例

以下配置举例，仅介绍与MSTP和QINQ相关的配置。

######  配置 BPDU TUNNEL 功能


【配置方法】 

+ 在运营商网络边缘设备（本例为Provider S1/Provider S2上开启基本QinQ功能，使用户网络的数据报文在运营商网络的VLAN 200 中传输。
+ 在运营商网络边缘设备（本例为Provider S1/Provider S2上开启STP协议透传功能，使运营商网络可以通过BPDU TUNNEL对用户网络的STP报文进行隧道传输。

Provider S1  第一步，创建服务商VLAN 200

```
Ruijie#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)#vlan 200
Ruijie(config-vlan)#exit
```

第二步，在连接用户网络的接口上开启基本QinQ功能，使用VLAN 200对用户网络的数据进行隧道传输

```
Ruijie(config)#interface gigabitEthernet 0 /1
Ruijie(config-if-GigabitEthernet 0 /1)#switchport mode dot1q-tunnel
Ruijie(config-if-GigabitEthernet 0 /1)#switchport dot1q-tunnel native vlan 200
Ruijie(config-if-GigabitEthernet 0 /1)#switchport dot1q-tunnel allowed vlan add untagged 200
```

第三步，在连接用户网络的接口上开启STP协议透传功能

```
Ruijie(config-if-GigabitEthernet 0 /1)#l2protocol-tunnel stp enable
Ruijie(config-if-GigabitEthernet 0 /1)#exit
第四步，全局开启STP协议透传功能
Ruijie(config)#l2protocol-tunnel stp
```

第五步，配置uplink port

```
Ruijie(config)# interface gigabitEthernet 0 /5
Ruijie(config-if-GigabitEthernet 0 /5)#switchport mode uplink
```

Provider S2  Provider S2设备上的配置同Provider S1配置类似，请参考上文Provider S1的配置。此处不再重复说明。

【检验方法】 

+ 查看BPDU TUNNEL配置是否正确。
+ 查看Tunnel口的配置是否正确，关注点：接口类型是否为dot1q-tunnel，外层Tag VLAN是否为Native
  VLAN且其是否已加入接口的许可VLAN列表，运营商网络边缘设备上链口的类型是否为Uplink。

Provider S1 1 ：查看BPDU TUNNEL配置是否正确：

```
Ruijie#show l2protocol-tunnel stp
L2protocol-tunnel: stp Enable
L2protocol-tunnel destination mac address: 01d0.f800.0005
GigabitEthernet 0/1 l2protocol-tunnel stp enable
```

2 ：查看QINQ配置是否正确：

```
Ruijie#show running-config
interface GigabitEthernet 0 /1
switchport mode dot1q-tunnel
switchport dot1q-tunnel allowed vlan add untagged 200
switchport dot1q-tunnel native vlan 200
l2protocol-tunnel stp enable
spanning-tree bpdufilter enable
！
interface GigabitEthernet 0 /5
switchport mode uplink
```

Provider S2 同Provider S1

##### 常见错误

+ 运营商网络中，配置的BPDU TUNNEL透传地址要一致，才能正确透传BPDU帧。

### 10.5 监视与维护

##### 清除各类信息

在设备运行过程中执行clear命令，可能因为重要信息丢失而导致业务中断。

<table border="1">
  <tr>
    <th>作用</th>
    <th>命令</th>
  </tr>
  <tr>
    <td>清除端口的收发包统计信息</td>
    <td>clear spanning-tree counters [ interface interface-id ]</td>
  </tr>
  <tr>
    <td>清除 STP 的拓扑改变信息</td>
    <td>clear spanning-tree mst instance-id topochange record</td>
  </tr>
</table>




**查看运行情况**

<table border="1">
  <tr>
    <th>作用</th>
    <th>命令</th>
  </tr>
  <tr>
    <td>显示 MSTP 的各项参数信息及生成树的拓扑信息</td>
    <td>show spanning-tree</td>
  </tr>
  <tr>
    <td>显示 MSTP 的收发包统计信息</td>
    <td>show spanning-tree counters [ interface interface-id ]</td>
  </tr>
  <tr>
    <td>显示 MSTP 的各 instance 的信息及其端口转发状态信息</td>
    <td>show spanning-tree summary</td>
  </tr>
  <tr>
    <td>显示因根保护或环路保护而 block 的端口</td>
    <td>show spanning-tree inconsistentports</td>
  </tr>
  <tr>
    <td>显示 MST 域的配置信息</td>
    <td>show spanning-tree mst configuration</td>
  </tr>
  <tr>
    <td>显示该 instance 的 MSTP 信息</td>
    <td>show spanning-tree mst instance-id</td>
  </tr>
  <tr>
    <td>显示指定 interface 的对应 instance 的 MSTP 信息</td>
    <td>show spanning-tree mst instance-id interface interface-id</td>
  </tr>
  <tr>
    <td>显示指定实例中的接口的拓扑改变信息</td>
    <td>show spanning-tree mst instance-id topchange record</td>
  </tr>
  <tr>
    <td>显示指定 interface 的所有 instance 的 MSTP 信息</td>
    <td>show spanning-tree interface interface-id</td>
  </tr>
  <tr>
    <td>显示 forward-time</td>
    <td>show spanning-tree forward-time</td>
  </tr>
  <tr>
    <td>显示 Hello time</td>
    <td>show spanning-tree hello time</td>
  </tr>
  <tr>
    <td>显示 max-hops</td>
    <td>show spanning-tree max-hops</td>
  </tr>
  <tr>
    <td>显示 tx-hold-count</td>
    <td>show spanning-tree tx-hold-count</td>
  </tr>
  <tr>
    <td>显示 pathcost method</td>
    <td>show spanning-tree pathcost method</td>
  </tr>
  <tr>
    <td>显示 BPDU TUNNEL 信息</td>
    <td>show l2protocol-tunnel stp</td>
  </tr>
</table>





##### 查看调试信息

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>打开生成树所有的调试开关</td>         <td>debug mstp all</td>     </tr>     <tr>         <td>打开生成树 GR 的调试开关</td>         <td>debug mstp gr</td>     </tr>     <tr>         <td>打开接收 BPDU 报文的调试开关</td>         <td>debug mstp rx</td>     </tr>     <tr>         <td>打开发送 BPDU 报文的调试开关</td>         <td>debug mstp tx</td>     </tr>     <tr>         <td>打开生成树事件调试开关</td>         <td>debug mstp event</td>     </tr>     <tr>         <td>打开生成树 Loop Guard 特性调试开关</td>         <td>debug mstp loopguard</td>     </tr>     <tr>         <td>打开生成树 Root Guard 特性调试开关</td>         <td>debug mstp rootguard</td>     </tr>     <tr>         <td>打开 Bridge Detect 状态机调试开关</td>         <td>debug mstp bridgedetect</td>     </tr>     <tr>         <td>打开 Port Information 状态机调试开关</td>         <td>debug mstp portinfo</td>     </tr>     <tr>         <td>打开 Port Protocol Migration 状态机调试开关</td>         <td>debug mstp protomigrat</td>     </tr>     <tr>         <td>打开生成树拓扑变化的调试开关</td>         <td>debug mstp topochange</td>     </tr>     <tr>         <td>打开生成树接收状态机调试开关</td>         <td>debug mstp receive</td>     </tr>     <tr>         <td>打开 Port Role Transitions 状态机调试开关</td>         <td>debug mstp roletran</td>     </tr>     <tr>         <td>打开 Port State Transition 状态机调试开关</td>         <td>debug mstp statetran</td>     </tr>     <tr>         <td>打开生成树发送状态机调试开关</td>         <td>debug mstp transmit</td>     </tr> </table>

输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。








## 11 GVRP

### 11.1 概述

GVRP（GARP VLAN Registration Protocol , GARP VLAN 注册协议）是一种动态配置和扩散VLAN成员关系的GARP（Generic Attribute Registration Protocol，通用属性注册协议）应用。通过GVRP功能，可以简化VLAN配置管理，减少了用户手动配置VLAN和端口加入VLAN的工作，减少因配置不一致导致网络不通的问题的可能性。而且能动态维护VLAN的创建和端口加入/退出VLAN，保证拓扑内VLAN的连通性。

下文仅介绍GVRP的相关内容。

##### 协议规范

IEEE standard 802.1D

IEEE standard 802.1Q

### 11.2 典型应用

<table>     <thead>         <tr>             <th>典型应用</th>             <th>场景描述</th>         </tr>     </thead>     <tbody>         <tr>             <td>局域网内配置 GVRP</td>             <td>两台交换机局域网内相连，实现 vlan 的同步</td>         </tr>         <tr>             <td>GVRP PDUs TUNNEL 应用</td>             <td>在 QINQ 网络环境中，使用 GVRP PDUs TUNNEL 功能，实现 GVRP 协议报文的隧道透传。</td>         </tr>     </tbody> </table>

#### 11.2.1 局域网内配置 GVRP

##### 应用场景

通过启用 GVRP 功能，并配置GVRP 的注册模式为Normal 模式，来实现Device A 和Device F 之间所有动态和静态VLAN的注册和注销。

【注释】 Device A-F为交换机设备，设备之间相连的端口均为Trunk口。
Device A和Device F两台交换机配置需要用来通信的静态VLAN。
交换机Device A-F设备上均开启GVRP功能。

**功能部署**

+ 所有设备均开启GVRP功能，且使能动态创建vlan功能，确保中间设备都能创建动态VLAN。

+ 在交换机Device A和Device F配置需要用来通信的静态VLAN，交换机Device B-E设备上通过GVRP协议动态学习这些VLAN。

为防止用户拓扑产生环路，建议开STP（Spanning Tree Protocol，生成树协议）功能

#### 11.2.2 GVRP PDUs TUNNEL 应用

##### 应用场景

在QINQ网络中，通常分为用户网络和运营商网络。为了实现用户网络之间GVRP协议报文的传输而又不对运营商网络产生影响，可以使用GVRP PDUs TUNNEL功能，以达到用户网络和运营商网络的GVRP协议分开计算，互不干扰。

图 11 - 2 GVRP PDUs Tunnel应用拓扑图

【注释】 如上图所示，上部为运营商网络，下部为用户网络。其中，运营商网络包括边缘设备Provider S1和Provider S2。Customer Network A1和Customer Network A2为同一用户在不同地域的两个站点，Customer S1和Customer S2为用户网络到运营商网络的接入设备，分别通过Provider S1和Provider S2接入运营商网络。应用GVRP PDUs TUNNEL功能，可以满足处于不同地域的Customer Network A1和Customer Network A2可以跨越运营商网络进行统一GVRP计算，而不影响运营商网络的GVRP计算。

##### 功能部属

+ 在运营商边缘设备（本例为Provider S1/Provider S2上开启基本QinQ功能，实现用户网络的数据报文在运营商网络的指定VLAN内传输。

+ 在运营商边缘设备（本例为Provider S1/Provider S2上开启GVRP协议透传功能，使运营商网络可以通过GVRP PDUs TUNNEL对用户网络的GVRP报文进行隧道传输。

### 11.3 功能详解

##### 基本概念

######  GVRP

GVRP（GARP VLAN Registration Protocol，GARP VLAN 注册协议）就是GARP 的应用之一，用于注册和注销VLAN

属性。GVRP 协议实现VLAN 属性注册和注销的方式如下：

+ 当端口收到一个 VLAN 属性的声明时，该端口将注册该声明中所包含的VLAN 属性（即该端口加入到该VLAN 中）。

+  当端口收到一个 VLAN 属性的回收声明时，该端口将注销该声明中所包含的VLAN 属性（即该端口退出该VLAN）。

######  动态 VLAN

可以动态创建和删除，无需用户手动配置的VLAN称为动态VLAN。
可以通过手动配置，将VLAN从动态模式切换为静态模式，但无法从静态模式切换为动态模式。由GVRP协议功能创建的动态VLAN加入端口由协议状态机控制，即GVRP协议创建的动态VLAN仅能加入收到GVRP注册该VLAN的Trunk口，而不是所有的Trunk口，同样不能手动将端口加入动态VLAN。

######  消息类型

(1) Join 消息
当一个 GARP 应用实体希望其它GARP 实体注册自己的属性信息时，它会发送Join 消息；当收到来自其它实体的Join 消息或由于本实体静态配置了某些属性而需要其它实体进行注册时，它也会发送Join 消息。Join 消息又分为JoinEmpty 和JoinIn 两种，二者的区别如下：

+ JoinEmpty：用于声明一个本身没有注册的属性。

+ JoinIn：用于声明一个本身已经注册的属性。

(2) Leave 消息
当一个GARP 应用实体希望其它GARP 实体注销自己的属性信息时，它会发送Leave 消息；当收到来自其它实体的Leave 消息或由于本实体静态注销了某些属性而需要其它实体进行注销时，它也会发送Leave 消息。Leave 消息又分为LeaveEmpty 和LeaveIn 两种，二者的区别如下：

+ LeaveEmpty：用于注销一个本身没有注册的属性。

+ LeaveIn：用于注销一个本身已经注册的属性。

(3) LeaveAll 消息
每个 GARP 应用实体启动时都会启动各自的LeaveAll 定时器，当该定时器超时后，它就会发送LeaveAll 消息来注销所有的属性，从而使其它GARP 实体重新注册属性信息；当收到来自其它实体的LeaveAll 消息时，它也会发送LeaveAll 消息。在发送LeaveAll 消息同时重新启动LeaveAll定时器，开始新的一轮循环。

######  定时器类型

GARP 定义了四种定时器，用于控制各种GARP 消息的发送。
(1) Hold 定时器
Hold 定时器用来控制GARP 消息（包括Join 消息和Leave 消息）的发送。当GARP 应用实体的属性改变或收到来自其它实体的GARP 消息时，不会立即将该消息发送出去，而是在Hold 定时器超时后，将此时段内待发送的所有GARP 消息封装成尽可能少的报文发送出去，这样就减少了报文的发送数量，从而节省了带宽资源。
(2) Join 定时器
Join 定时器用来控制Join 消息的发送。为了保证Join 消息能够可靠地传输到其它实体，GARP应用实体在发出Join 消息后将等待一个Join 定时器的时间间隔：如果在该定时器超时前收到了其它实体发来的JoinIn 消息，它便不会重发该Join 消息；否则，它将重发一次该Join 消息。并非每个属性都有自己的 Join 定时器，而是每个GARP 应用实体共用一个。

(3) Leave 定时器
Leave 定时器用来控制属性的注销。当GARP 应用实体希望其它实体注销自己的某属性信息时会发送Leave 消息，收到该消息的实体将启动Leave 定时器，只有在该定时器超时前没有收到该属性信息的Join 消息，该属性信息才会被注销。
(4) LeaveAll 定时器
每个 GARP 应用实体启动时都会启动各自的LeaveAll 定时器，当该定时器超时后，GARP 应用实体就会对外发送LeaveAll 消息，从而使其它实体重新注册属性信息。随后再重新启动LeaveAll定时器，开始新一轮的循环。

######  GVRP 通告模式

GVRP通告模式指的是交换机设备告诉其它互连的设备自己有哪些VLAN，对端设备可能需要创建哪些VLAN并将收发GVRP报文的端口加入相关VLAN。
GVRP的通告模式有两种：

+ normal模式：对外通告本设备上的VLAN信息，包括动态和静态VLAN信息。

+ non- applicant模式：不对外通告本设备上的VLAN信息。

######  GVRP 注册模式

GVRP注册模式指的是交换机设备收到GVRP报文后，是否处理报文内的VLAN信息，如动态创建不存在的VLAN并将收报文的端口加入VLAN等。
GVRP的通告模式有两种：

+ normal模式：收到GVRP报文后，处理报文内的VLAN信息。

+ disabled模式：收到GVRP报文后，不处理报文内的VLAN信息。

**功能特性**

<table>     <thead>         <tr>             <th>功能特性</th>             <th>作用</th>         </tr>     </thead>     <tbody>         <tr>             <td>同步拓扑内 VLAN 信息</td>             <td>同步拓扑内 VLAN 信息，动态创建 VLAN 并将端口动态加入/退出 VLAN，减少用户手动配置工作和减少用户因配置遗漏导致 VLAN 内网络不通的概率。</td>         </tr>     </tbody> </table>

#### 11.3.1 同步拓扑内 vlan 信息

##### 工作原理

GVRP 是GARP 应用的一种，它基于GARP 的工作机制来维护设备中的VLAN 动态注册信息，并将该信息向其它设备传播：当设备启动了GVRP 之后，就能够接收来自其它设备的VLAN 注册信息，并动态更新本地的VLAN 注册信息；此外，设备还能够将本地的VLAN 注册信息向其它设备传播，从而使同一局域网内所有设备的VLAN 信息都达成一致。GVRP 传播的VLAN注册信息既包括本地手工配置的静态注册信息，也包括来自其它设备的动态注册信息。

######  对外通告 VLAN 信息

开启GVRP功能的设备上的Trunk口会定时收集Trunk口内的VLAN信息，告诉对端设备本Trunk口加入了哪些VLAN或者
退出哪些VLAN，通过将这些VLAN信息封装在GVRP报文内发送给对端设备，对端设备连接的Trunk口收到GVRP报文后


配置指南 GVRP

会解析VLAN信息，动态的创建VLAN并将端口加入VLAN或者将端口退出VLAN。具体会有哪些VLAN信息可以见上面将
的GVRP消息类型。

######  注册 / 注销 VLAN

交换机设备在收到GVRP报文后会根据端口的注册模式选择是否处理VLAN信息。具体行为见上面的GVRP注册模式解释。

#### 11.4 配置详解

<table>
  <thead>
    <tr>
      <th>配置项</th>
      <th colspan="2">配置建议 & 相关命令</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="9">配置GVRP基本功能，同步VLAN信息</td>
      <td colspan="2">必须配置。用于使能 GVRP 及允许动态创建 vlan 功能。</td>
    </tr>
    <tr>
      <td>gvrp enable </td>
      <td>启动 GVRP 功能。</td>
    </tr>
    <tr>
      <td>gvrp dynamic-vlan-creation enable </td>
      <td>启动允许动态创建 vlan 功能。</td>
    </tr>      
    <tr>
      <td>switchport mode trunk </td>
      <td>（端口模式下）切换端口模式为 trunk, trunk 模式下的端口 GVRP 功能才生效。</td>
    </tr>
    <tr>
      <td>switchport trunk allowed vlan all </td>
      <td>允许全部 vlan 通过。</td>
    </tr> 
    <tr>
      <td>gvrp applicant state </td>
      <td>设置端口的通告模式，normal 模式表示对外通告VLAN 信息，发送 GVRP 报文。否则不对外通告VLAN 信息。</td>
    </tr> 
    <tr>
      <td>gvrp registration mode </td>
      <td>设置端口的登记模式，normal 模式表示收到GVRP 报文后，会处理相关 VLAN 信息，如动态创建 VLAN，将端口加入 VLAN。否则不关心报
文内容。</td>
    </tr> 
    <tr>
      <td colspan="2">可选配置。用于设置定时器，端口的登记模式及通告模式。</td> 
    </tr>
    <tr>
      <td>gvrp timer</td>
      <td>设置定时器。</td>
    </tr>      
    <tr>
      <td rowspan="2">使能端口 Voice VLAN 功能</td>
      <td colspan="2">必选配置。 用于开启端口 Voice VLAN 功能。</td>
    </tr>
    <tr>
      <td>voice vlan enable </td>
      <td>使能端口的 Voice VLAN 功能。</td>
    </tr>
    <tr>
      <td rowspan="2">配置 Voice VLAN 老化时间</td>
      <td colspan="2">可选配置。 用于配置 Voice VLAN 老化时间。</td>
    </tr>
    <tr>
      <td>voice vlan aging </td>
      <td>配置 Voice VLAN 的老化时间，取值范围为 5-10000 分钟，缺省为 1440 分钟。</td>
    </tr>
    <tr>
      <td rowspan="2">配置 GVRP PDUs 透传功能</td>
      <td colspan="2">可选配置。用于配置 GVRP PDUs 透传功能。</td>
    </tr>
    <tr>
      <td>bridge-frame forwarding protocol gvrp </td>
      <td>打开 GVRP PDUs 透传功能。</td>
    </tr>   
    <tr>
      <td rowspan="4">配 置 GVRP PDUs TUNNEL</td>
      <td colspan="2">可选配置。用于配置 GVRP PDUs TUNNEL 功能。</td>
    </tr>
    <tr>
      <td>l2protocol-tunnel gvrp  </td>
      <td>全局使能 GVRP PDUs TUNNEL 功能。</td>
    </tr>    
    <tr>
      <td>l2protocol-tunnel gvrp enable  </td>
      <td>接口使能 GVRP PDUs TUNNEL 功能。</td>
    </tr> 
    <tr>
      <td>l2protocol-tunnel gvrp tunnel-dmac </td>
      <td>配置 GVRP PDUs TUNNEL 的透传地址。</td>
    </tr>              
  </tbody>
</table>

### 

#### 11.4.1 配置 GVRP 基本功能，同步 VLAN 信息

##### 配置效果

+ 可以动态创建/删除VLAN，并将端口动态加入/退出VLAN。

+ 设备之间同步各自的VLAN信息，拓扑内通信正常。

+ 减少用户手动配置工作，方便VLAN管理。

注意事项

+ 相互连接进行通信的两台设备都应启动GVRP，GVRP信息只在Trunk Links中传播，但传播的信息包括当前设备的所有VLAN信息，不管VLAN是动态学习的，或是手工设置的。

+ 在运行STP（Spanning-tree Protocol）的情况下，只有状态为Forwarding的端口才会参与GVRP的运行，如接收、发送GVRP PDU，只有状态为Forwarding的端口的VLAN信息会被GVRP扩散。

+ 所有由GVRP添加的VLAN Port都是Tagged Port。

+ 所有由GVRP动态学习的VLAN信息都未保存在系统中，当设备复位时，这些信息将全部丢失。用户也不可以保存这些动态学习到的VLAN信息。

+ 网络中所有需要交换GVRP信息的设备的GVRP Timers（Join，Leave，Leaveall）必须保持一致。

+ 在未运行STP（Spanning-tree Protocol , 生成树协议）的环境，所有可用端口都可以参与GVRP的运行。在运行SST（Single Spanning-tree , 单生成树）的环境中，只有在当前SST Context中处于Forwarding状态的端口才参与GVRP的运行。在运行MST（Multi Spanning-tree , 多生成树）的环境中，GVRP可在VLAN 1所属的Spanning-tree Context中运行，用户不能指定其它Spanning-tree Context。

##### 配置方法

######  使能 GVRP 功能

 必须配置。

 只有开启该功能，设备才能处理GVRP报文。

 打开则开启GVRP功能，对外发送含VLAN信息的GVRP报文；关闭则不对外发送含VLAN信息的GVRP报文，且不处
理GVRP报文。

【命令格式】 gvrp enable
【参数说明】 -
【缺省配置】 关闭GVRP
【命令模式】 全局模式
【使用指导】 只有在全局使能允许的情况下GVRP才会启动。在GVRP未全局使能的状态下，其它GVRP参数可以进行配置，
但只有在GVRP开始运行时，这些GVRP选项设置才能发生作用。

######  使能动态创建 VLAN 的功能

+ 必须配置。

+ 只有开启了该功能，设备在收到GVRP的join类型报文时，才会动态创建VLAN。

用户不能修改由GVRP创建的动态VLAN的参数。

【命令格式】 gvrp dynamic-vlan-creation enable
【参数说明】 -
【缺省配置】 禁止动态创建vlan
【命令模式】 全局模式
【使用指导】 当一个端口接收到的信息（仅限于Joinin Joinempty）中所指示的VLAN在本地设备不存在时，GVRP可能会创
建这个VLAN。是否允许动态创建VLAN由用户控制。

######  配置定时器

+ 可选配置。

+ GVRP功能有三个定时器，Join timer、Leave timer和Leaveall timer，用来控制各种类型报文的发送间隔。

+ 三个定时器之间的大小关系：Leave timer必须大于等于三倍的Join timer；Leaveall timer必须大于Leave timer。

+ 三个定时器由GVRP状态机控制，并且相互之间可以触发。

【命令格式】 gvrp timer { join timer-value | leave timer-value | leaveall timer-value }
【参数说明】 timer-value ： 1 - 2147483647 ms
【缺省配置】 join timer缺省值是200ms，leave timer缺省值是600ms，leaveall timer缺省值是10,000ms
【命令模式】 全局模式
【使用指导】 Leave timer时间必须大于或等于jointimer的 3 倍。
Leaveall timer的值必须比leave timer大。
时间单位为毫秒。
在实际组网中，建议用户将GVRP定时器配置为以下的推荐值：
Join Timer： 600 0ms（ 6 秒钟）；
Leave Timer： 3000 0ms（ 30 秒钟）；
LeaveAll Timer： 12000 0ms（ 2 分钟）。

要保证所有互联的GVRP设备中的GVRP Timer 设置保持一致，否则GVRP可能工作异常。

######  配置端口的通告模式

+ 可选配置。

+ GVRP的通告模式有normal和non- applicant两种，默认为normal模式。

+ Normal模式：表示对外通告本设备的VLAN信息。

+ Non- applicant模式：表示不对外通告本设备的VLAN信息。

【命令格式】 gvrp applicant state { normal | non-applicant }
【参数说明】 normal **：** 端口对外通告VLAN消息^
non-applicant **：** 端口不对外通告VLAN消息
【缺省配置】 允许端口发送GVRP通告
【命令模式】 接口模式
【使用指导】 设置端口的GVRP 通告模式

######  配置端口的登记模式

+ 可选配置。

+ GVRP的登记模式有normal和disabled两种。

+ 接口上使用命令gvrp registration mode normal开启注册动态VLAN功能，gvrp register mode disable 关闭注册动
  态VLAN功能。

+ 打开则收到对端VLAN信息后创建动态VLAN；关闭则收到GVRP报文时，不进行添加动态VLAN动作。

这两种登记模式不会影响端口上的静态VLAN，用户创建的静态VLAN永远都是 Fixed Registrar。

【命令格式】 gvrp registration mode { normal | disabled }
【参数说明】 normal **：** 端口允许加入动态VLAN
disabled **：** 端口不允许加入动态VLAN
【缺省配置】 gvrp功能开启时，trunk模式端口默认开启注册动态VLAN功能
【命令模式】 接口模式
【使用指导】 设置端口的GVRP 登记模式

######  切换端口模式为 trunk 模式

+ 必须配置，GVRP功能只有在trunk模式的端口上才生效。

+ GVRP功能仅在Trunk口上生效。

##### 检验方法

+ show gvrp configuration 查看配置信息。

+ 查看是否有创建动态VLAN，并将对应端口加入VLAN。

##### 配置举例

######  在拓扑环境中开启 GVRP 功能，动态维护 VLAN 以及 VLAN 和端口关系



【配置方法】 

+ 在交换机A和C上配置用户通信的VLAN。 
+ 在交换机A、B和C上开启GVRP功能，开启动态VLAN创建的开关。
+ 交换机之间互连的接口设置为Trunk口，必须保证这些Trunk口的VLAN许可列表包含用户通信的VLAN，默认Trunk口是允许所有VLAN。
+ 环境中最好开启STP协议，以免造成环路。

```
A  1 ：创建用户网络通信的VLAN 1- 200 。
A# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
A(config)# vlan range 1- 200
2 ：开启GVRP和动态VLAN创建的功能。
A(config)# gvrp enable
A(config)# gvrp dynamic-vlan-creation enable
3 ：将设备连接端口配置为Trunk口，Trunk口默认允许所有VLAN。
A(config)# interface gigabitEthernet 0/1
A(config-if-GigabitEthernet 0/1)# switchport mode trunk
4 ：配置Trunk口的通告模式和注册模式，默认为normal，可以不用手动配置。
A(config-if-GigabitEthernet 0/1)# gvrp applicant state normal
A(config-if-GigabitEthernet 0/1)# gvrp registration mode normal
A(config-if-GigabitEthernet 0/1)# end
```

```
C  配置同交换机A，这里不再赘述。
```

```
B
1 ：设备上开启GVRP和动态VLAN创建的功能。
B# configure terminal
B(config)# gvrp enable
B(config)# gvrp dynamic-vlan-creation enable
2 ：将互连设备的端口设置为trunk口。
B(config)# interface range GigabitEthernet 0/2- 3
B(config-if-GigabitEthernet 0/ 2 )# switchport mode trunk
```



【检验方法】 查看各个设备上GVRP配置是否正确。查看交换机B上是否有动态创建VLAN 2- 100 。并查看交换机B上G 0/2和G0/3口是否有加入这些动态VLAN。

```
A A# show gvrp configuration
Global GVRP Configuration:
GVRP Feature:enabled
GVRP dynamic VLAN creation:enabled
Join Timers(ms): 200
Leave Timers(ms): 600
Leaveall Timers(ms): 1000
Port based GVRP Configuration:
PORT Applicant Status Registration Mode
----------------------- -------------------- ---------------------
GigabitEthernet 0/ 1 normal normal
```

```
B B# show gvrp configuration
Global GVRP Configuration:
GVRP Feature:enabled
GVRP dynamic VLAN creation:enabled
Join Timers(ms): 200
Leave Timers(ms): 600
Leaveall Timers(ms): 1000
Port based GVRP Configuration:
PORT Applicant Status Registration Mode
----------------------- -------------------- ---------------------
GigabitEthernet 0/ 2 normal normal
GigabitEthernet 0/ 3 normal normal
```

```
C C# show gvrp configuration
Global GVRP Configuration:
GVRP Feature:enabled
GVRP dynamic VLAN creation:enabled
Join Timers(ms): 200
Leave Timers(ms): 600
Leaveall Timers(ms): 1000
Port based GVRP Configuration:
PORT Applicant Status Registration Mode
----------------------- -------------------- ---------------------
GigabitEthernet 0/ 1 normal normal
```

##### 常见配置错误

+ 设备连接的端口不是Trunk模式。

+ 设备连接的端口许可VLAN列表不包含用户通信的VLAN。

+ Trunk口的GVRP通告模式和注册模式不是normal模式。

#### 11.4.2 配置 GVRP PDUs 透传功能

##### 配置效果

设备未开启GVRP协议时，需要透传GVRP PDUs帧，使得与之互连的设备之间的GVRP计算正常。

##### 注意事项

GVRP PDUs 透传功能只在GVRP协议关闭时才启作用。当GVRP协议打开时，设备不透传GVRP PDUs帧。

##### 配置方法

######  配置 GVRP PDUs 透传功能

+ 可选配置

+ 设备未开启GVRP协议时，如里需要透传GVRP PDUs帧，则需要配置GVRP PDUs透传功能。

【命令格式】 bridge-frame forwarding protocol gvrp
【参数说明】 -
【缺省配置】 缺省是关闭的
【命令模式】 全局配置模式
【使用指导】 在IEEE 802.1Q标准中，GVRP PDUs的目的MAC地址 01 - 80 - C2- 00 - 00 - 06 是作为保留地址使用的，即遵循IEEE 802.1Q标准的设备，对于接收到的GVRP PDUs帧是不转发的。然而，在实际的网络布署中，可能需
要设备能够支持透传GVRP PDUs帧。例如，设备未开启GVRP协议时，需要透传GVRP PDUs帧，使得与之互连的设备之间的GVRP计算正常。
GVRP PDUs透传功能只在GVRP协议关闭时才启作用。当GVRP协议打开时，设备不透传GVRP PDUs帧。

##### 检验方法

显示验证。

##### 配置举例

######  配置 GVRP PDUs 透传功能

【网络环境】

DEVA，C上开启GVRP协议，DEV B未开启GVRP协议。

【配置方法】 DEV B上配置GVRP PDUs透传功能，使得DEV A，C之间的GVRP协议能够正确计算。

```
DEV B Ruijie(config)#bridge-frame forwarding protocol gvrp
```

【检验方法】 通过show run查看GVRP PDUs透传功能是否开启。

```
DEV B Ruijie#show run
Building configuration...
Current configuration : 694 bytes
bridge-frame forwarding protocol gvrp
```

#### 11.4.3 配置 GVRP PDUs TUNNEL

##### 配置效果

配置GVRP PDUs TUNNEL功能，使用户网络的GVRP协议报文能够通过运营商网络进行隧道透传，用户网络之间的GVRP协议报文的传输对运营商网络不会产生影响，从而使得用户网络和运营商网络的GVRP协议分开计算，互不干扰。

##### 注意事项

需要全局和接口同时开启GVRP PDUs TUNNEL功能后，GVRP PDUs TUNNEL功能才生效。

**配置方法**

######  配置 GVRP PDUs 透传功能

+ 可选配置。在QINQ网络中，如果需要用户网络和运营商网络的GVRP协议分开计算，互不干扰，可以通过配置GVRP PDUs TUNNEL达到效果。

+ 通过l2protocol-tunnel gvrp命令配置全局使能GVRP PDUs TUNNEL功能。

+ 通过l2protocol-tunnel gvrp enable命令配置接口使能GVRP PDUs TUNNEL功能。

+ 通过l2protocol-tunnel gvrp tunnel-dmac mac-address命令配置GVRP PDUs TUNNEL的透传地址。

【命令格式】 l2protocol-tunnel gvrp
【参数说明】 -
【缺省配置】 缺省是关闭的
【命令模式】 全局配置模式
【使用指导】 GVRP PDUs TUNNEL功能只在全局和接口同时使能的情况下才启作用。

【命令格式】 l2protocol-tunnel gvrp^ enable^
【参数说明】 -
【缺省配置】 缺省是关闭的
【命令模式】 接口配置模式
【使用指导】 GVRP PDUs TUNNEL功能只在全局和接口同时使能的情况下才启作用。

【命令格式】 l2protocol-tunnel gvrp tunnel-dmac mac-address

【参数说明】 mac-address：需要透传的GVRP协议地址
【缺省配置】 缺省使用的地址为01d0.f800.0006
【命令模式】 全局配置模式
【使用指导】 GVRP PDUs TUNNEL应用中，当用户网络的GVRP协议报文进入运营商网络的边缘设备后，将目的mac地址改成私有地址在运营商网络中转发，到了另外一端边缘设备后，再将目的mac地址改成公有地址回到另
一端用户网络，以达到GVRP协议报文在运营商网络透传的效果。这个私有地址，即为GVRP PDUs TUNNEL的透传地址。

GVRP报文可选透传地址范围：01d0.f800.0006 、011a.a900.0006 。
当未配置透传地址时，GVRP PDUs TUNNEL缺省使用的地址为01d0.f800.0006。

##### 检验方法

通过show l2protocol-tunnel gvrp命令查看GVRP PDUs TUNNEL配置。

##### 配置举例

以下配置举例，仅介绍与GVRP和QINQ相关的配置。

######  配置 GVRP PDUs TUNNEL 功能

【网络环境】
【配置方法】 

+ 在运营商网络边缘设备（本例为Provider S1/Provider S2上开启基本QinQ功能，使用户网络的数据报
  文在运营商网络的VLAN 200 中传输。
+ 在运营商网络边缘设备（本例为Provider S1/Provider S2上开启GVRP协议透传功能，使运营商网络可以通过GVRP PDUs TUNNEL对用户网络的GVRP报文进行隧道传输。Provider S1 (^) 第一步，创建服务商VLAN 200

```
Ruijie#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Ruijie(config)#vlan 200
Ruijie(config-vlan)#exit
第二步，在连接用户网络的接口上开启基本QinQ功能，使用VLAN 200对用户网络的数据进行隧道传输
Ruijie(config)#interface gigabitEthernet 0 /1
Ruijie(config-if-GigabitEthernet 0 /1)#switchport mode dot1q-tunnel
Ruijie(config-if-GigabitEthernet 0 /1)#switchport dot1q-tunnel native vlan 200
Ruijie(config-if-GigabitEthernet 0 /1)#switchport dot1q-tunnel allowed vlan add untagged 200
第三步，在连接用户网络的接口上开启GVRP协议透传功能
Ruijie(config-if-GigabitEthernet 0 /1)#l2protocol-tunnel gvrp enable
Ruijie(config-if-GigabitEthernet 0 /1)#exit
第四步，全局开启GVRP协议透传功能
Ruijie(config)#l2protocol-tunnel gvrp
第五步，配置uplink port
Ruijie(config)# interface gigabitEthernet 0 /5
Ruijie(config-if-GigabitEthernet 0 /5)#switchport mode uplink
```

Provider S2  Provider S2设备上的配置同Provider S1配置类似，请参考上文Provider S1的配置。此处不再重复说明。
【检验方法】 

+ 查看GVRP PDUs TUNNEL配置是否正确。
+ 查看Tunnel口的配置是否正确，关注点：接口类型是否为dot1q-tunnel，外层Tag VLAN是否为Native VLAN且其是否已加入接口的许可VLAN列表，运营商网络边缘设备上链口的类型是否为Uplink。
  Provider S1 

1 ：查看GVRP PDUs TUNNEL配置是否正确：

```
Ruijie#show l2protocol-tunnel gvrp
L2protocol-tunnel: Gvrp Enable
L2protocol-tunnel destination mac address: 01d0.f800.000 6
GigabitEthernet 0/1 l2protocol-tunnel gvrp enable
```

2 ：查看QINQ配置是否正确：

```
Ruijie#show running-config
interface GigabitEthernet 0 /1
switchport mode dot1q-tunnel
switchport dot1q-tunnel allowed vlan add untagged 200
switchport dot1q-tunnel native vlan 200
l2protocol-tunnel gvrp enable
！
interface GigabitEthernet 0 /5
switchport mode uplink
```

Provider S2 同Provider S1

##### 常见错误

运营商网络中，配置的GVRP PDUs TUNNEL透传地址要一致，才能正确透传GVRP PDUs帧。

## 11.5 监视与维护

##### 清除各类信息

在设备运行过程中执行clear命令，可能因为重要信息丢失而导致业务中断。

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>清除端口的统计值</td>         <td>clear gvrp statistics { interface-id | all }</td>     </tr> </table>

##### 查看运行情况

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>显示端口的统计值</td>         <td>show gvrp statistics { interface-id | all }</td>     </tr>     <tr>         <td>显示当前 GVRP 的运行状态</td>         <td>show gvrp status</td>     </tr>     <tr>         <td>显示当前 GVRP 的配置状态</td>         <td>show gvrp configuration</td>     </tr>     <tr>         <td>显示 GVRP PDUs TUNNEL 信息</td>         <td>show l2protocol-tunnel gvrp</td>     </tr> </table>

##### 查看调试信息

<table>     <tr>         <th>作用</th>         <th>命令</th>     </tr>     <tr>         <td>打开 GVRP 事件 debug 开关</td>         <td>debug gvrp event</td>     </tr>     <tr>         <td>打开 GVRP 定时器 debug 开关</td>         <td>debug gvrp timer</td>     </tr> </table>

输出调试信息，会占用系统资源。使用完毕后，请立即关闭调试开关。