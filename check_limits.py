from Battery_Status import battery_status
from SOC import check_soc
from Temperature import Check_Temperature
from charge_rate import check_charge_rate

if __name__ == '__main__':
  assert(battery_status(25, 70, 0.7) is True)
  assert(battery_status(50, 85, 0) is False) 
  assert(Check_Temperature(-1) is False)
  assert(Check_Temperature(0) is True)
  assert(check_charge_rate(0.9) is False)
  assert(check_charge_rate(0.8) is True)
  assert(check_soc(19) is False)
  assert(check_soc(20) is True)
