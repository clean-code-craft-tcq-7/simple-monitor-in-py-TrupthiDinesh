from battery_status import battery_is_ok
from SOC import check_soc
from Temperature import check_temperature
from charge_rate import check_charge_rate

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False) 
  assert(check_temperature(-1) is False)
  assert(check_temperature(0) is True)
  assert(check_charge_rate(0.9) is False)
  assert(check_charge_rate(0.8) is True)
  assert(check_soc(19) is False)
  assert(check_soc(20) is True)
