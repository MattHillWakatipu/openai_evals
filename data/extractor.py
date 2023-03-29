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
            type_text = hero['Type Text']
            health = hero['Health']
            intelligence = hero['Intelligence']
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
        print(cards)
