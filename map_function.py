def valmap(value, istart, istop, ostart, ostop):
  return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))

def calc_angle(final_angle):
    #angle = 270
    value_to_send = valmap(final_angle, 0, 360, 0, 1)

    if final_angle <= 180: # Adjustment because the Orbit Plugin uses values from 0-1 with 1 being 180 degrees and 0.5 at 0 degrees
        value_to_send += 0.5
    elif final_angle > 180:
        value_to_send -= 0.5

    print('Value to send=', value_to_send)
    return value_to_send
