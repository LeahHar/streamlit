import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFFFFF;  /* Main background color updated to white */
        max-width: 1000px;
        margin: 20px auto;
        padding: 20px;
        border-radius: 10px;
    }
    h1.title {
        color: purple !important;  /* Purple title */
    }
    h2, h5 {
        color: #000000 !important;  /* Changed text color to black for better contrast */
    }
    input {
        background-color: #538ffc !important;  /* HEX color for input fields */
        color: #FFFFFF !important;
        padding: 10px;
    }
    label {
        font-size: 16px;
        color: red !important;
        margin-bottom: 5px;
    }
    div.stNumberInput, div.stTextInput {
        margin-bottom: 15px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown('<h1 class="title">SaaS ROI Calculator</h1>', unsafe_allow_html=True)

# Input Metrics
st.header("Enter Your Details")

employees = st.number_input("Number of employees/processes impacted", min_value=1, value=10)
time_per_task = st.number_input("Time spent per task (in hours)", min_value=0.1, value=2.0)
hourly_cost = st.number_input("Hourly cost of employees (£)", min_value=1.0, value=25.0)
current_tool_cost = st.number_input("Cost of current tools (£ per month)", min_value=0.0, value=500.0)
saas_product_cost = st.number_input("Subscription cost of SaaS product (£ per month)", min_value=0.0, value=300.0)

# ROI Calculations
st.header("Results")
time_saved_per_month = employees * time_per_task * 22
cost_saved = time_saved_per_month * hourly_cost
total_cost_savings = cost_saved - saas_product_cost
roi_percentage = ((cost_saved - total_cost_savings) / current_tool_cost) * 100 if current_tool_cost > 0 else 0

# Display Results
st.write(f"### Monthly Time Saved: {time_saved_per_month:.2f} hours")
st.write(f"### Monthly Net Savings: £{total_cost_savings:.2f}")
st.write(f"### ROI: {roi_percentage:.2f}%")
st.markdown('<h6>Adjust the inputs above to see how your ROI changes!</h6>', unsafe_allow_html=True)
