# Fall Detection Project: Next Steps and Documentation

This document outlines the technical requirements for transitioning the 6-phase fall detection algorithm from a desktop CSV-based prototype to a mobile background application.

## 1. Background Execution and System Integration
To keep the app running without a visible window, or to handle long-running detection logic without freezing the UI.

* **Toga App Lifecycle:** [https://toga.readthedocs.io/en/latest/reference/api/app.html](https://toga.readthedocs.io/en/latest/reference/api/app.html)
* **Asynchronous Tasks:** Use `self.add_background_task()` to run the detection loop.
* **System Tray:** Explore the `App.icon` and `App.commands` for status bar integration.

## 2. Dynamic Window Management
How to trigger an emergency UI when `detect_fall()` returns a positive result.

* **Toga Window API:** [https://toga.readthedocs.io/en/latest/reference/api/widgets/window.html](https://toga.readthedocs.io/en/latest/reference/api/widgets/window.html)
* **Implementation Concept:** 
    1. Define a function to create a new `toga.Window` instance.
    2. Define a `toga.Box` with `COLUMN` direction.
    3. Add multiple `toga.Button` widgets for "Cancel" and "Emergency".
    4. Call `.show()` on the window object when the algorithm triggers.

## 3. Mobile Hardware Sensor Access (Android/iOS)
Accessing real-time Accelerometer and Gyroscope data requires bridging Python to native mobile APIs.

* **BeeWare Hardware Guide:** [https://beeware.org/project/using/](https://beeware.org/project/using/)
* **Android (Java Bridge):** Accessing `android.hardware.SensorManager` via the Android backend.
* **iOS (Obj-C Bridge):** Accessing `CoreMotion` using `rubicon-objc`.
* **Briefcase Mobile Tutorial:** [https://docs.beeware.org/en/latest/tutorial/tutorial-4.html](https://docs.beeware.org/en/latest/tutorial/tutorial-4.html)

## 4. Current Environment Summary
* **Host:** Nobara Linux
* **Container:** Fedora Docker
* **Dependencies:** Toga, Briefcase, NumPy, Pandas
* **Project Structure:** 
    - `src/fall_detection/app.py` (GUI/Lifecycle)
    - `src/fall_detection/fall_detection.py` (Algorithm Logic)
    - `src/fall_detection/resources/` (CSV Data Sets)