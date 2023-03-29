import json

# Open the file in write mode
with open('data.jsonl', 'w') as output_file:

    # Open hero file in read mode
    with open('wtr_cards_hero.json', 'r') as hero_file:

        # Read from JSON file
        heroes = json.loads(hero_file.read())
        print(heroes)

        # For each hero construct an ideal answer string and save it to the JSONL file
        for hero in heroes:

            # Get hero data
            name = hero['Name']
            health = hero['Health']
            intelligence = hero['Intelligence']
            type_text = hero['Type Text']
            functional_text = hero['Functional Text']

            # Construct an ideal string from the data
            ideal = f"{name} is a '{type_text}' card from the 'Welcome to Rathe' set. It has {health} Health, {intelligence} Intelligence and the abilities; {functional_text}"
            json_line = {"input": [{"role": "system", "content": f"In the card game Flesh and Blood, what does the card {name} do?"}], "ideal": ideal}

            # Write to JSONL file
            output_file.write(json.dumps(json_line))
            output_file.write('\n')

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
            type_text = card['Type Text']
            functional_text = card['Functional Text']

            # Add the colour for cycle cards
            # TODO

            # Construct an ideal string from the data
            ideal = f"{name} is a '{type_text}' card from the 'Welcome to Rathe' set. It costs {cost}, pitches for {pitch}, defends for {defense}, has {power} power, and has the abilities; {functional_text}"
            json_line = {"input": [{"role": "system", "content": f"In the card game Flesh and Blood, what does the card {name} do?"}], "ideal": ideal}

            # Write to JSONL file
            output_file.write(json.dumps(json_line))
            output_file.write('\n')