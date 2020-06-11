function processData(input) {
    //Enter your code here
    const values = input.split('\n');
    for (let i=1; i<values.length; i++){
        let value = +values[i];
        if (value === 1){
            console.log('Not prime');
            continue;
        }
        let prime = true;
        for (let j = 2; j <= Math.floor(Math.sqrt(value)); j++){
            if (+values[i] % j === 0) {
                prime = false;
                break;
            }
        }
        console.log(prime ? 'Prime' : 'Not prime');
    }
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
