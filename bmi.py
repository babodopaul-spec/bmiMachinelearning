import streamlit as st
import pandas as pd

st.title('Welcome to BMI Calculator')

weight=st.number_input('Enter your weight in kilograms (kg):', min_value=1.0, max_value=500.0, value=70.0, step=0.1)
status=st.radio('Select your height unit:', ('cm', 'm', 'ft'))

try:
    if status == 'cm':
        height = st.number_input('Cm')
        bmi = weight / ((height / 100) ** 2)

    elif status == 'm':
        height = st.number_input('m')
        bmi = weight / (height ** 2)

    else : 
        height = st.number_input('ft')
        bmi = weight / ((height * 0.3048) ** 2)
except : 
    print('Zero division error')


if (st.button('Calculate BMI')):
    st.write(f'Your BMI is: {bmi:.2f}')

    if bmi < 18.5:
        st.warning('You are underweight. Consider consulting a healthcare professional for advice on healthy weight gain.')
    elif 18.5 <= bmi < 24.9:
        st.success('You have a normal weight. Keep up the good work maintaining a healthy lifestyle!')
    elif 25 <= bmi < 29.9:
        st.warning('You are overweight. Consider adopting a healthier diet and increasing physical activity.')
    else:
        st.error('You are obese. It is advisable to consult a healthcare professional for guidance on weight management.')