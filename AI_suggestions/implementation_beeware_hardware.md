# Project: Fall Detection & Emergency Response System

## 1. System Architecture
The project is split into two distinct parts to ensure reliability and bypass platform restrictions (like the Apple "Mac requirement").

### Part A: The Edge Device (The Detector)
- **Hardware:** iPhone (via BeeWare/Kivy) or ESP32/Arduino with Accelerometer.
- **Role:** Monitors Gyroscope and Accelerometer data.
- **Logic:** Runs a Fall Detection Algorithm. If a fall is detected and not cancelled, it sends an HTTP POST request to the Central Server.
- **Connectivity:** Wi-Fi (Home) or 5G/LTE (via Phone Hotspot or dedicated Cellular Module).

### Part B: The Central Server (The Dispatcher)
- **Technology:** Python with FastAPI or Flask.
- **Role:** An "Always-On" listener. When it receives a signal from the Edge Device, it triggers the emergency workflow.
- **Services:**
    - **Twilio API:** For sending automated SMS and Voice Calls.
    - **SendGrid API:** For sending backup emergency emails.
- **Hosting:** 
    - **Development:** Local machine with `ngrok` for tunneling.
    - **Production:** A VPS (DigitalOcean/AWS) or a Raspberry Pi.

## 2. Technical Hurdles & Solutions
- **The "Apple Wall":** Native iOS development requires a Mac. By offloading the "Action" (calling/texting) to a Central Server, the phone app only needs to send a simple web request, which is much easier to code across platforms.
- **Background Execution:** iOS limits background tasks. Using a dedicated hardware device (Arduino/ESP32) avoids "app sleep" issues entirely.
- **Stable Environment:** Avoid using experimental Python versions (like 3.14). Stick to **Python 3.12** for maximum compatibility with BeeWare, Kivy, and FastAPI.

## 3. Development Phases
1. **Phase 1: Logic.** Refine the Python math for identifying a "fall" versus "sitting down quickly."
2. **Phase 2: The Server.** Build a FastAPI app that can successfully send a text message via Twilio when a specific URL is hit.
3. **Phase 3: The Bridge.** Connect the Edge Device to the Server so that a physical button press (simulating a fall) triggers the text message.
4. **Phase 4: Field Testing.** Test the 5G connectivity and GPS coordinate transmission.

# Boots rewrote with some more requests:
# Project Blueprint: Python-Powered Fall Detector & Emergency Bridge

## 1. System Architecture
This project uses a "Client-Server" model to bypass mobile OS restrictions and ensure the emergency alert is handled by a reliable, always-on back-end.

### Part A: The Edge Device (The Detector)
- **Hardware:** ESP32 Microcontroller (Chosen for MicroPython support & built-in Wi-Fi).
- **Sensors:** 
    - **MPU-6050:** Accelerometer/Gyroscope for fall detection.
    - **NEO-6M:** GPS module for location tracking.
- **Language:** MicroPython (Python 3 for microcontrollers).
- **Role:** Monitors motion 24/7. Upon detecting a fall, it captures GPS coordinates and sends an HTTP POST request to the Central Server.

### Part B: The Central Server (The Dispatcher)
- **Technology:** Python with FastAPI.
- **Role:** Listens for alerts from the ESP32.
- **Services:** Uses **Twilio API** to send SMS or automated voice calls to emergency contacts.
- **Hosting:** 
    - **Dev:** Local Nobara machine with `ngrok` tunnel.
    - **Prod:** A VPS (DigitalOcean/AWS) or a 24/7 Raspberry Pi.

---

## 2. Hardware Learning & Assembly
Building the physical device requires moving from a "simulation" to a "portable" build.

### Phase 1: Virtual Prototyping
- **Tool:** [Wokwi.com](https://wokwi.com)
- **Goal:** Simulate an ESP32 wired to an MPU-6050. Write MicroPython code in the browser to test the logic before buying parts.

### Phase 2: Physical Prototyping (The Breadboard)
- **Required Gear:** ESP32 DevKit, Breadboard, Jumper Wires.
- **Wiring Protocols:**
    - **I2C (for MPU-6050):** Connect SDA/SCL pins. 
    - **UART (for GPS):** Connect TX (GPS) to RX (ESP32) and RX (GPS) to TX (ESP32).
- **Learning Resource:** Search **"Random Nerd Tutorials ESP32 MicroPython I2C"** for step-by-step wiring diagrams.

### Phase 3: Power & Portability
- **Battery:** 3.7V LiPo battery with a TP4056 charging module.
- **Outdoor Connectivity:** 
    - **Option 1:** Smartphone Hotspot (ESP32 connects via Wi-Fi).
    - **Option 2:** SIM7600 4G Module (Allows direct 5G/LTE connection).

---

## 3. Software Development Roadmap
1. **Stable Environment:** Use **Python 3.12** on the local machine. Avoid experimental versions (3.14+).
2. **Fall Algorithm:** Logic should detect "Freefall" (~0g) followed by "High Impact" (>3g) and then "Lack of Movement."
3. **The Dispatcher:** Create a FastAPI endpoint `/alert` that triggers a Twilio SMS.
4. **The Flash:** Use **Thonny IDE** to flash MicroPython onto the ESP32 and upload `main.py`.

---

## 4. Key Resources
- **MicroPython Docs:** [docs.micropython.org](https://docs.micropython.org)
- **Component Basics:** YouTube search: **"GreatScott! Electronic Basics"** (specifically for Accelerometers and LiPo batteries).
- **Soldering:** **"Adafruit Guide to Excellent Soldering"** (needed for the final wearable version).