# spine3

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [Management API HTTP](#management-api-http)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Configuration](#internal-vlan-allocation-policy-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | oob_management | oob | MGMT | 192.168.0.13/24 | 192.168.0.1 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management0
   description oob_management
   no shutdown
   vrf MGMT
   ip address 192.168.0.13/24
```

### DNS Domain

#### DNS domain: atd.lab

#### DNS Domain Device Configuration

```eos
dns domain atd.lab
!
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

#### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Type | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | -----| ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet3 | P2P_LINK_TO_LEAF1_Ethernet5 | routed | - | 192.168.0.4/31 | default | 1500 | False | - | - |
| Ethernet4 | P2P_LINK_TO_LEAF2_Ethernet5 | routed | - | 192.168.0.16/31 | default | 1500 | False | - | - |
| Ethernet5 | P2P_LINK_TO_LEAF3_Ethernet5 | routed | - | 192.168.0.28/31 | default | 1500 | False | - | - |
| Ethernet6 | P2P_LINK_TO_LEAF4_Ethernet5 | routed | - | 192.168.0.40/31 | default | 1500 | False | - | - |
| Ethernet7 | P2P_LINK_TO_LEAF5_Ethernet5 | routed | - | 192.168.0.52/31 | default | 1500 | False | - | - |
| Ethernet8 | P2P_LINK_TO_LEAF6_Ethernet5 | routed | - | 192.168.0.64/31 | default | 1500 | False | - | - |
| Ethernet9 | P2P_LINK_TO_LEAF7_Ethernet5 | routed | - | 192.168.0.76/31 | default | 1500 | False | - | - |
| Ethernet10 | P2P_LINK_TO_LEAF8_Ethernet5 | routed | - | 192.168.0.88/31 | default | 1500 | False | - | - |
| Ethernet11 | P2P_LINK_TO_LEAF9_Ethernet5 | routed | - | 192.168.0.100/31 | default | 1500 | False | - | - |
| Ethernet12 | P2P_LINK_TO_LEAF10_Ethernet5 | routed | - | 192.168.0.112/31 | default | 1500 | False | - | - |
| Ethernet13 | P2P_LINK_TO_LEAF11_Ethernet5 | routed | - | 192.168.0.124/31 | default | 1500 | False | - | - |
| Ethernet14 | P2P_LINK_TO_LEAF12_Ethernet5 | routed | - | 192.168.0.136/31 | default | 1500 | False | - | - |
| Ethernet15 | P2P_LINK_TO_LEAF13_Ethernet5 | routed | - | 192.168.0.148/31 | default | 1500 | False | - | - |
| Ethernet16 | P2P_LINK_TO_LEAF14_Ethernet5 | routed | - | 192.168.0.160/31 | default | 1500 | False | - | - |
| Ethernet17 | P2P_LINK_TO_LEAF15_Ethernet5 | routed | - | 192.168.0.172/31 | default | 1500 | False | - | - |
| Ethernet18 | P2P_LINK_TO_LEAF16_Ethernet5 | routed | - | 192.168.0.184/31 | default | 1500 | False | - | - |
| Ethernet19 | P2P_LINK_TO_LEAF17_Ethernet5 | routed | - | 192.168.0.196/31 | default | 1500 | False | - | - |
| Ethernet20 | P2P_LINK_TO_LEAF18_Ethernet5 | routed | - | 192.168.0.208/31 | default | 1500 | False | - | - |
| Ethernet21 | P2P_LINK_TO_LEAF19_Ethernet5 | routed | - | 192.168.0.220/31 | default | 1500 | False | - | - |
| Ethernet22 | P2P_LINK_TO_LEAF20_Ethernet5 | routed | - | 192.168.0.232/31 | default | 1500 | False | - | - |
| Ethernet23 | P2P_LINK_TO_LEAF21_Ethernet5 | routed | - | 192.168.0.244/31 | default | 1500 | False | - | - |
| Ethernet24 | P2P_LINK_TO_LEAF22_Ethernet5 | routed | - | 192.168.1.0/31 | default | 1500 | False | - | - |
| Ethernet25 | P2P_LINK_TO_LEAF23_Ethernet5 | routed | - | 192.168.1.12/31 | default | 1500 | False | - | - |
| Ethernet26 | P2P_LINK_TO_LEAF24_Ethernet5 | routed | - | 192.168.1.24/31 | default | 1500 | False | - | - |
| Ethernet27 | P2P_LINK_TO_LEAF25_Ethernet5 | routed | - | 192.168.1.36/31 | default | 1500 | False | - | - |
| Ethernet28 | P2P_LINK_TO_LEAF26_Ethernet5 | routed | - | 192.168.1.48/31 | default | 1500 | False | - | - |
| Ethernet29 | P2P_LINK_TO_LEAF27_Ethernet5 | routed | - | 192.168.1.60/31 | default | 1500 | False | - | - |
| Ethernet30 | P2P_LINK_TO_LEAF28_Ethernet5 | routed | - | 192.168.1.72/31 | default | 1500 | False | - | - |
| Ethernet31 | P2P_LINK_TO_LEAF29_Ethernet5 | routed | - | 192.168.1.84/31 | default | 1500 | False | - | - |
| Ethernet32 | P2P_LINK_TO_LEAF30_Ethernet5 | routed | - | 192.168.1.96/31 | default | 1500 | False | - | - |
| Ethernet33 | P2P_LINK_TO_LEAF31_Ethernet5 | routed | - | 192.168.1.108/31 | default | 1500 | False | - | - |
| Ethernet34 | P2P_LINK_TO_LEAF32_Ethernet5 | routed | - | 192.168.1.120/31 | default | 1500 | False | - | - |
| Ethernet35 | P2P_LINK_TO_LEAF33_Ethernet5 | routed | - | 192.168.1.132/31 | default | 1500 | False | - | - |
| Ethernet36 | P2P_LINK_TO_LEAF34_Ethernet5 | routed | - | 192.168.1.144/31 | default | 1500 | False | - | - |
| Ethernet37 | P2P_LINK_TO_LEAF35_Ethernet5 | routed | - | 192.168.1.156/31 | default | 1500 | False | - | - |
| Ethernet38 | P2P_LINK_TO_LEAF36_Ethernet5 | routed | - | 192.168.1.168/31 | default | 1500 | False | - | - |
| Ethernet39 | P2P_LINK_TO_LEAF37_Ethernet5 | routed | - | 192.168.1.180/31 | default | 1500 | False | - | - |
| Ethernet40 | P2P_LINK_TO_LEAF38_Ethernet5 | routed | - | 192.168.1.192/31 | default | 1500 | False | - | - |
| Ethernet41 | P2P_LINK_TO_LEAF39_Ethernet5 | routed | - | 192.168.1.204/31 | default | 1500 | False | - | - |
| Ethernet42 | P2P_LINK_TO_LEAF40_Ethernet5 | routed | - | 192.168.1.216/31 | default | 1500 | False | - | - |
| Ethernet43 | P2P_LINK_TO_LEAF41_Ethernet5 | routed | - | 192.168.1.228/31 | default | 1500 | False | - | - |
| Ethernet44 | P2P_LINK_TO_LEAF42_Ethernet5 | routed | - | 192.168.1.240/31 | default | 1500 | False | - | - |
| Ethernet45 | P2P_LINK_TO_LEAF43_Ethernet5 | routed | - | 192.168.1.252/31 | default | 1500 | False | - | - |
| Ethernet46 | P2P_LINK_TO_LEAF44_Ethernet5 | routed | - | 192.168.2.8/31 | default | 1500 | False | - | - |
| Ethernet47 | P2P_LINK_TO_LEAF45_Ethernet5 | routed | - | 192.168.2.20/31 | default | 1500 | False | - | - |
| Ethernet48 | P2P_LINK_TO_LEAF46_Ethernet5 | routed | - | 192.168.2.32/31 | default | 1500 | False | - | - |
| Ethernet49 | P2P_LINK_TO_LEAF47_Ethernet5 | routed | - | 192.168.2.44/31 | default | 1500 | False | - | - |
| Ethernet50 | P2P_LINK_TO_LEAF48_Ethernet5 | routed | - | 192.168.2.56/31 | default | 1500 | False | - | - |
| Ethernet51 | P2P_LINK_TO_LEAF49_Ethernet5 | routed | - | 192.168.2.68/31 | default | 1500 | False | - | - |
| Ethernet52 | P2P_LINK_TO_LEAF50_Ethernet5 | routed | - | 192.168.2.80/31 | default | 1500 | False | - | - |
| Ethernet53 | P2P_LINK_TO_LEAF51_Ethernet5 | routed | - | 192.168.2.92/31 | default | 1500 | False | - | - |
| Ethernet54 | P2P_LINK_TO_LEAF52_Ethernet5 | routed | - | 192.168.2.104/31 | default | 1500 | False | - | - |
| Ethernet55 | P2P_LINK_TO_LEAF53_Ethernet5 | routed | - | 192.168.2.116/31 | default | 1500 | False | - | - |
| Ethernet56 | P2P_LINK_TO_LEAF54_Ethernet5 | routed | - | 192.168.2.128/31 | default | 1500 | False | - | - |
| Ethernet57 | P2P_LINK_TO_LEAF55_Ethernet5 | routed | - | 192.168.2.140/31 | default | 1500 | False | - | - |
| Ethernet58 | P2P_LINK_TO_LEAF56_Ethernet5 | routed | - | 192.168.2.152/31 | default | 1500 | False | - | - |
| Ethernet59 | P2P_LINK_TO_LEAF57_Ethernet5 | routed | - | 192.168.2.164/31 | default | 1500 | False | - | - |
| Ethernet60 | P2P_LINK_TO_LEAF58_Ethernet5 | routed | - | 192.168.2.176/31 | default | 1500 | False | - | - |
| Ethernet61 | P2P_LINK_TO_LEAF59_Ethernet5 | routed | - | 192.168.2.188/31 | default | 1500 | False | - | - |
| Ethernet62 | P2P_LINK_TO_LEAF60_Ethernet5 | routed | - | 192.168.2.200/31 | default | 1500 | False | - | - |
| Ethernet63 | P2P_LINK_TO_LEAF61_Ethernet5 | routed | - | 192.168.2.212/31 | default | 1500 | False | - | - |
| Ethernet64 | P2P_LINK_TO_LEAF62_Ethernet5 | routed | - | 192.168.2.224/31 | default | 1500 | False | - | - |
| Ethernet65 | P2P_LINK_TO_LEAF63_Ethernet5 | routed | - | 192.168.2.236/31 | default | 1500 | False | - | - |
| Ethernet66 | P2P_LINK_TO_LEAF64_Ethernet5 | routed | - | 192.168.2.248/31 | default | 1500 | False | - | - |
| Ethernet67 | P2P_LINK_TO_LEAF65_Ethernet5 | routed | - | 192.168.3.4/31 | default | 1500 | False | - | - |
| Ethernet68 | P2P_LINK_TO_LEAF66_Ethernet5 | routed | - | 192.168.3.16/31 | default | 1500 | False | - | - |
| Ethernet69 | P2P_LINK_TO_LEAF67_Ethernet5 | routed | - | 192.168.3.28/31 | default | 1500 | False | - | - |
| Ethernet70 | P2P_LINK_TO_LEAF68_Ethernet5 | routed | - | 192.168.3.40/31 | default | 1500 | False | - | - |
| Ethernet71 | P2P_LINK_TO_LEAF69_Ethernet5 | routed | - | 192.168.3.52/31 | default | 1500 | False | - | - |
| Ethernet72 | P2P_LINK_TO_LEAF70_Ethernet5 | routed | - | 192.168.3.64/31 | default | 1500 | False | - | - |
| Ethernet73 | P2P_LINK_TO_LEAF71_Ethernet5 | routed | - | 192.168.3.76/31 | default | 1500 | False | - | - |
| Ethernet74 | P2P_LINK_TO_LEAF72_Ethernet5 | routed | - | 192.168.3.88/31 | default | 1500 | False | - | - |
| Ethernet75 | P2P_LINK_TO_LEAF73_Ethernet5 | routed | - | 192.168.3.100/31 | default | 1500 | False | - | - |
| Ethernet76 | P2P_LINK_TO_LEAF74_Ethernet5 | routed | - | 192.168.3.112/31 | default | 1500 | False | - | - |
| Ethernet77 | P2P_LINK_TO_LEAF75_Ethernet5 | routed | - | 192.168.3.124/31 | default | 1500 | False | - | - |
| Ethernet78 | P2P_LINK_TO_LEAF76_Ethernet5 | routed | - | 192.168.3.136/31 | default | 1500 | False | - | - |
| Ethernet79 | P2P_LINK_TO_LEAF77_Ethernet5 | routed | - | 192.168.3.148/31 | default | 1500 | False | - | - |
| Ethernet80 | P2P_LINK_TO_LEAF78_Ethernet5 | routed | - | 192.168.3.160/31 | default | 1500 | False | - | - |
| Ethernet81 | P2P_LINK_TO_LEAF79_Ethernet5 | routed | - | 192.168.3.172/31 | default | 1500 | False | - | - |
| Ethernet82 | P2P_LINK_TO_LEAF80_Ethernet5 | routed | - | 192.168.3.184/31 | default | 1500 | False | - | - |
| Ethernet83 | P2P_LINK_TO_LEAF81_Ethernet5 | routed | - | 192.168.3.196/31 | default | 1500 | False | - | - |
| Ethernet84 | P2P_LINK_TO_LEAF82_Ethernet5 | routed | - | 192.168.3.208/31 | default | 1500 | False | - | - |
| Ethernet85 | P2P_LINK_TO_LEAF83_Ethernet5 | routed | - | 192.168.3.220/31 | default | 1500 | False | - | - |
| Ethernet86 | P2P_LINK_TO_LEAF84_Ethernet5 | routed | - | 192.168.3.232/31 | default | 1500 | False | - | - |
| Ethernet87 | P2P_LINK_TO_LEAF85_Ethernet5 | routed | - | 192.168.3.244/31 | default | 1500 | False | - | - |
| Ethernet88 | P2P_LINK_TO_LEAF86_Ethernet5 | routed | - | 192.168.4.0/31 | default | 1500 | False | - | - |
| Ethernet89 | P2P_LINK_TO_LEAF87_Ethernet5 | routed | - | 192.168.4.12/31 | default | 1500 | False | - | - |
| Ethernet90 | P2P_LINK_TO_LEAF88_Ethernet5 | routed | - | 192.168.4.24/31 | default | 1500 | False | - | - |
| Ethernet91 | P2P_LINK_TO_LEAF89_Ethernet5 | routed | - | 192.168.4.36/31 | default | 1500 | False | - | - |
| Ethernet92 | P2P_LINK_TO_LEAF90_Ethernet5 | routed | - | 192.168.4.48/31 | default | 1500 | False | - | - |
| Ethernet93 | P2P_LINK_TO_LEAF91_Ethernet5 | routed | - | 192.168.4.60/31 | default | 1500 | False | - | - |
| Ethernet94 | P2P_LINK_TO_LEAF92_Ethernet5 | routed | - | 192.168.4.72/31 | default | 1500 | False | - | - |
| Ethernet95 | P2P_LINK_TO_LEAF93_Ethernet5 | routed | - | 192.168.4.84/31 | default | 1500 | False | - | - |
| Ethernet96 | P2P_LINK_TO_LEAF94_Ethernet5 | routed | - | 192.168.4.96/31 | default | 1500 | False | - | - |
| Ethernet97 | P2P_LINK_TO_LEAF95_Ethernet5 | routed | - | 192.168.4.108/31 | default | 1500 | False | - | - |
| Ethernet98 | P2P_LINK_TO_LEAF96_Ethernet5 | routed | - | 192.168.4.120/31 | default | 1500 | False | - | - |
| Ethernet99 | P2P_LINK_TO_LEAF97_Ethernet5 | routed | - | 192.168.4.132/31 | default | 1500 | False | - | - |
| Ethernet100 | P2P_LINK_TO_LEAF98_Ethernet5 | routed | - | 192.168.4.144/31 | default | 1500 | False | - | - |
| Ethernet101 | P2P_LINK_TO_LEAF99_Ethernet5 | routed | - | 192.168.4.156/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description P2P_LINK_TO_LEAF1_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.4/31
!
interface Ethernet4
   description P2P_LINK_TO_LEAF2_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.16/31
!
interface Ethernet5
   description P2P_LINK_TO_LEAF3_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.28/31
!
interface Ethernet6
   description P2P_LINK_TO_LEAF4_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.40/31
!
interface Ethernet7
   description P2P_LINK_TO_LEAF5_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.52/31
!
interface Ethernet8
   description P2P_LINK_TO_LEAF6_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.64/31
!
interface Ethernet9
   description P2P_LINK_TO_LEAF7_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.76/31
!
interface Ethernet10
   description P2P_LINK_TO_LEAF8_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.88/31
!
interface Ethernet11
   description P2P_LINK_TO_LEAF9_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.100/31
!
interface Ethernet12
   description P2P_LINK_TO_LEAF10_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.112/31
!
interface Ethernet13
   description P2P_LINK_TO_LEAF11_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.124/31
!
interface Ethernet14
   description P2P_LINK_TO_LEAF12_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.136/31
!
interface Ethernet15
   description P2P_LINK_TO_LEAF13_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.148/31
!
interface Ethernet16
   description P2P_LINK_TO_LEAF14_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.160/31
!
interface Ethernet17
   description P2P_LINK_TO_LEAF15_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.172/31
!
interface Ethernet18
   description P2P_LINK_TO_LEAF16_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.184/31
!
interface Ethernet19
   description P2P_LINK_TO_LEAF17_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.196/31
!
interface Ethernet20
   description P2P_LINK_TO_LEAF18_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.208/31
!
interface Ethernet21
   description P2P_LINK_TO_LEAF19_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.220/31
!
interface Ethernet22
   description P2P_LINK_TO_LEAF20_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.232/31
!
interface Ethernet23
   description P2P_LINK_TO_LEAF21_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.244/31
!
interface Ethernet24
   description P2P_LINK_TO_LEAF22_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.0/31
!
interface Ethernet25
   description P2P_LINK_TO_LEAF23_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.12/31
!
interface Ethernet26
   description P2P_LINK_TO_LEAF24_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.24/31
!
interface Ethernet27
   description P2P_LINK_TO_LEAF25_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.36/31
!
interface Ethernet28
   description P2P_LINK_TO_LEAF26_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.48/31
!
interface Ethernet29
   description P2P_LINK_TO_LEAF27_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.60/31
!
interface Ethernet30
   description P2P_LINK_TO_LEAF28_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.72/31
!
interface Ethernet31
   description P2P_LINK_TO_LEAF29_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.84/31
!
interface Ethernet32
   description P2P_LINK_TO_LEAF30_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.96/31
!
interface Ethernet33
   description P2P_LINK_TO_LEAF31_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.108/31
!
interface Ethernet34
   description P2P_LINK_TO_LEAF32_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.120/31
!
interface Ethernet35
   description P2P_LINK_TO_LEAF33_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.132/31
!
interface Ethernet36
   description P2P_LINK_TO_LEAF34_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.144/31
!
interface Ethernet37
   description P2P_LINK_TO_LEAF35_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.156/31
!
interface Ethernet38
   description P2P_LINK_TO_LEAF36_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.168/31
!
interface Ethernet39
   description P2P_LINK_TO_LEAF37_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.180/31
!
interface Ethernet40
   description P2P_LINK_TO_LEAF38_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.192/31
!
interface Ethernet41
   description P2P_LINK_TO_LEAF39_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.204/31
!
interface Ethernet42
   description P2P_LINK_TO_LEAF40_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.216/31
!
interface Ethernet43
   description P2P_LINK_TO_LEAF41_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.228/31
!
interface Ethernet44
   description P2P_LINK_TO_LEAF42_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.240/31
!
interface Ethernet45
   description P2P_LINK_TO_LEAF43_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.252/31
!
interface Ethernet46
   description P2P_LINK_TO_LEAF44_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.8/31
!
interface Ethernet47
   description P2P_LINK_TO_LEAF45_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.20/31
!
interface Ethernet48
   description P2P_LINK_TO_LEAF46_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.32/31
!
interface Ethernet49
   description P2P_LINK_TO_LEAF47_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.44/31
!
interface Ethernet50
   description P2P_LINK_TO_LEAF48_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.56/31
!
interface Ethernet51
   description P2P_LINK_TO_LEAF49_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.68/31
!
interface Ethernet52
   description P2P_LINK_TO_LEAF50_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.80/31
!
interface Ethernet53
   description P2P_LINK_TO_LEAF51_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.92/31
!
interface Ethernet54
   description P2P_LINK_TO_LEAF52_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.104/31
!
interface Ethernet55
   description P2P_LINK_TO_LEAF53_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.116/31
!
interface Ethernet56
   description P2P_LINK_TO_LEAF54_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.128/31
!
interface Ethernet57
   description P2P_LINK_TO_LEAF55_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.140/31
!
interface Ethernet58
   description P2P_LINK_TO_LEAF56_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.152/31
!
interface Ethernet59
   description P2P_LINK_TO_LEAF57_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.164/31
!
interface Ethernet60
   description P2P_LINK_TO_LEAF58_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.176/31
!
interface Ethernet61
   description P2P_LINK_TO_LEAF59_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.188/31
!
interface Ethernet62
   description P2P_LINK_TO_LEAF60_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.200/31
!
interface Ethernet63
   description P2P_LINK_TO_LEAF61_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.212/31
!
interface Ethernet64
   description P2P_LINK_TO_LEAF62_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.224/31
!
interface Ethernet65
   description P2P_LINK_TO_LEAF63_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.236/31
!
interface Ethernet66
   description P2P_LINK_TO_LEAF64_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.248/31
!
interface Ethernet67
   description P2P_LINK_TO_LEAF65_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.4/31
!
interface Ethernet68
   description P2P_LINK_TO_LEAF66_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.16/31
!
interface Ethernet69
   description P2P_LINK_TO_LEAF67_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.28/31
!
interface Ethernet70
   description P2P_LINK_TO_LEAF68_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.40/31
!
interface Ethernet71
   description P2P_LINK_TO_LEAF69_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.52/31
!
interface Ethernet72
   description P2P_LINK_TO_LEAF70_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.64/31
!
interface Ethernet73
   description P2P_LINK_TO_LEAF71_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.76/31
!
interface Ethernet74
   description P2P_LINK_TO_LEAF72_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.88/31
!
interface Ethernet75
   description P2P_LINK_TO_LEAF73_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.100/31
!
interface Ethernet76
   description P2P_LINK_TO_LEAF74_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.112/31
!
interface Ethernet77
   description P2P_LINK_TO_LEAF75_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.124/31
!
interface Ethernet78
   description P2P_LINK_TO_LEAF76_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.136/31
!
interface Ethernet79
   description P2P_LINK_TO_LEAF77_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.148/31
!
interface Ethernet80
   description P2P_LINK_TO_LEAF78_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.160/31
!
interface Ethernet81
   description P2P_LINK_TO_LEAF79_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.172/31
!
interface Ethernet82
   description P2P_LINK_TO_LEAF80_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.184/31
!
interface Ethernet83
   description P2P_LINK_TO_LEAF81_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.196/31
!
interface Ethernet84
   description P2P_LINK_TO_LEAF82_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.208/31
!
interface Ethernet85
   description P2P_LINK_TO_LEAF83_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.220/31
!
interface Ethernet86
   description P2P_LINK_TO_LEAF84_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.232/31
!
interface Ethernet87
   description P2P_LINK_TO_LEAF85_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.244/31
!
interface Ethernet88
   description P2P_LINK_TO_LEAF86_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.0/31
!
interface Ethernet89
   description P2P_LINK_TO_LEAF87_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.12/31
!
interface Ethernet90
   description P2P_LINK_TO_LEAF88_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.24/31
!
interface Ethernet91
   description P2P_LINK_TO_LEAF89_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.36/31
!
interface Ethernet92
   description P2P_LINK_TO_LEAF90_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.48/31
!
interface Ethernet93
   description P2P_LINK_TO_LEAF91_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.60/31
!
interface Ethernet94
   description P2P_LINK_TO_LEAF92_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.72/31
!
interface Ethernet95
   description P2P_LINK_TO_LEAF93_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.84/31
!
interface Ethernet96
   description P2P_LINK_TO_LEAF94_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.96/31
!
interface Ethernet97
   description P2P_LINK_TO_LEAF95_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.108/31
!
interface Ethernet98
   description P2P_LINK_TO_LEAF96_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.120/31
!
interface Ethernet99
   description P2P_LINK_TO_LEAF97_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.132/31
!
interface Ethernet100
   description P2P_LINK_TO_LEAF98_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.144/31
!
interface Ethernet101
   description P2P_LINK_TO_LEAF99_Ethernet5
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.156/31
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.101.13/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |


#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ip address 192.168.101.13/32
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| MGMT | 0.0.0.0/0 | 192.168.0.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.0.1
```

### Router BGP

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001|  192.168.101.13 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Next-hop unchanged | True |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- |
| 192.168.0.5 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.17 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.29 | 65299 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.41 | 65299 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.53 | 65104 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.65 | 65105 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.77 | 65106 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.89 | 65107 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.101 | 65108 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.113 | 65109 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.125 | 65110 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.137 | 65111 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.149 | 65112 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.161 | 65113 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.173 | 65114 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.185 | 65115 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.197 | 65116 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.209 | 65117 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.221 | 65118 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.233 | 65119 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.245 | 65120 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.1 | 65121 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.13 | 65122 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.25 | 65123 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.37 | 65124 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.49 | 65125 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.61 | 65126 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.73 | 65127 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.85 | 65128 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.97 | 65129 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.109 | 65130 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.121 | 65131 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.133 | 65132 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.145 | 65133 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.157 | 65134 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.169 | 65135 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.181 | 65136 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.193 | 65137 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.205 | 65138 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.217 | 65139 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.229 | 65140 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.241 | 65141 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.253 | 65142 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.9 | 65143 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.21 | 65144 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.33 | 65145 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.45 | 65146 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.57 | 65147 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.69 | 65148 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.81 | 65149 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.93 | 65150 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.105 | 65151 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.117 | 65152 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.129 | 65153 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.141 | 65154 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.153 | 65155 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.165 | 65156 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.177 | 65157 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.189 | 65158 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.201 | 65159 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.213 | 65160 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.225 | 65161 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.237 | 65162 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.249 | 65163 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.5 | 65164 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.17 | 65165 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.29 | 65166 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.41 | 65167 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.53 | 65168 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.65 | 65169 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.77 | 65170 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.89 | 65171 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.101 | 65172 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.113 | 65173 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.125 | 65174 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.137 | 65175 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.149 | 65176 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.161 | 65177 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.173 | 65178 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.185 | 65179 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.197 | 65180 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.209 | 65181 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.221 | 65182 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.233 | 65183 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.245 | 65184 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.1 | 65185 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.13 | 65186 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.25 | 65187 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.37 | 65188 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.49 | 65189 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.61 | 65190 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.73 | 65191 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.85 | 65192 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.97 | 65193 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.109 | 65194 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.121 | 65195 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.133 | 65196 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.145 | 65197 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.157 | 65198 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.101.1 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.2 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.3 | 65299 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.4 | 65299 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.5 | 65104 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.6 | 65105 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.7 | 65106 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.8 | 65107 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.9 | 65108 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.10 | 65109 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.11 | 65110 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.12 | 65111 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.13 | 65112 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.14 | 65113 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.15 | 65114 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.16 | 65115 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.17 | 65116 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.18 | 65117 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.19 | 65118 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.20 | 65119 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.21 | 65120 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.22 | 65121 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.23 | 65122 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.24 | 65123 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.25 | 65124 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.26 | 65125 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.27 | 65126 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.28 | 65127 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.29 | 65128 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.30 | 65129 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.31 | 65130 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.32 | 65131 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.33 | 65132 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.34 | 65133 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.35 | 65134 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.36 | 65135 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.37 | 65136 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.38 | 65137 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.39 | 65138 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.40 | 65139 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.41 | 65140 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.42 | 65141 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.43 | 65142 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.44 | 65143 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.45 | 65144 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.46 | 65145 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.47 | 65146 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.48 | 65147 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.49 | 65148 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.50 | 65149 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.51 | 65150 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.52 | 65151 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.53 | 65152 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.54 | 65153 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.55 | 65154 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.56 | 65155 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.57 | 65156 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.58 | 65157 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.59 | 65158 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.60 | 65159 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.61 | 65160 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.62 | 65161 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.63 | 65162 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.64 | 65163 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.65 | 65164 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.66 | 65165 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.67 | 65166 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.68 | 65167 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.69 | 65168 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.70 | 65169 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.71 | 65170 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.72 | 65171 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.73 | 65172 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.74 | 65173 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.75 | 65174 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.76 | 65175 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.77 | 65176 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.78 | 65177 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.79 | 65178 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.80 | 65179 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.81 | 65180 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.82 | 65181 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.83 | 65182 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.84 | 65183 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.85 | 65184 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.86 | 65185 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.87 | 65186 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.88 | 65187 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.89 | 65188 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.90 | 65189 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.91 | 65190 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.92 | 65191 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.93 | 65192 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.94 | 65193 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.95 | 65194 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.96 | 65195 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.97 | 65196 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.98 | 65197 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.101.99 | 65198 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 192.168.101.13
   maximum-paths 4 ecmp 4
   no bgp default ipv4-unicast
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 192.168.0.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.5 remote-as 65100
   neighbor 192.168.0.5 description leaf1_Ethernet5
   neighbor 192.168.0.17 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.17 remote-as 65100
   neighbor 192.168.0.17 description leaf2_Ethernet5
   neighbor 192.168.0.29 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.29 remote-as 65299
   neighbor 192.168.0.29 description leaf3_Ethernet5
   neighbor 192.168.0.41 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.41 remote-as 65299
   neighbor 192.168.0.41 description leaf4_Ethernet5
   neighbor 192.168.0.53 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.53 remote-as 65104
   neighbor 192.168.0.53 description leaf5_Ethernet5
   neighbor 192.168.0.65 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.65 remote-as 65105
   neighbor 192.168.0.65 description leaf6_Ethernet5
   neighbor 192.168.0.77 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.77 remote-as 65106
   neighbor 192.168.0.77 description leaf7_Ethernet5
   neighbor 192.168.0.89 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.89 remote-as 65107
   neighbor 192.168.0.89 description leaf8_Ethernet5
   neighbor 192.168.0.101 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.101 remote-as 65108
   neighbor 192.168.0.101 description leaf9_Ethernet5
   neighbor 192.168.0.113 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.113 remote-as 65109
   neighbor 192.168.0.113 description leaf10_Ethernet5
   neighbor 192.168.0.125 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.125 remote-as 65110
   neighbor 192.168.0.125 description leaf11_Ethernet5
   neighbor 192.168.0.137 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.137 remote-as 65111
   neighbor 192.168.0.137 description leaf12_Ethernet5
   neighbor 192.168.0.149 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.149 remote-as 65112
   neighbor 192.168.0.149 description leaf13_Ethernet5
   neighbor 192.168.0.161 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.161 remote-as 65113
   neighbor 192.168.0.161 description leaf14_Ethernet5
   neighbor 192.168.0.173 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.173 remote-as 65114
   neighbor 192.168.0.173 description leaf15_Ethernet5
   neighbor 192.168.0.185 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.185 remote-as 65115
   neighbor 192.168.0.185 description leaf16_Ethernet5
   neighbor 192.168.0.197 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.197 remote-as 65116
   neighbor 192.168.0.197 description leaf17_Ethernet5
   neighbor 192.168.0.209 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.209 remote-as 65117
   neighbor 192.168.0.209 description leaf18_Ethernet5
   neighbor 192.168.0.221 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.221 remote-as 65118
   neighbor 192.168.0.221 description leaf19_Ethernet5
   neighbor 192.168.0.233 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.233 remote-as 65119
   neighbor 192.168.0.233 description leaf20_Ethernet5
   neighbor 192.168.0.245 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.245 remote-as 65120
   neighbor 192.168.0.245 description leaf21_Ethernet5
   neighbor 192.168.1.1 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.1 remote-as 65121
   neighbor 192.168.1.1 description leaf22_Ethernet5
   neighbor 192.168.1.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.13 remote-as 65122
   neighbor 192.168.1.13 description leaf23_Ethernet5
   neighbor 192.168.1.25 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.25 remote-as 65123
   neighbor 192.168.1.25 description leaf24_Ethernet5
   neighbor 192.168.1.37 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.37 remote-as 65124
   neighbor 192.168.1.37 description leaf25_Ethernet5
   neighbor 192.168.1.49 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.49 remote-as 65125
   neighbor 192.168.1.49 description leaf26_Ethernet5
   neighbor 192.168.1.61 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.61 remote-as 65126
   neighbor 192.168.1.61 description leaf27_Ethernet5
   neighbor 192.168.1.73 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.73 remote-as 65127
   neighbor 192.168.1.73 description leaf28_Ethernet5
   neighbor 192.168.1.85 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.85 remote-as 65128
   neighbor 192.168.1.85 description leaf29_Ethernet5
   neighbor 192.168.1.97 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.97 remote-as 65129
   neighbor 192.168.1.97 description leaf30_Ethernet5
   neighbor 192.168.1.109 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.109 remote-as 65130
   neighbor 192.168.1.109 description leaf31_Ethernet5
   neighbor 192.168.1.121 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.121 remote-as 65131
   neighbor 192.168.1.121 description leaf32_Ethernet5
   neighbor 192.168.1.133 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.133 remote-as 65132
   neighbor 192.168.1.133 description leaf33_Ethernet5
   neighbor 192.168.1.145 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.145 remote-as 65133
   neighbor 192.168.1.145 description leaf34_Ethernet5
   neighbor 192.168.1.157 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.157 remote-as 65134
   neighbor 192.168.1.157 description leaf35_Ethernet5
   neighbor 192.168.1.169 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.169 remote-as 65135
   neighbor 192.168.1.169 description leaf36_Ethernet5
   neighbor 192.168.1.181 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.181 remote-as 65136
   neighbor 192.168.1.181 description leaf37_Ethernet5
   neighbor 192.168.1.193 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.193 remote-as 65137
   neighbor 192.168.1.193 description leaf38_Ethernet5
   neighbor 192.168.1.205 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.205 remote-as 65138
   neighbor 192.168.1.205 description leaf39_Ethernet5
   neighbor 192.168.1.217 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.217 remote-as 65139
   neighbor 192.168.1.217 description leaf40_Ethernet5
   neighbor 192.168.1.229 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.229 remote-as 65140
   neighbor 192.168.1.229 description leaf41_Ethernet5
   neighbor 192.168.1.241 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.241 remote-as 65141
   neighbor 192.168.1.241 description leaf42_Ethernet5
   neighbor 192.168.1.253 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.253 remote-as 65142
   neighbor 192.168.1.253 description leaf43_Ethernet5
   neighbor 192.168.2.9 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.9 remote-as 65143
   neighbor 192.168.2.9 description leaf44_Ethernet5
   neighbor 192.168.2.21 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.21 remote-as 65144
   neighbor 192.168.2.21 description leaf45_Ethernet5
   neighbor 192.168.2.33 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.33 remote-as 65145
   neighbor 192.168.2.33 description leaf46_Ethernet5
   neighbor 192.168.2.45 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.45 remote-as 65146
   neighbor 192.168.2.45 description leaf47_Ethernet5
   neighbor 192.168.2.57 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.57 remote-as 65147
   neighbor 192.168.2.57 description leaf48_Ethernet5
   neighbor 192.168.2.69 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.69 remote-as 65148
   neighbor 192.168.2.69 description leaf49_Ethernet5
   neighbor 192.168.2.81 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.81 remote-as 65149
   neighbor 192.168.2.81 description leaf50_Ethernet5
   neighbor 192.168.2.93 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.93 remote-as 65150
   neighbor 192.168.2.93 description leaf51_Ethernet5
   neighbor 192.168.2.105 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.105 remote-as 65151
   neighbor 192.168.2.105 description leaf52_Ethernet5
   neighbor 192.168.2.117 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.117 remote-as 65152
   neighbor 192.168.2.117 description leaf53_Ethernet5
   neighbor 192.168.2.129 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.129 remote-as 65153
   neighbor 192.168.2.129 description leaf54_Ethernet5
   neighbor 192.168.2.141 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.141 remote-as 65154
   neighbor 192.168.2.141 description leaf55_Ethernet5
   neighbor 192.168.2.153 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.153 remote-as 65155
   neighbor 192.168.2.153 description leaf56_Ethernet5
   neighbor 192.168.2.165 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.165 remote-as 65156
   neighbor 192.168.2.165 description leaf57_Ethernet5
   neighbor 192.168.2.177 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.177 remote-as 65157
   neighbor 192.168.2.177 description leaf58_Ethernet5
   neighbor 192.168.2.189 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.189 remote-as 65158
   neighbor 192.168.2.189 description leaf59_Ethernet5
   neighbor 192.168.2.201 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.201 remote-as 65159
   neighbor 192.168.2.201 description leaf60_Ethernet5
   neighbor 192.168.2.213 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.213 remote-as 65160
   neighbor 192.168.2.213 description leaf61_Ethernet5
   neighbor 192.168.2.225 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.225 remote-as 65161
   neighbor 192.168.2.225 description leaf62_Ethernet5
   neighbor 192.168.2.237 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.237 remote-as 65162
   neighbor 192.168.2.237 description leaf63_Ethernet5
   neighbor 192.168.2.249 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.249 remote-as 65163
   neighbor 192.168.2.249 description leaf64_Ethernet5
   neighbor 192.168.3.5 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.5 remote-as 65164
   neighbor 192.168.3.5 description leaf65_Ethernet5
   neighbor 192.168.3.17 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.17 remote-as 65165
   neighbor 192.168.3.17 description leaf66_Ethernet5
   neighbor 192.168.3.29 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.29 remote-as 65166
   neighbor 192.168.3.29 description leaf67_Ethernet5
   neighbor 192.168.3.41 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.41 remote-as 65167
   neighbor 192.168.3.41 description leaf68_Ethernet5
   neighbor 192.168.3.53 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.53 remote-as 65168
   neighbor 192.168.3.53 description leaf69_Ethernet5
   neighbor 192.168.3.65 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.65 remote-as 65169
   neighbor 192.168.3.65 description leaf70_Ethernet5
   neighbor 192.168.3.77 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.77 remote-as 65170
   neighbor 192.168.3.77 description leaf71_Ethernet5
   neighbor 192.168.3.89 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.89 remote-as 65171
   neighbor 192.168.3.89 description leaf72_Ethernet5
   neighbor 192.168.3.101 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.101 remote-as 65172
   neighbor 192.168.3.101 description leaf73_Ethernet5
   neighbor 192.168.3.113 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.113 remote-as 65173
   neighbor 192.168.3.113 description leaf74_Ethernet5
   neighbor 192.168.3.125 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.125 remote-as 65174
   neighbor 192.168.3.125 description leaf75_Ethernet5
   neighbor 192.168.3.137 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.137 remote-as 65175
   neighbor 192.168.3.137 description leaf76_Ethernet5
   neighbor 192.168.3.149 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.149 remote-as 65176
   neighbor 192.168.3.149 description leaf77_Ethernet5
   neighbor 192.168.3.161 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.161 remote-as 65177
   neighbor 192.168.3.161 description leaf78_Ethernet5
   neighbor 192.168.3.173 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.173 remote-as 65178
   neighbor 192.168.3.173 description leaf79_Ethernet5
   neighbor 192.168.3.185 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.185 remote-as 65179
   neighbor 192.168.3.185 description leaf80_Ethernet5
   neighbor 192.168.3.197 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.197 remote-as 65180
   neighbor 192.168.3.197 description leaf81_Ethernet5
   neighbor 192.168.3.209 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.209 remote-as 65181
   neighbor 192.168.3.209 description leaf82_Ethernet5
   neighbor 192.168.3.221 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.221 remote-as 65182
   neighbor 192.168.3.221 description leaf83_Ethernet5
   neighbor 192.168.3.233 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.233 remote-as 65183
   neighbor 192.168.3.233 description leaf84_Ethernet5
   neighbor 192.168.3.245 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.245 remote-as 65184
   neighbor 192.168.3.245 description leaf85_Ethernet5
   neighbor 192.168.4.1 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.1 remote-as 65185
   neighbor 192.168.4.1 description leaf86_Ethernet5
   neighbor 192.168.4.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.13 remote-as 65186
   neighbor 192.168.4.13 description leaf87_Ethernet5
   neighbor 192.168.4.25 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.25 remote-as 65187
   neighbor 192.168.4.25 description leaf88_Ethernet5
   neighbor 192.168.4.37 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.37 remote-as 65188
   neighbor 192.168.4.37 description leaf89_Ethernet5
   neighbor 192.168.4.49 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.49 remote-as 65189
   neighbor 192.168.4.49 description leaf90_Ethernet5
   neighbor 192.168.4.61 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.61 remote-as 65190
   neighbor 192.168.4.61 description leaf91_Ethernet5
   neighbor 192.168.4.73 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.73 remote-as 65191
   neighbor 192.168.4.73 description leaf92_Ethernet5
   neighbor 192.168.4.85 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.85 remote-as 65192
   neighbor 192.168.4.85 description leaf93_Ethernet5
   neighbor 192.168.4.97 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.97 remote-as 65193
   neighbor 192.168.4.97 description leaf94_Ethernet5
   neighbor 192.168.4.109 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.109 remote-as 65194
   neighbor 192.168.4.109 description leaf95_Ethernet5
   neighbor 192.168.4.121 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.121 remote-as 65195
   neighbor 192.168.4.121 description leaf96_Ethernet5
   neighbor 192.168.4.133 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.133 remote-as 65196
   neighbor 192.168.4.133 description leaf97_Ethernet5
   neighbor 192.168.4.145 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.145 remote-as 65197
   neighbor 192.168.4.145 description leaf98_Ethernet5
   neighbor 192.168.4.157 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.157 remote-as 65198
   neighbor 192.168.4.157 description leaf99_Ethernet5
   neighbor 192.168.101.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.1 remote-as 65100
   neighbor 192.168.101.1 description leaf1
   neighbor 192.168.101.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.2 remote-as 65100
   neighbor 192.168.101.2 description leaf2
   neighbor 192.168.101.3 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.3 remote-as 65299
   neighbor 192.168.101.3 description leaf3
   neighbor 192.168.101.4 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.4 remote-as 65299
   neighbor 192.168.101.4 description leaf4
   neighbor 192.168.101.5 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.5 remote-as 65104
   neighbor 192.168.101.5 description leaf5
   neighbor 192.168.101.6 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.6 remote-as 65105
   neighbor 192.168.101.6 description leaf6
   neighbor 192.168.101.7 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.7 remote-as 65106
   neighbor 192.168.101.7 description leaf7
   neighbor 192.168.101.8 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.8 remote-as 65107
   neighbor 192.168.101.8 description leaf8
   neighbor 192.168.101.9 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.9 remote-as 65108
   neighbor 192.168.101.9 description leaf9
   neighbor 192.168.101.10 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.10 remote-as 65109
   neighbor 192.168.101.10 description leaf10
   neighbor 192.168.101.11 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.11 remote-as 65110
   neighbor 192.168.101.11 description leaf11
   neighbor 192.168.101.12 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.12 remote-as 65111
   neighbor 192.168.101.12 description leaf12
   neighbor 192.168.101.13 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.13 remote-as 65112
   neighbor 192.168.101.13 description leaf13
   neighbor 192.168.101.14 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.14 remote-as 65113
   neighbor 192.168.101.14 description leaf14
   neighbor 192.168.101.15 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.15 remote-as 65114
   neighbor 192.168.101.15 description leaf15
   neighbor 192.168.101.16 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.16 remote-as 65115
   neighbor 192.168.101.16 description leaf16
   neighbor 192.168.101.17 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.17 remote-as 65116
   neighbor 192.168.101.17 description leaf17
   neighbor 192.168.101.18 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.18 remote-as 65117
   neighbor 192.168.101.18 description leaf18
   neighbor 192.168.101.19 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.19 remote-as 65118
   neighbor 192.168.101.19 description leaf19
   neighbor 192.168.101.20 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.20 remote-as 65119
   neighbor 192.168.101.20 description leaf20
   neighbor 192.168.101.21 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.21 remote-as 65120
   neighbor 192.168.101.21 description leaf21
   neighbor 192.168.101.22 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.22 remote-as 65121
   neighbor 192.168.101.22 description leaf22
   neighbor 192.168.101.23 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.23 remote-as 65122
   neighbor 192.168.101.23 description leaf23
   neighbor 192.168.101.24 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.24 remote-as 65123
   neighbor 192.168.101.24 description leaf24
   neighbor 192.168.101.25 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.25 remote-as 65124
   neighbor 192.168.101.25 description leaf25
   neighbor 192.168.101.26 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.26 remote-as 65125
   neighbor 192.168.101.26 description leaf26
   neighbor 192.168.101.27 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.27 remote-as 65126
   neighbor 192.168.101.27 description leaf27
   neighbor 192.168.101.28 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.28 remote-as 65127
   neighbor 192.168.101.28 description leaf28
   neighbor 192.168.101.29 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.29 remote-as 65128
   neighbor 192.168.101.29 description leaf29
   neighbor 192.168.101.30 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.30 remote-as 65129
   neighbor 192.168.101.30 description leaf30
   neighbor 192.168.101.31 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.31 remote-as 65130
   neighbor 192.168.101.31 description leaf31
   neighbor 192.168.101.32 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.32 remote-as 65131
   neighbor 192.168.101.32 description leaf32
   neighbor 192.168.101.33 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.33 remote-as 65132
   neighbor 192.168.101.33 description leaf33
   neighbor 192.168.101.34 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.34 remote-as 65133
   neighbor 192.168.101.34 description leaf34
   neighbor 192.168.101.35 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.35 remote-as 65134
   neighbor 192.168.101.35 description leaf35
   neighbor 192.168.101.36 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.36 remote-as 65135
   neighbor 192.168.101.36 description leaf36
   neighbor 192.168.101.37 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.37 remote-as 65136
   neighbor 192.168.101.37 description leaf37
   neighbor 192.168.101.38 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.38 remote-as 65137
   neighbor 192.168.101.38 description leaf38
   neighbor 192.168.101.39 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.39 remote-as 65138
   neighbor 192.168.101.39 description leaf39
   neighbor 192.168.101.40 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.40 remote-as 65139
   neighbor 192.168.101.40 description leaf40
   neighbor 192.168.101.41 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.41 remote-as 65140
   neighbor 192.168.101.41 description leaf41
   neighbor 192.168.101.42 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.42 remote-as 65141
   neighbor 192.168.101.42 description leaf42
   neighbor 192.168.101.43 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.43 remote-as 65142
   neighbor 192.168.101.43 description leaf43
   neighbor 192.168.101.44 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.44 remote-as 65143
   neighbor 192.168.101.44 description leaf44
   neighbor 192.168.101.45 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.45 remote-as 65144
   neighbor 192.168.101.45 description leaf45
   neighbor 192.168.101.46 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.46 remote-as 65145
   neighbor 192.168.101.46 description leaf46
   neighbor 192.168.101.47 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.47 remote-as 65146
   neighbor 192.168.101.47 description leaf47
   neighbor 192.168.101.48 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.48 remote-as 65147
   neighbor 192.168.101.48 description leaf48
   neighbor 192.168.101.49 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.49 remote-as 65148
   neighbor 192.168.101.49 description leaf49
   neighbor 192.168.101.50 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.50 remote-as 65149
   neighbor 192.168.101.50 description leaf50
   neighbor 192.168.101.51 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.51 remote-as 65150
   neighbor 192.168.101.51 description leaf51
   neighbor 192.168.101.52 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.52 remote-as 65151
   neighbor 192.168.101.52 description leaf52
   neighbor 192.168.101.53 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.53 remote-as 65152
   neighbor 192.168.101.53 description leaf53
   neighbor 192.168.101.54 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.54 remote-as 65153
   neighbor 192.168.101.54 description leaf54
   neighbor 192.168.101.55 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.55 remote-as 65154
   neighbor 192.168.101.55 description leaf55
   neighbor 192.168.101.56 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.56 remote-as 65155
   neighbor 192.168.101.56 description leaf56
   neighbor 192.168.101.57 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.57 remote-as 65156
   neighbor 192.168.101.57 description leaf57
   neighbor 192.168.101.58 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.58 remote-as 65157
   neighbor 192.168.101.58 description leaf58
   neighbor 192.168.101.59 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.59 remote-as 65158
   neighbor 192.168.101.59 description leaf59
   neighbor 192.168.101.60 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.60 remote-as 65159
   neighbor 192.168.101.60 description leaf60
   neighbor 192.168.101.61 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.61 remote-as 65160
   neighbor 192.168.101.61 description leaf61
   neighbor 192.168.101.62 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.62 remote-as 65161
   neighbor 192.168.101.62 description leaf62
   neighbor 192.168.101.63 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.63 remote-as 65162
   neighbor 192.168.101.63 description leaf63
   neighbor 192.168.101.64 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.64 remote-as 65163
   neighbor 192.168.101.64 description leaf64
   neighbor 192.168.101.65 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.65 remote-as 65164
   neighbor 192.168.101.65 description leaf65
   neighbor 192.168.101.66 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.66 remote-as 65165
   neighbor 192.168.101.66 description leaf66
   neighbor 192.168.101.67 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.67 remote-as 65166
   neighbor 192.168.101.67 description leaf67
   neighbor 192.168.101.68 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.68 remote-as 65167
   neighbor 192.168.101.68 description leaf68
   neighbor 192.168.101.69 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.69 remote-as 65168
   neighbor 192.168.101.69 description leaf69
   neighbor 192.168.101.70 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.70 remote-as 65169
   neighbor 192.168.101.70 description leaf70
   neighbor 192.168.101.71 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.71 remote-as 65170
   neighbor 192.168.101.71 description leaf71
   neighbor 192.168.101.72 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.72 remote-as 65171
   neighbor 192.168.101.72 description leaf72
   neighbor 192.168.101.73 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.73 remote-as 65172
   neighbor 192.168.101.73 description leaf73
   neighbor 192.168.101.74 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.74 remote-as 65173
   neighbor 192.168.101.74 description leaf74
   neighbor 192.168.101.75 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.75 remote-as 65174
   neighbor 192.168.101.75 description leaf75
   neighbor 192.168.101.76 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.76 remote-as 65175
   neighbor 192.168.101.76 description leaf76
   neighbor 192.168.101.77 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.77 remote-as 65176
   neighbor 192.168.101.77 description leaf77
   neighbor 192.168.101.78 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.78 remote-as 65177
   neighbor 192.168.101.78 description leaf78
   neighbor 192.168.101.79 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.79 remote-as 65178
   neighbor 192.168.101.79 description leaf79
   neighbor 192.168.101.80 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.80 remote-as 65179
   neighbor 192.168.101.80 description leaf80
   neighbor 192.168.101.81 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.81 remote-as 65180
   neighbor 192.168.101.81 description leaf81
   neighbor 192.168.101.82 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.82 remote-as 65181
   neighbor 192.168.101.82 description leaf82
   neighbor 192.168.101.83 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.83 remote-as 65182
   neighbor 192.168.101.83 description leaf83
   neighbor 192.168.101.84 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.84 remote-as 65183
   neighbor 192.168.101.84 description leaf84
   neighbor 192.168.101.85 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.85 remote-as 65184
   neighbor 192.168.101.85 description leaf85
   neighbor 192.168.101.86 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.86 remote-as 65185
   neighbor 192.168.101.86 description leaf86
   neighbor 192.168.101.87 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.87 remote-as 65186
   neighbor 192.168.101.87 description leaf87
   neighbor 192.168.101.88 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.88 remote-as 65187
   neighbor 192.168.101.88 description leaf88
   neighbor 192.168.101.89 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.89 remote-as 65188
   neighbor 192.168.101.89 description leaf89
   neighbor 192.168.101.90 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.90 remote-as 65189
   neighbor 192.168.101.90 description leaf90
   neighbor 192.168.101.91 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.91 remote-as 65190
   neighbor 192.168.101.91 description leaf91
   neighbor 192.168.101.92 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.92 remote-as 65191
   neighbor 192.168.101.92 description leaf92
   neighbor 192.168.101.93 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.93 remote-as 65192
   neighbor 192.168.101.93 description leaf93
   neighbor 192.168.101.94 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.94 remote-as 65193
   neighbor 192.168.101.94 description leaf94
   neighbor 192.168.101.95 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.95 remote-as 65194
   neighbor 192.168.101.95 description leaf95
   neighbor 192.168.101.96 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.96 remote-as 65195
   neighbor 192.168.101.96 description leaf96
   neighbor 192.168.101.97 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.97 remote-as 65196
   neighbor 192.168.101.97 description leaf97
   neighbor 192.168.101.98 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.98 remote-as 65197
   neighbor 192.168.101.98 description leaf98
   neighbor 192.168.101.99 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.101.99 remote-as 65198
   neighbor 192.168.101.99 description leaf99
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.101.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.101.0/24 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```
