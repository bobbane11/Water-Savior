from datetime import datetime
from threading import Timer
import requests
import yagmail
import json
import random

x=datetime.today()
y=x.replace(day=x.day+1, hour=0, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

yag = yagmail.SMTP('watersaviororiginal', 'WATER2018!')
quarterbody = "Warning! You are getting this email because you have used 75% of your water limit! Please be cautios of how you use your remaining water as it would be very unfortunate if you run out of water before the 30 - day period end.\nGood Luck,\nThe Water Saviors."

fullbody = "This is a very big problem, you have used up all your water before the 30 - day period ends. If you need water, you can pay for more at a higher rate. Next time, be sure to make sure you aren't overusing the water and follow these tips in order to not waste water:\n\n\t 1. Turn off the tap while brushing your teeth\n\n\t 2. Turn off the tap while washing your hands\n\n\t 3. Fix any potential leaks\n\n\t 4. Cut your time in the shower\n\n\t 5. Don't run the washing machine or dish washer unless it is fully loaded\n\nBetter luck next time,\nThe Water Saviors."

def update(incr):
    data = requests.get('http://localhost:5000/user/all')
    i=0
    jsn = json.loads(data.text)
    for cont in jsn:
        cont['gallons'] = int(cont['gallons']) + incr
        if cont['gallons'] >= int(cont['threshold']):
            yag.send(cont['email'], 'You have surpassed your water limit', "Dear " + cont['username'] + ',\n' + fullbody)
        elif cont['gallons'] >= 0.75*int(cont['threshold']):
            yag.send(cont['email'], 'You are close to reaching your water limit', "Dear " + cont['username'] + ',\n' + quarterbody)
        jsn[i].update(gallons=cont['gallons'])
    [requests.put('http://localhost:5000/user/' + info['username'], {'email': info['email'], 'gallons': info['gallons'], 'password': info['password'], 'threshold': info['threshold']}) for info in jsn]
    

while True:
    incr = input("how much should be added?")
    update(incr)
