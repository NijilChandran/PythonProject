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


def placeHolder():
    place1 = st.empty()
    place2 = st.empty()
    data = []
    for i in range(10):
        sensor = read_sensor()
        data.append(sensor)
        place1.write(f'Sensor data: {sensor}')
        place2.line_chart(data)
    place1.write("Complete Placeholder")

def container():
    place = st.container()
    st.write('Some more content')

    data = []
    for i in range(10):
        sensor = read_sensor()
        data.append(sensor)
        place.line_chart(data)
    place.write("Complete Container")

def columns():
    left_cols , right_cols = st.columns(2)

    data = []
    for i in range(10):
        sensor = read_sensor()
        data.append(sensor)

    left_cols.write("Data:")
    left_cols.write(data)
    right_cols.area_chart(data)

if __name__ == '__main__':
    #placeHolder()
    #container()
    columns()