# VintagePioneerIR
Smart Remote for Vintage Pioneer Amps
 
 
### Bring your classic audio gear into the smart home era with EspHome

 

Many vintage Pioneer amplifiers have lost their original remote controls — but they still deserve modern convenience. VintagePioneerIR is an ESP32-based smart remote replacement that integrates seamlessly with Home Assistant using ESPHome. Control your beloved Pioneer amp (and many others) directly from your smart home setup.
***

## ✨ Features

- Fully replaces lost or broken Pioneer remote controls
- Connects seamlessly with Home Assistant through Wi-Fi
- Easy customization using the included **Python configuration tool**
- Add support for other amplifier brands or new functions with minimal coding
- Open source and completely free to use

***

## 🛠 Hardware Requirements

- ESP32 development board
- IR LED and suitable resistor
- 5V USB power source
- (Optional) IR receiver module for learning custom codes

***

## ⚙️ Installation

1. Flash the provided ESPHome-firmware to your ESP32 (instructions in `/firmware` folder).
2. Connect the IR LED to the appropriate GPIO pins (see wiring diagram).
3. Configure your Wi-Fi and Home Assistant integration.
4. Restart your ESP32 — it will appear as a new device in Home Assistant.

***

## 💻 Customize With Python

A ready-to-use Python script is provided (`prontocode2yaml.py`) for creating new commands or supporting additional brands.

- Define new button codes easily
- Extend functionality for other amplifiers
- No deep coding knowledge required
- example of pronto IR codes : (https://www.remotecentral.com/cgi-bin/codes/pioneer/vs-x305_reciever/page-1/)

***

## ❤️ Support the Project

You’re free to use, modify, and share this code — no strings attached.
If you enjoy this project or find it useful, please leave a **positive reply in the Home Assistant forum**. It helps others discover the project and keeps the community growing.

***

## 📜 License

This project is released under the **MIT License**.

***

Would you like me to make the README sound more technical (for developers) or more accessible (for vintage audio enthusiasts)?

