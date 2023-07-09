import requests
import json
from bluepy.btle import Scanner, ScanEntry, DefaultDelegate

# Authors: Aggelos Kiriakoulis, Themis Nikellis
# Date: 2023-02-14
# Description
"""This code is a Bluetooth Low Energy (BLE) scanner that scans for two specific ®Renesas BLE devices with known Bluetooth addresses. When each device is detected, the Received Signal Strength Indicator (RSSI) is checked to determine the proximity of the device. If the device is within a certain range, the code sends a PUT request to the ®Yodiwo YodiFEM Platform with JSON data that includes the proximity of the device. This is one of the 2 implemented scanners"""

json_dict={"48:23:35:ee:bb:aa":["https://fm2service-dev.yodiwo.com/fm/assets/31843", {
  "OrgId": "65",
  "DeploymentId": "272",
  "BuildingId": "1439",
  "Name": "DEMO ASSET OSCILLOSCOPE",
  "Description": "",
  "RefAssetId": None,
  "AssetTypeId": 68,
  "AssetCategoryId": None,
  "MaintainerId": None,
  "GeoJson": None,
  "ExtraFields": [
    {
      "AssetExtraFieldInfoId": 105,
      "ValueStr": "DEMO_ASSET_OSCILLOSCOPE_ID"
    },
    {
      "AssetExtraFieldInfoId": 106,
      "ValueStr": "OSCILLOSCOPE"
    },
    {
      "AssetExtraFieldInfoId": 107,
      "ValueStr": "Far"
    }
    
  ]
}],
	"48:23:35:00:00:f8":["https://fm2service-dev.yodiwo.com/fm/assets/31844", {
  "OrgId": "65",
  "DeploymentId": "272",
  "BuildingId": "1439",
  "Name": "DEMO ASSET GENERATOR",
  "Description": "",
  "RefAssetId": None,
  "AssetTypeId": 68,
  "AssetCategoryId": None,
  "MaintainerId": None,
  "GeoJson": None,
  "ExtraFields": [
    {
      "AssetExtraFieldInfoId": 105,
      "ValueStr": "DEMO_ASSET_GENERATOR_ID"
    },
    {
      "AssetExtraFieldInfoId": 106,
      "ValueStr": "GENERATOR"
    },
    {
      "AssetExtraFieldInfoId": 107,
      "ValueStr": "Near"
    }
  ]
}]}


"""This function takes an integer value representing the RSSI of a detected device and returns a string indicating the proximity of the device based on pre-defined ranges. The ranges are defined as Immediate, Near, and Far. The function is used to set the value of an "ExtraField" in the JSON data to the proximity of the device."""
def check_range(num):
    if -59 <= num <= -20:
        return "Immediate"
    elif -79 <= num <= -60:
        return "Near"
    elif -100 <= num <= -80:
        return "Far"
    else:
        return "Number is not in any of the given ranges."
        
        
"""This function takes the Bluetooth address and RSSI of a detected device and constructs a JSON payload with the proximity value based on the RSSI. The payload is then sent in a PUT request to the ®YodiFEM Platform with the provided headers."""        
def put_json(BD_address,RSSI):
    url = json_dict[BD_address][0]
    print(check_range(RSSI))
    json_dict[BD_address][1]["ExtraFields"][2]["ValueStr"] = check_range(RSSI)
    
    payload = json.dumps(json_dict[BD_address][1])
    
    headers = {
      'x-api-key': '_UxiU2rXZxqSH8e9rM8ihm6b_7kOEZTOTw5td40B0pic4-OCNb1h6PQMXczj_ldj57f2T3vOusn2FBjLfhUcgyKCPkOo0218o5KOLMrS5kAyIlC_1B9r6WqjqZAK9wF9STrmo_Cc4RUIf3l63PEf-9LuMwZNljjghjr6hMQn_UTHMSgfbkQ7QCOr28ACARCldx1wZHb6AfbbsBMDWbMvTk0OxGGWMYCLfUNut3Ckcy4P7ckHXjaxxG-JV0D8u-w',
      'Content-Type': 'application/json',
      'Cookie': 'NCSRF_FEMP=RandomBytes%23jMEZH%2fHzcy%2f96g%3d%3d%7cHmac%23zOb%2btoJATefbdTHG%2f22bBN5GXAoLqh39A844IaTLr7k%3d%7cCreatedDate%232023-01-19T18%3a09%3a06.2288017%2b00%3a00'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
    
    
"""This class inherits from the DefaultDelegate class of the bluepy.btle module and overrides the handleDiscovery() method to handle 
BLE device discoveries. When a new device is discovered, the method checks if it matches the specified Bluetooth addresses, and if so, 
it calls the put_json() function with the device's address and RSSI."""       
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
        
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewData and dev.addr == "48:23:35:ee:bb:aa":
            print("Received new data from", dev.addr)
            print(f'Device {dev.addr} found, RSSI={dev.rssi} dB\n')
            put_json(dev.addr,dev.rssi)
        if isNewData and dev.addr == "48:23:35:00:00:f8":
            print("Received new data from", dev.addr)
            print(f'Device {dev.addr} found, RSSI={dev.rssi} dB\n')
            put_json(dev.addr,dev.rssi)
            
scanner = Scanner(1).withDelegate(ScanDelegate())
while True:
    """This line starts an infinite loop that scans for BLE devices every 2 seconds using the Scanner object from 
    the bluepy.btle module with the ScanDelegate class as a delegate. This loop will continue to run until the program is manually stopped."""
    scanner.scan(2.0)    

