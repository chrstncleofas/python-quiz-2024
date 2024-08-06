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

class Sample:

    def sampleFunction(fname: str, lname: str, age: str, address: str) -> None:
        print('Firstname: ', fname)
        print('Lastname: ', lname)
        print('Age: ', age)
        print('Address: ', address)

    for personDetails in listOfMember:
        fname = personDetails['Firstname'] 
        lname = personDetails['Lastname']
        age = personDetails['Age']
        address = personDetails['Address']

        print('-------')
        sampleFunction(
            fname=fname,
            lname=lname,
            age=age,
            address=address
        )
