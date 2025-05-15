![Micro:bit](https://img.shields.io/badge/Device-Micro:bit%20v2-blue) ![Python](https://img.shields.io/badge/Language-Python3-green)

# Micro:Bit Assignment {Computer Architecture/EGC 121}

## Table of Contents
- [Overview](#overview)
- [Features](#features-of-jiosaavn-music-controller)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup](#setup)
  - [Micro:bit Firmware](#microbit-firmware)
  - [PC Controller](#pc-controller)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Explanation](#code-explanation)
- [Demonstration Videos](#demonstration-videos)
- [Side Projects](#side-projects)
- [Future Improvements](#future-improvements-in-jiosaavn-music-controller)
- [Team Members](#team-members)

---

## Overview

This repository contains a Micro:bit v2–based controller for the [JioSaavn](https://www.jiosaavn.com) web music player. The Micro:bit reads button presses and gestures, sends commands over USB serial to a Python/Selenium script on your PC, and automates playback controls (play/pause, next/previous track, volume up/down) on JioSaavn’s Chrome web interface.

Project Report : [JioSaavnMusicController_Report.pdf](https://drive.google.com/file/d/1JNTrQSUfPg2VnSIRVZ11Q-pMMHzhOtIT/view?usp=share_link)

Additionally, three side projects are included:
1. **Chrome Dino Game** – Play the offline dinosaur game using Micro:bit button controls.
2. **Digital Compass** – Real-time compass using the Micro:bit’s magnetometer and LED display.
3. **Memory Game** – A Simon-says style memory game on the Micro:bit LED matrix.

---

## Features of JioSaavn Music Controller

- **Play/Pause** via shake gesture
- **Restart Track** (press A)
- **Next Track** (press B)
- **Previous Track** (press A just after restarting) 
- **Volume Up** (double-press B)
- **Volume Down** (double-press A)
- LED feedback icons for each command
- Python/Selenium bridge for reliable web automation

---

## Hardware Requirements

- BBC Micro:bit v2
- USB Type-A to Micro-USB cable
- PC running Windows/macOS/Linux
- Google Chrome browser

---

## Software Requirements

- Python 3.7+
- [MicroPython firmware](https://microbit-micropython.readthedocs.io/) on Micro:bit
- `selenium` and `pyserial` Python packages
- ChromeDriver executable (compatible with your Chrome version)

---

## Setup

### Micro:bit Firmware

1. Download `microbit.py` from this repository.  
2. Flash it to your Micro:bit v2 using the MicroPython UF2 tool.

### PC Controller

1. Clone this repo:
   ```bash
   git clone https://github.com/<KINGKK-007>/<micro-bit-assignment>.git
   cd <micro-bit-assignment>

2. Install dependencies:
   ```bash
   pip install selenium pyserial
3. Place chromedriver in your PATH or project root.
4. Update the serial port in jiosavan_controller.py (e.g., COM9 or /dev/ttyACM0).

---

## Usage

1. Connect your **Micro:bit** to your PC via USB.

2. Run the controller script:

   ```bash
   python jiosavan_controller.py
3. Open **Chrome** and navigate to [JioSaavn](https://www.jiosaavn.com).
4. Use the Micro:bit controls:
- Shake: Play/Pause.
- Press B: Next track.
- Press A: Previous track or Restart (depends on single vs. double press).
- Double-press B: Volume up.
- Double-press A: Volume down.
- LED icons on the Micro:bit confirm each action.

---

## Project Structure

<pre>├── JioSaavnMusicController/
│ ├── microbit.py                  # Micro:bit MicroPython script 
│ ├── jiosavan.py                  # Selenium automation helper
│ ├── jiosavan_controller.py       # Serial-to-Selenium bridge
│ ├── JioSaavn_Report.pdf          # JioSaavn project report
│ └── DetailedCodeExplanations.pdf # Detailed explanation of main controller code
│
├── SideHustles/
│ ├── chrome_dino.py               # Chrome Dino control script
│ ├── Chrome_Dino.pdf              # Chrome Dino project report
│ ├── compass.py                   # Digital Compass control script
│ ├── Compass.pdf                  # Digital Compass project report
│ ├── memory_game.py               # Memory Game logic script
│ └── Memory_Game.pdf              # Memory Game project report
│
└── README.md                      # This file</pre>

---

## Code Explanation

- [DetailedCodeExplanation.pdf](https://drive.google.com/file/d/1-tRX-3y9bqGs4DAnv0N1B6Pl2MKri8Ud/view?usp=share_link)

- **microbit.py**  
  Detects button events and gestures, sends commands (`PLAY`, `NEXT`, `PREV`, `VOL_UP`, `VOL_DOWN`) over UART.

- **jiosavan_controller.py**  
  Opens serial port (115200 baud), listens for UART commands, and dispatches them to Selenium functions.

- **jiosavan.py**  
  Implements Selenium routines to control playback on JioSaavn (play/pause, skip, volume adjustments).

---

## Demonstration Videos 

Main controller demo:

- [JioSaavn Music Controller Working](https://drive.google.com/file/d/17tipGkDq-_PeUA8daU7xiVDqFFfhpIk-/view?usp=share_link)

Side Projects demo:

- [Memory Game Working](https://drive.google.com/file/d/1PsbJtFaRprxVQib4Qu50ni7nIJhfd5Ud/view?usp=share_link)

- [Chrome Dino Working](https://drive.google.com/file/d/1vZhc-wmto0BQOWm81tPAqW0lz1AOGBVR/view?usp=share_link)

- [Compass Working](https://drive.google.com/file/d/13PJoXrYQ3vEFnqC_ez0mqVcEbzZqfWS9/view?usp=share_link)

---

## Side Projects

| Project         | Description                                            | Project Report                                                                                               |
|-----------------|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Chrome Dino Game | Play Chrome’s offline dinosaur game via Micro:bit buttons. | [Chrome_Dino.pdf](https://drive.google.com/file/d/1GfbnPI2qqRzQFXjczvlgWyWPj0Vj7e_J/view?usp=share_link)           |
| Digital Compass  | Real-time compass using the Micro:bit magnetometer and LEDs. | [Compass.pdf](https://drive.google.com/file/d/1uXZRCnBlLe97KueORwLwOkBkAegXOD_f/view?usp=sharing)           |
| Memory Game     | Simon-says style memory challenge on the Micro:bit LED matrix. | [Memory_Game.pdf](https://drive.google.com/file/d/1CpypCTweukLDyuhZLQkP-RXxjaZ0s1BH/view?usp=sharing)           |

---

## Future Improvements in JioSaavn Music Controller

- **Wireless BLE:** Swap USB serial for Bluetooth LE.
- **Gesture Volume:** Tilt-based continuous volume control.
- **LED Feedback:** Show track titles or volume levels on the LED matrix.

---

## Team Members

| Name          | Roll Number | GitHub                                      | 
|---------------|-------------|---------------------------------------------|
| Ayush Patel   | BT2024054   | [GitHub](https://github.com/ayushpatel)  |
| Kabir Ahuja   | BT2024004   | [Kabir646](https://github.com/Kabir646)        |
| Kanav Kumar   | BT2024021   | [KINGKK-007](https://github.com/KINGKK-007)     |
| Dayal Gupta   | BT2024167   | [DayalGupta03](https://github.com/DayalGupta03)     |
| Parth Malhotra| BT2024197   | [GitHub](https://github.com/parthmalhotra)  |
| Sachin Nain   | BT2024203   | [SachinSNain](https://github.com/SachinSNain)     |
| Tanmay Dixit  | BT2024016   | [tdixit547](https://github.com/tdixit547)    |

---
