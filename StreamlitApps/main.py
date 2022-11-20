import streamlit as st
import pandas as pd
from PIL import Image

def print_hi(name):
    st.title(name)


def streamlitWebApp():
    st.title("Sales Report")
    st.header('Q1 Results')
    q1_sales = {
        'January': 1000,
        'February': 1500,
        'March': 1800
    }
    st.write('First Quarter sales:')
    st.write(q1_sales)

    st.header('Q2 Results')
    q2_sales = {
        'April': 1800,
        'May': 2000,
        'June': 2100
    }

    'Second Quarter Sales:smile:'
    q2_sales

    q1_df = pd.DataFrame(q1_sales.items(), columns=['month', 'amount'])
    'Display as a table '
    st.table(q1_df)
    'Display as a dataframe '
    st.dataframe(q1_df)

    # https://stackoverflow.com/questions/69578431/how-to-fix-streamlitapiexception-expected-bytes-got-a-int-object-conver
    st.line_chart(q1_df['amount'].astype(str))
    st.area_chart(q1_df['amount'].astype(str))
    st.bar_chart([q1_sales.values(),q2_sales.values()])

    st.image(image=Image.open("flower_peacock.JPG"), caption="art")


if __name__ == '__main__':
    txt = "Hello World!"
    #print_hi(txt)
    streamlitWebApp()
