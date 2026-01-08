import urllib.request
import json


def parse_inverter_data(input_data):
    """
    Parses raw inverter data dictionary and returns meaningful information
    matching the provided app screenshots.
    """
    # Extract the raw data list
    raw = input_data.get("Data", [])
    info = input_data.get("Information", [])

    if not raw:
        return "No data found."

    def scale(value, factor):
        """Scales integer values to floats (e.g., 2502 -> 250.2)"""
        return round(value * factor, 1)

    parsed_data = {
        "Device Info": {
            "Serial Number": input_data.get("sn"),
            "Model/Info": info[2] if len(info) > 2 else "Unknown",
        },
        "Solar": {
            "PV1 Voltage": f"{scale(raw[4], 0.1)} V",
            "PV1 Current": f"{scale(raw[1], 0.1)} A",
            "PV1 Input Power": f"{float(raw[3])} W",
            "Total Solar Power": f"{float(raw[13])} W",
        },
        "Grid": {
            "Voltage": f"{scale(raw[0], 0.1)} V",
            "Current": f"{scale(raw[8], 0.1)} A",
            "Frequency": f"{scale(raw[2], 0.01)} Hz",
            "Grid Power": f"{float(raw[11])} W",
            "Consumed": "0.0 kWh",
            "Exported Energy": "0.0 kWh",
        },
        "Inverter": {
            "Active Power": f"{float(raw[3])} W",  # Matches 'Inverter' bubble in screenshot
            "Temperature": (
                f"{raw[23]} °C" if len(raw) > 23 else "N/A"
            ),  # inferred, index 23 is often temp
        },
        "Yield": {
            "Daily Yield": f"{scale(raw[21], 0.1)} kWh",
            "Total Yield": f"{scale(raw[19], 0.1)} kWh",
        },
    }

    return parsed_data


# CONFIGURATION
IP = "192.168.10.10"
PWD = "SRXXXXXXXXX"


def fetch_and_dump():
    url = f"http://{IP}/"
    headers = {"X-Forwarded-For": "5.8.8.8"}
    payload = f"optType=ReadRealTimeData&pwd={PWD}".encode("utf-8")

    print(f"[*] Fetching full telemetry from {IP}...")

    try:
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=10) as response:
            resp_json = json.loads(response.read().decode("utf-8"))

            parsed_data = parse_inverter_data(resp_json)

            print(parsed_data)

    except Exception as e:
        print(f"[!] FAILED: {e}")


if __name__ == "__main__":
    fetch_and_dump()
