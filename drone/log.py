#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
© Copyright 2015-2016, 3D Robotics.
vehicle_state.py: 

Demonstrates how to get and set vehicle state and parameter information, 
and how to observe vehicle attribute (state) changes.

Full documentation is provided at http://python.dronekit.io/examples/vehicle_state.html
"""
from __future__ import print_function
from dronekit import connect, VehicleMode
import time
import requests
import getpass
import datetime
import pyudev
import subprocess

user = getpass.getuser()
URL = "http://13.125.54.237:3000/memo"
context = pyudev.Context()

#Set up option parsing to get connection string
import argparse  
parser = argparse.ArgumentParser(description='Print out vehicle state information. Connects to SITL on local PC by default.')
parser.add_argument('--connect', 
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = '/dev/ttyACM0'



# Connect to the Vehicle. 
#   Set `wait_ready=True` to ensure default attributes are populated before `connect()` returns.
print("\nConnecting to vehicle on: %s" % connection_string)
vehicle = connect(connection_string, wait_ready=True)

vehicle.wait_ready('autopilot_version')

ff=0
while True:
    try:
        time.sleep(1.5)
        print("DEVICE DEBUG MESSAGE")
        pyudev.Devices.from_device_file(context, '/dev/usb/hiddev0')
        print("YUBIKEY CONNTECTED")
        time.sleep(1.5)
        requests.post(URL, json={'Yubikey Status': "CONNECTED"})

    except:
        time.sleep(1.5)
        print("YUBIKEY DISCONNECTED")
        requests.post(URL, json={'Yubikey Status': "DISCONNECTED"})
        break
    curtime = datetime.datetime.now()
    print("\nGet all vehicle attribute values:")
    print(" Autopilot Firmware version: %s" % vehicle.version)
    print(" Global Location: %s" % vehicle.location.global_frame)
    print(" Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
    print(" Local Location: %s" % vehicle.location.local_frame)
    print(" Attitude: %s" % vehicle.attitude)
    print(" Velocity: %s" % vehicle.velocity)
    print(" GPS: %s" % vehicle.gps_0)
    print(" Battery: %s" % vehicle.battery)
    print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
    print(" Heading: %s" % vehicle.heading)
    print(" Is Armable?: %s" % vehicle.is_armable)
    print(" System status: %s" % vehicle.system_status.state)
    print(" Groundspeed: %s" % vehicle.groundspeed)    # settable
    print(" Airspeed: %s" % vehicle.airspeed)    # settable
    print(" Mode: %s" % vehicle.mode.name)    # settable
    print(" Armed: %s" % vehicle.armed)    # settable
    print(" User: %s" % user)
    print(" Time : %s" % curtime)
    requests.post(URL, json={'Autopilot Firmware Version': "%s"%vehicle.version,
        'Global Location': "%s"%vehicle.location.global_frame,
        'Global Location (relative altitude)': "%s"%vehicle.location.global_relative_frame,
        'Local Location': "%s"%vehicle.location.local_frame,
        'Attitude': "%s"%vehicle.attitude,
        'Velocity': "%s"%vehicle.velocity,
        'GPS': "%s"%vehicle.gps_0,
        'Battery': "%s"%vehicle.battery,
        'Last Heartbeat': "%s"%vehicle.last_heartbeat,
        'Heading': "%s"%vehicle.heading,
        'Is Armable': "%s"%vehicle.is_armable,
        'System status': "%s"%vehicle.system_status.state,
        'Groundspeed': "%s"%vehicle.groundspeed,
        'Airspeed': "%s"%vehicle.airspeed,
        'Mode': "%s"%vehicle.mode.name,
        'Armed': "%s"%vehicle.armed,
        'User': "%s"%user,
        'Time': "%s"%curtime})
        
    ff=ff+1
    time.sleep(2)
    if ff == 10:
        break
    
time.sleep(2)

#Close vehicle object before exiting script
print("\nClose vehicle object")
vehicle.close()
print("Completed")
print("Blocking Drone Controll")
time.sleep(5)
subprocess.call('./stop.sh', shell=True)



