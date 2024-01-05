# spine2

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
| Management0 | oob_management | oob | MGMT | 192.168.0.12/24 | 192.168.0.1 |

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
   ip address 192.168.0.12/24
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
| Ethernet3 | P2P_LINK_TO_LEAF1_Ethernet4 | routed | - | 192.168.0.2/31 | default | 1500 | False | - | - |
| Ethernet4 | P2P_LINK_TO_LEAF2_Ethernet4 | routed | - | 192.168.0.14/31 | default | 1500 | False | - | - |
| Ethernet5 | P2P_LINK_TO_LEAF3_Ethernet4 | routed | - | 192.168.0.26/31 | default | 1500 | False | - | - |
| Ethernet6 | P2P_LINK_TO_LEAF4_Ethernet4 | routed | - | 192.168.0.38/31 | default | 1500 | False | - | - |
| Ethernet7 | P2P_LINK_TO_LEAF5_Ethernet4 | routed | - | 192.168.0.50/31 | default | 1500 | False | - | - |
| Ethernet8 | P2P_LINK_TO_LEAF6_Ethernet4 | routed | - | 192.168.0.62/31 | default | 1500 | False | - | - |
| Ethernet9 | P2P_LINK_TO_LEAF7_Ethernet4 | routed | - | 192.168.0.74/31 | default | 1500 | False | - | - |
| Ethernet10 | P2P_LINK_TO_LEAF8_Ethernet4 | routed | - | 192.168.0.86/31 | default | 1500 | False | - | - |
| Ethernet11 | P2P_LINK_TO_LEAF9_Ethernet4 | routed | - | 192.168.0.98/31 | default | 1500 | False | - | - |
| Ethernet12 | P2P_LINK_TO_LEAF10_Ethernet4 | routed | - | 192.168.0.110/31 | default | 1500 | False | - | - |
| Ethernet13 | P2P_LINK_TO_LEAF11_Ethernet4 | routed | - | 192.168.0.122/31 | default | 1500 | False | - | - |
| Ethernet14 | P2P_LINK_TO_LEAF12_Ethernet4 | routed | - | 192.168.0.134/31 | default | 1500 | False | - | - |
| Ethernet15 | P2P_LINK_TO_LEAF13_Ethernet4 | routed | - | 192.168.0.146/31 | default | 1500 | False | - | - |
| Ethernet16 | P2P_LINK_TO_LEAF14_Ethernet4 | routed | - | 192.168.0.158/31 | default | 1500 | False | - | - |
| Ethernet17 | P2P_LINK_TO_LEAF15_Ethernet4 | routed | - | 192.168.0.170/31 | default | 1500 | False | - | - |
| Ethernet18 | P2P_LINK_TO_LEAF16_Ethernet4 | routed | - | 192.168.0.182/31 | default | 1500 | False | - | - |
| Ethernet19 | P2P_LINK_TO_LEAF17_Ethernet4 | routed | - | 192.168.0.194/31 | default | 1500 | False | - | - |
| Ethernet20 | P2P_LINK_TO_LEAF18_Ethernet4 | routed | - | 192.168.0.206/31 | default | 1500 | False | - | - |
| Ethernet21 | P2P_LINK_TO_LEAF19_Ethernet4 | routed | - | 192.168.0.218/31 | default | 1500 | False | - | - |
| Ethernet22 | P2P_LINK_TO_LEAF20_Ethernet4 | routed | - | 192.168.0.230/31 | default | 1500 | False | - | - |
| Ethernet23 | P2P_LINK_TO_LEAF21_Ethernet4 | routed | - | 192.168.0.242/31 | default | 1500 | False | - | - |
| Ethernet24 | P2P_LINK_TO_LEAF22_Ethernet4 | routed | - | 192.168.0.254/31 | default | 1500 | False | - | - |
| Ethernet25 | P2P_LINK_TO_LEAF23_Ethernet4 | routed | - | 192.168.1.10/31 | default | 1500 | False | - | - |
| Ethernet26 | P2P_LINK_TO_LEAF24_Ethernet4 | routed | - | 192.168.1.22/31 | default | 1500 | False | - | - |
| Ethernet27 | P2P_LINK_TO_LEAF25_Ethernet4 | routed | - | 192.168.1.34/31 | default | 1500 | False | - | - |
| Ethernet28 | P2P_LINK_TO_LEAF26_Ethernet4 | routed | - | 192.168.1.46/31 | default | 1500 | False | - | - |
| Ethernet29 | P2P_LINK_TO_LEAF27_Ethernet4 | routed | - | 192.168.1.58/31 | default | 1500 | False | - | - |
| Ethernet30 | P2P_LINK_TO_LEAF28_Ethernet4 | routed | - | 192.168.1.70/31 | default | 1500 | False | - | - |
| Ethernet31 | P2P_LINK_TO_LEAF29_Ethernet4 | routed | - | 192.168.1.82/31 | default | 1500 | False | - | - |
| Ethernet32 | P2P_LINK_TO_LEAF30_Ethernet4 | routed | - | 192.168.1.94/31 | default | 1500 | False | - | - |
| Ethernet33 | P2P_LINK_TO_LEAF31_Ethernet4 | routed | - | 192.168.1.106/31 | default | 1500 | False | - | - |
| Ethernet34 | P2P_LINK_TO_LEAF32_Ethernet4 | routed | - | 192.168.1.118/31 | default | 1500 | False | - | - |
| Ethernet35 | P2P_LINK_TO_LEAF33_Ethernet4 | routed | - | 192.168.1.130/31 | default | 1500 | False | - | - |
| Ethernet36 | P2P_LINK_TO_LEAF34_Ethernet4 | routed | - | 192.168.1.142/31 | default | 1500 | False | - | - |
| Ethernet37 | P2P_LINK_TO_LEAF35_Ethernet4 | routed | - | 192.168.1.154/31 | default | 1500 | False | - | - |
| Ethernet38 | P2P_LINK_TO_LEAF36_Ethernet4 | routed | - | 192.168.1.166/31 | default | 1500 | False | - | - |
| Ethernet39 | P2P_LINK_TO_LEAF37_Ethernet4 | routed | - | 192.168.1.178/31 | default | 1500 | False | - | - |
| Ethernet40 | P2P_LINK_TO_LEAF38_Ethernet4 | routed | - | 192.168.1.190/31 | default | 1500 | False | - | - |
| Ethernet41 | P2P_LINK_TO_LEAF39_Ethernet4 | routed | - | 192.168.1.202/31 | default | 1500 | False | - | - |
| Ethernet42 | P2P_LINK_TO_LEAF40_Ethernet4 | routed | - | 192.168.1.214/31 | default | 1500 | False | - | - |
| Ethernet43 | P2P_LINK_TO_LEAF41_Ethernet4 | routed | - | 192.168.1.226/31 | default | 1500 | False | - | - |
| Ethernet44 | P2P_LINK_TO_LEAF42_Ethernet4 | routed | - | 192.168.1.238/31 | default | 1500 | False | - | - |
| Ethernet45 | P2P_LINK_TO_LEAF43_Ethernet4 | routed | - | 192.168.1.250/31 | default | 1500 | False | - | - |
| Ethernet46 | P2P_LINK_TO_LEAF44_Ethernet4 | routed | - | 192.168.2.6/31 | default | 1500 | False | - | - |
| Ethernet47 | P2P_LINK_TO_LEAF45_Ethernet4 | routed | - | 192.168.2.18/31 | default | 1500 | False | - | - |
| Ethernet48 | P2P_LINK_TO_LEAF46_Ethernet4 | routed | - | 192.168.2.30/31 | default | 1500 | False | - | - |
| Ethernet49 | P2P_LINK_TO_LEAF47_Ethernet4 | routed | - | 192.168.2.42/31 | default | 1500 | False | - | - |
| Ethernet50 | P2P_LINK_TO_LEAF48_Ethernet4 | routed | - | 192.168.2.54/31 | default | 1500 | False | - | - |
| Ethernet51 | P2P_LINK_TO_LEAF49_Ethernet4 | routed | - | 192.168.2.66/31 | default | 1500 | False | - | - |
| Ethernet52 | P2P_LINK_TO_LEAF50_Ethernet4 | routed | - | 192.168.2.78/31 | default | 1500 | False | - | - |
| Ethernet53 | P2P_LINK_TO_LEAF51_Ethernet4 | routed | - | 192.168.2.90/31 | default | 1500 | False | - | - |
| Ethernet54 | P2P_LINK_TO_LEAF52_Ethernet4 | routed | - | 192.168.2.102/31 | default | 1500 | False | - | - |
| Ethernet55 | P2P_LINK_TO_LEAF53_Ethernet4 | routed | - | 192.168.2.114/31 | default | 1500 | False | - | - |
| Ethernet56 | P2P_LINK_TO_LEAF54_Ethernet4 | routed | - | 192.168.2.126/31 | default | 1500 | False | - | - |
| Ethernet57 | P2P_LINK_TO_LEAF55_Ethernet4 | routed | - | 192.168.2.138/31 | default | 1500 | False | - | - |
| Ethernet58 | P2P_LINK_TO_LEAF56_Ethernet4 | routed | - | 192.168.2.150/31 | default | 1500 | False | - | - |
| Ethernet59 | P2P_LINK_TO_LEAF57_Ethernet4 | routed | - | 192.168.2.162/31 | default | 1500 | False | - | - |
| Ethernet60 | P2P_LINK_TO_LEAF58_Ethernet4 | routed | - | 192.168.2.174/31 | default | 1500 | False | - | - |
| Ethernet61 | P2P_LINK_TO_LEAF59_Ethernet4 | routed | - | 192.168.2.186/31 | default | 1500 | False | - | - |
| Ethernet62 | P2P_LINK_TO_LEAF60_Ethernet4 | routed | - | 192.168.2.198/31 | default | 1500 | False | - | - |
| Ethernet63 | P2P_LINK_TO_LEAF61_Ethernet4 | routed | - | 192.168.2.210/31 | default | 1500 | False | - | - |
| Ethernet64 | P2P_LINK_TO_LEAF62_Ethernet4 | routed | - | 192.168.2.222/31 | default | 1500 | False | - | - |
| Ethernet65 | P2P_LINK_TO_LEAF63_Ethernet4 | routed | - | 192.168.2.234/31 | default | 1500 | False | - | - |
| Ethernet66 | P2P_LINK_TO_LEAF64_Ethernet4 | routed | - | 192.168.2.246/31 | default | 1500 | False | - | - |
| Ethernet67 | P2P_LINK_TO_LEAF65_Ethernet4 | routed | - | 192.168.3.2/31 | default | 1500 | False | - | - |
| Ethernet68 | P2P_LINK_TO_LEAF66_Ethernet4 | routed | - | 192.168.3.14/31 | default | 1500 | False | - | - |
| Ethernet69 | P2P_LINK_TO_LEAF67_Ethernet4 | routed | - | 192.168.3.26/31 | default | 1500 | False | - | - |
| Ethernet70 | P2P_LINK_TO_LEAF68_Ethernet4 | routed | - | 192.168.3.38/31 | default | 1500 | False | - | - |
| Ethernet71 | P2P_LINK_TO_LEAF69_Ethernet4 | routed | - | 192.168.3.50/31 | default | 1500 | False | - | - |
| Ethernet72 | P2P_LINK_TO_LEAF70_Ethernet4 | routed | - | 192.168.3.62/31 | default | 1500 | False | - | - |
| Ethernet73 | P2P_LINK_TO_LEAF71_Ethernet4 | routed | - | 192.168.3.74/31 | default | 1500 | False | - | - |
| Ethernet74 | P2P_LINK_TO_LEAF72_Ethernet4 | routed | - | 192.168.3.86/31 | default | 1500 | False | - | - |
| Ethernet75 | P2P_LINK_TO_LEAF73_Ethernet4 | routed | - | 192.168.3.98/31 | default | 1500 | False | - | - |
| Ethernet76 | P2P_LINK_TO_LEAF74_Ethernet4 | routed | - | 192.168.3.110/31 | default | 1500 | False | - | - |
| Ethernet77 | P2P_LINK_TO_LEAF75_Ethernet4 | routed | - | 192.168.3.122/31 | default | 1500 | False | - | - |
| Ethernet78 | P2P_LINK_TO_LEAF76_Ethernet4 | routed | - | 192.168.3.134/31 | default | 1500 | False | - | - |
| Ethernet79 | P2P_LINK_TO_LEAF77_Ethernet4 | routed | - | 192.168.3.146/31 | default | 1500 | False | - | - |
| Ethernet80 | P2P_LINK_TO_LEAF78_Ethernet4 | routed | - | 192.168.3.158/31 | default | 1500 | False | - | - |
| Ethernet81 | P2P_LINK_TO_LEAF79_Ethernet4 | routed | - | 192.168.3.170/31 | default | 1500 | False | - | - |
| Ethernet82 | P2P_LINK_TO_LEAF80_Ethernet4 | routed | - | 192.168.3.182/31 | default | 1500 | False | - | - |
| Ethernet83 | P2P_LINK_TO_LEAF81_Ethernet4 | routed | - | 192.168.3.194/31 | default | 1500 | False | - | - |
| Ethernet84 | P2P_LINK_TO_LEAF82_Ethernet4 | routed | - | 192.168.3.206/31 | default | 1500 | False | - | - |
| Ethernet85 | P2P_LINK_TO_LEAF83_Ethernet4 | routed | - | 192.168.3.218/31 | default | 1500 | False | - | - |
| Ethernet86 | P2P_LINK_TO_LEAF84_Ethernet4 | routed | - | 192.168.3.230/31 | default | 1500 | False | - | - |
| Ethernet87 | P2P_LINK_TO_LEAF85_Ethernet4 | routed | - | 192.168.3.242/31 | default | 1500 | False | - | - |
| Ethernet88 | P2P_LINK_TO_LEAF86_Ethernet4 | routed | - | 192.168.3.254/31 | default | 1500 | False | - | - |
| Ethernet89 | P2P_LINK_TO_LEAF87_Ethernet4 | routed | - | 192.168.4.10/31 | default | 1500 | False | - | - |
| Ethernet90 | P2P_LINK_TO_LEAF88_Ethernet4 | routed | - | 192.168.4.22/31 | default | 1500 | False | - | - |
| Ethernet91 | P2P_LINK_TO_LEAF89_Ethernet4 | routed | - | 192.168.4.34/31 | default | 1500 | False | - | - |
| Ethernet92 | P2P_LINK_TO_LEAF90_Ethernet4 | routed | - | 192.168.4.46/31 | default | 1500 | False | - | - |
| Ethernet93 | P2P_LINK_TO_LEAF91_Ethernet4 | routed | - | 192.168.4.58/31 | default | 1500 | False | - | - |
| Ethernet94 | P2P_LINK_TO_LEAF92_Ethernet4 | routed | - | 192.168.4.70/31 | default | 1500 | False | - | - |
| Ethernet95 | P2P_LINK_TO_LEAF93_Ethernet4 | routed | - | 192.168.4.82/31 | default | 1500 | False | - | - |
| Ethernet96 | P2P_LINK_TO_LEAF94_Ethernet4 | routed | - | 192.168.4.94/31 | default | 1500 | False | - | - |
| Ethernet97 | P2P_LINK_TO_LEAF95_Ethernet4 | routed | - | 192.168.4.106/31 | default | 1500 | False | - | - |
| Ethernet98 | P2P_LINK_TO_LEAF96_Ethernet4 | routed | - | 192.168.4.118/31 | default | 1500 | False | - | - |
| Ethernet99 | P2P_LINK_TO_LEAF97_Ethernet4 | routed | - | 192.168.4.130/31 | default | 1500 | False | - | - |
| Ethernet100 | P2P_LINK_TO_LEAF98_Ethernet4 | routed | - | 192.168.4.142/31 | default | 1500 | False | - | - |
| Ethernet101 | P2P_LINK_TO_LEAF99_Ethernet4 | routed | - | 192.168.4.154/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description P2P_LINK_TO_LEAF1_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.2/31
!
interface Ethernet4
   description P2P_LINK_TO_LEAF2_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.14/31
