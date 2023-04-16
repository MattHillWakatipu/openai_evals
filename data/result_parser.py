import csv
import json

# Open the file in write mode
with open('runs/wtr_full_run/results.csv', 'w', encoding='utf8', newline='') as output_file:

    # Set CSV field names and create csv writer
    fieldnames = ['prompt', 'sampled']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    # Open hero file in read mode
    with open('runs/wtr_full_run/results.jsonl', 'r', encoding='utf8') as input_file:

        for line in input_file:

            result = json.loads(line)
            # print(result)

            try:
                data = result['data']

                prompt = data['prompt'][0]['content']

                sampled = data['sampled']

                # Write row to file
                writer.writerow({'prompt': prompt, 'sampled': sampled})

            except KeyError:
                pass
