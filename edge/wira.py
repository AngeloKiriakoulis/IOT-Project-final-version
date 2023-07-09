from bluepy.btle import Scanner, ScanEntry, DefaultDelegate
import struct
import requests
import json

# Authors: Aggelos Kiriakoulis, Themis Nikellis
# Date: 2023-02-14
# Description
"""This is a Python code that acts as a Bluetooth Low Energy (BLE) Gateway. It gathers the information sent by the ®Renesas WiRa Device (Initiator), which is an AltBeacon Message (non connectable undirected advertising), that contains the distance between the device and 3 static Beacons (Responders).The code then uses trilateration to calculate the location of the device in a 2D space relative to three predefined points. The calculated location is then sent to the ®Yodiwo YodiFEM Platform in the form of a JSON object."""

#X_MAX = 8.42 #Distance between 2 responders (68,f1), in the x axis.
#Y_MAX = 7.35 #Distance between 2 responders (68,f2), in the y axis.
X_MAX = 1.7 #Test Distance (x axis)
Y_MAX = 4.25 #Test Distance (y axis)

"""This function takes the BLE advertisement data as an argument, and parses the AltBeacon Message, in order to retrieve the distances between the Initiator and the Responders. It converts the hexadecimal data to float numbers and returns the three distances in a list."""
def getDistance(val):
    indexes=[]
    distances=[]
    for i in range(8,14,2):
        indexes.append(val[i:i+2])
    hexnums=[]
    for i in range(20,44,8):
        hexnums.append(val[i:i+8])
    for hex_num in hexnums:
        hex_inv = ""
        for i in range(7,0,-2):
            hex_inv += hex_num[i-1] + hex_num[i]
            l = int(hex_inv, 16)
            f = struct.pack('>l', l)
            f = struct.unpack('>f', f)[0]
        distances.append(f)
    print(indexes,distances)
    x_norm, y_norm = triangulate(indexes,distances)
    return x_norm, y_norm


"""This function takes the list of distances and the list of indexes that identify the three reference points, and performs trilateration to estimate the location of the device. The function returns the normalized (0 to 1) x and y coordinates of the estimated location. We normalize the distance, so it can be shown in the ®Yodiwo Emerald Map Widget"""
def triangulate(ind,dist):
    coordinates = {'68':[0.0,0.0],'f2':[0.0,Y_MAX],'f1':[X_MAX,0.0]}
    x1 = coordinates[ind[0]][0]
    y1 = coordinates[ind[0]][1]
    r1 = dist[0]
    
    x2 = coordinates[ind[1]][0]
    y2 = coordinates[ind[1]][1]
    r2 = dist[1]
    
    x3 = coordinates[ind[2]][0]
    y3 = coordinates[ind[2]][1]
    r3 = dist[2]
    
    x = 0.0
    y = 0.0
    
    A = x1 - x2 
    B = y1 - y2
    D = x1 - x3
    E = y1 - y3
    
    T = (r1*r1 - x1*x1 - y1*y1)
    C = (r2*r2 - x2*x2 - y2*y2) - T
    F = (r3*r3 - x3*x3 - y3*y3) - T
    
    Mx = (C*E - B*F)/2.0
    My = (A*F - D*C)/2.0
    
    M = A*E - D*B
    
    if M != 0:
        x = Mx/M
        y = My/M
        if x<0: x=0.0
        if y<0: y=0.0
    print(x,y,'\n')
    
    x_norm=x/X_MAX
    y_norm=y/Y_MAX
    if x_norm>1.0: x_norm=1.0
    if y_norm>1.0: y_norm=1.0
    print(x_norm,y_norm,'\n')
    return x_norm, y_norm
    
    
"""This function takes the x and y coordinates of the estimated location, constructs a JSON object, and sends it as an HTTP PUT request the ®YodiFEM URL."""
def put_json(x,y):
    url = "https://fm2service-dev.yodiwo.com/fm/assets/31853"

    payload = json.dumps({
  "OrgId": "65",
  "DeploymentId": "272",
  "BuildingId": "1439",
  "Name": "ASSET_FOR_DEMO_2",
  "Description": "",
  "RefAssetId": None,
  "AssetTypeId": 70,
  "AssetCategoryId": None,
  "MaintainerId": None,
  "GeoJson": None,
  "ExtraFields": [
    {
      "AssetExtraFieldInfoId": 111,
      "ValueDbl": x
    },
    {
      "AssetExtraFieldInfoId": 112,
      "ValueDbl": y
    }
  ]
})
    headers = {
  'x-api-key': '_UxiU2rXZxqSH8e9rM8ihm6b_7kOEZTOTw5td40B0pic4-OCNb1h6PQMXczj_ldj57f2T3vOusn2FBjLfhUcgyKCPkOo0218o5KOLMrS5kAyIlC_1B9r6WqjqZAK9wF9STrmo_Cc4RUIf3l63PEf-9LuMwZNljjghjr6hMQn_UTHMSgfbkQ7QCOr28ACARCldx1wZHb6AfbbsBMDWbMvTk0OxGGWMYCLfUNut3Ckcy4P7ckHXjaxxG-JV0D8u-w',
  'Content-Type': 'application/json',
  'Cookie': 'NCSRF_FEMP=RandomBytes%234ZZcsc4Qri5uUw%3d%3d%7cHmac%23dPZ8F5aSG3lR0sUusuRWDphrM%2ftbRoeYkWrea2KQ1nk%3d%7cCreatedDate%232023-02-14T10%3a38%3a54.8379777%2b00%3a00'
}

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
    
    
"""This is a class that is derived from the DefaultDelegate class of the bluepy.btle module. It is used to handle BLE scan events, detected by the ®Renesas BLE Controller"""    
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    """This is a method of the ScanDelegate class that is called when a new BLE advertisement from the initiator is detected."""    
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewData and dev.addr == "48:23:35:27:11:04":
            print("Received new data from", dev.addr)
            print(f'Device {dev.addr} found, RSSI={dev.rssi} dB')
            for (adtype, desc, value) in dev.getScanData():
                x,y = getDistance(value)
                put_json(x,y)
                    
scanner = Scanner(1).withDelegate(ScanDelegate())
while True:
    scanner.scan(2.0)
