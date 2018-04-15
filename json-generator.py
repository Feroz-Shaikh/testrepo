import json

gpsdata = {
  "acceleration_x": -0.3075714,
  "acceleration_y": -0.3994140,
  "acceleration_z": 9.834366,
  "roll": 0.031264,
  "pitch": 0.0405719,
  "yaw": 0.0027097,
  "longitude": 76.8663,
  "latitude": 8.5710,
  "heading": 0.0,
  "speed": 0.0,
  "timestamp": "2018-04-15T 14:30:32.759+05:30"
}

def generate_datapoints(d):
    d['acceleration_x'] = d['acceleration_x'] + 0.057
    d['acceleration_y'] = d['acceleration_y'] + 0.157
    d['acceleration_z'] = d['acceleration_z'] + 1.057
    d['longitude'] = d['longitude'] + 2.00
    d['latitude'] = d['latitude'] + 2.00
    d['timestamp'] = strftime("%Y-%m-%dT %H:%M:%S +0530", gmtime())
    return d
