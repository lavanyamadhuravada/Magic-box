#magic Square using javasacript
function magic_square(n) {
    var magicSquare = [];
    for (var i = 0; i < 3; i++) {
        var l = [];
        for (var j = 0; j < 3; j++) {
            l.push(0);
        }
        magicSquare.push(l);
    }
    var i = Math.floor(3 / 2);
    var j = 3 - 1;
    var num = 3 * 3;
    var count = 1;
    while (count <= num) {
        if (i == -1 && j == n) {
            j = 3 - 2;
            i = 0;
        } else {
            if (j == 3) {
                j = 0;
            }
            if (i < 0) {
                i = 3 - 1;
            }
        }
        if (magicSquare[i][j] != 0) {
            j = j - 2;
            i = i + 1;
            continue;
        } else {
            magicSquare[i][j] = count;
            count += 1;
        }
        i = i - 1;
        j = j + 1;
    }
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            console.log(magicSquare[i][j]);
        }
        console.log();
    }
    console.log("The sum of row/column/diagonal is: " + String(3 * (3 ** 2) / 2));
}
magic_square(3);
   