!
interface Ethernet5
   description P2P_LINK_TO_LEAF3_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.26/31
!
interface Ethernet6
   description P2P_LINK_TO_LEAF4_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.38/31
!
interface Ethernet7
   description P2P_LINK_TO_LEAF5_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.50/31
!
interface Ethernet8
   description P2P_LINK_TO_LEAF6_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.62/31
!
interface Ethernet9
   description P2P_LINK_TO_LEAF7_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.74/31
!
interface Ethernet10
   description P2P_LINK_TO_LEAF8_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.86/31
!
interface Ethernet11
   description P2P_LINK_TO_LEAF9_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.98/31
!
interface Ethernet12
   description P2P_LINK_TO_LEAF10_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.110/31
!
interface Ethernet13
   description P2P_LINK_TO_LEAF11_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.122/31
!
interface Ethernet14
   description P2P_LINK_TO_LEAF12_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.134/31
!
interface Ethernet15
   description P2P_LINK_TO_LEAF13_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.146/31
!
interface Ethernet16
   description P2P_LINK_TO_LEAF14_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.158/31
!
interface Ethernet17
   description P2P_LINK_TO_LEAF15_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.170/31
!
interface Ethernet18
   description P2P_LINK_TO_LEAF16_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.182/31
!
interface Ethernet19
   description P2P_LINK_TO_LEAF17_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.194/31
