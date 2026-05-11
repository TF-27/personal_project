import numpy
import math

def detect_fall():
    # Translate sensor feed to array (or do we do this in their own file?)
    # Need to take gyro data ass well and pass it down? -> As array of that timeframe
    if phase_one(accelerometer_continuous):
        return True
    return False # I considered removing this True/False feedback loop, but I think it might be good to keep it. To log and detect false positives/negatives. SO IMPLEMENT A "FALSE-LOG" IN MAIN!


def phase_one(accelerometer_cont, gyro_cont):
    if # Test Asvm < 800mg:     # Set limit as var?
        # select frame for acc AND gyro

        if phase_two(acc_frame, gyro_frame):
            return True
    return False


def phase_two(acc_frame, gyro_frame):
    if # Test Asvm > 1400mg:        # Set limit as var?
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

    if psi_angle(dev_sample_psi) < 60:
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

def calculate_deviation(selected_frame):
    mu = numpy.mean(selected_frame)
    sum_array = []
    for svm in selected_frame:
        sum_array.append((svm-mu)**2)
    deviation = numpy.sum(sum_array) / 50
    deviation = math.sqrt(deviation)
    
    return deviation

def psi_angle(dev_sample_psi):
