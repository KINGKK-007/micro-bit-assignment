![Micro:bit](https://img.shields.io/badge/Device-Micro:bit%20v2-blue) ![Python](https://img.shields.io/badge/Language-Python3-green)

# JioSaavn Music Controller

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup](#setup)
  - [Micro:bit Firmware](#microbit-firmware)
  - [PC Controller](#pc-controller)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Explanation](#code-explanation)
- [Demonstration](#demonstration)
- [Side Projects](#side-projects)
- [Future Improvements](#future-improvements)
- [Team Members](#team-members)
- [License](#license)

---

## Overview

This repository contains a Micro:bit v2–based controller for the [JioSaavn](https://www.jiosaavn.com) web music player. The Micro:bit reads button presses and gestures, sends commands over USB serial to a Python/Selenium script on your PC, and automates playback controls (play/pause, next/previous track, volume up/down) on JioSaavn’s Chrome web interface.

Additionally, three side projects are included:
1. **Chrome Dino Game** – Play the offline dinosaur game using Micro:bit button controls.
2. **Digital Compass** – Real-time compass using the Micro:bit’s magnetometer and LED display.
3. **Memory Game** – A Simon-says style memory game on the Micro:bit LED matrix.

---

## Features

- **Play/Pause** via shake gesture
- **Next Track** (press B)
- **Previous Track** (press A)
- **Restart Track** (single press A)
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
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
