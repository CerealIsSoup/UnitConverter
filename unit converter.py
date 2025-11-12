def primInfo():
    name = input("What is your name? ").lower()
    height = float(input("What is your height? "))
    return name, height

def secInfo():
    mesSys = input("Does your country use the metric system (m) or the U.S. customary system (c)? ").lower()

    while mesSys not in ["m", "c"]:
        mesSys = input("Invalid input. Type 'm' for metric or 'c' for customary: ").lower()

    if mesSys == "m":
        temp = float(input("What is the temperature in Celsius? "))
    else:
        temp = float(input("What is the temperature in Fahrenheit? "))

    return mesSys, temp


def convert(mesSys, height, temp):
    if mesSys == "m":
        height_in_inches = height / 0.0254
        temp_in_f = (temp * 9/5) + 32
        return height_in_inches, temp_in_f, "converted to U.S. customary units"
    else:
        height_in_m = height * 0.0254
        temp_in_c = (temp - 32) * 5/9
        return height_in_m, temp_in_c, "converted to metric units"


name, height = primInfo()
mesSys, temp = secInfo()

converted_height, converted_temp, system_msg = convert(mesSys, height, temp)

print(f"\n{name.title()}, your info {system_msg}:")
if mesSys == "m":
    print(f"Height: {converted_height:.2f} inches")
    print(f"Temperature: {converted_temp:.2f}°F")
else:
    print(f"Height: {converted_height:.2f} meters")
    print(f"Temperature: {converted_temp:.2f}°C")
