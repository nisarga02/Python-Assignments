# 10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = int(input('Enter your salary: '))
year_of_service = int(input('Enter your year of service: '))

if year_of_service > 5:
  net_bonus_amount = .05 * salary
print(net_bonus_amount)
