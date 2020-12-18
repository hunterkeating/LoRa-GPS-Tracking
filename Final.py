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

    if '"gpsLocation"' in y:
        if y[21:37] == 'ac1f09fffe00371d':

            keyword='"gpsLocation":'
            before_keyword, keyword, after_keyword = y.partition(keyword)
            keyword='"latitude":'
            before_keyword, keyword, after_keyword = after_keyword.partition(keyword)

            if after_keyword[0] == '-':
                thislati=after_keyword[0:8]
                if ',' in thislati:
                    thislati=after_keyword[0:7]
            else:
                thislati=after_keyword[0:7]
                if ',' in thislati:
                    thislati=after_keyword[0:6]

            keyword='"gpsLocation":'
            before_keyword, keyword, after_keyword = y.partition(keyword)
            keyword='"longitude":'
            before_keyword, keyword, after_keyword = after_keyword.partition(keyword)

            if after_keyword[0] == '-':
                thislong=after_keyword[0:8]
                if ',' in thislong:
                    thislong=thislong[0:7]
            else:
                thislong=after_keyword[0:7]
                if ',' in thislong:
                    thislong=thislong[0:6]


        elif y[21:37] == 'ac1f09fffe0036ef':

            keyword='"gpsLocation":'
            before_keyword, keyword, after_keyword = y.partition(keyword)
            keyword='"latitude":'
            before_keyword, keyword, after_keyword = after_keyword.partition(keyword)

            if after_keyword[0] == '-':
                otherlati=after_keyword[0:8]
                if ',' in otherlati:
                    otherlati=after_keyword[0:7]
            else:
                otherlati=after_keyword[0:7]
                if ',' in otherlati:
                    otherlati=after_keyword[0:6]

            keyword='"gpsLocation":'
            before_keyword, keyword, after_keyword = y.partition(keyword)
            keyword='"longitude":'
            before_keyword, keyword, after_keyword = after_keyword.partition(keyword)

            if after_keyword[0] == '-':
                otherlong=after_keyword[0:8]
                if '}' in otherlong:
                    otherlong=otherlong[0:7]
            else:
                otherlong=after_keyword[0:7]
                if '}' in otherlong:
                    otherlong=otherlong[0:6]


        if len(otherlati) == 0 or len(thislati) == 0:
            continue
        else:
            distance_function(thislati,thislong,otherlati,otherlong)
            angle_function(thislati,thislong,otherlati,otherlong)

        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        print('Time=', current_time, '\n')