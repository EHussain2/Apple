

from statistics import mean

if __name__ == '__main__':
    TIMES = ['8am', '10am', '12 noon', '2pm', '4pm', '6pm',]
    temperatures =[]


    for reading_time in TIMES:

       reading = int(input(f'Enter {reading_time} reading: ')[:-1])
       temperatures.append(reading)

       max_temp = max(temperatures)
       min_temp = min(temperatures)
       avg_temp = mean(temperatures)
       print()
       print(f'maximum: {max_temp} C .')
       print(f'minimimum: {min_temp} C .')
       print(f'Average: {avg_temp} C.')