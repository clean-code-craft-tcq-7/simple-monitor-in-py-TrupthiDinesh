from soc import check_soc
from Temperature import check_temperature
from charge_rate import check_charge_rate


def battery_status(temperature, soc, charge_rate):
  temperature_check = check_temperature(temperature)
  soc_check = check_soc(soc)
  charge_rate_check = check_charge_rate(charge_rate)
  return (temperature_check and soc_check and charge_rate_check)
