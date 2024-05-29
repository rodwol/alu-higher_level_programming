#!/usr/bin/node

const arg_1 = process.argv[2] || 'undefined';
const arg_2 = process.argv[3] || 'undefined';

if ( arg_1 && arg_2) {
	console.log(`${arg_1} ${arg_2}`);
} else if ( arg_1) {
	console.log(arg_1 + "is undefined");
} else 
	console.log("undefined is undefined");
