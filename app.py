import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

conversions = {
    "Length": {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084,
        "inches": 39.3701,
        "centimeters": 100
    },
    "Weight": {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274,
        "milligrams": 1000
    },
    "Temperature": {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x * 9/5) + 32,
        "Kelvin": lambda x: x + 273.15
    },
    "Volume": {
        "liters": 1,
        "milliliters": 1000,
        "gallons": 0.264172,
        "cubic meters": 0.001
    },
    "Speed": {
        "meters per second": 1,
        "kilometers per hour": 3.6,
        "miles per hour": 2.23694
    },
    "Pressure": {
        "pascals": 1,
        "atmospheres": 9.8692e-6,
        "bars": 1e-5,
        "psi": 0.000145038
    }
}

def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        return conversions[category][to_unit](conversions[category][from_unit](value))
    else:
        return value * conversions[category][to_unit] / conversions[category][from_unit]

st.title("🔄 Unit Converter")

st.sidebar.header("Conversion Settings")
category = st.sidebar.selectbox("Select category", list(conversions.keys()))

if category:
    units = list(conversions[category].keys())
    from_unit = st.sidebar.selectbox("From", units)
    to_unit = st.sidebar.selectbox("To", units)
    value = st.sidebar.number_input("Enter value", min_value=0.0, format="%.6f")
    
    if st.sidebar.button("Convert"):
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"✅ {value} {from_unit} is equal to {result:.6f} {to_unit}")
        st.sidebar.success(f"✅ {value} {from_unit} is equal to {result:.6f} {to_unit}")
    
        st.info("🔍 Additional Information")
        st.write(f"You converted {value} {from_unit} to {to_unit}, categorized under {category}.")
        st.balloons()
    
    # Placeholder for API-based currency conversion
    if category == "Currency":
        st.warning("⚠️ Live currency conversion requires an API integration.")
        st.info("💡 You can use `forex-python` library for this purpose.")
