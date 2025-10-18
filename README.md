# VintagePioneerIR
Smart Remote for Vintage Pioneer Amps
 
 
### Bring your classic audio gear into the smart home era

Many vintage Pioneer amplifiers have lost their original remote controls over time — but they still deserve modern convenience. This project offers a **smart ESP32-based replacement** that allows you to control your beloved Pioneer amp directly from **Home Assistant** or **any smart home platform**.

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

1. Flash the provided firmware to your ESP32 (instructions in `/firmware` folder).
2. Connect the IR LED to the appropriate GPIO pins (see wiring diagram).
3. Configure your Wi-Fi and Home Assistant integration in the `config.yaml` file.
4. Restart your ESP32 — it will appear as a new device in Home Assistant.

***

## 💻 Customize With Python

A ready-to-use Python script is provided (`prontocode2yaml.py`) for creating new commands or supporting additional brands.

- Define new button codes easily
- Extend functionality for other amplifiers
- No deep coding knowledge required

***

## ❤️ Support the Project

You’re free to use, modify, and share this code — no strings attached.
If you enjoy this project or find it useful, please leave a **positive reply in the Home Assistant forum**. It helps others discover the project and keeps the community growing.

***

## 📜 License

This project is released under the **MIT License**.

***

Would you like me to make the README sound more technical (for developers) or more accessible (for vintage audio enthusiasts)?

