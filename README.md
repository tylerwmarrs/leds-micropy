# LEDs MicroPY
This repository is used to store various MicroPython based LED projects.

# Folder Structure
Each folder contains a separate project and README.md on how to run it. The exception is that there is a modules folder containing a common code base.

# Setup
All of these projects have been tested on ESP based microcontrollers: Wemos D1 Mini or NodeMCU. The instructions are written for a Debian based operating system.

## Install Requirements
Of course you can create an environment file or virtual environment first. That is not covered here.

```
pip install -r requirements.txt
```

The requirements file includes the esptool.py to flash your microcontroller and ampy to upload files to the microcontroller.

## Download MicroPython
Download the latest MicroPython firmware for the esp8266:
https://micropython.org/download#esp8266

## Add User to dialout
If you want to use ampy and esptool.py without requiring sudo, you should add your user to the dialout group. It will require a restart or login/logout.

```
sudo usermod -a -G dialout $USER
```

## Identify Port
Connect the device via USB, run this command, and look for the text below.

```
sudo dmesg
```

```
ch341-uart converter now attached to ttyUSB0
```

The attached to could be any device, but usually is ttyUSB0. We now know our device path:

```
/dev/ttyUSB0
```

## Erase Flash
Run the following substituting the device path as needed. Your microcontroller must be plugged in.

```
esptool.py --port /dev/ttyUSB0 erase_flash
```

## Flash MicroPython
This flashes MicroPython onto the microcontroller. Be sure that it is plugged in and you substitute the FIRMWARE_PATH with the location of the firmware you downloaded and device path if needed.

```
esptool.py  --port /dev/ttyUSB0 --baud 460800 write_flash -fm dio --flash_size=detect 0 FIRMWARE_PATH
```
