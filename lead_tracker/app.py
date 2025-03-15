import streamlit as st
from backend.lead_manager import get_all_leads, add_lead, edit_lead
from backend.lead_generator import generate_random_leads

st.title("🚀 Lead Tracker App")

# Sidebar menu
menu = st.sidebar.selectbox("Menu", ["View Leads", "Add Lead", "Edit Lead", "Generate Random Leads"])

# View Leads
if menu == "View Leads":
    st.header("📊 Active Leads")
    leads = get_all_leads()
    active_leads = [lead for lead in leads if lead["active"]]

    if not active_leads:
        st.warning("No active leads found.")
    else:
        for lead in sorted(active_leads, key=lambda x: x["score"], reverse=True):
            st.write(f"**{lead['name']}** - {lead['email']}")
            st.write(f"Lead Score: {lead['score']}")
            st.write(f"Expected Deal Value: ${lead['deal_value']}")
            st.markdown("---")

# Add a New Lead
elif menu == "Add Lead":
    st.header("➕ Add a New Lead")
    name = st.text_input("Lead Name")
    email = st.text_input("Email")
    score = st.slider("Lead Score", 0, 100, 50)
    deal_value = st.number_input("Deal Value ($)", min_value=0.0, format="%.2f")
    active = st.checkbox("Active")

    if st.button("Add Lead"):
        add_lead(name, email, score, deal_value, active)
        st.success(f"Lead '{name}' added successfully!")

# Edit a Lead's Score
elif menu == "Edit Lead":
    st.header("✏️ Edit Lead Score")
    leads = get_all_leads()
    lead_names = [lead["name"] for lead in leads]

    lead_to_edit = st.selectbox("Select Lead", lead_names)
    new_score = st.slider("New Score", 0, 100, 50)

    if st.button("Update Score"):
        success = edit_lead(lead_to_edit, new_score)
        if success:
            st.success(f"Updated '{lead_to_edit}' score to {new_score}!")
        else:
            st.error("Lead not found!")

# Generate Random Leads
elif menu == "Generate Random Leads":
    st.header("🎲 Generate Random Leads")
    num = st.number_input("How many leads?", min_value=1, max_value=10, step=1)

    if st.button("Generate"):
        generate_random_leads(num)
        st.success(f"Generated {num} random leads!")
