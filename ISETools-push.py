#Simple config push script for writing configs to Cisco IOS Devices
#Part of ISETools by @RockstarWiFi - WiFiTraining.com / ActiveExpert.com
#Requires text file 'devices' with list of IPv4 addresses you want to push code to, 1 per line, no spaces. 
#Requires 'commands' text file with list of commands, no confg t needed, 1 command per line, no spaces.

from netmiko import ConnectHandler

with open('commands.ios') as f:
    commands_list = f.read().splitlines()

with open('devices') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'chris',
        'password': 'Cisco123'
    }

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(commands_list)
    print (output)
