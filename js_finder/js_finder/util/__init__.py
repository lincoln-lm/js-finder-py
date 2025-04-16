from math import floor

system_data = {
    "RSE": {"frame_rate": (16777216 / 280896), "offset_ms": 0},   
    "GBA": {"frame_rate": (16777216 / 280896), "offset_ms": -260},
    "GBP": {"frame_rate": (16777216 / 280896), "offset_ms": 200},
    "NDS": {"frame_rate": (16756991 / 280896), "offset_ms": 788},
    "3DS": {"frame_rate": (16756991 / 280896), "offset_ms": 1558},
}

def frame_to_ms(frame, system):
        return floor((frame) / (system_data[system]["frame_rate"]) * 1000) + system_data[system]["offset_ms"]

