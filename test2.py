listOfMember = [
    {
        "Firstname": "Christian",
        "Lastname": "Cleofas",
        "Age": "25",
        "Address": "Iba Zambales",
    },
    {
        "Firstname": "Cyrus",
        "Lastname": "Leal",
        "Age": "22",
        "Address": "Iba Zambales",
    },
    {
        "Firstname": "Kian Adrienne",
        "Lastname": "Cleofas",
        "Age": "6",
        "Address": "Botolan Zambales",
    },
]

for memberDetails in listOfMember:
    fname = memberDetails['Firstname']
    lname = memberDetails['Lastname']
    age = memberDetails['Age']
    address = memberDetails['Address']

    print(fname, lname, age, address)
