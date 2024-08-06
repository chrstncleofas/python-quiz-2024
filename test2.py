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

class ObjectClass:
    def information(fname: str, lname: str, age: str, address: str):
        print('Firstname: ', fname)
        print('Lastname: ', lname)
        print('Age: ', age)
        print('Address: ', address)

    for memberDetails in listOfMember:
        fname = memberDetails['Firstname']
        lname = memberDetails['Lastname']
        age = memberDetails['Age']
        address = memberDetails['Address']

        print('------------------------')
        information(
            fname=fname,
            lname=lname,
            age=age,
            address=address
        )

ObjectClass()