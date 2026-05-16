import numpy
import math
from calculate_variables import calculate_Asvm, calculate_deviation, calculate_mean_psi_abs
from csv_tests import get_data
import random #remove in final code! Is for testing at random only!
import sys


## NEW IDEAS:
# Detection is a call in main(). Calls get_gyro() and get_acc() every 1/100 s (2/200 right?). Then builds an instance of a class 'fall', which then starts collecting the 199 samples after that and storing it. 
# That class can then have properties like which phases were checked as well-> export to store on hd for analyses.
# Finally the class will have an alert status set to false/true. At check 6 if it's true -> raise alarm.


#NumPy may be usefull for storing data. It works more like C! 
#Boots suggestions for going to a phone: Kivy or BeeWare

class PotentialFall:
    def __init__(self, accelerometer_data, gyro_data, time):
        self.acc_x = accelerometer_data.Ax[time]
        self.acc_y = accelerometer_data.Ay[time]
        self.acc_z = accelerometer_data.Az[time]
        self.time = time
        self.asvm = calculate_Asvm(self.acc_x, self.acc_y, self.acc_z)

        self.acc_frame = None #self.generate_test_frame(accelerometer_data, self.time)
        self.gyro_frame = None #self.generate_test_frame(gyro_data, self.time)
        self.asvm_list = None

    def generate_test_frame(self, data_set, time):
        test_frame = {
            't': data_set.t[time:time+199].tolist(),
            'x': data_set.Ax[time:time+199].tolist(),
            'y': data_set.Ay[time:time+199].tolist(),
            'z': data_set.Az[time:time+199].tolist(),
        }
        return test_frame

    def calculate_asvm_list(self): #WRONG!!! NO NEED ANYMORE, ONLY FOR SUBSET!
        asvm_list = []
        for coord in range(0,len(self.acc_frame['t'])):
            asvm_list.append(calculate_Asvm(self.acc_frame['x'][coord], self.acc_frame['y'][coord], self.acc_frame['z'][coord]))
        return asvm_list      




def detect_fall_test2():
    accelerometer_data = get_data("acc")
    gyro_data = get_data("gyro")
    test_next = False

    for time in range(0,len(accelerometer_data.t)-200):
        test_object = PotentialFall(accelerometer_data, gyro_data, time)

        #Phase 1
        print("\n###########################################\n")
        if phase_one_test2(test_object):
            print("Phase one positive")
            test_next = True
        else:
            print("Phase one negative")
            test_next = False
            # not logging, too much data. Logging past phase 2

        while test_next:
            #Phase 2
            if phase_two_test2(test_object, accelerometer_data): #will have to adapt when going with the live feed
                print("Phase two positve")
            else:
                print("Phase two negative")
                test_next = False
                continue

            #Phase 3
            if phase_three_test2(test_object):
                print("Phase three positive")
            else:
                print("Phase three negative")
                test_next = False
                continue

            #Phase 4
            if phase_four_test2(test_object, gyro_data):
                print("Phase four positive")
                return f"\nTest object size: {sys.getsizeof(test_object)}\ntime: {test_object.time}\n\nasvm_list:\n{test_object.asvm_list}\n\nacc_frame:\nX\n{test_object.acc_frame['x']}\nY\n{test_object.acc_frame['y']}\nZ\n{test_object.acc_frame['z']}"
            else:
                test_next = False
                continue

            
            print("\n###########################################\n")
            
    
    return test_object






def phase_one_test2(test_object):
    if calculate_Asvm(test_object.acc_x, test_object.acc_y, test_object.acc_z) < 800: #CHANGE TO SET VARIABLE FORM LIST (MAIN BRANCH)
        return True
    return False

def phase_two_test2(test_object, accelerometer_data):
    test_object.acc_frame = test_object.generate_test_frame(accelerometer_data, test_object.time)
    test_object.asvm_list = test_object.calculate_asvm_list()
    for asvm in test_object.asvm_list:
        if asvm > 1400: #import test limit from main branch
            return True
    return False

def phase_three_test2(test_object):
    deviation_sample_acc = calculate_deviation(test_object.asvm_list[150:])
    if deviation_sample_acc < 100:
        return True
    return False

def phase_four_test2(test_object, gyro_data):
    return True












def detect_fall():
    accelerometer_data = get_data("acc")
    gyro_data = get_data("gyro")
    for time in range(0,len(accelerometer_data.t)):
        if phase_one(accelerometer_data, gyro_data, time):
            return True
    return False # I considered removing this True/False feedback loop, but I think it might be good to keep it. To log and detect false positives/negatives. SO IMPLEMENT A "FALSE-LOG" IN MAIN!

# may have to redesign depending on how continuous data is fed. For example, could only return true/fals for phase one and then generate a dataset of 200 points to feed to phase 2 etc. Good way to also log the frames in alert and no alert