!
interface Ethernet20
   description P2P_LINK_TO_LEAF18_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.206/31
!
interface Ethernet21
   description P2P_LINK_TO_LEAF19_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.218/31
!
interface Ethernet22
   description P2P_LINK_TO_LEAF20_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.230/31
!
interface Ethernet23
   description P2P_LINK_TO_LEAF21_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.242/31
!
interface Ethernet24
   description P2P_LINK_TO_LEAF22_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.0.254/31
!
interface Ethernet25
   description P2P_LINK_TO_LEAF23_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.10/31
!
interface Ethernet26
   description P2P_LINK_TO_LEAF24_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.22/31
!
interface Ethernet27
   description P2P_LINK_TO_LEAF25_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.34/31
!
interface Ethernet28
   description P2P_LINK_TO_LEAF26_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.46/31
!
interface Ethernet29
   description P2P_LINK_TO_LEAF27_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.58/31
!
interface Ethernet30
   description P2P_LINK_TO_LEAF28_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.70/31
!
interface Ethernet31
   description P2P_LINK_TO_LEAF29_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.82/31
!
interface Ethernet32
   description P2P_LINK_TO_LEAF30_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.94/31
!
interface Ethernet33
   description P2P_LINK_TO_LEAF31_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.106/31
!
interface Ethernet34
   description P2P_LINK_TO_LEAF32_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.118/31
