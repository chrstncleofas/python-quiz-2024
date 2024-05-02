var rows = parseInt(prompt("Enter the number of rows for the left triangle: "));

for (var i = 1; i <= rows; i++) {
    var row = "";
    for (var j = 1; j <= i; j++) {
        row += "*";
    }
    console.log(row);
}