def phase_one(accelerometer_data, gyro_data, time):
    print("\n\n==========================================================\n\n")
    Axv = accelerometer_data.Ax[time]
    Ayv = accelerometer_data.Ay[time]
    Azv = accelerometer_data.Az[time]

    print(f"\nTime index: {time}")
    print(f"Axv at time {time}: {Axv}")
    print(f"Ayv at time {time}: {Ayv}")
    print(f"Azv at time {time}: {Azv}")

    print(f"Asvm for {time}: {calculate_Asvm(Axv, Ayv, Azv)}")
    if calculate_Asvm(Axv, Ayv, Azv) < 800:     # Set limit as var? (i.e. create a dictionary)
        #print(f"Asvm is {calculate_Asvm(Axv, Ayv, Azv)}")
        #print(f"\nAxv: {Axv}\nAy: {Ayv}\nAzv: {Azv}\n\naccelerometer_cont: {accelerometer_cont}\n\naccelerometer_cont.Ax[10]: {accelerometer_cont.Ax[10]}")
        acc_frame = {
            't': accelerometer_data.t[time:time+199].tolist(),
            'x': accelerometer_data.Ax[time:time+199].tolist(),
            'y': accelerometer_data.Ay[time:time+199].tolist(),
            'z': accelerometer_data.Az[time:time+199].tolist(),
        }

        print(f"\nacc_frame['x'] (first 5 values): {acc_frame['x'][:5]}")
        print(f"acc_frame['x'] (last 5 values): {acc_frame['x'][-5:]}")
        print(f"acc_frame['y'] (first 5 values): {acc_frame['y'][:5]}")
        print(f"acc_frame['y'] (last 5 values): {acc_frame['y'][-5:]}")
        print(f"acc_frame['z'] (first 5 values): {acc_frame['z'][:5]}")
        print(f"acc_frame['z'] (last 5 values): {acc_frame['z'][-5:]}")

        gyro_frame = {
            't': gyro_data.t[time:time+199].tolist(),
            'x': gyro_data.Wx[time:time+199].tolist(),
            'y': gyro_data.Wy[time:time+199].tolist(),
            'z': gyro_data.Wz[time:time+199].tolist(),
        }

        print("\nPhase 1 positive\n")
        if phase_two(acc_frame, gyro_frame): #seriously considering changing this to make detect_fall() call all the phases.
            return True
    return False


def phase_two(acc_frame, gyro_frame):
    Asvm_list = []
    for coord in range(0,len(acc_frame['t'])):
        Asvm_list.append(calculate_Asvm(acc_frame['x'][coord], acc_frame['y'][coord], acc_frame['z'][coord]))
    asvm_hit = False
    for asvm in Asvm_list:
        if asvm > 1400: #NO HITS IN TEST DATA, ADJUST TEST DATA TO HAVE SOME FALLS! (MAY BE THE SAMPLING, SINCE IT'S NOT EVERY 1/100 SECONDs). Current data set goes fully to phase 6 if set to 1039 or lower. should be 1400 in real run
            print("Phase 2 positive\n")
            print(f"asvm in phase two: {asvm}")
            asvm_hit = True
            break
    if asvm_hit:
        if phase_three(Asvm_list, gyro_frame): #this is where we keep feeding the same list in each loop! Is that an issue? I think it's supposed to happen like this. Which means we could stop the loop after one positive.
            return True
    return False

def phase_three(asvm_list, gyro_frame):
    dev_sample_acc = asvm_list[150:]
#    print(f"dev_sample_acc: {dev_sample_acc}")
    print(f"Asvm deviation: {calculate_deviation(dev_sample_acc)}")
    if calculate_deviation(dev_sample_acc) < 100: # Set limit as var?
        print("Phase 3 positive\n")

        if phase_four(gyro_frame):
            return True
    return False


def phase_four(gyro_frame):
    gsvm_list = []
    for coord in range(0,len(gyro_frame['t'])):
        gsvm_list.append(calculate_Asvm(gyro_frame['x'][coord], gyro_frame['y'][coord], gyro_frame['z'][coord]))
    
    dev_sample_gyro = gsvm_list[150:]
    print(f"Gsvm deviation: {calculate_deviation(dev_sample_gyro)}")
    if calculate_deviation(dev_sample_gyro) < 10: # SET BACK TO ORIGINAL: 10!
        print("Phase 5 Positive\n")
        if phase_five(gyro_frame):
            return True
    return False

def phase_five(gyro_frame):
    gyro_frame_psi = {
        't': gyro_frame['t'][180:],
        'x': gyro_frame['x'][180:],
        'y': gyro_frame['y'][180:],
        'z': gyro_frame['z'][180:],
    }
#    print(f"gyro_frame: {gyro_frame_psi}")
    print(f"dev_sample_psi: {calculate_mean_psi_abs(gyro_frame_psi)}")
    if calculate_mean_psi_abs(gyro_frame_psi) < 60:
        print("Phase 6 positive")
        phase_6()
        return True
    return False

def phase_6():
    print("All checks positive, raising the alarm\nSending GPS")
    #function_to_log gps
    #function_to_alarm_wearer + countdown clock
    #function to alarm emergency contact at clock == 00:00
    #function to call emergency services if emergency contact doesn't answer?
    #Either return to phase 1/detect fall or have main always calling phase 1/detect fall

# Or do we generate an instance of a class? Containing the accelerometer and gyro data of that frame? That way we don't have to push down the data all the way!
# Gyro frame is unclear as of yet. Will it contain all three axis, and what do we extract? If this becomes too tricky: build a class to contain the gyro data.
# Right now your limits are hardcoded. Maybe generate a table of library containing the limits set. That way you can tweak


