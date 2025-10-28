import time
import serial
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


arduino = serial.Serial('COM8',9600)
time.sleep(2)

temperatures = []
humidities = []
times = []

plt.ion()
fig,ax = plt.subplots()
start_time = time.time()

while True:
    data = arduino.readline().decode('utf-8').strip()
    if data:
        try:
            temp,humid = map(float,data.split(','))
            current_time = start_time - time.time()
            temperatures.append(temp)
            humidities.append(humid)
            times.append(current_time)

            ax.clear()
            ax.plot(times,temperatures,lebel='Temp Plot')
            ax.plot(times,humidities,label = 'Humid Plot')
            ax.set_xlabel('Times')
            ax.set_ylabel('Values')
            ax.set_title('Real Time Temperatures and Humidities')
            plt.pause(0.1)

            print(f"Temp: {temp}°C | Humidity: {humid}%")
        except:
            pass