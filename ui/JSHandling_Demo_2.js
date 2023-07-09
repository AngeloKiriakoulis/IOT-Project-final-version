let asset = input.QueryResults.Results[2].ExtraFields;
let GeoJSON =
{
  "type": "FeatureCollection",
  "pictureURL": "https://static.yodiwo.com/content/img/uop_coaching_student_demos/UoP_demo_bg_1.png",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "value": 4,
        "popup": {
          "title": "Title",
          "subtitle": "Subtitle",
          "imageUrl": "https://tcyan.yodiwo.com/Content/img/Logos/favicon-32x32.png",
          "items": [
            {
              "type": "table",
              "label": "Table",
              "value": [
                [
                  "Device ID:",
                  "37C2EB"
                ],
                [
                  "Asset Name:",
                  "Power meter"
                ],
                [
                  "Value:",
                  "100w"
                ]
              ]
            },
            {
              "type": "text",
              "label": "Text",
              "value": "Type..."
            },
            {
              "type": "checkbox",
              "label": "Checkbox",
              "value": true
            },
            {
              "type": "switch",
              "label": "Switch",
              "value": true,
              "settings": {
                "isUserInput": true
              }
            },
            {
              "type": "percentage",
              "label": "Percentage",
              "value": "20"
            },
            {
              "type": "button",
              "label": "Button with action",
              "settings": {
                "pageUrl": "https://www.yodiwo.com/"
              },
              "value": "Something that you need to read in Cyan"
            },
            {
              "type": "button",
              "label": "Maintenance request",
              "value": "Something that you need to read in Cyan"
            }
          ]
        },
        "tooltip": "Mouse tooltip",
        "marker": {
          "prefix": "fa",
          "icon": "laptop",
          "markerColor": "orange",
          "iconColor": "blue",
          "shape": "circle",
          "layer": "Layer 1",
          "size": "large"
        }
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          asset[0].ValueDbl,
          asset[1].ValueDbl
        ]
      }
    }
  ]
}

return { GeoJSON }