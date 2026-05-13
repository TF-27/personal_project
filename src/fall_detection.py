import numpy
import math
from calculate_variables import calculate_Asvm, calculate_deviation #calculate_mean_psi_abs
from csv_tests import get_data
import random


## NEW IDEAS:
# Detection is a call in main(). Calls get_gyro() and get_acc() every 1/100 s (2/200 right?). Then builds an instance of a class 'fall', which then starts collecting the 199 samples after that and storing it. 
# That class can then have properties like which phases were checked as well-> export to store on hd for analyses.
# Finally the class will have an alert status set to false/true. At check 6 if it's true -> raise alarm.

def detect_fall():
    accelerometer_data = get_data("acc")
    if phase_one(accelerometer_data, None, random.randrange(0,1652)):
        return True
    return False # I considered removing this True/False feedback loop, but I think it might be good to keep it. To log and detect false positives/negatives. SO IMPLEMENT A "FALSE-LOG" IN MAIN!

# may have to redesign depending on how continuous data is fed. For example, could only return true/fals for phase one and then generate a dataset of 200 points to feed to phase 2 etc. Good way to also log the frames in alert and no alert

def phase_one(accelerometer_cont, gyro_cont, time):
    Axv = accelerometer_cont.Ax[time]
    Ayv = accelerometer_cont.Ay[time]
    Azv = accelerometer_cont.Az[time]

    if calculate_Asvm(Axv, Ayv, Azv) < 800:     # Set limit as var? (i.e. create a dictionary)
        #print(f"Asvm is {calculate_Asvm(Axv, Ayv, Azv)}")
        #print(f"\nAxv: {Axv}\nAy: {Ayv}\nAzv: {Azv}\n\naccelerometer_cont: {accelerometer_cont}\n\naccelerometer_cont.Ax[10]: {accelerometer_cont.Ax[10]}")
        acc_frame = {
            't': accelerometer_cont.t[0:199].tolist(),
            'x': accelerometer_cont.Ax[0:199].tolist(),
            'y': accelerometer_cont.Ay[0:199].tolist(),
            'z': accelerometer_cont.Az[0:199].tolist(),
        }

#        gyro_frame = {
#            time: #gyro_cont[time:time+199]
#            x: # same frames,
#            y: # same frames,
#            z: # same frames,
#        }
        print("\nPhase 1 positive\n")
        if phase_two(acc_frame, None): #seriously considering changing this to make detect_fall() call all the phases.
            return True
    return False


def phase_two(acc_frame, gyro_frame):
    Asvm_list = []
    for coord in range(0,len(acc_frame['t'])):
        Asvm_list.append(calculate_Asvm(acc_frame['x'][coord], acc_frame['y'][coord], acc_frame['z'][coord]))
    for asvm in Asvm_list:
        if asvm > 1400: #NO HITS IN TEST DATA, ADJUST TEST DATA TO HAVE SOME FALLS! (MAY BE THE SAMPLING, SINCE IT'S NOT EVERY 1/100 SECOND)
            print("Phase 2 positive\n")
            if phase_three(Asvm_list, gyro_frame):
                return True
    return False


def phase_three(asvm_list, gyro_frame):
    dev_sample_acc = asvm_list[150:]

    if calculate_deviation(dev_sample_acc) < 100: # Set limit as var?
        print("Phase 3 positive\n")
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
    pass
    #function_to_log gps
    #function_to_alarm_wearer + countdown clock
    #function to alarm emergency contact at clock == 00:00
    #function to call emergency services if emergency contact doesn't answer?
    #Either return to phase 1/detect fall or have main always calling phase 1/detect fall

# Or do we generate an instance of a class? Containing the accelerometer and gyro data of that frame? That way we don't have to push down the data all the way!
# Gyro frame is unclear as of yet. Will it contain all three axis, and what do we extract? If this becomes too tricky: build a class to contain the gyro data.
# Right now your limits are hardcoded. Maybe generate a table of library containing the limits set. That way you can tweak


