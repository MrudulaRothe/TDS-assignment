import streamlit as st

st.title('Addition of 2 numbers')
a = st.number_input('Enter a number')
b = st.number_input('Enter another number')
result = a + b
st.write(a, ' + ', b , '= ', result)
