import pandas
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

acc_path = BASE_DIR / "resources" / "acceleration_testdata.csv"
gyro_path = BASE_DIR / "resources" / "gyroscope_testdata.csv"

def get_data(sensor):
    if sensor == "acc":
        return pandas.read_csv(acc_path, header=0)
    if sensor == "gyro":
        return pandas.read_csv(gyro_path, header=0)
