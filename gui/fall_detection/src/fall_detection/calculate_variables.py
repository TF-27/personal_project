import math
import numpy

def calculate_Asvm(x, y, z):
    # m/s^2 to mg
    ax = x / 0.00980665
    ay = y / 0.00980665
    az = z / 0.00980665
    return math.sqrt(ax**2 + ay**2 + az**2)

def calculate_Gsvm(x, y, z):
    gx = x * 180 / math.pi
    gy = y * 180 / math.pi
    gz = z * 180 / math.pi #conversions from rad/s to degrees/s

    return math.sqrt(gx**2 + gy**2 + gz**2)


def calculate_deviation(selected_frame):
    mu = numpy.mean(selected_frame)
    sum_array = []
    for svm in selected_frame:
        sum_array.append((svm-mu)**2)
    deviation = numpy.sum(sum_array) / len(selected_frame)
    deviation = math.sqrt(deviation)
    
    return deviation

def calculate_mean_psi_abs(gyro_frame_dictionary):
    psirray = []
    for time in range(0,len(gyro_frame_dictionary['t'])):
        psi = numpy.arctan(gyro_frame_dictionary['y'][time] / math.sqrt(gyro_frame_dictionary['z'][time]**2 + gyro_frame_dictionary['x'][time]**2)) #correct so x,y,z are elements of time
        psirray.append(psi)
    mean_psi = numpy.sum(psirray) / len(psirray)
    return numpy.absolute(mean_psi)
