
mlag = 1
group = 3
for leaf in range(5,100):
    sgroup = str(group)
    sleaf = str(leaf)
 #   print("    - group: mlag"+sgroup)
 #   print("      nodes:")
    print("    - name: leaf"+sleaf)
    print("      id:", sleaf)
    ip = leaf + 100
    ip = str(ip)
    uplink = leaf + 2
    uplink = str(uplink)
    print("      mgmt_ip: 192.168.0."+ip)
    print("      uplink_switch_interfaces: [Ethernet"+uplink+", Ethernet"+uplink+", Ethernet"+uplink+", Ethernet"+uplink+", Ethernet"+uplink+", Ethernet"+uplink+"]") 
    group = group + 1

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
