  def check_charge_rate(charge_rate):
    if charge_rate > 0.8:
        print("Charge rate is out of range!")
        return False
    print("Charge rate of battery is ok!")
    return True