!
interface Ethernet35
   description P2P_LINK_TO_LEAF33_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.130/31
!
interface Ethernet36
   description P2P_LINK_TO_LEAF34_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.142/31
!
interface Ethernet37
   description P2P_LINK_TO_LEAF35_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.154/31
!
interface Ethernet38
   description P2P_LINK_TO_LEAF36_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.166/31
!
interface Ethernet39
   description P2P_LINK_TO_LEAF37_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.178/31
!
interface Ethernet40
   description P2P_LINK_TO_LEAF38_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.190/31
!
interface Ethernet41
   description P2P_LINK_TO_LEAF39_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.202/31
!
interface Ethernet42
   description P2P_LINK_TO_LEAF40_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.214/31
!
interface Ethernet43
   description P2P_LINK_TO_LEAF41_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.226/31
!
interface Ethernet44
   description P2P_LINK_TO_LEAF42_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.238/31
!
interface Ethernet45
   description P2P_LINK_TO_LEAF43_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.250/31
!
interface Ethernet46
   description P2P_LINK_TO_LEAF44_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.6/31
!
interface Ethernet47
   description P2P_LINK_TO_LEAF45_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.18/31
!
interface Ethernet48
   description P2P_LINK_TO_LEAF46_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.30/31
!
interface Ethernet49
   description P2P_LINK_TO_LEAF47_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.42/31
