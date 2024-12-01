# Final Architecture Analysis for the Project:
## **"BLE-based Indoor Asset and People Tracking"**

### **Architecture Overview:**
**Edge → Database → GEM → Widget**

---

### **1. Edge-Level Architecture:**
We utilized BLE devices to detect the location of assets or people indoors. Specifically, we worked with SmartBond™ DA14695 Bluetooth Low Energy 5.2 Daughter Boards/Main Boards and SmartBond™ Wireless Ranging (WiRa™) technology provided by Renesas.  

#### **BLE Gateways:**
- **Custom Gateways Implementation:**
  - Two custom BLE Gateways were implemented using DA14695 Main Boards with the BlueZ protocol stack.
  - The Python `pybluez` library was used to access BLE data from the Main Board for two distinct demos:

    1. **Proximity Sensing Demo:**
       - BLE signals were filtered to focus on two specific DA14695 Daughter Boards.
       - RSSI values were used to classify device proximity into three levels: *Immediate, Near,* and *Far*.
       - This demo mimicked a BLE Mesh solution where each Gateway acted as a node capable of peer-to-peer communication or relaying messages Over-The-Air (OTA) through intermediate nodes.

    2. **Precise Localization Demo:**
       - Leveraged WiRa™ for high-accuracy localization.
       - At least three static beacons (DA14695 Daughter Boards) were placed as responders, while one WiRa™ device configured as an initiator calculated distances to the beacons.
       - Using BLE Range DTE data, triangulation was performed to determine the WiRa™ device’s coordinates.
       - Parsed AltBeacon messages were sent to the custom Gateway for further processing, such as normalization of coordinates for use in the project’s UI.

---

### **2. Cloud Integration:**
- **Data Transfer to Cloud:**
  - PUT requests sent from the edge to the Yodiwo platform using Postman for request formatting in Python.
  - The Yodiwo database was configured with asset types and extra fields depending on the demo:
    - *Proximity Sensing Demo:* Extra fields included `id`, `name`, `proximity_level_from_gateway1`, and `proximity_level_from_gateway2`.
    - *Localization Demo:* Extra fields included `xcoordinate` and `ycoordinate`.
  - These fields were regularly updated to ensure the database remained in sync with real-time asset data.

- **UI Implementation:**
  - Two widgets were used for visualization: an *Asset Tracker Widget* for the Proximity Sensing Demo and a *Maps Widget* for the Localization Demo.
  - Data for these widgets was processed through a custom GEM, which automated data retrieval and rendering.

---

### **3. GEM Workflow:**
The GEM was composed of five stages, facilitating the connection between the database and the UI widgets:

1. **Data SRC:** Collect account-specific data (e.g., `OrgId`, `RestAPIBasePath`) for use in subsequent steps.
2. **JS Preparation:** Process results from the previous stage and prepare them for querying.
3. **Query:** Perform POST requests to Yodiwo's API endpoint (`https://$(config.RestAPIBasePath)/fm/assets/search`) to fetch relevant asset data.
4. **JS Handling:** Write JavaScript code to transform database data into the appropriate format for the widget.
5. **Data DST:** Map the output variables from the previous stage to the input ports of the widget for final display.

---

### **Summary:**
This project demonstrated the implementation of a BLE-based asset tracking system that utilized edge computing for real-time processing and cloud integration for visualization. The architecture provided a scalable, efficient solution for both proximity sensing and precise localization.
