# Fall detection clip-on for watch/bracelet
## Why not an existing wearable or phone?
    I am building this for my father-in-law. He likes his watch. It's a nice analogue one that he's had for a long time. He doesn't want a smartwatch, that's not his style. I imagine more people will feel this way. Many people of his generation are fit people who built an entire life for themselves. But age has brought some issues with mobility and recovery from falls. Understandably however, younger people telling them that they need help or an unappealing piece of hardware can be patronizing and undignified. This clip-on is mostly invisible and allows them to alert their loved ones without changing their lifestyle.

## This is a boot.dev personal project
    I am currently figuring out if I can actually do this. But in essence it is a clip-on for any watch or bracelet that uses gyroscope and accelerometer data to determine if a fall has occured using a 6-phase detection scheme (Tseng, Huang & Kau, 2025). When a fall is detected it will start a timer of X seconds/minutes for the wearer to respond on their phone app (options: "I'm fine", "Tell [emergency contact]", or "Help!"). If no response is given in time it will default to "Tell [emergency contact]". After another x seconds/minutes it will default to "Help!" unless the emergency contact has cancelled the alarm on their app. In all non-safe cases the app will collect and send gps. "Help!" will use the phone to call emergency services [SET FOR YOUR REGION!]" and "Tell [emergency contact]" too which it will add that "Help!" was triggered. 

### Clip on fall detection sensor
    1. 5-phase identification based on accelerometer and gyroscope: Tseng, Huang and Kau 2025
    2. Gyroscope and accelerometer + transmitter (testing via arduino)
    3. Phone app/webapp to inform emergency contact / call emergency services

### Sources
- Tseng, C.-K.; Huang, S.-J.; Kau, L.-J. Wearable Fall Detection System with Real-Time Localization and Notification Capabilities. *Sensors* **2025**, 25, 3632. https://doi.org/10.3390/s25123632
- GitHub: stm32duino - LSM6DSO. https://github.com/stm32duino/LSM6DSO. Consulted on 11/05/2026 (EU date style).
