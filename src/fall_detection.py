import numpy
import math
from calculate_variables import calculate_deviation, calculate_mean_psi_abs, calculate_Asvm
from csv_tests import get_data
import random #remove in final code! Is for testing at random only!
import sys
from fall_object import PotentialFall


## NEW IDEAS:
# Detection is a call in main(). Calls get_gyro() and get_acc() every 1/100 s (2/200 right?). Then builds an instance of a class 'fall', which then starts collecting the 199 samples after that and storing it. 
# That class can then have properties like which phases were checked as well-> export to store on hd for analyses.
# Finally the class will have an alert status set to false/true. At check 6 if it's true -> raise alarm.


#NumPy may be usefull for storing data. It works more like C! 
#Boots suggestions for going to a phone

def detect_fall():
    accelerometer_data = get_data("acc")
    gyro_data = get_data("gyro")
    test_next = False
    data_log = []

    for time in range(0,len(accelerometer_data.t)-200):
        test_object = PotentialFall(accelerometer_data, gyro_data, time)

        #Phase 1
        print("\n###########################################\n")
        if phase_one(test_object):
            print("Phase one positive")
            test_object.last_phase = 1
            test_next = True
        else:
            print("Phase one negative")
            test_next = False
            # not logging, too much data. Logging past phase 2

        while test_next:
            #Phase 2
            if phase_two(test_object, accelerometer_data): #will have to adapt when going with the live feed
                print("Phase two positve")
                test_object.last_phase = 2
            else:
                print("Phase two negative")
                test_next = False
                continue

            #Phase 3
            if phase_three(test_object):
                print("Phase three positive")
                test_object.last_phase = 3
            else:
                print("Phase three negative")
                test_next = False
                data_log.append(test_object.time)
                continue

            #Phase 4
            if phase_four(test_object, gyro_data):
                print("Phase four positive")
                test_object.last_phase = 4
            else:
                test_next = False
                data_log.append(test_object.time)
                continue
            
            #Phase 5
            if phase_five(test_object):
                print("Phase five positive")
                test_object.last_phase = 5
            else:
                test_next = False
                data_log.append(test_object)
                continue

            #Phase 6
            data_log.append(phase_six(test_object))
            return data_log
            
            print("\n###########################################\n")
    return data_log


# Test log:
#return f"\nTest object size: {sys.getsizeof(test_object)}\ntime: {test_object.time}\n\nasvm_list:\n{test_object.asvm_list}\n\nacc_frame:\nX\n{test_object.acc_frame['x']}\nY\n{test_object.acc_frame['y']}\nZ\n{test_object.acc_frame['z']}\n\ngyro_frame:\nX\n{test_object.gyro_frame['x']}\nY\n{test_object.gyro_frame['y']}\nZ\n{test_object.gyro_frame['z']}\n\nMean Psi: {test_object.mean_psi}"


def phase_one(test_object):
    if calculate_Asvm(test_object.acc_x, test_object.acc_y, test_object.acc_z) < 800: #CHANGE TO SET VARIABLE FORM LIST (MAIN BRANCH)
        return True
    return False

def phase_two(test_object, accelerometer_data):
    test_object.acc_frame = test_object.generate_test_frame(accelerometer_data, test_object.time, "acc")
    test_object.asvm_list = test_object.calculate_asvm_list()
    for asvm in test_object.asvm_list:
        if asvm > 1000: #import test limit from main branch ORIGINAL IS 1400
            return True
    return False

def phase_three(test_object):
    deviation_sample_acc = calculate_deviation(test_object.asvm_list[150:])
    if deviation_sample_acc < 100:
        return True
    return False

def phase_four(test_object, gyro_data):
    test_object.gyro_frame = test_object.generate_test_frame(gyro_data, test_object.time, "gyro")
    test_object.gsvm_list = test_object.calculate_gsvm_list()
    deviation_sample_gyro = calculate_deviation(test_object.gsvm_list[150:])
    if deviation_sample_gyro < 10:
        return True
    return False

def phase_five(test_object):
    gyro_frame_psi = {
        't': test_object.gyro_frame['t'][180:],
        'x': test_object.gyro_frame['x'][180:],
        'y': test_object.gyro_frame['y'][180:],
        'z': test_object.gyro_frame['z'][180:],
    }
    test_object.mean_psi = calculate_mean_psi_abs(gyro_frame_psi)
    if test_object.mean_psi < 60:
        return True
    return False

def phase_six(test_object):
    print("All checks positive, raising the alarm\nSending GPS")
    return test_object.time
    #function_to_alarm_wearer + countdown clock
    #function to alarm emergency contact at clock == 00:00
    #function to call emergency services if emergency contact doesn't answer?
    #Either return to phase 1/detect fall or have main always calling phase 1/detect fall

# Or do we generate an instance of a class? Containing the accelerometer and gyro data of that frame? That way we don't have to push down the data all the way!
# Gyro frame is unclear as of yet. Will it contain all three axis, and what do we extract? If this becomes too tricky: build a class to contain the gyro data.
# Right now your limits are hardcoded. Maybe generate a table of library containing the limits set. That way you can tweak


