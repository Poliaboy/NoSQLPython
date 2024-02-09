import json


def convert_arrays_to_string(dictionary):
    for key in dictionary.keys():
        if isinstance(dictionary[key], list):
            dictionary[key] = ','.join(map(str, dictionary[key]))
        elif isinstance(dictionary[key], dict):
            convert_arrays_to_string(dictionary[key])



# Open and read the JSON Lines file line by line
with open('/Users/alexs/Documents/NoSQL/Rendu_Cass/stocks.json', 'r') as f, open('/Users/alexs/Documents/NoSQL/Rendu_Cass/stocks_clean.json', 'w') as f_out:
    for line in f:
        data = json.loads(line)

        # Convert arrays to strings
        convert_arrays_to_string(data)

        # Flatten the JSON and remove nested keys
        flattened_data = {**data['_id'], **data['description'], **data}  # include all nested keys here
        keys_to_remove = ['_id', 'description']  # include all nested keys here
        for key in keys_to_remove:
            del flattened_data[key]

        keys = ", ".join(flattened_data.keys())
        values = ", ".join(['%s'] * len(flattened_data))
        print(len(keys))

        json.dump(flattened_data, f_out)
        f_out.write('\n')
