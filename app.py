
import streamlit as st

# App title
st.title("Titanic Survival Predictor")
st.write("Enter passenger details to predict survival.")

# Passenger class dropdown
pclass = st.selectbox(
    "Passenger Class (Pclass)",
    [1, 2, 3]
)

# Sex dropdown
sex = st.selectbox(
    "Sex",
    ["male", "female"]
)

# Age slider
age = st.slider(
    "Age",
    min_value=1,
    max_value=100,
    value=25
)

# Prediction button
if st.button("Predict Survival"):

    # Sample prediction rules
    if sex == "female":
        prediction = "Survived"
    elif pclass == 1 and age < 18:
        prediction = "Survived"
    else:
        prediction = "Died"

    # Display result
    st.subheader("Prediction Result")

    if prediction == "Survived":
        st.success("Survived")
    else:
        st.error("Died")
