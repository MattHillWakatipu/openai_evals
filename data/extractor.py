import json

# Open the file in write mode
with open('data.jsonl', 'w') as output_file:

    # Open hero file in read mode
    with open('wtr_cards.json', 'r') as card_file:

        # Read from JSON file
        cards = json.loads(card_file.read())

        # For each card construct an ideal answer string and save it to the JSONL file
        for card in cards:

            # Get card data
            name = card['Name']
            pitch = card['Pitch']
            cost = card['Cost']
            power = card['Power']
            defense = card['Defense']
            health = card['Health']
            intelligence = card['Intelligence']
            functional_text = card['Functional Text']
            type_text = card['Type Text']

            # TODO change to match in python 3.10
            # Construct an ideal string from the data
            if 'Equipment' in type_text:
                print(f'Eq:{name}')
                ideal = f"{name} is a '{type_text}' card from the 'Welcome to Rathe' set. It defends for {defense} and has the abilities; {functional_text}"
            elif 'Weapon' in type_text:
                print(f'Wpn:{name}')
                ideal = f"{name} is a '{type_text}' card from the 'Welcome to Rathe' set. It has {power} power and the abilities; {functional_text}"
            else:
                print(f'Crd:{name}')
                is_cycle = card['Is Cycle']

                # TODO make this a match statement
                if pitch == 1:
                    colour = 'Red'
                elif pitch == 2:
                    colour = 'Yellow'
                elif pitch == 3:
                    colour = 'Blue'

                if is_cycle == 1:
                    ideal = f"{name} ({colour}) is a '{type_text}' card from the 'Welcome to Rathe' set. It costs {cost}, pitches for {pitch}, defends for {defense}, has {power} power, and has the abilities; {functional_text}"
                else:
                    ideal = f"{name} is a '{type_text}' card from the 'Welcome to Rathe' set. It costs {cost}, pitches for {pitch}, defends for {defense}, has {power} power, and has the abilities; {functional_text}"

            # Create JSON line
            json_line = {"input": [{"role": "system", "content": f"In the card game Flesh and Blood, what does the card {name} do?"}], "ideal": ideal}

            # Write to JSONL file
            output_file.write(json.dumps(json_line))
            output_file.write('\n')
