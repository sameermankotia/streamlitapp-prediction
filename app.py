import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('inorganic_model.pkl', 'rb'))

# Define a function to make predictions
def predict_band(compound_name):
    # Convert the input to a feature vector
    input = np.array([compound_name]).reshape(1, -1)
    # Make a prediction
    prediction = model.predict(input)[0]
    return prediction

# Define the main function
def main():
    # Set up the app interface
    st.title("Inorganic Solid Band Prediction App")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Inorganic Solid Band Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    compound_name = st.text_input("Enter the name of the inorganic compound", "Type Here")
    if st.button("Predict"):
        output = predict_band(compound_name)
        st.success('The band gap of {} is predicted to be {}'.format(compound_name, output))

# Run the app
if __name__=='__main__':
    main()
