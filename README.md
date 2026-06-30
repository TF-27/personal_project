# Fall detection clip-on for watch/bracelet
## Why not an existing wearable or phone?
    I am building this for my father-in-law. He likes his watch. It's a nice analogue one that he's had for a long time. He doesn't want a smartwatch, that's not his style. WWhich I imagine is a feeling shared by a lot of people, including myself. Many people of his generation are fit people who built an entire life for themselves. But age has brought some issues with mobility and recovery from falls. Understandably however, younger people telling them that they need help or an unappealing piece of hardware can be patronizing and undignified. This clip-on is mostly invisible and allows them to alert their loved ones without changing their lifestyle.

## This is a boot.dev personal project
    I am currently figuring out if I can actually do this. The design idea (current state below): in essence it is a clip-on for any watch or bracelet that uses gyroscope and accelerometer data** to determine if a fall has occured using a 6-phase detection scheme (Tseng, Huang & Kau, 2025). When a fall is detected it will start a timer of X seconds/minutes for the wearer to respond on their phone app (options: "Call 112!", "Message [emergency contact]", or "No help needed - I'm safe!"). If no response is given in time it will default to "Tell [emergency contact]". After another x seconds/minutes it will default to "Call 112!" unless the emergency contact has cancelled the alarm on their app. In all non-safe cases the app will collect and send gps data. "Call 112!" will use the phone to call emergency services (SET FOR YOUR REGION!)" and "Message [emergency contact]", to which it will add that "Call 112!" was triggered. 

### Main elements
    1. 5-phase identification based on accelerometer and gyroscope (Tseng, Huang & Kau, 2025) NOTE: they call it 6-phase, but phase 6 is raising the alarm. So I sometimes call it 5-phase when talking about the detection part.
    2. Gyroscope and accelerometer + transmitter (testing via arduino)
    3. Phone app/webapp to inform emergency contact / call emergency services

### Sources
- Tseng, C.-K.; Huang, S.-J.; Kau, L.-J. Wearable Fall Detection System with Real-Time Localization and Notification Capabilities. *Sensors* **2025**, 25, 3632. https://doi.org/10.3390/s25123632
- GitHub: stm32duino - LSM6DSO. https://github.com/stm32duino/LSM6DSO. Consulted on 11/05/2026 (EU date style).


## Current state of the app
- It can run a csv file embedded in the app. That's two sensor sets combined in which a few falls a detected. 
- It has a settings menu for the emergency contact
- It has pop-ups telling the user it does the actions described above, but does not actually do these things yet.

### What's next?
For my capstone project on Boot.dev I want to add:
- Access to phone sensor data (gyroscope, accelerometer and gps)
- Send an SMS
- Call 112

This will in essence make this a phone app to detect falls. The paper on 6-phase detection describes a belt/pocket position should suffice. But that heavily relies on the phone actually being in the person's pocket.

The third step for me will be to learn electronics and add to the system:
- Access to bluetooth to read remote sensors (gyroscope and accelerometer)
- A chip with those sensors that can clip to a watch