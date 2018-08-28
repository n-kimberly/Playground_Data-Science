import csv
import matplotlib.pyplot as plt

weather_data = 'sitka_july-weather.csv'

with open(weather_data) as f:

    reader = csv.reader(f)
    header =  next(reader)

    for index, column in enumerate(header):
        print("index = %s, column is = %s" % (index, column))

    date = [] 
    daily_min_temp = []
    daily_max_temp = []
    
    for row in reader:
        date.append(int(row[0][7:]))
        daily_min_temp.append(int(row[3]))
        daily_max_temp.append(int(row[1])) 

    plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(date, daily_min_temp, c="blue")
    plt.plot(date, daily_max_temp, c="red")
    plt.title("Temperatures in Sitka, July 2014", fontsize=22)
    plt.xlabel("Days in July", fontsize=16)
    plt.ylabel("Temperature (deg F)", fontsize=16) 
    plt.show()
