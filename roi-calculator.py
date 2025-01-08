import streamlit as st

st.markdown(
    """

    <style>

   .stApp {
    background-color: #0000FF; 
    width: 90%; 
    max-width: 1000px; 
    margin: 20px auto; 
    padding: 20px; 
    box-sizing: border-box; 
    border-radius: 10px; 
}

    h1.title {
        color: orange !important; 
    }
    h2, h5 {
        color: #FFFFFF !important; 
    }
    .stTextInput input, .stNumberInput input {

         # border: 2px solid orange !important;
        background-color: #1a1a1a !important;
         padding: 10px; 
        color: #000000 !important; 
        background-color: #FFFFFF !important; 
    }
    .stTextInput label, .stNumberInput label {
        font-size: 16px;
        color: red !important; 
        margin-bottom: 5px !important; 
    }
    div.stNumberInput, div.stTextInput {
        margin-bottom: 15px !important; 
    }
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the ROI Calculator
st.markdown('<h1 class="title">SaaS ROI Calculator</h1>', unsafe_allow_html=True)

# Input Metrics
st.header("Enter Your Details")

# Inputs where the label appears above the input field
st.markdown('<h5>Number of employees/processes impacted</h5>', unsafe_allow_html=True)
employees = st.number_input("Number of employees/processes impacted", min_value=1, value=10,
                            label_visibility="collapsed")

st.markdown('<h5>Time spent per task (in hours)</h5>', unsafe_allow_html=True)
time_per_task = st.number_input("Time spent per task (in hours)", min_value=0.1, value=2.0,
                                label_visibility="collapsed")

st.markdown('<h5>Hourly cost of employees (£)</h5>', unsafe_allow_html=True)
hourly_cost = st.number_input("Hourly cost of employees (£)", min_value=1.0, value=25.0, label_visibility="collapsed")

st.markdown('<h5>Cost of current tools (£ per month)</h5>', unsafe_allow_html=True)
current_tool_cost = st.number_input("Cost of current tools (£ per month)", min_value=0.0, value=500.0,
                                    label_visibility="collapsed")

st.markdown('<h5>Subscription cost of SaaS product (£ per month)</h5>', unsafe_allow_html=True)
saas_product_cost = st.number_input("Subscription cost of SaaS product (£ per month)", min_value=0.0, value=300.0,
                                    label_visibility="collapsed")

# ROI Calculations
st.header("Results")

# Calculate benefits
time_saved_per_month = employees * time_per_task * 22  # Assuming 22 working days per month
cost_saved = time_saved_per_month * hourly_cost
total_cost_savings = cost_saved - saas_product_cost  # Net savings after new SaaS cost

# Calculate ROI
total_cost = current_tool_cost + saas_product_cost
if total_cost > 0:
    roi_percentage = ((total_cost_savings - current_tool_cost) / current_tool_cost) * 100
else:
    roi_percentage = 0

# Display Results
st.write(f"### Monthly Time Saved: {time_saved_per_month:.2f} hours")
st.write(f"### Monthly Net Savings: £{total_cost_savings:.2f}")
st.write(f"### ROI: {roi_percentage:.2f}%")
st.markdown('<h6>Adjust the inputs above to see how your ROI changes!</h6>', unsafe_allow_html=True)



