import random
import requests
from dotenv import load_dotenv
import os
import ast

# Load environment variables from .env file
load_dotenv()

# Clearstream API credentials
api_key = os.getenv("CLEARSTREAM_API_KEY")

# API URL for sending SMS
api_url = "https://api.getclearstream.com/v1/texts"

# Load players from the .env file (as a string and convert to a list)
players = ast.literal_eval(os.getenv("PLAYERS"))

# Load storyteller from the .env file
storyteller = {
    "name": os.getenv("STORYTELLER_NAME"),
    "phone": os.getenv("STORYTELLER_PHONE")
}

# Gameplay roles
roles = ["Werewolf 1", "Werewolf 2", "Detective", "Hunter", "Witch", "Doctor", "Mushroom"]

# Function to send SMS using Clearstream API
def send_sms(to, message):
    try:
        payload = {
            "to": to,
            "text_body": message
        }
        headers = {
            "X-Api-Key": api_key,
            "Content-Type": "application/json"
        }
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"Message sent to {to}: {response.json().get('message')}")
        else:
            print(f"Failed to send message to {to}: {response.text}")
    except Exception as e:
        print(f"Error sending message to {to}: {e}")

# Shuffle players and roles
random.shuffle(players)
random.shuffle(roles)

# Assign unique roles to shuffled players
assigned_roles = {}
for i, player in enumerate(players):
    if i < len(roles):
        role = roles[i]  # Assign unique role
    else:
        role = "Civilian"  # Assign "Civilian" role for extra players
    assigned_roles[player["name"]] = role
    # Notify player of their role
    send_sms(player["phone"], f"Hi {player['name']}, your role is: {role}.")

# Prepare storyteller summary
summary = "Game Roles Summary:\n"
for name, role in assigned_roles.items():
    summary += f"{name}: {role}\n"

# Notify storyteller of the role summary
send_sms(storyteller["phone"], summary)
print("Storyteller notified with role summary.")
