gamers = {"Давид": ["меч", "щит"], "Макс": ["кинжал", "верёвка"], "Маша": ["лук", "стрелы"]}
gamers["Макар"] = ["молот", "топор"]
gamers["Макс"].append("копьё")
del gamers["Давид"]
for name in gamers:
    print(name, "имеет в арсенале: ", *gamers[name])