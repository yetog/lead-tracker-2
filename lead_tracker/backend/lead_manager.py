from backend.data_handler import load_leads, save_leads

def get_all_leads():
    """Return all leads."""
    return load_leads()

def add_lead(name, email, score, deal_value, active):
    """Add a new lead to the list and save."""
    leads = load_leads()
    new_lead = {
        "name": name,
        "email": email,
        "score": score,
        "deal_value": deal_value,
        "active": active
    }
    leads.append(new_lead)
    save_leads(leads)

def edit_lead(name, new_score):
    """Edit a lead's score."""
    leads = load_leads()
    for lead in leads:
        if lead["name"].lower() == name.lower():
            lead["score"] = new_score
            save_leads(leads)
            return True
    return False  # Lead not found
