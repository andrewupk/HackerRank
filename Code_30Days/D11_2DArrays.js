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
}
*/


//function main() {
    let arr = Array(6);

    /*for (let i = 0; i < 6; i++) {
        arr[i] = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }*/
    arr = [ [ 1, 1, 1, 0, 0, 0 ],
		  [ 0, 1, 0, 0, 0, 0 ],
		  [ 1, 1, 1, 0, 0, 0 ],
		  [ 0, 0, 2, 4, 4, 0 ],
		  [ 0, 0, 0, 2, 0, 0 ],
		  [ 0, 0, 1, 2, 4, 0 ] ];

    console.log(arr);
    
    let hourglasses = [];
    
    for (let n=0; n<4; n++){
		for (let k=0; k<4; k++){
			let hourglas = [];
			for (let i=0; i<3; i++){
				hourglas.push([]);
				for (let j=0; j<3; j++){
					hourglas[i].push(arr[i+n][j+k]);
				}
			}
			hourglasses.push(hourglas);
		}
	}
	
	let sums = hourglasses.map((hourglass) => hourglasSum(hourglass));
	sums.sort((a, b) => b-a)
	console.log(sums);
	/*for (let i=0; i<hourglasses.length; i++){
		console.log(hourglasSum(hourglasses[i]));
	}*/
//}

function hourglasSum(hourglass){
	let res = 0;
	for (let i=0; i<3; i++){
		for (let j=0; j<3; j++){
			if (i === 1 && (j === 0 || j === 2)){
				continue;
			}
			res += hourglass[i][j];
		}
	}
	return res;
}
