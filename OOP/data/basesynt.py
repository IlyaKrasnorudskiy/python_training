import json

with open('egypt.json', 'r') as country_file:
    file_data = json.load(country_file)

print(file_data)
print(file_data['Country'])
print(file_data['max_temp'])