function processData(input) {
    //Enter your code here
    //console.log(input.split('\n'));
    inputs = input.split('\n');
    const n = parseInt(inputs[0]);
    let phone_book = {};
    for (let i=1; i<=n; i++){
        phone_book[inputs[i].split(' ')[0]] = inputs[i].split(' ')[1];
    }
    //console.log(phone_book);
    for (let i=n+1; i<inputs.length; i++){
        if (phone_book[inputs[i]]){
            console.log(inputs[i] + '=' + phone_book[inputs[i]]);
        } else {
            console.log('Not found');
        }
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
