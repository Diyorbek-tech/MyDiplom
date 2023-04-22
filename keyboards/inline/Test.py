import json
with open("../../data/Morfologik_buttons.json") as json_file:
    json_data = json.load(json_file)
print(json_data['Ot'].keys())
print(json_data['Ot']['Atoqli ot'].keys())
print(json_data['Ot']['Atoqli ot']['Sodda'].keys())
print(json_data['Ot']['Atoqli ot']['Sodda']['Shaxs nomi'])
print(json_data['Ot']['Atoqli ot'])