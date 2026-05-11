import numpy
import math
from calculate_variables import get_Asvm, calculate_deviation, calculate_mean_psi_abs

def detect_fall():

    if phase_one(accelerometer_data):
        return True
    return False # I considered removing this True/False feedback loop, but I think it might be good to keep it. To log and detect false positives/negatives. SO IMPLEMENT A "FALSE-LOG" IN MAIN!

# may have to redesign depending on how continuous data is fed. For example, could only return true/fals for phase one and then generate a dataset of 200 points to feed to phase 2 etc. Good way to also log the frames in alert and no alert

def phase_one(accelerometer_cont, gyro_cont, time):
    # data -> x/y/z
    
    if get_Asvm(x,y,z) < 800:     # Set limit as var? (i.e. create a dictionary)
        acc_frame = {
            time: #accelerometer_cont[time:time+199],
            x: # same frames,
            y: # same frames,
            z: # same frames,
        }

        gyro_frame = {
            time: #gyro_cont[time:time+199]
            x: # same frames,
            y: # same frames,
            z: # same frames,
        }

        if phase_two(acc_frame, gyro_frame): #seriously considering changing this to make detect_fall() call all the phases.
            return True
    return False


def phase_two(acc_frame, gyro_frame):
    
    for datapoint in acc_frame:
        if get_Asvm(datapoint) > 1400:        # Set limit as var?
            if phase_three(acc_frame, gyro_frame):
                return True
    return False


def phase_three(acc_frame, gyro_frame):
    dev_sample_acc = acc_frame[150:]

    if calculate_deviation(dev_sample_acc) < 100: # Set limit as var?
        if phase_four(gyro_frame):
            return True
    return False


def phase_four(gyro_frame):
    dev_sample_gyro = gyro_frame[150:]
    
    if calculate_deviation(dev_sample_gyro) < 10: # Set limit as var?
        if phase_five(gyro_frame):
            return True
    return False

def phase_five(gyro_frame):
    dev_sample_psi = gyro_frame[180:]

    if calculate_mean_psi_abs(dev_sample_psi) < 60:
        phase(six)
        return True
    return False

def phase_6():
    #function_to_log gps
    #function_to_alarm_wearer + countdown clock
    #function to alarm emergency contact at clock == 00:00
    #function to call emergency services if emergency contact doesn't answer?
    #Either return to phase 1/detect fall or have main always calling phase 1/detect fall

# Or do we generate an instance of a class? Containing the accelerometer and gyro data of that frame? That way we don't have to push down the data all the way!
# Gyro frame is unclear as of yet. Will it contain all three axis, and what do we extract? If this becomes too tricky: build a class to contain the gyro data.
# Right now your limits are hardcoded. Maybe generate a table of library containing the limits set. That way you can tweak


