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
| DC1_POD1 | l3leaf | leaf1 | 192.168.0.21/24 | - | Provisioned |
| DC1_POD1 | l3leaf | leaf2 | 192.168.0.22/24 | - | Provisioned |
| DC1_POD2 | l3leaf | leaf3 | 192.168.0.23/24 | - | Provisioned |
| DC1_POD2 | l3leaf | leaf4 | 192.168.0.24/24 | - | Provisioned |
| DC1_POD1 | spine | spine1 | 192.168.0.11/24 | - | Provisioned |
| DC1_POD1 | spine | spine2 | 192.168.0.12/24 | - | Provisioned |
| DC1_POD2 | spine | spine3 | 192.168.0.13/24 | - | Provisioned |
| DC1_POD2 | spine | spine4 | 192.168.0.14/24 | - | Provisioned |
| DC1 | super-spine | superspine1 | 192.168.0.25/24 | - | Provisioned |
| DC1 | super-spine | superspine2 | 192.168.0.26/24 | - | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | leaf1 | Ethernet1 | mlag_peer | leaf2 | Ethernet1 |
| l3leaf | leaf1 | Ethernet2 | mlag_peer | leaf2 | Ethernet2 |
| l3leaf | leaf1 | Ethernet3 | spine | spine1 | Ethernet3 |
| l3leaf | leaf1 | Ethernet4 | spine | spine2 | Ethernet3 |
| l3leaf | leaf2 | Ethernet3 | spine | spine1 | Ethernet4 |
| l3leaf | leaf2 | Ethernet4 | spine | spine2 | Ethernet4 |
| l3leaf | leaf3 | Ethernet1 | mlag_peer | leaf4 | Ethernet1 |
| l3leaf | leaf3 | Ethernet2 | mlag_peer | leaf4 | Ethernet2 |
| l3leaf | leaf3 | Ethernet5 | spine | spine3 | Ethernet5 |
| l3leaf | leaf3 | Ethernet6 | spine | spine4 | Ethernet5 |
| l3leaf | leaf4 | Ethernet5 | spine | spine3 | Ethernet6 |
| l3leaf | leaf4 | Ethernet6 | spine | spine4 | Ethernet6 |
| spine | spine1 | Ethernet7 | super-spine | superspine1 | Ethernet3 |
| spine | spine1 | Ethernet8 | super-spine | superspine2 | Ethernet3 |
| spine | spine2 | Ethernet7 | super-spine | superspine1 | Ethernet4 |
| spine | spine2 | Ethernet8 | super-spine | superspine2 | Ethernet4 |
| spine | spine3 | Ethernet7 | super-spine | superspine1 | Ethernet5 |
| spine | spine3 | Ethernet8 | super-spine | superspine2 | Ethernet5 |
| spine | spine4 | Ethernet7 | super-spine | superspine1 | Ethernet6 |
| spine | spine4 | Ethernet8 | super-spine | superspine2 | Ethernet6 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.103.0/24 | 256 | 0 | 0.0 % |
| 192.168.203.0/24 | 256 | 0 | 0.0 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.99.0/24 | 256 | 2 | 0.79 % |
| 192.168.101.0/24 | 256 | 4 | 1.57 % |
| 192.168.201.0/24 | 256 | 4 | 1.57 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_POD1 | leaf1 | 192.168.101.1/32 |
| DC1_POD1 | leaf2 | 192.168.101.2/32 |
| DC1_POD2 | leaf3 | 192.168.201.3/32 |
| DC1_POD2 | leaf4 | 192.168.201.4/32 |
| DC1_POD1 | spine1 | 192.168.101.11/32 |
| DC1_POD1 | spine2 | 192.168.101.12/32 |
| DC1_POD2 | spine3 | 192.168.201.13/32 |
| DC1_POD2 | spine4 | 192.168.201.14/32 |
| DC1 | superspine1 | 192.168.99.201/32 |
| DC1 | superspine2 | 192.168.99.202/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.102.0/24 | 256 | 2 | 0.79 % |
| 192.168.202.0/24 | 256 | 2 | 0.79 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_POD1 | leaf1 | 192.168.102.1/32 |
| DC1_POD1 | leaf2 | 192.168.102.1/32 |
| DC1_POD2 | leaf3 | 192.168.202.3/32 |
| DC1_POD2 | leaf4 | 192.168.202.3/32 |
