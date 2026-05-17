from calculate_variables import calculate_Asvm, calculate_Gsvm
#class FallFrame(timestamp):
#    __init__(self): #check syntax!
#    self.alarm = False
#    self.acc = #collect acceleration data
#    self.gyro = #collect gyro data
#    self.last_phase_checked = 0

#    return self

class PotentialFall:
    def __init__(self, accelerometer_data, gyro_data, time):
        self.acc_x = accelerometer_data.Ax[time]
        self.acc_y = accelerometer_data.Ay[time]
        self.acc_z = accelerometer_data.Az[time]
        self.time = time
        self.asvm = calculate_Asvm(self.acc_x, self.acc_y, self.acc_z)
        self.last_phase = 0

        self.acc_frame = None #self.generate_test_frame(accelerometer_data, self.time)
        self.gyro_frame = None #self.generate_test_frame(gyro_data, self.time)
        self.asvm_list = None
        self.gsvm_list = None

    def generate_test_frame(self, data_set, time, data_type):
        if data_type == "acc":
            test_frame = {
                't': data_set.t[time:time+199].tolist(),
                'x': data_set.Ax[time:time+199].tolist(),
                'y': data_set.Ay[time:time+199].tolist(),
                'z': data_set.Az[time:time+199].tolist(),
            }
        if data_type == "gyro":
            test_frame = {
                't': data_set.t[time:time+199].tolist(),
                'x': data_set.Wx[time:time+199].tolist(),
                'y': data_set.Wy[time:time+199].tolist(),
                'z': data_set.Wz[time:time+199].tolist(),
            }
        return test_frame

    def calculate_asvm_list(self):
        asvm_list = []
        for coord in range(0,len(self.acc_frame['t'])):
            asvm_list.append(calculate_Asvm(self.acc_frame['x'][coord], self.acc_frame['y'][coord], self.acc_frame['z'][coord]))
        return asvm_list

    def calculate_gsvm_list(self):
        gsvm_list = []
        for coord in range(0,len(self.gyro_frame['t'])):
            gsvm_list.append(calculate_Gsvm(self.gyro_frame['x'][coord], self.gyro_frame['y'][coord], self.gyro_frame['z'][coord]))
        return gsvm_list            
