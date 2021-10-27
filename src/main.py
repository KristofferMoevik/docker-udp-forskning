# Import mavutil
from pymavlink import mavutil
import sys
import time

# def pymav():
#     userinput = input("Start takeoff?")
#     # Create the connection
#     master = mavutil.mavlink_connection('udpin:0.0.0.0:14551')
#     # Wait a heartbeat before sending commands
#     for i in range(0,3):
#         print("Waiting for heartbeat ...")
#         master.wait_heartbeat()
#         print("It's alive.")
#     print("trying to arm")

#     #
#     #   Arm
#     #

#     if(not master.motors_armed()):
#         master.mav.command_long_send(
#         master.target_system,
#         master.target_component,
#         mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
#         0,
#         1, 0, 0, 0, 0, 0, 0)
        
                
#         # wait until arming confirmed (can manually check with master.motors_armed())
#         print("Waiting for the vehicle to arm ...")
#         master.motors_armed_wait()
#         print('Armed.')
#     else:
#         print('Motors already armed.')


#     #
#     #   Set mode
#     #

#     print('Setting mode ...')

#     # Choose a mode
#     mode = 'GUIDED'

#     # Check if mode is available
#     if mode not in master.mode_mapping():
#         print('Unknown mode : {}'.format(mode))
#         print('Try:', list(master.mode_mapping().keys()))
#         sys.exit(1)

#     # Mode name to int
#     mode_id = master.mode_mapping()[mode]
#     # Command
#     # master.mav.command_long_send(
#     #    master.target_system, master.target_component,
#     #    mavutil.mavlink.MAV_CMD_DO_SET_MODE,
#     #    0,
#     #    0, # Custom mode
#     #    mode_id, # Custom submode
#     #    0,
#     #    0,
#     #    0,
#     #    0,
#     #    0)

#     master.set_mode(mode_id)

#     # while True:
#     #     # Wait for ACK command
#     #     ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
#     #     ack_msg = ack_msg.to_dict()

#     #     # Check if command in the same in `set_mode`
#     #     if ack_msg['command'] != mavutil.mavlink.MAVLINK_MSG_ID_SET_MODE:
#     #         continue

#     #     # Print the ACK result !
#     #     print(mavutil.mavlink.enums['MAV_RESULT'][ack_msg['result']].description)
#     #     break

#     print('Mode set.')


#     #
#     #   Take-off
#     #

#     print('Sending takeoff ...')

#     master.mav.command_long_send(
#         master.target_system,
#         master.target_component,
#         mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
#         0,
#         0, # pitch https://mavlink.io/en/messages/common.html
#         0, 
#         0,
#         0, # yaw
#         0, # lat
#         0, # long
#         3) # alt

#     print('Takeoff sent.')

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 14552
MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
