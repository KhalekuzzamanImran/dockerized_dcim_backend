
import django
import os
import sys
import time 


count = 0
rt_data = []
eny_data = []

current2 = os.path.dirname(os.path.realpath(__file__))
current1 = os.path.dirname(current2)
parent = os.path.dirname(current1)
sys.path.append(parent)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcim.settings')
django.setup()

from pop.models import POPDevice, POPDeviceState
from pop.CPM_RT_mixins import rt_mongo_create
from pop.CPM_DAY_DATA_mongo_mixins import day_data_mongo_create
from pop.CPM_ENY_FRZ_mongo_mixins import eny_frz_mongo_create
from pop.CPM_ENY_NOW_mongo_mixins import eny_now_mongo_create
from pop.thermohygrometer_modhumati_mixins import thermohygrometer_mongo_create

from paho.mqtt import client as mqtt_client
from decouple import config
import random
import json



broker_address = config('BROKER_ADDRESS')
port = int(config('BROKER_PORT'))
username = config('BROKER_USERNAME')
password = config('BROKER_PASSWORD')

# generate client ID with pub prefix randomly
client_id = f'mqtt-{random.randint(0, 100)}'

# MQRTT_RT_DATA normalize or remove redundency
def normalize_data(data):
    global count
    count += 1
    temp = data.copy()

    if (count == 1):
        del temp['time']
        del temp['isend']
        return temp

    if (count != 1):
        del temp['id']
        del temp['time']
        del temp['isend']
        return temp


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker_address, port)
    return client


def subscribe(client: mqtt_client):
    
    def on_message(client, userdata, msg):
        global count
        global rt_data, eny_data
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        try:
            data = msg.payload.decode()  # json formated data
            data = json.loads(data)      # python dictionary
                
           # DCIM
            if (msg.topic == 'MQTT_RT_DATA'):
                rt_data.append(normalize_data(data))
                    
                if(int(data['isend']) == 1):
                    count = 0
                    rt_mongo_create(rt_data, msg.topic)
                    rt_data = []

            elif (msg.topic == 'MQTT_DAY_DATA'):
                day_data_mongo_create(data, msg.topic)

            elif (msg.topic == 'MQTT_ENY_NOW'):
                eny_data.append(normalize_data(data))

                if(int(data['isend']) == 1):
                    count = 0
                    eny_now_mongo_create(eny_data, msg.topic)
                    eny_data = []
            
            elif (msg.topic == 'MQTT_ENY_FRZ'):
                eny_frz_mongo_create(data, msg.topic)

            elif (msg.topic == 'DCIM/ModhumatiBank/ENV_01'):
                thermohygrometer_mongo_create(data, msg.topic)
                

        except Exception as error:
            raise error
        
    for pop_device in POPDevice.objects.filter(is_active=True):
        for state in POPDeviceState.objects.filter(device_code=pop_device.id):
            if state.time_range == 'TODAY':
                print('===========================================================================', state.topic)
                client.subscribe(state.topic)

    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
    
