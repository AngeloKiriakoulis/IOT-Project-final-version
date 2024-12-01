### **Installation Guide for Edge-Level Setup:**
**Project:** BLE-based Indoor Asset and People Tracking

1. Install Linux OS on a host or virtual machine. For the demo, Ubuntu OS was used, installed on VMWare Workstation 17 Player.
2. Install Python 3.x as described on [opensource.com](https://opensource.com/article/20/4/install-python-linux). Ensure the `python3-docutils` dependency is included.
3. Install BlueZ 5.x following the instructions on [Adafruit](https://learn.adafruit.com/install-bluez-on-the-raspberry-pi/installation).
4. Install the Python libraries `bluepy`, `requests`, and `json` using `pip3`.
5. Connect the BLE Controller (SmartBond™ DA14695 Bluetooth Low Energy 5.2 Main-Board) to a USB port (for virtual machines, ensure the device is connected to the VM, not the host). Run the command `hciattach -s 115200 /dev/ttyUSB0 any` for setup.

**For the BLE-Mesh Demo:**
6. Activate the asset beacons (SmartBond™ DA14695 Bluetooth Low Energy 5.2 Daughter-Board) using the built-in switch.
7. Run the `ble_mesh.py` script. Some asset beacons may require a reset to begin data advertisement after a period of inactivity.

**For the WiRa Demo:**
6. Connect the SmartBond™ Wireless Ranging (WiRa™) device to a USB port. Configuration was performed using the SmartSnippetsToolBox under supervision from Renesas.
7. Use Tera Term to display serial input data from the WiRa™ device.
8. Run the `wira.py` script.

**Accessing the UI:**
- Access to the application’s UI requires login credentials for the Yodiwo platform.

---

### **Summary:**
This project demonstrated the implementation of a BLE-based asset tracking system that utilized edge computing for real-time processing and cloud integration for visualization. The architecture provided a scalable, efficient solution for both proximity sensing and precise localization.
