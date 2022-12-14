 def Check_Temperature(temperature):
    if temperature < 0 or temperature > 45:
        print("temperature of battery is not ok!")
        return False
    print("temperature of battery is ok!")
    return True
