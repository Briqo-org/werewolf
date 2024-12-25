
# Werewolf Game Role Assignment Script

This script automates the role assignment for the Werewolf game. It sends SMS messages to players informing them of their roles and provides the storyteller with a summary of all assigned roles using the Clearstream API.

---

## Features

- Randomly shuffles players and roles to ensure fairness.
- Assigns unique roles to players, with remaining players assigned the role "Civilian".
- Sends SMS notifications to players with their assigned roles.
- Sends a summary of all assigned roles to the storyteller.

---

## Requirements

- Python 3.7+
- `requests` library
- `python-dotenv` library
- A Clearstream API key

---

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Briqo-org/werewolf
   cd werewolf
   ```

2. **Install dependencies**:
   Install the required Python libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**:
   Create a `.env` file in the project root directory and add the following:

   ```env
   CLEARSTREAM_API_KEY=your_api_key

   # Players list in the format: [{"name": "Name1", "phone": "+1234567890"}, ...]
   PLAYERS=[]

   # Storyteller details
   STORYTELLER_NAME=Game Master
   STORYTELLER_PHONE=+1234567890
   ```

4. **Run the script**:
   Execute the script to assign roles and send notifications:
   ```bash
   python werewolf.py
   ```

---

## How It Works

1. **Player Shuffling**:
   The script randomly shuffles the list of players and the list of roles for fair assignment.

2. **Role Assignment**:
   - Players are assigned unique roles from the shuffled roles list.
   - If there are more players than roles, the remaining players are assigned the role "Civilian".

3. **SMS Notifications**:
   - Each player receives an SMS with their assigned role.
   - The storyteller receives a summary of all assigned roles.

---

## Environment Variables

- **CLEARSTREAM_API_KEY**: Your Clearstream API key.
- **PLAYERS**: A JSON-like list of players with `name` and `phone` keys.
- **STORYTELLER_NAME**: The name of the storyteller.
- **STORYTELLER_PHONE**: The phone number of the storyteller.

---

## Example Output

### Player SMS:
```
Hi Name1, your role is: Werewolf 1.
```

### Storyteller SMS:
```
Game Roles Summary:
Name1: Werewolf 1
Name2: Witch
Name3: Doctor
...
```

---

## Dependencies

- `requests`
- `python-dotenv`

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
