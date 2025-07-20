import streamlit as st

st.title("Body Mass Index (BMI) Estimator")

# Collecting input
weight = st.number_input("Enter your weight in kilograms (kg):")
height_feet = st.number_input("Height (Feet):")
height_inches = st.number_input("Height (Inches):", max_value=11)

if st.button("Compute BMI"):

    # Check weight and height are valid or not
    if weight <= 0 or (height_feet <= 0 and height_inches <= 0 ):
        st.warning("Please ensure you enter non-zero weight and height.")
        st.stop()

    total_height_inches = (height_feet * 12) + height_inches
    height_m = total_height_inches * 0.0254

    bmi_value = round(weight / (height_m ** 2), 2)
    st.success(f"Calculated BMI: {bmi_value}")

    if bmi_value < 16:
        st.error("Severely Underweight. Bhat khane gara.")
    elif bmi_value < 18.5:
        st.warning("Underweight. Ajhai khau bhat.")
    elif bmi_value < 25:
        st.success("Classification: Normal. Good job")
    elif bmi_value < 30:
        st.info("Classification: Overweight. Kudne gara")
    else:
        st.error("Classification: Obese. Kaam khau dherai kuda")
