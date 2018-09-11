"""
Programmet konverterar feet till meter; km/h till mph och celcius till farenheit
"""

feet = 3.28084
mph = 0.62137

metric = input("Skriv in höjd i meter: ")
totfeet = float(metric) * feet

kmh = input("Skriv in hastighet i km/h: ")
totmiles = mph * float(kmh)

tempC = input("Skriv in temperatur i celcius: ")
tottempF = float(tempC) * 9 / 5 + 32

metertofeet = "Meter konverterat till feet: " + str(totfeet) + " feet "
kmhtomph = "Km/h konverterat till mph: "+ str(totmiles) + " mph. "
CtoF = "Yttertemperatur: " + str(tottempF) + " Farenheit"

print(metertofeet+kmhtomph+CtoF)
