# Oefening 8: volume van een cilinder
import math
diameter = float(input("Diameter: "))
hoogte = float(input("Hoogte: "))
volumeCilinder = round((math.pi * math.pow(diameter, 2)) / 4 * hoogte, 1)
print(f"Volume: {volumeCilinder}")
