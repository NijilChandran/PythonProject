from random import randint
from time import sleep
import streamlit as st

def read_sensor():
    '''
    place holder is a container that keeps refreshing
    without re-running the page
    Only one item per placeholder
    '''
    sleep(0.3)
    return randint(1,10)

place1 = st.empty()
place2 = st.empty()

data = []
for i in range(10):
    sensor = read_sensor()
    data.append(sensor)
    place1.write(f'Sensor data: {sensor}')
    place2.line_chart(data)

place1.write("Complete")