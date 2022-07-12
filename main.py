macAdres = input("Wprowadz adres mac: ")

def converter(mac_adres):
    _newMacAdres = ""
    newMacAdres = []
    for index, char in enumerate(mac_adres):
        newMacAdres.append(index)
        if char == "-":
            newMacAdres[index] = ":"
        elif char.islower:
            newMacAdres[index] = char.upper()
        else:
            newMacAdres[index] = char
    for x in newMacAdres:
        _newMacAdres += x
    print(_newMacAdres)


converter(macAdres)

