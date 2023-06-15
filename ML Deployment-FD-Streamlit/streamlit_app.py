import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

def welcome():
    return 'welcome all'


def prediction(Al2O3, B2O3, BeO, Ga2O3, GeO2, Li2O, K2O, Na2O,
           Rb2O, Cs2O, SrO, H2O, F, OSDA1, OSDA2, OH,
           Area1, Area2, T, t, rpm):
    prediction = model.predict([[Al2O3, B2O3, BeO, Ga2O3, GeO2, Li2O, K2O, Na2O,
                                Rb2O, Cs2O, SrO, H2O, F, OSDA1, OSDA2, OH,
                                Area1, Area2, T, t, rpm]])
    print(prediction)
    return prediction


def main():
    st.title("Prediction of Framework Density in Zeolites")
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Framework Density Prediction </h1>
    </div>
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    Al = st.text_input("Al2O3/Si", "Type Here")
    B = st.text_input("B2O3/Si", "Type Here")
    Be = st.text_input("BeO/Si", "Type Here")
    Ga2O3 = st.text_input("Ga2O3/Si", "Type Here")
    GeO2 = st.text_input("GeO2/Si", "Type Here")
    Li2O = st.text_input("Li2O/Si", "Type Here")
    K2O = st.text_input("K2O/Si", "Type Here")
    Na2O = st.text_input("Na2O/Si", "Type Here")
    Rb2O = st.text_input("Rb2O/Si", "Type Here")
    Cs2O = st.text_input("Cs2O/Si", "Type Here")
    SrO = st.text_input("SrO/Si", "Type Here")
    H2O = st.text_input("H2O/Si", "Type Here")
    F = st.text_input("F/Si", "Type Here")
    OSDA1 = st.text_input("OSDA-1/Si", "Type Here")
    OSDA2 = st.text_input("OSDA-2/Si", "Type Here")
    OH = st.text_input("OH/Si", "Type Here")
    Area1 = st.text_input("Area-1", "Type Here")
    Area2 = st.text_input("Area-2", "Type Here")
    T = st.text_input("Temperature", "Type Here")
    t = st.text_input("Crystallization time", "Type Here")
    rpm = st.text_input("rpm", "Type Here")
    result = ""
    if st.button("Predict"):
        result = prediction(Al, B, Be, Ga2O3, GeO2, Li2O, K2O, Na2O, Rb2O,
                            Cs2O, SrO,  H2O, F, OSDA1, OSDA2, OH, Area1, Area2,
                            T, t,  rpm)
    st.success('The output is {}'.format(result))

if __name__ == '__main__':
        main()




