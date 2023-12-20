// This piece of code is part of the Advent of Coding 2023 puzzles
// look at https://adventofcode.com/2023/day/1 for more information about the task.

var fs = require("fs");
// Read file Calibrations.txt
let words = fs.readFileSync('./Calibrations.txt', 'utf-8');
console.log("this is the start of the list");
words = words.split ('\r\n');
let total = 0;
//A loop for checking each line of the input list.
for (let i = 0; i < words.length; i++){
    //removes all characters that are not numbers.
    words[i]= words[i].replace(/[^\d]/g, '');
        //selects the first and last number in the the new line
        var first = words[i][0];
        var last = words[i][words[i].length -1];
        //combines two strings into one string 
        var both = first + last;
        //converts the string into a number
        var numBoth = parseInt(both);
        // adds the total value to this strings number value.
        total = total + numBoth;
        // uncomment below if you want to see the progressive addition to the total value.
        //console.log(total);
}
//final result
console.log(total);