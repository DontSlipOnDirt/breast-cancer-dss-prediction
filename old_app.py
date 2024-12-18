import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

# read in data to display
data = pd.read_csv("data/test_data.csv")
predicted_label = pd.read_csv("survival_labels.csv")
index = 0

# plot survival curve
survival_probabilities = pd.read_csv("survival_probabilities.csv")

if 'Patient_ID' in survival_probabilities.columns:
    df = survival_probabilities.drop(columns=['Patient_ID'])
survival_probabilities_dict = {col: df[col].values for col in df.columns}

time_points = ['1', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100']

def plot_surv_curve(index):
    # Create a new figure and Axes for the subplot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Extract survival probabilities for the patient at the given index
    patient_probabilities = [survival_probabilities_dict[t][index] for t in time_points]

    # Plot on the subplot
    ax.plot(time_points, patient_probabilities, marker='o', label="Survival Probability")
    ax.axvline(x='60', color='red', linestyle='--', label='x = 60')
    ax.set_title("Survival Curve for Patient in Test Dataset")
    ax.set_xlabel("Months")
    ax.set_ylabel("Survival Score")
    ax.set_ylim(0, 1.05)
    ax.grid(True)
    ax.legend()

    return fig

# generate report
def generate_report():
    
    st.pyplot(plot_surv_curve(index))

# sidebar
with st.sidebar:
    select_case = st.radio(
        "Choose input",
        ("Example 1", "Example 2", "Random Patient")
    )

# change page depending on sidebar input
if select_case == "Example 1 (not survivor)":
    index = 15
    patient = data.iloc[index]

elif select_case == "Example 2 (survivor)":
    index = 1

elif select_case == "Random Patient":
    index = random.randint(0, 117)

st.title("Breast Cancer DSS predictor")

# genetic data
st.markdown("## Genetic Expression Data")
st.text_input("Enter comma-separated expression values")

# clinical data
st.markdown("## Clinical Data")
age_input = st.number_input("Enter age:", min_value=0, max_value=120, step=1)
menopausal_state_input = st.toggle("Menopausal State")

st.markdown("### Tumour data")
tumour_size_input = st.number_input("Enter tumour size in cm:", key="tumour_size")
neoplasm_histologic_grade_input = st.selectbox("Neoplasm Histologic Grade", [1, 2, 3, 4])
cellularity_input = st.selectbox("Cellularity", ["Low","Medium", "High"])

st.markdown("### Therapies")
radio_therapy_input = st.toggle("Radio therapy", value=1)
chemotherapy_input = st.toggle("Chemotherapy")
hormone_therapy_input = st.toggle("Hormone Therapy")

st.markdown("### Surgeries")
surgery_breast_conserving_input = st.toggle("Breast conserving surgery")
surgery_mastectomy_input = st.toggle("Masectomy")

# Generate report button
if st.button("Generate Report"):
    if age_input > 0:
        generate_report()
    else:
        st.error("Please fill out the age field.")
