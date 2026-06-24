import datetime

food_donations = []

def create_donation(venue_name, food_type, neighborhood, hours_fresh):
    donation = {
        "id": len(food_donations) + 1,
        "venue": venue_name,
        "food": food_type,
        "location": neighborhood,
        "time_created": datetime.datetime.now(),
        "expiry_hours": hours_fresh,
        "status": "Available"
    }
    food_donations.append(donation)
    print(f"✔️ Listed: {food_type} at {venue_name}!")

def get_safe_local_matches(shelter_location):
    print(f"\n--- Matches for {shelter_location} ---")
    for food in food_donations:
        if food["location"] == shelter_location and food["status"] == "Available":
            print(f"🚀 FOUND: ID [{food['id']}]: {food['food']} is nearby!")

# --- PHONE LIVE TEST ---
# 1. This simulates a wedding hall listing food
create_donation("Khyber Wedding Hall", "Chicken Biryani (50 Servings)", "Peshawar", 4)

# 2. This simulates a shelter in Peshawar checking their screen
get_safe_local_matches("Peshawar")