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


function information(fname, lname, age, address) {
    console.log('Firstname: ', fname)
    console.log('Lastname: ', lname)
    console.log('Age: ', age)
    console.log('Address: ', address)
}

for (var i = 0; i < listOfMember.length; i++){
    var fname = listOfMember[i]['Firstname']
    var lname = listOfMember[i]['Lastname']
    var age = listOfMember[i]['Age']
    var address = listOfMember[i]['Address']

    console.log('-----------------------------')

    information(
        fname=fname,
        lname=lname,
        age=age,
        address=address
    )
}
