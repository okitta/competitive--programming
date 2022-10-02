'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'gradingStudents' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY grades as parameter.
 */

function gradingStudents(grades) {
  return grades.map(grade => {
        
        if(grade < 38) {
            return grade;
        }
        
        const modOf5 = (grade % 5);

        const nextMultipleOf5 = (grade + 5) - modOf5;

        const differenceBetweenGradeAndNextMultipleOf5 = nextMultipleOf5 - grade;


        if(differenceBetweenGradeAndNextMultipleOf5 > 0 && differenceBetweenGradeAndNextMultipleOf5 < 3) {
            return nextMultipleOf5
        }
        
        return grade; 
    })

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const gradesCount = parseInt(readLine().trim(), 10);

    let grades = [];

    for (let i = 0; i < gradesCount; i++) {
        const gradesItem = parseInt(readLine().trim(), 10);
        grades.push(gradesItem);
    }

    const result = gradingStudents(grades);

    ws.write(result.join('\n') + '\n');

    ws.end();
}