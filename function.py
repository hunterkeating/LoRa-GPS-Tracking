from math import sin, cos, sqrt, atan2, radians, pi, atan, degrees
R=6373.0 # Radius of Earth in km

def distance_function(thislati,thislong,otherlati,otherlong): # Defining distance function
    otherlat=float(otherlati) # Converting str to float
    otherlon=float(otherlong)
    thislat=float(thislati)
    thislon=float(thislong)
    thislatr=radians(thislat) # Converting degrees to radians
    thislonr=radians(thislon)
    otherlatr=radians(otherlat)
    otherlonr=radians(otherlon)
    dlat=otherlatr-thislatr # Difference in between the 2 nodes latitude 
    dlon=otherlonr-thislonr # Difference in between the 2 nodes longitude
    a=sin(dlat/2)**2+cos(thislatr)*cos(otherlatr)*sin(dlon/2)**2 # Haversines formulas (determines distance in m given two gps coordinates in radians)
    c=2*atan2(sqrt(a),sqrt(1-a)) # Haversines formulas
    distance=(R*c)*1000 # Haversines formulas
    print("Distance in meters:", distance)


def angle_function(thislati,thislong,otherlati,otherlong):
    otherlat=float(otherlati)
    otherlon=float(otherlong)
    thislat=float(thislati)
    thislon=float(thislong)
    thislatr=radians(thislat)
    thislonr=radians(thislon)
    otherlatr=radians(otherlat)
    otherlonr=radians(otherlon)
    dlat=otherlatr-thislatr
    dlon=otherlonr-thislonr

    # Determining which quadrant other lat long is with respect to this lat long
    if otherlatr==thislatr and otherlonr==thislonr:
        print('You are supposedly on top of eachother')
        result=0 # Assigns angle between this location and other location clockwise from true north
    elif otherlonr>thislonr:
        if otherlatr==thislatr:
            print('True East')
            result=(pi/2) # Assigns angle between this location and other location clockwise from true north
        elif otherlatr>thislatr:
            result=atan(abs(dlon)/abs(dlat)) # Assigns angle between this location and other location clockwise from true north
        elif otherlatr<thislatr:
            result=(pi/2)+atan(abs(dlat)/abs(dlon)) # Assigns angle between this location and other location clockwise from true north
    elif otherlonr<thislonr:
        if otherlatr==thislatr:
            print('True West')
            result=(1.5*pi) # Assigns angle between this location and other location clockwise from true north
        elif otherlatr<thislatr:
            result=(pi)+atan(abs(dlon)/abs(dlat)) # Assigns angle between this location and other location clockwise from true north
        elif otherlatr>thislatr:
            result=(1.5*pi)+atan(abs(dlat)/abs(dlon)) # Assigns angle between this location and other location clockwise from true north
    elif otherlonr==thislonr:
        if otherlatr>thislatr:
            print('True North')
            result=0 # Assigns angle between this location and other location clockwise from true north
        elif otherlatr<thislatr:
            print('True South')
            result=pi # Assigns angle between this location and other location clockwise from true north
    final_angle=degrees(result) # Converts angle in radians to degrees
    print("Angle clockwise from true north:", final_angle) # Prints angle clockwise from true north
