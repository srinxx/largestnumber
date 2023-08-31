import streamlit as st
num1  = st.number_input("select a number",min_value = 0)
num2  = st.number_input("select a number",min_value = 0)
num3  = st.number_input("select a number",min_value = 0)
if (num1 > num2) and (num1 > num3):
        largest_num = num1
elif (num2 > num1) and (num2 > num3):
        largest_num = num2
else:
        largest_num = num3
st.write("The largest of the 3 numbers is : ", largest_num)
if value1 > value2:
    st.write("value1 is greater")
else:
    st.write("value2 is greater")
