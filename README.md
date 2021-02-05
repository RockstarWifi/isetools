# isetools
A few tools to simplify deploying Cisco Identity Services Engine ISE & all that this entails. 
Will be adding several of the scripts we use at Active Expert / WiFi Training with our mentored consulting engagement.
ISE 3.0, ISE 2.7, ise 2.6, ise 2.4, ise 2.3, ise 2.1, ise 2.0, ise 1.4, ise 1.3, ise 1.2, ISE. 
Support for all types of Cisco IOS / IOS-XE devices / look for code\platform specific instructions. 

To use this script you must have the following installed
Python 3.6+
Netmiko

Download the isetools files using git or copy paste the text to your local machine. 

There are 3 files required to make the script work, and keep it SUPER SIMPLE. 
devices - list of IP addresses you want to push a configuration to, paste 1 IP per line.
commands.ios - text file with list of IOS or IOS-XE commands to deploy to the devicves in the devices file
ISETools-push.py - Script which makes the magic work, whichever commands used in commands.ios will be entered in each device, just as if you were sitting at the terminal. 

If you want to save the config to the device with the same script, use write mem at the end of your config in commands.ios (text file). 

NOTE - If you are NEW to Python, DO NOT MODIFY the script, even changing the spacing or tabs can break it with python's nested configs. 

It's best to test this with 1 devices, then you can replicate to as many devices as you like. This script is not efficient if you have hundreds to do quickly. 
