import numpy
import math
from .calculate_variables import calculate_deviation, calculate_mean_psi_abs, calculate_Asvm
from .csv_tests import get_data
import random #remove in final code! Is for testing at random only!
import sys
from .fall_object import PotentialFall
from . import variables


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
            return True
            
            print("\n###########################################\n")
    return False



def phase_one(test_object):
    if calculate_Asvm(test_object.acc_x, test_object.acc_y, test_object.acc_z) < variables.Asvm_initial_treshold:
        return True
    return False

def phase_two(test_object, accelerometer_data):
    test_object.acc_frame = test_object.generate_test_frame(accelerometer_data, test_object.time, "acc")
    test_object.asvm_list = test_object.calculate_asvm_list()
    for asvm in test_object.asvm_list:
        if asvm > variables.Asvm_sample_treshold:
            return True
    return False

def phase_three(test_object):
    deviation_sample_acc = calculate_deviation(test_object.asvm_list[150:])
    if deviation_sample_acc < variables.Asvm_deviation_upper:
        return True
    return False

def phase_four(test_object, gyro_data):
    test_object.gyro_frame = test_object.generate_test_frame(gyro_data, test_object.time, "gyro")
    test_object.gsvm_list = test_object.calculate_gsvm_list()
    deviation_sample_gyro = calculate_deviation(test_object.gsvm_list[150:])
    if deviation_sample_gyro < variables.Gsvm_deviation_upper:
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
    if test_object.mean_psi < variables.mean_psi_upper:
        return True
    return False

def phase_six(test_object):
    print("All checks positive, raising the alarm\nSending GPS")
    return test_object.time



