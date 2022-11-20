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
    q2_df = pd.DataFrame(q2_sales.items(), columns=['month', 'amount'])

    'Display as a table '
    st.table(q1_df)
    'Display as a dataframe '
    st.dataframe(q1_df)

    # https://stackoverflow.com/questions/69578431/how-to-fix-streamlitapiexception-expected-bytes-got-a-int-object-conver
    st.line_chart(q1_df['amount'].astype(str))
    st.area_chart(q1_df['amount'].astype(str))
    st.bar_chart([q1_sales.values(),q2_sales.values()])

    st.image(image=Image.open("flower_peacock.JPG"), caption="art")

    if st.button('Show Q2 data'):
        st.table(q2_df)
    else:
        st.table(q1_df)

    if st.checkbox('Show Q2 data'):
        st.line_chart(q2_df['amount'].astype(str))
    else:
        st.line_chart(q1_df['amount'].astype(str))

    qtr = st.radio('Select a Quarter', ('Q1','Q2'))
    if qtr == 'Q2':
        st.area_chart(q2_df['amount'].astype(str))
    elif qtr== 'Q1':
        st.area_chart(q1_df['amount'].astype(str))

    sel_qtr = st.selectbox('Select a Quarter', ('Q1','Q2'))
    if sel_qtr == 'Q2':
        st.line_chart(q2_df['amount'].astype(str))
    elif sel_qtr== 'Q1':
        st.line_chart(q1_df['amount'].astype(str))
        
if __name__ == '__main__':
    txt = "Hello World!"
    #print_hi(txt)
    streamlitWebApp()
