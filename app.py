import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

# read in data to display
data = pd.read_csv("data/test_data.csv")
predicted_labels = pd.read_csv("survival_labels.csv")
index = 0
patient = data.iloc[index]

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
    ax.axvline(x='60', color='red', linestyle='--', label='5-year mark')
    ax.set_title("Survival Curve for Patient in Test Dataset")
    ax.set_xlabel("Months")
    ax.set_ylabel("Survival Score")
    ax.set_ylim(0, 1.05)
    ax.grid(True)
    ax.legend()

    return fig

# sidebar
with st.sidebar:
    st.write("Choose example input")

    if st.button("Example 1 (not survivor)"):
        index = 15
        patient = data.iloc[index]

    if st.button("Example 2 (survivor)"):
        index = 1
        patient = data.iloc[index]

    if st.button("Random patient"):
        index = random.randint(0, 117)
        patient = data.iloc[index]

# main page
st.title("Breast Cancer DSS predictor")

# genetic data
# st.markdown("## Genetic Expression Data")
# # st.write(patient['ESR1','PGR','ERBB2','MKI67','PLAU','ELAVL1','EGFR','BTRC','FBXO6','SHMT2','KRAS','SRPK2','YWHAQ','PDHA1','EWSR1','ZDHHC17','ENO1','DBN1','PLK1','GSK3B'])

# clinical data
st.markdown("## Clinical Data")
age_input = st.number_input("Age:", value=patient['Age'], disabled=True)
menopausal_state_input = st.toggle("Menopausal State", value=patient['Menopausal State'], disabled=True)

st.markdown("### Tumour data")
tumour_size_input = st.number_input("Enter tumour size in cm:", key="tumour_size", value=patient['Size'], disabled=True)
neoplasm_histologic_grade_input = st.number_input("Neoplasm Histologic Grade", key="neoplasm", value=patient['Neoplasm Histologic Grade'], disabled=True)
cellularity_input = st.number_input("Cellularity", value=patient['Cellularity'], disabled=True)

st.markdown("### Therapies")
radio_therapy_input = st.toggle("Radio therapy", value=patient['Radio Therapy'], disabled=True)
chemotherapy_input = st.toggle("Chemotherapy", value=patient['Chemotherapy'], disabled=True)
hormone_therapy_input = st.toggle("Hormone Therapy", value=patient['Hormone Therapy'], disabled=True)

st.markdown("### Surgeries")
surgery_breast_conserving_input = st.toggle("Breast conserving surgery", value=patient['Surgery-breast conserving'], disabled=True)
surgery_mastectomy_input = st.toggle("Masectomy", value=patient['Surgery-mastectomy'], disabled=True)

st.pyplot(plot_surv_curve(index))
# st.write(f"Actual label: {patient['Label']}")
# predicted_row = predicted_labels.iloc[index]
# st.write(f"Predicted label: {predicted_row['Label']}")