import streamlit as st
def convert_units(value,unit_from,unit_to):
    conversions ={
        "meter_kilometer" : 0.001,  #1meter = 0.001kilometer
        "kilometer_meter" : 1000,   #kilometer =1000 meter
        "gram_kilogram" : 0.001,
        "kilogram_gram" : 1000,
    }

    key = f"{unit_from}_{unit_to}"  #generate a unique key for the conversion

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "conversion not suported!"

st.title("Unit Converter app 🏪")
value = st.number_input("Enter the value to convert: ")
unit_from = st.selectbox("Select the unit to convert from:" , ["meter","kilometer","gram","kilogram"])
unit_to = st.selectbox("select the unit convert to : ", ["meter","kilometer","gram","kilogram"])

if st.button("Convert"):
    result = convert_units(value,unit_from,unit_to)
    st.success(f"The result of {value} {unit_from} is {result} {unit_to}🎉")

