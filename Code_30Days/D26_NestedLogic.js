function processData(input) {
    //Enter your code here
    const inputs = input.split('\n');
    const returned = new Date(+inputs[0].split(' ')[2], +inputs[0].split(' ')[1]-1, +inputs[0].split(' ')[0]);
    const planned = new Date(+inputs[1].split(' ')[2], +inputs[1].split(' ')[1]-1, +inputs[1].split(' ')[0]);
    if (returned.getTime() - planned.getTime() < 0){
        console.log(0);
        return;
    }
    if (returned.getFullYear() === planned.getFullYear()){
        if (returned.getMonth() === planned.getMonth()){
            console.log((returned.getDate() - planned.getDate())*15);
        } else {
            console.log((returned.getMonth() - planned.getMonth())*500);
        }
    } else {
        console.log(10000);
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
