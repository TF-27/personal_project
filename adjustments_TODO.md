# Adjustments to implement

## calculate_variables.py
1. ~~Make a function to convert accelerometer and gyro data. So you only need to call one svm function (and can ignore it if the actual function uses the correct units)~~
2. ~~Generate the 3-coordinate dictionaries as a function call executable by the object (see fall_detection.py 2.)~~
3. ~~Generate Asvm and Gsvm as a function call executable by the object (see fall_detection.py 2.)~~
    a. ~~2 and 3 will make it easier for each phase to call on properties of the object~~


## fall_detection.py
1. ~~detect_fall() should create a class instance with all the variables in it (not generated for each function)~~
2. ~~Remove return structure and variable adjustment in phase calls~~
3. ~~Make detect_fall() call the phases one by one.~~ On a hit call alarm function, on a miss log the object to a log.

## main.py
1. Make a log objects going past phase one (fall_detect.py 3.) If too much data. 

## GIT
1. ~~Generate a separate branch for the restructuring of fall_detection.py (and associated calculate_variables.py) AFTER finishing the full phase call tree.~~


## Suggestions / Plan for app
1. Boots suggested either Kivy or BeeWare to implement the app
2. Implement NumPy if you're storing datalogs. Works kinda like C