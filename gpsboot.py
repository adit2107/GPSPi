import os
import time

print("Initializing gps")
print(os.getpid())
time.sleep(20)
os.system("/usr/bin/python3 /home/pi/Desktop/TCPGPSSOCKET_working/mpu_gps_logging.py")
