from math import sin, cos, sqrt, atan2, radians, pi, atan, degrees
R=6373.0

def distance_function(thislati,thislong,otherlati,otherlong):
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
    a=sin(dlat/2)**2+cos(thislatr)*cos(otherlatr)*sin(dlon/2)**2
    c=2*atan2(sqrt(a),sqrt(1-a))
    distance=(R*c)*1000
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
    if otherlatr==thislatr and otherlonr==thislonr:
        print('You are supposedly on top of eachother')
        result=0
    elif otherlonr>thislonr:
        if otherlatr==thislatr:
            print('True East')
            result=(pi/2)
        elif otherlatr>thislatr:
            result=atan(abs(dlon)/abs(dlat))
        elif otherlatr<thislatr:
            result=(pi/2)+atan(abs(dlat)/abs(dlon))
    elif otherlonr<thislonr:
        if otherlatr==thislatr:
            print('True West')
            result=(1.5*pi)
        elif otherlatr<thislatr:
            result=(pi)+atan(abs(dlon)/abs(dlat))
        elif otherlatr>thislatr:
            result=(1.5*pi)+atan(abs(dlat)/abs(dlon))
    elif otherlonr==thislonr:
        if otherlatr>thislatr:
            print('True North')
            result=0
        elif otherlatr<thislatr:
            print('True South')
            result=pi
    final_angle=degrees(result)
    print("Angle clockwise from true north:", final_angle)