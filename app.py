import streamlit as st
import pandas as pd

# read in data to display
data = pd.read_csv("data/test_data.csv")

# generate UI depending on selection
def input_page(generate=False):
    return

# generate report
def generate_report():

    report = f"""
    # You are going to die in 2 days :)
    """
    st.pyplot()

    return report

# sidebar
with st.sidebar:
    select_case = st.radio(
        "Choose input",
        ("Example 1", "Example 2", "Random Patient", "Custom")
    )

# change page depending on sidebar input
if select_case == "Example 1 (not survivor)":
    index = 0
elif select_case == "Example 2 (survivor)":
    index = 1
elif select_case == "Random Patient":
    index = 2
elif select_case == "Custom":
    index = 3

st.title("Breast Cancer DSS predictor")

# genetic data
st.markdown("## Genetic Expression Data")
st.text_input("Enter comma-separated expression values")

# ESR1 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key="ESR1")
# PGR = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=0)
# ERBB2 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=1)
# MKI67 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=2)
# PLAU = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=3)
# ELAVL1 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=4)
# EGFR = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=5)
# BTRC = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=6)
# FBXO6 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=7)
# SHMT2 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=8)
# KRAS = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=9)
# SRPK2 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=10)
# YWHAQ = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=11)
# PDHA1 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=12)
# EWSR1 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=13)
# ZDHHC17 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=14)
# ENO1 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=15)
# DBN1 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=16)
# PLK1 = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=17)
# GSK3B = st.number_input("Enter expression value:", min_value=0.0, max_value=1.0, step=0.1, key=18)


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
        report = generate_report()
        st.markdown(report)
    else:
        st.error("Please fill out the age field.")
