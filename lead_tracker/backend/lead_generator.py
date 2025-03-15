import random
from backend.data_handler import save_leads, load_leads

lead_names = ["CloudMasters", "DataSecure", "AI Hub", "WebXperts", "DevOps Co."]

def generate_random_leads(num):
    """Generate and add random leads."""
    leads = load_leads()
    for _ in range(num):
        lead = {
            "name": random.choice(lead_names),
            "email": f"{random.choice(lead_names).lower()}@example.com",
            "score": random.randint(50, 100),
            "deal_value": round(random.uniform(2000, 15000), 2),
            "active": random.choice([True, False])
        }
        leads.append(lead)
    save_leads(leads)
