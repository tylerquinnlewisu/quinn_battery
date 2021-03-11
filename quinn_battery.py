# Tyler Quinn
# CPSC 21000 - Programming Fundamentals






# Centered heading 
print('*'* 60)
print('*%58s*' % "TYLER QUINN'S BATTERY LIFE ESTIMATOR".center(58))
print('*'* 60)

print('')


total_percent_reduction = 0

remainder = 0

#Asking for user response on KWH
kilowatt_hour = float(input('What is the current KWH on the battery?'))


#Asking for user response on temperature 
current_temperature = float(input('What is the current temperature?'))

traffic_choice = 0

current_traffic = 0

average_speed = 0


#Asking for user response on traffic
while traffic_choice == 0:
    print('These are your choices for describing traffic conditions: ')
    print('1. Good')
    print('2. Moderate')
    print('3. Stop-and-go')
    traffic_choice = float(input('Enter the number which describes your traffic: '))
    #Assigning reduction value for traffic
    if traffic_choice == 1:
        current_traffic = 0
    elif traffic_choice == 2:
        current_traffic = 10
    elif traffic_choice == 3:
        current_traffic = 25


#Asking for user response on speed so long as traffic is good    
while traffic_choice == 1 and average_speed == 0:
    average_speed = float(input('What will your average speed be in miles per hour?'))

climate_control_choice = 0

climate_control = 0

#Asking for user response on climate control
while climate_control_choice == 0:
    print('These are your choices for climate control: ')
    print('1. Off')
    print('2. Low')
    print('3. Medium')
    print('4. High')
    climate_control_choice = float(input('Enter the number of your climate control: '))
    #Assigning reduction value for climate control
    if climate_control_choice == 1:
        climate_control = 0
    elif climate_control_choice == 2: 
        climate_control = 5
    elif climate_control_choice == 3:
        climate_control = 10
    elif climate_control_choice == 4:
        climate_control = 20

#Calculating starting range using KWH 
starting_range = kilowatt_hour * 2.2

temperature_reduction = 0

#Determining temperature reduction
if current_temperature < 0:
    temperature_reduction = 40
elif current_temperature < 20: 
    temperature_reduction = 30
elif current_temperature < 40:
    temperature_reduction = 20
elif current_temperature > 85: 
    temperature_reduction = 10
elif current_temperature > 100:
    temperature_reduction = 30

speed_reduction = 0


#Determining speed reduction
if average_speed > 80:
    speed_reduction = 20
elif average_speed > 60: 
    speed_reduction = 10


#Calculating ending range
total_percent_reduction = temperature_reduction + current_traffic + speed_reduction + climate_control 

remainder = 100 - total_percent_reduction

overall_range = starting_range * (remainder/100)

print('')
print('')

#Battery report 
battery_report = ('Here is your battery range report:')



general_starting_range_statement = ('The starting range in miles is %.2f' %(starting_range))

general_temperature_reduction_statement = ('The percent temperature reduction is %.2f' %(temperature_reduction))

general_traffic_reduction_statement = ('The percent traffic reduction is %.2f' %(current_traffic))

general_speed_reduction_statement = ('The percent speed reduction is %.2f' %(speed_reduction))

general_climate_control_statement = ('The percent climate control reduction is %.2f' %(climate_control))

total_percent_reduction_statement = ('The total percent reduction is %.2f' %(total_percent_reduction))

overall_range_statement = ('The overall range in miles is %.2f' %(overall_range))


#Printing battery report statements in a table separated by dashes 
print(battery_report)

print('')

print('-'* 50)

print(general_starting_range_statement)

print('-'* 50)

print(general_temperature_reduction_statement)

print('-'* 50)

print(general_traffic_reduction_statement)

print('-'* 50)

print(general_speed_reduction_statement)

print('-'* 50)

print(general_climate_control_statement)

print('-'* 50)

print(total_percent_reduction_statement)

print('-'* 50)

print(overall_range_statement)

print('-'* 50)

print('*'* 60)