import numpy as np
import pandas as pd
import streamlit as st
import pickle
from flask import Flask, request, jsonify, render_template

model = pickle.load(open("model.pkl", "rb"))

def welcome():
    return 'welcome all'




def prediction(Ge, Al, OH, H2O, F, OSDA, B, Na2O, Cl, Temperature, time, AR, Area, CN, rpm):
    prediction=model.predict([[Ge, Al, OH, H2O, F, OSDA, B, Na2O, Cl, Temperature, time, AR, Area, CN, rpm]])
    print(prediction)
    return prediction


def main():
    st.title("Prediction of framework density in zeolites")
    html_temp = """
    <div style ="background-color:yellow;padding:10px">
    <h1 style ="color:black;text-align:center; font-size: 10px;">

     (1) T=Si+Ge,

     (2) time=crystallization time in hour,

     (3) AR - if OSDA contains an aromatic ring, then assign 1; else assign zero, 

     (4) Area-Connolly molecular area of OSDA calculated from Chem3D,

     (5) Prediction- If output is : [0]- >12 [1] - <12</h1>
    </div>
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    Ge = st.text_input("Ge/Si", "Type Here")
    Al = st.text_input("Al/T", "Type Here")
    OH = st.text_input("OH/T", "Type Here")
    H2O = st.text_input("H2O/T", "Type Here")
    F = st.text_input("F/T", "Type Here")
    OSDA = st.text_input("OSDA/T", "Type Here")
    B = st.text_input("B/T", "Type Here")
    Na2O = st.text_input("Na2O/T", "Type Here")
    Cl = st.text_input("Cl/T", "Type Here")
    Temperature = st.text_input("Temperature", "Type Here")
    time = st.text_input("time", "Type Here")
    AR = st.text_input("AR", "Type Here")
    Area = st.text_input("Area", "Type Here")
    CN = st.text_input("C/N", "Type Here")
    rpm = st.text_input("rpm", "Type Here")
    result = ""
    if st.button("Predict"):
        result = prediction(Ge, Al, OH, H2O, F, OSDA, B, Na2O, Cl, Temperature, time, AR, Area, CN, rpm)
    st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()
