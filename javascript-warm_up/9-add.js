#!/usr/bin/node

function add (a, b) {
  if (isNaN(a, b)) {
    console.log(NaN);
    return NaN;
  }

  const add = a + b;
  console.log(add);
  return add;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

add(a, b);
