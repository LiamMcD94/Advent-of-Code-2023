/* read https://adventofcode.com/2023/day/1 for information about this puzzle, if you would like to use the code to solve the puzzle, just empty calibrations.txt 
   and copy and paste your own input data into it. */ 
var fs = require("fs");
 var i = 0;
 var result;
 var intResult;;

// PART 1
function part1(){
    //reads file and splits each line into it's own entry in the array called "line"
    let line = fs.readFileSync('./Calibrations.txt', 'utf-8').split ('\r\n');
    let total = 0;
    for (i = 0; i < line.length; i++){
        //removes all characters that are not numbers.
        line[i]= line[i].replace(/[^\d]/g, '');

        //combines two strings into one string 
        result = line[i][0] + line[i][line[i].length -1];

         //converts the string into a number
        intResult = parseInt(result);

        // adds the total value to this strings number value.
        total = total + intResult;
    };
    return total;
};

// PART 2
function part2(){
    let line = fs.readFileSync('./Calibrations.txt', 'utf-8').split ('\r\n');
    let total = 0;
    const numberConvert = {
        'one' : 'o1e',
        'two' : 't2wo',
        'three' : 'thr3e',
        'four' : 'fo4ur',
        'five' : 'f5ve',
        'six' : 's6x',
        'seven' : 'se7ven',
        'eight' : 'ei8ght',
        'nine' : 'ni9ne'
    };

    //A loop for checking each line of the input list.
    for (i = 0; i < line.length; i++){
        //removes all non numberic characters.
        line[i]= line[i].replace(/one|two|three|four|five|six|seven|eight|nine/g, m => numberConvert[m]);
        line[i]= line[i].replace(/one|two|three|four|five|six|seven|eight|nine/g, m => numberConvert[m]);
        //removes all characters that are not numbers.
        line[i]= line[i].replace(/[^\d]/g, '');
        //selects the first and last number in the the new line and combines the two strings into one string 
        result = line[i][0] + line[i][line[i].length -1];
        intResult = parseInt(result);
        // adds the total value to both number value.
        total = total + intResult;
    };

    return total;
}

//final result
console.log("Part 1 Result: ", part1());
console.log("Part 2 Result: ", part2());