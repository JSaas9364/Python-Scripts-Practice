import csv

filename = 'input1.csv'
data_dict = {}

with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 0: #ignore empty lines
            # Clean row
            row = row[0].strip().strip('{').strip('}').split(':')
            #print(row)
            if len(row) == 2: #proper k, v format
                key = row[0].strip("'").strip('"') # remove quotes
                value = row[1].strip()
                try:
                    #convert numbers to float/int
                    value = float(value) if "." in value else int(value)
                except ValueError:
                    pass # keep as string if conversion fails
                data_dict[key] = value
print(data_dict)   

new_data = [
    ["eggs", "cheese", "butter"],  # List
    {"yogurt": 1.99, "orange juice": 3.49, "cereal": 4.99},  # Dict
    "End of new data block"  # String
]
# Independent variables for each data type
list_data = ["eggs", "cheese", "butter"]  # Row 1 (List)
dict_data = {"yogurt": 1.99, "orange juice": 3.49, "cereal": 4.99}  # Row 2 (Dict)
string_data = "End of new data block"  # Row 3 (String)  

with open(filename, 'a') as f:
    writer = csv.writer(f)
#writerow for list data
    writer.writerow(list_data)
#writerows for dict data
    writer.writerows([dict_data.items()])
#writerow for string data
    writer.writerow([string_data])
