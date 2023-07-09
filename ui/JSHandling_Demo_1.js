if (input.Error != null || input.QueryResults.IsSuccess != true || input.QueryResults.Results == null)
  return;
let oscilloscope = input.QueryResults.Results[0].ExtraFields;
let generator = input.QueryResults.Results[1].ExtraFields;
//[0].ValueStr;

let gwInfo = [
  {
    "Id": "GW-1",
    "FriendlyName": "GW-1 Name",
    "Description": "GW-1 Description",
    "LocationId": 1
  },
  {
    "Id": "GW-2",
    "FriendlyName": "GW-2 Name",
    "Description": "GW-2 Description",
    "LocationId": 2
  }
];

let trackerSettings = {
  "Layout": {
    "GW-1": {
      "Key": "GW-1",
      "X": 12.65,
      "Y": 2.1,
      "H": 3,
      "W": 3,
      "IsDraggable": true,
      "IsResizable": false,
      "IsStatic": false,
      "MaxH": 3,
      "MaxW": 3,
      "MinH": 3,
      "MinW": 3,
      "DefiesGrid": true
    },
    "GW-2": {
      "Key": "GW-2",
      "X": 18.6,
      "Y": 16,
      "H": 3,
      "W": 3,
      "IsDraggable": true,
      "IsResizable": false,
      "IsStatic": false,
      "MaxH": 3,
      "MaxW": 3,
      "MinH": 3,
      "MinW": 3,
      "DefiesGrid": true
    }
  },
  "VisibleGateways": [
    "GW-1",
    "GW-2"
  ],
  "GatewaySettings": {
    "GW-1": {
      "circles": {
        "quarters": [
          true,
          true,
          true,
          true
        ],
        "radiusCoefficient": 2.9,
        "color": "#50e3c2",
        "thickness": 2,
        "polarAngle": 0
      }
    },
    "GW-2": {
      "circles": {
        "quarters": [
          true,
          true,
          true,
          true
        ],
        "radiusCoefficient": 2.9,
        "color": "#eb5d5d",
        "thickness": 2,
        "polarAngle": 0
      }
    }
  },
  "TooltipSettings": {
    "color": "#d0021b",
    "fontSize": 14
  }
};

let assetInfo = {
  "GW-1": [
    {
      //[0].ValueStr;
      //Our first asset -> oscilloscope
      "Id": oscilloscope[0].ValueStr,
      "AssetName": oscilloscope[1].ValueStr,
      "ProximityLevel": oscilloscope[2].ValueStr,
      "IsRemoved": false,
      "IsLost": false,
      "Data": "Oscilloscope position around GW1"
    },
    {
      //Our second asset -> generator
      "Id": generator[2].ValueStr,
      "AssetName": generator[3].ValueStr,
      "ProximityLevel": generator[1].ValueStr,
      "IsRemoved": false,
      "IsLost": true,
      "Data": "Generator position around GW1"
    }
  ],
  "GW-2": [
    {
      //Our first asset -> oscilloscope
      "Id": oscilloscope[0].ValueStr,
      "AssetName": oscilloscope[1].ValueStr,
      "ProximityLevel": oscilloscope[3].ValueStr,
      "IsRemoved": false,
      "IsLost": false,
      "Data": "Oscilloscope position around GW2"
    },
    {
      //Our second asset -> generator
      "Id": generator[2].ValueStr,
      "AssetName": generator[3].ValueStr,
      "ProximityLevel": generator[0].ValueStr,
      "IsRemoved": false,
      "IsLost": true,
      "Data": "Generator position around GW2"
    }
  ]
}

return { gwInfo, trackerSettings, assetInfo } 