!
interface Ethernet50
   description P2P_LINK_TO_LEAF48_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.54/31
!
interface Ethernet51
   description P2P_LINK_TO_LEAF49_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.66/31
!
interface Ethernet52
   description P2P_LINK_TO_LEAF50_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.78/31
!
interface Ethernet53
   description P2P_LINK_TO_LEAF51_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.90/31
!
interface Ethernet54
   description P2P_LINK_TO_LEAF52_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.102/31
!
interface Ethernet55
   description P2P_LINK_TO_LEAF53_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.114/31
!
interface Ethernet56
   description P2P_LINK_TO_LEAF54_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.126/31
!
interface Ethernet57
   description P2P_LINK_TO_LEAF55_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.138/31
!
interface Ethernet58
   description P2P_LINK_TO_LEAF56_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.150/31
!
interface Ethernet59
   description P2P_LINK_TO_LEAF57_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.162/31
!
interface Ethernet60
   description P2P_LINK_TO_LEAF58_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.174/31
!
interface Ethernet61
   description P2P_LINK_TO_LEAF59_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.186/31
!
interface Ethernet62
   description P2P_LINK_TO_LEAF60_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.198/31
!
interface Ethernet63
   description P2P_LINK_TO_LEAF61_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.210/31
!
interface Ethernet64
   description P2P_LINK_TO_LEAF62_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.222/31
!
interface Ethernet65
   description P2P_LINK_TO_LEAF63_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.234/31
!
interface Ethernet66
   description P2P_LINK_TO_LEAF64_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.2.246/31
!
interface Ethernet67
   description P2P_LINK_TO_LEAF65_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.2/31
!
interface Ethernet68
   description P2P_LINK_TO_LEAF66_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.14/31
!
interface Ethernet69
   description P2P_LINK_TO_LEAF67_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.26/31
!
interface Ethernet70
   description P2P_LINK_TO_LEAF68_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.38/31
!
interface Ethernet71
   description P2P_LINK_TO_LEAF69_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.50/31
!
interface Ethernet72
   description P2P_LINK_TO_LEAF70_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.62/31
!
interface Ethernet73
   description P2P_LINK_TO_LEAF71_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.74/31
!
interface Ethernet74
   description P2P_LINK_TO_LEAF72_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.86/31
!
interface Ethernet75
   description P2P_LINK_TO_LEAF73_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.98/31
!
interface Ethernet76
   description P2P_LINK_TO_LEAF74_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.110/31
!
interface Ethernet77
   description P2P_LINK_TO_LEAF75_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.122/31
!
interface Ethernet78
   description P2P_LINK_TO_LEAF76_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.134/31
!
interface Ethernet79
   description P2P_LINK_TO_LEAF77_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.146/31
!
interface Ethernet80
   description P2P_LINK_TO_LEAF78_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.158/31
!
interface Ethernet81
   description P2P_LINK_TO_LEAF79_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.170/31
!
interface Ethernet82
   description P2P_LINK_TO_LEAF80_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.182/31
!
interface Ethernet83
   description P2P_LINK_TO_LEAF81_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.194/31
!
interface Ethernet84
   description P2P_LINK_TO_LEAF82_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.206/31
!
interface Ethernet85
   description P2P_LINK_TO_LEAF83_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.218/31
!
interface Ethernet86
   description P2P_LINK_TO_LEAF84_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.230/31
!
interface Ethernet87
   description P2P_LINK_TO_LEAF85_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.242/31
!
interface Ethernet88
   description P2P_LINK_TO_LEAF86_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.3.254/31
!
interface Ethernet89
   description P2P_LINK_TO_LEAF87_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.10/31
!
interface Ethernet90
   description P2P_LINK_TO_LEAF88_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.22/31
!
interface Ethernet91
   description P2P_LINK_TO_LEAF89_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.34/31
!
interface Ethernet92
   description P2P_LINK_TO_LEAF90_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.46/31
!
interface Ethernet93
   description P2P_LINK_TO_LEAF91_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.58/31
!
interface Ethernet94
   description P2P_LINK_TO_LEAF92_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.70/31
!
interface Ethernet95
   description P2P_LINK_TO_LEAF93_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.82/31
!
interface Ethernet96
   description P2P_LINK_TO_LEAF94_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.94/31
!
interface Ethernet97
   description P2P_LINK_TO_LEAF95_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.106/31
!
interface Ethernet98
   description P2P_LINK_TO_LEAF96_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.118/31
!
interface Ethernet99
   description P2P_LINK_TO_LEAF97_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.130/31
!
interface Ethernet100
   description P2P_LINK_TO_LEAF98_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.142/31
