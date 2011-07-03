# Define modifiers for your raw sensor values
# e.g. Thermistor calculations

import math

# thermistor calculation for Seeed Temperature Sensor Twig SEN23292P
def modify(rawValue):
        a0 = float(rawValue)
	B = 3975
        resistance = (1024-a0)*10000/a0
        print resistance
        tempC = 1/(math.log(resistance/10000)/B+1/298.15)-273.15
	roundTempC = round(tempC,2)
	return roundTempC

