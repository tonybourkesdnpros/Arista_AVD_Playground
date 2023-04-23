
# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 933 | 727 | 206 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| borderleaf1-DC1 |  68 | 51 | 17 | IP Reachability, Loopback0 Reachability |
| borderleaf1-DC2 |  67 | 50 | 17 | IP Reachability, Loopback0 Reachability |
| borderleaf2-DC1 |  65 | 48 | 17 | IP Reachability, Loopback0 Reachability |
| borderleaf2-DC2 |  68 | 51 | 17 | IP Reachability, Loopback0 Reachability |
| DCI |  14 | 6 | 8 | LLDP Topology, IP Reachability |
| leaf1-DC1 |  66 | 50 | 16 | Loopback0 Reachability |
| leaf1-DC2 |  66 | 50 | 16 | Loopback0 Reachability |
| leaf2-DC1 |  66 | 50 | 16 | Loopback0 Reachability |
| leaf2-DC2 |  66 | 50 | 16 | Loopback0 Reachability |
| leaf3-DC1 |  66 | 50 | 16 | Loopback0 Reachability |
| leaf3-DC2 |  66 | 49 | 17 | Interface State, Loopback0 Reachability |
| leaf4-DC1 |  66 | 50 | 16 | Loopback0 Reachability |
| leaf4-DC2 |  66 | 49 | 17 | Interface State, Loopback0 Reachability |
| spine1-DC1 |  20 | 20 | 0 | - |
| spine1-DC2 |  21 | 21 | 0 | - |
| spine2-DC1 |  20 | 20 | 0 | - |
| spine2-DC2 |  21 | 21 | 0 | - |
| spine3-DC1 |  20 | 20 | 0 | - |
| spine3-DC2 |  21 | 21 | 0 | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  19 | 19 | 0 |
| Interface State |  242 | 240 | 2 |
| LLDP Topology |  104 | 100 | 4 |
| MLAG |  12 | 12 | 0 |
| IP Reachability |  8 | 0 | 8 |
| BGP |  92 | 92 | 0 |
| Routing Table |  264 | 264 | 0 |
| Loopback0 Reachability |  192 | 0 | 192 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 155 | leaf3-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel6 - host2-DC2_PortChannel host2 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 159 | leaf4-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel6 - host2-DC2_PortChannel host2 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 286 | DCI | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: borderleaf1-DC1_Ethernet12 | FAIL | core1-ISP1.arista.lab - Ethernet2 |
| 287 | DCI | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: borderleaf2-DC1_Ethernet12 | FAIL | core2-ISP1.arista.lab - Ethernet2 |
| 288 | DCI | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: borderleaf1-DC2_Ethernet12 | FAIL | core1-ISP2.arista.lab - Ethernet2 |
| 289 | DCI | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: borderleaf2-DC2_Ethernet12 | FAIL | core2-ISP2.arista.lab - Ethernet2 |
| 378 | borderleaf1-DC1 | IP Reachability | ip reachability test p2p links | Source: borderleaf1-DC1_Ethernet12 - Destination: DCI_Ethernet1 | FAIL | 100% packet loss |
| 379 | borderleaf1-DC2 | IP Reachability | ip reachability test p2p links | Source: borderleaf1-DC2_Ethernet12 - Destination: DCI_Ethernet3 | FAIL | 100% packet loss |
| 380 | borderleaf2-DC1 | IP Reachability | ip reachability test p2p links | Source: borderleaf2-DC1_Ethernet12 - Destination: DCI_Ethernet2 | FAIL | 100% packet loss |
| 381 | borderleaf2-DC2 | IP Reachability | ip reachability test p2p links | Source: borderleaf2-DC2_Ethernet12 - Destination: DCI_Ethernet4 | FAIL | 100% packet loss |
| 382 | DCI | IP Reachability | ip reachability test p2p links | Source: DCI_Ethernet1 - Destination: borderleaf1-DC1_Ethernet12 | FAIL | 100% packet loss |
| 383 | DCI | IP Reachability | ip reachability test p2p links | Source: DCI_Ethernet2 - Destination: borderleaf2-DC1_Ethernet12 | FAIL | 100% packet loss |
| 384 | DCI | IP Reachability | ip reachability test p2p links | Source: DCI_Ethernet3 - Destination: borderleaf1-DC2_Ethernet12 | FAIL | 100% packet loss |
| 385 | DCI | IP Reachability | ip reachability test p2p links | Source: DCI_Ethernet4 - Destination: borderleaf2-DC2_Ethernet12 | FAIL | 100% packet loss |
| 742 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 743 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 744 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 745 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 746 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 747 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 748 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 749 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 750 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 751 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 752 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 753 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 754 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 755 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 756 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 757 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 758 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 759 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 760 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 761 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 762 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 763 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 764 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 765 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 766 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 767 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 768 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 769 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 770 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 771 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 772 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 773 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 774 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 775 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 776 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 777 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 778 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 779 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 780 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 781 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 782 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 783 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 784 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 785 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 786 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 787 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 788 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 789 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 790 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 791 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 792 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 793 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 794 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 795 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 796 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 797 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 798 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 799 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 800 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 801 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 802 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 803 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 804 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 805 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 806 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 807 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 808 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 809 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 810 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 811 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 812 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 813 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 814 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 815 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 816 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 817 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 818 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 819 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 820 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 821 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 822 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 823 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 824 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 825 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 826 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 827 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 828 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 829 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 830 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 831 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 832 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 833 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 834 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 835 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 836 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 837 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 838 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 839 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 840 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 841 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 842 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 843 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 844 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 845 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 846 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 847 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 848 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 849 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 850 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 851 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 852 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 853 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 854 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 855 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 856 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 857 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 858 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 859 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 860 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 861 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 862 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 863 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 864 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 865 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 866 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 867 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 868 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 869 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 870 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 871 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 872 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 873 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 874 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 875 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 876 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 877 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 878 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 879 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 880 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 881 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 882 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 883 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 884 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 885 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 886 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 887 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 888 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 889 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 890 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 891 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 892 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 893 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 894 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 895 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 896 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 897 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 898 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 899 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 900 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 901 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 902 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 903 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 904 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 905 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 906 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 907 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 908 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 909 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 910 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 911 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 912 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 913 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 914 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 915 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 916 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 917 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 918 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 919 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 920 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 921 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 922 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 923 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 924 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 925 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 926 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 927 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 928 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 929 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 930 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 931 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 932 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 933 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.13 | FAIL | 100% packet loss |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | borderleaf1-DC1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 2 | borderleaf1-DC2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 3 | borderleaf2-DC1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 4 | borderleaf2-DC2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 5 | DCI | NTP | Synchronised with NTP server | NTP | PASS | - |
| 6 | leaf1-DC1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 7 | leaf1-DC2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 8 | leaf2-DC1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 9 | leaf2-DC2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 10 | leaf3-DC1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 11 | leaf3-DC2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 12 | leaf4-DC1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 13 | leaf4-DC2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 14 | spine1-DC1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 15 | spine1-DC2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 16 | spine2-DC1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 17 | spine2-DC2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 18 | spine3-DC1 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 19 | spine3-DC2 | NTP | Synchronised with NTP server | NTP | PASS | - |
| 20 | borderleaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_borderleaf2-DC1_Ethernet1 | PASS | - |
| 21 | borderleaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_borderleaf2-DC1_Ethernet2 | PASS | - |
| 22 | borderleaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC1_Ethernet6 | PASS | - |
| 23 | borderleaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC1_Ethernet6 | PASS | - |
| 24 | borderleaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC1_Ethernet6 | PASS | - |
| 25 | borderleaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet12 - P2P_LINK_TO_DCI_Ethernet1 | PASS | - |
| 26 | borderleaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_borderleaf2-DC2_Ethernet1 | PASS | - |
| 27 | borderleaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_borderleaf2-DC2_Ethernet2 | PASS | - |
| 28 | borderleaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC2_Ethernet6 | PASS | - |
| 29 | borderleaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC2_Ethernet6 | PASS | - |
| 30 | borderleaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC2_Ethernet6 | PASS | - |
| 31 | borderleaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet12 - P2P_LINK_TO_DCI_Ethernet3 | PASS | - |
| 32 | borderleaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_borderleaf1-DC1_Ethernet1 | PASS | - |
| 33 | borderleaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_borderleaf1-DC1_Ethernet2 | PASS | - |
| 34 | borderleaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC1_Ethernet7 | PASS | - |
| 35 | borderleaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC1_Ethernet7 | PASS | - |
| 36 | borderleaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC1_Ethernet7 | PASS | - |
| 37 | borderleaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet12 - P2P_LINK_TO_DCI_Ethernet2 | PASS | - |
| 38 | borderleaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_borderleaf1-DC2_Ethernet1 | PASS | - |
| 39 | borderleaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_borderleaf1-DC2_Ethernet2 | PASS | - |
| 40 | borderleaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC2_Ethernet7 | PASS | - |
| 41 | borderleaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC2_Ethernet7 | PASS | - |
| 42 | borderleaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC2_Ethernet7 | PASS | - |
| 43 | borderleaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet12 - P2P_LINK_TO_DCI_Ethernet4 | PASS | - |
| 44 | DCI | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_borderleaf1-DC1_Ethernet12 | PASS | - |
| 45 | DCI | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_borderleaf2-DC1_Ethernet12 | PASS | - |
| 46 | DCI | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_borderleaf1-DC2_Ethernet12 | PASS | - |
| 47 | DCI | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_borderleaf2-DC2_Ethernet12 | PASS | - |
| 48 | leaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf2-DC1_Ethernet1 | PASS | - |
| 49 | leaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf2-DC1_Ethernet2 | PASS | - |
| 50 | leaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC1_Ethernet2 | PASS | - |
| 51 | leaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC1_Ethernet2 | PASS | - |
| 52 | leaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC1_Ethernet2 | PASS | - |
| 53 | leaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - host1-DC1_Ethernet1 | PASS | - |
| 54 | leaf1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1-DC1_Ethernet2 | PASS | - |
| 55 | leaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf2-DC2_Ethernet1 | PASS | - |
| 56 | leaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf2-DC2_Ethernet2 | PASS | - |
| 57 | leaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC2_Ethernet2 | PASS | - |
| 58 | leaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC2_Ethernet2 | PASS | - |
| 59 | leaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC2_Ethernet2 | PASS | - |
| 60 | leaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - host1-DC2_Ethernet1 | PASS | - |
| 61 | leaf1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1-DC2_Ethernet2 | PASS | - |
| 62 | leaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf1-DC1_Ethernet1 | PASS | - |
| 63 | leaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf1-DC1_Ethernet2 | PASS | - |
| 64 | leaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC1_Ethernet3 | PASS | - |
| 65 | leaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC1_Ethernet3 | PASS | - |
| 66 | leaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC1_Ethernet3 | PASS | - |
| 67 | leaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - host1-DC1_Ethernet3 | PASS | - |
| 68 | leaf2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1-DC1_Ethernet4 | PASS | - |
| 69 | leaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf1-DC2_Ethernet1 | PASS | - |
| 70 | leaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf1-DC2_Ethernet2 | PASS | - |
| 71 | leaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC2_Ethernet3 | PASS | - |
| 72 | leaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC2_Ethernet3 | PASS | - |
| 73 | leaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC2_Ethernet3 | PASS | - |
| 74 | leaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - host1-DC2_Ethernet3 | PASS | - |
| 75 | leaf2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host1-DC2_Ethernet4 | PASS | - |
| 76 | leaf3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf4-DC1_Ethernet1 | PASS | - |
| 77 | leaf3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf4-DC1_Ethernet2 | PASS | - |
| 78 | leaf3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC1_Ethernet4 | PASS | - |
| 79 | leaf3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC1_Ethernet4 | PASS | - |
| 80 | leaf3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC1_Ethernet4 | PASS | - |
| 81 | leaf3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - host2-DC1_Ethernet1 | PASS | - |
| 82 | leaf3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host2-DC1_Ethernet2 | PASS | - |
| 83 | leaf3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf4-DC2_Ethernet1 | PASS | - |
| 84 | leaf3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf4-DC2_Ethernet2 | PASS | - |
| 85 | leaf3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC2_Ethernet4 | PASS | - |
| 86 | leaf3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC2_Ethernet4 | PASS | - |
| 87 | leaf3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC2_Ethernet4 | PASS | - |
| 88 | leaf3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - host2-DC2_Ethernet1 | PASS | - |
| 89 | leaf3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host2-DC2_Ethernet2 | PASS | - |
| 90 | leaf4-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf3-DC1_Ethernet1 | PASS | - |
| 91 | leaf4-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf3-DC1_Ethernet2 | PASS | - |
| 92 | leaf4-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC1_Ethernet5 | PASS | - |
| 93 | leaf4-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC1_Ethernet5 | PASS | - |
| 94 | leaf4-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC1_Ethernet5 | PASS | - |
| 95 | leaf4-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - host2-DC1_Ethernet3 | PASS | - |
| 96 | leaf4-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host2-DC1_Ethernet4 | PASS | - |
| 97 | leaf4-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet1 - MLAG_PEER_leaf3-DC2_Ethernet1 | PASS | - |
| 98 | leaf4-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - MLAG_PEER_leaf3-DC2_Ethernet2 | PASS | - |
| 99 | leaf4-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_SPINE1-DC2_Ethernet5 | PASS | - |
| 100 | leaf4-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_SPINE2-DC2_Ethernet5 | PASS | - |
| 101 | leaf4-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_SPINE3-DC2_Ethernet5 | PASS | - |
| 102 | leaf4-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - host2-DC2_Ethernet3 | PASS | - |
| 103 | leaf4-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - host2-DC2_Ethernet4 | PASS | - |
| 104 | spine1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF1-DC1_Ethernet3 | PASS | - |
| 105 | spine1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF2-DC1_Ethernet3 | PASS | - |
| 106 | spine1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF3-DC1_Ethernet3 | PASS | - |
| 107 | spine1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF4-DC1_Ethernet3 | PASS | - |
| 108 | spine1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_BORDERLEAF1-DC1_Ethernet3 | PASS | - |
| 109 | spine1-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_BORDERLEAF2-DC1_Ethernet3 | PASS | - |
| 110 | spine1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF1-DC2_Ethernet3 | PASS | - |
| 111 | spine1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF2-DC2_Ethernet3 | PASS | - |
| 112 | spine1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF3-DC2_Ethernet3 | PASS | - |
| 113 | spine1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF4-DC2_Ethernet3 | PASS | - |
| 114 | spine1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_BORDERLEAF1-DC2_Ethernet3 | PASS | - |
| 115 | spine1-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_BORDERLEAF2-DC2_Ethernet3 | PASS | - |
| 116 | spine2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF1-DC1_Ethernet4 | PASS | - |
| 117 | spine2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF2-DC1_Ethernet4 | PASS | - |
| 118 | spine2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF3-DC1_Ethernet4 | PASS | - |
| 119 | spine2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF4-DC1_Ethernet4 | PASS | - |
| 120 | spine2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_BORDERLEAF1-DC1_Ethernet4 | PASS | - |
| 121 | spine2-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_BORDERLEAF2-DC1_Ethernet4 | PASS | - |
| 122 | spine2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF1-DC2_Ethernet4 | PASS | - |
| 123 | spine2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF2-DC2_Ethernet4 | PASS | - |
| 124 | spine2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF3-DC2_Ethernet4 | PASS | - |
| 125 | spine2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF4-DC2_Ethernet4 | PASS | - |
| 126 | spine2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_BORDERLEAF1-DC2_Ethernet4 | PASS | - |
| 127 | spine2-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_BORDERLEAF2-DC2_Ethernet4 | PASS | - |
| 128 | spine3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF1-DC1_Ethernet5 | PASS | - |
| 129 | spine3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF2-DC1_Ethernet5 | PASS | - |
| 130 | spine3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF3-DC1_Ethernet5 | PASS | - |
| 131 | spine3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF4-DC1_Ethernet5 | PASS | - |
| 132 | spine3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_BORDERLEAF1-DC1_Ethernet5 | PASS | - |
| 133 | spine3-DC1 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_BORDERLEAF2-DC1_Ethernet5 | PASS | - |
| 134 | spine3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF1-DC2_Ethernet5 | PASS | - |
| 135 | spine3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF2-DC2_Ethernet5 | PASS | - |
| 136 | spine3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF3-DC2_Ethernet5 | PASS | - |
| 137 | spine3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet5 - P2P_LINK_TO_LEAF4-DC2_Ethernet5 | PASS | - |
| 138 | spine3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet6 - P2P_LINK_TO_BORDERLEAF1-DC2_Ethernet5 | PASS | - |
| 139 | spine3-DC2 | Interface State | Ethernet Interface & Line Protocol == "up" | Ethernet7 - P2P_LINK_TO_BORDERLEAF2-DC2_Ethernet5 | PASS | - |
| 140 | borderleaf1-DC1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_borderleaf2-DC1_Po1 | PASS | - |
| 141 | borderleaf1-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_borderleaf2-DC2_Po1 | PASS | - |
| 142 | borderleaf2-DC1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_borderleaf1-DC1_Po1 | PASS | - |
| 143 | borderleaf2-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_borderleaf1-DC2_Po1 | PASS | - |
| 144 | leaf1-DC1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf2-DC1_Po1 | PASS | - |
| 145 | leaf1-DC1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel6 - host1-DC1_PortChannel host1-DC1 | PASS | - |
| 146 | leaf1-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf2-DC2_Po1 | PASS | - |
| 147 | leaf1-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel6 - host1-DC2_PortChannel host1-DC1 | PASS | - |
| 148 | leaf2-DC1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf1-DC1_Po1 | PASS | - |
| 149 | leaf2-DC1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel6 - host1-DC1_PortChannel host1-DC1 | PASS | - |
| 150 | leaf2-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf1-DC2_Po1 | PASS | - |
| 151 | leaf2-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel6 - host1-DC2_PortChannel host1-DC1 | PASS | - |
| 152 | leaf3-DC1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf4-DC1_Po1 | PASS | - |
| 153 | leaf3-DC1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel6 - host2-DC1_PortChannel host2 | PASS | - |
| 154 | leaf3-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf4-DC2_Po1 | PASS | - |
| 155 | leaf3-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel6 - host2-DC2_PortChannel host2 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 156 | leaf4-DC1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf3-DC1_Po1 | PASS | - |
| 157 | leaf4-DC1 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel6 - host2-DC1_PortChannel host2 | PASS | - |
| 158 | leaf4-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel1 - MLAG_PEER_leaf3-DC2_Po1 | PASS | - |
| 159 | leaf4-DC2 | Interface State | Port-Channel Interface & Line Protocol == "up" | Port-Channel6 - host2-DC2_PortChannel host2 | FAIL | Interface shutdown: False - interface status: down - line protocol status: lowerLayerDown |
| 160 | borderleaf1-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 161 | borderleaf1-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 162 | borderleaf1-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 163 | borderleaf1-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 164 | borderleaf1-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 165 | borderleaf1-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 166 | borderleaf1-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 167 | borderleaf1-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 168 | borderleaf1-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 169 | borderleaf1-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 170 | borderleaf2-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 171 | borderleaf2-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 172 | borderleaf2-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 173 | borderleaf2-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 174 | borderleaf2-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 175 | borderleaf2-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 176 | borderleaf2-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 177 | borderleaf2-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 178 | borderleaf2-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 179 | borderleaf2-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 180 | leaf1-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 181 | leaf1-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 182 | leaf1-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 183 | leaf1-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 184 | leaf1-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 185 | leaf1-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 186 | leaf1-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 187 | leaf1-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 188 | leaf1-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 189 | leaf1-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 190 | leaf2-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 191 | leaf2-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 192 | leaf2-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 193 | leaf2-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 194 | leaf2-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 195 | leaf2-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 196 | leaf2-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 197 | leaf2-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 198 | leaf2-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 199 | leaf2-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 200 | leaf3-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 201 | leaf3-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 202 | leaf3-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 203 | leaf3-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 204 | leaf3-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 205 | leaf3-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 206 | leaf3-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 207 | leaf3-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 208 | leaf3-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 209 | leaf3-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 210 | leaf4-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 211 | leaf4-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 212 | leaf4-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 213 | leaf4-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 214 | leaf4-DC1 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 215 | leaf4-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 216 | leaf4-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 217 | leaf4-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan10 - DMZ | PASS | - |
| 218 | leaf4-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan20 - Internal | PASS | - |
| 219 | leaf4-DC2 | Interface State | Vlan Interface & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf VRF_A | PASS | - |
| 220 | borderleaf1-DC1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 221 | borderleaf1-DC2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 222 | borderleaf2-DC1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 223 | borderleaf2-DC2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 224 | leaf1-DC1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 225 | leaf1-DC2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 226 | leaf2-DC1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 227 | leaf2-DC2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 228 | leaf3-DC1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 229 | leaf3-DC2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 230 | leaf4-DC1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 231 | leaf4-DC2 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 232 | borderleaf1-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 233 | borderleaf1-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 234 | borderleaf1-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 235 | borderleaf1-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 236 | borderleaf2-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 237 | borderleaf2-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 238 | borderleaf2-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 239 | borderleaf2-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 240 | leaf1-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 241 | leaf1-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 242 | leaf1-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 243 | leaf1-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 244 | leaf2-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 245 | leaf2-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 246 | leaf2-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 247 | leaf2-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 248 | leaf3-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 249 | leaf3-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 250 | leaf3-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 251 | leaf3-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 252 | leaf4-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 253 | leaf4-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 254 | leaf4-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 255 | leaf4-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 256 | spine1-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 257 | spine1-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 258 | spine2-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 259 | spine2-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 260 | spine3-DC1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 261 | spine3-DC2 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 262 | borderleaf1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: borderleaf2-DC1_Ethernet1 | PASS | - |
| 263 | borderleaf1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: borderleaf2-DC1_Ethernet2 | PASS | - |
| 264 | borderleaf1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC1_Ethernet6 | PASS | - |
| 265 | borderleaf1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC1_Ethernet6 | PASS | - |
| 266 | borderleaf1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC1_Ethernet6 | PASS | - |
| 267 | borderleaf1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet12 - remote: DCI_Ethernet1 | PASS | - |
| 268 | borderleaf1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: borderleaf2-DC2_Ethernet1 | PASS | - |
| 269 | borderleaf1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: borderleaf2-DC2_Ethernet2 | PASS | - |
| 270 | borderleaf1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC2_Ethernet6 | PASS | - |
| 271 | borderleaf1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC2_Ethernet6 | PASS | - |
| 272 | borderleaf1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC2_Ethernet6 | PASS | - |
| 273 | borderleaf1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet12 - remote: DCI_Ethernet3 | PASS | - |
| 274 | borderleaf2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: borderleaf1-DC1_Ethernet1 | PASS | - |
| 275 | borderleaf2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: borderleaf1-DC1_Ethernet2 | PASS | - |
| 276 | borderleaf2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC1_Ethernet7 | PASS | - |
| 277 | borderleaf2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC1_Ethernet7 | PASS | - |
| 278 | borderleaf2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC1_Ethernet7 | PASS | - |
| 279 | borderleaf2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet12 - remote: DCI_Ethernet2 | PASS | - |
| 280 | borderleaf2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: borderleaf1-DC2_Ethernet1 | PASS | - |
| 281 | borderleaf2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: borderleaf1-DC2_Ethernet2 | PASS | - |
| 282 | borderleaf2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC2_Ethernet7 | PASS | - |
| 283 | borderleaf2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC2_Ethernet7 | PASS | - |
| 284 | borderleaf2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC2_Ethernet7 | PASS | - |
| 285 | borderleaf2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet12 - remote: DCI_Ethernet4 | PASS | - |
| 286 | DCI | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: borderleaf1-DC1_Ethernet12 | FAIL | core1-ISP1.arista.lab - Ethernet2 |
| 287 | DCI | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: borderleaf2-DC1_Ethernet12 | FAIL | core2-ISP1.arista.lab - Ethernet2 |
| 288 | DCI | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: borderleaf1-DC2_Ethernet12 | FAIL | core1-ISP2.arista.lab - Ethernet2 |
| 289 | DCI | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: borderleaf2-DC2_Ethernet12 | FAIL | core2-ISP2.arista.lab - Ethernet2 |
| 290 | leaf1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf2-DC1_Ethernet1 | PASS | - |
| 291 | leaf1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf2-DC1_Ethernet2 | PASS | - |
| 292 | leaf1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC1_Ethernet2 | PASS | - |
| 293 | leaf1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC1_Ethernet2 | PASS | - |
| 294 | leaf1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC1_Ethernet2 | PASS | - |
| 295 | leaf1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf2-DC2_Ethernet1 | PASS | - |
| 296 | leaf1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf2-DC2_Ethernet2 | PASS | - |
| 297 | leaf1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC2_Ethernet2 | PASS | - |
| 298 | leaf1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC2_Ethernet2 | PASS | - |
| 299 | leaf1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC2_Ethernet2 | PASS | - |
| 300 | leaf2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf1-DC1_Ethernet1 | PASS | - |
| 301 | leaf2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1-DC1_Ethernet2 | PASS | - |
| 302 | leaf2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC1_Ethernet3 | PASS | - |
| 303 | leaf2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC1_Ethernet3 | PASS | - |
| 304 | leaf2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC1_Ethernet3 | PASS | - |
| 305 | leaf2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf1-DC2_Ethernet1 | PASS | - |
| 306 | leaf2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1-DC2_Ethernet2 | PASS | - |
| 307 | leaf2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC2_Ethernet3 | PASS | - |
| 308 | leaf2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC2_Ethernet3 | PASS | - |
| 309 | leaf2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC2_Ethernet3 | PASS | - |
| 310 | leaf3-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf4-DC1_Ethernet1 | PASS | - |
| 311 | leaf3-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf4-DC1_Ethernet2 | PASS | - |
| 312 | leaf3-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC1_Ethernet4 | PASS | - |
| 313 | leaf3-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC1_Ethernet4 | PASS | - |
| 314 | leaf3-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC1_Ethernet4 | PASS | - |
| 315 | leaf3-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf4-DC2_Ethernet1 | PASS | - |
| 316 | leaf3-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf4-DC2_Ethernet2 | PASS | - |
| 317 | leaf3-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC2_Ethernet4 | PASS | - |
| 318 | leaf3-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC2_Ethernet4 | PASS | - |
| 319 | leaf3-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC2_Ethernet4 | PASS | - |
| 320 | leaf4-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf3-DC1_Ethernet1 | PASS | - |
| 321 | leaf4-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf3-DC1_Ethernet2 | PASS | - |
| 322 | leaf4-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC1_Ethernet5 | PASS | - |
| 323 | leaf4-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC1_Ethernet5 | PASS | - |
| 324 | leaf4-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC1_Ethernet5 | PASS | - |
| 325 | leaf4-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf3-DC2_Ethernet1 | PASS | - |
| 326 | leaf4-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf3-DC2_Ethernet2 | PASS | - |
| 327 | leaf4-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: spine1-DC2_Ethernet5 | PASS | - |
| 328 | leaf4-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: spine2-DC2_Ethernet5 | PASS | - |
| 329 | leaf4-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: spine3-DC2_Ethernet5 | PASS | - |
| 330 | spine1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1-DC1_Ethernet3 | PASS | - |
| 331 | spine1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf2-DC1_Ethernet3 | PASS | - |
| 332 | spine1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf3-DC1_Ethernet3 | PASS | - |
| 333 | spine1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf4-DC1_Ethernet3 | PASS | - |
| 334 | spine1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: borderleaf1-DC1_Ethernet3 | PASS | - |
| 335 | spine1-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: borderleaf2-DC1_Ethernet3 | PASS | - |
| 336 | spine1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1-DC2_Ethernet3 | PASS | - |
| 337 | spine1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf2-DC2_Ethernet3 | PASS | - |
| 338 | spine1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf3-DC2_Ethernet3 | PASS | - |
| 339 | spine1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf4-DC2_Ethernet3 | PASS | - |
| 340 | spine1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: borderleaf1-DC2_Ethernet3 | PASS | - |
| 341 | spine1-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: borderleaf2-DC2_Ethernet3 | PASS | - |
| 342 | spine2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1-DC1_Ethernet4 | PASS | - |
| 343 | spine2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf2-DC1_Ethernet4 | PASS | - |
| 344 | spine2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf3-DC1_Ethernet4 | PASS | - |
| 345 | spine2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf4-DC1_Ethernet4 | PASS | - |
| 346 | spine2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: borderleaf1-DC1_Ethernet4 | PASS | - |
| 347 | spine2-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: borderleaf2-DC1_Ethernet4 | PASS | - |
| 348 | spine2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1-DC2_Ethernet4 | PASS | - |
| 349 | spine2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf2-DC2_Ethernet4 | PASS | - |
| 350 | spine2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf3-DC2_Ethernet4 | PASS | - |
| 351 | spine2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf4-DC2_Ethernet4 | PASS | - |
| 352 | spine2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: borderleaf1-DC2_Ethernet4 | PASS | - |
| 353 | spine2-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: borderleaf2-DC2_Ethernet4 | PASS | - |
| 354 | spine3-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1-DC1_Ethernet5 | PASS | - |
| 355 | spine3-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf2-DC1_Ethernet5 | PASS | - |
| 356 | spine3-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf3-DC1_Ethernet5 | PASS | - |
| 357 | spine3-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf4-DC1_Ethernet5 | PASS | - |
| 358 | spine3-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: borderleaf1-DC1_Ethernet5 | PASS | - |
| 359 | spine3-DC1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: borderleaf2-DC1_Ethernet5 | PASS | - |
| 360 | spine3-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf1-DC2_Ethernet5 | PASS | - |
| 361 | spine3-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf2-DC2_Ethernet5 | PASS | - |
| 362 | spine3-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf3-DC2_Ethernet5 | PASS | - |
| 363 | spine3-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf4-DC2_Ethernet5 | PASS | - |
| 364 | spine3-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: borderleaf1-DC2_Ethernet5 | PASS | - |
| 365 | spine3-DC2 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet7 - remote: borderleaf2-DC2_Ethernet5 | PASS | - |
| 366 | borderleaf1-DC1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 367 | borderleaf1-DC2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 368 | borderleaf2-DC1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 369 | borderleaf2-DC2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 370 | leaf1-DC1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 371 | leaf1-DC2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 372 | leaf2-DC1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 373 | leaf2-DC2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 374 | leaf3-DC1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 375 | leaf3-DC2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 376 | leaf4-DC1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 377 | leaf4-DC2 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 378 | borderleaf1-DC1 | IP Reachability | ip reachability test p2p links | Source: borderleaf1-DC1_Ethernet12 - Destination: DCI_Ethernet1 | FAIL | 100% packet loss |
| 379 | borderleaf1-DC2 | IP Reachability | ip reachability test p2p links | Source: borderleaf1-DC2_Ethernet12 - Destination: DCI_Ethernet3 | FAIL | 100% packet loss |
| 380 | borderleaf2-DC1 | IP Reachability | ip reachability test p2p links | Source: borderleaf2-DC1_Ethernet12 - Destination: DCI_Ethernet2 | FAIL | 100% packet loss |
| 381 | borderleaf2-DC2 | IP Reachability | ip reachability test p2p links | Source: borderleaf2-DC2_Ethernet12 - Destination: DCI_Ethernet4 | FAIL | 100% packet loss |
| 382 | DCI | IP Reachability | ip reachability test p2p links | Source: DCI_Ethernet1 - Destination: borderleaf1-DC1_Ethernet12 | FAIL | 100% packet loss |
| 383 | DCI | IP Reachability | ip reachability test p2p links | Source: DCI_Ethernet2 - Destination: borderleaf2-DC1_Ethernet12 | FAIL | 100% packet loss |
| 384 | DCI | IP Reachability | ip reachability test p2p links | Source: DCI_Ethernet3 - Destination: borderleaf1-DC2_Ethernet12 | FAIL | 100% packet loss |
| 385 | DCI | IP Reachability | ip reachability test p2p links | Source: DCI_Ethernet4 - Destination: borderleaf2-DC2_Ethernet12 | FAIL | 100% packet loss |
| 386 | borderleaf1-DC1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 387 | borderleaf1-DC2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 388 | borderleaf2-DC1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 389 | borderleaf2-DC2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 390 | DCI | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 391 | leaf1-DC1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 392 | leaf1-DC2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 393 | leaf2-DC1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 394 | leaf2-DC2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 395 | leaf3-DC1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 396 | leaf3-DC2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 397 | leaf4-DC1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 398 | leaf4-DC2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 399 | spine1-DC1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 400 | spine1-DC2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 401 | spine2-DC1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 402 | spine2-DC2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 403 | spine3-DC1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 404 | spine3-DC2 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 405 | borderleaf1-DC1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.252.1 | PASS | - |
| 406 | borderleaf2-DC1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.252.3 | PASS | - |
| 407 | borderleaf2-DC2 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.252.7 | PASS | - |
| 408 | borderleaf1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.99.1 | PASS | - |
| 409 | borderleaf1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 410 | borderleaf1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 411 | borderleaf1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 412 | borderleaf1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.99.1 | PASS | - |
| 413 | borderleaf1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 414 | borderleaf1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 415 | borderleaf1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 416 | borderleaf2-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.99.1 | PASS | - |
| 417 | borderleaf2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.99.1 | PASS | - |
| 418 | borderleaf2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 419 | borderleaf2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 420 | borderleaf2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 421 | leaf1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 422 | leaf1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 423 | leaf1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 424 | leaf1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 425 | leaf1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 426 | leaf1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 427 | leaf2-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 428 | leaf2-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 429 | leaf2-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 430 | leaf2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 431 | leaf2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 432 | leaf2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 433 | leaf3-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 434 | leaf3-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 435 | leaf3-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 436 | leaf3-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 437 | leaf3-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 438 | leaf3-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 439 | leaf4-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 440 | leaf4-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 441 | leaf4-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 442 | leaf4-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.11 | PASS | - |
| 443 | leaf4-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.12 | PASS | - |
| 444 | leaf4-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.13 | PASS | - |
| 445 | spine1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.5 | PASS | - |
| 446 | spine1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.1 | PASS | - |
| 447 | spine1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.2 | PASS | - |
| 448 | spine1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.3 | PASS | - |
| 449 | spine1-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.4 | PASS | - |
| 450 | spine1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.5 | PASS | - |
| 451 | spine1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.6 | PASS | - |
| 452 | spine1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.1 | PASS | - |
| 453 | spine1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.2 | PASS | - |
| 454 | spine1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.3 | PASS | - |
| 455 | spine1-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.4 | PASS | - |
| 456 | spine2-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.5 | PASS | - |
| 457 | spine2-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.1 | PASS | - |
| 458 | spine2-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.2 | PASS | - |
| 459 | spine2-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.3 | PASS | - |
| 460 | spine2-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.4 | PASS | - |
| 461 | spine2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.5 | PASS | - |
| 462 | spine2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.6 | PASS | - |
| 463 | spine2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.1 | PASS | - |
| 464 | spine2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.2 | PASS | - |
| 465 | spine2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.3 | PASS | - |
| 466 | spine2-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.4 | PASS | - |
| 467 | spine3-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.5 | PASS | - |
| 468 | spine3-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.1 | PASS | - |
| 469 | spine3-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.2 | PASS | - |
| 470 | spine3-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.3 | PASS | - |
| 471 | spine3-DC1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.101.4 | PASS | - |
| 472 | spine3-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.5 | PASS | - |
| 473 | spine3-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.6 | PASS | - |
| 474 | spine3-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.1 | PASS | - |
| 475 | spine3-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.2 | PASS | - |
| 476 | spine3-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.3 | PASS | - |
| 477 | spine3-DC2 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.201.4 | PASS | - |
| 478 | borderleaf1-DC1 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 479 | borderleaf1-DC1 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 480 | borderleaf1-DC1 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 481 | borderleaf1-DC1 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 482 | borderleaf1-DC1 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 483 | borderleaf1-DC1 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 484 | borderleaf1-DC2 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 485 | borderleaf1-DC2 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 486 | borderleaf1-DC2 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 487 | borderleaf1-DC2 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 488 | borderleaf1-DC2 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 489 | borderleaf1-DC2 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 490 | borderleaf2-DC1 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 491 | borderleaf2-DC1 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 492 | borderleaf2-DC1 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 493 | borderleaf2-DC1 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 494 | borderleaf2-DC1 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 495 | borderleaf2-DC1 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 496 | borderleaf2-DC2 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 497 | borderleaf2-DC2 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 498 | borderleaf2-DC2 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 499 | borderleaf2-DC2 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 500 | borderleaf2-DC2 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 501 | borderleaf2-DC2 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 502 | leaf1-DC1 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 503 | leaf1-DC1 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 504 | leaf1-DC1 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 505 | leaf1-DC1 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 506 | leaf1-DC1 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 507 | leaf1-DC1 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 508 | leaf1-DC2 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 509 | leaf1-DC2 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 510 | leaf1-DC2 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 511 | leaf1-DC2 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 512 | leaf1-DC2 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 513 | leaf1-DC2 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 514 | leaf2-DC1 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 515 | leaf2-DC1 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 516 | leaf2-DC1 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 517 | leaf2-DC1 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 518 | leaf2-DC1 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 519 | leaf2-DC1 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 520 | leaf2-DC2 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 521 | leaf2-DC2 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 522 | leaf2-DC2 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 523 | leaf2-DC2 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 524 | leaf2-DC2 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 525 | leaf2-DC2 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 526 | leaf3-DC1 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 527 | leaf3-DC1 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 528 | leaf3-DC1 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 529 | leaf3-DC1 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 530 | leaf3-DC1 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 531 | leaf3-DC1 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 532 | leaf3-DC2 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 533 | leaf3-DC2 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 534 | leaf3-DC2 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 535 | leaf3-DC2 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 536 | leaf3-DC2 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 537 | leaf3-DC2 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 538 | leaf4-DC1 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 539 | leaf4-DC1 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 540 | leaf4-DC1 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 541 | leaf4-DC1 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 542 | leaf4-DC1 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 543 | leaf4-DC1 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 544 | leaf4-DC2 | Routing Table | Remote VTEP address | 192.168.102.5 | PASS | - |
| 545 | leaf4-DC2 | Routing Table | Remote VTEP address | 192.168.202.5 | PASS | - |
| 546 | leaf4-DC2 | Routing Table | Remote VTEP address | 192.168.102.1 | PASS | - |
| 547 | leaf4-DC2 | Routing Table | Remote VTEP address | 192.168.202.1 | PASS | - |
| 548 | leaf4-DC2 | Routing Table | Remote VTEP address | 192.168.102.3 | PASS | - |
| 549 | leaf4-DC2 | Routing Table | Remote VTEP address | 192.168.202.3 | PASS | - |
| 550 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 551 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 552 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 553 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 554 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 555 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 556 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 557 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 558 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 559 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 560 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 561 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 562 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 563 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 564 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 565 | borderleaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 566 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 567 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 568 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 569 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 570 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 571 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 572 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 573 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 574 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 575 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 576 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 577 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 578 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 579 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 580 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 581 | borderleaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 582 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 583 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 584 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 585 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 586 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 587 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 588 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 589 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 590 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 591 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 592 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 593 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 594 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 595 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 596 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 597 | borderleaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 598 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 599 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 600 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 601 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 602 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 603 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 604 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 605 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 606 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 607 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 608 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 609 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 610 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 611 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 612 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 613 | borderleaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 614 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 615 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 616 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 617 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 618 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 619 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 620 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 621 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 622 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 623 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 624 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 625 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 626 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 627 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 628 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 629 | leaf1-DC1 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 630 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 631 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 632 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 633 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 634 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 635 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 636 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 637 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 638 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 639 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 640 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 641 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 642 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 643 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 644 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 645 | leaf1-DC2 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 646 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 647 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 648 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 649 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 650 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 651 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 652 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 653 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 654 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 655 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 656 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 657 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 658 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 659 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 660 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 661 | leaf2-DC1 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 662 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 663 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 664 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 665 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 666 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 667 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 668 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 669 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 670 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 671 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 672 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 673 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 674 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 675 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 676 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 677 | leaf2-DC2 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 678 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 679 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 680 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 681 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 682 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 683 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 684 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 685 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 686 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 687 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 688 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 689 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 690 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 691 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 692 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 693 | leaf3-DC1 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 694 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 695 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 696 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 697 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 698 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 699 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 700 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 701 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 702 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 703 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 704 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 705 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 706 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 707 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 708 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 709 | leaf3-DC2 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 710 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 711 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 712 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 713 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 714 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 715 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 716 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 717 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 718 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 719 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 720 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 721 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 722 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 723 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 724 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 725 | leaf4-DC1 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 726 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.101.5 | PASS | - |
| 727 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.201.5 | PASS | - |
| 728 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.101.6 | PASS | - |
| 729 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.201.6 | PASS | - |
| 730 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.99.1 | PASS | - |
| 731 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.101.1 | PASS | - |
| 732 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.201.1 | PASS | - |
| 733 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.101.2 | PASS | - |
| 734 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.201.2 | PASS | - |
| 735 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.101.3 | PASS | - |
| 736 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.201.3 | PASS | - |
| 737 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.101.4 | PASS | - |
| 738 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.201.4 | PASS | - |
| 739 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.101.11 | PASS | - |
| 740 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.101.12 | PASS | - |
| 741 | leaf4-DC2 | Routing Table | Remote Lo0 address | 192.168.101.13 | PASS | - |
| 742 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 743 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 744 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 745 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 746 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 747 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 748 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 749 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 750 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 751 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 752 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 753 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 754 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 755 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 756 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 757 | borderleaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC1 - 192.168.101.5 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 758 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 759 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 760 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 761 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 762 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 763 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 764 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 765 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 766 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 767 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 768 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 769 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 770 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 771 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 772 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 773 | borderleaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf1-DC2 - 192.168.201.5 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 774 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 775 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 776 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 777 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 778 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 779 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 780 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 781 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 782 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 783 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 784 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 785 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 786 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 787 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 788 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 789 | borderleaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC1 - 192.168.101.6 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 790 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 791 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 792 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 793 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 794 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 795 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 796 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 797 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 798 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 799 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 800 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 801 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 802 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 803 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 804 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 805 | borderleaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: borderleaf2-DC2 - 192.168.201.6 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 806 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 807 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 808 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 809 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 810 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 811 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 812 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 813 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 814 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 815 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 816 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 817 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 818 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 819 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 820 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 821 | leaf1-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC1 - 192.168.101.1 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 822 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 823 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 824 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 825 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 826 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 827 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 828 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 829 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 830 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 831 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 832 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 833 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 834 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 835 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 836 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 837 | leaf1-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf1-DC2 - 192.168.201.1 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 838 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 839 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 840 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 841 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 842 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 843 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 844 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 845 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 846 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 847 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 848 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 849 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 850 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 851 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 852 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 853 | leaf2-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC1 - 192.168.101.2 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 854 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 855 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 856 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 857 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 858 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 859 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 860 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 861 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 862 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 863 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 864 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 865 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 866 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 867 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 868 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 869 | leaf2-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf2-DC2 - 192.168.201.2 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 870 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 871 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 872 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 873 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 874 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 875 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 876 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 877 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 878 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 879 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 880 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 881 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 882 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 883 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 884 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 885 | leaf3-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC1 - 192.168.101.3 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 886 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 887 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 888 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 889 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 890 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 891 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 892 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 893 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 894 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 895 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 896 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 897 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 898 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 899 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 900 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 901 | leaf3-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf3-DC2 - 192.168.201.3 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 902 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 903 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 904 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 905 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 906 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 907 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 908 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 909 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 910 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 911 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 912 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 913 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 914 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 915 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 916 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 917 | leaf4-DC1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC1 - 192.168.101.4 Destination: 192.168.101.13 | FAIL | 100% packet loss |
| 918 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.5 | FAIL | 100% packet loss |
| 919 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.5 | FAIL | 100% packet loss |
| 920 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.6 | FAIL | 100% packet loss |
| 921 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.6 | FAIL | 100% packet loss |
| 922 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.99.1 | FAIL | 100% packet loss |
| 923 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.1 | FAIL | 100% packet loss |
| 924 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.1 | FAIL | 100% packet loss |
| 925 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.2 | FAIL | 100% packet loss |
| 926 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.2 | FAIL | 100% packet loss |
| 927 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.3 | FAIL | 100% packet loss |
| 928 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.3 | FAIL | 100% packet loss |
| 929 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.4 | FAIL | 100% packet loss |
| 930 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.201.4 | FAIL | 100% packet loss |
| 931 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.11 | FAIL | 100% packet loss |
| 932 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.12 | FAIL | 100% packet loss |
| 933 | leaf4-DC2 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf4-DC2 - 192.168.201.4 Destination: 192.168.101.13 | FAIL | 100% packet loss |
