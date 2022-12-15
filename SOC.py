 def check_soc(soc):
    if soc < 20 or soc > 80:
        print("'State of Charge is out of range!")
        return False
    print("State of charge of battery is ok")
    return True