!
interface Ethernet101
   description P2P_LINK_TO_LEAF99_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.4.154/31
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.101.12/32 |

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
   ip address 192.168.101.12/32
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
| 65001|  192.168.101.12 |

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
| 192.168.0.3 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.15 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.27 | 65299 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.39 | 65299 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.51 | 65104 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.63 | 65105 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.75 | 65106 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.87 | 65107 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.99 | 65108 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.111 | 65109 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.123 | 65110 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.135 | 65111 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.147 | 65112 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.159 | 65113 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.171 | 65114 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.183 | 65115 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.195 | 65116 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.207 | 65117 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.219 | 65118 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.231 | 65119 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.243 | 65120 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.0.255 | 65121 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.11 | 65122 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.23 | 65123 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.35 | 65124 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.47 | 65125 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.59 | 65126 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.71 | 65127 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.83 | 65128 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.95 | 65129 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.107 | 65130 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.119 | 65131 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.131 | 65132 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.143 | 65133 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.155 | 65134 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.167 | 65135 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.179 | 65136 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.191 | 65137 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.203 | 65138 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.215 | 65139 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.227 | 65140 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.239 | 65141 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.1.251 | 65142 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.7 | 65143 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.19 | 65144 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.31 | 65145 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.43 | 65146 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.55 | 65147 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.67 | 65148 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.79 | 65149 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.91 | 65150 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.103 | 65151 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.115 | 65152 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.127 | 65153 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.139 | 65154 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.151 | 65155 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.163 | 65156 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.175 | 65157 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.187 | 65158 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.199 | 65159 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.211 | 65160 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.223 | 65161 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.235 | 65162 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.2.247 | 65163 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.3 | 65164 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.15 | 65165 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.27 | 65166 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.39 | 65167 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.51 | 65168 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.63 | 65169 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.75 | 65170 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.87 | 65171 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.99 | 65172 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.111 | 65173 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.123 | 65174 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.135 | 65175 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.147 | 65176 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.159 | 65177 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.171 | 65178 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.183 | 65179 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.195 | 65180 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.207 | 65181 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.219 | 65182 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.231 | 65183 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.243 | 65184 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.3.255 | 65185 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.11 | 65186 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.23 | 65187 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.35 | 65188 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.47 | 65189 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.59 | 65190 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.71 | 65191 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.83 | 65192 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.95 | 65193 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.107 | 65194 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.119 | 65195 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.131 | 65196 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.143 | 65197 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
| 192.168.4.155 | 65198 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - |
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
   router-id 192.168.101.12
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
   neighbor 192.168.0.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.3 remote-as 65100
   neighbor 192.168.0.3 description leaf1_Ethernet4
   neighbor 192.168.0.15 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.15 remote-as 65100
   neighbor 192.168.0.15 description leaf2_Ethernet4
   neighbor 192.168.0.27 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.27 remote-as 65299
   neighbor 192.168.0.27 description leaf3_Ethernet4
   neighbor 192.168.0.39 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.39 remote-as 65299
   neighbor 192.168.0.39 description leaf4_Ethernet4
   neighbor 192.168.0.51 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.51 remote-as 65104
   neighbor 192.168.0.51 description leaf5_Ethernet4
   neighbor 192.168.0.63 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.63 remote-as 65105
   neighbor 192.168.0.63 description leaf6_Ethernet4
   neighbor 192.168.0.75 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.75 remote-as 65106
   neighbor 192.168.0.75 description leaf7_Ethernet4
   neighbor 192.168.0.87 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.87 remote-as 65107
   neighbor 192.168.0.87 description leaf8_Ethernet4
   neighbor 192.168.0.99 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.99 remote-as 65108
   neighbor 192.168.0.99 description leaf9_Ethernet4
   neighbor 192.168.0.111 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.111 remote-as 65109
   neighbor 192.168.0.111 description leaf10_Ethernet4
   neighbor 192.168.0.123 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.123 remote-as 65110
   neighbor 192.168.0.123 description leaf11_Ethernet4
   neighbor 192.168.0.135 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.135 remote-as 65111
   neighbor 192.168.0.135 description leaf12_Ethernet4
   neighbor 192.168.0.147 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.147 remote-as 65112
   neighbor 192.168.0.147 description leaf13_Ethernet4
   neighbor 192.168.0.159 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.159 remote-as 65113
   neighbor 192.168.0.159 description leaf14_Ethernet4
   neighbor 192.168.0.171 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.171 remote-as 65114
   neighbor 192.168.0.171 description leaf15_Ethernet4
   neighbor 192.168.0.183 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.183 remote-as 65115
   neighbor 192.168.0.183 description leaf16_Ethernet4
   neighbor 192.168.0.195 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.195 remote-as 65116
   neighbor 192.168.0.195 description leaf17_Ethernet4
   neighbor 192.168.0.207 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.207 remote-as 65117
   neighbor 192.168.0.207 description leaf18_Ethernet4
   neighbor 192.168.0.219 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.219 remote-as 65118
   neighbor 192.168.0.219 description leaf19_Ethernet4
   neighbor 192.168.0.231 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.231 remote-as 65119
   neighbor 192.168.0.231 description leaf20_Ethernet4
   neighbor 192.168.0.243 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.243 remote-as 65120
   neighbor 192.168.0.243 description leaf21_Ethernet4
   neighbor 192.168.0.255 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.0.255 remote-as 65121
   neighbor 192.168.0.255 description leaf22_Ethernet4
   neighbor 192.168.1.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.11 remote-as 65122
   neighbor 192.168.1.11 description leaf23_Ethernet4
   neighbor 192.168.1.23 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.23 remote-as 65123
   neighbor 192.168.1.23 description leaf24_Ethernet4
   neighbor 192.168.1.35 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.35 remote-as 65124
   neighbor 192.168.1.35 description leaf25_Ethernet4
   neighbor 192.168.1.47 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.47 remote-as 65125
   neighbor 192.168.1.47 description leaf26_Ethernet4
   neighbor 192.168.1.59 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.59 remote-as 65126
   neighbor 192.168.1.59 description leaf27_Ethernet4
   neighbor 192.168.1.71 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.71 remote-as 65127
   neighbor 192.168.1.71 description leaf28_Ethernet4
   neighbor 192.168.1.83 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.83 remote-as 65128
   neighbor 192.168.1.83 description leaf29_Ethernet4
   neighbor 192.168.1.95 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.95 remote-as 65129
   neighbor 192.168.1.95 description leaf30_Ethernet4
   neighbor 192.168.1.107 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.107 remote-as 65130
   neighbor 192.168.1.107 description leaf31_Ethernet4
   neighbor 192.168.1.119 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.119 remote-as 65131
   neighbor 192.168.1.119 description leaf32_Ethernet4
   neighbor 192.168.1.131 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.131 remote-as 65132
   neighbor 192.168.1.131 description leaf33_Ethernet4
   neighbor 192.168.1.143 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.143 remote-as 65133
   neighbor 192.168.1.143 description leaf34_Ethernet4
   neighbor 192.168.1.155 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.155 remote-as 65134
   neighbor 192.168.1.155 description leaf35_Ethernet4
   neighbor 192.168.1.167 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.167 remote-as 65135
   neighbor 192.168.1.167 description leaf36_Ethernet4
   neighbor 192.168.1.179 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.179 remote-as 65136
   neighbor 192.168.1.179 description leaf37_Ethernet4
   neighbor 192.168.1.191 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.191 remote-as 65137
   neighbor 192.168.1.191 description leaf38_Ethernet4
   neighbor 192.168.1.203 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.203 remote-as 65138
   neighbor 192.168.1.203 description leaf39_Ethernet4
   neighbor 192.168.1.215 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.215 remote-as 65139
   neighbor 192.168.1.215 description leaf40_Ethernet4
   neighbor 192.168.1.227 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.227 remote-as 65140
   neighbor 192.168.1.227 description leaf41_Ethernet4
   neighbor 192.168.1.239 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.239 remote-as 65141
   neighbor 192.168.1.239 description leaf42_Ethernet4
   neighbor 192.168.1.251 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.1.251 remote-as 65142
   neighbor 192.168.1.251 description leaf43_Ethernet4
   neighbor 192.168.2.7 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.7 remote-as 65143
   neighbor 192.168.2.7 description leaf44_Ethernet4
   neighbor 192.168.2.19 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.19 remote-as 65144
   neighbor 192.168.2.19 description leaf45_Ethernet4
   neighbor 192.168.2.31 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.31 remote-as 65145
   neighbor 192.168.2.31 description leaf46_Ethernet4
   neighbor 192.168.2.43 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.43 remote-as 65146
   neighbor 192.168.2.43 description leaf47_Ethernet4
   neighbor 192.168.2.55 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.55 remote-as 65147
   neighbor 192.168.2.55 description leaf48_Ethernet4
   neighbor 192.168.2.67 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.67 remote-as 65148
   neighbor 192.168.2.67 description leaf49_Ethernet4
   neighbor 192.168.2.79 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.79 remote-as 65149
   neighbor 192.168.2.79 description leaf50_Ethernet4
   neighbor 192.168.2.91 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.91 remote-as 65150
   neighbor 192.168.2.91 description leaf51_Ethernet4
   neighbor 192.168.2.103 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.103 remote-as 65151
   neighbor 192.168.2.103 description leaf52_Ethernet4
   neighbor 192.168.2.115 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.115 remote-as 65152
   neighbor 192.168.2.115 description leaf53_Ethernet4
   neighbor 192.168.2.127 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.127 remote-as 65153
   neighbor 192.168.2.127 description leaf54_Ethernet4
   neighbor 192.168.2.139 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.139 remote-as 65154
   neighbor 192.168.2.139 description leaf55_Ethernet4
   neighbor 192.168.2.151 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.151 remote-as 65155
   neighbor 192.168.2.151 description leaf56_Ethernet4
   neighbor 192.168.2.163 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.163 remote-as 65156
   neighbor 192.168.2.163 description leaf57_Ethernet4
   neighbor 192.168.2.175 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.175 remote-as 65157
   neighbor 192.168.2.175 description leaf58_Ethernet4
   neighbor 192.168.2.187 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.187 remote-as 65158
   neighbor 192.168.2.187 description leaf59_Ethernet4
   neighbor 192.168.2.199 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.199 remote-as 65159
   neighbor 192.168.2.199 description leaf60_Ethernet4
   neighbor 192.168.2.211 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.211 remote-as 65160
   neighbor 192.168.2.211 description leaf61_Ethernet4
   neighbor 192.168.2.223 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.223 remote-as 65161
   neighbor 192.168.2.223 description leaf62_Ethernet4
   neighbor 192.168.2.235 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.235 remote-as 65162
   neighbor 192.168.2.235 description leaf63_Ethernet4
   neighbor 192.168.2.247 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.2.247 remote-as 65163
   neighbor 192.168.2.247 description leaf64_Ethernet4
   neighbor 192.168.3.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.3 remote-as 65164
   neighbor 192.168.3.3 description leaf65_Ethernet4
   neighbor 192.168.3.15 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.15 remote-as 65165
   neighbor 192.168.3.15 description leaf66_Ethernet4
   neighbor 192.168.3.27 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.27 remote-as 65166
   neighbor 192.168.3.27 description leaf67_Ethernet4
   neighbor 192.168.3.39 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.39 remote-as 65167
   neighbor 192.168.3.39 description leaf68_Ethernet4
   neighbor 192.168.3.51 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.51 remote-as 65168
   neighbor 192.168.3.51 description leaf69_Ethernet4
   neighbor 192.168.3.63 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.63 remote-as 65169
   neighbor 192.168.3.63 description leaf70_Ethernet4
   neighbor 192.168.3.75 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.75 remote-as 65170
   neighbor 192.168.3.75 description leaf71_Ethernet4
   neighbor 192.168.3.87 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.87 remote-as 65171
   neighbor 192.168.3.87 description leaf72_Ethernet4
   neighbor 192.168.3.99 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.99 remote-as 65172
   neighbor 192.168.3.99 description leaf73_Ethernet4
   neighbor 192.168.3.111 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.111 remote-as 65173
   neighbor 192.168.3.111 description leaf74_Ethernet4
   neighbor 192.168.3.123 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.123 remote-as 65174
   neighbor 192.168.3.123 description leaf75_Ethernet4
   neighbor 192.168.3.135 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.135 remote-as 65175
   neighbor 192.168.3.135 description leaf76_Ethernet4
   neighbor 192.168.3.147 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.147 remote-as 65176
   neighbor 192.168.3.147 description leaf77_Ethernet4
   neighbor 192.168.3.159 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.159 remote-as 65177
   neighbor 192.168.3.159 description leaf78_Ethernet4
   neighbor 192.168.3.171 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.171 remote-as 65178
   neighbor 192.168.3.171 description leaf79_Ethernet4
   neighbor 192.168.3.183 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.183 remote-as 65179
   neighbor 192.168.3.183 description leaf80_Ethernet4
   neighbor 192.168.3.195 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.195 remote-as 65180
   neighbor 192.168.3.195 description leaf81_Ethernet4
   neighbor 192.168.3.207 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.207 remote-as 65181
   neighbor 192.168.3.207 description leaf82_Ethernet4
   neighbor 192.168.3.219 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.219 remote-as 65182
   neighbor 192.168.3.219 description leaf83_Ethernet4
   neighbor 192.168.3.231 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.231 remote-as 65183
   neighbor 192.168.3.231 description leaf84_Ethernet4
   neighbor 192.168.3.243 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.243 remote-as 65184
   neighbor 192.168.3.243 description leaf85_Ethernet4
   neighbor 192.168.3.255 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.3.255 remote-as 65185
   neighbor 192.168.3.255 description leaf86_Ethernet4
   neighbor 192.168.4.11 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.11 remote-as 65186
   neighbor 192.168.4.11 description leaf87_Ethernet4
   neighbor 192.168.4.23 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.23 remote-as 65187
   neighbor 192.168.4.23 description leaf88_Ethernet4
   neighbor 192.168.4.35 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.35 remote-as 65188
   neighbor 192.168.4.35 description leaf89_Ethernet4
   neighbor 192.168.4.47 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.47 remote-as 65189
   neighbor 192.168.4.47 description leaf90_Ethernet4
   neighbor 192.168.4.59 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.59 remote-as 65190
   neighbor 192.168.4.59 description leaf91_Ethernet4
   neighbor 192.168.4.71 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.71 remote-as 65191
   neighbor 192.168.4.71 description leaf92_Ethernet4
   neighbor 192.168.4.83 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.83 remote-as 65192
   neighbor 192.168.4.83 description leaf93_Ethernet4
   neighbor 192.168.4.95 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.95 remote-as 65193
   neighbor 192.168.4.95 description leaf94_Ethernet4
   neighbor 192.168.4.107 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.107 remote-as 65194
   neighbor 192.168.4.107 description leaf95_Ethernet4
   neighbor 192.168.4.119 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.119 remote-as 65195
   neighbor 192.168.4.119 description leaf96_Ethernet4
   neighbor 192.168.4.131 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.131 remote-as 65196
   neighbor 192.168.4.131 description leaf97_Ethernet4
   neighbor 192.168.4.143 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.143 remote-as 65197
   neighbor 192.168.4.143 description leaf98_Ethernet4
   neighbor 192.168.4.155 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.4.155 remote-as 65198
   neighbor 192.168.4.155 description leaf99_Ethernet4
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
