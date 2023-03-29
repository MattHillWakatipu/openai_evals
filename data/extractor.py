import json

# Open the file in write mode
with open('data.jsonl', 'w') as output_file:

    # Open hero file in read mode
    with open('wtr_cards_hero.json', 'r') as hero_file:

        # Read from JSON file
        heroes = json.loads(hero_file.read())
        print(heroes)

    # Open hero file in read mode
    with open('wtr_cards.json', 'r') as card_file:
        # Read from JSON file
        cards = json.loads(card_file.read())
        print(cards)
