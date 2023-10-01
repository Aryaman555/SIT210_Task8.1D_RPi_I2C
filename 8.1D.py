import smbus2
from bh1750 import BH1750

# Define I2C bus and BH1750 sensor address
bus = smbus2.SMBus(1)  # Use I2C bus 1 (Raspberry Pi 3/4)
sensor = BH1750(bus, address=0x23)  # Default I2C address for BH1750

# Function to categorize light intensity
def categorize_light(intensity):
    if intensity > 10000:
        return "Too bright"
    elif intensity > 5000:
        return "Bright"
    elif intensity > 2000:
        return "Medium"
    elif intensity > 1000:
        return "Dark"
    else:
        return "Too dark"

try:
    while True:
        # Read light intensity data
        light_intensity = sensor.measure_high_res()
        print("Light Intensity:", light_intensity, "lx")
        category = categorize_light(light_intensity)
        print("Category:", category)

except KeyboardInterrupt:
    print("Measurement stopped by the user.")
