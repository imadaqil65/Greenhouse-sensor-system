from cProfile import run
from xml.etree.ElementTree import Comment
from flask import Flask, render_template
import time, sys
from fhict_cb_01.CustomPymata4 import CustomPymata4
from datetime import datetime
import csv
board = CustomPymata4(baud_rate=57600, com_port = "COM7")


board.set_pin_mode_dht(12, sensor_type=11)
board.set_pin_mode_analog_input(2)

temperaturelist = [1]
humiditylist = [1]
lightlist = [1]

def temp():
    temperature=board.dht_read(12)[1]
    temperaturelist.append(temperature)
    return temperature

def humid():
    humidity= board.dht_read(12)[0]
    humiditylist.append(humidity)
    return humidity

def light():
    ldrVal= board.analog_read(2)[0]
    lightlist.append(ldrVal)
    return ldrVal

def date_time():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    return date_time

# def loop():
#     avgtem=sum(temperaturelist)/len(temperaturelist)
#     for i in range (len(temperaturelist)):
#         if i != 0:
#             True
#     mintem=min(temperaturelist)
#     maxtem=max(temperaturelist)
    
#     avghum=sum(humiditylist)/len(humiditylist)
#     minhum=min(humiditylist)
#     maxhum=max(humiditylist)

#     avglig=sum(lightlist)/len(lightlist)
#     minlig=min(lightlist)
#     maxlig=max(lightlist)



app = Flask(__name__)
@app.route('/')

@app.route("/index.html")
def index():
    global temperaturelist, humiditylist, lightlist

    return render_template("index.html", Title="Flask server", lig=light(), tem=temp(),  hum=humid(), date_time=date_time(),
                            avgtem=round(sum(temperaturelist)/(len(temperaturelist)-1)), mintem=min(i for i in temperaturelist if i > 1),
                            maxtem=max(temperaturelist), full='''temperaturelist''', avghum=round(sum(humiditylist)/(len(humiditylist)-1)),
                            minhum=min(i for i in humiditylist if i > 1), maxhum=max(humiditylist),
                            avglig=round(sum(lightlist)/(len(lightlist)-1)), minlig=min(i for i in lightlist if i > 1),
                            maxlig=max(lightlist))

# def index():
#     with open('stats.csv', 'r', newline='') as file: 
#         reader = csv.DictReader(file)
#         temperature=[]
#         header=next(reader)
#         for row in reader:
#             tempt=row['Temperature']
#             temperature.append(tempt)
#         avr=0
#         for i in range(len(temperature)):
#             avr+=float(temperature[i])
#         avr=avr/len(temperature)
#         return render_template("index2.html", maxtemp=max(temperature), mintemp=min(temperature),avrtemp=int(avr))


if __name__=="__main__":
    app.run() 
else: 
    print("Dont import me")
    
