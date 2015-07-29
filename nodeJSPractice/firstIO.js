var arguments = process.argv;

if (arguments.length < 2) return;

var fileSystem = require('fs');

var buffer = fileSystem.readFileSync(arguments[2]);

var stringRep = (buffer.toString());
//console.log(stringRep);
var splitRep = stringRep.split('\n');
//console.log(splitRep);
var numElem = splitRep.length - 1;

console.log(numElem);
