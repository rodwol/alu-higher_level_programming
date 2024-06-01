#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    console.log('1');
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const n = parseInt(process.argv[2]);
factorial(n);
