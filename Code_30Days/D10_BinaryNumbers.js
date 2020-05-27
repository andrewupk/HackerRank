'use strict';

/*process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}*/



//function main() {
//    const n = parseInt(readLine(), 10);
	const n = 65535;
    const binary = n.toString(2);
    console.log(binary);
    let result = [];
    let current = 0;
    for (let i=0; i<binary.length - 1; i++){
		console.log(binary[i]);
        if (binary[i] === '1'){
            current++;
        } else {
            result.push(current);
            current = 0;
        }
        console.log(current);
    }
    if (binary[binary.length-1] === '1'){
		result.push(current+1);
	} else {
		result.push(current);
	}
    console.log(result);
	result.sort((a, b) => b - a);
	console.log(result[0]);
//}
