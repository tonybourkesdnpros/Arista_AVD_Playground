# FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | l3leaf | leaf1 | 192.168.0.21/24 | - | Provisioned | - |
| FABRIC | l3leaf | leaf2 | 192.168.0.22/24 | - | Provisioned | - |
| FABRIC | l3leaf | leaf3 | 192.168.0.23/24 | - | Provisioned | - |
| FABRIC | l3leaf | leaf4 | 192.168.0.24/24 | - | Provisioned | - |
| FABRIC | l3leaf | leaf5 | 192.168.0.25/24 | - | Provisioned | - |
| FABRIC | l3leaf | leaf6 | 192.168.0.106 | - | Provisioned | - |
| FABRIC | l3leaf | leaf7 | 192.168.0.107 | - | Provisioned | - |
| FABRIC | l3leaf | leaf8 | 192.168.0.108 | - | Provisioned | - |
| FABRIC | l3leaf | leaf9 | 192.168.0.109 | - | Provisioned | - |
| FABRIC | l3leaf | leaf10 | 192.168.0.110 | - | Provisioned | - |
| FABRIC | l3leaf | leaf11 | 192.168.0.111 | - | Provisioned | - |
| FABRIC | l3leaf | leaf12 | 192.168.0.112 | - | Provisioned | - |
| FABRIC | l3leaf | leaf13 | 192.168.0.113 | - | Provisioned | - |
| FABRIC | l3leaf | leaf14 | 192.168.0.114 | - | Provisioned | - |
| FABRIC | l3leaf | leaf15 | 192.168.0.115 | - | Provisioned | - |
| FABRIC | l3leaf | leaf16 | 192.168.0.116 | - | Provisioned | - |
| FABRIC | l3leaf | leaf17 | 192.168.0.117 | - | Provisioned | - |
| FABRIC | l3leaf | leaf18 | 192.168.0.118 | - | Provisioned | - |
| FABRIC | l3leaf | leaf19 | 192.168.0.119 | - | Provisioned | - |
| FABRIC | l3leaf | leaf20 | 192.168.0.120 | - | Provisioned | - |
| FABRIC | l3leaf | leaf21 | 192.168.0.121 | - | Provisioned | - |
| FABRIC | l3leaf | leaf22 | 192.168.0.122 | - | Provisioned | - |
| FABRIC | l3leaf | leaf23 | 192.168.0.123 | - | Provisioned | - |
| FABRIC | l3leaf | leaf24 | 192.168.0.124 | - | Provisioned | - |
| FABRIC | l3leaf | leaf25 | 192.168.0.125 | - | Provisioned | - |
| FABRIC | l3leaf | leaf26 | 192.168.0.126 | - | Provisioned | - |
| FABRIC | l3leaf | leaf27 | 192.168.0.127 | - | Provisioned | - |
| FABRIC | l3leaf | leaf28 | 192.168.0.128 | - | Provisioned | - |
| FABRIC | l3leaf | leaf29 | 192.168.0.129 | - | Provisioned | - |
| FABRIC | l3leaf | leaf30 | 192.168.0.130 | - | Provisioned | - |
| FABRIC | l3leaf | leaf31 | 192.168.0.131 | - | Provisioned | - |
| FABRIC | l3leaf | leaf32 | 192.168.0.132 | - | Provisioned | - |
| FABRIC | l3leaf | leaf33 | 192.168.0.133 | - | Provisioned | - |
| FABRIC | l3leaf | leaf34 | 192.168.0.134 | - | Provisioned | - |
| FABRIC | l3leaf | leaf35 | 192.168.0.135 | - | Provisioned | - |
| FABRIC | l3leaf | leaf36 | 192.168.0.136 | - | Provisioned | - |
| FABRIC | l3leaf | leaf37 | 192.168.0.137 | - | Provisioned | - |
| FABRIC | l3leaf | leaf38 | 192.168.0.138 | - | Provisioned | - |
| FABRIC | l3leaf | leaf39 | 192.168.0.139 | - | Provisioned | - |
| FABRIC | l3leaf | leaf40 | 192.168.0.140 | - | Provisioned | - |
| FABRIC | l3leaf | leaf41 | 192.168.0.141 | - | Provisioned | - |
| FABRIC | l3leaf | leaf42 | 192.168.0.142 | - | Provisioned | - |
| FABRIC | l3leaf | leaf43 | 192.168.0.143 | - | Provisioned | - |
| FABRIC | l3leaf | leaf44 | 192.168.0.144 | - | Provisioned | - |
| FABRIC | l3leaf | leaf45 | 192.168.0.145 | - | Provisioned | - |
| FABRIC | l3leaf | leaf46 | 192.168.0.146 | - | Provisioned | - |
| FABRIC | l3leaf | leaf47 | 192.168.0.147 | - | Provisioned | - |
| FABRIC | l3leaf | leaf48 | 192.168.0.148 | - | Provisioned | - |
| FABRIC | l3leaf | leaf49 | 192.168.0.149 | - | Provisioned | - |
| FABRIC | l3leaf | leaf50 | 192.168.0.150 | - | Provisioned | - |
| FABRIC | l3leaf | leaf51 | 192.168.0.151 | - | Provisioned | - |
| FABRIC | l3leaf | leaf52 | 192.168.0.152 | - | Provisioned | - |
| FABRIC | l3leaf | leaf53 | 192.168.0.153 | - | Provisioned | - |
| FABRIC | l3leaf | leaf54 | 192.168.0.154 | - | Provisioned | - |
| FABRIC | l3leaf | leaf55 | 192.168.0.155 | - | Provisioned | - |
| FABRIC | l3leaf | leaf56 | 192.168.0.156 | - | Provisioned | - |
| FABRIC | l3leaf | leaf57 | 192.168.0.157 | - | Provisioned | - |
| FABRIC | l3leaf | leaf58 | 192.168.0.158 | - | Provisioned | - |
| FABRIC | l3leaf | leaf59 | 192.168.0.159 | - | Provisioned | - |
| FABRIC | l3leaf | leaf60 | 192.168.0.160 | - | Provisioned | - |
| FABRIC | l3leaf | leaf61 | 192.168.0.161 | - | Provisioned | - |
| FABRIC | l3leaf | leaf62 | 192.168.0.162 | - | Provisioned | - |
| FABRIC | l3leaf | leaf63 | 192.168.0.163 | - | Provisioned | - |
| FABRIC | l3leaf | leaf64 | 192.168.0.164 | - | Provisioned | - |
| FABRIC | l3leaf | leaf65 | 192.168.0.165 | - | Provisioned | - |
| FABRIC | l3leaf | leaf66 | 192.168.0.166 | - | Provisioned | - |
| FABRIC | l3leaf | leaf67 | 192.168.0.167 | - | Provisioned | - |
| FABRIC | l3leaf | leaf68 | 192.168.0.168 | - | Provisioned | - |
| FABRIC | l3leaf | leaf69 | 192.168.0.169 | - | Provisioned | - |
| FABRIC | l3leaf | leaf70 | 192.168.0.170 | - | Provisioned | - |
| FABRIC | l3leaf | leaf71 | 192.168.0.171 | - | Provisioned | - |
| FABRIC | l3leaf | leaf72 | 192.168.0.172 | - | Provisioned | - |
| FABRIC | l3leaf | leaf73 | 192.168.0.173 | - | Provisioned | - |
| FABRIC | l3leaf | leaf74 | 192.168.0.174 | - | Provisioned | - |
| FABRIC | l3leaf | leaf75 | 192.168.0.175 | - | Provisioned | - |
| FABRIC | l3leaf | leaf76 | 192.168.0.176 | - | Provisioned | - |
| FABRIC | l3leaf | leaf77 | 192.168.0.177 | - | Provisioned | - |
| FABRIC | l3leaf | leaf78 | 192.168.0.178 | - | Provisioned | - |
| FABRIC | l3leaf | leaf79 | 192.168.0.179 | - | Provisioned | - |
| FABRIC | l3leaf | leaf80 | 192.168.0.180 | - | Provisioned | - |
| FABRIC | l3leaf | leaf81 | 192.168.0.181 | - | Provisioned | - |
| FABRIC | l3leaf | leaf82 | 192.168.0.182 | - | Provisioned | - |
| FABRIC | l3leaf | leaf83 | 192.168.0.183 | - | Provisioned | - |
| FABRIC | l3leaf | leaf84 | 192.168.0.184 | - | Provisioned | - |
| FABRIC | l3leaf | leaf85 | 192.168.0.185 | - | Provisioned | - |
| FABRIC | l3leaf | leaf86 | 192.168.0.186 | - | Provisioned | - |
| FABRIC | l3leaf | leaf87 | 192.168.0.187 | - | Provisioned | - |
| FABRIC | l3leaf | leaf88 | 192.168.0.188 | - | Provisioned | - |
| FABRIC | l3leaf | leaf89 | 192.168.0.189 | - | Provisioned | - |
| FABRIC | l3leaf | leaf90 | 192.168.0.190 | - | Provisioned | - |
| FABRIC | l3leaf | leaf91 | 192.168.0.191 | - | Provisioned | - |
| FABRIC | l3leaf | leaf92 | 192.168.0.192 | - | Provisioned | - |
| FABRIC | l3leaf | leaf93 | 192.168.0.193 | - | Provisioned | - |
| FABRIC | l3leaf | leaf94 | 192.168.0.194 | - | Provisioned | - |
| FABRIC | l3leaf | leaf95 | 192.168.0.195 | - | Provisioned | - |
| FABRIC | l3leaf | leaf96 | 192.168.0.196 | - | Provisioned | - |
| FABRIC | l3leaf | leaf97 | 192.168.0.197 | - | Provisioned | - |
| FABRIC | l3leaf | leaf98 | 192.168.0.198 | - | Provisioned | - |
| FABRIC | l3leaf | leaf99 | 192.168.0.199 | - | Provisioned | - |
| FABRIC | spine | spine1 | 192.168.0.11/24 | - | Provisioned | - |
| FABRIC | spine | spine2 | 192.168.0.12/24 | - | Provisioned | - |
| FABRIC | spine | spine3 | 192.168.0.13/24 | - | Provisioned | - |
| FABRIC | spine | spine4 | 192.168.0.14/24 | - | Provisioned | - |
| FABRIC | spine | spine5 | 192.168.0.15/24 | - | Provisioned | - |
| FABRIC | spine | spine6 | 192.168.0.16/24 | - | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | leaf1 | Ethernet1 | mlag_peer | leaf2 | Ethernet1 |
| l3leaf | leaf1 | Ethernet2 | mlag_peer | leaf2 | Ethernet2 |
| l3leaf | leaf1 | Ethernet3 | spine | spine1 | Ethernet3 |
| l3leaf | leaf1 | Ethernet4 | spine | spine2 | Ethernet3 |
| l3leaf | leaf1 | Ethernet5 | spine | spine3 | Ethernet3 |
| l3leaf | leaf1 | Ethernet6 | spine | spine4 | Ethernet3 |
| l3leaf | leaf1 | Ethernet8 | spine | spine6 | Ethernet3 |
| l3leaf | leaf2 | Ethernet3 | spine | spine1 | Ethernet4 |
| l3leaf | leaf2 | Ethernet4 | spine | spine2 | Ethernet4 |
| l3leaf | leaf2 | Ethernet5 | spine | spine3 | Ethernet4 |
| l3leaf | leaf2 | Ethernet6 | spine | spine4 | Ethernet4 |
| l3leaf | leaf2 | Ethernet8 | spine | spine6 | Ethernet4 |
| l3leaf | leaf3 | Ethernet1 | mlag_peer | leaf4 | Ethernet1 |
| l3leaf | leaf3 | Ethernet2 | mlag_peer | leaf4 | Ethernet2 |
| l3leaf | leaf3 | Ethernet3 | spine | spine1 | Ethernet5 |
| l3leaf | leaf3 | Ethernet4 | spine | spine2 | Ethernet5 |
| l3leaf | leaf3 | Ethernet5 | spine | spine3 | Ethernet5 |
| l3leaf | leaf3 | Ethernet6 | spine | spine4 | Ethernet5 |
| l3leaf | leaf3 | Ethernet7 | spine | spine5 | Ethernet5 |
| l3leaf | leaf3 | Ethernet8 | spine | spine6 | Ethernet5 |
| l3leaf | leaf4 | Ethernet3 | spine | spine1 | Ethernet6 |
| l3leaf | leaf4 | Ethernet4 | spine | spine2 | Ethernet6 |
| l3leaf | leaf4 | Ethernet5 | spine | spine3 | Ethernet6 |
| l3leaf | leaf4 | Ethernet6 | spine | spine4 | Ethernet6 |
| l3leaf | leaf4 | Ethernet7 | spine | spine5 | Ethernet6 |
| l3leaf | leaf4 | Ethernet8 | spine | spine6 | Ethernet6 |
| l3leaf | leaf5 | Ethernet3 | spine | spine1 | Ethernet7 |
| l3leaf | leaf5 | Ethernet4 | spine | spine2 | Ethernet7 |
| l3leaf | leaf5 | Ethernet5 | spine | spine3 | Ethernet7 |
| l3leaf | leaf5 | Ethernet6 | spine | spine4 | Ethernet7 |
| l3leaf | leaf5 | Ethernet7 | spine | spine5 | Ethernet7 |
| l3leaf | leaf5 | Ethernet8 | spine | spine6 | Ethernet7 |
| l3leaf | leaf6 | Ethernet3 | spine | spine1 | Ethernet8 |
| l3leaf | leaf6 | Ethernet4 | spine | spine2 | Ethernet8 |
| l3leaf | leaf6 | Ethernet5 | spine | spine3 | Ethernet8 |
| l3leaf | leaf6 | Ethernet6 | spine | spine4 | Ethernet8 |
| l3leaf | leaf6 | Ethernet7 | spine | spine5 | Ethernet8 |
| l3leaf | leaf6 | Ethernet8 | spine | spine6 | Ethernet8 |
| l3leaf | leaf7 | Ethernet3 | spine | spine1 | Ethernet9 |
| l3leaf | leaf7 | Ethernet4 | spine | spine2 | Ethernet9 |
| l3leaf | leaf7 | Ethernet5 | spine | spine3 | Ethernet9 |
| l3leaf | leaf7 | Ethernet6 | spine | spine4 | Ethernet9 |
| l3leaf | leaf7 | Ethernet7 | spine | spine5 | Ethernet9 |
| l3leaf | leaf7 | Ethernet8 | spine | spine6 | Ethernet9 |
| l3leaf | leaf8 | Ethernet3 | spine | spine1 | Ethernet10 |
| l3leaf | leaf8 | Ethernet4 | spine | spine2 | Ethernet10 |
| l3leaf | leaf8 | Ethernet5 | spine | spine3 | Ethernet10 |
| l3leaf | leaf8 | Ethernet6 | spine | spine4 | Ethernet10 |
| l3leaf | leaf8 | Ethernet7 | spine | spine5 | Ethernet10 |
| l3leaf | leaf8 | Ethernet8 | spine | spine6 | Ethernet10 |
| l3leaf | leaf9 | Ethernet3 | spine | spine1 | Ethernet11 |
| l3leaf | leaf9 | Ethernet4 | spine | spine2 | Ethernet11 |
| l3leaf | leaf9 | Ethernet5 | spine | spine3 | Ethernet11 |
| l3leaf | leaf9 | Ethernet6 | spine | spine4 | Ethernet11 |
| l3leaf | leaf9 | Ethernet7 | spine | spine5 | Ethernet11 |
| l3leaf | leaf9 | Ethernet8 | spine | spine6 | Ethernet11 |
| l3leaf | leaf10 | Ethernet3 | spine | spine1 | Ethernet12 |
| l3leaf | leaf10 | Ethernet4 | spine | spine2 | Ethernet12 |
| l3leaf | leaf10 | Ethernet5 | spine | spine3 | Ethernet12 |
| l3leaf | leaf10 | Ethernet6 | spine | spine4 | Ethernet12 |
| l3leaf | leaf10 | Ethernet7 | spine | spine5 | Ethernet12 |
| l3leaf | leaf10 | Ethernet8 | spine | spine6 | Ethernet12 |
| l3leaf | leaf11 | Ethernet3 | spine | spine1 | Ethernet13 |
| l3leaf | leaf11 | Ethernet4 | spine | spine2 | Ethernet13 |
| l3leaf | leaf11 | Ethernet5 | spine | spine3 | Ethernet13 |
| l3leaf | leaf11 | Ethernet6 | spine | spine4 | Ethernet13 |
| l3leaf | leaf11 | Ethernet7 | spine | spine5 | Ethernet13 |
| l3leaf | leaf11 | Ethernet8 | spine | spine6 | Ethernet13 |
| l3leaf | leaf12 | Ethernet3 | spine | spine1 | Ethernet14 |
| l3leaf | leaf12 | Ethernet4 | spine | spine2 | Ethernet14 |
| l3leaf | leaf12 | Ethernet5 | spine | spine3 | Ethernet14 |
| l3leaf | leaf12 | Ethernet6 | spine | spine4 | Ethernet14 |
| l3leaf | leaf12 | Ethernet7 | spine | spine5 | Ethernet14 |
| l3leaf | leaf12 | Ethernet8 | spine | spine6 | Ethernet14 |
| l3leaf | leaf13 | Ethernet3 | spine | spine1 | Ethernet15 |
| l3leaf | leaf13 | Ethernet4 | spine | spine2 | Ethernet15 |
| l3leaf | leaf13 | Ethernet5 | spine | spine3 | Ethernet15 |
| l3leaf | leaf13 | Ethernet6 | spine | spine4 | Ethernet15 |
| l3leaf | leaf13 | Ethernet7 | spine | spine5 | Ethernet15 |
| l3leaf | leaf13 | Ethernet8 | spine | spine6 | Ethernet15 |
| l3leaf | leaf14 | Ethernet3 | spine | spine1 | Ethernet16 |
| l3leaf | leaf14 | Ethernet4 | spine | spine2 | Ethernet16 |
| l3leaf | leaf14 | Ethernet5 | spine | spine3 | Ethernet16 |
| l3leaf | leaf14 | Ethernet6 | spine | spine4 | Ethernet16 |
| l3leaf | leaf14 | Ethernet7 | spine | spine5 | Ethernet16 |
| l3leaf | leaf14 | Ethernet8 | spine | spine6 | Ethernet16 |
| l3leaf | leaf15 | Ethernet3 | spine | spine1 | Ethernet17 |
| l3leaf | leaf15 | Ethernet4 | spine | spine2 | Ethernet17 |
| l3leaf | leaf15 | Ethernet5 | spine | spine3 | Ethernet17 |
| l3leaf | leaf15 | Ethernet6 | spine | spine4 | Ethernet17 |
| l3leaf | leaf15 | Ethernet7 | spine | spine5 | Ethernet17 |
| l3leaf | leaf15 | Ethernet8 | spine | spine6 | Ethernet17 |
| l3leaf | leaf16 | Ethernet3 | spine | spine1 | Ethernet18 |
| l3leaf | leaf16 | Ethernet4 | spine | spine2 | Ethernet18 |
| l3leaf | leaf16 | Ethernet5 | spine | spine3 | Ethernet18 |
| l3leaf | leaf16 | Ethernet6 | spine | spine4 | Ethernet18 |
| l3leaf | leaf16 | Ethernet7 | spine | spine5 | Ethernet18 |
| l3leaf | leaf16 | Ethernet8 | spine | spine6 | Ethernet18 |
| l3leaf | leaf17 | Ethernet3 | spine | spine1 | Ethernet19 |
| l3leaf | leaf17 | Ethernet4 | spine | spine2 | Ethernet19 |
| l3leaf | leaf17 | Ethernet5 | spine | spine3 | Ethernet19 |
| l3leaf | leaf17 | Ethernet6 | spine | spine4 | Ethernet19 |
| l3leaf | leaf17 | Ethernet7 | spine | spine5 | Ethernet19 |
| l3leaf | leaf17 | Ethernet8 | spine | spine6 | Ethernet19 |
| l3leaf | leaf18 | Ethernet3 | spine | spine1 | Ethernet20 |
| l3leaf | leaf18 | Ethernet4 | spine | spine2 | Ethernet20 |
| l3leaf | leaf18 | Ethernet5 | spine | spine3 | Ethernet20 |
| l3leaf | leaf18 | Ethernet6 | spine | spine4 | Ethernet20 |
| l3leaf | leaf18 | Ethernet7 | spine | spine5 | Ethernet20 |
| l3leaf | leaf18 | Ethernet8 | spine | spine6 | Ethernet20 |
| l3leaf | leaf19 | Ethernet3 | spine | spine1 | Ethernet21 |
| l3leaf | leaf19 | Ethernet4 | spine | spine2 | Ethernet21 |
| l3leaf | leaf19 | Ethernet5 | spine | spine3 | Ethernet21 |
| l3leaf | leaf19 | Ethernet6 | spine | spine4 | Ethernet21 |
| l3leaf | leaf19 | Ethernet7 | spine | spine5 | Ethernet21 |
| l3leaf | leaf19 | Ethernet8 | spine | spine6 | Ethernet21 |
| l3leaf | leaf20 | Ethernet3 | spine | spine1 | Ethernet22 |
| l3leaf | leaf20 | Ethernet4 | spine | spine2 | Ethernet22 |
| l3leaf | leaf20 | Ethernet5 | spine | spine3 | Ethernet22 |
| l3leaf | leaf20 | Ethernet6 | spine | spine4 | Ethernet22 |
| l3leaf | leaf20 | Ethernet7 | spine | spine5 | Ethernet22 |
| l3leaf | leaf20 | Ethernet8 | spine | spine6 | Ethernet22 |
| l3leaf | leaf21 | Ethernet3 | spine | spine1 | Ethernet23 |
| l3leaf | leaf21 | Ethernet4 | spine | spine2 | Ethernet23 |
| l3leaf | leaf21 | Ethernet5 | spine | spine3 | Ethernet23 |
| l3leaf | leaf21 | Ethernet6 | spine | spine4 | Ethernet23 |
| l3leaf | leaf21 | Ethernet7 | spine | spine5 | Ethernet23 |
| l3leaf | leaf21 | Ethernet8 | spine | spine6 | Ethernet23 |
| l3leaf | leaf22 | Ethernet3 | spine | spine1 | Ethernet24 |
| l3leaf | leaf22 | Ethernet4 | spine | spine2 | Ethernet24 |
| l3leaf | leaf22 | Ethernet5 | spine | spine3 | Ethernet24 |
| l3leaf | leaf22 | Ethernet6 | spine | spine4 | Ethernet24 |
| l3leaf | leaf22 | Ethernet7 | spine | spine5 | Ethernet24 |
| l3leaf | leaf22 | Ethernet8 | spine | spine6 | Ethernet24 |
| l3leaf | leaf23 | Ethernet3 | spine | spine1 | Ethernet25 |
| l3leaf | leaf23 | Ethernet4 | spine | spine2 | Ethernet25 |
| l3leaf | leaf23 | Ethernet5 | spine | spine3 | Ethernet25 |
| l3leaf | leaf23 | Ethernet6 | spine | spine4 | Ethernet25 |
| l3leaf | leaf23 | Ethernet7 | spine | spine5 | Ethernet25 |
| l3leaf | leaf23 | Ethernet8 | spine | spine6 | Ethernet25 |
| l3leaf | leaf24 | Ethernet3 | spine | spine1 | Ethernet26 |
| l3leaf | leaf24 | Ethernet4 | spine | spine2 | Ethernet26 |
| l3leaf | leaf24 | Ethernet5 | spine | spine3 | Ethernet26 |
| l3leaf | leaf24 | Ethernet6 | spine | spine4 | Ethernet26 |
| l3leaf | leaf24 | Ethernet7 | spine | spine5 | Ethernet26 |
| l3leaf | leaf24 | Ethernet8 | spine | spine6 | Ethernet26 |
| l3leaf | leaf25 | Ethernet3 | spine | spine1 | Ethernet27 |
| l3leaf | leaf25 | Ethernet4 | spine | spine2 | Ethernet27 |
| l3leaf | leaf25 | Ethernet5 | spine | spine3 | Ethernet27 |
| l3leaf | leaf25 | Ethernet6 | spine | spine4 | Ethernet27 |
| l3leaf | leaf25 | Ethernet7 | spine | spine5 | Ethernet27 |
| l3leaf | leaf25 | Ethernet8 | spine | spine6 | Ethernet27 |
| l3leaf | leaf26 | Ethernet3 | spine | spine1 | Ethernet28 |
| l3leaf | leaf26 | Ethernet4 | spine | spine2 | Ethernet28 |
| l3leaf | leaf26 | Ethernet5 | spine | spine3 | Ethernet28 |
| l3leaf | leaf26 | Ethernet6 | spine | spine4 | Ethernet28 |
| l3leaf | leaf26 | Ethernet7 | spine | spine5 | Ethernet28 |
| l3leaf | leaf26 | Ethernet8 | spine | spine6 | Ethernet28 |
| l3leaf | leaf27 | Ethernet3 | spine | spine1 | Ethernet29 |
| l3leaf | leaf27 | Ethernet4 | spine | spine2 | Ethernet29 |
| l3leaf | leaf27 | Ethernet5 | spine | spine3 | Ethernet29 |
| l3leaf | leaf27 | Ethernet6 | spine | spine4 | Ethernet29 |
| l3leaf | leaf27 | Ethernet7 | spine | spine5 | Ethernet29 |
| l3leaf | leaf27 | Ethernet8 | spine | spine6 | Ethernet29 |
| l3leaf | leaf28 | Ethernet3 | spine | spine1 | Ethernet30 |
| l3leaf | leaf28 | Ethernet4 | spine | spine2 | Ethernet30 |
| l3leaf | leaf28 | Ethernet5 | spine | spine3 | Ethernet30 |
| l3leaf | leaf28 | Ethernet6 | spine | spine4 | Ethernet30 |
| l3leaf | leaf28 | Ethernet7 | spine | spine5 | Ethernet30 |
| l3leaf | leaf28 | Ethernet8 | spine | spine6 | Ethernet30 |
| l3leaf | leaf29 | Ethernet3 | spine | spine1 | Ethernet31 |
| l3leaf | leaf29 | Ethernet4 | spine | spine2 | Ethernet31 |
| l3leaf | leaf29 | Ethernet5 | spine | spine3 | Ethernet31 |
| l3leaf | leaf29 | Ethernet6 | spine | spine4 | Ethernet31 |
| l3leaf | leaf29 | Ethernet7 | spine | spine5 | Ethernet31 |
| l3leaf | leaf29 | Ethernet8 | spine | spine6 | Ethernet31 |
| l3leaf | leaf30 | Ethernet3 | spine | spine1 | Ethernet32 |
| l3leaf | leaf30 | Ethernet4 | spine | spine2 | Ethernet32 |
| l3leaf | leaf30 | Ethernet5 | spine | spine3 | Ethernet32 |
| l3leaf | leaf30 | Ethernet6 | spine | spine4 | Ethernet32 |
| l3leaf | leaf30 | Ethernet7 | spine | spine5 | Ethernet32 |
| l3leaf | leaf30 | Ethernet8 | spine | spine6 | Ethernet32 |
| l3leaf | leaf31 | Ethernet3 | spine | spine1 | Ethernet33 |
| l3leaf | leaf31 | Ethernet4 | spine | spine2 | Ethernet33 |
| l3leaf | leaf31 | Ethernet5 | spine | spine3 | Ethernet33 |
| l3leaf | leaf31 | Ethernet6 | spine | spine4 | Ethernet33 |
| l3leaf | leaf31 | Ethernet7 | spine | spine5 | Ethernet33 |
| l3leaf | leaf31 | Ethernet8 | spine | spine6 | Ethernet33 |
| l3leaf | leaf32 | Ethernet3 | spine | spine1 | Ethernet34 |
| l3leaf | leaf32 | Ethernet4 | spine | spine2 | Ethernet34 |
| l3leaf | leaf32 | Ethernet5 | spine | spine3 | Ethernet34 |
| l3leaf | leaf32 | Ethernet6 | spine | spine4 | Ethernet34 |
| l3leaf | leaf32 | Ethernet7 | spine | spine5 | Ethernet34 |
| l3leaf | leaf32 | Ethernet8 | spine | spine6 | Ethernet34 |
| l3leaf | leaf33 | Ethernet3 | spine | spine1 | Ethernet35 |
| l3leaf | leaf33 | Ethernet4 | spine | spine2 | Ethernet35 |
| l3leaf | leaf33 | Ethernet5 | spine | spine3 | Ethernet35 |
| l3leaf | leaf33 | Ethernet6 | spine | spine4 | Ethernet35 |
| l3leaf | leaf33 | Ethernet7 | spine | spine5 | Ethernet35 |
| l3leaf | leaf33 | Ethernet8 | spine | spine6 | Ethernet35 |
| l3leaf | leaf34 | Ethernet3 | spine | spine1 | Ethernet36 |
| l3leaf | leaf34 | Ethernet4 | spine | spine2 | Ethernet36 |
| l3leaf | leaf34 | Ethernet5 | spine | spine3 | Ethernet36 |
| l3leaf | leaf34 | Ethernet6 | spine | spine4 | Ethernet36 |
| l3leaf | leaf34 | Ethernet7 | spine | spine5 | Ethernet36 |
| l3leaf | leaf34 | Ethernet8 | spine | spine6 | Ethernet36 |
| l3leaf | leaf35 | Ethernet3 | spine | spine1 | Ethernet37 |
| l3leaf | leaf35 | Ethernet4 | spine | spine2 | Ethernet37 |
| l3leaf | leaf35 | Ethernet5 | spine | spine3 | Ethernet37 |
| l3leaf | leaf35 | Ethernet6 | spine | spine4 | Ethernet37 |
| l3leaf | leaf35 | Ethernet7 | spine | spine5 | Ethernet37 |
| l3leaf | leaf35 | Ethernet8 | spine | spine6 | Ethernet37 |
| l3leaf | leaf36 | Ethernet3 | spine | spine1 | Ethernet38 |
| l3leaf | leaf36 | Ethernet4 | spine | spine2 | Ethernet38 |
| l3leaf | leaf36 | Ethernet5 | spine | spine3 | Ethernet38 |
| l3leaf | leaf36 | Ethernet6 | spine | spine4 | Ethernet38 |
| l3leaf | leaf36 | Ethernet7 | spine | spine5 | Ethernet38 |
| l3leaf | leaf36 | Ethernet8 | spine | spine6 | Ethernet38 |
| l3leaf | leaf37 | Ethernet3 | spine | spine1 | Ethernet39 |
| l3leaf | leaf37 | Ethernet4 | spine | spine2 | Ethernet39 |
| l3leaf | leaf37 | Ethernet5 | spine | spine3 | Ethernet39 |
| l3leaf | leaf37 | Ethernet6 | spine | spine4 | Ethernet39 |
| l3leaf | leaf37 | Ethernet7 | spine | spine5 | Ethernet39 |
| l3leaf | leaf37 | Ethernet8 | spine | spine6 | Ethernet39 |
| l3leaf | leaf38 | Ethernet3 | spine | spine1 | Ethernet40 |
| l3leaf | leaf38 | Ethernet4 | spine | spine2 | Ethernet40 |
| l3leaf | leaf38 | Ethernet5 | spine | spine3 | Ethernet40 |
| l3leaf | leaf38 | Ethernet6 | spine | spine4 | Ethernet40 |
| l3leaf | leaf38 | Ethernet7 | spine | spine5 | Ethernet40 |
| l3leaf | leaf38 | Ethernet8 | spine | spine6 | Ethernet40 |
| l3leaf | leaf39 | Ethernet3 | spine | spine1 | Ethernet41 |
| l3leaf | leaf39 | Ethernet4 | spine | spine2 | Ethernet41 |
| l3leaf | leaf39 | Ethernet5 | spine | spine3 | Ethernet41 |
| l3leaf | leaf39 | Ethernet6 | spine | spine4 | Ethernet41 |
| l3leaf | leaf39 | Ethernet7 | spine | spine5 | Ethernet41 |
| l3leaf | leaf39 | Ethernet8 | spine | spine6 | Ethernet41 |
| l3leaf | leaf40 | Ethernet3 | spine | spine1 | Ethernet42 |
| l3leaf | leaf40 | Ethernet4 | spine | spine2 | Ethernet42 |
| l3leaf | leaf40 | Ethernet5 | spine | spine3 | Ethernet42 |
| l3leaf | leaf40 | Ethernet6 | spine | spine4 | Ethernet42 |
| l3leaf | leaf40 | Ethernet7 | spine | spine5 | Ethernet42 |
| l3leaf | leaf40 | Ethernet8 | spine | spine6 | Ethernet42 |
| l3leaf | leaf41 | Ethernet3 | spine | spine1 | Ethernet43 |
| l3leaf | leaf41 | Ethernet4 | spine | spine2 | Ethernet43 |
| l3leaf | leaf41 | Ethernet5 | spine | spine3 | Ethernet43 |
| l3leaf | leaf41 | Ethernet6 | spine | spine4 | Ethernet43 |
| l3leaf | leaf41 | Ethernet7 | spine | spine5 | Ethernet43 |
| l3leaf | leaf41 | Ethernet8 | spine | spine6 | Ethernet43 |
| l3leaf | leaf42 | Ethernet3 | spine | spine1 | Ethernet44 |
| l3leaf | leaf42 | Ethernet4 | spine | spine2 | Ethernet44 |
| l3leaf | leaf42 | Ethernet5 | spine | spine3 | Ethernet44 |
| l3leaf | leaf42 | Ethernet6 | spine | spine4 | Ethernet44 |
| l3leaf | leaf42 | Ethernet7 | spine | spine5 | Ethernet44 |
| l3leaf | leaf42 | Ethernet8 | spine | spine6 | Ethernet44 |
| l3leaf | leaf43 | Ethernet3 | spine | spine1 | Ethernet45 |
| l3leaf | leaf43 | Ethernet4 | spine | spine2 | Ethernet45 |
| l3leaf | leaf43 | Ethernet5 | spine | spine3 | Ethernet45 |
| l3leaf | leaf43 | Ethernet6 | spine | spine4 | Ethernet45 |
| l3leaf | leaf43 | Ethernet7 | spine | spine5 | Ethernet45 |
| l3leaf | leaf43 | Ethernet8 | spine | spine6 | Ethernet45 |
| l3leaf | leaf44 | Ethernet3 | spine | spine1 | Ethernet46 |
| l3leaf | leaf44 | Ethernet4 | spine | spine2 | Ethernet46 |
| l3leaf | leaf44 | Ethernet5 | spine | spine3 | Ethernet46 |
| l3leaf | leaf44 | Ethernet6 | spine | spine4 | Ethernet46 |
| l3leaf | leaf44 | Ethernet7 | spine | spine5 | Ethernet46 |
| l3leaf | leaf44 | Ethernet8 | spine | spine6 | Ethernet46 |
| l3leaf | leaf45 | Ethernet3 | spine | spine1 | Ethernet47 |
| l3leaf | leaf45 | Ethernet4 | spine | spine2 | Ethernet47 |
| l3leaf | leaf45 | Ethernet5 | spine | spine3 | Ethernet47 |
| l3leaf | leaf45 | Ethernet6 | spine | spine4 | Ethernet47 |
| l3leaf | leaf45 | Ethernet7 | spine | spine5 | Ethernet47 |
| l3leaf | leaf45 | Ethernet8 | spine | spine6 | Ethernet47 |
| l3leaf | leaf46 | Ethernet3 | spine | spine1 | Ethernet48 |
| l3leaf | leaf46 | Ethernet4 | spine | spine2 | Ethernet48 |
| l3leaf | leaf46 | Ethernet5 | spine | spine3 | Ethernet48 |
| l3leaf | leaf46 | Ethernet6 | spine | spine4 | Ethernet48 |
| l3leaf | leaf46 | Ethernet7 | spine | spine5 | Ethernet48 |
| l3leaf | leaf46 | Ethernet8 | spine | spine6 | Ethernet48 |
| l3leaf | leaf47 | Ethernet3 | spine | spine1 | Ethernet49 |
| l3leaf | leaf47 | Ethernet4 | spine | spine2 | Ethernet49 |
| l3leaf | leaf47 | Ethernet5 | spine | spine3 | Ethernet49 |
| l3leaf | leaf47 | Ethernet6 | spine | spine4 | Ethernet49 |
| l3leaf | leaf47 | Ethernet7 | spine | spine5 | Ethernet49 |
| l3leaf | leaf47 | Ethernet8 | spine | spine6 | Ethernet49 |
| l3leaf | leaf48 | Ethernet3 | spine | spine1 | Ethernet50 |
| l3leaf | leaf48 | Ethernet4 | spine | spine2 | Ethernet50 |
| l3leaf | leaf48 | Ethernet5 | spine | spine3 | Ethernet50 |
| l3leaf | leaf48 | Ethernet6 | spine | spine4 | Ethernet50 |
| l3leaf | leaf48 | Ethernet7 | spine | spine5 | Ethernet50 |
| l3leaf | leaf48 | Ethernet8 | spine | spine6 | Ethernet50 |
| l3leaf | leaf49 | Ethernet3 | spine | spine1 | Ethernet51 |
| l3leaf | leaf49 | Ethernet4 | spine | spine2 | Ethernet51 |
| l3leaf | leaf49 | Ethernet5 | spine | spine3 | Ethernet51 |
| l3leaf | leaf49 | Ethernet6 | spine | spine4 | Ethernet51 |
| l3leaf | leaf49 | Ethernet7 | spine | spine5 | Ethernet51 |
| l3leaf | leaf49 | Ethernet8 | spine | spine6 | Ethernet51 |
| l3leaf | leaf50 | Ethernet3 | spine | spine1 | Ethernet52 |
| l3leaf | leaf50 | Ethernet4 | spine | spine2 | Ethernet52 |
| l3leaf | leaf50 | Ethernet5 | spine | spine3 | Ethernet52 |
| l3leaf | leaf50 | Ethernet6 | spine | spine4 | Ethernet52 |
| l3leaf | leaf50 | Ethernet7 | spine | spine5 | Ethernet52 |
| l3leaf | leaf50 | Ethernet8 | spine | spine6 | Ethernet52 |
| l3leaf | leaf51 | Ethernet3 | spine | spine1 | Ethernet53 |
| l3leaf | leaf51 | Ethernet4 | spine | spine2 | Ethernet53 |
| l3leaf | leaf51 | Ethernet5 | spine | spine3 | Ethernet53 |
| l3leaf | leaf51 | Ethernet6 | spine | spine4 | Ethernet53 |
| l3leaf | leaf51 | Ethernet7 | spine | spine5 | Ethernet53 |
| l3leaf | leaf51 | Ethernet8 | spine | spine6 | Ethernet53 |
| l3leaf | leaf52 | Ethernet3 | spine | spine1 | Ethernet54 |
| l3leaf | leaf52 | Ethernet4 | spine | spine2 | Ethernet54 |
| l3leaf | leaf52 | Ethernet5 | spine | spine3 | Ethernet54 |
| l3leaf | leaf52 | Ethernet6 | spine | spine4 | Ethernet54 |
| l3leaf | leaf52 | Ethernet7 | spine | spine5 | Ethernet54 |
| l3leaf | leaf52 | Ethernet8 | spine | spine6 | Ethernet54 |
| l3leaf | leaf53 | Ethernet3 | spine | spine1 | Ethernet55 |
| l3leaf | leaf53 | Ethernet4 | spine | spine2 | Ethernet55 |
| l3leaf | leaf53 | Ethernet5 | spine | spine3 | Ethernet55 |
| l3leaf | leaf53 | Ethernet6 | spine | spine4 | Ethernet55 |
| l3leaf | leaf53 | Ethernet7 | spine | spine5 | Ethernet55 |
| l3leaf | leaf53 | Ethernet8 | spine | spine6 | Ethernet55 |
| l3leaf | leaf54 | Ethernet3 | spine | spine1 | Ethernet56 |
| l3leaf | leaf54 | Ethernet4 | spine | spine2 | Ethernet56 |
| l3leaf | leaf54 | Ethernet5 | spine | spine3 | Ethernet56 |
| l3leaf | leaf54 | Ethernet6 | spine | spine4 | Ethernet56 |
| l3leaf | leaf54 | Ethernet7 | spine | spine5 | Ethernet56 |
| l3leaf | leaf54 | Ethernet8 | spine | spine6 | Ethernet56 |
| l3leaf | leaf55 | Ethernet3 | spine | spine1 | Ethernet57 |
| l3leaf | leaf55 | Ethernet4 | spine | spine2 | Ethernet57 |
| l3leaf | leaf55 | Ethernet5 | spine | spine3 | Ethernet57 |
| l3leaf | leaf55 | Ethernet6 | spine | spine4 | Ethernet57 |
| l3leaf | leaf55 | Ethernet7 | spine | spine5 | Ethernet57 |
| l3leaf | leaf55 | Ethernet8 | spine | spine6 | Ethernet57 |
| l3leaf | leaf56 | Ethernet3 | spine | spine1 | Ethernet58 |
| l3leaf | leaf56 | Ethernet4 | spine | spine2 | Ethernet58 |
| l3leaf | leaf56 | Ethernet5 | spine | spine3 | Ethernet58 |
| l3leaf | leaf56 | Ethernet6 | spine | spine4 | Ethernet58 |
| l3leaf | leaf56 | Ethernet7 | spine | spine5 | Ethernet58 |
| l3leaf | leaf56 | Ethernet8 | spine | spine6 | Ethernet58 |
| l3leaf | leaf57 | Ethernet3 | spine | spine1 | Ethernet59 |
| l3leaf | leaf57 | Ethernet4 | spine | spine2 | Ethernet59 |
| l3leaf | leaf57 | Ethernet5 | spine | spine3 | Ethernet59 |
| l3leaf | leaf57 | Ethernet6 | spine | spine4 | Ethernet59 |
| l3leaf | leaf57 | Ethernet7 | spine | spine5 | Ethernet59 |
| l3leaf | leaf57 | Ethernet8 | spine | spine6 | Ethernet59 |
| l3leaf | leaf58 | Ethernet3 | spine | spine1 | Ethernet60 |
| l3leaf | leaf58 | Ethernet4 | spine | spine2 | Ethernet60 |
| l3leaf | leaf58 | Ethernet5 | spine | spine3 | Ethernet60 |
| l3leaf | leaf58 | Ethernet6 | spine | spine4 | Ethernet60 |
| l3leaf | leaf58 | Ethernet7 | spine | spine5 | Ethernet60 |
| l3leaf | leaf58 | Ethernet8 | spine | spine6 | Ethernet60 |
| l3leaf | leaf59 | Ethernet3 | spine | spine1 | Ethernet61 |
| l3leaf | leaf59 | Ethernet4 | spine | spine2 | Ethernet61 |
| l3leaf | leaf59 | Ethernet5 | spine | spine3 | Ethernet61 |
| l3leaf | leaf59 | Ethernet6 | spine | spine4 | Ethernet61 |
| l3leaf | leaf59 | Ethernet7 | spine | spine5 | Ethernet61 |
| l3leaf | leaf59 | Ethernet8 | spine | spine6 | Ethernet61 |
| l3leaf | leaf60 | Ethernet3 | spine | spine1 | Ethernet62 |
| l3leaf | leaf60 | Ethernet4 | spine | spine2 | Ethernet62 |
| l3leaf | leaf60 | Ethernet5 | spine | spine3 | Ethernet62 |
| l3leaf | leaf60 | Ethernet6 | spine | spine4 | Ethernet62 |
| l3leaf | leaf60 | Ethernet7 | spine | spine5 | Ethernet62 |
| l3leaf | leaf60 | Ethernet8 | spine | spine6 | Ethernet62 |
| l3leaf | leaf61 | Ethernet3 | spine | spine1 | Ethernet63 |
| l3leaf | leaf61 | Ethernet4 | spine | spine2 | Ethernet63 |
| l3leaf | leaf61 | Ethernet5 | spine | spine3 | Ethernet63 |
| l3leaf | leaf61 | Ethernet6 | spine | spine4 | Ethernet63 |
| l3leaf | leaf61 | Ethernet7 | spine | spine5 | Ethernet63 |
| l3leaf | leaf61 | Ethernet8 | spine | spine6 | Ethernet63 |
| l3leaf | leaf62 | Ethernet3 | spine | spine1 | Ethernet64 |
| l3leaf | leaf62 | Ethernet4 | spine | spine2 | Ethernet64 |
| l3leaf | leaf62 | Ethernet5 | spine | spine3 | Ethernet64 |
| l3leaf | leaf62 | Ethernet6 | spine | spine4 | Ethernet64 |
| l3leaf | leaf62 | Ethernet7 | spine | spine5 | Ethernet64 |
| l3leaf | leaf62 | Ethernet8 | spine | spine6 | Ethernet64 |
| l3leaf | leaf63 | Ethernet3 | spine | spine1 | Ethernet65 |
| l3leaf | leaf63 | Ethernet4 | spine | spine2 | Ethernet65 |
| l3leaf | leaf63 | Ethernet5 | spine | spine3 | Ethernet65 |
| l3leaf | leaf63 | Ethernet6 | spine | spine4 | Ethernet65 |
| l3leaf | leaf63 | Ethernet7 | spine | spine5 | Ethernet65 |
| l3leaf | leaf63 | Ethernet8 | spine | spine6 | Ethernet65 |
| l3leaf | leaf64 | Ethernet3 | spine | spine1 | Ethernet66 |
| l3leaf | leaf64 | Ethernet4 | spine | spine2 | Ethernet66 |
| l3leaf | leaf64 | Ethernet5 | spine | spine3 | Ethernet66 |
| l3leaf | leaf64 | Ethernet6 | spine | spine4 | Ethernet66 |
| l3leaf | leaf64 | Ethernet7 | spine | spine5 | Ethernet66 |
| l3leaf | leaf64 | Ethernet8 | spine | spine6 | Ethernet66 |
| l3leaf | leaf65 | Ethernet3 | spine | spine1 | Ethernet67 |
| l3leaf | leaf65 | Ethernet4 | spine | spine2 | Ethernet67 |
| l3leaf | leaf65 | Ethernet5 | spine | spine3 | Ethernet67 |
| l3leaf | leaf65 | Ethernet6 | spine | spine4 | Ethernet67 |
| l3leaf | leaf65 | Ethernet7 | spine | spine5 | Ethernet67 |
| l3leaf | leaf65 | Ethernet8 | spine | spine6 | Ethernet67 |
| l3leaf | leaf66 | Ethernet3 | spine | spine1 | Ethernet68 |
| l3leaf | leaf66 | Ethernet4 | spine | spine2 | Ethernet68 |
| l3leaf | leaf66 | Ethernet5 | spine | spine3 | Ethernet68 |
| l3leaf | leaf66 | Ethernet6 | spine | spine4 | Ethernet68 |
| l3leaf | leaf66 | Ethernet7 | spine | spine5 | Ethernet68 |
| l3leaf | leaf66 | Ethernet8 | spine | spine6 | Ethernet68 |
| l3leaf | leaf67 | Ethernet3 | spine | spine1 | Ethernet69 |
| l3leaf | leaf67 | Ethernet4 | spine | spine2 | Ethernet69 |
| l3leaf | leaf67 | Ethernet5 | spine | spine3 | Ethernet69 |
| l3leaf | leaf67 | Ethernet6 | spine | spine4 | Ethernet69 |
| l3leaf | leaf67 | Ethernet7 | spine | spine5 | Ethernet69 |
| l3leaf | leaf67 | Ethernet8 | spine | spine6 | Ethernet69 |
| l3leaf | leaf68 | Ethernet3 | spine | spine1 | Ethernet70 |
| l3leaf | leaf68 | Ethernet4 | spine | spine2 | Ethernet70 |
| l3leaf | leaf68 | Ethernet5 | spine | spine3 | Ethernet70 |
| l3leaf | leaf68 | Ethernet6 | spine | spine4 | Ethernet70 |
| l3leaf | leaf68 | Ethernet7 | spine | spine5 | Ethernet70 |
| l3leaf | leaf68 | Ethernet8 | spine | spine6 | Ethernet70 |
| l3leaf | leaf69 | Ethernet3 | spine | spine1 | Ethernet71 |
| l3leaf | leaf69 | Ethernet4 | spine | spine2 | Ethernet71 |
| l3leaf | leaf69 | Ethernet5 | spine | spine3 | Ethernet71 |
| l3leaf | leaf69 | Ethernet6 | spine | spine4 | Ethernet71 |
| l3leaf | leaf69 | Ethernet7 | spine | spine5 | Ethernet71 |
| l3leaf | leaf69 | Ethernet8 | spine | spine6 | Ethernet71 |
| l3leaf | leaf70 | Ethernet3 | spine | spine1 | Ethernet72 |
| l3leaf | leaf70 | Ethernet4 | spine | spine2 | Ethernet72 |
| l3leaf | leaf70 | Ethernet5 | spine | spine3 | Ethernet72 |
| l3leaf | leaf70 | Ethernet6 | spine | spine4 | Ethernet72 |
| l3leaf | leaf70 | Ethernet7 | spine | spine5 | Ethernet72 |
| l3leaf | leaf70 | Ethernet8 | spine | spine6 | Ethernet72 |
| l3leaf | leaf71 | Ethernet3 | spine | spine1 | Ethernet73 |
| l3leaf | leaf71 | Ethernet4 | spine | spine2 | Ethernet73 |
| l3leaf | leaf71 | Ethernet5 | spine | spine3 | Ethernet73 |
| l3leaf | leaf71 | Ethernet6 | spine | spine4 | Ethernet73 |
| l3leaf | leaf71 | Ethernet7 | spine | spine5 | Ethernet73 |
| l3leaf | leaf71 | Ethernet8 | spine | spine6 | Ethernet73 |
| l3leaf | leaf72 | Ethernet3 | spine | spine1 | Ethernet74 |
| l3leaf | leaf72 | Ethernet4 | spine | spine2 | Ethernet74 |
| l3leaf | leaf72 | Ethernet5 | spine | spine3 | Ethernet74 |
| l3leaf | leaf72 | Ethernet6 | spine | spine4 | Ethernet74 |
| l3leaf | leaf72 | Ethernet7 | spine | spine5 | Ethernet74 |
| l3leaf | leaf72 | Ethernet8 | spine | spine6 | Ethernet74 |
| l3leaf | leaf73 | Ethernet3 | spine | spine1 | Ethernet75 |
| l3leaf | leaf73 | Ethernet4 | spine | spine2 | Ethernet75 |
| l3leaf | leaf73 | Ethernet5 | spine | spine3 | Ethernet75 |
| l3leaf | leaf73 | Ethernet6 | spine | spine4 | Ethernet75 |
| l3leaf | leaf73 | Ethernet7 | spine | spine5 | Ethernet75 |
| l3leaf | leaf73 | Ethernet8 | spine | spine6 | Ethernet75 |
| l3leaf | leaf74 | Ethernet3 | spine | spine1 | Ethernet76 |
| l3leaf | leaf74 | Ethernet4 | spine | spine2 | Ethernet76 |
| l3leaf | leaf74 | Ethernet5 | spine | spine3 | Ethernet76 |
| l3leaf | leaf74 | Ethernet6 | spine | spine4 | Ethernet76 |
| l3leaf | leaf74 | Ethernet7 | spine | spine5 | Ethernet76 |
| l3leaf | leaf74 | Ethernet8 | spine | spine6 | Ethernet76 |
| l3leaf | leaf75 | Ethernet3 | spine | spine1 | Ethernet77 |
| l3leaf | leaf75 | Ethernet4 | spine | spine2 | Ethernet77 |
| l3leaf | leaf75 | Ethernet5 | spine | spine3 | Ethernet77 |
| l3leaf | leaf75 | Ethernet6 | spine | spine4 | Ethernet77 |
| l3leaf | leaf75 | Ethernet7 | spine | spine5 | Ethernet77 |
| l3leaf | leaf75 | Ethernet8 | spine | spine6 | Ethernet77 |
| l3leaf | leaf76 | Ethernet3 | spine | spine1 | Ethernet78 |
| l3leaf | leaf76 | Ethernet4 | spine | spine2 | Ethernet78 |
| l3leaf | leaf76 | Ethernet5 | spine | spine3 | Ethernet78 |
| l3leaf | leaf76 | Ethernet6 | spine | spine4 | Ethernet78 |
| l3leaf | leaf76 | Ethernet7 | spine | spine5 | Ethernet78 |
| l3leaf | leaf76 | Ethernet8 | spine | spine6 | Ethernet78 |
| l3leaf | leaf77 | Ethernet3 | spine | spine1 | Ethernet79 |
| l3leaf | leaf77 | Ethernet4 | spine | spine2 | Ethernet79 |
| l3leaf | leaf77 | Ethernet5 | spine | spine3 | Ethernet79 |
| l3leaf | leaf77 | Ethernet6 | spine | spine4 | Ethernet79 |
| l3leaf | leaf77 | Ethernet7 | spine | spine5 | Ethernet79 |
| l3leaf | leaf77 | Ethernet8 | spine | spine6 | Ethernet79 |
| l3leaf | leaf78 | Ethernet3 | spine | spine1 | Ethernet80 |
| l3leaf | leaf78 | Ethernet4 | spine | spine2 | Ethernet80 |
| l3leaf | leaf78 | Ethernet5 | spine | spine3 | Ethernet80 |
| l3leaf | leaf78 | Ethernet6 | spine | spine4 | Ethernet80 |
| l3leaf | leaf78 | Ethernet7 | spine | spine5 | Ethernet80 |
| l3leaf | leaf78 | Ethernet8 | spine | spine6 | Ethernet80 |
| l3leaf | leaf79 | Ethernet3 | spine | spine1 | Ethernet81 |
| l3leaf | leaf79 | Ethernet4 | spine | spine2 | Ethernet81 |
| l3leaf | leaf79 | Ethernet5 | spine | spine3 | Ethernet81 |
| l3leaf | leaf79 | Ethernet6 | spine | spine4 | Ethernet81 |
| l3leaf | leaf79 | Ethernet7 | spine | spine5 | Ethernet81 |
| l3leaf | leaf79 | Ethernet8 | spine | spine6 | Ethernet81 |
| l3leaf | leaf80 | Ethernet3 | spine | spine1 | Ethernet82 |
| l3leaf | leaf80 | Ethernet4 | spine | spine2 | Ethernet82 |
| l3leaf | leaf80 | Ethernet5 | spine | spine3 | Ethernet82 |
| l3leaf | leaf80 | Ethernet6 | spine | spine4 | Ethernet82 |
| l3leaf | leaf80 | Ethernet7 | spine | spine5 | Ethernet82 |
| l3leaf | leaf80 | Ethernet8 | spine | spine6 | Ethernet82 |
| l3leaf | leaf81 | Ethernet3 | spine | spine1 | Ethernet83 |
| l3leaf | leaf81 | Ethernet4 | spine | spine2 | Ethernet83 |
| l3leaf | leaf81 | Ethernet5 | spine | spine3 | Ethernet83 |
| l3leaf | leaf81 | Ethernet6 | spine | spine4 | Ethernet83 |
| l3leaf | leaf81 | Ethernet7 | spine | spine5 | Ethernet83 |
| l3leaf | leaf81 | Ethernet8 | spine | spine6 | Ethernet83 |
| l3leaf | leaf82 | Ethernet3 | spine | spine1 | Ethernet84 |
| l3leaf | leaf82 | Ethernet4 | spine | spine2 | Ethernet84 |
| l3leaf | leaf82 | Ethernet5 | spine | spine3 | Ethernet84 |
| l3leaf | leaf82 | Ethernet6 | spine | spine4 | Ethernet84 |
| l3leaf | leaf82 | Ethernet7 | spine | spine5 | Ethernet84 |
| l3leaf | leaf82 | Ethernet8 | spine | spine6 | Ethernet84 |
| l3leaf | leaf83 | Ethernet3 | spine | spine1 | Ethernet85 |
| l3leaf | leaf83 | Ethernet4 | spine | spine2 | Ethernet85 |
| l3leaf | leaf83 | Ethernet5 | spine | spine3 | Ethernet85 |
| l3leaf | leaf83 | Ethernet6 | spine | spine4 | Ethernet85 |
| l3leaf | leaf83 | Ethernet7 | spine | spine5 | Ethernet85 |
| l3leaf | leaf83 | Ethernet8 | spine | spine6 | Ethernet85 |
| l3leaf | leaf84 | Ethernet3 | spine | spine1 | Ethernet86 |
| l3leaf | leaf84 | Ethernet4 | spine | spine2 | Ethernet86 |
| l3leaf | leaf84 | Ethernet5 | spine | spine3 | Ethernet86 |
| l3leaf | leaf84 | Ethernet6 | spine | spine4 | Ethernet86 |
| l3leaf | leaf84 | Ethernet7 | spine | spine5 | Ethernet86 |
| l3leaf | leaf84 | Ethernet8 | spine | spine6 | Ethernet86 |
| l3leaf | leaf85 | Ethernet3 | spine | spine1 | Ethernet87 |
| l3leaf | leaf85 | Ethernet4 | spine | spine2 | Ethernet87 |
| l3leaf | leaf85 | Ethernet5 | spine | spine3 | Ethernet87 |
| l3leaf | leaf85 | Ethernet6 | spine | spine4 | Ethernet87 |
| l3leaf | leaf85 | Ethernet7 | spine | spine5 | Ethernet87 |
| l3leaf | leaf85 | Ethernet8 | spine | spine6 | Ethernet87 |
| l3leaf | leaf86 | Ethernet3 | spine | spine1 | Ethernet88 |
| l3leaf | leaf86 | Ethernet4 | spine | spine2 | Ethernet88 |
| l3leaf | leaf86 | Ethernet5 | spine | spine3 | Ethernet88 |
| l3leaf | leaf86 | Ethernet6 | spine | spine4 | Ethernet88 |
| l3leaf | leaf86 | Ethernet7 | spine | spine5 | Ethernet88 |
| l3leaf | leaf86 | Ethernet8 | spine | spine6 | Ethernet88 |
| l3leaf | leaf87 | Ethernet3 | spine | spine1 | Ethernet89 |
| l3leaf | leaf87 | Ethernet4 | spine | spine2 | Ethernet89 |
| l3leaf | leaf87 | Ethernet5 | spine | spine3 | Ethernet89 |
| l3leaf | leaf87 | Ethernet6 | spine | spine4 | Ethernet89 |
| l3leaf | leaf87 | Ethernet7 | spine | spine5 | Ethernet89 |
| l3leaf | leaf87 | Ethernet8 | spine | spine6 | Ethernet89 |
| l3leaf | leaf88 | Ethernet3 | spine | spine1 | Ethernet90 |
| l3leaf | leaf88 | Ethernet4 | spine | spine2 | Ethernet90 |
| l3leaf | leaf88 | Ethernet5 | spine | spine3 | Ethernet90 |
| l3leaf | leaf88 | Ethernet6 | spine | spine4 | Ethernet90 |
| l3leaf | leaf88 | Ethernet7 | spine | spine5 | Ethernet90 |
| l3leaf | leaf88 | Ethernet8 | spine | spine6 | Ethernet90 |
| l3leaf | leaf89 | Ethernet3 | spine | spine1 | Ethernet91 |
| l3leaf | leaf89 | Ethernet4 | spine | spine2 | Ethernet91 |
| l3leaf | leaf89 | Ethernet5 | spine | spine3 | Ethernet91 |
| l3leaf | leaf89 | Ethernet6 | spine | spine4 | Ethernet91 |
| l3leaf | leaf89 | Ethernet7 | spine | spine5 | Ethernet91 |
| l3leaf | leaf89 | Ethernet8 | spine | spine6 | Ethernet91 |
| l3leaf | leaf90 | Ethernet3 | spine | spine1 | Ethernet92 |
| l3leaf | leaf90 | Ethernet4 | spine | spine2 | Ethernet92 |
| l3leaf | leaf90 | Ethernet5 | spine | spine3 | Ethernet92 |
| l3leaf | leaf90 | Ethernet6 | spine | spine4 | Ethernet92 |
| l3leaf | leaf90 | Ethernet7 | spine | spine5 | Ethernet92 |
| l3leaf | leaf90 | Ethernet8 | spine | spine6 | Ethernet92 |
| l3leaf | leaf91 | Ethernet3 | spine | spine1 | Ethernet93 |
| l3leaf | leaf91 | Ethernet4 | spine | spine2 | Ethernet93 |
| l3leaf | leaf91 | Ethernet5 | spine | spine3 | Ethernet93 |
| l3leaf | leaf91 | Ethernet6 | spine | spine4 | Ethernet93 |
| l3leaf | leaf91 | Ethernet7 | spine | spine5 | Ethernet93 |
| l3leaf | leaf91 | Ethernet8 | spine | spine6 | Ethernet93 |
| l3leaf | leaf92 | Ethernet3 | spine | spine1 | Ethernet94 |
| l3leaf | leaf92 | Ethernet4 | spine | spine2 | Ethernet94 |
| l3leaf | leaf92 | Ethernet5 | spine | spine3 | Ethernet94 |
| l3leaf | leaf92 | Ethernet6 | spine | spine4 | Ethernet94 |
| l3leaf | leaf92 | Ethernet7 | spine | spine5 | Ethernet94 |
| l3leaf | leaf92 | Ethernet8 | spine | spine6 | Ethernet94 |
| l3leaf | leaf93 | Ethernet3 | spine | spine1 | Ethernet95 |
| l3leaf | leaf93 | Ethernet4 | spine | spine2 | Ethernet95 |
| l3leaf | leaf93 | Ethernet5 | spine | spine3 | Ethernet95 |
| l3leaf | leaf93 | Ethernet6 | spine | spine4 | Ethernet95 |
| l3leaf | leaf93 | Ethernet7 | spine | spine5 | Ethernet95 |
| l3leaf | leaf93 | Ethernet8 | spine | spine6 | Ethernet95 |
| l3leaf | leaf94 | Ethernet3 | spine | spine1 | Ethernet96 |
| l3leaf | leaf94 | Ethernet4 | spine | spine2 | Ethernet96 |
| l3leaf | leaf94 | Ethernet5 | spine | spine3 | Ethernet96 |
| l3leaf | leaf94 | Ethernet6 | spine | spine4 | Ethernet96 |
| l3leaf | leaf94 | Ethernet7 | spine | spine5 | Ethernet96 |
| l3leaf | leaf94 | Ethernet8 | spine | spine6 | Ethernet96 |
| l3leaf | leaf95 | Ethernet3 | spine | spine1 | Ethernet97 |
| l3leaf | leaf95 | Ethernet4 | spine | spine2 | Ethernet97 |
| l3leaf | leaf95 | Ethernet5 | spine | spine3 | Ethernet97 |
| l3leaf | leaf95 | Ethernet6 | spine | spine4 | Ethernet97 |
| l3leaf | leaf95 | Ethernet7 | spine | spine5 | Ethernet97 |
| l3leaf | leaf95 | Ethernet8 | spine | spine6 | Ethernet97 |
| l3leaf | leaf96 | Ethernet3 | spine | spine1 | Ethernet98 |
| l3leaf | leaf96 | Ethernet4 | spine | spine2 | Ethernet98 |
| l3leaf | leaf96 | Ethernet5 | spine | spine3 | Ethernet98 |
| l3leaf | leaf96 | Ethernet6 | spine | spine4 | Ethernet98 |
| l3leaf | leaf96 | Ethernet7 | spine | spine5 | Ethernet98 |
| l3leaf | leaf96 | Ethernet8 | spine | spine6 | Ethernet98 |
| l3leaf | leaf97 | Ethernet3 | spine | spine1 | Ethernet99 |
| l3leaf | leaf97 | Ethernet4 | spine | spine2 | Ethernet99 |
| l3leaf | leaf97 | Ethernet5 | spine | spine3 | Ethernet99 |
| l3leaf | leaf97 | Ethernet6 | spine | spine4 | Ethernet99 |
| l3leaf | leaf97 | Ethernet7 | spine | spine5 | Ethernet99 |
| l3leaf | leaf97 | Ethernet8 | spine | spine6 | Ethernet99 |
| l3leaf | leaf98 | Ethernet3 | spine | spine1 | Ethernet100 |
| l3leaf | leaf98 | Ethernet4 | spine | spine2 | Ethernet100 |
| l3leaf | leaf98 | Ethernet5 | spine | spine3 | Ethernet100 |
| l3leaf | leaf98 | Ethernet6 | spine | spine4 | Ethernet100 |
| l3leaf | leaf98 | Ethernet7 | spine | spine5 | Ethernet100 |
| l3leaf | leaf98 | Ethernet8 | spine | spine6 | Ethernet100 |
| l3leaf | leaf99 | Ethernet3 | spine | spine1 | Ethernet101 |
| l3leaf | leaf99 | Ethernet4 | spine | spine2 | Ethernet101 |
| l3leaf | leaf99 | Ethernet5 | spine | spine3 | Ethernet101 |
| l3leaf | leaf99 | Ethernet6 | spine | spine4 | Ethernet101 |
| l3leaf | leaf99 | Ethernet7 | spine | spine5 | Ethernet101 |
| l3leaf | leaf99 | Ethernet8 | spine | spine6 | Ethernet101 |
| spine | spine5 | Ethernet3 | l3leaf | leaf1 | Ethernet7 |
| spine | spine5 | Ethernet4 | l3leaf | leaf2 | Ethernet7 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.0.0/20 | 4096 | 1293 | 31.57 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| leaf1 | Ethernet3 | 192.168.0.1/31 | spine1 | Ethernet3 | 192.168.0.0/31 |
| leaf1 | Ethernet4 | 192.168.0.3/31 | spine2 | Ethernet3 | 192.168.0.2/31 |
| leaf1 | Ethernet5 | 192.168.0.5/31 | spine3 | Ethernet3 | 192.168.0.4/31 |
| leaf1 | Ethernet6 | 192.168.0.7/31 | spine4 | Ethernet3 | 192.168.0.6/31 |
| leaf1 | Ethernet8 | 192.168.0.11/31 | spine6 | Ethernet3 | 192.168.0.10/31 |
| leaf2 | Ethernet3 | 192.168.0.13/31 | spine1 | Ethernet4 | 192.168.0.12/31 |
| leaf2 | Ethernet4 | 192.168.0.15/31 | spine2 | Ethernet4 | 192.168.0.14/31 |
| leaf2 | Ethernet5 | 192.168.0.17/31 | spine3 | Ethernet4 | 192.168.0.16/31 |
| leaf2 | Ethernet6 | 192.168.0.19/31 | spine4 | Ethernet4 | 192.168.0.18/31 |
| leaf2 | Ethernet8 | 192.168.0.23/31 | spine6 | Ethernet4 | 192.168.0.22/31 |
| leaf3 | Ethernet3 | 192.168.0.25/31 | spine1 | Ethernet5 | 192.168.0.24/31 |
| leaf3 | Ethernet4 | 192.168.0.27/31 | spine2 | Ethernet5 | 192.168.0.26/31 |
| leaf3 | Ethernet5 | 192.168.0.29/31 | spine3 | Ethernet5 | 192.168.0.28/31 |
| leaf3 | Ethernet6 | 192.168.0.31/31 | spine4 | Ethernet5 | 192.168.0.30/31 |
| leaf3 | Ethernet7 | 192.168.0.33/31 | spine5 | Ethernet5 | 192.168.0.32/31 |
| leaf3 | Ethernet8 | 192.168.0.35/31 | spine6 | Ethernet5 | 192.168.0.34/31 |
| leaf4 | Ethernet3 | 192.168.0.37/31 | spine1 | Ethernet6 | 192.168.0.36/31 |
| leaf4 | Ethernet4 | 192.168.0.39/31 | spine2 | Ethernet6 | 192.168.0.38/31 |
| leaf4 | Ethernet5 | 192.168.0.41/31 | spine3 | Ethernet6 | 192.168.0.40/31 |
| leaf4 | Ethernet6 | 192.168.0.43/31 | spine4 | Ethernet6 | 192.168.0.42/31 |
| leaf4 | Ethernet7 | 192.168.0.45/31 | spine5 | Ethernet6 | 192.168.0.44/31 |
| leaf4 | Ethernet8 | 192.168.0.47/31 | spine6 | Ethernet6 | 192.168.0.46/31 |
| leaf5 | Ethernet3 | 192.168.0.49/31 | spine1 | Ethernet7 | 192.168.0.48/31 |
| leaf5 | Ethernet4 | 192.168.0.51/31 | spine2 | Ethernet7 | 192.168.0.50/31 |
| leaf5 | Ethernet5 | 192.168.0.53/31 | spine3 | Ethernet7 | 192.168.0.52/31 |
| leaf5 | Ethernet6 | 192.168.0.55/31 | spine4 | Ethernet7 | 192.168.0.54/31 |
| leaf5 | Ethernet7 | 192.168.0.57/31 | spine5 | Ethernet7 | 192.168.0.56/31 |
| leaf5 | Ethernet8 | 192.168.0.59/31 | spine6 | Ethernet7 | 192.168.0.58/31 |
| leaf6 | Ethernet3 | 192.168.0.61/31 | spine1 | Ethernet8 | 192.168.0.60/31 |
| leaf6 | Ethernet4 | 192.168.0.63/31 | spine2 | Ethernet8 | 192.168.0.62/31 |
| leaf6 | Ethernet5 | 192.168.0.65/31 | spine3 | Ethernet8 | 192.168.0.64/31 |
| leaf6 | Ethernet6 | 192.168.0.67/31 | spine4 | Ethernet8 | 192.168.0.66/31 |
| leaf6 | Ethernet7 | 192.168.0.69/31 | spine5 | Ethernet8 | 192.168.0.68/31 |
| leaf6 | Ethernet8 | 192.168.0.71/31 | spine6 | Ethernet8 | 192.168.0.70/31 |
| leaf7 | Ethernet3 | 192.168.0.73/31 | spine1 | Ethernet9 | 192.168.0.72/31 |
| leaf7 | Ethernet4 | 192.168.0.75/31 | spine2 | Ethernet9 | 192.168.0.74/31 |
| leaf7 | Ethernet5 | 192.168.0.77/31 | spine3 | Ethernet9 | 192.168.0.76/31 |
| leaf7 | Ethernet6 | 192.168.0.79/31 | spine4 | Ethernet9 | 192.168.0.78/31 |
| leaf7 | Ethernet7 | 192.168.0.81/31 | spine5 | Ethernet9 | 192.168.0.80/31 |
| leaf7 | Ethernet8 | 192.168.0.83/31 | spine6 | Ethernet9 | 192.168.0.82/31 |
| leaf8 | Ethernet3 | 192.168.0.85/31 | spine1 | Ethernet10 | 192.168.0.84/31 |
| leaf8 | Ethernet4 | 192.168.0.87/31 | spine2 | Ethernet10 | 192.168.0.86/31 |
| leaf8 | Ethernet5 | 192.168.0.89/31 | spine3 | Ethernet10 | 192.168.0.88/31 |
| leaf8 | Ethernet6 | 192.168.0.91/31 | spine4 | Ethernet10 | 192.168.0.90/31 |
| leaf8 | Ethernet7 | 192.168.0.93/31 | spine5 | Ethernet10 | 192.168.0.92/31 |
| leaf8 | Ethernet8 | 192.168.0.95/31 | spine6 | Ethernet10 | 192.168.0.94/31 |
| leaf9 | Ethernet3 | 192.168.0.97/31 | spine1 | Ethernet11 | 192.168.0.96/31 |
| leaf9 | Ethernet4 | 192.168.0.99/31 | spine2 | Ethernet11 | 192.168.0.98/31 |
| leaf9 | Ethernet5 | 192.168.0.101/31 | spine3 | Ethernet11 | 192.168.0.100/31 |
| leaf9 | Ethernet6 | 192.168.0.103/31 | spine4 | Ethernet11 | 192.168.0.102/31 |
| leaf9 | Ethernet7 | 192.168.0.105/31 | spine5 | Ethernet11 | 192.168.0.104/31 |
| leaf9 | Ethernet8 | 192.168.0.107/31 | spine6 | Ethernet11 | 192.168.0.106/31 |
| leaf10 | Ethernet3 | 192.168.0.109/31 | spine1 | Ethernet12 | 192.168.0.108/31 |
| leaf10 | Ethernet4 | 192.168.0.111/31 | spine2 | Ethernet12 | 192.168.0.110/31 |
| leaf10 | Ethernet5 | 192.168.0.113/31 | spine3 | Ethernet12 | 192.168.0.112/31 |
| leaf10 | Ethernet6 | 192.168.0.115/31 | spine4 | Ethernet12 | 192.168.0.114/31 |
| leaf10 | Ethernet7 | 192.168.0.117/31 | spine5 | Ethernet12 | 192.168.0.116/31 |
| leaf10 | Ethernet8 | 192.168.0.119/31 | spine6 | Ethernet12 | 192.168.0.118/31 |
| leaf11 | Ethernet3 | 192.168.0.121/31 | spine1 | Ethernet13 | 192.168.0.120/31 |
| leaf11 | Ethernet4 | 192.168.0.123/31 | spine2 | Ethernet13 | 192.168.0.122/31 |
| leaf11 | Ethernet5 | 192.168.0.125/31 | spine3 | Ethernet13 | 192.168.0.124/31 |
| leaf11 | Ethernet6 | 192.168.0.127/31 | spine4 | Ethernet13 | 192.168.0.126/31 |
| leaf11 | Ethernet7 | 192.168.0.129/31 | spine5 | Ethernet13 | 192.168.0.128/31 |
| leaf11 | Ethernet8 | 192.168.0.131/31 | spine6 | Ethernet13 | 192.168.0.130/31 |
| leaf12 | Ethernet3 | 192.168.0.133/31 | spine1 | Ethernet14 | 192.168.0.132/31 |
| leaf12 | Ethernet4 | 192.168.0.135/31 | spine2 | Ethernet14 | 192.168.0.134/31 |
| leaf12 | Ethernet5 | 192.168.0.137/31 | spine3 | Ethernet14 | 192.168.0.136/31 |
| leaf12 | Ethernet6 | 192.168.0.139/31 | spine4 | Ethernet14 | 192.168.0.138/31 |
| leaf12 | Ethernet7 | 192.168.0.141/31 | spine5 | Ethernet14 | 192.168.0.140/31 |
| leaf12 | Ethernet8 | 192.168.0.143/31 | spine6 | Ethernet14 | 192.168.0.142/31 |
| leaf13 | Ethernet3 | 192.168.0.145/31 | spine1 | Ethernet15 | 192.168.0.144/31 |
| leaf13 | Ethernet4 | 192.168.0.147/31 | spine2 | Ethernet15 | 192.168.0.146/31 |
| leaf13 | Ethernet5 | 192.168.0.149/31 | spine3 | Ethernet15 | 192.168.0.148/31 |
| leaf13 | Ethernet6 | 192.168.0.151/31 | spine4 | Ethernet15 | 192.168.0.150/31 |
| leaf13 | Ethernet7 | 192.168.0.153/31 | spine5 | Ethernet15 | 192.168.0.152/31 |
| leaf13 | Ethernet8 | 192.168.0.155/31 | spine6 | Ethernet15 | 192.168.0.154/31 |
| leaf14 | Ethernet3 | 192.168.0.157/31 | spine1 | Ethernet16 | 192.168.0.156/31 |
| leaf14 | Ethernet4 | 192.168.0.159/31 | spine2 | Ethernet16 | 192.168.0.158/31 |
| leaf14 | Ethernet5 | 192.168.0.161/31 | spine3 | Ethernet16 | 192.168.0.160/31 |
| leaf14 | Ethernet6 | 192.168.0.163/31 | spine4 | Ethernet16 | 192.168.0.162/31 |
| leaf14 | Ethernet7 | 192.168.0.165/31 | spine5 | Ethernet16 | 192.168.0.164/31 |
| leaf14 | Ethernet8 | 192.168.0.167/31 | spine6 | Ethernet16 | 192.168.0.166/31 |
| leaf15 | Ethernet3 | 192.168.0.169/31 | spine1 | Ethernet17 | 192.168.0.168/31 |
| leaf15 | Ethernet4 | 192.168.0.171/31 | spine2 | Ethernet17 | 192.168.0.170/31 |
| leaf15 | Ethernet5 | 192.168.0.173/31 | spine3 | Ethernet17 | 192.168.0.172/31 |
| leaf15 | Ethernet6 | 192.168.0.175/31 | spine4 | Ethernet17 | 192.168.0.174/31 |
| leaf15 | Ethernet7 | 192.168.0.177/31 | spine5 | Ethernet17 | 192.168.0.176/31 |
| leaf15 | Ethernet8 | 192.168.0.179/31 | spine6 | Ethernet17 | 192.168.0.178/31 |
| leaf16 | Ethernet3 | 192.168.0.181/31 | spine1 | Ethernet18 | 192.168.0.180/31 |
| leaf16 | Ethernet4 | 192.168.0.183/31 | spine2 | Ethernet18 | 192.168.0.182/31 |
| leaf16 | Ethernet5 | 192.168.0.185/31 | spine3 | Ethernet18 | 192.168.0.184/31 |
| leaf16 | Ethernet6 | 192.168.0.187/31 | spine4 | Ethernet18 | 192.168.0.186/31 |
| leaf16 | Ethernet7 | 192.168.0.189/31 | spine5 | Ethernet18 | 192.168.0.188/31 |
| leaf16 | Ethernet8 | 192.168.0.191/31 | spine6 | Ethernet18 | 192.168.0.190/31 |
| leaf17 | Ethernet3 | 192.168.0.193/31 | spine1 | Ethernet19 | 192.168.0.192/31 |
| leaf17 | Ethernet4 | 192.168.0.195/31 | spine2 | Ethernet19 | 192.168.0.194/31 |
| leaf17 | Ethernet5 | 192.168.0.197/31 | spine3 | Ethernet19 | 192.168.0.196/31 |
| leaf17 | Ethernet6 | 192.168.0.199/31 | spine4 | Ethernet19 | 192.168.0.198/31 |
| leaf17 | Ethernet7 | 192.168.0.201/31 | spine5 | Ethernet19 | 192.168.0.200/31 |
| leaf17 | Ethernet8 | 192.168.0.203/31 | spine6 | Ethernet19 | 192.168.0.202/31 |
| leaf18 | Ethernet3 | 192.168.0.205/31 | spine1 | Ethernet20 | 192.168.0.204/31 |
| leaf18 | Ethernet4 | 192.168.0.207/31 | spine2 | Ethernet20 | 192.168.0.206/31 |
| leaf18 | Ethernet5 | 192.168.0.209/31 | spine3 | Ethernet20 | 192.168.0.208/31 |
| leaf18 | Ethernet6 | 192.168.0.211/31 | spine4 | Ethernet20 | 192.168.0.210/31 |
| leaf18 | Ethernet7 | 192.168.0.213/31 | spine5 | Ethernet20 | 192.168.0.212/31 |
| leaf18 | Ethernet8 | 192.168.0.215/31 | spine6 | Ethernet20 | 192.168.0.214/31 |
| leaf19 | Ethernet3 | 192.168.0.217/31 | spine1 | Ethernet21 | 192.168.0.216/31 |
| leaf19 | Ethernet4 | 192.168.0.219/31 | spine2 | Ethernet21 | 192.168.0.218/31 |
| leaf19 | Ethernet5 | 192.168.0.221/31 | spine3 | Ethernet21 | 192.168.0.220/31 |
| leaf19 | Ethernet6 | 192.168.0.223/31 | spine4 | Ethernet21 | 192.168.0.222/31 |
| leaf19 | Ethernet7 | 192.168.0.225/31 | spine5 | Ethernet21 | 192.168.0.224/31 |
| leaf19 | Ethernet8 | 192.168.0.227/31 | spine6 | Ethernet21 | 192.168.0.226/31 |
| leaf20 | Ethernet3 | 192.168.0.229/31 | spine1 | Ethernet22 | 192.168.0.228/31 |
| leaf20 | Ethernet4 | 192.168.0.231/31 | spine2 | Ethernet22 | 192.168.0.230/31 |
| leaf20 | Ethernet5 | 192.168.0.233/31 | spine3 | Ethernet22 | 192.168.0.232/31 |
| leaf20 | Ethernet6 | 192.168.0.235/31 | spine4 | Ethernet22 | 192.168.0.234/31 |
| leaf20 | Ethernet7 | 192.168.0.237/31 | spine5 | Ethernet22 | 192.168.0.236/31 |
| leaf20 | Ethernet8 | 192.168.0.239/31 | spine6 | Ethernet22 | 192.168.0.238/31 |
| leaf21 | Ethernet3 | 192.168.0.241/31 | spine1 | Ethernet23 | 192.168.0.240/31 |
| leaf21 | Ethernet4 | 192.168.0.243/31 | spine2 | Ethernet23 | 192.168.0.242/31 |
| leaf21 | Ethernet5 | 192.168.0.245/31 | spine3 | Ethernet23 | 192.168.0.244/31 |
| leaf21 | Ethernet6 | 192.168.0.247/31 | spine4 | Ethernet23 | 192.168.0.246/31 |
| leaf21 | Ethernet7 | 192.168.0.249/31 | spine5 | Ethernet23 | 192.168.0.248/31 |
| leaf21 | Ethernet8 | 192.168.0.251/31 | spine6 | Ethernet23 | 192.168.0.250/31 |
| leaf22 | Ethernet3 | 192.168.0.253/31 | spine1 | Ethernet24 | 192.168.0.252/31 |
| leaf22 | Ethernet4 | 192.168.0.255/31 | spine2 | Ethernet24 | 192.168.0.254/31 |
| leaf22 | Ethernet5 | 192.168.1.1/31 | spine3 | Ethernet24 | 192.168.1.0/31 |
| leaf22 | Ethernet6 | 192.168.1.3/31 | spine4 | Ethernet24 | 192.168.1.2/31 |
| leaf22 | Ethernet7 | 192.168.1.5/31 | spine5 | Ethernet24 | 192.168.1.4/31 |
| leaf22 | Ethernet8 | 192.168.1.7/31 | spine6 | Ethernet24 | 192.168.1.6/31 |
| leaf23 | Ethernet3 | 192.168.1.9/31 | spine1 | Ethernet25 | 192.168.1.8/31 |
| leaf23 | Ethernet4 | 192.168.1.11/31 | spine2 | Ethernet25 | 192.168.1.10/31 |
| leaf23 | Ethernet5 | 192.168.1.13/31 | spine3 | Ethernet25 | 192.168.1.12/31 |
| leaf23 | Ethernet6 | 192.168.1.15/31 | spine4 | Ethernet25 | 192.168.1.14/31 |
| leaf23 | Ethernet7 | 192.168.1.17/31 | spine5 | Ethernet25 | 192.168.1.16/31 |
| leaf23 | Ethernet8 | 192.168.1.19/31 | spine6 | Ethernet25 | 192.168.1.18/31 |
| leaf24 | Ethernet3 | 192.168.1.21/31 | spine1 | Ethernet26 | 192.168.1.20/31 |
| leaf24 | Ethernet4 | 192.168.1.23/31 | spine2 | Ethernet26 | 192.168.1.22/31 |
| leaf24 | Ethernet5 | 192.168.1.25/31 | spine3 | Ethernet26 | 192.168.1.24/31 |
| leaf24 | Ethernet6 | 192.168.1.27/31 | spine4 | Ethernet26 | 192.168.1.26/31 |
| leaf24 | Ethernet7 | 192.168.1.29/31 | spine5 | Ethernet26 | 192.168.1.28/31 |
| leaf24 | Ethernet8 | 192.168.1.31/31 | spine6 | Ethernet26 | 192.168.1.30/31 |
| leaf25 | Ethernet3 | 192.168.1.33/31 | spine1 | Ethernet27 | 192.168.1.32/31 |
| leaf25 | Ethernet4 | 192.168.1.35/31 | spine2 | Ethernet27 | 192.168.1.34/31 |
| leaf25 | Ethernet5 | 192.168.1.37/31 | spine3 | Ethernet27 | 192.168.1.36/31 |
| leaf25 | Ethernet6 | 192.168.1.39/31 | spine4 | Ethernet27 | 192.168.1.38/31 |
| leaf25 | Ethernet7 | 192.168.1.41/31 | spine5 | Ethernet27 | 192.168.1.40/31 |
| leaf25 | Ethernet8 | 192.168.1.43/31 | spine6 | Ethernet27 | 192.168.1.42/31 |
| leaf26 | Ethernet3 | 192.168.1.45/31 | spine1 | Ethernet28 | 192.168.1.44/31 |
| leaf26 | Ethernet4 | 192.168.1.47/31 | spine2 | Ethernet28 | 192.168.1.46/31 |
| leaf26 | Ethernet5 | 192.168.1.49/31 | spine3 | Ethernet28 | 192.168.1.48/31 |
| leaf26 | Ethernet6 | 192.168.1.51/31 | spine4 | Ethernet28 | 192.168.1.50/31 |
| leaf26 | Ethernet7 | 192.168.1.53/31 | spine5 | Ethernet28 | 192.168.1.52/31 |
| leaf26 | Ethernet8 | 192.168.1.55/31 | spine6 | Ethernet28 | 192.168.1.54/31 |
| leaf27 | Ethernet3 | 192.168.1.57/31 | spine1 | Ethernet29 | 192.168.1.56/31 |
| leaf27 | Ethernet4 | 192.168.1.59/31 | spine2 | Ethernet29 | 192.168.1.58/31 |
| leaf27 | Ethernet5 | 192.168.1.61/31 | spine3 | Ethernet29 | 192.168.1.60/31 |
| leaf27 | Ethernet6 | 192.168.1.63/31 | spine4 | Ethernet29 | 192.168.1.62/31 |
| leaf27 | Ethernet7 | 192.168.1.65/31 | spine5 | Ethernet29 | 192.168.1.64/31 |
| leaf27 | Ethernet8 | 192.168.1.67/31 | spine6 | Ethernet29 | 192.168.1.66/31 |
| leaf28 | Ethernet3 | 192.168.1.69/31 | spine1 | Ethernet30 | 192.168.1.68/31 |
| leaf28 | Ethernet4 | 192.168.1.71/31 | spine2 | Ethernet30 | 192.168.1.70/31 |
| leaf28 | Ethernet5 | 192.168.1.73/31 | spine3 | Ethernet30 | 192.168.1.72/31 |
| leaf28 | Ethernet6 | 192.168.1.75/31 | spine4 | Ethernet30 | 192.168.1.74/31 |
| leaf28 | Ethernet7 | 192.168.1.77/31 | spine5 | Ethernet30 | 192.168.1.76/31 |
| leaf28 | Ethernet8 | 192.168.1.79/31 | spine6 | Ethernet30 | 192.168.1.78/31 |
| leaf29 | Ethernet3 | 192.168.1.81/31 | spine1 | Ethernet31 | 192.168.1.80/31 |
| leaf29 | Ethernet4 | 192.168.1.83/31 | spine2 | Ethernet31 | 192.168.1.82/31 |
| leaf29 | Ethernet5 | 192.168.1.85/31 | spine3 | Ethernet31 | 192.168.1.84/31 |
| leaf29 | Ethernet6 | 192.168.1.87/31 | spine4 | Ethernet31 | 192.168.1.86/31 |
| leaf29 | Ethernet7 | 192.168.1.89/31 | spine5 | Ethernet31 | 192.168.1.88/31 |
| leaf29 | Ethernet8 | 192.168.1.91/31 | spine6 | Ethernet31 | 192.168.1.90/31 |
| leaf30 | Ethernet3 | 192.168.1.93/31 | spine1 | Ethernet32 | 192.168.1.92/31 |
| leaf30 | Ethernet4 | 192.168.1.95/31 | spine2 | Ethernet32 | 192.168.1.94/31 |
| leaf30 | Ethernet5 | 192.168.1.97/31 | spine3 | Ethernet32 | 192.168.1.96/31 |
| leaf30 | Ethernet6 | 192.168.1.99/31 | spine4 | Ethernet32 | 192.168.1.98/31 |
| leaf30 | Ethernet7 | 192.168.1.101/31 | spine5 | Ethernet32 | 192.168.1.100/31 |
| leaf30 | Ethernet8 | 192.168.1.103/31 | spine6 | Ethernet32 | 192.168.1.102/31 |
| leaf31 | Ethernet3 | 192.168.1.105/31 | spine1 | Ethernet33 | 192.168.1.104/31 |
| leaf31 | Ethernet4 | 192.168.1.107/31 | spine2 | Ethernet33 | 192.168.1.106/31 |
| leaf31 | Ethernet5 | 192.168.1.109/31 | spine3 | Ethernet33 | 192.168.1.108/31 |
| leaf31 | Ethernet6 | 192.168.1.111/31 | spine4 | Ethernet33 | 192.168.1.110/31 |
| leaf31 | Ethernet7 | 192.168.1.113/31 | spine5 | Ethernet33 | 192.168.1.112/31 |
| leaf31 | Ethernet8 | 192.168.1.115/31 | spine6 | Ethernet33 | 192.168.1.114/31 |
| leaf32 | Ethernet3 | 192.168.1.117/31 | spine1 | Ethernet34 | 192.168.1.116/31 |
| leaf32 | Ethernet4 | 192.168.1.119/31 | spine2 | Ethernet34 | 192.168.1.118/31 |
| leaf32 | Ethernet5 | 192.168.1.121/31 | spine3 | Ethernet34 | 192.168.1.120/31 |
| leaf32 | Ethernet6 | 192.168.1.123/31 | spine4 | Ethernet34 | 192.168.1.122/31 |
| leaf32 | Ethernet7 | 192.168.1.125/31 | spine5 | Ethernet34 | 192.168.1.124/31 |
| leaf32 | Ethernet8 | 192.168.1.127/31 | spine6 | Ethernet34 | 192.168.1.126/31 |
| leaf33 | Ethernet3 | 192.168.1.129/31 | spine1 | Ethernet35 | 192.168.1.128/31 |
| leaf33 | Ethernet4 | 192.168.1.131/31 | spine2 | Ethernet35 | 192.168.1.130/31 |
| leaf33 | Ethernet5 | 192.168.1.133/31 | spine3 | Ethernet35 | 192.168.1.132/31 |
| leaf33 | Ethernet6 | 192.168.1.135/31 | spine4 | Ethernet35 | 192.168.1.134/31 |
| leaf33 | Ethernet7 | 192.168.1.137/31 | spine5 | Ethernet35 | 192.168.1.136/31 |
| leaf33 | Ethernet8 | 192.168.1.139/31 | spine6 | Ethernet35 | 192.168.1.138/31 |
| leaf34 | Ethernet3 | 192.168.1.141/31 | spine1 | Ethernet36 | 192.168.1.140/31 |
| leaf34 | Ethernet4 | 192.168.1.143/31 | spine2 | Ethernet36 | 192.168.1.142/31 |
| leaf34 | Ethernet5 | 192.168.1.145/31 | spine3 | Ethernet36 | 192.168.1.144/31 |
| leaf34 | Ethernet6 | 192.168.1.147/31 | spine4 | Ethernet36 | 192.168.1.146/31 |
| leaf34 | Ethernet7 | 192.168.1.149/31 | spine5 | Ethernet36 | 192.168.1.148/31 |
| leaf34 | Ethernet8 | 192.168.1.151/31 | spine6 | Ethernet36 | 192.168.1.150/31 |
| leaf35 | Ethernet3 | 192.168.1.153/31 | spine1 | Ethernet37 | 192.168.1.152/31 |
| leaf35 | Ethernet4 | 192.168.1.155/31 | spine2 | Ethernet37 | 192.168.1.154/31 |
| leaf35 | Ethernet5 | 192.168.1.157/31 | spine3 | Ethernet37 | 192.168.1.156/31 |
| leaf35 | Ethernet6 | 192.168.1.159/31 | spine4 | Ethernet37 | 192.168.1.158/31 |
| leaf35 | Ethernet7 | 192.168.1.161/31 | spine5 | Ethernet37 | 192.168.1.160/31 |
| leaf35 | Ethernet8 | 192.168.1.163/31 | spine6 | Ethernet37 | 192.168.1.162/31 |
| leaf36 | Ethernet3 | 192.168.1.165/31 | spine1 | Ethernet38 | 192.168.1.164/31 |
| leaf36 | Ethernet4 | 192.168.1.167/31 | spine2 | Ethernet38 | 192.168.1.166/31 |
| leaf36 | Ethernet5 | 192.168.1.169/31 | spine3 | Ethernet38 | 192.168.1.168/31 |
| leaf36 | Ethernet6 | 192.168.1.171/31 | spine4 | Ethernet38 | 192.168.1.170/31 |
| leaf36 | Ethernet7 | 192.168.1.173/31 | spine5 | Ethernet38 | 192.168.1.172/31 |
| leaf36 | Ethernet8 | 192.168.1.175/31 | spine6 | Ethernet38 | 192.168.1.174/31 |
| leaf37 | Ethernet3 | 192.168.1.177/31 | spine1 | Ethernet39 | 192.168.1.176/31 |
| leaf37 | Ethernet4 | 192.168.1.179/31 | spine2 | Ethernet39 | 192.168.1.178/31 |
| leaf37 | Ethernet5 | 192.168.1.181/31 | spine3 | Ethernet39 | 192.168.1.180/31 |
| leaf37 | Ethernet6 | 192.168.1.183/31 | spine4 | Ethernet39 | 192.168.1.182/31 |
| leaf37 | Ethernet7 | 192.168.1.185/31 | spine5 | Ethernet39 | 192.168.1.184/31 |
| leaf37 | Ethernet8 | 192.168.1.187/31 | spine6 | Ethernet39 | 192.168.1.186/31 |
| leaf38 | Ethernet3 | 192.168.1.189/31 | spine1 | Ethernet40 | 192.168.1.188/31 |
| leaf38 | Ethernet4 | 192.168.1.191/31 | spine2 | Ethernet40 | 192.168.1.190/31 |
| leaf38 | Ethernet5 | 192.168.1.193/31 | spine3 | Ethernet40 | 192.168.1.192/31 |
| leaf38 | Ethernet6 | 192.168.1.195/31 | spine4 | Ethernet40 | 192.168.1.194/31 |
| leaf38 | Ethernet7 | 192.168.1.197/31 | spine5 | Ethernet40 | 192.168.1.196/31 |
| leaf38 | Ethernet8 | 192.168.1.199/31 | spine6 | Ethernet40 | 192.168.1.198/31 |
| leaf39 | Ethernet3 | 192.168.1.201/31 | spine1 | Ethernet41 | 192.168.1.200/31 |
| leaf39 | Ethernet4 | 192.168.1.203/31 | spine2 | Ethernet41 | 192.168.1.202/31 |
| leaf39 | Ethernet5 | 192.168.1.205/31 | spine3 | Ethernet41 | 192.168.1.204/31 |
| leaf39 | Ethernet6 | 192.168.1.207/31 | spine4 | Ethernet41 | 192.168.1.206/31 |
| leaf39 | Ethernet7 | 192.168.1.209/31 | spine5 | Ethernet41 | 192.168.1.208/31 |
| leaf39 | Ethernet8 | 192.168.1.211/31 | spine6 | Ethernet41 | 192.168.1.210/31 |
| leaf40 | Ethernet3 | 192.168.1.213/31 | spine1 | Ethernet42 | 192.168.1.212/31 |
| leaf40 | Ethernet4 | 192.168.1.215/31 | spine2 | Ethernet42 | 192.168.1.214/31 |
| leaf40 | Ethernet5 | 192.168.1.217/31 | spine3 | Ethernet42 | 192.168.1.216/31 |
| leaf40 | Ethernet6 | 192.168.1.219/31 | spine4 | Ethernet42 | 192.168.1.218/31 |
| leaf40 | Ethernet7 | 192.168.1.221/31 | spine5 | Ethernet42 | 192.168.1.220/31 |
| leaf40 | Ethernet8 | 192.168.1.223/31 | spine6 | Ethernet42 | 192.168.1.222/31 |
| leaf41 | Ethernet3 | 192.168.1.225/31 | spine1 | Ethernet43 | 192.168.1.224/31 |
| leaf41 | Ethernet4 | 192.168.1.227/31 | spine2 | Ethernet43 | 192.168.1.226/31 |
| leaf41 | Ethernet5 | 192.168.1.229/31 | spine3 | Ethernet43 | 192.168.1.228/31 |
| leaf41 | Ethernet6 | 192.168.1.231/31 | spine4 | Ethernet43 | 192.168.1.230/31 |
| leaf41 | Ethernet7 | 192.168.1.233/31 | spine5 | Ethernet43 | 192.168.1.232/31 |
| leaf41 | Ethernet8 | 192.168.1.235/31 | spine6 | Ethernet43 | 192.168.1.234/31 |
| leaf42 | Ethernet3 | 192.168.1.237/31 | spine1 | Ethernet44 | 192.168.1.236/31 |
| leaf42 | Ethernet4 | 192.168.1.239/31 | spine2 | Ethernet44 | 192.168.1.238/31 |
| leaf42 | Ethernet5 | 192.168.1.241/31 | spine3 | Ethernet44 | 192.168.1.240/31 |
| leaf42 | Ethernet6 | 192.168.1.243/31 | spine4 | Ethernet44 | 192.168.1.242/31 |
| leaf42 | Ethernet7 | 192.168.1.245/31 | spine5 | Ethernet44 | 192.168.1.244/31 |
| leaf42 | Ethernet8 | 192.168.1.247/31 | spine6 | Ethernet44 | 192.168.1.246/31 |
| leaf43 | Ethernet3 | 192.168.1.249/31 | spine1 | Ethernet45 | 192.168.1.248/31 |
| leaf43 | Ethernet4 | 192.168.1.251/31 | spine2 | Ethernet45 | 192.168.1.250/31 |
| leaf43 | Ethernet5 | 192.168.1.253/31 | spine3 | Ethernet45 | 192.168.1.252/31 |
| leaf43 | Ethernet6 | 192.168.1.255/31 | spine4 | Ethernet45 | 192.168.1.254/31 |
| leaf43 | Ethernet7 | 192.168.2.1/31 | spine5 | Ethernet45 | 192.168.2.0/31 |
| leaf43 | Ethernet8 | 192.168.2.3/31 | spine6 | Ethernet45 | 192.168.2.2/31 |
| leaf44 | Ethernet3 | 192.168.2.5/31 | spine1 | Ethernet46 | 192.168.2.4/31 |
| leaf44 | Ethernet4 | 192.168.2.7/31 | spine2 | Ethernet46 | 192.168.2.6/31 |
| leaf44 | Ethernet5 | 192.168.2.9/31 | spine3 | Ethernet46 | 192.168.2.8/31 |
| leaf44 | Ethernet6 | 192.168.2.11/31 | spine4 | Ethernet46 | 192.168.2.10/31 |
| leaf44 | Ethernet7 | 192.168.2.13/31 | spine5 | Ethernet46 | 192.168.2.12/31 |
| leaf44 | Ethernet8 | 192.168.2.15/31 | spine6 | Ethernet46 | 192.168.2.14/31 |
| leaf45 | Ethernet3 | 192.168.2.17/31 | spine1 | Ethernet47 | 192.168.2.16/31 |
| leaf45 | Ethernet4 | 192.168.2.19/31 | spine2 | Ethernet47 | 192.168.2.18/31 |
| leaf45 | Ethernet5 | 192.168.2.21/31 | spine3 | Ethernet47 | 192.168.2.20/31 |
| leaf45 | Ethernet6 | 192.168.2.23/31 | spine4 | Ethernet47 | 192.168.2.22/31 |
| leaf45 | Ethernet7 | 192.168.2.25/31 | spine5 | Ethernet47 | 192.168.2.24/31 |
| leaf45 | Ethernet8 | 192.168.2.27/31 | spine6 | Ethernet47 | 192.168.2.26/31 |
| leaf46 | Ethernet3 | 192.168.2.29/31 | spine1 | Ethernet48 | 192.168.2.28/31 |
| leaf46 | Ethernet4 | 192.168.2.31/31 | spine2 | Ethernet48 | 192.168.2.30/31 |
| leaf46 | Ethernet5 | 192.168.2.33/31 | spine3 | Ethernet48 | 192.168.2.32/31 |
| leaf46 | Ethernet6 | 192.168.2.35/31 | spine4 | Ethernet48 | 192.168.2.34/31 |
| leaf46 | Ethernet7 | 192.168.2.37/31 | spine5 | Ethernet48 | 192.168.2.36/31 |
| leaf46 | Ethernet8 | 192.168.2.39/31 | spine6 | Ethernet48 | 192.168.2.38/31 |
| leaf47 | Ethernet3 | 192.168.2.41/31 | spine1 | Ethernet49 | 192.168.2.40/31 |
| leaf47 | Ethernet4 | 192.168.2.43/31 | spine2 | Ethernet49 | 192.168.2.42/31 |
| leaf47 | Ethernet5 | 192.168.2.45/31 | spine3 | Ethernet49 | 192.168.2.44/31 |
| leaf47 | Ethernet6 | 192.168.2.47/31 | spine4 | Ethernet49 | 192.168.2.46/31 |
| leaf47 | Ethernet7 | 192.168.2.49/31 | spine5 | Ethernet49 | 192.168.2.48/31 |
| leaf47 | Ethernet8 | 192.168.2.51/31 | spine6 | Ethernet49 | 192.168.2.50/31 |
| leaf48 | Ethernet3 | 192.168.2.53/31 | spine1 | Ethernet50 | 192.168.2.52/31 |
| leaf48 | Ethernet4 | 192.168.2.55/31 | spine2 | Ethernet50 | 192.168.2.54/31 |
| leaf48 | Ethernet5 | 192.168.2.57/31 | spine3 | Ethernet50 | 192.168.2.56/31 |
| leaf48 | Ethernet6 | 192.168.2.59/31 | spine4 | Ethernet50 | 192.168.2.58/31 |
| leaf48 | Ethernet7 | 192.168.2.61/31 | spine5 | Ethernet50 | 192.168.2.60/31 |
| leaf48 | Ethernet8 | 192.168.2.63/31 | spine6 | Ethernet50 | 192.168.2.62/31 |
| leaf49 | Ethernet3 | 192.168.2.65/31 | spine1 | Ethernet51 | 192.168.2.64/31 |
| leaf49 | Ethernet4 | 192.168.2.67/31 | spine2 | Ethernet51 | 192.168.2.66/31 |
| leaf49 | Ethernet5 | 192.168.2.69/31 | spine3 | Ethernet51 | 192.168.2.68/31 |
| leaf49 | Ethernet6 | 192.168.2.71/31 | spine4 | Ethernet51 | 192.168.2.70/31 |
| leaf49 | Ethernet7 | 192.168.2.73/31 | spine5 | Ethernet51 | 192.168.2.72/31 |
| leaf49 | Ethernet8 | 192.168.2.75/31 | spine6 | Ethernet51 | 192.168.2.74/31 |
| leaf50 | Ethernet3 | 192.168.2.77/31 | spine1 | Ethernet52 | 192.168.2.76/31 |
| leaf50 | Ethernet4 | 192.168.2.79/31 | spine2 | Ethernet52 | 192.168.2.78/31 |
| leaf50 | Ethernet5 | 192.168.2.81/31 | spine3 | Ethernet52 | 192.168.2.80/31 |
| leaf50 | Ethernet6 | 192.168.2.83/31 | spine4 | Ethernet52 | 192.168.2.82/31 |
| leaf50 | Ethernet7 | 192.168.2.85/31 | spine5 | Ethernet52 | 192.168.2.84/31 |
| leaf50 | Ethernet8 | 192.168.2.87/31 | spine6 | Ethernet52 | 192.168.2.86/31 |
| leaf51 | Ethernet3 | 192.168.2.89/31 | spine1 | Ethernet53 | 192.168.2.88/31 |
| leaf51 | Ethernet4 | 192.168.2.91/31 | spine2 | Ethernet53 | 192.168.2.90/31 |
| leaf51 | Ethernet5 | 192.168.2.93/31 | spine3 | Ethernet53 | 192.168.2.92/31 |
| leaf51 | Ethernet6 | 192.168.2.95/31 | spine4 | Ethernet53 | 192.168.2.94/31 |
| leaf51 | Ethernet7 | 192.168.2.97/31 | spine5 | Ethernet53 | 192.168.2.96/31 |
| leaf51 | Ethernet8 | 192.168.2.99/31 | spine6 | Ethernet53 | 192.168.2.98/31 |
| leaf52 | Ethernet3 | 192.168.2.101/31 | spine1 | Ethernet54 | 192.168.2.100/31 |
| leaf52 | Ethernet4 | 192.168.2.103/31 | spine2 | Ethernet54 | 192.168.2.102/31 |
| leaf52 | Ethernet5 | 192.168.2.105/31 | spine3 | Ethernet54 | 192.168.2.104/31 |
| leaf52 | Ethernet6 | 192.168.2.107/31 | spine4 | Ethernet54 | 192.168.2.106/31 |
| leaf52 | Ethernet7 | 192.168.2.109/31 | spine5 | Ethernet54 | 192.168.2.108/31 |
| leaf52 | Ethernet8 | 192.168.2.111/31 | spine6 | Ethernet54 | 192.168.2.110/31 |
| leaf53 | Ethernet3 | 192.168.2.113/31 | spine1 | Ethernet55 | 192.168.2.112/31 |
| leaf53 | Ethernet4 | 192.168.2.115/31 | spine2 | Ethernet55 | 192.168.2.114/31 |
| leaf53 | Ethernet5 | 192.168.2.117/31 | spine3 | Ethernet55 | 192.168.2.116/31 |
| leaf53 | Ethernet6 | 192.168.2.119/31 | spine4 | Ethernet55 | 192.168.2.118/31 |
| leaf53 | Ethernet7 | 192.168.2.121/31 | spine5 | Ethernet55 | 192.168.2.120/31 |
| leaf53 | Ethernet8 | 192.168.2.123/31 | spine6 | Ethernet55 | 192.168.2.122/31 |
| leaf54 | Ethernet3 | 192.168.2.125/31 | spine1 | Ethernet56 | 192.168.2.124/31 |
| leaf54 | Ethernet4 | 192.168.2.127/31 | spine2 | Ethernet56 | 192.168.2.126/31 |
| leaf54 | Ethernet5 | 192.168.2.129/31 | spine3 | Ethernet56 | 192.168.2.128/31 |
| leaf54 | Ethernet6 | 192.168.2.131/31 | spine4 | Ethernet56 | 192.168.2.130/31 |
| leaf54 | Ethernet7 | 192.168.2.133/31 | spine5 | Ethernet56 | 192.168.2.132/31 |
| leaf54 | Ethernet8 | 192.168.2.135/31 | spine6 | Ethernet56 | 192.168.2.134/31 |
| leaf55 | Ethernet3 | 192.168.2.137/31 | spine1 | Ethernet57 | 192.168.2.136/31 |
| leaf55 | Ethernet4 | 192.168.2.139/31 | spine2 | Ethernet57 | 192.168.2.138/31 |
| leaf55 | Ethernet5 | 192.168.2.141/31 | spine3 | Ethernet57 | 192.168.2.140/31 |
| leaf55 | Ethernet6 | 192.168.2.143/31 | spine4 | Ethernet57 | 192.168.2.142/31 |
| leaf55 | Ethernet7 | 192.168.2.145/31 | spine5 | Ethernet57 | 192.168.2.144/31 |
| leaf55 | Ethernet8 | 192.168.2.147/31 | spine6 | Ethernet57 | 192.168.2.146/31 |
| leaf56 | Ethernet3 | 192.168.2.149/31 | spine1 | Ethernet58 | 192.168.2.148/31 |
| leaf56 | Ethernet4 | 192.168.2.151/31 | spine2 | Ethernet58 | 192.168.2.150/31 |
| leaf56 | Ethernet5 | 192.168.2.153/31 | spine3 | Ethernet58 | 192.168.2.152/31 |
| leaf56 | Ethernet6 | 192.168.2.155/31 | spine4 | Ethernet58 | 192.168.2.154/31 |
| leaf56 | Ethernet7 | 192.168.2.157/31 | spine5 | Ethernet58 | 192.168.2.156/31 |
| leaf56 | Ethernet8 | 192.168.2.159/31 | spine6 | Ethernet58 | 192.168.2.158/31 |
| leaf57 | Ethernet3 | 192.168.2.161/31 | spine1 | Ethernet59 | 192.168.2.160/31 |
| leaf57 | Ethernet4 | 192.168.2.163/31 | spine2 | Ethernet59 | 192.168.2.162/31 |
| leaf57 | Ethernet5 | 192.168.2.165/31 | spine3 | Ethernet59 | 192.168.2.164/31 |
| leaf57 | Ethernet6 | 192.168.2.167/31 | spine4 | Ethernet59 | 192.168.2.166/31 |
| leaf57 | Ethernet7 | 192.168.2.169/31 | spine5 | Ethernet59 | 192.168.2.168/31 |
| leaf57 | Ethernet8 | 192.168.2.171/31 | spine6 | Ethernet59 | 192.168.2.170/31 |
| leaf58 | Ethernet3 | 192.168.2.173/31 | spine1 | Ethernet60 | 192.168.2.172/31 |
| leaf58 | Ethernet4 | 192.168.2.175/31 | spine2 | Ethernet60 | 192.168.2.174/31 |
| leaf58 | Ethernet5 | 192.168.2.177/31 | spine3 | Ethernet60 | 192.168.2.176/31 |
| leaf58 | Ethernet6 | 192.168.2.179/31 | spine4 | Ethernet60 | 192.168.2.178/31 |
| leaf58 | Ethernet7 | 192.168.2.181/31 | spine5 | Ethernet60 | 192.168.2.180/31 |
| leaf58 | Ethernet8 | 192.168.2.183/31 | spine6 | Ethernet60 | 192.168.2.182/31 |
| leaf59 | Ethernet3 | 192.168.2.185/31 | spine1 | Ethernet61 | 192.168.2.184/31 |
| leaf59 | Ethernet4 | 192.168.2.187/31 | spine2 | Ethernet61 | 192.168.2.186/31 |
| leaf59 | Ethernet5 | 192.168.2.189/31 | spine3 | Ethernet61 | 192.168.2.188/31 |
| leaf59 | Ethernet6 | 192.168.2.191/31 | spine4 | Ethernet61 | 192.168.2.190/31 |
| leaf59 | Ethernet7 | 192.168.2.193/31 | spine5 | Ethernet61 | 192.168.2.192/31 |
| leaf59 | Ethernet8 | 192.168.2.195/31 | spine6 | Ethernet61 | 192.168.2.194/31 |
| leaf60 | Ethernet3 | 192.168.2.197/31 | spine1 | Ethernet62 | 192.168.2.196/31 |
| leaf60 | Ethernet4 | 192.168.2.199/31 | spine2 | Ethernet62 | 192.168.2.198/31 |
| leaf60 | Ethernet5 | 192.168.2.201/31 | spine3 | Ethernet62 | 192.168.2.200/31 |
| leaf60 | Ethernet6 | 192.168.2.203/31 | spine4 | Ethernet62 | 192.168.2.202/31 |
| leaf60 | Ethernet7 | 192.168.2.205/31 | spine5 | Ethernet62 | 192.168.2.204/31 |
| leaf60 | Ethernet8 | 192.168.2.207/31 | spine6 | Ethernet62 | 192.168.2.206/31 |
| leaf61 | Ethernet3 | 192.168.2.209/31 | spine1 | Ethernet63 | 192.168.2.208/31 |
| leaf61 | Ethernet4 | 192.168.2.211/31 | spine2 | Ethernet63 | 192.168.2.210/31 |
| leaf61 | Ethernet5 | 192.168.2.213/31 | spine3 | Ethernet63 | 192.168.2.212/31 |
| leaf61 | Ethernet6 | 192.168.2.215/31 | spine4 | Ethernet63 | 192.168.2.214/31 |
| leaf61 | Ethernet7 | 192.168.2.217/31 | spine5 | Ethernet63 | 192.168.2.216/31 |
| leaf61 | Ethernet8 | 192.168.2.219/31 | spine6 | Ethernet63 | 192.168.2.218/31 |
| leaf62 | Ethernet3 | 192.168.2.221/31 | spine1 | Ethernet64 | 192.168.2.220/31 |
| leaf62 | Ethernet4 | 192.168.2.223/31 | spine2 | Ethernet64 | 192.168.2.222/31 |
| leaf62 | Ethernet5 | 192.168.2.225/31 | spine3 | Ethernet64 | 192.168.2.224/31 |
| leaf62 | Ethernet6 | 192.168.2.227/31 | spine4 | Ethernet64 | 192.168.2.226/31 |
| leaf62 | Ethernet7 | 192.168.2.229/31 | spine5 | Ethernet64 | 192.168.2.228/31 |
| leaf62 | Ethernet8 | 192.168.2.231/31 | spine6 | Ethernet64 | 192.168.2.230/31 |
| leaf63 | Ethernet3 | 192.168.2.233/31 | spine1 | Ethernet65 | 192.168.2.232/31 |
| leaf63 | Ethernet4 | 192.168.2.235/31 | spine2 | Ethernet65 | 192.168.2.234/31 |
| leaf63 | Ethernet5 | 192.168.2.237/31 | spine3 | Ethernet65 | 192.168.2.236/31 |
| leaf63 | Ethernet6 | 192.168.2.239/31 | spine4 | Ethernet65 | 192.168.2.238/31 |
| leaf63 | Ethernet7 | 192.168.2.241/31 | spine5 | Ethernet65 | 192.168.2.240/31 |
| leaf63 | Ethernet8 | 192.168.2.243/31 | spine6 | Ethernet65 | 192.168.2.242/31 |
| leaf64 | Ethernet3 | 192.168.2.245/31 | spine1 | Ethernet66 | 192.168.2.244/31 |
| leaf64 | Ethernet4 | 192.168.2.247/31 | spine2 | Ethernet66 | 192.168.2.246/31 |
| leaf64 | Ethernet5 | 192.168.2.249/31 | spine3 | Ethernet66 | 192.168.2.248/31 |
| leaf64 | Ethernet6 | 192.168.2.251/31 | spine4 | Ethernet66 | 192.168.2.250/31 |
| leaf64 | Ethernet7 | 192.168.2.253/31 | spine5 | Ethernet66 | 192.168.2.252/31 |
| leaf64 | Ethernet8 | 192.168.2.255/31 | spine6 | Ethernet66 | 192.168.2.254/31 |
| leaf65 | Ethernet3 | 192.168.3.1/31 | spine1 | Ethernet67 | 192.168.3.0/31 |
| leaf65 | Ethernet4 | 192.168.3.3/31 | spine2 | Ethernet67 | 192.168.3.2/31 |
| leaf65 | Ethernet5 | 192.168.3.5/31 | spine3 | Ethernet67 | 192.168.3.4/31 |
| leaf65 | Ethernet6 | 192.168.3.7/31 | spine4 | Ethernet67 | 192.168.3.6/31 |
| leaf65 | Ethernet7 | 192.168.3.9/31 | spine5 | Ethernet67 | 192.168.3.8/31 |
| leaf65 | Ethernet8 | 192.168.3.11/31 | spine6 | Ethernet67 | 192.168.3.10/31 |
| leaf66 | Ethernet3 | 192.168.3.13/31 | spine1 | Ethernet68 | 192.168.3.12/31 |
| leaf66 | Ethernet4 | 192.168.3.15/31 | spine2 | Ethernet68 | 192.168.3.14/31 |
| leaf66 | Ethernet5 | 192.168.3.17/31 | spine3 | Ethernet68 | 192.168.3.16/31 |
| leaf66 | Ethernet6 | 192.168.3.19/31 | spine4 | Ethernet68 | 192.168.3.18/31 |
| leaf66 | Ethernet7 | 192.168.3.21/31 | spine5 | Ethernet68 | 192.168.3.20/31 |
| leaf66 | Ethernet8 | 192.168.3.23/31 | spine6 | Ethernet68 | 192.168.3.22/31 |
| leaf67 | Ethernet3 | 192.168.3.25/31 | spine1 | Ethernet69 | 192.168.3.24/31 |
| leaf67 | Ethernet4 | 192.168.3.27/31 | spine2 | Ethernet69 | 192.168.3.26/31 |
| leaf67 | Ethernet5 | 192.168.3.29/31 | spine3 | Ethernet69 | 192.168.3.28/31 |
| leaf67 | Ethernet6 | 192.168.3.31/31 | spine4 | Ethernet69 | 192.168.3.30/31 |
| leaf67 | Ethernet7 | 192.168.3.33/31 | spine5 | Ethernet69 | 192.168.3.32/31 |
| leaf67 | Ethernet8 | 192.168.3.35/31 | spine6 | Ethernet69 | 192.168.3.34/31 |
| leaf68 | Ethernet3 | 192.168.3.37/31 | spine1 | Ethernet70 | 192.168.3.36/31 |
| leaf68 | Ethernet4 | 192.168.3.39/31 | spine2 | Ethernet70 | 192.168.3.38/31 |
| leaf68 | Ethernet5 | 192.168.3.41/31 | spine3 | Ethernet70 | 192.168.3.40/31 |
| leaf68 | Ethernet6 | 192.168.3.43/31 | spine4 | Ethernet70 | 192.168.3.42/31 |
| leaf68 | Ethernet7 | 192.168.3.45/31 | spine5 | Ethernet70 | 192.168.3.44/31 |
| leaf68 | Ethernet8 | 192.168.3.47/31 | spine6 | Ethernet70 | 192.168.3.46/31 |
| leaf69 | Ethernet3 | 192.168.3.49/31 | spine1 | Ethernet71 | 192.168.3.48/31 |
| leaf69 | Ethernet4 | 192.168.3.51/31 | spine2 | Ethernet71 | 192.168.3.50/31 |
| leaf69 | Ethernet5 | 192.168.3.53/31 | spine3 | Ethernet71 | 192.168.3.52/31 |
| leaf69 | Ethernet6 | 192.168.3.55/31 | spine4 | Ethernet71 | 192.168.3.54/31 |
| leaf69 | Ethernet7 | 192.168.3.57/31 | spine5 | Ethernet71 | 192.168.3.56/31 |
| leaf69 | Ethernet8 | 192.168.3.59/31 | spine6 | Ethernet71 | 192.168.3.58/31 |
| leaf70 | Ethernet3 | 192.168.3.61/31 | spine1 | Ethernet72 | 192.168.3.60/31 |
| leaf70 | Ethernet4 | 192.168.3.63/31 | spine2 | Ethernet72 | 192.168.3.62/31 |
| leaf70 | Ethernet5 | 192.168.3.65/31 | spine3 | Ethernet72 | 192.168.3.64/31 |
| leaf70 | Ethernet6 | 192.168.3.67/31 | spine4 | Ethernet72 | 192.168.3.66/31 |
| leaf70 | Ethernet7 | 192.168.3.69/31 | spine5 | Ethernet72 | 192.168.3.68/31 |
| leaf70 | Ethernet8 | 192.168.3.71/31 | spine6 | Ethernet72 | 192.168.3.70/31 |
| leaf71 | Ethernet3 | 192.168.3.73/31 | spine1 | Ethernet73 | 192.168.3.72/31 |
| leaf71 | Ethernet4 | 192.168.3.75/31 | spine2 | Ethernet73 | 192.168.3.74/31 |
| leaf71 | Ethernet5 | 192.168.3.77/31 | spine3 | Ethernet73 | 192.168.3.76/31 |
| leaf71 | Ethernet6 | 192.168.3.79/31 | spine4 | Ethernet73 | 192.168.3.78/31 |
| leaf71 | Ethernet7 | 192.168.3.81/31 | spine5 | Ethernet73 | 192.168.3.80/31 |
| leaf71 | Ethernet8 | 192.168.3.83/31 | spine6 | Ethernet73 | 192.168.3.82/31 |
| leaf72 | Ethernet3 | 192.168.3.85/31 | spine1 | Ethernet74 | 192.168.3.84/31 |
| leaf72 | Ethernet4 | 192.168.3.87/31 | spine2 | Ethernet74 | 192.168.3.86/31 |
| leaf72 | Ethernet5 | 192.168.3.89/31 | spine3 | Ethernet74 | 192.168.3.88/31 |
| leaf72 | Ethernet6 | 192.168.3.91/31 | spine4 | Ethernet74 | 192.168.3.90/31 |
| leaf72 | Ethernet7 | 192.168.3.93/31 | spine5 | Ethernet74 | 192.168.3.92/31 |
| leaf72 | Ethernet8 | 192.168.3.95/31 | spine6 | Ethernet74 | 192.168.3.94/31 |
| leaf73 | Ethernet3 | 192.168.3.97/31 | spine1 | Ethernet75 | 192.168.3.96/31 |
| leaf73 | Ethernet4 | 192.168.3.99/31 | spine2 | Ethernet75 | 192.168.3.98/31 |
| leaf73 | Ethernet5 | 192.168.3.101/31 | spine3 | Ethernet75 | 192.168.3.100/31 |
| leaf73 | Ethernet6 | 192.168.3.103/31 | spine4 | Ethernet75 | 192.168.3.102/31 |
| leaf73 | Ethernet7 | 192.168.3.105/31 | spine5 | Ethernet75 | 192.168.3.104/31 |
| leaf73 | Ethernet8 | 192.168.3.107/31 | spine6 | Ethernet75 | 192.168.3.106/31 |
| leaf74 | Ethernet3 | 192.168.3.109/31 | spine1 | Ethernet76 | 192.168.3.108/31 |
| leaf74 | Ethernet4 | 192.168.3.111/31 | spine2 | Ethernet76 | 192.168.3.110/31 |
| leaf74 | Ethernet5 | 192.168.3.113/31 | spine3 | Ethernet76 | 192.168.3.112/31 |
| leaf74 | Ethernet6 | 192.168.3.115/31 | spine4 | Ethernet76 | 192.168.3.114/31 |
| leaf74 | Ethernet7 | 192.168.3.117/31 | spine5 | Ethernet76 | 192.168.3.116/31 |
| leaf74 | Ethernet8 | 192.168.3.119/31 | spine6 | Ethernet76 | 192.168.3.118/31 |
| leaf75 | Ethernet3 | 192.168.3.121/31 | spine1 | Ethernet77 | 192.168.3.120/31 |
| leaf75 | Ethernet4 | 192.168.3.123/31 | spine2 | Ethernet77 | 192.168.3.122/31 |
| leaf75 | Ethernet5 | 192.168.3.125/31 | spine3 | Ethernet77 | 192.168.3.124/31 |
| leaf75 | Ethernet6 | 192.168.3.127/31 | spine4 | Ethernet77 | 192.168.3.126/31 |
| leaf75 | Ethernet7 | 192.168.3.129/31 | spine5 | Ethernet77 | 192.168.3.128/31 |
| leaf75 | Ethernet8 | 192.168.3.131/31 | spine6 | Ethernet77 | 192.168.3.130/31 |
| leaf76 | Ethernet3 | 192.168.3.133/31 | spine1 | Ethernet78 | 192.168.3.132/31 |
| leaf76 | Ethernet4 | 192.168.3.135/31 | spine2 | Ethernet78 | 192.168.3.134/31 |
| leaf76 | Ethernet5 | 192.168.3.137/31 | spine3 | Ethernet78 | 192.168.3.136/31 |
| leaf76 | Ethernet6 | 192.168.3.139/31 | spine4 | Ethernet78 | 192.168.3.138/31 |
| leaf76 | Ethernet7 | 192.168.3.141/31 | spine5 | Ethernet78 | 192.168.3.140/31 |
| leaf76 | Ethernet8 | 192.168.3.143/31 | spine6 | Ethernet78 | 192.168.3.142/31 |
| leaf77 | Ethernet3 | 192.168.3.145/31 | spine1 | Ethernet79 | 192.168.3.144/31 |
| leaf77 | Ethernet4 | 192.168.3.147/31 | spine2 | Ethernet79 | 192.168.3.146/31 |
| leaf77 | Ethernet5 | 192.168.3.149/31 | spine3 | Ethernet79 | 192.168.3.148/31 |
| leaf77 | Ethernet6 | 192.168.3.151/31 | spine4 | Ethernet79 | 192.168.3.150/31 |
| leaf77 | Ethernet7 | 192.168.3.153/31 | spine5 | Ethernet79 | 192.168.3.152/31 |
| leaf77 | Ethernet8 | 192.168.3.155/31 | spine6 | Ethernet79 | 192.168.3.154/31 |
| leaf78 | Ethernet3 | 192.168.3.157/31 | spine1 | Ethernet80 | 192.168.3.156/31 |
| leaf78 | Ethernet4 | 192.168.3.159/31 | spine2 | Ethernet80 | 192.168.3.158/31 |
| leaf78 | Ethernet5 | 192.168.3.161/31 | spine3 | Ethernet80 | 192.168.3.160/31 |
| leaf78 | Ethernet6 | 192.168.3.163/31 | spine4 | Ethernet80 | 192.168.3.162/31 |
| leaf78 | Ethernet7 | 192.168.3.165/31 | spine5 | Ethernet80 | 192.168.3.164/31 |
| leaf78 | Ethernet8 | 192.168.3.167/31 | spine6 | Ethernet80 | 192.168.3.166/31 |
| leaf79 | Ethernet3 | 192.168.3.169/31 | spine1 | Ethernet81 | 192.168.3.168/31 |
| leaf79 | Ethernet4 | 192.168.3.171/31 | spine2 | Ethernet81 | 192.168.3.170/31 |
| leaf79 | Ethernet5 | 192.168.3.173/31 | spine3 | Ethernet81 | 192.168.3.172/31 |
| leaf79 | Ethernet6 | 192.168.3.175/31 | spine4 | Ethernet81 | 192.168.3.174/31 |
| leaf79 | Ethernet7 | 192.168.3.177/31 | spine5 | Ethernet81 | 192.168.3.176/31 |
| leaf79 | Ethernet8 | 192.168.3.179/31 | spine6 | Ethernet81 | 192.168.3.178/31 |
| leaf80 | Ethernet3 | 192.168.3.181/31 | spine1 | Ethernet82 | 192.168.3.180/31 |
| leaf80 | Ethernet4 | 192.168.3.183/31 | spine2 | Ethernet82 | 192.168.3.182/31 |
| leaf80 | Ethernet5 | 192.168.3.185/31 | spine3 | Ethernet82 | 192.168.3.184/31 |
| leaf80 | Ethernet6 | 192.168.3.187/31 | spine4 | Ethernet82 | 192.168.3.186/31 |
| leaf80 | Ethernet7 | 192.168.3.189/31 | spine5 | Ethernet82 | 192.168.3.188/31 |
| leaf80 | Ethernet8 | 192.168.3.191/31 | spine6 | Ethernet82 | 192.168.3.190/31 |
| leaf81 | Ethernet3 | 192.168.3.193/31 | spine1 | Ethernet83 | 192.168.3.192/31 |
| leaf81 | Ethernet4 | 192.168.3.195/31 | spine2 | Ethernet83 | 192.168.3.194/31 |
| leaf81 | Ethernet5 | 192.168.3.197/31 | spine3 | Ethernet83 | 192.168.3.196/31 |
| leaf81 | Ethernet6 | 192.168.3.199/31 | spine4 | Ethernet83 | 192.168.3.198/31 |
| leaf81 | Ethernet7 | 192.168.3.201/31 | spine5 | Ethernet83 | 192.168.3.200/31 |
| leaf81 | Ethernet8 | 192.168.3.203/31 | spine6 | Ethernet83 | 192.168.3.202/31 |
| leaf82 | Ethernet3 | 192.168.3.205/31 | spine1 | Ethernet84 | 192.168.3.204/31 |
| leaf82 | Ethernet4 | 192.168.3.207/31 | spine2 | Ethernet84 | 192.168.3.206/31 |
| leaf82 | Ethernet5 | 192.168.3.209/31 | spine3 | Ethernet84 | 192.168.3.208/31 |
| leaf82 | Ethernet6 | 192.168.3.211/31 | spine4 | Ethernet84 | 192.168.3.210/31 |
| leaf82 | Ethernet7 | 192.168.3.213/31 | spine5 | Ethernet84 | 192.168.3.212/31 |
| leaf82 | Ethernet8 | 192.168.3.215/31 | spine6 | Ethernet84 | 192.168.3.214/31 |
| leaf83 | Ethernet3 | 192.168.3.217/31 | spine1 | Ethernet85 | 192.168.3.216/31 |
| leaf83 | Ethernet4 | 192.168.3.219/31 | spine2 | Ethernet85 | 192.168.3.218/31 |
| leaf83 | Ethernet5 | 192.168.3.221/31 | spine3 | Ethernet85 | 192.168.3.220/31 |
| leaf83 | Ethernet6 | 192.168.3.223/31 | spine4 | Ethernet85 | 192.168.3.222/31 |
| leaf83 | Ethernet7 | 192.168.3.225/31 | spine5 | Ethernet85 | 192.168.3.224/31 |
| leaf83 | Ethernet8 | 192.168.3.227/31 | spine6 | Ethernet85 | 192.168.3.226/31 |
| leaf84 | Ethernet3 | 192.168.3.229/31 | spine1 | Ethernet86 | 192.168.3.228/31 |
| leaf84 | Ethernet4 | 192.168.3.231/31 | spine2 | Ethernet86 | 192.168.3.230/31 |
| leaf84 | Ethernet5 | 192.168.3.233/31 | spine3 | Ethernet86 | 192.168.3.232/31 |
| leaf84 | Ethernet6 | 192.168.3.235/31 | spine4 | Ethernet86 | 192.168.3.234/31 |
| leaf84 | Ethernet7 | 192.168.3.237/31 | spine5 | Ethernet86 | 192.168.3.236/31 |
| leaf84 | Ethernet8 | 192.168.3.239/31 | spine6 | Ethernet86 | 192.168.3.238/31 |
| leaf85 | Ethernet3 | 192.168.3.241/31 | spine1 | Ethernet87 | 192.168.3.240/31 |
| leaf85 | Ethernet4 | 192.168.3.243/31 | spine2 | Ethernet87 | 192.168.3.242/31 |
| leaf85 | Ethernet5 | 192.168.3.245/31 | spine3 | Ethernet87 | 192.168.3.244/31 |
| leaf85 | Ethernet6 | 192.168.3.247/31 | spine4 | Ethernet87 | 192.168.3.246/31 |
| leaf85 | Ethernet7 | 192.168.3.249/31 | spine5 | Ethernet87 | 192.168.3.248/31 |
| leaf85 | Ethernet8 | 192.168.3.251/31 | spine6 | Ethernet87 | 192.168.3.250/31 |
| leaf86 | Ethernet3 | 192.168.3.253/31 | spine1 | Ethernet88 | 192.168.3.252/31 |
| leaf86 | Ethernet4 | 192.168.3.255/31 | spine2 | Ethernet88 | 192.168.3.254/31 |
| leaf86 | Ethernet5 | 192.168.4.1/31 | spine3 | Ethernet88 | 192.168.4.0/31 |
| leaf86 | Ethernet6 | 192.168.4.3/31 | spine4 | Ethernet88 | 192.168.4.2/31 |
| leaf86 | Ethernet7 | 192.168.4.5/31 | spine5 | Ethernet88 | 192.168.4.4/31 |
| leaf86 | Ethernet8 | 192.168.4.7/31 | spine6 | Ethernet88 | 192.168.4.6/31 |
| leaf87 | Ethernet3 | 192.168.4.9/31 | spine1 | Ethernet89 | 192.168.4.8/31 |
| leaf87 | Ethernet4 | 192.168.4.11/31 | spine2 | Ethernet89 | 192.168.4.10/31 |
| leaf87 | Ethernet5 | 192.168.4.13/31 | spine3 | Ethernet89 | 192.168.4.12/31 |
| leaf87 | Ethernet6 | 192.168.4.15/31 | spine4 | Ethernet89 | 192.168.4.14/31 |
| leaf87 | Ethernet7 | 192.168.4.17/31 | spine5 | Ethernet89 | 192.168.4.16/31 |
| leaf87 | Ethernet8 | 192.168.4.19/31 | spine6 | Ethernet89 | 192.168.4.18/31 |
| leaf88 | Ethernet3 | 192.168.4.21/31 | spine1 | Ethernet90 | 192.168.4.20/31 |
| leaf88 | Ethernet4 | 192.168.4.23/31 | spine2 | Ethernet90 | 192.168.4.22/31 |
| leaf88 | Ethernet5 | 192.168.4.25/31 | spine3 | Ethernet90 | 192.168.4.24/31 |
| leaf88 | Ethernet6 | 192.168.4.27/31 | spine4 | Ethernet90 | 192.168.4.26/31 |
| leaf88 | Ethernet7 | 192.168.4.29/31 | spine5 | Ethernet90 | 192.168.4.28/31 |
| leaf88 | Ethernet8 | 192.168.4.31/31 | spine6 | Ethernet90 | 192.168.4.30/31 |
| leaf89 | Ethernet3 | 192.168.4.33/31 | spine1 | Ethernet91 | 192.168.4.32/31 |
| leaf89 | Ethernet4 | 192.168.4.35/31 | spine2 | Ethernet91 | 192.168.4.34/31 |
| leaf89 | Ethernet5 | 192.168.4.37/31 | spine3 | Ethernet91 | 192.168.4.36/31 |
| leaf89 | Ethernet6 | 192.168.4.39/31 | spine4 | Ethernet91 | 192.168.4.38/31 |
| leaf89 | Ethernet7 | 192.168.4.41/31 | spine5 | Ethernet91 | 192.168.4.40/31 |
| leaf89 | Ethernet8 | 192.168.4.43/31 | spine6 | Ethernet91 | 192.168.4.42/31 |
| leaf90 | Ethernet3 | 192.168.4.45/31 | spine1 | Ethernet92 | 192.168.4.44/31 |
| leaf90 | Ethernet4 | 192.168.4.47/31 | spine2 | Ethernet92 | 192.168.4.46/31 |
| leaf90 | Ethernet5 | 192.168.4.49/31 | spine3 | Ethernet92 | 192.168.4.48/31 |
| leaf90 | Ethernet6 | 192.168.4.51/31 | spine4 | Ethernet92 | 192.168.4.50/31 |
| leaf90 | Ethernet7 | 192.168.4.53/31 | spine5 | Ethernet92 | 192.168.4.52/31 |
| leaf90 | Ethernet8 | 192.168.4.55/31 | spine6 | Ethernet92 | 192.168.4.54/31 |
| leaf91 | Ethernet3 | 192.168.4.57/31 | spine1 | Ethernet93 | 192.168.4.56/31 |
| leaf91 | Ethernet4 | 192.168.4.59/31 | spine2 | Ethernet93 | 192.168.4.58/31 |
| leaf91 | Ethernet5 | 192.168.4.61/31 | spine3 | Ethernet93 | 192.168.4.60/31 |
| leaf91 | Ethernet6 | 192.168.4.63/31 | spine4 | Ethernet93 | 192.168.4.62/31 |
| leaf91 | Ethernet7 | 192.168.4.65/31 | spine5 | Ethernet93 | 192.168.4.64/31 |
| leaf91 | Ethernet8 | 192.168.4.67/31 | spine6 | Ethernet93 | 192.168.4.66/31 |
| leaf92 | Ethernet3 | 192.168.4.69/31 | spine1 | Ethernet94 | 192.168.4.68/31 |
| leaf92 | Ethernet4 | 192.168.4.71/31 | spine2 | Ethernet94 | 192.168.4.70/31 |
| leaf92 | Ethernet5 | 192.168.4.73/31 | spine3 | Ethernet94 | 192.168.4.72/31 |
| leaf92 | Ethernet6 | 192.168.4.75/31 | spine4 | Ethernet94 | 192.168.4.74/31 |
| leaf92 | Ethernet7 | 192.168.4.77/31 | spine5 | Ethernet94 | 192.168.4.76/31 |
| leaf92 | Ethernet8 | 192.168.4.79/31 | spine6 | Ethernet94 | 192.168.4.78/31 |
| leaf93 | Ethernet3 | 192.168.4.81/31 | spine1 | Ethernet95 | 192.168.4.80/31 |
| leaf93 | Ethernet4 | 192.168.4.83/31 | spine2 | Ethernet95 | 192.168.4.82/31 |
| leaf93 | Ethernet5 | 192.168.4.85/31 | spine3 | Ethernet95 | 192.168.4.84/31 |
| leaf93 | Ethernet6 | 192.168.4.87/31 | spine4 | Ethernet95 | 192.168.4.86/31 |
| leaf93 | Ethernet7 | 192.168.4.89/31 | spine5 | Ethernet95 | 192.168.4.88/31 |
| leaf93 | Ethernet8 | 192.168.4.91/31 | spine6 | Ethernet95 | 192.168.4.90/31 |
| leaf94 | Ethernet3 | 192.168.4.93/31 | spine1 | Ethernet96 | 192.168.4.92/31 |
| leaf94 | Ethernet4 | 192.168.4.95/31 | spine2 | Ethernet96 | 192.168.4.94/31 |
| leaf94 | Ethernet5 | 192.168.4.97/31 | spine3 | Ethernet96 | 192.168.4.96/31 |
| leaf94 | Ethernet6 | 192.168.4.99/31 | spine4 | Ethernet96 | 192.168.4.98/31 |
| leaf94 | Ethernet7 | 192.168.4.101/31 | spine5 | Ethernet96 | 192.168.4.100/31 |
| leaf94 | Ethernet8 | 192.168.4.103/31 | spine6 | Ethernet96 | 192.168.4.102/31 |
| leaf95 | Ethernet3 | 192.168.4.105/31 | spine1 | Ethernet97 | 192.168.4.104/31 |
| leaf95 | Ethernet4 | 192.168.4.107/31 | spine2 | Ethernet97 | 192.168.4.106/31 |
| leaf95 | Ethernet5 | 192.168.4.109/31 | spine3 | Ethernet97 | 192.168.4.108/31 |
| leaf95 | Ethernet6 | 192.168.4.111/31 | spine4 | Ethernet97 | 192.168.4.110/31 |
| leaf95 | Ethernet7 | 192.168.4.113/31 | spine5 | Ethernet97 | 192.168.4.112/31 |
| leaf95 | Ethernet8 | 192.168.4.115/31 | spine6 | Ethernet97 | 192.168.4.114/31 |
| leaf96 | Ethernet3 | 192.168.4.117/31 | spine1 | Ethernet98 | 192.168.4.116/31 |
| leaf96 | Ethernet4 | 192.168.4.119/31 | spine2 | Ethernet98 | 192.168.4.118/31 |
| leaf96 | Ethernet5 | 192.168.4.121/31 | spine3 | Ethernet98 | 192.168.4.120/31 |
| leaf96 | Ethernet6 | 192.168.4.123/31 | spine4 | Ethernet98 | 192.168.4.122/31 |
| leaf96 | Ethernet7 | 192.168.4.125/31 | spine5 | Ethernet98 | 192.168.4.124/31 |
| leaf96 | Ethernet8 | 192.168.4.127/31 | spine6 | Ethernet98 | 192.168.4.126/31 |
| leaf97 | Ethernet3 | 192.168.4.129/31 | spine1 | Ethernet99 | 192.168.4.128/31 |
| leaf97 | Ethernet4 | 192.168.4.131/31 | spine2 | Ethernet99 | 192.168.4.130/31 |
| leaf97 | Ethernet5 | 192.168.4.133/31 | spine3 | Ethernet99 | 192.168.4.132/31 |
| leaf97 | Ethernet6 | 192.168.4.135/31 | spine4 | Ethernet99 | 192.168.4.134/31 |
| leaf97 | Ethernet7 | 192.168.4.137/31 | spine5 | Ethernet99 | 192.168.4.136/31 |
| leaf97 | Ethernet8 | 192.168.4.139/31 | spine6 | Ethernet99 | 192.168.4.138/31 |
| leaf98 | Ethernet3 | 192.168.4.141/31 | spine1 | Ethernet100 | 192.168.4.140/31 |
| leaf98 | Ethernet4 | 192.168.4.143/31 | spine2 | Ethernet100 | 192.168.4.142/31 |
| leaf98 | Ethernet5 | 192.168.4.145/31 | spine3 | Ethernet100 | 192.168.4.144/31 |
| leaf98 | Ethernet6 | 192.168.4.147/31 | spine4 | Ethernet100 | 192.168.4.146/31 |
| leaf98 | Ethernet7 | 192.168.4.149/31 | spine5 | Ethernet100 | 192.168.4.148/31 |
| leaf98 | Ethernet8 | 192.168.4.151/31 | spine6 | Ethernet100 | 192.168.4.150/31 |
| leaf99 | Ethernet3 | 192.168.4.153/31 | spine1 | Ethernet101 | 192.168.4.152/31 |
| leaf99 | Ethernet4 | 192.168.4.155/31 | spine2 | Ethernet101 | 192.168.4.154/31 |
| leaf99 | Ethernet5 | 192.168.4.157/31 | spine3 | Ethernet101 | 192.168.4.156/31 |
| leaf99 | Ethernet6 | 192.168.4.159/31 | spine4 | Ethernet101 | 192.168.4.158/31 |
| leaf99 | Ethernet7 | 192.168.4.161/31 | spine5 | Ethernet101 | 192.168.4.160/31 |
| leaf99 | Ethernet8 | 192.168.4.163/31 | spine6 | Ethernet101 | 192.168.4.162/31 |
| spine5 | Ethernet3 | 192.168.0.8/31 | leaf1 | Ethernet7 | 192.168.0.9/31 |
| spine5 | Ethernet4 | 192.168.0.20/31 | leaf2 | Ethernet7 | 192.168.0.21/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.101.0/24 | 256 | 105 | 41.02 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | leaf1 | 192.168.101.1/32 |
| FABRIC | leaf2 | 192.168.101.2/32 |
| FABRIC | leaf3 | 192.168.101.3/32 |
| FABRIC | leaf4 | 192.168.101.4/32 |
| FABRIC | leaf5 | 192.168.101.5/32 |
| FABRIC | leaf6 | 192.168.101.6/32 |
| FABRIC | leaf7 | 192.168.101.7/32 |
| FABRIC | leaf8 | 192.168.101.8/32 |
| FABRIC | leaf9 | 192.168.101.9/32 |
| FABRIC | leaf10 | 192.168.101.10/32 |
| FABRIC | leaf11 | 192.168.101.11/32 |
| FABRIC | leaf12 | 192.168.101.12/32 |
| FABRIC | leaf13 | 192.168.101.13/32 |
| FABRIC | leaf14 | 192.168.101.14/32 |
| FABRIC | leaf15 | 192.168.101.15/32 |
| FABRIC | leaf16 | 192.168.101.16/32 |
| FABRIC | leaf17 | 192.168.101.17/32 |
| FABRIC | leaf18 | 192.168.101.18/32 |
| FABRIC | leaf19 | 192.168.101.19/32 |
| FABRIC | leaf20 | 192.168.101.20/32 |
| FABRIC | leaf21 | 192.168.101.21/32 |
| FABRIC | leaf22 | 192.168.101.22/32 |
| FABRIC | leaf23 | 192.168.101.23/32 |
| FABRIC | leaf24 | 192.168.101.24/32 |
| FABRIC | leaf25 | 192.168.101.25/32 |
| FABRIC | leaf26 | 192.168.101.26/32 |
| FABRIC | leaf27 | 192.168.101.27/32 |
| FABRIC | leaf28 | 192.168.101.28/32 |
| FABRIC | leaf29 | 192.168.101.29/32 |
| FABRIC | leaf30 | 192.168.101.30/32 |
| FABRIC | leaf31 | 192.168.101.31/32 |
| FABRIC | leaf32 | 192.168.101.32/32 |
| FABRIC | leaf33 | 192.168.101.33/32 |
| FABRIC | leaf34 | 192.168.101.34/32 |
| FABRIC | leaf35 | 192.168.101.35/32 |
| FABRIC | leaf36 | 192.168.101.36/32 |
| FABRIC | leaf37 | 192.168.101.37/32 |
| FABRIC | leaf38 | 192.168.101.38/32 |
| FABRIC | leaf39 | 192.168.101.39/32 |
| FABRIC | leaf40 | 192.168.101.40/32 |
| FABRIC | leaf41 | 192.168.101.41/32 |
| FABRIC | leaf42 | 192.168.101.42/32 |
| FABRIC | leaf43 | 192.168.101.43/32 |
| FABRIC | leaf44 | 192.168.101.44/32 |
| FABRIC | leaf45 | 192.168.101.45/32 |
| FABRIC | leaf46 | 192.168.101.46/32 |
| FABRIC | leaf47 | 192.168.101.47/32 |
| FABRIC | leaf48 | 192.168.101.48/32 |
| FABRIC | leaf49 | 192.168.101.49/32 |
| FABRIC | leaf50 | 192.168.101.50/32 |
| FABRIC | leaf51 | 192.168.101.51/32 |
| FABRIC | leaf52 | 192.168.101.52/32 |
| FABRIC | leaf53 | 192.168.101.53/32 |
| FABRIC | leaf54 | 192.168.101.54/32 |
| FABRIC | leaf55 | 192.168.101.55/32 |
| FABRIC | leaf56 | 192.168.101.56/32 |
| FABRIC | leaf57 | 192.168.101.57/32 |
| FABRIC | leaf58 | 192.168.101.58/32 |
| FABRIC | leaf59 | 192.168.101.59/32 |
| FABRIC | leaf60 | 192.168.101.60/32 |
| FABRIC | leaf61 | 192.168.101.61/32 |
| FABRIC | leaf62 | 192.168.101.62/32 |
| FABRIC | leaf63 | 192.168.101.63/32 |
| FABRIC | leaf64 | 192.168.101.64/32 |
| FABRIC | leaf65 | 192.168.101.65/32 |
| FABRIC | leaf66 | 192.168.101.66/32 |
| FABRIC | leaf67 | 192.168.101.67/32 |
| FABRIC | leaf68 | 192.168.101.68/32 |
| FABRIC | leaf69 | 192.168.101.69/32 |
| FABRIC | leaf70 | 192.168.101.70/32 |
| FABRIC | leaf71 | 192.168.101.71/32 |
| FABRIC | leaf72 | 192.168.101.72/32 |
| FABRIC | leaf73 | 192.168.101.73/32 |
| FABRIC | leaf74 | 192.168.101.74/32 |
| FABRIC | leaf75 | 192.168.101.75/32 |
| FABRIC | leaf76 | 192.168.101.76/32 |
| FABRIC | leaf77 | 192.168.101.77/32 |
| FABRIC | leaf78 | 192.168.101.78/32 |
| FABRIC | leaf79 | 192.168.101.79/32 |
| FABRIC | leaf80 | 192.168.101.80/32 |
| FABRIC | leaf81 | 192.168.101.81/32 |
| FABRIC | leaf82 | 192.168.101.82/32 |
| FABRIC | leaf83 | 192.168.101.83/32 |
| FABRIC | leaf84 | 192.168.101.84/32 |
| FABRIC | leaf85 | 192.168.101.85/32 |
| FABRIC | leaf86 | 192.168.101.86/32 |
| FABRIC | leaf87 | 192.168.101.87/32 |
| FABRIC | leaf88 | 192.168.101.88/32 |
| FABRIC | leaf89 | 192.168.101.89/32 |
| FABRIC | leaf90 | 192.168.101.90/32 |
| FABRIC | leaf91 | 192.168.101.91/32 |
| FABRIC | leaf92 | 192.168.101.92/32 |
| FABRIC | leaf93 | 192.168.101.93/32 |
| FABRIC | leaf94 | 192.168.101.94/32 |
| FABRIC | leaf95 | 192.168.101.95/32 |
| FABRIC | leaf96 | 192.168.101.96/32 |
| FABRIC | leaf97 | 192.168.101.97/32 |
| FABRIC | leaf98 | 192.168.101.98/32 |
| FABRIC | leaf99 | 192.168.101.99/32 |
| FABRIC | spine1 | 192.168.101.11/32 |
| FABRIC | spine2 | 192.168.101.12/32 |
| FABRIC | spine3 | 192.168.101.13/32 |
| FABRIC | spine4 | 192.168.101.11/32 |
| FABRIC | spine5 | 192.168.101.12/32 |
| FABRIC | spine6 | 192.168.101.13/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.102.0/24 | 256 | 99 | 38.68 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | leaf1 | 192.168.102.1/32 |
| FABRIC | leaf2 | 192.168.102.1/32 |
| FABRIC | leaf3 | 192.168.102.3/32 |
| FABRIC | leaf4 | 192.168.102.3/32 |
| FABRIC | leaf5 | 192.168.102.5/32 |
| FABRIC | leaf6 | 192.168.102.6/32 |
| FABRIC | leaf7 | 192.168.102.7/32 |
| FABRIC | leaf8 | 192.168.102.8/32 |
| FABRIC | leaf9 | 192.168.102.9/32 |
| FABRIC | leaf10 | 192.168.102.10/32 |
| FABRIC | leaf11 | 192.168.102.11/32 |
| FABRIC | leaf12 | 192.168.102.12/32 |
| FABRIC | leaf13 | 192.168.102.13/32 |
| FABRIC | leaf14 | 192.168.102.14/32 |
| FABRIC | leaf15 | 192.168.102.15/32 |
| FABRIC | leaf16 | 192.168.102.16/32 |
| FABRIC | leaf17 | 192.168.102.17/32 |
| FABRIC | leaf18 | 192.168.102.18/32 |
| FABRIC | leaf19 | 192.168.102.19/32 |
| FABRIC | leaf20 | 192.168.102.20/32 |
| FABRIC | leaf21 | 192.168.102.21/32 |
| FABRIC | leaf22 | 192.168.102.22/32 |
| FABRIC | leaf23 | 192.168.102.23/32 |
| FABRIC | leaf24 | 192.168.102.24/32 |
| FABRIC | leaf25 | 192.168.102.25/32 |
| FABRIC | leaf26 | 192.168.102.26/32 |
| FABRIC | leaf27 | 192.168.102.27/32 |
| FABRIC | leaf28 | 192.168.102.28/32 |
| FABRIC | leaf29 | 192.168.102.29/32 |
| FABRIC | leaf30 | 192.168.102.30/32 |
| FABRIC | leaf31 | 192.168.102.31/32 |
| FABRIC | leaf32 | 192.168.102.32/32 |
| FABRIC | leaf33 | 192.168.102.33/32 |
| FABRIC | leaf34 | 192.168.102.34/32 |
| FABRIC | leaf35 | 192.168.102.35/32 |
| FABRIC | leaf36 | 192.168.102.36/32 |
| FABRIC | leaf37 | 192.168.102.37/32 |
| FABRIC | leaf38 | 192.168.102.38/32 |
| FABRIC | leaf39 | 192.168.102.39/32 |
| FABRIC | leaf40 | 192.168.102.40/32 |
| FABRIC | leaf41 | 192.168.102.41/32 |
| FABRIC | leaf42 | 192.168.102.42/32 |
| FABRIC | leaf43 | 192.168.102.43/32 |
| FABRIC | leaf44 | 192.168.102.44/32 |
| FABRIC | leaf45 | 192.168.102.45/32 |
| FABRIC | leaf46 | 192.168.102.46/32 |
| FABRIC | leaf47 | 192.168.102.47/32 |
| FABRIC | leaf48 | 192.168.102.48/32 |
| FABRIC | leaf49 | 192.168.102.49/32 |
| FABRIC | leaf50 | 192.168.102.50/32 |
| FABRIC | leaf51 | 192.168.102.51/32 |
| FABRIC | leaf52 | 192.168.102.52/32 |
| FABRIC | leaf53 | 192.168.102.53/32 |
| FABRIC | leaf54 | 192.168.102.54/32 |
| FABRIC | leaf55 | 192.168.102.55/32 |
| FABRIC | leaf56 | 192.168.102.56/32 |
| FABRIC | leaf57 | 192.168.102.57/32 |
| FABRIC | leaf58 | 192.168.102.58/32 |
| FABRIC | leaf59 | 192.168.102.59/32 |
| FABRIC | leaf60 | 192.168.102.60/32 |
| FABRIC | leaf61 | 192.168.102.61/32 |
| FABRIC | leaf62 | 192.168.102.62/32 |
| FABRIC | leaf63 | 192.168.102.63/32 |
| FABRIC | leaf64 | 192.168.102.64/32 |
| FABRIC | leaf65 | 192.168.102.65/32 |
| FABRIC | leaf66 | 192.168.102.66/32 |
| FABRIC | leaf67 | 192.168.102.67/32 |
| FABRIC | leaf68 | 192.168.102.68/32 |
| FABRIC | leaf69 | 192.168.102.69/32 |
| FABRIC | leaf70 | 192.168.102.70/32 |
| FABRIC | leaf71 | 192.168.102.71/32 |
| FABRIC | leaf72 | 192.168.102.72/32 |
| FABRIC | leaf73 | 192.168.102.73/32 |
| FABRIC | leaf74 | 192.168.102.74/32 |
| FABRIC | leaf75 | 192.168.102.75/32 |
| FABRIC | leaf76 | 192.168.102.76/32 |
| FABRIC | leaf77 | 192.168.102.77/32 |
| FABRIC | leaf78 | 192.168.102.78/32 |
| FABRIC | leaf79 | 192.168.102.79/32 |
| FABRIC | leaf80 | 192.168.102.80/32 |
| FABRIC | leaf81 | 192.168.102.81/32 |
| FABRIC | leaf82 | 192.168.102.82/32 |
| FABRIC | leaf83 | 192.168.102.83/32 |
| FABRIC | leaf84 | 192.168.102.84/32 |
| FABRIC | leaf85 | 192.168.102.85/32 |
| FABRIC | leaf86 | 192.168.102.86/32 |
| FABRIC | leaf87 | 192.168.102.87/32 |
| FABRIC | leaf88 | 192.168.102.88/32 |
| FABRIC | leaf89 | 192.168.102.89/32 |
| FABRIC | leaf90 | 192.168.102.90/32 |
| FABRIC | leaf91 | 192.168.102.91/32 |
| FABRIC | leaf92 | 192.168.102.92/32 |
| FABRIC | leaf93 | 192.168.102.93/32 |
| FABRIC | leaf94 | 192.168.102.94/32 |
| FABRIC | leaf95 | 192.168.102.95/32 |
| FABRIC | leaf96 | 192.168.102.96/32 |
| FABRIC | leaf97 | 192.168.102.97/32 |
| FABRIC | leaf98 | 192.168.102.98/32 |
| FABRIC | leaf99 | 192.168.102.99/32 |
