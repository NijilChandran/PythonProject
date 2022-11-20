import streamlit as st
import pandas as pd
from PIL import Image
import time

def print_hi(name):
    st.title(name)

@st.cache(max_entries=2,ttl=120)
def download_data(qtr):
    sales = [1000,2000,3000,4000]
    time.sleep(2)
    return sales[qtr-1]

def streamlitWebApp():
    st.title("Sales Report")
    q1_sales = {
        'January': 1000,
        'February': 1500,
        'March': 1800
    }
    q2_sales = {
        'April': 1800,
        'May': 2000,
        'June': 2100
    }
    q1_df = pd.DataFrame(q1_sales.items(), columns=['month', 'amount'])
    q2_df = pd.DataFrame(q2_sales.items(), columns=['month', 'amount'])

    section = st.sidebar.radio("Select type of Visualization",
                               ("Text","Charts","Widgets","More Widgets","Caching"))

    if section == 'Text':
        display_text(q1_df, q1_sales, q2_sales)
    elif section == 'Charts':
        display_charts(q1_df, q1_sales, q2_sales)
    elif section == 'Widgets':
        display_widgets(q1_df, q2_df)
    elif section == 'More Widgets':
        display_more_widgets()
    elif section == 'Caching':
        qtr = st.number_input('Which Quarter?',1,4)
        sales_amt = download_data(qtr)
        st.write(sales_amt)

def display_more_widgets():
    st.write(st.slider('quarters', 1, 4, (1, 2)))
    st.write(st.multiselect('Choose quarters', ['Q1', 'Q2', 'Q3', 'Q4']))
    st.write(st.number_input('Which quarters', 1, 4))


def display_widgets(q1_df, q2_df):
    if st.button('Show Q2 data'):
        st.table(q2_df)
    else:
        st.table(q1_df)
    if st.checkbox('Show Q2 data'):
        st.line_chart(q2_df['amount'].astype(str))
    else:
        st.line_chart(q1_df['amount'].astype(str))
    qtr = st.radio('Select a Quarter', ('Q1', 'Q2'))
    if qtr == 'Q2':
        st.area_chart(q2_df['amount'].astype(str))
    elif qtr == 'Q1':
        st.area_chart(q1_df['amount'].astype(str))
    sel_qtr = st.selectbox('Select a Quarter', ('Q1', 'Q2'))
    if sel_qtr == 'Q2':
        st.line_chart(q2_df['amount'].astype(str))
    elif sel_qtr == 'Q1':
        st.line_chart(q1_df['amount'].astype(str))


def display_charts(q1_df, q1_sales, q2_sales):
    # https://stackoverflow.com/questions/69578431/how-to-fix-streamlitapiexception-expected-bytes-got-a-int-object-conver
    st.line_chart(q1_df['amount'].astype(str))
    st.area_chart(q1_df['amount'].astype(str))
    st.bar_chart([q1_sales.values(), q2_sales.values()])
    st.image(image=Image.open("visualization.png"), caption="imageupload")


def display_text(q1_df, q1_sales, q2_sales):
    st.header('Q1 Results')
    st.write('First Quarter sales:')
    st.write(q1_sales)
    st.header('Q2 Results')
    'Second Quarter Sales:smile:'
    q2_sales
    'Display as a table '
    st.table(q1_df)
    'Display as a dataframe '
    st.dataframe(q1_df)


if __name__ == '__main__':
    txt = "Hello World!"
    #print_hi(txt)
    streamlitWebApp()
