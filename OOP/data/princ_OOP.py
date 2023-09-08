import json

class CountryData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_data = self.read_data()
        self.country = self.file_data['Country']
        self.max_temp = self.file_data['max_temp']
        self.min_temp = self.file_data['min_temp']

    def read_data(self):
        with open(self.file_path, 'r') as country_file:
            return json.load(country_file)
    #Полиморфизм
    def comfort(self):
        return self.max_temp - self.min_temp > 10
    
#Наследование от базового класса
class CountryDataWithSunDays(CountryData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.sunny_days = self.file_data['sunny_days']

    # 1Полиморфизм
    def comfort(self):
        return self.max_temp - self.min_temp + self.sunny_days > 10


egypt = CountryData('egypt.json')
print(egypt.file_data)
print(egypt.max_temp)
sweden = CountryDataWithSunDays('sweden.json')
print(sweden.file_data)
print(sweden.max_temp)
print(sweden.sunny_days)
sweden.read_data()
print(egypt.comfort())
print(sweden.comfort())