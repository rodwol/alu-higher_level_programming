#!/usr/bin/node

function secondbiggestnum () {
  const num = process.argv.slice(2).map(Number);

  if (num.length < 2) {
    console.log(0);
    return 0;
  } else {
    const sortnums = num.sort((a, b) => b - a);
    console.log(sortnums[1]);
    return sortnums[1];
  }
}

secondbiggestnum();
