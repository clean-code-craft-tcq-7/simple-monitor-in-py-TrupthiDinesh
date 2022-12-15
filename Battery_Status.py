from SOC import check_soc
from Temperature import Check_Temperature
from Charge_rate import check_charge_rate


def battery_is_ok(temperature, soc, charge_rate):
  temperature_check = Check_Temperature(temperature)
  soc_check = check_soc(soc)
  charge_rate_check = check_charge_rate(charge_rate)
  return (temperature_check and soc_check and charge_rate_check)
