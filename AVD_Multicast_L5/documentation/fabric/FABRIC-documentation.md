# FABRIC

# Table of Contents

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

# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| FABRIC | l3leaf | leaf1-DC1 | 192.168.0.21/24 | - | Provisioned |
| FABRIC | l3leaf | leaf1-DC2 | 192.168.0.31/24 | - | Provisioned |
| FABRIC | l3leaf | leaf2-DC1 | 192.168.0.22/24 | - | Provisioned |
| FABRIC | l3leaf | leaf2-DC2 | 192.168.0.32/24 | - | Provisioned |
| FABRIC | l3leaf | leaf3-DC1 | 192.168.0.23/24 | - | Provisioned |
| FABRIC | l3leaf | leaf3-DC2 | 192.168.0.33/24 | - | Provisioned |
| FABRIC | l3leaf | leaf4-DC1 | 192.168.0.24/24 | - | Provisioned |
| FABRIC | l3leaf | leaf4-DC2 | 192.168.0.44/24 | - | Provisioned |
| FABRIC | spine | spine1-DC1 | 192.168.0.11/24 | - | Provisioned |
| FABRIC | spine | spine1-DC2 | 192.168.0.14/24 | - | Provisioned |
| FABRIC | spine | spine2-DC1 | 192.168.0.12/24 | - | Provisioned |
| FABRIC | spine | spine2-DC2 | 192.168.0.15/24 | - | Provisioned |
| FABRIC | spine | spine3-DC1 | 192.168.0.13/24 | - | Provisioned |
| FABRIC | spine | spine3-DC2 | 192.168.0.16/24 | - | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | leaf1-DC1 | Ethernet1 | mlag_peer | leaf2-DC1 | Ethernet1 |
| l3leaf | leaf1-DC1 | Ethernet2 | mlag_peer | leaf2-DC1 | Ethernet2 |
| l3leaf | leaf1-DC1 | Ethernet3 | spine | spine1-DC1 | Ethernet2 |
| l3leaf | leaf1-DC1 | Ethernet4 | spine | spine2-DC1 | Ethernet2 |
| l3leaf | leaf1-DC1 | Ethernet5 | spine | spine3-DC1 | Ethernet2 |
| l3leaf | leaf1-DC2 | Ethernet1 | mlag_peer | leaf2-DC2 | Ethernet1 |
| l3leaf | leaf1-DC2 | Ethernet2 | mlag_peer | leaf2-DC2 | Ethernet2 |
| l3leaf | leaf1-DC2 | Ethernet3 | spine | spine1-DC2 | Ethernet2 |
| l3leaf | leaf1-DC2 | Ethernet4 | spine | spine2-DC2 | Ethernet2 |
| l3leaf | leaf1-DC2 | Ethernet5 | spine | spine3-DC2 | Ethernet1 |
| l3leaf | leaf2-DC1 | Ethernet3 | spine | spine1-DC1 | Ethernet3 |
| l3leaf | leaf2-DC1 | Ethernet4 | spine | spine2-DC1 | Ethernet3 |
| l3leaf | leaf2-DC1 | Ethernet5 | spine | spine3-DC1 | Ethernet3 |
| l3leaf | leaf2-DC2 | Ethernet3 | spine | spine1-DC2 | Ethernet3 |
| l3leaf | leaf2-DC2 | Ethernet4 | spine | spine2-DC2 | Ethernet3 |
| l3leaf | leaf2-DC2 | Ethernet5 | spine | spine3-DC2 | Ethernet2 |
| l3leaf | leaf3-DC1 | Ethernet1 | mlag_peer | leaf4-DC1 | Ethernet1 |
| l3leaf | leaf3-DC1 | Ethernet2 | mlag_peer | leaf4-DC1 | Ethernet2 |
| l3leaf | leaf3-DC1 | Ethernet3 | spine | spine1-DC1 | Ethernet4 |
| l3leaf | leaf3-DC1 | Ethernet4 | spine | spine2-DC1 | Ethernet4 |
| l3leaf | leaf3-DC1 | Ethernet5 | spine | spine3-DC1 | Ethernet4 |
| l3leaf | leaf3-DC2 | Ethernet1 | mlag_peer | leaf4-DC2 | Ethernet1 |
| l3leaf | leaf3-DC2 | Ethernet2 | mlag_peer | leaf4-DC2 | Ethernet2 |
| l3leaf | leaf3-DC2 | Ethernet3 | spine | spine1-DC2 | Ethernet4 |
| l3leaf | leaf3-DC2 | Ethernet4 | spine | spine2-DC2 | Ethernet4 |
| l3leaf | leaf3-DC2 | Ethernet5 | spine | spine3-DC2 | Ethernet3 |
| l3leaf | leaf4-DC1 | Ethernet3 | spine | spine1-DC1 | Ethernet5 |
| l3leaf | leaf4-DC1 | Ethernet4 | spine | spine2-DC1 | Ethernet5 |
| l3leaf | leaf4-DC1 | Ethernet5 | spine | spine3-DC1 | Ethernet5 |
| l3leaf | leaf4-DC2 | Ethernet3 | spine | spine1-DC2 | Ethernet5 |
| l3leaf | leaf4-DC2 | Ethernet4 | spine | spine2-DC2 | Ethernet5 |
| l3leaf | leaf4-DC2 | Ethernet5 | spine | spine3-DC2 | Ethernet4 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.103.0/24 | 256 | 24 | 9.38 % |
| 192.168.203.0/24 | 256 | 24 | 9.38 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| leaf1-DC1 | Ethernet3 | 192.168.103.121/31 | spine1-DC1 | Ethernet2 | 192.168.103.120/31 |
| leaf1-DC1 | Ethernet4 | 192.168.103.123/31 | spine2-DC1 | Ethernet2 | 192.168.103.122/31 |
| leaf1-DC1 | Ethernet5 | 192.168.103.125/31 | spine3-DC1 | Ethernet2 | 192.168.103.124/31 |
| leaf1-DC2 | Ethernet3 | 192.168.203.121/31 | spine1-DC2 | Ethernet2 | 192.168.203.120/31 |
| leaf1-DC2 | Ethernet4 | 192.168.203.123/31 | spine2-DC2 | Ethernet2 | 192.168.203.122/31 |
| leaf1-DC2 | Ethernet5 | 192.168.203.125/31 | spine3-DC2 | Ethernet1 | 192.168.203.124/31 |
| leaf2-DC1 | Ethernet3 | 192.168.103.127/31 | spine1-DC1 | Ethernet3 | 192.168.103.126/31 |
| leaf2-DC1 | Ethernet4 | 192.168.103.129/31 | spine2-DC1 | Ethernet3 | 192.168.103.128/31 |
| leaf2-DC1 | Ethernet5 | 192.168.103.131/31 | spine3-DC1 | Ethernet3 | 192.168.103.130/31 |
| leaf2-DC2 | Ethernet3 | 192.168.203.127/31 | spine1-DC2 | Ethernet3 | 192.168.203.126/31 |
| leaf2-DC2 | Ethernet4 | 192.168.203.129/31 | spine2-DC2 | Ethernet3 | 192.168.203.128/31 |
| leaf2-DC2 | Ethernet5 | 192.168.203.131/31 | spine3-DC2 | Ethernet2 | 192.168.203.130/31 |
| leaf3-DC1 | Ethernet3 | 192.168.103.133/31 | spine1-DC1 | Ethernet4 | 192.168.103.132/31 |
| leaf3-DC1 | Ethernet4 | 192.168.103.135/31 | spine2-DC1 | Ethernet4 | 192.168.103.134/31 |
| leaf3-DC1 | Ethernet5 | 192.168.103.137/31 | spine3-DC1 | Ethernet4 | 192.168.103.136/31 |
| leaf3-DC2 | Ethernet3 | 192.168.203.133/31 | spine1-DC2 | Ethernet4 | 192.168.203.132/31 |
| leaf3-DC2 | Ethernet4 | 192.168.203.135/31 | spine2-DC2 | Ethernet4 | 192.168.203.134/31 |
| leaf3-DC2 | Ethernet5 | 192.168.203.137/31 | spine3-DC2 | Ethernet3 | 192.168.203.136/31 |
| leaf4-DC1 | Ethernet3 | 192.168.103.139/31 | spine1-DC1 | Ethernet5 | 192.168.103.138/31 |
| leaf4-DC1 | Ethernet4 | 192.168.103.141/31 | spine2-DC1 | Ethernet5 | 192.168.103.140/31 |
| leaf4-DC1 | Ethernet5 | 192.168.103.143/31 | spine3-DC1 | Ethernet5 | 192.168.103.142/31 |
| leaf4-DC2 | Ethernet3 | 192.168.203.139/31 | spine1-DC2 | Ethernet5 | 192.168.203.138/31 |
| leaf4-DC2 | Ethernet4 | 192.168.203.141/31 | spine2-DC2 | Ethernet5 | 192.168.203.140/31 |
| leaf4-DC2 | Ethernet5 | 192.168.203.143/31 | spine3-DC2 | Ethernet4 | 192.168.203.142/31 |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.101.0/24 | 256 | 4 | 1.57 % |
| 192.168.201.0/24 | 256 | 10 | 3.91 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| FABRIC | leaf1-DC1 | 192.168.101.21/32 |
| FABRIC | leaf1-DC2 | 192.168.201.21/32 |
| FABRIC | leaf2-DC1 | 192.168.101.22/32 |
| FABRIC | leaf2-DC2 | 192.168.201.22/32 |
| FABRIC | leaf3-DC1 | 192.168.101.23/32 |
| FABRIC | leaf3-DC2 | 192.168.201.23/32 |
| FABRIC | leaf4-DC1 | 192.168.101.24/32 |
| FABRIC | leaf4-DC2 | 192.168.201.24/32 |
| FABRIC | spine1-DC1 | 192.168.201.14/32 |
| FABRIC | spine1-DC2 | 192.168.201.14/32 |
| FABRIC | spine2-DC1 | 192.168.201.15/32 |
| FABRIC | spine2-DC2 | 192.168.201.15/32 |
| FABRIC | spine3-DC1 | 192.168.201.16/32 |
| FABRIC | spine3-DC2 | 192.168.201.16/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.102.0/24 | 256 | 4 | 1.57 % |
| 192.168.202.0/24 | 256 | 4 | 1.57 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| FABRIC | leaf1-DC1 | 192.168.102.21/32 |
| FABRIC | leaf1-DC2 | 192.168.202.21/32 |
| FABRIC | leaf2-DC1 | 192.168.102.21/32 |
| FABRIC | leaf2-DC2 | 192.168.202.21/32 |
| FABRIC | leaf3-DC1 | 192.168.102.23/32 |
| FABRIC | leaf3-DC2 | 192.168.202.23/32 |
| FABRIC | leaf4-DC1 | 192.168.102.23/32 |
| FABRIC | leaf4-DC2 | 192.168.202.23/32 |
