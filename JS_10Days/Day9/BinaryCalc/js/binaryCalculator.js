let resString = '';
let expression = '';

function addToExpression(sign){
    expression += sign;
    showInResDiv(expression);
}

/*function addZero(){
    expression += '0';
    showInResDiv(expression);
}

function addOne(){
    expression += '1';
    showInResDiv(expression);
}

function addAsterisk(){
    expression += '*';
    showInResDiv(expression);
}

function addSlash(){
    expression += '/';
    showInResDiv(expression);
}

function addPlus(){
    expression += '+';
    showInResDiv(expression);
}

function addMinus(){
    expression += '-';
    showInResDiv(expression);
}*/

function clearResult(){
    expression = '';
    resString = '';
    showInResDiv('');
}

function calculateResult(){
    const regex = /(?<operand1>\d+)(?<operator>\/|\+|\*|\-)(?<operand2>\d+)/g;
    let m;
    let operand1;
    let operand2;
    let operator;

    while ((m = regex.exec(expression)) !== null) {
        // This is necessary to avoid infinite loops with zero-width matches
        if (m.index === regex.lastIndex) {
            regex.lastIndex++;
        }
        
        operand1 = parseInt(m.groups.operand1, 2);
        operand2 = parseInt(m.groups.operand2, 2);
        operator = m.groups.operator;
    }
    
    switch (operator){
        case '+':
            resString = Number(operand1 + operand2).toString(2);
            break;
        case '-':
            resString = Number(operand1 - operand2).toString(2);
            break;
        case '*':
            resString = Number(operand1 * operand2).toString(2);
            break;
        case '/':
            resString = Math.floor(Number(operand1 / operand2)).toString(2);
            break;
    }
    
    expression = resString;
    showInResDiv(expression);
}

function showInResDiv(str){
    document.getElementById('res').innerHTML = str;
}
