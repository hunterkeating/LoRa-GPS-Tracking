import subprocess
from datetime import datetime
from function import distance_function,angle_function

otherlati = '' # Setting base variables so function will continue to run until variables are no longer blank
thislati = ''
otherlong = ''
thislong = ''

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
                thislati=after_keyword[1:11]
            else:
                thislati=after_keyword[1:10]

        keyword='"gps":' # Defines keyword as "gps":
        before_keyword, keyword, after_keyword = y.partition(keyword) # Splits data into everything before, kw, and everything after
        keyword='"longitude":' # Redefines keyword as "longitude":
        before_keyword, keyword, after_keyword = after_keyword.partition(keyword) # Splits data from previous after_keyword into new before_keyword, kw, after_keyword
        if 'gps' in y: # Ensures that packet has the data we are looking for
            if after_keyword[1] == '-': # Determines length of data depending on if the latitude is a positive number or negative number
                thislong=after_keyword[1:11]
            else:
                thislong=after_keyword[1:10]

    ## Repeats Process for second device (device #2)
    if y[21:37] == 'ac1f09fffe0036f7': # ID for device # 2
        keyword='"gps":'
        before_keyword, keyword, after_keyword = y.partition(keyword)
        keyword='"latitude":'
        before_keyword, keyword, after_keyword = after_keyword.partition(keyword)
        if 'gps' in y:
            if after_keyword[1] == '-':
                otherlati=after_keyword[1:11]
            else:
                otherlati=after_keyword[1:10]

        keyword='"gps":'
        before_keyword, keyword, after_keyword = y.partition(keyword)
        keyword='"longitude":'
        before_keyword, keyword, after_keyword = after_keyword.partition(keyword)
        if 'gps' in y:
            if after_keyword[1] == '-':
                otherlong=after_keyword[1:11]
            else:
                otherlong=after_keyword[1:10]


    if len(otherlati) == 0 or len(thislati) == 0: # Checks if variables have values attached to them to perform calculations
        continue
    else:
        distance_function(thislati,thislong,otherlati,otherlong) # Puts variables into previously defined function and prints distance
        angle_function(thislati,thislong,otherlati,otherlong) # Prints variables into previously defined function and prints angle

    now=datetime.now() # Pulls the time
    current_time=now.strftime("%H:%M:%S") # Defines format of the time
    print('Time=', current_time, '\n') # Prints the time