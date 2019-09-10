from __future__ import print_function
# import mavutil
from pymavlink import mavutil
from dronekit import connect, VehicleMode
import time

# create the connection
# From topside computer
connection_string = '/dev/ttyACM0'
master = mavutil.mavlink_connection(connection_string)
master.wait_heartbeat()


master.mav.param_request_list_send(master.target_system, master.target_component)
master.mav.param_request_read_send(master.target_system, master.target_component, b'CBRK_IO_SAFETY', -1)
#master.mav.param_request_read_send(master.target_system, master.target_component, b'CBRK_IO_SAFETY', -1)
print('param recv complete')

'''
while True:
    try:
        message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
        
        print('name: %s\tvalue: %f' % (message['param_id'].decode("utf-8"), message['param_value']))
    except Exception as e:
        print(e)
        exit(0)
'''

time.sleep(0.5)
# Set io process
master.mav.param_set_send(master.target_system, master.target_component, b'CBRK_IO_SAFETY', 0, mavutil.mavlink.MAV_PARAM_TYPE_INT32)
#master.mav.param_set_send(master.target_system, master.target_component, b'CBRK_USB_CHK', 0, mavutil.mavlink.MAV_PARAM_TYPE_INT32)
#master.mav.param_set_send(master.target_system, master.target_component, b'CBRK_SUPPLY_CHK', 0, mavutil.mavlink.MAV_PARAM_TYPE_INT32)
print('io set complete')


# read ACK, IMPORTANT
num=0
message=None
while num<50:
    try:
        message = master.recv_match().to_dict()
        #print('name: %s\tvalue: %f' % (message['param_id'].decode("utf-8"), message['param_value']))
        num=num+1
    except Exception as e:
        break

#master.recv_match().to_dict()

# request param to confirm
master.mav.param_request_read_send(master.target_system, master.target_component, b'CBRK_IO_SAFETY', -1)
#master.mav.param_request_read_send(master.target_system, master.target_component, b'CBRK_USB_CHK', -1)
#master.mav.param_request_read_send(master.target_system, master.target_component, b'CBRK_SUPPLY_CHK', -1)
print('io request complete')


# USB set
#
#
master.mav.param_request_read_send(master.target_system, master.target_component, b'CBRK_USB_CHK', -1)
master.mav.param_set_send(master.target_system, master.target_component, b'CBRK_USB_CHK', 0, mavutil.mavlink.MAV_PARAM_TYPE_INT32)
# read ACK, IMPORTANT
num=0
message=None
while num<50:
    try:
        message = master.recv_match().to_dict()
        #print('name: %s\tvalue: %f' % (message['param_id'].decode("utf-8"), message['param_value']))
        num=num+1
    except Exception as e:
        break
master.mav.param_request_read_send(master.target_system, master.target_component, b'CBRK_USB_CHK', -1)
print('USB check complete')

'''
# set SUPPLY
#
#
master.mav.param_set_send(master.target_system, master.target_component, b'CBRK_SUPPLY_CHK', 0, mavutil.mavlink.MAV_PARAM_TYPE_INT32)
# read ACK, IMPORTANT
num=0
message=None
while num<50:
    try:
        message = master.recv_match().to_dict()
        #print('name: %s\tvalue: %f' % (message['param_id'].decode("utf-8"), message['param_value']))
        num=num+1
    except Exception as e:
        break
master.mav.param_request_read_send(master.target_system, master.target_component, b'CBRK_SUPPLY_CHK', -1)
print('SUPPLY check complete')
'''
#reboot
master.close()
vehicle = connect(connection_string, wait_ready=True)
vehicle.reboot()
print('reboot?')
