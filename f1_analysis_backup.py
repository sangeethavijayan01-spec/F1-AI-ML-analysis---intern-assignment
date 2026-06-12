import fastf1
import pandas as pd
import matplotlib.pyplot as plt

print("Loading Bahrain 2024 Race Data...")

session = fastf1.get_session(2024, "Bahrain", "R")
session.load()

# Get lap data
laps = session.laps

# Convert lap times to seconds
laps["LapTimeSeconds"] = laps["LapTime"].dt.total_seconds()

print("\nLap Time Statistics:")
print(laps["LapTimeSeconds"].describe())

# Driver comparison
ver_laps = laps.pick_drivers("VER")
lec_laps = laps.pick_drivers("LEC")

plt.figure(figsize=(12, 6))

plt.plot(
    ver_laps["LapNumber"],
    ver_laps["LapTimeSeconds"],
    label="VER"
)

plt.plot(
    lec_laps["LapNumber"],
    lec_laps["LapTimeSeconds"],
    label="LEC"
)

plt.title("VER vs LEC Lap Times - Bahrain GP 2024")
plt.xlabel("Lap Number")
plt.ylabel("Lap Time (Seconds)")
plt.legend()

plt.savefig("driver_comparison.png")
plt.show()