import csv
import matplotlib.pyplot as plt
import calendar
from datetime import datetime

weather_data = 'sitka_2014-weather.csv'

with open(weather_data) as f:

    reader = csv.reader(f)
    header =  next(reader)

    dates = [] 
    daily_min_temps = []
    daily_max_temps = []
    
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            daily_min_temp = int(row[3])
            daily_max_temp = int(row[1])
        except ValueError:
            print(date, 'missing data')
        else:
            # dates.append(str(calendar.month_abbr[date.month]) + ' ' + str(date.year))
            dates.append(date)
            daily_min_temps.append(daily_min_temp)
            daily_max_temps.append(daily_max_temp) 

    fig = plt.figure(dpi=128, figsize=(10, 8))
    plt.plot(dates, daily_min_temps, c='blue', label='Min daily temperatures')
    plt.plot(dates, daily_max_temps, c='red', label='Max daily temperatures')
    plt.fill_between(dates, daily_min_temps, daily_max_temps, facecolor='blue', alpha=0.1)

    plt.title('Sitka - Local Temperatures in 2014', fontsize=22)
    plt.xlabel('Date', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16) 
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.savefig('sitka_2014-temperatures.png')
    plt.show()
