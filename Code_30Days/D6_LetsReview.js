function processData(input) {

    input_arr= input.split('\n');
    
    for (let k=1; k<input_arr.length; k++){
        let evens = '';
        let odds = '';
        for (let i=0; i<input_arr[k].length; i++){
            if (i % 2 === 0){
                evens += input_arr[k][i];
            } else {
                odds += input_arr[k][i];
            }
        }
        console.log(evens, odds);
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
