#---------------- Average High Temperature ----------------
days = int(input('How many day\'s temperature do you want?'))
temperatureList = []

for day in range(days):
    tempOfDay = int(input(f'Day {day}\'s high temp: '))
    temperatureList.append(tempOfDay)

averageTemperature = sum(temperatureList) / days

aboveAverageDays = 0
for temperature in temperatureList:
    if temperature > averageTemperature:
        aboveAverageDays +=1

print(f'The average high temperature was: {averageTemperature}')
print(f'There were {aboveAverageDays} days where the temperature was above average')

