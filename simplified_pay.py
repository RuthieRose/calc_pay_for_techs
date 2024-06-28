
'''

 replace the 0s with your pay structure
 hours are currently defined based on the pay plan this was based on
 you can adjust the shop hours according to your tiers
 in case of additional tiers 
 follow the pattern to add any additional tiers

 ** also mechanics are underpaid **

'''

#Inputs

#Change the payperiod ending
payperiod_ending = 'June 21, 2024'
payperiod_statement = f'Payperiod ending {payperiod_ending}'

#Change the hours below
hours_week1 = 224
hours_week2 = 324

#Change the base pay to your base pay
base_pay = 0

#Adjust the multiplier to your pay plan. If you remove any multipliers be sure to remove them from the function
multiplier_tier1 = 0
multiplier_tier2 = 0
multiplier_tier3 = 0
multiplier_tier4 = 0
multiplier_tier5 = 0

#If there are additional bonuses (not common for us) then they can be added here
additional_bonus_1 = 0
additional_bonus_2 = 0

#Functions 

def bonus_for_week(hours, additional_bonus, week):
    # bonus is instantiated here, the multiplier adds to the 0
    #Change the hours to whatever your multiplier hour requirement is
    bonus = 0
    if hours >= 170 and hours < 180:
        print(f'The multiplier for {week} is {multiplier_tier1}')
        bonus += hours * multiplier_tier1
    if hours >= 180 and hours < 190: 
        print(f'The multiplier for {week} is {multiplier_tier2}')
        bonus += hours * multiplier_tier2 
    if hours >= 190 and hours < 200: 
        print(f'The multiplier for {week} is {multiplier_tier3}')
        bonus += hours * multiplier_tier3
    if hours >= 200 and hours < 235:
        print(f'The multiplier for {week} is {multiplier_tier4}')
        bonus += hours * multiplier_tier4
    if hours >= 235:
        print(f'The multiplier for {week} is {multiplier_tier5}')
        bonus += hours * multiplier_tier5
    bonus += additional_bonus
    if additional_bonus > 0: print(f'The additional bonus for {week} is {additional_bonus}')
    return bonus 

def expected_pay(hours,additional_bonus, week):
    return bonus_for_week(hours,additional_bonus, week) + base_pay

week1_expected_pay = expected_pay(hours_week1,additional_bonus_1, 'week 1')
week2_expected_pay = expected_pay(hours_week2,additional_bonus_2, 'week 2')

#Print Statements, will print to the terminal when you run the program in the terminal

print(f'Expected pay for week 1 is {week1_expected_pay}')
print(f'Expected pay for week 2 is {week2_expected_pay}')
print(f'Expected pay for {payperiod_statement} is {week1_expected_pay + week2_expected_pay}')