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
4. New way of getting data may be g instead of Ax already. Make sure to correct for that when testing. Also alter to single file input.

## main.py
1. Make a log objects going past phase one (fall_detect.py 3.) If too much data. 

## GIT
1. ~~Generate a separate branch for the restructuring of fall_detection.py (and associated calculate_variables.py) AFTER finishing the full phase call tree.~~

## Next phase
1. Test with new csv data that actually measures some falls!
2. Figure out how to build the app for a phone
    a. later on how to do it with a remote sensor
3. alter data detection from csv to live feed from phone

### Challenges
- BeeWare and Kivy both have issues with my distro. Get help on the packaging command!
- iPhone WILL NOT ALLOW me to install my BeeWare/Kivy code
    - Either use a Mac to do some conversions (figure out) OR employ online services.
    - Alternatives: webapp or arduino with online connection/connection to phone
        - could tunnel through phone if needed
- HARDWARE! :S



## Suggestions / Plan for app
1. Boots suggested either Kivy or BeeWare to implement the app
    - **Before lost in the woods:** BeeWare "Briefcase" documentation/approach
2. Implement NumPy if you're storing datalogs. Works kinda like C


### BeeWare approach

#### Suggested resources (Boots)
- Official tutorial: https://docs.beeware.org/en/latest/tutorial/tutorial-0.html
- Video tutorial search: Codemy.com BeeWare on youtube (John Elder)

- General Python to Mobile:
    - Tech with Tim: Search 'Tech with Tim Python Mobile App'