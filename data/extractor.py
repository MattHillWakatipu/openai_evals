import csv
import json

# Open the file in write mode
with open('wtr_cards.json', 'r', encoding='utf8') as card_file, \
        open('embedding.csv', 'w', encoding='utf8') as embedding_file, \
        open('test.jsonl', 'w', encoding='utf8') as output_file:

    # Create csv writer and write header
    writer = csv.writer(embedding_file, delimiter=',', lineterminator='\n')
    writer.writerow(['name', 'description'])

    # Read from JSON file
    cards = json.loads(card_file.read())

    cards = cards[0:2]

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
            ideal = f"{name} is a '{type_text}' card from the 'Welcome to Rathe' set. " \
                    f"It defends for {defense} " \
                    f"and has the abilities; {functional_text}"
        elif 'Weapon' in type_text:
            ideal = f"{name} is a '{type_text}' card from the 'Welcome to Rathe' set. " \
                    f"It has {power} power " \
                    f"and the abilities; {functional_text}"
        else:

            # If it's a cycle we need to add the colour to the name string
            if card['Is Cycle'] == 1:

                # TODO make this a match statement
                if pitch == 1:
                    name += ' (Red)'
                elif pitch == 2:
                    name += ' (Yellow)'
                elif pitch == 3:
                    name += ' (Blue)'

            ideal = f"{name} is a '{type_text}' card from the 'Welcome to Rathe' set. " \
                    f"It costs {cost}, " \
                    f"pitches for {pitch}, " \
                    f"defends for {defense}, " \
                    f"has {power} power, " \
                    f"and has the abilities; {functional_text}"

        # Create JSON line
        json_line = {"input": [{"role": "system",
                                "content": f"In the card game Flesh and Blood, what does the card {name} do? "
                                           f"Make sure to include information when appropriate for the class, "
                                           f"card type, cost, pitch, defence, power, and any abilities."}],
                     "ideal": ideal}

        # Write to JSONL file
        output_file.write(json.dumps(json_line))
        output_file.write('\n')

        # Write to embedding CSV file
        embedding_row = [name, ideal]
        writer.writerow(embedding_row)
