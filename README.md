# Embedded Serial Communication Tool

A Python-based serial communication tool for embedded-system development and debugging.

## Features

* Connect to a microcontroller using UART/USB-Serial
* User-selectable COM port
* User-selectable baud rate
* Receive data from the embedded device
* Send commands to the embedded device
* Display device responses
* Gracefully handle serial connection errors

## Requirements

* Python 3.x
* USB-to-Serial adapter or development board
* Embedded device with UART/serial communication

## Installation

Clone the repository:

bash
git clone https://github.com/dhruvdave4/Embedded-Serial-Communication-Tool
cd embedded-serial-tool

Install the required Python package:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python src/serial_tool.py
```

The program will ask for:

1. COM port
2. Baud rate
3. Operation to perform

Example:

```text
================================
      EMBEDDED SERIAL TOOL
================================

Enter COM port: COM3
Enter baud rate: 115200

Connected to COM3 at 115200 baud.

1. Read Data
2. Send Command
3. Exit
```

## Future Improvements

* Automatic COM-port detection
* Serial data logging
* CSV export
* GUI interface
* Automatic embedded-device testing
* Sensor-data visualization
* Firmware information display

## Project Goal

The goal of this project is to create a lightweight Python tool that can be used by embedded developers for UART communication, debugging, and device testing.
Author

Dhruv Darv
