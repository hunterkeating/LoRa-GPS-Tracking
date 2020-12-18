import subprocess
from datetime import datetime
from function import distance_function,angle_function

otherlati = ''
thislati = ''
otherlong = ''
thislong = ''

p = subprocess.Popen(['sudo', 'mosquitto_sub', '-t', 'application/7/device/ac1f09fffe0036ef/#', '-t', 'application/7/device/ac1f09fffe00371d/#', '-v'], stdout=subprocess.PIPE) #device 2 and 3

for row in iter(p.stdout.readline, ''):
    x = row.rstrip()
    y = x.decode("utf-8")

    print(y)
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    print('Time=', current_time, '\n')