# Solax Python Wrapper

Exploited [CVE-2023-35835](https://app.opencve.io/cve/CVE-2023-35835).

This device exposes status and telemetry report over the network. The wrapper fetches device status, including current (A) and voltage (V) readings.

# Data Mapping

The mapping of data fields from the Solax API response.

The data is extracted from a JSON response which contains a `Data` list (referred to as `raw` in the script), an `Information` list, and some root-level properties.

### `Data` list (`raw`)

| Index | Description           | Notes                                  |
| ----- | --------------------- | -------------------------------------- |
| 0     | Grid Voltage          | Scaled by 0.1, in Volts (V)            |
| 1     | PV1 Current           | Scaled by 0.1, in Amperes (A)          |
| 2     | Grid Frequency        | Scaled by 0.01, in Hertz (Hz)          |
| 3     | PV1 Input Power       | In Watts (W)                           |
| 3     | Inverter Active Power | In Watts (W)                           |
| 4     | PV1 Voltage           | Scaled by 0.1, in Volts (V)            |
| 8     | Grid Current          | Scaled by 0.1, in Amperes (A)          |
| 11    | Grid Power            | In Watts (W)                           |
| 13    | Total Solar Power     | In Watts (W)                           |
| 19    | Total Yield           | Scaled by 0.1, in kilowatt-hours (kWh) |
| 21    | Daily Yield           | Scaled by 0.1, in kilowatt-hours (kWh) |
| 23    | Inverter Temperature  | In Celsius (°C)                        |

### `Information` list (`info`)

| Index | Description       |
| ----- | ----------------- |
| 2     | Device Model/Info |

### Root JSON object

| Key  | Description          |
| ---- | -------------------- |
| `sn` | Device Serial Number |
