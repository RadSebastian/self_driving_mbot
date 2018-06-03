# Self driving mBot through neural network
Table of contents
=================

  * [Description](#description)
  * [Software Dependencies](#software-dependencies)
  * [Installation](#installation)
  * [Usage](#usage)

Description
-----------
Given two distances from the ultrasonic sensors use the trained neural network
to predict the direction.


It works on Linux, Windows 7 and OS X.

Software Dependencies
---------------------

* Makeblock Library (https://github.com/Makeblock-official/Makeblock-Libraries)
* Python (http://python.org/download/)
* Cython (http://cython.org/#download)
* cython-hidapi (https://github.com/trezor/cython-hidapi)
* pyserial

Prepare for Makeblock's Bots
----------------------------
1. Download the source from the git https://github.com/Makeblock-official/Makeblock-Libraries

2. copy the makeblock folder to your arduino default library. Your Arduino library folder should now look like this
(on Windows): [arduino installation directory]\libraries\makeblock\src
(on MACOS): [arduino Package Contents]\contents\Java\libraries\makeblock\src

3. Open the Arduino Application. (If it's already open, you will need to restart it to see changes.)

4. Click "File-> Examples". Here are firmwares for Makeblock's bots in "MakeBlockDrive->Firmware_for_mBlock".

5. Upload the Firmware to your bot.

Installation
-------

install python 2.7.x ( http://python.org/downloads )

  ```
  for Windows users: 
    set path x:/Python27 x:/Python27/Scripts
    Install Microsoft Visual C++ Compiler for Python 2.7
    (http://www.microsoft.com/en-us/download/confirmation.aspx?id=44266)
  ```
  ```
  for Macosx users:
    pip install --upgrade setuptools --user python
  ```
  ```
  [sudo] pip install cython
  [sudo] pip install pyserial
  [sudo] pip install hidapi
  ```
Usage
-----------------
 ```
  git clone https://github.com/radsebastian/self_driving_mbot
 ```
 Enter the folder "self_driving_mbot"
 
 Edit self_driving_mbot.py
 ```python
from lib.mBot import *

if __name__ == '__main__':
	 bot = mBot()
	 bot.startWithSerial("COM15") or bot.startWithHID()
	 while(1):
	   bot.requestLightOnBoard(1,onLight)
	   sleep(0.5)
 ```
  
  using usb serial or bluetooth serial:
  
  change the serial port name "COMX or /dev/tty.XXX" for your mBot on system
  ```
  bot.startWithSerial("COM15")
  ```
  
  using wireless HID:
  
  ```
  bot.startWithHID()
  ```
  
  running:
  
  ```
  [sudo] python self_driving_mbot.py
  ```
  
###Learn more from Makeblock official website http://www.makeblock.com
