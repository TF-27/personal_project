import pandas

def get_data(sensor):
    if sensor == "acc":
        return pandas.read_csv('/home/jeroen/workspace/bootdotdev/curriculum/personal_project/test_data/acceleration_testdata.csv', header=0)
    if sensor == "gyro":
        return pandas.read_csv('/home/jeroen/workspace/bootdotdev/curriculum/personal_project/test_data/acceleration_testdata.csv', header=0)
