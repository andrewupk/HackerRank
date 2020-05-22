'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    const vowelsregex = /[aeiou]/gm;

    let m;

    while ((m = vowelsregex.exec(s)) !== null) {
        // This is necessary to avoid infinite loops with zero-width matches
        if (m.index === vowelsregex.lastIndex) {
            regex.lastIndex++;
        }
        
        // The result can be accessed through the `m`-variable.
        m.forEach((match, groupIndex) => {
            console.log(`${match}`);
        });
    }

    const consonantsregex = /[bcdfghjklmnpqrstvwxys]/gm;
    while ((m = consonantsregex.exec(s)) !== null) {
        // This is necessary to avoid infinite loops with zero-width matches
        if (m.index === consonantsregex.lastIndex) {
            regex.lastIndex++;
        }
        
        // The result can be accessed through the `m`-variable.
        m.forEach((match, groupIndex) => {
            console.log(`${match}`);
        });
    }
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
