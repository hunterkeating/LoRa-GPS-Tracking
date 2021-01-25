import subprocess
from datetime import datetime
from function import distance_function,angle_function
from math import atan2,degrees


otherlati = '' # Setting base variables so function will continue to run until variables are no longer blank
thislati = ''
otherlong = ''
thislong = ''
run = ''
cycle = 1

# Takes data from input command in terminal and enables Python parsing
p = subprocess.Popen(['sudo', 'mosquitto_sub', '-t', 'application/7/device/ac1f09fffe0036f7/#', '-t', 'application/7/device/ac1f09fffe00371d/#', '-v'], stdout=subprocess.PIPE) # Device 2 and 3

for row in iter(p.stdout.readline, ''): # Reading the data
    x = row.rstrip() # Removes trailing chars
    y = x.decode("utf-8") # Standard to use for character. y holds useful data

    ## Determining if the incoming packet is from device #2 or device #3
    if y[21:37] == 'ac1f09fffe00371d': # ID for device # 3
        keyword='"gps":' # Defines keyword as "gps":
        before_keyword, keyword, after_keyword = y.partition(keyword) # Splits data into everything before, kw, and everything after
        keyword='"latitude":' # Redefines keyword as "latitude":
        before_keyword, keyword, after_keyword = after_keyword.partition(keyword) # Splits data from previous after_keyword into new before_keyword, kw, after_keyword
        if 'gps' in y: # Ensures that packet has the data we are looking for
            if after_keyword[1] == '-': # Determines length of data depending on if the latitude is a positive number or negative number
                otherlati=after_keyword[1:11]
            else:
                otherlati=after_keyword[1:10]

        keyword='"gps":' # Defines keyword as "gps":
        before_keyword, keyword, after_keyword = y.partition(keyword) # Splits data into everything before, kw, and everything after
        keyword='"longitude":' # Redefines keyword as "longitude":
        before_keyword, keyword, after_keyword = after_keyword.partition(keyword) # Splits data from previous after_keyword into new before_keyword, kw, after_keyword
        if 'gps' in y: # Ensures that packet has the data we are looking for
            if after_keyword[1] == '-': # Determines length of data depending on if the latitude is a positive number or negative number
                otherlong=after_keyword[1:11]
            else:
                otherlong=after_keyword[1:10]

    ## Repeats Process for second device (device #2)
    if y[21:37] == 'ac1f09fffe0036f7': # ID for device # 2
        keyword='"gps":'
        before_keyword, keyword, after_keyword = y.partition(keyword)
        keyword='"latitude":'
        before_keyword, keyword, after_keyword = after_keyword.partition(keyword)
        if 'gps' in y:
            if after_keyword[1] == '-':
                thislati=after_keyword[1:11]
            else:
                thislati=after_keyword[1:10]

        keyword='"gps":'
        before_keyword, keyword, after_keyword = y.partition(keyword)
        keyword='"longitude":'
        before_keyword, keyword, after_keyword = after_keyword.partition(keyword)
        if 'gps' in y:
            if after_keyword[1] == '-':
                thislong=after_keyword[1:11]
            else:
                thislong=after_keyword[1:10]

        # Magnetometer reading
        keyword='"magnetometer":' # Defines magnetometer as keyword
        before_keyword, keyword, after_keyword = y.partition(keyword) # Splits data into three different sections
        keyword='"x":' # Redefines keyword as "x":
        before_keyword, keyword, after_keyword = after_keyword.partition(keyword) # Splits data into three different sections
        X=after_keyword[1:7] # Defines desired data as X
        if 'magnetometer' in y:
            if X[1] == '-': # Ensuring that the correct amount of data is parsed
                X=after_keyword[1:7]
                if 'μ' in X:
                    X=after_keyword[1:6]
            else:
                X=after_keyword[1:6]
                if 'μ' in X:
                    X=after_keyword[1:5]
        keyword='"y":' # Redefines keyword as "y":
        before_keyword, keyword, after_keyword = after_keyword.partition(keyword) # Splits data into three different sections
        Y=after_keyword[1:7] # Defines desired data as Y
        if 'magnetometer' in y:
            if Y[1] == '-': # Ensuring that the correct amount of data is parsed
                Y=after_keyword[1:7]
                if 'μ' in Y:
                    Y=after_keyword[1:6]
            else:
                Y=after_keyword[1:6]
                if 'μ' in Y:
                    Y=after_keyword[1:5]


            # Calibration
            if cycle == 2: # Ensuring that east calibration happens on the second cycle
                y1 = Y # Determing magnetometers y position in magnetic field
                print('East calibrated')
                cycle = cycle + 1
            elif cycle == 1: # Ensuring that North calibration happens on the first cycle
                x1 = X # Determing magnetometers x position in magnetic field
                print('North calibrated')
                cycle = cycle + 1
            else:
                x1 = float(x1) # Converts strings into floats
                y1 = float(y1)
                X = float(X)
                Y = float(Y)
                X = X - x1 # Taking the difference between the X value from new reading and magnetometers x position in magnetic field
                Y = Y - y1 # Taking the difference between the Y value from new reading and magnetometers y position in magnetic field
                heading = atan2(X,Y) # Taking inverse tangent to determine heading
                heading = degrees(heading) # Converting heading into degrees
                if heading < 0: # If heading is less that zero 360 must be added to ensure that we always have positive angles
                    heading = heading + 360
                run = 'go'


    if len(otherlati) == 0 or len(thislati) == 0 or len(run) == 0: # Checks if variables have values attached to them to perform calculations
        continue
    elif cycle > 2:
        distance_function(thislati,thislong,otherlati,otherlong) # Puts variables into previously defined function and prints distance
        angle_function(thislati,thislong,otherlati,otherlong,heading) # Prints variables into previously defined function and prints angle


        now=datetime.now() # Pulls the time
        current_time=now.strftime("%H:%M:%S") # Defines format of the time
        print('Time=', current_time, '\n') # Prints the time