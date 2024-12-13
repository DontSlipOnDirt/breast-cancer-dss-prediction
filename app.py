import streamlit as st

def generate_report():

    report = f"""
    # You are going to die in 2 days :)
    """
    return report

with st.sidebar:
    add_radio = st.radio(
        "Choose an example to view",
        ("Example 1 (not survivor)", "Example 2 (survivor)", "Random Patient")
    )

st.title("Breast Cancer DSS predictor")

st.markdown("## Genetic Expression Data")

# genetic data
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

st.markdown("## Clinical Data")

# clinical data
age = st.number_input("Enter age:", min_value=0, max_value=120, step=1)
menopausal_state = st.toggle("Menopausal State")
st.markdown("### Tumour data")
tumour_size = st.number_input("Enter tumour size in cm:", key = "tumour_size")
neoplasm_histologic_grade = st.selectbox("Neoplasm Histologic Grade", [1, 2, 3, 4])
cellularity = st.selectbox("Cellularity", ["Low","Medium", "High"])
st.markdown("### Therapies")
radio_therapy = st.toggle("Radio therapy")
chemotherapy = st.toggle("Chemotherapy")
hormone_therapy = st.toggle("Hormone Therapy")
st.markdown("### Surgeries")
surgery_breast_conserving = st.toggle("Breast conserving surgery")
surgery_mastectomy = st.toggle("Masectomy")

# Generate report button
if st.button("Generate Report"):
    if age > 0:
        report = generate_report()
        st.markdown(report)
    else:
        st.error("Please fill out the age field.")
